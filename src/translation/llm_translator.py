"""Optional LLM-assisted translation renderer.

Uses Claude API to generate fluent English translations, constrained
by the Bayesian engine's ambiguity resolutions. The LLM does not make
linguistic decisions — those are made by the Bayesian engine. The LLM
only renders the resolved interpretation into natural English.

This module is optional. If the anthropic package is not installed,
the system falls back to rule-based translation only.
"""

from __future__ import annotations

from src.models import (
    AmbiguityClass,
    AmbiguityResolution,
    SegmentedMessage,
    TranslationCandidate,
)

LLM_AVAILABLE = False
try:
    import anthropic
    LLM_AVAILABLE = True
except ImportError:
    pass


SYSTEM_PROMPT = """You are a precise Chinese-to-English translator. You will receive:
1. A Traditional Chinese sentence
2. Specific disambiguation constraints (dropped subjects, word meanings, particle interpretations)

Your job is to render natural, fluent English that EXACTLY reflects the given constraints.
Do NOT re-interpret or override the constraints. If the constraint says the dropped subject
is "I", translate with "I" — even if you might choose differently.

Output ONLY the English translation. No explanations, no alternatives."""


def build_constraint_text(resolutions: list[AmbiguityResolution]) -> str:
    """Build a constraint description from ambiguity resolutions."""
    constraints = []
    for r in resolutions:
        if r.ambiguity_class == AmbiguityClass.PRODROP:
            constraints.append(
                f"- Dropped subject resolved to: {r.chosen} (confidence: {r.probability:.0%})"
            )
        elif r.ambiguity_class == AmbiguityClass.POLYSEMY:
            constraints.append(
                f"- Word '{r.span}' means: {r.chosen}"
            )
        elif r.ambiguity_class == AmbiguityClass.PARTICLE:
            constraints.append(
                f"- Particle '{r.span}' functions as: {r.chosen}"
            )
        elif r.ambiguity_class == AmbiguityClass.REFERENT:
            constraints.append(
                f"- '{r.span}' refers to: {r.chosen}"
            )
    return '\n'.join(constraints) if constraints else "No specific constraints."


def translate_with_llm(
    seg_msg: SegmentedMessage,
    candidate: TranslationCandidate,
    context_before: str = "",
    context_after: str = "",
) -> str | None:
    """Generate a fluent English translation using Claude API.

    Args:
        seg_msg: The segmented Chinese message.
        candidate: Translation candidate with resolved ambiguities.
        context_before: Previous messages for discourse context.
        context_after: Following messages for discourse context.

    Returns:
        Fluent English translation string, or None if LLM unavailable.
    """
    if not LLM_AVAILABLE:
        return None

    chinese_text = seg_msg.message.raw_text
    constraints = build_constraint_text(candidate.resolutions)

    user_message = f"""Chinese sentence: {chinese_text}

Disambiguation constraints:
{constraints}"""

    if context_before:
        user_message += f"\n\nPreceding conversation context:\n{context_before}"

    try:
        client = anthropic.Anthropic()
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=256,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_message}],
        )
        return response.content[0].text.strip()
    except Exception:
        return None


def batch_translate_with_llm(
    seg_msg: SegmentedMessage,
    candidates: list[TranslationCandidate],
    context_before: str = "",
) -> list[TranslationCandidate]:
    """Enhance candidates with LLM translations where possible.

    Only translates the top candidate to minimize API calls.
    Falls back to rule-based translation if LLM is unavailable.

    Returns:
        Candidates with english_text populated (LLM for top, rule-based for rest).
    """
    if not LLM_AVAILABLE or not candidates:
        return candidates

    # Only use LLM for the top candidate
    top = candidates[0]
    llm_text = translate_with_llm(seg_msg, top, context_before)
    if llm_text:
        top.english_text = llm_text

    return candidates
