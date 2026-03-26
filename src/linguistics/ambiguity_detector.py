"""Orchestrates all ambiguity sub-detectors into a unified pipeline.

This module provides the main entry point for linguistic decomposition:
take a segmented message and return all detected ambiguities.
"""

from __future__ import annotations

from typing import Optional

from src.models import Message, SegmentedMessage, Token
from .candidate_generator import decompose_message
from .segmenter import BaseSegmenter


class AmbiguityPipeline:
    """Runs linguistic decomposition on Chinese messages."""

    def __init__(self, segmenter: BaseSegmenter):
        self.segmenter = segmenter

    def analyze(
        self,
        message: Message,
        preceding_message: Optional[Message] = None,
    ) -> SegmentedMessage:
        """Segment and analyze a Chinese message for ambiguities.

        Args:
            message: A Chinese message to analyze.
            preceding_message: The message before this one (for context).

        Returns:
            SegmentedMessage with tokens and ambiguity annotations.
        """
        tokens = self.segmenter.segment(message.raw_text)
        return decompose_message(tokens, message, preceding_message)

    def analyze_batch(
        self,
        messages: list[Message],
        all_messages: list[Message],
    ) -> list[SegmentedMessage]:
        """Analyze a batch of Chinese messages with context.

        Args:
            messages: Chinese messages to analyze.
            all_messages: Full message list for finding preceding context.

        Returns:
            List of SegmentedMessages.
        """
        # Build index of message positions
        msg_positions = {m.index: i for i, m in enumerate(all_messages)}

        results = []
        for msg in messages:
            # Find the preceding message (any speaker)
            pos = msg_positions.get(msg.index, 0)
            preceding = all_messages[pos - 1] if pos > 0 else None

            seg = self.analyze(msg, preceding)
            results.append(seg)

        return results
