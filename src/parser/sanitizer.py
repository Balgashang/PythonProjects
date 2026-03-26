"""Sanitization: strip injected translations, detect media descriptions.

CRITICAL: Do not contaminate the corpus. Any pre-existing English translations
of Chinese messages (from WeChat, DeepSeek, or prior AI) must be stripped before
the Bayesian engine sees the data. Only the raw Chinese feeds the model.
"""

import re

# Patterns indicating a WeChat/Weixin inline translation
WEIXIN_PATTERNS = [
    re.compile(r'\[?\s*Translated by Weixin\s*\]?', re.IGNORECASE),
    re.compile(r'\[?\s*翻[譯译]自微信\s*\]?'),
]

# Patterns for media descriptions (these are not translatable text)
MEDIA_PATTERNS = [
    re.compile(r'^\s*\[(?:Photo|Image|Video|Sticker|GIF|Voice|File|Sends?\s)', re.IGNORECASE),
    re.compile(r'^\s*\[.*(?:photo|image|video|gif|sticker|selfie|screenshot|card|slides?|PowerPoint).*\]\s*$', re.IGNORECASE),
]


def is_weixin_translation_marker(line: str) -> bool:
    """Check if a line is a WeChat translation marker."""
    return any(p.search(line) for p in WEIXIN_PATTERNS)


def is_media_description(text: str) -> bool:
    """Check if text is a bracketed media description rather than message content."""
    text = text.strip()
    if not text:
        return False
    # Must start with [ and be primarily a description
    if any(p.match(text) for p in MEDIA_PATTERNS):
        return True
    # Generic bracket check for single-line bracketed descriptions
    if text.startswith('[') and text.endswith(']') and len(text) < 200:
        return True
    return False


def sanitize_message(text: str) -> tuple[str, bool]:
    """Remove any injected translations from a message.

    Returns:
        Tuple of (cleaned_text, was_sanitized).
        If was_sanitized is True, translations were found and removed.
    """
    lines = text.split('\n')
    cleaned = []
    was_sanitized = False
    skip_next = False

    for line in lines:
        if skip_next:
            skip_next = False
            was_sanitized = True
            continue

        if is_weixin_translation_marker(line):
            # Skip the marker and the next line (the translation itself)
            skip_next = True
            was_sanitized = True
            continue

        cleaned.append(line)

    return '\n'.join(cleaned), was_sanitized
