"""Pragmatic particle analysis for Mandarin Chinese.

Sentence-final particles carry pragmatic meaning that changes the entire
interpretation of a sentence. The same words with different particles
can be a suggestion, a command, a question, or a concession.

This module classifies particle usage and generates candidate
pragmatic interpretations.
"""

from __future__ import annotations

from src.models import AmbiguityAnnotation, AmbiguityClass, Token

# Particle interpretation candidates by surface form
PARTICLE_INTERPRETATIONS: dict[str, list[tuple[str, str]]] = {
    '吧': [
        ('suggestion', "Let's... / How about..."),
        ('concession', "Fine, go ahead / I suppose so"),
        ('uncertainty', "I think so / probably"),
        ('softened_command', "You should... (softened)"),
    ],
    '啊': [
        ('exclamation', "Wow / emphasis"),
        ('filler', "Softening / conversational filler"),
        ('realization', "Oh! / I see"),
        ('urging', "Come on / hurry up"),
    ],
    '嘛': [
        ('obviously', "Of course / it's obvious"),
        ('mild_reproach', "You should know this"),
        ('explanation', "Because... / the thing is..."),
    ],
    '呢': [
        ('reciprocal_question', "What about...? / And you?"),
        ('continuation', "Still... / ongoing"),
        ('emphasis', "Indeed / really"),
    ],
    '了': [
        ('completed_action', "Action completed / done"),
        ('change_of_state', "Now... / things have changed"),
        ('excessive', "Too much / overly"),
    ],
    '喔': [
        ('acknowledgment', "Oh, I see"),
        ('mild_surprise', "Oh really?"),
        ('reminder', "Don't forget / by the way"),
    ],
    '啦': [
        ('reassurance', "Don't worry / it's fine"),
        ('impatience', "Come on already"),
        ('emphasis', "Really / for sure"),
    ],
    '嗎': [
        ('yes_no_question', "Is it? / Did you?"),
        ('rhetorical', "Isn't it obvious?"),
    ],
    '哦': [
        ('acknowledgment', "Oh, OK"),
        ('mild_surprise', "Oh?"),
    ],
}


def analyze_particles(tokens: list[Token]) -> list[AmbiguityAnnotation]:
    """Identify sentence-final particles and generate interpretation candidates.

    Only flags particles that have multiple valid pragmatic readings.
    Single-interpretation particles (like 嗎 in a clear question) are not flagged.

    Args:
        tokens: Segmented tokens of the Chinese message.

    Returns:
        List of AmbiguityAnnotations for ambiguous particles.
    """
    annotations = []

    if not tokens:
        return annotations

    # Check the last few tokens for sentence-final particles
    # (particles can appear at position -1 or -2 if punctuation follows)
    check_positions = []
    for i in range(len(tokens) - 1, max(len(tokens) - 3, -1), -1):
        if i >= 0:
            check_positions.append(i)

    for pos in check_positions:
        token = tokens[pos]
        surface = token.surface

        if surface in PARTICLE_INTERPRETATIONS:
            interps = PARTICLE_INTERPRETATIONS[surface]

            # Only flag if genuinely ambiguous (2+ interpretations)
            if len(interps) >= 2:
                candidates = [f"{label}: {desc}" for label, desc in interps]
                annotations.append(AmbiguityAnnotation(
                    ambiguity_class=AmbiguityClass.PARTICLE,
                    span=surface,
                    candidates=candidates,
                    position=pos,
                ))

            # Mark the token
            token.ambiguity_class = AmbiguityClass.PARTICLE
            token.candidates = [label for label, _ in interps]
            break  # Only the final particle matters most

    return annotations
