"""Build Bayesian priors from the unambiguous portion of the corpus.

Three-tier prior strategy:
1. Corpus-derived: frequency statistics from unambiguous messages
2. Structural/linguistic: conditional probability tables from Mandarin grammar knowledge
3. Laplace-smoothed uniform: fallback for sparse data

The priors encode how Mei Hui uses language — her subject patterns,
particle preferences, and vocabulary tendencies.
"""

from __future__ import annotations

from collections import Counter
from typing import Optional

import numpy as np

from src.models import (
    AmbiguityClass,
    PriorDistribution,
    SegmentedMessage,
    Speaker,
    Token,
    Message,
)
from src.linguistics.prodrop_detector import PRONOUN_MAP


class PriorBuilder:
    """Builds prior distributions from corpus statistics."""

    def __init__(self, laplace_alpha: float = 1.0):
        self.alpha = laplace_alpha
        self.subject_counts: Counter[str] = Counter()
        self.particle_counts: Counter[str] = Counter()
        self.particle_context_counts: dict[str, Counter[str]] = {}
        self.word_freq: Counter[str] = Counter()
        self.total_messages_analyzed = 0

    def scan_corpus(
        self,
        segmented_messages: list[SegmentedMessage],
    ) -> dict[str, PriorDistribution]:
        """Scan all segmented messages to build prior distributions.

        Focuses on UNAMBIGUOUS messages to build reliable priors.

        Args:
            segmented_messages: All Chinese messages after segmentation.

        Returns:
            Dict of prior distributions keyed by name.
        """
        for seg_msg in segmented_messages:
            self.total_messages_analyzed += 1
            tokens = seg_msg.tokens

            # Count explicit subjects (unambiguous messages)
            if not seg_msg.has_dropped_subject:
                for tok in tokens:
                    if tok.surface in PRONOUN_MAP:
                        self.subject_counts[tok.surface] += 1

            # Count particle usage
            for tok in tokens:
                if tok.is_particle:
                    self.particle_counts[tok.surface] += 1

            # Word frequencies
            for tok in tokens:
                self.word_freq[tok.surface] += 1

        return self._build_distributions()

    def _build_distributions(self) -> dict[str, PriorDistribution]:
        """Convert raw counts into normalized probability distributions."""
        priors: dict[str, PriorDistribution] = {}

        # Subject referent prior
        priors['subject_referent'] = self._counts_to_prior(
            name='subject_referent',
            counts=self.subject_counts,
            default_labels=['我', '你', '我們', '她', '他們'],
        )

        # Particle usage prior
        priors['particle_usage'] = self._counts_to_prior(
            name='particle_usage',
            counts=self.particle_counts,
            default_labels=['吧', '啊', '嘛', '呢', '了', '喔', '啦'],
        )

        return priors

    def _counts_to_prior(
        self,
        name: str,
        counts: Counter[str],
        default_labels: list[str],
    ) -> PriorDistribution:
        """Convert a Counter into a Dirichlet-smoothed distribution.

        Uses Laplace smoothing (add alpha to all counts) to ensure
        no probability is zero, even for unseen labels.
        """
        # Merge default labels with any observed labels
        all_labels = list(dict.fromkeys(default_labels + list(counts.keys())))

        raw_counts = np.array(
            [counts.get(label, 0) + self.alpha for label in all_labels],
            dtype=np.float64,
        )
        probabilities = raw_counts / raw_counts.sum()

        return PriorDistribution(
            name=name,
            labels=all_labels,
            probabilities=probabilities.tolist(),
            sample_count=sum(counts.values()),
        )

    def get_subject_prior(self) -> PriorDistribution:
        """Get the subject referent prior distribution."""
        return self._counts_to_prior(
            name='subject_referent',
            counts=self.subject_counts,
            default_labels=['我', '你', '我們', '她', '他們'],
        )


# =============================================================================
# Structural priors: linguistic knowledge about Mandarin grammar
# =============================================================================

# Conditional probability tables: P(dropped_subject | context_feature)
# These encode well-known patterns in Mandarin pro-drop
STRUCTURAL_SUBJECT_PRIORS: dict[str, dict[str, float]] = {
    # When responding to a question about "you"
    'responding_to_you_question': {
        '我': 0.60,    # Most likely answering about self
        '你': 0.05,    # Echoing back is rare
        '我們': 0.20,  # "we" is possible in inclusive contexts
        '她': 0.05,
        '他們': 0.10,
    },
    # When initiating a new topic
    'topic_initiation': {
        '我': 0.40,
        '你': 0.20,
        '我們': 0.25,
        '她': 0.05,
        '他們': 0.10,
    },
    # When giving advice or instructions
    'giving_advice': {
        '我': 0.05,
        '你': 0.65,    # "You should..." with dropped subject
        '我們': 0.15,
        '她': 0.05,
        '他們': 0.10,
    },
    # Default fallback
    'default': {
        '我': 0.35,
        '你': 0.25,
        '我們': 0.20,
        '她': 0.10,
        '他們': 0.10,
    },
}


def get_structural_subject_prior(context_type: str = 'default') -> dict[str, float]:
    """Get structural prior for subject referent based on discourse context."""
    return STRUCTURAL_SUBJECT_PRIORS.get(
        context_type,
        STRUCTURAL_SUBJECT_PRIORS['default'],
    )
