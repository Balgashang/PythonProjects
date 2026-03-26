"""Word segmentation abstraction with ckip-transformers and jieba backends.

Segments Traditional Chinese text into tokens with part-of-speech tags.
The segmenter is the foundation for all downstream ambiguity detection.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from src.models import Token, ParticleType

# Sentence-final particles and their types
PARTICLES = {
    '吧': ParticleType.MODAL,
    '嘛': ParticleType.MODAL,
    '啊': ParticleType.SENTENCE_FINAL,
    '呢': ParticleType.SENTENCE_FINAL,
    '喔': ParticleType.SENTENCE_FINAL,
    '啦': ParticleType.SENTENCE_FINAL,
    '哦': ParticleType.SENTENCE_FINAL,
    '嗎': ParticleType.SENTENCE_FINAL,
    '了': ParticleType.ASPECTUAL,
    '過': ParticleType.ASPECTUAL,
    '著': ParticleType.ASPECTUAL,
    '的': ParticleType.STRUCTURAL,
    '地': ParticleType.STRUCTURAL,
    '得': ParticleType.STRUCTURAL,
}

# POS tags that indicate particles (varies by tagger)
PARTICLE_POS = {'T', 'Td', 'Tc', 'uj', 'ul', 'u', 'y', 'Nf'}


class BaseSegmenter(ABC):
    """Abstract base for Chinese word segmenters."""

    @abstractmethod
    def segment(self, text: str) -> list[Token]:
        """Segment text into a list of Tokens with POS tags."""
        ...

    def _annotate_particle(self, token: Token) -> Token:
        """Check if a token is a known particle and annotate it."""
        if token.surface in PARTICLES:
            token.is_particle = True
            token.particle_type = PARTICLES[token.surface]
        elif token.pos in PARTICLE_POS:
            token.is_particle = True
        return token


class JiebaSegmenter(BaseSegmenter):
    """Jieba-based segmenter with Traditional Chinese support."""

    def __init__(self):
        import jieba
        import jieba.posseg as pseg
        # jieba initializes with its default dictionary automatically
        self._pseg = pseg
        self._initialized = True

    def segment(self, text: str) -> list[Token]:
        tokens = []
        for word, flag in self._pseg.cut(text):
            word = word.strip()
            if not word:
                continue
            token = Token(surface=word, pos=flag)
            token = self._annotate_particle(token)
            tokens.append(token)
        return tokens


class CkipSegmenter(BaseSegmenter):
    """CKIP-transformers-based segmenter (preferred for Traditional Chinese)."""

    def __init__(self):
        try:
            from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger
            self._ws = CkipWordSegmenter(model="bert-base")
            self._pos = CkipPosTagger(model="bert-base")
            self._available = True
        except ImportError:
            self._available = False
            raise ImportError(
                "ckip-transformers not installed. "
                "Install with: pip install ckip-transformers torch"
            )

    def segment(self, text: str) -> list[Token]:
        ws_results = self._ws([text])
        pos_results = self._pos(ws_results)

        tokens = []
        for word, pos in zip(ws_results[0], pos_results[0]):
            word = word.strip()
            if not word:
                continue
            token = Token(surface=word, pos=pos)
            token = self._annotate_particle(token)
            tokens.append(token)
        return tokens


def create_segmenter(backend: str = "jieba") -> BaseSegmenter:
    """Factory function to create the configured segmenter."""
    if backend == "ckip":
        try:
            return CkipSegmenter()
        except ImportError:
            print("Warning: ckip-transformers not available, falling back to jieba")
            return JiebaSegmenter()
    return JiebaSegmenter()
