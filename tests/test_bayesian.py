"""Tests for Bayesian prior construction and posterior computation."""

import pytest
import numpy as np

from src.models import (
    AmbiguityAnnotation,
    AmbiguityClass,
    Language,
    Message,
    PriorDistribution,
    SegmentedMessage,
    Speaker,
    Token,
    TranslationCandidate,
)
from src.bayesian.prior_builder import PriorBuilder, get_structural_subject_prior
from src.bayesian.posterior_engine import (
    PosteriorEngine,
    PosteriorResult,
    resolve_message_ambiguities,
)


class TestPriorBuilder:
    def test_laplace_smoothing(self):
        """Priors should have no zero probabilities due to Laplace smoothing."""
        builder = PriorBuilder(laplace_alpha=1.0)
        prior = builder._counts_to_prior(
            name='test',
            counts={},
            default_labels=['a', 'b', 'c'],
        )
        assert all(p > 0 for p in prior.probabilities)
        assert abs(sum(prior.probabilities) - 1.0) < 0.001

    def test_observed_counts_influence(self):
        """Labels with more observations should have higher probability."""
        from collections import Counter
        builder = PriorBuilder(laplace_alpha=1.0)
        counts = Counter({'我': 50, '你': 10, '我們': 5})
        prior = builder._counts_to_prior(
            name='test',
            counts=counts,
            default_labels=['我', '你', '我們'],
        )
        # 我 should have highest probability
        idx_wo = prior.labels.index('我')
        idx_ni = prior.labels.index('你')
        assert prior.probabilities[idx_wo] > prior.probabilities[idx_ni]

    def test_scan_corpus(self):
        """Scanning a corpus should produce valid prior distributions."""
        builder = PriorBuilder()
        # Create some segmented messages with known tokens
        messages = [
            SegmentedMessage(
                message=Message(
                    index=0, speaker=Speaker.MEI_HUI,
                    raw_text="我吃早餐", language=Language.ZH_TW,
                ),
                tokens=[
                    Token(surface='我', pos='r'),
                    Token(surface='吃', pos='v'),
                    Token(surface='早餐', pos='n'),
                ],
                has_dropped_subject=False,
            ),
            SegmentedMessage(
                message=Message(
                    index=1, speaker=Speaker.MEI_HUI,
                    raw_text="你也快去吃", language=Language.ZH_TW,
                ),
                tokens=[
                    Token(surface='你', pos='r'),
                    Token(surface='也', pos='d'),
                    Token(surface='快', pos='d'),
                    Token(surface='去', pos='v'),
                    Token(surface='吃', pos='v'),
                ],
                has_dropped_subject=False,
            ),
        ]
        priors = builder.scan_corpus(messages)
        assert 'subject_referent' in priors
        assert sum(priors['subject_referent'].probabilities) == pytest.approx(1.0, abs=0.01)


class TestStructuralPriors:
    def test_advice_prior_boosts_you(self):
        prior = get_structural_subject_prior('giving_advice')
        assert prior['你'] > prior['我']

    def test_response_prior_boosts_i(self):
        prior = get_structural_subject_prior('responding_to_you_question')
        assert prior['我'] > prior['你']

    def test_default_sums_to_one(self):
        prior = get_structural_subject_prior('default')
        assert abs(sum(prior.values()) - 1.0) < 0.001


class TestResolveAmbiguities:
    def test_no_ambiguity(self):
        seg_msg = SegmentedMessage(
            message=Message(
                index=0, speaker=Speaker.MEI_HUI,
                raw_text="好的", language=Language.ZH_TW,
            ),
            tokens=[Token(surface='好的', pos='a')],
        )
        candidates = resolve_message_ambiguities(seg_msg, [])
        assert len(candidates) == 1
        assert candidates[0].probability == 1.0

    def test_single_ambiguity(self):
        ambiguity = AmbiguityAnnotation(
            ambiguity_class=AmbiguityClass.PRODROP,
            span="[dropped subject]",
            candidates=["我", "你", "我們"],
        )
        posterior_result = PosteriorResult(
            ambiguity=ambiguity,
            posterior=[("我", 0.6), ("你", 0.3), ("我們", 0.1)],
        )
        seg_msg = SegmentedMessage(
            message=Message(
                index=0, speaker=Speaker.MEI_HUI,
                raw_text="去了", language=Language.ZH_TW,
            ),
            tokens=[Token(surface='去', pos='v'), Token(surface='了', pos='u')],
            ambiguities=[ambiguity],
            has_dropped_subject=True,
        )
        candidates = resolve_message_ambiguities(seg_msg, [posterior_result])
        assert len(candidates) >= 2
        # Probabilities should sum to ~1
        total = sum(c.probability for c in candidates)
        assert abs(total - 1.0) < 0.01
        # Top candidate should have highest probability
        assert candidates[0].probability >= candidates[-1].probability
