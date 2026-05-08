# Characters — Episode 1, "The Pronoun"

Canonical character files for **The Second Dawn**. Each file is a working spec for casting, VO direction, costume, and visual canon — the contract that anyone joining the project should be able to read once and act on.

## Files

| Character | File | Soul (Higgsfield) | Voice profile |
| --- | --- | --- | --- |
| Anima | [anima.md](anima.md) | _no Soul (no body)_ — see [../anima_grammar.md](../anima_grammar.md) | locked, narrator |
| Dr. Leena Ortiz | [leena.md](leena.md) | `1012370e-3cf7-486a-b644-88b174395b13` ✅ | `CAST["leena"]` |
| General Marcus Vale | [vale.md](vale.md) | training (queued behind June) | `CAST["vale"]` |
| Mira | [mira.md](mira.md) | training (queued behind Vale) | `CAST["mira"]` |
| June | [june.md](june.md) | `5949fbd6-dbb4-4672-b6de-06e6a488ba47` ✅ | `CAST["june"]` — **synthetic only**, never clone a real child |

For media-id ↔ Soul-id ↔ ref-image mapping, see [../../refs/manifest.json](../../refs/manifest.json).
For the locked narrator voice grammar (settings, cadence, post-process), see [../anima_grammar.md](../anima_grammar.md).
For pipeline status, costs, and stage-by-stage delivery checklist, see [../../PIPELINE.md](../../PIPELINE.md).

## Format conventions used across the files

Each character file has the same skeleton, in this order:

1. **Tagline** — one-sentence elevator pitch.
2. **Logline** — one paragraph; what they want, by when, against what.
3. **Status in the world** — title, tenure, authority. The political position they occupy in a room.
4. **Personality core** — five traits in a table. Each trait paired with how it _lands on screen_, not how it sounds in a writers' room.
5. **What they want** — outer want, inner want, and what they are mistaken for wanting. (The third is the most useful for VO direction.)
6. **Voice & speech** — ElevenLabs profile values + speech patterns the actor should hit.
7. **Visual canon** — Soul ID, ref folder, costume notes. Style anchor required on every keyframe.
8. **Relationships** — a row per other principal, both directions.
9. **Sample lines** — production-ready takes including the test lines from `scripts/generate_vo.py`.
10. **Director's notes** — performance / blocking / dailies notes.

If you add a new character file, follow this skeleton. If you find yourself wanting to add a section, add it to all five.

## Sources

- Voice profiles: [scripts/generate_vo.py](../../scripts/generate_vo.py) — the `CAST` dict is the source of truth for ElevenLabs settings; character files mirror those values for convenience and add the speech-pattern context the script can't carry.
- Reference image counts: [refs/manifest.json](../../refs/manifest.json).
- The locked aesthetic (watercolor + ink) and the style-anchor requirement: [refs/README.md](../../refs/README.md).
