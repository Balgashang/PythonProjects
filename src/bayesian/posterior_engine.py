"""Bayesian posterior computation for ambiguity resolution.

For each ambiguous message, computes:
    P(interpretation | evidence) ∝ P(evidence | interpretation) × P(interpretation)

Evidence sources:
- Local discourse context (high weight)
- Topic model assignment (medium weight)
- Speaker corpus-wide patterns (medium weight)
- Structural linguistic constraints (low weight)

Uses naive Bayes factorization across ambiguity axes to avoid
combinatorial explosion.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from src.models import (
    AmbiguityAnnotation,
    AmbiguityClass,
    AmbiguityResolution,
    ConfidenceTier,
    Message,
    PriorDistribution,
    SegmentedMessage,
    TranslationCandidate,
)
from .discourse_context import DiscourseContext, extract_context
from .prior_builder import PriorBuilder, get_structural_subject_prior
from .topic_model import TopicModel


# Evidence weights for different sources
EVIDENCE_WEIGHTS = {
    'local_context': 0.40,
    'topic': 0.20,
    'speaker_patterns': 0.25,
    'structural': 0.15,
}


@dataclass
class PosteriorResult:
    """Result of posterior computation for one ambiguity."""
    ambiguity: AmbiguityAnnotation
    posterior: list[tuple[str, float]]  # (candidate, probability) sorted desc
    evidence_breakdown: dict[str, list[float]] = field(default_factory=dict)


class PosteriorEngine:
    """Computes Bayesian posteriors for ambiguous messages."""

    def __init__(
        self,
        prior_builder: PriorBuilder,
        topic_model: TopicModel | None = None,
        context_window_before: int = 3,
        context_window_after: int = 2,
    ):
        self.prior_builder = prior_builder
        self.topic_model = topic_model
        self.window_before = context_window_before
        self.window_after = context_window_after
        self._priors: dict[str, PriorDistribution] = {}

    def set_priors(self, priors: dict[str, PriorDistribution]):
        """Set the pre-computed prior distributions."""
        self._priors = priors

    def compute_posterior(
        self,
        seg_msg: SegmentedMessage,
        all_messages: list[Message],
    ) -> list[PosteriorResult]:
        """Compute posteriors for all ambiguities in a message.

        Args:
            seg_msg: The segmented message with detected ambiguities.
            all_messages: Full message list for context extraction.

        Returns:
            List of PosteriorResults, one per ambiguity.
        """
        if not seg_msg.ambiguities:
            return []

        # Extract discourse context
        msg_idx = seg_msg.message.index
        ctx = extract_context(
            target_index=msg_idx,
            all_messages=all_messages,
            window_before=self.window_before,
            window_after=self.window_after,
        )

        results = []
        for ambiguity in seg_msg.ambiguities:
            result = self._resolve_ambiguity(ambiguity, ctx, seg_msg)
            results.append(result)

        return results

    def _resolve_ambiguity(
        self,
        ambiguity: AmbiguityAnnotation,
        ctx: DiscourseContext,
        seg_msg: SegmentedMessage,
    ) -> PosteriorResult:
        """Resolve a single ambiguity using Bayesian inference."""
        candidates = ambiguity.candidates
        n = len(candidates)

        if n == 0:
            return PosteriorResult(ambiguity=ambiguity, posterior=[])

        # 1. Get prior distribution
        prior = self._get_prior(ambiguity, n)

        # 2. Compute likelihood from each evidence source
        local_likelihood = self._local_context_likelihood(ambiguity, ctx, n)
        topic_likelihood = self._topic_likelihood(ambiguity, seg_msg, n)
        speaker_likelihood = self._speaker_pattern_likelihood(ambiguity, n)
        structural_likelihood = self._structural_likelihood(ambiguity, ctx, n)

        # 3. Weighted combination of likelihoods (log-space for stability)
        log_posterior = np.log(prior + 1e-10)
        log_posterior += EVIDENCE_WEIGHTS['local_context'] * np.log(local_likelihood + 1e-10)
        log_posterior += EVIDENCE_WEIGHTS['topic'] * np.log(topic_likelihood + 1e-10)
        log_posterior += EVIDENCE_WEIGHTS['speaker_patterns'] * np.log(speaker_likelihood + 1e-10)
        log_posterior += EVIDENCE_WEIGHTS['structural'] * np.log(structural_likelihood + 1e-10)

        # 4. Normalize to get posterior
        log_posterior -= np.max(log_posterior)  # for numerical stability
        posterior = np.exp(log_posterior)
        posterior /= posterior.sum()

        # Sort by probability descending
        ranked = sorted(
            zip(candidates, posterior.tolist()),
            key=lambda x: x[1],
            reverse=True,
        )

        return PosteriorResult(
            ambiguity=ambiguity,
            posterior=ranked,
            evidence_breakdown={
                'prior': prior.tolist(),
                'local_context': local_likelihood.tolist(),
                'topic': topic_likelihood.tolist(),
                'speaker_patterns': speaker_likelihood.tolist(),
                'structural': structural_likelihood.tolist(),
            },
        )

    def _get_prior(
        self, ambiguity: AmbiguityAnnotation, n: int
    ) -> np.ndarray:
        """Get the prior distribution for an ambiguity."""
        if ambiguity.ambiguity_class == AmbiguityClass.PRODROP:
            prior_dist = self._priors.get('subject_referent')
            if prior_dist:
                # Map prior labels to candidate order
                prior_map = dict(zip(prior_dist.labels, prior_dist.probabilities))
                return np.array([
                    prior_map.get(c.split(':')[0].strip(), 1.0 / n)
                    for c in ambiguity.candidates
                ])
        # Uniform prior for other ambiguity types or when no corpus prior exists
        return np.ones(n) / n

    def _local_context_likelihood(
        self, ambiguity: AmbiguityAnnotation, ctx: DiscourseContext, n: int
    ) -> np.ndarray:
        """Compute likelihood from local discourse context."""
        likelihood = np.ones(n)

        if ambiguity.ambiguity_class == AmbiguityClass.PRODROP:
            # If Justin asked a question about "you", boost "I" (answering about self)
            if ctx.question_about_you:
                for i, candidate in enumerate(ambiguity.candidates):
                    if '我' in candidate:
                        likelihood[i] *= 2.5
                    elif '你' in candidate:
                        likelihood[i] *= 0.3

            # If this is advice-giving, boost "you"
            if ctx.context_type == 'giving_advice':
                for i, candidate in enumerate(ambiguity.candidates):
                    if '你' in candidate:
                        likelihood[i] *= 2.5
                    elif '我' in candidate:
                        likelihood[i] *= 0.8

        elif ambiguity.ambiguity_class == AmbiguityClass.PARTICLE:
            # If preceded by a question, particle likely marks response type
            if ctx.is_response_to_question:
                for i, candidate in enumerate(ambiguity.candidates):
                    if 'acknowledgment' in candidate.lower() or 'agreement' in candidate.lower():
                        likelihood[i] *= 1.8

        # Normalize
        total = likelihood.sum()
        if total > 0:
            likelihood /= total
        return likelihood

    def _topic_likelihood(
        self, ambiguity: AmbiguityAnnotation, seg_msg: SegmentedMessage, n: int
    ) -> np.ndarray:
        """Compute likelihood from topic model."""
        if self.topic_model is None:
            return np.ones(n) / n

        topic = self.topic_model.get_topic_at(seg_msg.message.index)
        if topic is None:
            return np.ones(n) / n

        likelihood = np.ones(n)

        # Topic keywords can influence polysemy resolution
        if ambiguity.ambiguity_class == AmbiguityClass.POLYSEMY:
            for i, candidate in enumerate(ambiguity.candidates):
                # Check if candidate meaning aligns with topic
                candidate_lower = candidate.lower()
                for kw in topic.topic_keywords:
                    if kw in candidate_lower:
                        likelihood[i] *= 1.5

        total = likelihood.sum()
        if total > 0:
            likelihood /= total
        return likelihood

    def _speaker_pattern_likelihood(
        self, ambiguity: AmbiguityAnnotation, n: int
    ) -> np.ndarray:
        """Compute likelihood from Mei Hui's corpus-wide usage patterns."""
        # For particles, check her typical usage
        if ambiguity.ambiguity_class == AmbiguityClass.PARTICLE:
            particle_prior = self._priors.get('particle_usage')
            if particle_prior and ambiguity.span in particle_prior.labels:
                # Her frequency of this particle relative to others
                # indicates her pragmatic preference
                idx = particle_prior.labels.index(ambiguity.span)
                freq = particle_prior.probabilities[idx]
                # Higher frequency particles tend toward their most common use
                likelihood = np.ones(n)
                # Boost the first (most common) interpretation proportionally
                likelihood[0] *= 1.0 + freq * 2.0
                total = likelihood.sum()
                if total > 0:
                    likelihood /= total
                return likelihood

        return np.ones(n) / n

    def _structural_likelihood(
        self, ambiguity: AmbiguityAnnotation, ctx: DiscourseContext, n: int
    ) -> np.ndarray:
        """Compute likelihood from structural linguistic knowledge."""
        if ambiguity.ambiguity_class == AmbiguityClass.PRODROP:
            structural = get_structural_subject_prior(ctx.context_type)
            return np.array([
                structural.get(c.split(':')[0].strip(), 1.0 / n)
                for c in ambiguity.candidates
            ])

        return np.ones(n) / n


def resolve_message_ambiguities(
    seg_msg: SegmentedMessage,
    posterior_results: list[PosteriorResult],
    max_candidates: int = 5,
) -> list[TranslationCandidate]:
    """Convert posterior results into ranked TranslationCandidates.

    For messages with multiple independent ambiguities, we take the
    top resolution for each axis (naive Bayes factorization) rather
    than enumerating all combinations.

    Args:
        seg_msg: The segmented message.
        posterior_results: Posterior results for each ambiguity.
        max_candidates: Maximum candidates to return.

    Returns:
        List of TranslationCandidates with probability and resolutions.
    """
    if not posterior_results:
        # No ambiguity — single interpretation
        return [TranslationCandidate(
            english_text="",  # filled by translator
            probability=1.0,
            resolutions=[],
        )]

    # For each ambiguity axis, take the top-k resolutions
    axes_top_k: list[list[tuple[str, float]]] = []
    for result in posterior_results:
        axes_top_k.append(result.posterior[:max_candidates])

    # Generate candidates from top resolutions
    # Simple approach: take the top resolution for each axis, then permute
    candidates: list[TranslationCandidate] = []

    if len(axes_top_k) == 1:
        # Single ambiguity axis — each resolution is a candidate
        for chosen, prob in axes_top_k[0]:
            resolutions = [AmbiguityResolution(
                ambiguity_class=posterior_results[0].ambiguity.ambiguity_class,
                span=posterior_results[0].ambiguity.span,
                chosen=chosen,
                probability=prob,
            )]
            candidates.append(TranslationCandidate(
                english_text="",
                probability=prob,
                resolutions=resolutions,
            ))
    else:
        # Multiple axes — take top from each, combine with joint probability
        # We generate candidates by varying one axis at a time from the top
        base_resolutions = []
        base_prob = 1.0
        for i, result in enumerate(posterior_results):
            top_chosen, top_prob = axes_top_k[i][0]
            base_resolutions.append(AmbiguityResolution(
                ambiguity_class=result.ambiguity.ambiguity_class,
                span=result.ambiguity.span,
                chosen=top_chosen,
                probability=top_prob,
            ))
            base_prob *= top_prob

        # Base candidate (all top resolutions)
        candidates.append(TranslationCandidate(
            english_text="",
            probability=base_prob,
            resolutions=list(base_resolutions),
        ))

        # Vary one axis at a time for alternative candidates
        for i, result in enumerate(posterior_results):
            for j, (chosen, prob) in enumerate(axes_top_k[i][1:], 1):
                alt_resolutions = list(base_resolutions)
                alt_resolutions[i] = AmbiguityResolution(
                    ambiguity_class=result.ambiguity.ambiguity_class,
                    span=result.ambiguity.span,
                    chosen=chosen,
                    probability=prob,
                )
                alt_prob = base_prob / base_resolutions[i].probability * prob
                candidates.append(TranslationCandidate(
                    english_text="",
                    probability=alt_prob,
                    resolutions=alt_resolutions,
                ))

    # Sort by probability and trim
    candidates.sort(key=lambda c: c.probability, reverse=True)

    # Normalize probabilities
    total = sum(c.probability for c in candidates)
    if total > 0:
        for c in candidates:
            c.probability /= total

    return candidates[:max_candidates]
