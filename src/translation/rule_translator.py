"""Rule-based Chinese-to-English translation renderer.

Produces English renderings from resolved ambiguity interpretations using:
- Dictionary lookup per token
- Dropped subject insertion with probability annotation
- Particle-to-English tone mapping
- Basic SOV→SVO reordering hints

This is the primary translator. It produces transparent, auditable output
where every translation decision is traceable to a Bayesian resolution.
The output is functional rather than fluent — clarity over elegance.
"""

from __future__ import annotations

from src.models import (
    AmbiguityClass,
    AmbiguityResolution,
    SegmentedMessage,
    Token,
    TranslationCandidate,
)

# Core vocabulary dictionary: Traditional Chinese -> English
# This covers common words in Mei Hui's register
VOCAB: dict[str, str] = {
    # Pronouns
    '我': 'I', '你': 'you', '我們': 'we', '你們': 'you all',
    '他': 'he', '她': 'she', '他們': 'they', '她們': 'they',
    '大家': 'everyone', '自己': 'oneself',
    # Common verbs
    '是': 'is/am/are', '有': 'have', '沒有': 'don\'t have', '沒': 'no/not',
    '不': 'not', '吃': 'eat', '喝': 'drink', '去': 'go', '來': 'come',
    '做': 'do/make', '看': 'look/see', '說': 'say', '想': 'want/think',
    '知道': 'know', '覺得': 'feel/think', '希望': 'hope',
    '喜歡': 'like', '認識': 'know/meet', '工作': 'work',
    '幫忙': 'help', '幫': 'help', '買': 'buy', '賣': 'sell',
    '學習': 'study/learn', '睡覺': 'sleep', '起床': 'wake up',
    '開車': 'drive', '回': 'return/go back', '回去': 'go back',
    '回來': 'come back', '煮': 'cook', '忙': 'busy', '懂': 'understand',
    '住': 'live', '搬': 'move', '租': 'rent', '存': 'save',
    '帶': 'bring/wear', '戴': 'wear', '改善': 'improve',
    '注意': 'pay attention', '小心': 'be careful',
    # Nouns
    '早餐': 'breakfast', '午餐': 'lunch', '晚餐': 'dinner',
    '飯': 'rice/meal', '菜': 'vegetables/dishes', '水': 'water',
    '水煮蛋': 'boiled egg', '牛油果': 'avocado', '堅果': 'nuts',
    '錢': 'money', '薪水': 'salary', '房租': 'rent',
    '身體': 'body/health', '健康': 'health/healthy',
    '家人': 'family', '爸爸': 'dad', '媽媽': 'mom',
    '妹妹': 'younger sister', '弟弟': 'younger brother',
    '朋友': 'friend', '老闆娘': 'boss lady',
    '同事': 'coworker', '產品': 'product', '量子環': 'quantum ring',
    '公司': 'company', '紐約': 'New York', '台灣': 'Taiwan',
    '時間': 'time', '安全': 'safety/safe', '平安': 'peace/safe',
    # Adjectives
    '好': 'good', '棒': 'great', '厲害': 'impressive',
    '辛苦': 'hard/difficult', '開心': 'happy', '健康': 'healthy',
    '重要': 'important', '簡單': 'simple', '貴': 'expensive',
    '善良': 'kind/good-hearted', '乖': 'well-behaved/good',
    # Time
    '今天': 'today', '明天': 'tomorrow', '昨天': 'yesterday',
    '現在': 'now', '以後': 'later/future', '以前': 'before/past',
    '早上': 'morning', '中午': 'noon', '晚上': 'evening',
    # Phrases
    '沒關係': 'it\'s okay/no worries', '沒事': 'it\'s nothing/no problem',
    '加油': 'keep it up/go for it', '好的': 'okay/alright',
    '是的': 'yes', '對': 'right/correct', '晚安': 'good night',
    '早上好': 'good morning', '謝謝': 'thank you', '不客氣': 'you\'re welcome',
    '你也是': 'you too', '快去': 'hurry and go',
    '不著急': 'no rush', '慢慢': 'slowly/take your time',
    '平安健康': 'peace and health', '順其自然': 'let nature take its course',
}

# Particle tone mappings
PARTICLE_TONES: dict[str, dict[str, str]] = {
    '吧': {
        'suggestion': ' (let\'s / how about)',
        'concession': ' (fine / I suppose)',
        'uncertainty': ' (I think / probably)',
        'softened_command': ' (you should)',
    },
    '啊': {
        'exclamation': '!',
        'filler': '',
        'realization': ' (oh!)',
        'urging': ' (come on)',
    },
    '嘛': {
        'obviously': ' (obviously)',
        'mild_reproach': ' (you should know)',
        'explanation': ' (the thing is)',
    },
    '呢': {
        'reciprocal_question': ' (and you?)',
        'continuation': ' (still)',
        'emphasis': ' (indeed)',
    },
    '了': {
        'completed_action': ' [completed]',
        'change_of_state': ' [now/changed]',
        'excessive': ' (too much)',
    },
}

# Subject annotation format
SUBJECT_ANNOTATION = "[{subject}, {prob:.0%}]"


def render_translation(
    seg_msg: SegmentedMessage,
    candidate: TranslationCandidate,
) -> str:
    """Render an English translation from a resolved interpretation.

    Args:
        seg_msg: The segmented Chinese message.
        candidate: A translation candidate with resolved ambiguities.

    Returns:
        English text with inline annotations.
    """
    tokens = seg_msg.tokens
    resolutions = {r.span: r for r in candidate.resolutions}

    parts: list[str] = []

    # Handle dropped subject
    subject_resolution = resolutions.get('[dropped subject]')
    if subject_resolution:
        subject_zh = subject_resolution.chosen
        subject_en = VOCAB.get(subject_zh, subject_zh)
        prob = subject_resolution.probability
        parts.append(SUBJECT_ANNOTATION.format(subject=subject_en, prob=prob))

    # Translate tokens
    for token in tokens:
        surface = token.surface

        # Check if this token has a polysemy resolution
        poly_res = resolutions.get(surface)
        if poly_res and poly_res.ambiguity_class == AmbiguityClass.POLYSEMY:
            # Use the resolved meaning
            meaning = poly_res.chosen.split(':')[0].strip()
            parts.append(meaning)
            continue

        # Check if this is a particle with resolution
        particle_res = resolutions.get(surface)
        if particle_res and particle_res.ambiguity_class == AmbiguityClass.PARTICLE:
            particle_use = particle_res.chosen.split(':')[0].strip()
            tone = PARTICLE_TONES.get(surface, {}).get(particle_use, '')
            parts.append(tone)
            continue

        # Standard dictionary lookup
        if surface in VOCAB:
            parts.append(VOCAB[surface])
        elif token.is_particle:
            # Known particle without specific resolution — skip or minimal
            tone = PARTICLE_TONES.get(surface, {})
            if tone:
                first_key = next(iter(tone))
                parts.append(tone[first_key])
        elif len(surface.strip()) > 0:
            # Unknown word — keep as-is with brackets
            parts.append(f'«{surface}»')

    # Join and clean up
    text = ' '.join(parts)
    # Clean up spacing around punctuation
    text = text.replace('  ', ' ').strip()

    return text


def batch_render(
    seg_msg: SegmentedMessage,
    candidates: list[TranslationCandidate],
) -> list[TranslationCandidate]:
    """Render English translations for all candidates.

    Modifies candidates in-place by setting their english_text field.

    Returns:
        The same candidates list with english_text populated.
    """
    for candidate in candidates:
        candidate.english_text = render_translation(seg_msg, candidate)
    return candidates
