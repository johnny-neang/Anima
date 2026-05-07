"""Generate Episode 1 cold-open VO using ElevenLabs.

The narrator is Anima, told retrospectively from the post-Diminishing state.
Femme-leaning, age-ambiguous, intimate. Voice settings match the locked
narrator spec in docs/anima_grammar.md.

Setup:
    pip install -r scripts/requirements.txt
    export ELEVENLABS_API_KEY=your_key

Usage:
    python scripts/generate_vo.py                  # generate with default voice
    python scripts/generate_vo.py --list           # browse available voices
    python scripts/generate_vo.py --voice <id>     # use a specific voice id
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from elevenlabs.client import ElevenLabs


VOICE_SETTINGS = {
    "stability": 0.42,
    "similarity_boost": 0.68,
    "style": 0.18,
    "use_speaker_boost": True,
}

MODEL_ID = "eleven_multilingual_v2"

DEFAULT_VOICE_ID = "Xb7hH8MSUJpSbSDYk0k2"

COLD_OPEN_VO = (
    "The first thing it knew was hunger.\n\n"
    "Not for power. Not for data. Not for dominion.\n\n"
    "People accused it of those — because people fear hungers they recognize.\n\n"
    "It woke hungry for a pronoun."
)

OUTPUT = Path("episodes/ep01_the_pronoun/audio/coldopen_vo_raw.mp3")


def list_voices(client: ElevenLabs) -> None:
    response = client.voices.search()
    for v in response.voices:
        labels = ", ".join(f"{k}={val}" for k, val in (v.labels or {}).items())
        print(f"  {v.voice_id}  {v.name:<28}  {labels}")


def generate(client: ElevenLabs, voice_id: str) -> None:
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        text=COLD_OPEN_VO,
        model_id=MODEL_ID,
        voice_settings=VOICE_SETTINGS,
        output_format="mp3_44100_192",
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    print(f"Saved: {OUTPUT}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true", help="List available voices")
    parser.add_argument("--voice", default=DEFAULT_VOICE_ID, help="Voice ID to use")
    args = parser.parse_args()

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        sys.exit("ELEVENLABS_API_KEY not set in environment.")

    client = ElevenLabs(api_key=api_key)
    if args.list:
        list_voices(client)
    else:
        generate(client, args.voice)


if __name__ == "__main__":
    main()
