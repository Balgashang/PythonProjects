"""Core data structures for the Bayesian-Shannon Translation Engine.

Every module communicates through these dataclasses. They define the contract
between pipeline stages: Parser -> Linguistics -> Bayesian -> Entropy -> Translation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional


class Language(Enum):
    ZH_TW = "zh-TW"
    EN = "en"
    MIXED = "mixed"
    UNKNOWN = "unknown"


class Speaker(Enum):
    MEI_HUI = "mei_hui"
    JUSTIN = "justin"
    SYSTEM = "system"  # date headers, timestamps, etc.


class AmbiguityClass(Enum):
    PRODROP = "prodrop"          # dropped subject
    POLYSEMY = "polysemy"        # word with multiple meanings
    PARTICLE = "particle"        # pragmatic particle ambiguity
    REFERENT = "referent"        # unclear demonstrative/pronoun referent
    IMPLICATURE = "implicature"  # pragmatic meaning beyond literal


class ParticleType(Enum):
    MODAL = "modal"              # 吧, 嘛
    ASPECTUAL = "aspectual"      # 了, 過, 著
    SENTENCE_FINAL = "sentence_final"  # 啊, 呢, 喔
    STRUCTURAL = "structural"    # 的, 地, 得


class ConfidenceTier(Enum):
    HIGH = "high"        # H < 0.3 — one dominant interpretation
    MEDIUM = "medium"    # 0.3 <= H < 1.0
    LOW = "low"          # 1.0 <= H < 2.0
    REVIEW = "review"    # H >= 2.0 — genuinely ambiguous


# =============================================================================
# Stage 1: Parser output
# =============================================================================

@dataclass
class Message:
    """A single message extracted from the transcript."""
    index: int
    speaker: Speaker
    raw_text: str
    language: Language
    timestamp: Optional[datetime] = None
    date_str: Optional[str] = None        # e.g. "2/20 FRI"
    time_str: Optional[str] = None        # e.g. "9:47 PM"
    is_media: bool = False                 # bracketed image/video description
    is_continuation: bool = False          # multi-line message from same speaker


# =============================================================================
# Stage 2: Linguistic decomposition output
# =============================================================================

@dataclass
class Token:
    """A segmented token with linguistic annotations."""
    surface: str                           # characters as they appear
    pos: str = ""                          # part-of-speech tag
    is_particle: bool = False
    particle_type: Optional[ParticleType] = None
    ambiguity_class: Optional[AmbiguityClass] = None
    candidates: list[str] = field(default_factory=list)


@dataclass
class AmbiguityAnnotation:
    """A single detected ambiguity in a message."""
    ambiguity_class: AmbiguityClass
    span: str                              # the ambiguous text span
    candidates: list[str]                  # possible interpretations/referents
    position: int = 0                      # token index in the sentence


@dataclass
class SegmentedMessage:
    """A Chinese message after linguistic decomposition."""
    message: Message
    tokens: list[Token]
    ambiguities: list[AmbiguityAnnotation] = field(default_factory=list)
    has_dropped_subject: bool = False
    subject_candidates: list[tuple[str, float]] = field(default_factory=list)


# =============================================================================
# Stage 3-4: Bayesian + Entropy output
# =============================================================================

@dataclass
class AmbiguityResolution:
    """How a specific ambiguity was resolved in a candidate interpretation."""
    ambiguity_class: AmbiguityClass
    span: str
    chosen: str                            # the selected interpretation
    probability: float                     # P(this resolution | evidence)


@dataclass
class TranslationCandidate:
    """One possible English rendering with its probability."""
    english_text: str
    probability: float
    resolutions: list[AmbiguityResolution] = field(default_factory=list)


@dataclass
class TranslatedMessage:
    """Final output for a single message."""
    source: SegmentedMessage
    candidates: list[TranslationCandidate]  # sorted by probability descending
    entropy: float = 0.0
    confidence_tier: ConfidenceTier = ConfidenceTier.HIGH
    primary_translation: str = ""           # top candidate's english_text


# =============================================================================
# Corpus-level structures
# =============================================================================

@dataclass
class Corpus:
    """The full parsed transcript as a structured corpus."""
    messages: list[Message]
    mei_hui_messages: list[Message] = field(default_factory=list)
    justin_messages: list[Message] = field(default_factory=list)
    date_range: tuple[Optional[str], Optional[str]] = (None, None)

    def __post_init__(self):
        if not self.mei_hui_messages:
            self.mei_hui_messages = [
                m for m in self.messages if m.speaker == Speaker.MEI_HUI
            ]
        if not self.justin_messages:
            self.justin_messages = [
                m for m in self.messages if m.speaker == Speaker.JUSTIN
            ]


@dataclass
class PriorDistribution:
    """A probability distribution used as a Bayesian prior."""
    name: str                              # e.g. "subject_drop_referent"
    labels: list[str]                      # e.g. ["我", "你", "我們", ...]
    probabilities: list[float]             # same length as labels, sums to 1.0
    sample_count: int = 0                  # how many observations built this prior
