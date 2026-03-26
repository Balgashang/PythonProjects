"""Shannon entropy computation and confidence tier classification.

Shannon entropy H measures the uncertainty in a probability distribution.
For translation candidates:
- Low H = one interpretation dominates → high confidence
- High H = multiple viable interpretations → needs human review

H = -Σ p_i × log₂(p_i) for all candidates i where p_i > 0

Maximum possible entropy for n candidates = log₂(n) (uniform distribution).
"""

from __future__ import annotations

from math import log2

import numpy as np

from src.models import ConfidenceTier, TranslatedMessage, TranslationCandidate


def shannon_entropy(probabilities: list[float]) -> float:
    """Compute Shannon entropy of a discrete probability distribution.

    Args:
        probabilities: List of probabilities (must sum to ~1.0).

    Returns:
        Entropy in bits (base 2).
    """
    h = 0.0
    for p in probabilities:
        if p > 0:
            h -= p * log2(p)
    return h


def max_entropy(n_candidates: int) -> float:
    """Maximum possible entropy for n candidates (uniform distribution)."""
    if n_candidates <= 1:
        return 0.0
    return log2(n_candidates)


def normalized_entropy(probabilities: list[float]) -> float:
    """Entropy normalized to [0, 1] range.

    0 = perfectly certain (one candidate has probability 1)
    1 = maximally uncertain (uniform distribution)
    """
    n = len(probabilities)
    if n <= 1:
        return 0.0
    h = shannon_entropy(probabilities)
    h_max = max_entropy(n)
    if h_max == 0:
        return 0.0
    return h / h_max


def classify_confidence(
    entropy: float,
    high_threshold: float = 0.3,
    medium_threshold: float = 1.0,
    low_threshold: float = 2.0,
) -> ConfidenceTier:
    """Classify entropy value into a confidence tier.

    Args:
        entropy: Shannon entropy in bits.
        high_threshold: Below this = high confidence.
        medium_threshold: Below this = medium confidence.
        low_threshold: Below this = low confidence, above = review.

    Returns:
        ConfidenceTier enum value.
    """
    if entropy < high_threshold:
        return ConfidenceTier.HIGH
    elif entropy < medium_threshold:
        return ConfidenceTier.MEDIUM
    elif entropy < low_threshold:
        return ConfidenceTier.LOW
    else:
        return ConfidenceTier.REVIEW


def score_message(
    candidates: list[TranslationCandidate],
    high_threshold: float = 0.3,
    medium_threshold: float = 1.0,
    low_threshold: float = 2.0,
) -> tuple[float, ConfidenceTier]:
    """Compute entropy and confidence tier for a set of translation candidates.

    Args:
        candidates: Ranked translation candidates with probabilities.
        high_threshold: Entropy threshold for high confidence.
        medium_threshold: Entropy threshold for medium confidence.
        low_threshold: Entropy threshold for low confidence.

    Returns:
        Tuple of (entropy, confidence_tier).
    """
    if not candidates:
        return 0.0, ConfidenceTier.HIGH

    probabilities = [c.probability for c in candidates]

    # Ensure probabilities are normalized
    total = sum(probabilities)
    if total > 0 and abs(total - 1.0) > 0.01:
        probabilities = [p / total for p in probabilities]

    entropy = shannon_entropy(probabilities)
    tier = classify_confidence(entropy, high_threshold, medium_threshold, low_threshold)

    return entropy, tier
