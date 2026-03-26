"""Combine ambiguity axes into candidate interpretations.

Each message may have multiple independent ambiguities (dropped subject,
polysemous word, particle). This module combines them into a tractable
set of candidate interpretations, using naive independence to avoid
combinatorial explosion.
"""

from __future__ import annotations

from itertools import product
from typing import Optional

from src.models import (
    AmbiguityAnnotation,
    AmbiguityClass,
    Message,
    SegmentedMessage,
    Speaker,
    Token,
)
from .prodrop_detector import detect_prodrop
from .particle_analyzer import analyze_particles
from .polysemy_detector import detect_polysemy


def decompose_message(
    tokens: list[Token],
    message: Message,
    preceding_message: Optional[Message] = None,
) -> SegmentedMessage:
    """Run all ambiguity detectors on a tokenized message.

    Args:
        tokens: Segmented tokens from the segmenter.
        message: The original Message object.
        preceding_message: The message immediately before this one.

    Returns:
        SegmentedMessage with all ambiguities annotated.
    """
    ambiguities: list[AmbiguityAnnotation] = []

    # 1. Pro-drop detection
    prodrop = detect_prodrop(tokens, preceding_message)
    has_dropped_subject = prodrop is not None
    subject_candidates: list[tuple[str, float]] = []
    if prodrop:
        ambiguities.append(prodrop)
        # Initial uniform weights (Bayesian engine will update these)
        n = len(prodrop.candidates)
        subject_candidates = [(c, 1.0 / n) for c in prodrop.candidates]

    # 2. Particle analysis
    particle_ambiguities = analyze_particles(tokens)
    ambiguities.extend(particle_ambiguities)

    # 3. Polysemy detection
    polysemy_ambiguities = detect_polysemy(tokens)
    ambiguities.extend(polysemy_ambiguities)

    return SegmentedMessage(
        message=message,
        tokens=tokens,
        ambiguities=ambiguities,
        has_dropped_subject=has_dropped_subject,
        subject_candidates=subject_candidates,
    )


def count_interpretation_combinations(seg_msg: SegmentedMessage) -> int:
    """Count total possible interpretation combinations.

    Used to assess complexity before generating all candidates.
    """
    if not seg_msg.ambiguities:
        return 1
    total = 1
    for amb in seg_msg.ambiguities:
        total *= len(amb.candidates)
    return total


def generate_interpretation_axes(
    seg_msg: SegmentedMessage,
) -> list[tuple[AmbiguityClass, str, list[str]]]:
    """Extract the independent axes of ambiguity for Bayesian processing.

    Returns:
        List of (ambiguity_class, span, candidates) tuples.
        Each tuple represents one dimension of the interpretation space.
    """
    axes = []
    for amb in seg_msg.ambiguities:
        axes.append((amb.ambiguity_class, amb.span, amb.candidates))
    return axes
