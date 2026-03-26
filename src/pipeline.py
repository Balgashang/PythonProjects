"""Pipeline orchestrator: wires all stages together.

Data flow:
1. Parse transcript → Corpus
2. Segment Chinese messages → SegmentedMessages
3. Build priors from unambiguous messages
4. Compute posteriors for ambiguous messages
5. Score entropy and classify confidence
6. Generate English translations
7. Format output
"""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path

import yaml

from src.models import (
    ConfidenceTier,
    Corpus,
    Language,
    Message,
    SegmentedMessage,
    Speaker,
    TranslatedMessage,
    TranslationCandidate,
)
from src.parser.transcript_parser import TranscriptParser
from src.linguistics.segmenter import create_segmenter
from src.linguistics.ambiguity_detector import AmbiguityPipeline
from src.bayesian.prior_builder import PriorBuilder
from src.bayesian.posterior_engine import PosteriorEngine, resolve_message_ambiguities
from src.bayesian.topic_model import build_topic_model
from src.entropy.scorer import score_message
from src.translation.rule_translator import batch_render


def load_config(config_path: str = "config.yaml") -> dict:
    """Load configuration from YAML file."""
    path = Path(config_path)
    if path.exists():
        with open(path) as f:
            return yaml.safe_load(f)
    return {}


class TranslationPipeline:
    """Orchestrates the full Bayesian-Shannon translation pipeline."""

    def __init__(self, config: dict | None = None):
        self.config = config or load_config()
        self._setup()

    def _setup(self):
        """Initialize pipeline components from config."""
        seg_config = self.config.get('segmenter', {})
        self.segmenter = create_segmenter(seg_config.get('backend', 'jieba'))
        self.ambiguity_pipeline = AmbiguityPipeline(self.segmenter)

        bay_config = self.config.get('bayesian', {})
        self.prior_builder = PriorBuilder(
            laplace_alpha=bay_config.get('laplace_alpha', 1.0)
        )

        ent_config = self.config.get('entropy', {})
        self.entropy_thresholds = {
            'high': ent_config.get('high_confidence', 0.3),
            'medium': ent_config.get('medium_confidence', 1.0),
            'low': ent_config.get('low_confidence', 2.0),
        }
        self.max_candidates = ent_config.get('max_candidates', 5)

        self.context_window_before = bay_config.get('context_window_before', 3)
        self.context_window_after = bay_config.get('context_window_after', 2)

    def run(self, transcript_text: str) -> list[TranslatedMessage]:
        """Run the full pipeline on a transcript.

        Args:
            transcript_text: Raw markdown transcript text.

        Returns:
            List of TranslatedMessages for all Chinese messages.
        """
        # Stage 1: Parse
        parser_config = self.config.get('parser', {})
        parser = TranscriptParser(
            cjk_threshold=parser_config.get('cjk_threshold', 0.3)
        )
        corpus = parser.parse(transcript_text)

        print(f"Parsed {len(corpus.messages)} messages "
              f"({len(corpus.mei_hui_messages)} Chinese, "
              f"{len(corpus.justin_messages)} English)")

        # Stage 2: Segment and analyze Chinese messages
        chinese_msgs = [
            m for m in corpus.mei_hui_messages
            if m.language == Language.ZH_TW and not m.is_media
        ]

        segmented = self.ambiguity_pipeline.analyze_batch(
            chinese_msgs, corpus.messages
        )
        print(f"Segmented {len(segmented)} Chinese messages")

        ambiguous_count = sum(1 for s in segmented if s.ambiguities)
        print(f"Found {ambiguous_count} messages with ambiguities")

        # Stage 3: Build priors from corpus
        priors = self.prior_builder.scan_corpus(segmented)
        print(f"Built priors from {self.prior_builder.total_messages_analyzed} messages")
        for name, prior in priors.items():
            print(f"  {name}: {prior.sample_count} observations, "
                  f"{len(prior.labels)} categories")

        # Stage 3b: Build topic model
        topic_config = self.config.get('bayesian', {})
        topic_model = build_topic_model(
            segmented,
            window_size=topic_config.get('topic_window', 10),
        )
        print(f"Topic model: {len(topic_model.segments)} segments identified")

        # Stage 4: Compute posteriors
        posterior_engine = PosteriorEngine(
            prior_builder=self.prior_builder,
            topic_model=topic_model,
            context_window_before=self.context_window_before,
            context_window_after=self.context_window_after,
        )
        posterior_engine.set_priors(priors)

        results: list[TranslatedMessage] = []

        for seg_msg in segmented:
            # Compute posteriors for ambiguities
            posterior_results = posterior_engine.compute_posterior(
                seg_msg, corpus.messages
            )

            # Generate translation candidates
            candidates = resolve_message_ambiguities(
                seg_msg, posterior_results, self.max_candidates
            )

            # Stage 5: Score entropy
            entropy, tier = score_message(
                candidates,
                self.entropy_thresholds['high'],
                self.entropy_thresholds['medium'],
                self.entropy_thresholds['low'],
            )

            # Stage 6: Generate English translations
            candidates = batch_render(seg_msg, candidates)

            # Try LLM enhancement if configured
            trans_config = self.config.get('translation', {})
            if trans_config.get('mode') == 'hybrid':
                try:
                    from src.translation.llm_translator import batch_translate_with_llm
                    candidates = batch_translate_with_llm(seg_msg, candidates)
                except Exception:
                    pass  # Fall back to rule-based

            primary = candidates[0].english_text if candidates else ""

            translated = TranslatedMessage(
                source=seg_msg,
                candidates=candidates,
                entropy=entropy,
                confidence_tier=tier,
                primary_translation=primary,
            )
            results.append(translated)

        # Summary
        tier_counts = {}
        for r in results:
            tier_counts[r.confidence_tier.value] = tier_counts.get(
                r.confidence_tier.value, 0
            ) + 1
        print(f"\nTranslation complete: {len(results)} messages")
        for tier, count in sorted(tier_counts.items()):
            print(f"  {tier}: {count}")

        return results


# =============================================================================
# Output formatters
# =============================================================================

def format_json(results: list[TranslatedMessage]) -> str:
    """Format results as JSON."""
    output = []
    for r in results:
        msg = {
            'index': r.source.message.index,
            'speaker': r.source.message.speaker.value,
            'date': r.source.message.date_str,
            'time': r.source.message.time_str,
            'chinese': r.source.message.raw_text,
            'primary_translation': r.primary_translation,
            'entropy': round(r.entropy, 4),
            'confidence': r.confidence_tier.value,
            'candidates': [
                {
                    'english': c.english_text,
                    'probability': round(c.probability, 4),
                    'resolutions': [
                        {
                            'type': res.ambiguity_class.value,
                            'span': res.span,
                            'chosen': res.chosen,
                            'probability': round(res.probability, 4),
                        }
                        for res in c.resolutions
                    ],
                }
                for c in r.candidates
            ],
            'ambiguities': [
                {
                    'type': a.ambiguity_class.value,
                    'span': a.span,
                    'candidates': a.candidates,
                }
                for a in r.source.ambiguities
            ],
        }
        output.append(msg)
    return json.dumps(output, ensure_ascii=False, indent=2)


def format_annotated_transcript(results: list[TranslatedMessage]) -> str:
    """Format results as a human-readable annotated transcript."""
    lines: list[str] = []
    current_date = None

    for r in results:
        # Date header
        if r.source.message.date_str != current_date:
            current_date = r.source.message.date_str
            lines.append(f"\n{'='*60}")
            lines.append(f"  {current_date}")
            lines.append(f"{'='*60}")

        # Time
        time_str = r.source.message.time_str or ""
        if time_str:
            time_str = f"[{time_str}] "

        # Confidence indicator
        conf_symbol = {
            ConfidenceTier.HIGH: 'H',
            ConfidenceTier.MEDIUM: 'M',
            ConfidenceTier.LOW: 'L',
            ConfidenceTier.REVIEW: '?',
        }[r.confidence_tier]

        entropy_str = f"H={r.entropy:.2f}"

        lines.append(f"\n{time_str}MEI HUI: {r.source.message.raw_text}")
        lines.append(f"  [{conf_symbol}|{entropy_str}] {r.primary_translation}")

        # Show alternatives for non-high-confidence translations
        if r.confidence_tier != ConfidenceTier.HIGH and len(r.candidates) > 1:
            lines.append("  Alternatives:")
            for i, c in enumerate(r.candidates[1:], 2):
                lines.append(f"    {i}. ({c.probability:.0%}) {c.english_text}")

        # Show ambiguity details for review-tier messages
        if r.confidence_tier == ConfidenceTier.REVIEW:
            lines.append("  AMBIGUITIES:")
            for a in r.source.ambiguities:
                lines.append(f"    {a.ambiguity_class.value}: '{a.span}'")
                for cand in a.candidates:
                    lines.append(f"      - {cand}")

    return '\n'.join(lines)
