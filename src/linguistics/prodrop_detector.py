"""Pro-drop (dropped subject) detection for Mandarin Chinese.

Chinese is aggressively pro-drop: subjects are routinely omitted when
recoverable from context. "去了" could mean I/you/she/we/they went.
This module detects when a subject has been dropped and generates
candidate referents with initial weights based on discourse position.
"""

from __future__ import annotations

from src.models import AmbiguityAnnotation, AmbiguityClass, Token, Message, Speaker

# POS tags that indicate a subject (noun, pronoun)
SUBJECT_POS = {
    # jieba tags
    'r', 'rr', 'rz', 'rn',  # pronouns
    'n', 'nr', 'ns', 'nt', 'nz',  # nouns
    # ckip tags
    'Nh', 'Nb', 'Na', 'Nc', 'Nd',  # CKIP noun/pronoun tags
}

# POS tags that indicate a verb (main predicate)
VERB_POS = {
    'v', 'vn', 'vd', 'vg',  # jieba verb tags
    'VA', 'VAC', 'VB', 'VC', 'VCL', 'VD', 'VE', 'VF',  # CKIP verb tags
    'VG', 'VH', 'VHC', 'VI', 'VJ', 'VK', 'VL',
}

# Common explicit subject pronouns in Mei Hui's speech
PRONOUN_MAP = {
    '我': 'I/me',
    '你': 'you',
    '我們': 'we/us',
    '你們': 'you (plural)',
    '他': 'he/him',
    '她': 'she/her',
    '他們': 'they/them',
    '她們': 'they/them (f)',
    '大家': 'everyone',
}

# Default candidate referents for dropped subjects, ordered by typical frequency
# in casual Taiwanese Mandarin conversation
DEFAULT_CANDIDATES = ['我', '你', '我們', '她', '他們']


def detect_prodrop(
    tokens: list[Token],
    preceding_message: Message | None = None,
) -> AmbiguityAnnotation | None:
    """Detect if a sentence has a dropped subject.

    Args:
        tokens: Segmented tokens of the Chinese message.
        preceding_message: The message immediately before this one (for context).

    Returns:
        AmbiguityAnnotation if a dropped subject is detected, None otherwise.
    """
    if not tokens:
        return None

    # Find the first verb
    first_verb_idx = None
    for i, tok in enumerate(tokens):
        if tok.pos in VERB_POS:
            first_verb_idx = i
            break

    if first_verb_idx is None:
        # No verb found — might be a fragment, not a pro-drop issue
        return None

    # Check if any subject-like token appears before the first verb
    has_subject = False
    for i in range(first_verb_idx):
        if tokens[i].pos in SUBJECT_POS:
            has_subject = True
            break
        # Also check for known pronoun surfaces directly
        if tokens[i].surface in PRONOUN_MAP:
            has_subject = True
            break

    if has_subject:
        return None

    # Subject is dropped — generate candidates
    candidates = list(DEFAULT_CANDIDATES)

    # Weight adjustment hint based on preceding message
    # If Justin asked a question about "you", the dropped subject is likely "I" (answering)
    if preceding_message and preceding_message.speaker == Speaker.JUSTIN:
        justin_text = preceding_message.raw_text.lower()
        if any(q in justin_text for q in ['you', 'your', 'have you', 'did you', 'are you']):
            # Likely answering about self
            if '我' in candidates:
                candidates.remove('我')
                candidates.insert(0, '我')

    return AmbiguityAnnotation(
        ambiguity_class=AmbiguityClass.PRODROP,
        span="[dropped subject]",
        candidates=candidates,
        position=0,
    )
