"""Lightweight topic model for conversation segmentation.

Uses TF-IDF over segmented tokens with sliding window clustering
to identify conversation topics. This feeds into the Bayesian engine
as a medium-weight evidence source for disambiguation.

Full LDA is overkill for a ~120 message corpus. Instead we use
cosine similarity between windowed TF-IDF vectors to detect
topic shifts and assign soft topic labels.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from math import log

import numpy as np

from src.models import SegmentedMessage


# Stop words to exclude from topic modeling (function words, particles)
STOP_WORDS_ZH = {
    '的', '了', '在', '是', '我', '你', '他', '她', '它',
    '們', '這', '那', '都', '也', '就', '不', '有', '會',
    '很', '好', '可以', '要', '把', '被', '跟', '和', '嗎',
    '吧', '啊', '呢', '嘛', '喔', '啦', '哦', '呀',
    '一', '個', '到', '去', '來', '上', '下', '中',
}


@dataclass
class TopicSegment:
    """A contiguous segment of conversation with a dominant topic."""
    start_index: int
    end_index: int
    topic_label: str
    topic_keywords: list[str]
    confidence: float


@dataclass
class TopicModel:
    """Lightweight topic model built from the conversation corpus."""
    segments: list[TopicSegment] = field(default_factory=list)
    vocabulary: list[str] = field(default_factory=list)
    idf: dict[str, float] = field(default_factory=dict)

    def get_topic_at(self, message_index: int) -> TopicSegment | None:
        """Get the topic segment containing a given message index."""
        for seg in self.segments:
            if seg.start_index <= message_index <= seg.end_index:
                return seg
        return None


def build_topic_model(
    segmented_messages: list[SegmentedMessage],
    window_size: int = 10,
    min_topic_shift_similarity: float = 0.3,
) -> TopicModel:
    """Build a topic model from segmented Chinese messages.

    Args:
        segmented_messages: All Chinese messages after segmentation.
        window_size: Number of messages per sliding window.
        min_topic_shift_similarity: Cosine similarity threshold below
            which a topic shift is detected.

    Returns:
        TopicModel with identified conversation segments.
    """
    if not segmented_messages:
        return TopicModel()

    # Extract content words (exclude stop words and particles)
    doc_words: list[list[str]] = []
    for seg_msg in segmented_messages:
        words = [
            tok.surface for tok in seg_msg.tokens
            if tok.surface not in STOP_WORDS_ZH
            and len(tok.surface) > 1  # skip single chars mostly
            and not tok.is_particle
        ]
        doc_words.append(words)

    # Build vocabulary and IDF
    vocab = set()
    for words in doc_words:
        vocab.update(words)
    vocab_list = sorted(vocab)
    vocab_index = {w: i for i, w in enumerate(vocab_list)}

    n_docs = len(doc_words)
    doc_freq: Counter[str] = Counter()
    for words in doc_words:
        for w in set(words):
            doc_freq[w] += 1

    idf = {}
    for word in vocab_list:
        idf[word] = log((n_docs + 1) / (doc_freq[word] + 1)) + 1

    # Build TF-IDF vectors for sliding windows
    def window_tfidf(start: int, end: int) -> np.ndarray:
        vec = np.zeros(len(vocab_list))
        tf: Counter[str] = Counter()
        for i in range(start, min(end, len(doc_words))):
            tf.update(doc_words[i])
        for word, count in tf.items():
            if word in vocab_index:
                vec[vocab_index[word]] = count * idf.get(word, 1.0)
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec /= norm
        return vec

    # Detect topic shifts via cosine similarity between adjacent windows
    segments: list[TopicSegment] = []
    segment_start = 0

    for i in range(window_size, len(segmented_messages), window_size // 2):
        prev_vec = window_tfidf(max(0, i - window_size), i)
        curr_vec = window_tfidf(i, i + window_size)

        similarity = float(np.dot(prev_vec, curr_vec))

        if similarity < min_topic_shift_similarity:
            # Topic shift detected
            seg = _build_segment(
                segmented_messages, doc_words, vocab_index, idf,
                segment_start, i - 1,
            )
            segments.append(seg)
            segment_start = i

    # Final segment
    if segment_start < len(segmented_messages):
        seg = _build_segment(
            segmented_messages, doc_words, vocab_index, idf,
            segment_start, len(segmented_messages) - 1,
        )
        segments.append(seg)

    return TopicModel(
        segments=segments,
        vocabulary=vocab_list,
        idf=idf,
    )


def _build_segment(
    segmented_messages: list[SegmentedMessage],
    doc_words: list[list[str]],
    vocab_index: dict[str, int],
    idf: dict[str, float],
    start: int,
    end: int,
) -> TopicSegment:
    """Build a TopicSegment from a range of messages."""
    # Aggregate word frequencies in this segment
    word_freq: Counter[str] = Counter()
    for i in range(start, min(end + 1, len(doc_words))):
        word_freq.update(doc_words[i])

    # Top keywords by TF-IDF score
    scored = [
        (word, count * idf.get(word, 1.0))
        for word, count in word_freq.items()
    ]
    scored.sort(key=lambda x: x[1], reverse=True)
    top_keywords = [w for w, _ in scored[:5]]

    # Simple topic label from top keyword
    topic_label = top_keywords[0] if top_keywords else "general"

    # Map back to original message indices
    start_idx = segmented_messages[start].message.index if start < len(segmented_messages) else 0
    end_idx = segmented_messages[min(end, len(segmented_messages) - 1)].message.index

    return TopicSegment(
        start_index=start_idx,
        end_index=end_idx,
        topic_label=topic_label,
        topic_keywords=top_keywords,
        confidence=0.5,  # base confidence, refined by posterior
    )
