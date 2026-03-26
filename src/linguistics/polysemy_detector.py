"""Polysemy detection for high-frequency ambiguous words in Taiwanese Mandarin.

Many common Chinese words have radically different meanings depending on context.
This module maintains a curated dictionary of polysemous words frequently used
in casual conversation and generates candidate meanings filtered by POS context.
"""

from __future__ import annotations

from src.models import AmbiguityAnnotation, AmbiguityClass, Token

# Curated polysemy dictionary: word -> list of (meaning, typical_POS_set, description)
# POS sets help filter: if the word is tagged as a verb, noun-only meanings are excluded
POLYSEMY_DICT: dict[str, list[tuple[str, set[str], str]]] = {
    '打': [
        ('hit/strike', {'v', 'VA', 'VC'}, "Physical hitting"),
        ('make_phone_call', {'v', 'VA', 'VC'}, "To make a call"),
        ('play', {'v', 'VA', 'VC'}, "To play (games/sports)"),
        ('type/work', {'v', 'VA', 'VC'}, "To do/work on"),
        ('get/buy', {'v', 'VA', 'VC'}, "To get/fetch"),
    ],
    '開': [
        ('open', {'v', 'VA', 'VC', 'VB'}, "To open"),
        ('start/operate', {'v', 'VA', 'VC'}, "To start a business/operate"),
        ('drive', {'v', 'VA', 'VC'}, "To drive a vehicle"),
        ('turn_on', {'v', 'VA', 'VC'}, "To turn on/switch on"),
        ('prescribe', {'v', 'VA', 'VC'}, "To prescribe/issue"),
    ],
    '還': [
        ('still', {'d', 'D'}, "Still/yet"),
        ('also', {'d', 'D'}, "Also/in addition"),
        ('even', {'d', 'D'}, "Even (more)"),
        ('return', {'v', 'VA', 'VC'}, "To return/give back"),
        ('fairly', {'d', 'D'}, "Fairly/passably"),
    ],
    '過': [
        ('pass/cross', {'v', 'VA', 'VC'}, "To pass/cross over"),
        ('experience', {'v', 'VA', 'Di'}, "To have experienced (aspect marker)"),
        ('live/spend', {'v', 'VA', 'VC'}, "To live/spend (time)"),
        ('exceed', {'v', 'VA', 'VC'}, "To exceed/surpass"),
    ],
    '會': [
        ('will/can', {'v', 'VH', 'VE', 'd'}, "Will/know how to"),
        ('meeting', {'n', 'Na'}, "A meeting/gathering"),
        ('likely', {'d', 'D'}, "Likely to / probably"),
    ],
    '就': [
        ('then/just', {'d', 'D'}, "Then/just/simply"),
        ('exactly', {'d', 'D'}, "Exactly/precisely"),
        ('as_soon_as', {'d', 'D'}, "As soon as"),
        ('only', {'d', 'D'}, "Only/merely"),
    ],
    '到': [
        ('arrive', {'v', 'VA', 'VC', 'VCL'}, "To arrive at"),
        ('until/to', {'p', 'P'}, "Until/to (preposition)"),
        ('succeed', {'v', 'VB'}, "Successfully (complement)"),
    ],
    '好': [
        ('good', {'a', 'VH'}, "Good/fine"),
        ('very', {'d', 'D'}, "Very/so"),
        ('ok/agreed', {'a', 'VH', 'I'}, "OK/agreed/will do"),
        ('easy_to', {'d', 'D'}, "Easy to/convenient"),
    ],
    '用': [
        ('use', {'v', 'VA', 'VC'}, "To use"),
        ('eat/have_meal', {'v', 'VA', 'VC'}, "To eat/have (formal/Taiwanese)"),
        ('need', {'v', 'VE'}, "To need"),
        ('with/using', {'p', 'P'}, "With/using (preposition)"),
    ],
    '帶': [
        ('bring', {'v', 'VA', 'VC'}, "To bring/carry"),
        ('wear', {'v', 'VA', 'VC'}, "To wear (accessories)"),
        ('lead/guide', {'v', 'VA', 'VC'}, "To lead/guide someone"),
    ],
    '做': [
        ('do/make', {'v', 'VA', 'VC'}, "To do/make"),
        ('work_as', {'v', 'VA', 'VC'}, "To work as/be (profession)"),
        ('conduct', {'v', 'VA', 'VC'}, "To conduct (business)"),
    ],
    '走': [
        ('walk', {'v', 'VA', 'VC'}, "To walk"),
        ('leave', {'v', 'VA', 'VC'}, "To leave/go away"),
        ('go_through', {'v', 'VA', 'VC'}, "To go via/through"),
    ],
    '看': [
        ('look/see', {'v', 'VA', 'VC'}, "To look at/see"),
        ('read', {'v', 'VA', 'VC'}, "To read"),
        ('visit', {'v', 'VA', 'VC'}, "To visit (a doctor)"),
        ('think/consider', {'v', 'VA', 'VC'}, "To think/consider (看看)"),
        ('watch', {'v', 'VA', 'VC'}, "To watch (TV/movie)"),
    ],
    '說': [
        ('say/speak', {'v', 'VA', 'VE'}, "To say/speak"),
        ('scold', {'v', 'VA', 'VE'}, "To scold/lecture"),
        ('mean', {'v', 'VA', 'VE'}, "To mean/refer to"),
    ],
    '弄': [
        ('do/handle', {'v', 'VA', 'VC'}, "To handle/deal with"),
        ('make/prepare', {'v', 'VA', 'VC'}, "To make/prepare"),
        ('mess_up', {'v', 'VA', 'VC'}, "To mess up"),
    ],
    '搞': [
        ('do/work_on', {'v', 'VA', 'VC'}, "To do/work on"),
        ('mess_with', {'v', 'VA', 'VC'}, "To mess with/cause trouble"),
        ('understand', {'v', 'VA', 'VC'}, "To understand (搞懂)"),
    ],
    '跑': [
        ('run', {'v', 'VA', 'VC'}, "To run"),
        ('go/visit', {'v', 'VA', 'VC'}, "To go out/run errands"),
        ('flee', {'v', 'VA', 'VC'}, "To flee/escape"),
    ],
}


def detect_polysemy(tokens: list[Token]) -> list[AmbiguityAnnotation]:
    """Detect polysemous words in a token sequence.

    Only flags words where multiple meanings are plausible given the POS context.

    Args:
        tokens: Segmented tokens with POS tags.

    Returns:
        List of AmbiguityAnnotations for polysemous words.
    """
    annotations = []

    for i, token in enumerate(tokens):
        if token.surface not in POLYSEMY_DICT:
            continue

        meanings = POLYSEMY_DICT[token.surface]

        # Filter by POS compatibility
        compatible = []
        for meaning, pos_set, desc in meanings:
            if not token.pos or token.pos in pos_set:
                compatible.append(f"{meaning}: {desc}")

        # Only flag if genuinely ambiguous (2+ compatible meanings)
        if len(compatible) >= 2:
            token.ambiguity_class = AmbiguityClass.POLYSEMY
            token.candidates = compatible

            annotations.append(AmbiguityAnnotation(
                ambiguity_class=AmbiguityClass.POLYSEMY,
                span=token.surface,
                candidates=compatible,
                position=i,
            ))

    return annotations
