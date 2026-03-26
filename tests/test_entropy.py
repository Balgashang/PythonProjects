"""Tests for Shannon entropy scoring."""

import pytest
from math import log2

from src.entropy.scorer import (
    shannon_entropy,
    max_entropy,
    normalized_entropy,
    classify_confidence,
    score_message,
)
from src.models import ConfidenceTier, TranslationCandidate


class TestShannonEntropy:
    def test_certain_distribution(self):
        """Single candidate with probability 1 should have zero entropy."""
        assert shannon_entropy([1.0]) == 0.0

    def test_uniform_two(self):
        """Uniform distribution over 2 should give entropy of 1 bit."""
        h = shannon_entropy([0.5, 0.5])
        assert abs(h - 1.0) < 0.001

    def test_uniform_four(self):
        """Uniform over 4 should give entropy of 2 bits."""
        h = shannon_entropy([0.25, 0.25, 0.25, 0.25])
        assert abs(h - 2.0) < 0.001

    def test_skewed_distribution(self):
        """Highly skewed should have low entropy."""
        h = shannon_entropy([0.95, 0.05])
        assert h < 0.4

    def test_max_entropy(self):
        assert abs(max_entropy(2) - 1.0) < 0.001
        assert abs(max_entropy(4) - 2.0) < 0.001
        assert max_entropy(1) == 0.0

    def test_normalized_entropy(self):
        # Uniform should normalize to 1.0
        assert abs(normalized_entropy([0.5, 0.5]) - 1.0) < 0.001
        # Certain should normalize to 0.0
        assert normalized_entropy([1.0]) == 0.0


class TestConfidenceTiers:
    def test_high_confidence(self):
        assert classify_confidence(0.1) == ConfidenceTier.HIGH

    def test_medium_confidence(self):
        assert classify_confidence(0.5) == ConfidenceTier.MEDIUM

    def test_low_confidence(self):
        assert classify_confidence(1.5) == ConfidenceTier.LOW

    def test_review(self):
        assert classify_confidence(2.5) == ConfidenceTier.REVIEW

    def test_boundary_high(self):
        assert classify_confidence(0.29) == ConfidenceTier.HIGH
        assert classify_confidence(0.3) == ConfidenceTier.MEDIUM


class TestScoreMessage:
    def test_single_candidate(self):
        candidates = [TranslationCandidate(english_text="hello", probability=1.0)]
        entropy, tier = score_message(candidates)
        assert entropy == 0.0
        assert tier == ConfidenceTier.HIGH

    def test_ambiguous_candidates(self):
        candidates = [
            TranslationCandidate(english_text="I go", probability=0.5),
            TranslationCandidate(english_text="you go", probability=0.5),
        ]
        entropy, tier = score_message(candidates)
        assert abs(entropy - 1.0) < 0.001
        # H=1.0 is at the boundary — classified as LOW (1.0 <= H < 2.0)
        assert tier == ConfidenceTier.LOW

    def test_highly_ambiguous(self):
        candidates = [
            TranslationCandidate(english_text=f"option {i}", probability=0.2)
            for i in range(5)
        ]
        entropy, tier = score_message(candidates)
        assert entropy > 2.0
        assert tier == ConfidenceTier.REVIEW

    def test_empty_candidates(self):
        entropy, tier = score_message([])
        assert entropy == 0.0
        assert tier == ConfidenceTier.HIGH
