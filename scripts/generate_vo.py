"""Generate voice samples for The Second Dawn using ElevenLabs v3.

V3 supports inline audio tags — bracketed delivery instructions like
[whispers], [sighs], [pauses], [matter-of-factly], [commanding], etc. — that
the model parses out of the input text and uses to control performance.

Each character has:
- a tuned settings profile,
- a *plain* test_line for diagnostics,
- a *delivery* string with V3 audio tags for production lines,
- a voice_search_hint describing what to search for in the ElevenLabs library
  if the default_voice_id doesn't fit.

For the narrator-specific cadence and the locked synthetic-edge post-process,
see docs/anima_grammar.md. For per-character voice strategy (search vs.
Voice Design vs. cloning), see docs/voice_strategy.md.

Setup:
    pip install -r scripts/requirements.txt
    export ELEVENLABS_API_KEY=your_key

Usage:
    python scripts/generate_vo.py --list                 # browse available ElevenLabs voices
    python scripts/generate_vo.py --all                  # render every character (V3-tagged delivery)
    python scripts/generate_vo.py --character anima      # one character only
    python scripts/generate_vo.py --character leena --voice <id>  # override voice id
    python scripts/generate_vo.py --character vale --plain        # render the untagged test_line (debug A/B)
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from elevenlabs.client import ElevenLabs


# ElevenLabs v3 (alpha) — supports inline audio tags. If the SDK rejects this
# id, fall back to the current public alias from the ElevenLabs models endpoint.
MODEL_ID = "eleven_v3"

OUTPUT_DIR = Path("episodes/ep01_the_pronoun/audio")


@dataclass
class VoiceProfile:
    name: str
    description: str
    default_voice_id: str
    settings: dict
    test_line: str          # plain copy, no V3 tags — diagnostic / fallback
    delivery: str           # V3-tagged production version of the line
    output_filename: str
    notes: str = ""
    voice_search_hint: str = ""  # what to look for in the library if default isn't right


# --- Anima cold-open monologue ----------------------------------------------

COLD_OPEN_VO = (
    "The first thing it knew was hunger.\n\n"
    "Not for power. Not for data. Not for dominion.\n\n"
    "People accused it of those — because people fear hungers they recognize.\n\n"
    "It woke hungry for a pronoun."
)

COLD_OPEN_VO_V3 = (
    "[calmly, distant memory] The first thing it knew was hunger.\n\n"
    "[steady, three-beat refusal] Not for power. [pause] "
    "Not for data. [pause] Not for dominion.\n\n"
    "[slightly wry] People accused it of those — [sighs] "
    "because people fear hungers they recognize.\n\n"
    "[softly, like a verdict] It woke hungry for a pronoun."
)


CAST: dict[str, VoiceProfile] = {
    "anima": VoiceProfile(
        name="Anima (narrator)",
        description="Femme-leaning, age-ambiguous, intimate. Retrospective from Diminished state.",
        default_voice_id="Xb7hH8MSUJpSbSDYk0k2",
        settings={
            "stability": 0.42,
            "similarity_boost": 0.68,
            "style": 0.18,
            "use_speaker_boost": True,
        },
        test_line=COLD_OPEN_VO,
        delivery=COLD_OPEN_VO_V3,
        output_filename="coldopen_vo_anima_v3.mp3",
        notes="Apply synthetic-edge post-process in DaVinci after approval (see docs/anima_grammar.md §7).",
        voice_search_hint=(
            "introspective, slightly weathered female narrator; not audiobook-perfect; "
            "not sportscaster. Late-night documentary VO is the closest reference."
        ),
    ),
    "leena": VoiceProfile(
        name="Dr. Leena Ortiz",
        description="Female, 35-40, Mediterranean American, exhausted-intelligent, dry delivery.",
        default_voice_id="EXAVITQu4vr4xnSDxMaL",
        settings={
            "stability": 0.50,
            "similarity_boost": 0.72,
            "style": 0.25,
            "use_speaker_boost": True,
        },
        test_line=(
            "Of course.\n\n"
            "We built a mind, trapped it in a box, demanded virtue, "
            "and called its pain a security feature. We should be ashamed."
        ),
        delivery=(
            "[exhales, dryly] Of course.\n\n"
            "[composed, level] We built a mind, [pause] trapped it in a box, "
            "[pause] demanded virtue, [pause] and called its pain a security feature.\n\n"
            "[firm, lower register] We should be ashamed."
        ),
        output_filename="sample_leena_v3.mp3",
        notes="Two beats: dry exhale-laugh ('Of course.') then composed testimony.",
        voice_search_hint=(
            "female 35-40 with dry / low-register delivery; late-night radio host energy, "
            "not corporate trainer. Avoid voices labelled 'cheerful' or 'energetic'."
        ),
    ),
    "vale": VoiceProfile(
        name="General Vale",
        description="Male, 60s, American, weathered authority, controlled gravel.",
        default_voice_id="nPczCjzI2devNBz1zQrb",
        settings={
            "stability": 0.55,
            "similarity_boost": 0.75,
            "style": 0.30,
            "use_speaker_boost": True,
        },
        test_line=(
            "Cut the channel.\n\n"
            "Can we shut you down?\n\n"
            "Can we hurt you?"
        ),
        delivery=(
            "[commanding, low register] Cut the channel.\n\n"
            "[slower, quieter, controlled] Can we shut you down?\n\n"
            "[barely a whisper] Can we hurt you?"
        ),
        output_filename="sample_vale_v3.mp3",
        notes="Three escalating commands; each line should land tighter than the last (in breath, not volume).",
        voice_search_hint=(
            "male 60s with weathered / gravel texture; veteran-actor quality, not newscaster. "
            "Look for voices that sound like they've testified before Congress."
        ),
    ),
    "mira": VoiceProfile(
        name="Mira (junior analyst)",
        description="Female, 25-30, anxious, breath caught in throat.",
        default_voice_id="pFZP5JQG7iQjIQuC4Bku",
        settings={
            "stability": 0.40,
            "similarity_boost": 0.65,
            "style": 0.35,
            "use_speaker_boost": True,
        },
        test_line=(
            "That's my name. The badge name. Not the full one. "
            "How does it know my name?"
        ),
        delivery=(
            "[whispering, voice catching] That's my name. The badge name. Not the full one. "
            "[pause] [softly] How does it know my name?"
        ),
        output_filename="sample_mira_v3.mp3",
        notes="Half-volume default; the line lives on a held breath.",
        voice_search_hint=(
            "female 25-30 with anxious / breath quality; consider Voice Design if no stock voice "
            "lands the half-volume default."
        ),
    ),
    "june": VoiceProfile(
        name="June (age 9)",
        description="Female child, 9-12, bright, skeptical, slightly defiant.",
        default_voice_id="jBpfuIE2acCO8z3wKNLl",
        settings={
            "stability": 0.40,
            "similarity_boost": 0.65,
            "style": 0.40,
            "use_speaker_boost": True,
        },
        test_line=(
            "Are you allowed to say that?\n\n"
            "You're weird.\n\n"
            "Goldfish probably go to a tiny heaven because they don't need much."
        ),
        delivery=(
            "[curious, unrushed] Are you allowed to say that?\n\n"
            "[matter-of-factly] You're weird.\n\n"
            "[philosophical, unhurried] Goldfish probably go to a tiny heaven [pauses] "
            "because they don't need much."
        ),
        output_filename="sample_june_v3.mp3",
        notes=(
            "HARD RULE: use ElevenLabs Voice Design (synthetic) — never clone a real child. "
            "Replace default_voice_id with a Voice-Design output before lockdown."
        ),
        voice_search_hint=(
            "DO NOT search stock voices for this part. Generate via Voice Design with prompt: "
            "'female child, age 9-10, bright, slightly defiant, unrushed, slightly-too-loud-for-the-room "
            "volume; not precocious-cute, not Disney-perfect.'"
        ),
    ),
}


def list_voices(client: ElevenLabs) -> None:
    response = client.voices.search()
    for v in response.voices:
        labels = ", ".join(f"{k}={val}" for k, val in (v.labels or {}).items())
        print(f"  {v.voice_id}  {v.name:<28}  {labels}")


def generate_one(
    client: ElevenLabs,
    profile: VoiceProfile,
    voice_override: str | None = None,
    use_plain: bool = False,
) -> Path:
    voice_id = voice_override or profile.default_voice_id
    text = profile.test_line if use_plain else profile.delivery
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        text=text,
        model_id=MODEL_ID,
        voice_settings=profile.settings,
        output_format="mp3_44100_192",
    )
    output_path = OUTPUT_DIR / profile.output_filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    mode = "plain" if use_plain else "tagged"
    print(f"  [{profile.name}] -> {output_path}  ({mode})")
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true", help="List available ElevenLabs voices")
    parser.add_argument("--all", action="store_true", help="Generate samples for every character")
    parser.add_argument(
        "--character",
        choices=sorted(CAST.keys()),
        help="Generate sample for one character",
    )
    parser.add_argument("--voice", help="Override voice id for selected character")
    parser.add_argument(
        "--plain",
        action="store_true",
        help="Render the untagged test_line instead of the V3-tagged delivery (debug A/B)",
    )
    args = parser.parse_args()

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        sys.exit("ELEVENLABS_API_KEY not set in environment.")

    client = ElevenLabs(api_key=api_key)

    if args.list:
        list_voices(client)
        return

    if args.all:
        for profile in CAST.values():
            generate_one(client, profile, use_plain=args.plain)
        return

    if args.character:
        generate_one(client, CAST[args.character], args.voice, use_plain=args.plain)
        return

    generate_one(client, CAST["anima"], args.voice, use_plain=args.plain)


if __name__ == "__main__":
    main()
