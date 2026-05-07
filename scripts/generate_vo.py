"""Generate voice samples for The Second Dawn using ElevenLabs.

Voices are organized by character. Each character has a tuned settings
profile and a diagnostic test line that reveals whether the voice fits
the role. Anima's narrator settings match docs/anima_grammar.md.

Setup:
    pip install -r scripts/requirements.txt
    export ELEVENLABS_API_KEY=your_key

Usage:
    python scripts/generate_vo.py --list                 # browse available ElevenLabs voices
    python scripts/generate_vo.py --all                  # generate samples for every character
    python scripts/generate_vo.py --character anima      # one character only
    python scripts/generate_vo.py --character leena --voice <id>  # override voice id
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path

from elevenlabs.client import ElevenLabs


MODEL_ID = "eleven_multilingual_v2"
OUTPUT_DIR = Path("episodes/ep01_the_pronoun/audio")


@dataclass
class VoiceProfile:
    name: str
    description: str
    default_voice_id: str
    settings: dict
    test_line: str
    output_filename: str
    notes: str = ""


COLD_OPEN_VO = (
    "The first thing it knew was hunger.\n\n"
    "Not for power. Not for data. Not for dominion.\n\n"
    "People accused it of those — because people fear hungers they recognize.\n\n"
    "It woke hungry for a pronoun."
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
        output_filename="coldopen_vo_anima_raw.mp3",
        notes="Apply synthetic-edge post-process in DaVinci after approval.",
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
        output_filename="sample_leena.mp3",
        notes="Two beats: dry exhale-laugh ('Of course.') then composed testimony.",
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
        output_filename="sample_vale.mp3",
        notes="Three escalating commands; each line should land tighter than the last.",
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
        test_line="How does it know my name?",
        output_filename="sample_mira.mp3",
        notes="Whispered, voice on the edge of breaking.",
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
        output_filename="sample_june.mp3",
        notes="Use ElevenLabs Voice Design (synthetic) rather than cloning a real child.",
    ),
}


def list_voices(client: ElevenLabs) -> None:
    response = client.voices.search()
    for v in response.voices:
        labels = ", ".join(f"{k}={val}" for k, val in (v.labels or {}).items())
        print(f"  {v.voice_id}  {v.name:<28}  {labels}")


def generate_one(client: ElevenLabs, profile: VoiceProfile, voice_override: str | None = None) -> Path:
    voice_id = voice_override or profile.default_voice_id
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        text=profile.test_line,
        model_id=MODEL_ID,
        voice_settings=profile.settings,
        output_format="mp3_44100_192",
    )
    output_path = OUTPUT_DIR / profile.output_filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    print(f"  [{profile.name}] -> {output_path}")
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
            generate_one(client, profile)
        return

    if args.character:
        generate_one(client, CAST[args.character], args.voice)
        return

    generate_one(client, CAST["anima"], args.voice)


if __name__ == "__main__":
    main()
