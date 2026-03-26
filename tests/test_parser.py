"""Tests for the transcript parser."""

import pytest
from pathlib import Path

from src.models import Language, Speaker
from src.parser.transcript_parser import TranscriptParser, parse_transcript
from src.parser.language_detector import detect_language, cjk_ratio
from src.parser.sanitizer import is_media_description, sanitize_message


# =============================================================================
# Language detection tests
# =============================================================================

class TestLanguageDetection:
    def test_pure_chinese(self):
        assert detect_language("你好，我是Cindy") == Language.ZH_TW

    def test_pure_english(self):
        assert detect_language("Hello, I am Justin") == Language.EN

    def test_empty(self):
        assert detect_language("") == Language.UNKNOWN

    def test_cjk_ratio_chinese(self):
        ratio = cjk_ratio("你好世界")
        assert ratio == 1.0

    def test_cjk_ratio_english(self):
        assert cjk_ratio("hello world") == 0.0

    def test_cjk_ratio_mixed(self):
        ratio = cjk_ratio("我是Cindy")
        # 2 CJK chars out of 7 total non-whitespace = 0.286
        assert 0.2 < ratio < 0.5


# =============================================================================
# Sanitizer tests
# =============================================================================

class TestSanitizer:
    def test_media_detection_sends(self):
        assert is_media_description("[Sends photo]")
        assert is_media_description("[Sends gif of a bird holding a flower]")

    def test_media_detection_photo(self):
        assert is_media_description("[Photo: breakfast — cashews, avocado]")

    def test_media_detection_not_media(self):
        assert not is_media_description("你好")
        assert not is_media_description("Hello world")

    def test_sanitize_weixin(self):
        text = "你好\n[Translated by Weixin]\nHello"
        cleaned, was_sanitized = sanitize_message(text)
        assert was_sanitized
        assert "Translated by Weixin" not in cleaned
        assert "Hello" not in cleaned
        assert "你好" in cleaned

    def test_sanitize_no_translation(self):
        text = "你好世界"
        cleaned, was_sanitized = sanitize_message(text)
        assert not was_sanitized
        assert cleaned == text


# =============================================================================
# Parser tests
# =============================================================================

class TestTranscriptParser:
    @pytest.fixture
    def sample_transcript(self):
        fixture_path = Path(__file__).parent / "fixtures" / "sample_transcript.md"
        return fixture_path.read_text(encoding='utf-8')

    def test_parse_extracts_messages(self, sample_transcript):
        corpus = parse_transcript(sample_transcript)
        assert len(corpus.messages) > 0

    def test_parse_identifies_speakers(self, sample_transcript):
        corpus = parse_transcript(sample_transcript)
        speakers = {m.speaker for m in corpus.messages}
        assert Speaker.MEI_HUI in speakers
        assert Speaker.JUSTIN in speakers

    def test_parse_separates_languages(self, sample_transcript):
        corpus = parse_transcript(sample_transcript)
        assert len(corpus.mei_hui_messages) > 0
        assert len(corpus.justin_messages) > 0

    def test_parse_detects_chinese(self, sample_transcript):
        corpus = parse_transcript(sample_transcript)
        chinese_msgs = [
            m for m in corpus.mei_hui_messages
            if m.language == Language.ZH_TW
        ]
        assert len(chinese_msgs) > 0

    def test_parse_extracts_dates(self, sample_transcript):
        corpus = parse_transcript(sample_transcript)
        dates = {m.date_str for m in corpus.messages if m.date_str}
        assert "2/20" in dates
        assert "2/21" in dates

    def test_parse_detects_media(self, sample_transcript):
        corpus = parse_transcript(sample_transcript)
        media = [m for m in corpus.messages if m.is_media]
        assert len(media) > 0

    def test_message_ordering(self, sample_transcript):
        corpus = parse_transcript(sample_transcript)
        indices = [m.index for m in corpus.messages]
        assert indices == sorted(indices)

    def test_corpus_date_range(self, sample_transcript):
        corpus = parse_transcript(sample_transcript)
        assert corpus.date_range[0] is not None
        assert corpus.date_range[1] is not None
