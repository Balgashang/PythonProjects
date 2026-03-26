"""Parse raw WeChat transcript markdown into structured Message objects.

The transcript format is structured markdown with:
- Date headers: ## M/DD DAY
- Time blocks: [time] or [~time]
- Speaker lines: MEI HUI: text  or  JUSTIN: text
- Media descriptions: [Sends photo], [Photo: ...], etc.
- Multi-line messages from same speaker (consecutive lines without speaker prefix)
"""

from __future__ import annotations

import re
from datetime import datetime
from typing import Optional

from src.models import Corpus, Language, Message, Speaker
from .language_detector import detect_language
from .sanitizer import is_media_description, sanitize_message


# Regex patterns for parsing
DATE_HEADER_RE = re.compile(
    r'^##\s+(\d{1,2}/\d{1,2})\s+(\w+)(?:\s*[—–-]\s*(.*))?$'
)
TIME_BLOCK_RE = re.compile(
    r'^\s*\[~?(\d{1,2}:\d{2}\s*(?:AM|PM)?)\s*\]\s*$', re.IGNORECASE
)
SPEAKER_RE = re.compile(
    r'^(MEI\s*HUI|JUSTIN)\s*:\s*(.*)$', re.IGNORECASE
)
# Lines that are just whitespace, code fences, or horizontal rules
SKIP_RE = re.compile(r'^(?:\s*```\s*|\s*---\s*|\s*)$')


def _parse_speaker(name: str) -> Speaker:
    name_upper = name.upper().replace(' ', '')
    if 'MEIHUI' in name_upper:
        return Speaker.MEI_HUI
    elif 'JUSTIN' in name_upper:
        return Speaker.JUSTIN
    return Speaker.SYSTEM


def _try_parse_time(time_str: str, date_str: Optional[str], year: int = 2026) -> Optional[datetime]:
    """Attempt to build a datetime from date and time strings."""
    if not date_str or not time_str:
        return None
    try:
        time_str = time_str.strip().upper()
        # Normalize various formats
        combined = f"{year}/{date_str} {time_str}"
        for fmt in [
            "%Y/%m/%d %I:%M %p",
            "%Y/%m/%d %I:%M%p",
            "%Y/%m/%d %H:%M",
        ]:
            try:
                return datetime.strptime(combined, fmt)
            except ValueError:
                continue
    except Exception:
        pass
    return None


class TranscriptParser:
    """Parses markdown-formatted WeChat transcript into a Corpus."""

    def __init__(self, cjk_threshold: float = 0.3):
        self.cjk_threshold = cjk_threshold

    def parse(self, text: str) -> Corpus:
        """Parse raw transcript text into a Corpus of Messages."""
        messages: list[Message] = []
        current_date: Optional[str] = None
        current_time: Optional[str] = None
        current_speaker: Optional[Speaker] = None
        msg_index = 0

        lines = text.split('\n')
        i = 0

        while i < len(lines):
            line = lines[i]

            # Skip code fences, horizontal rules, empty lines
            if SKIP_RE.match(line):
                i += 1
                continue

            # Date header: ## 2/20 FRI — SMS
            date_match = DATE_HEADER_RE.match(line)
            if date_match:
                current_date = date_match.group(1)
                current_speaker = None
                i += 1
                continue

            # Time block: [9:47 PM] or [~9:03 PM]
            time_match = TIME_BLOCK_RE.match(line)
            if time_match:
                current_time = time_match.group(1)
                current_speaker = None
                i += 1
                continue

            # Speaker line: MEI HUI: text or JUSTIN: text
            speaker_match = SPEAKER_RE.match(line)
            if speaker_match:
                speaker = _parse_speaker(speaker_match.group(1))
                text_content = speaker_match.group(2).strip()
                current_speaker = speaker

                if text_content:
                    # Check if this line is a media description
                    media = is_media_description(text_content)

                    # Sanitize: strip any injected translations
                    cleaned, _ = sanitize_message(text_content)
                    if not cleaned.strip():
                        i += 1
                        continue

                    lang = Language.ZH_TW if media else detect_language(
                        cleaned, self.cjk_threshold
                    )
                    if media:
                        lang = Language.EN  # descriptions are in English

                    msg = Message(
                        index=msg_index,
                        speaker=speaker,
                        raw_text=cleaned.strip(),
                        language=lang,
                        date_str=current_date,
                        time_str=current_time,
                        timestamp=_try_parse_time(current_time, current_date),
                        is_media=media,
                    )
                    messages.append(msg)
                    msg_index += 1

                i += 1
                continue

            # Continuation line: indented text under the same speaker
            # or a line that isn't a speaker/header/time
            stripped = line.strip()
            if stripped and current_speaker is not None:
                media = is_media_description(stripped)
                cleaned, _ = sanitize_message(stripped)
                if cleaned.strip():
                    lang = Language.EN if media else detect_language(
                        cleaned, self.cjk_threshold
                    )

                    msg = Message(
                        index=msg_index,
                        speaker=current_speaker,
                        raw_text=cleaned.strip(),
                        language=lang,
                        date_str=current_date,
                        time_str=current_time,
                        timestamp=_try_parse_time(current_time, current_date),
                        is_media=media,
                        is_continuation=True,
                    )
                    messages.append(msg)
                    msg_index += 1

            i += 1

        # Build corpus
        dates = [m.date_str for m in messages if m.date_str]
        date_range = (dates[0] if dates else None, dates[-1] if dates else None)

        corpus = Corpus(messages=messages, date_range=date_range)
        return corpus


def parse_transcript(text: str, cjk_threshold: float = 0.3) -> Corpus:
    """Convenience function to parse a transcript string."""
    parser = TranscriptParser(cjk_threshold=cjk_threshold)
    return parser.parse(text)
