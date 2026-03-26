"""Language detection based on Unicode character ranges.

Identifies Traditional Chinese vs English vs mixed content by examining
the ratio of CJK characters in a text string.
"""

import re
import unicodedata
from src.models import Language

# CJK Unicode ranges covering Traditional and Simplified Chinese
CJK_RANGES = [
    (0x4E00, 0x9FFF),    # CJK Unified Ideographs
    (0x3400, 0x4DBF),    # CJK Unified Ideographs Extension A
    (0x20000, 0x2A6DF),  # Extension B
    (0x2A700, 0x2B73F),  # Extension C
    (0x2B740, 0x2B81F),  # Extension D
    (0xF900, 0xFAFF),    # CJK Compatibility Ideographs
    (0x2F800, 0x2FA1F),  # CJK Compatibility Ideographs Supplement
]

# Bopomofo (unique to Traditional Chinese / Taiwanese input)
BOPOMOFO_RANGE = (0x3100, 0x312F)

# Common CJK punctuation
CJK_PUNCT = set("，。！？、；：「」『』【】（）《》〈〉～⋯—")


def is_cjk_char(char: str) -> bool:
    """Check if a character is in any CJK Unicode range."""
    cp = ord(char)
    for start, end in CJK_RANGES:
        if start <= cp <= end:
            return True
    return False


def cjk_ratio(text: str) -> float:
    """Return the ratio of CJK characters to total non-whitespace characters."""
    stripped = re.sub(r'\s+', '', text)
    if not stripped:
        return 0.0
    cjk_count = sum(1 for ch in stripped if is_cjk_char(ch))
    return cjk_count / len(stripped)


def detect_language(text: str, threshold: float = 0.3) -> Language:
    """Detect whether text is primarily Chinese, English, or mixed.

    Args:
        text: The raw message text.
        threshold: Minimum CJK ratio to classify as Chinese.

    Returns:
        Language enum value.
    """
    if not text or not text.strip():
        return Language.UNKNOWN

    ratio = cjk_ratio(text)

    if ratio >= threshold:
        return Language.ZH_TW
    elif ratio == 0.0:
        return Language.EN
    else:
        # Some CJK but below threshold — likely English with a few Chinese words
        # or mixed content
        if ratio > 0.1:
            return Language.MIXED
        return Language.EN
