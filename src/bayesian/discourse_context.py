"""Discourse context extraction for Bayesian inference.

Builds context features from the sliding window of messages surrounding
an ambiguous message. These features serve as evidence for the posterior
computation: what did Justin say? What topic are they discussing?
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from src.models import Message, Speaker, Language


@dataclass
class DiscourseContext:
    """Context features extracted from the message window."""
    preceding_messages: list[Message] = field(default_factory=list)
    following_messages: list[Message] = field(default_factory=list)
    justin_preceding: list[Message] = field(default_factory=list)
    meihui_preceding: list[Message] = field(default_factory=list)

    # Extracted features
    is_response_to_question: bool = False
    question_about_you: bool = False      # Justin asked about "you"
    question_about_what: bool = False     # Justin asked "what" question
    topic_keywords: list[str] = field(default_factory=list)
    context_type: str = "default"         # for structural prior lookup


# Question patterns in Justin's English messages
YOU_QUESTION_PATTERNS = [
    re.compile(r'\b(?:have you|did you|are you|do you|will you|can you|would you)\b', re.I),
    re.compile(r'\b(?:your|you)\b.*\?', re.I),
]

WHAT_QUESTION_PATTERNS = [
    re.compile(r'\b(?:what|which|how|where|when|why)\b', re.I),
]

# Keywords for detecting advice-giving context
ADVICE_KEYWORDS_ZH = {'要', '不要', '應該', '最好', '盡量', '千萬', '記得', '小心'}

# Keywords for topic detection
TOPIC_KEYWORDS = {
    'food': {'吃', '早餐', '午餐', '晚餐', '飯', '菜', '煮', '水煮蛋', '牛油果'},
    'health': {'健康', '身體', '針灸', '醫生', '量子環', '產品', '改善', '養生'},
    'work': {'工作', '上班', '下班', '老闆', '忙', '賺錢', '公司', '店'},
    'family': {'家人', '爸爸', '媽媽', '妹妹', '弟弟', '台灣', '家', '家庭'},
    'money': {'錢', '投資', '房租', '存錢', '保險', '薪水', '費用'},
    'relationship': {'朋友', '認識', '緣分', '聊天', '碰面'},
}


def extract_context(
    target_index: int,
    all_messages: list[Message],
    window_before: int = 3,
    window_after: int = 2,
) -> DiscourseContext:
    """Extract discourse context around a target message.

    Args:
        target_index: Position of the target message in all_messages.
        all_messages: Full ordered message list.
        window_before: Number of messages to look back.
        window_after: Number of messages to look ahead.

    Returns:
        DiscourseContext with extracted features.
    """
    ctx = DiscourseContext()

    # Gather window messages
    start = max(0, target_index - window_before)
    end = min(len(all_messages), target_index + window_after + 1)

    ctx.preceding_messages = all_messages[start:target_index]
    ctx.following_messages = all_messages[target_index + 1:end]

    # Split by speaker
    ctx.justin_preceding = [
        m for m in ctx.preceding_messages if m.speaker == Speaker.JUSTIN
    ]
    ctx.meihui_preceding = [
        m for m in ctx.preceding_messages if m.speaker == Speaker.MEI_HUI
    ]

    # Analyze Justin's preceding messages for question patterns
    for msg in ctx.justin_preceding:
        if msg.language in (Language.EN, Language.MIXED):
            text = msg.raw_text

            for pattern in YOU_QUESTION_PATTERNS:
                if pattern.search(text):
                    ctx.is_response_to_question = True
                    ctx.question_about_you = True
                    break

            for pattern in WHAT_QUESTION_PATTERNS:
                if pattern.search(text):
                    ctx.is_response_to_question = True
                    ctx.question_about_what = True
                    break

    # Detect advice-giving context from the target's surrounding Chinese
    target_msg = all_messages[target_index] if target_index < len(all_messages) else None
    if target_msg:
        text = target_msg.raw_text
        advice_count = sum(1 for kw in ADVICE_KEYWORDS_ZH if kw in text)
        if advice_count >= 1:
            ctx.context_type = 'giving_advice'
        elif ctx.question_about_you:
            ctx.context_type = 'responding_to_you_question'
        elif not ctx.preceding_messages or (
            ctx.preceding_messages and
            ctx.preceding_messages[-1].speaker == Speaker.MEI_HUI
        ):
            ctx.context_type = 'topic_initiation'

    # Extract topic keywords
    window_text = ' '.join(
        m.raw_text for m in ctx.preceding_messages + ctx.following_messages
    )
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(kw in window_text for kw in keywords):
            ctx.topic_keywords.append(topic)

    return ctx
