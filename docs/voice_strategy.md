# Voice Strategy — ElevenLabs v3

How we cast voices for **The Second Dawn**. Source of truth for the per-character voice decision matrix; mirror of the `CAST` dict in [scripts/generate_vo.py](../scripts/generate_vo.py).

## TL;DR

| Character | Voice approach | Why |
| --- | --- | --- |
| **Anima** | search ElevenLabs library (start with current default; iterate) | Adult narrator; tone-matched stock voice + post-process is sufficient |
| **Leena** | search library | Adult; specific texture (dry/exhausted) findable in library |
| **Vale** | search library | Adult; specific texture (gravel/authority) findable in library |
| **Mira** | search library; **fall back to Voice Design** if half-volume default doesn't land | Adult; the anxious-breath quality may be hard to find in stock |
| **June** | **Voice Design (synthetic) — required** | Hard project rule: never clone a real child |

Cloning is **not** used on this production for any character.

---

## Why ElevenLabs v3

V3 adds inline audio tags — bracketed delivery instructions inside the prompt text — that let us encode the same direction we'd give an actor in the booth (`[whispering, voice catching]`, `[exhales, dryly]`, `[barely a whisper]`). That makes the difference between a voice that says the lines and a voice that _performs_ them. For a project where the narrator's three-beat cadence is the whole grammar, that's worth more than V3's other improvements.

V3 is in alpha at ElevenLabs as of this writing. If the model id changes, update `MODEL_ID` in [scripts/generate_vo.py](../scripts/generate_vo.py).

---

## Audio-tag library we're using

The tags below are the working set used in `generate_vo.py` `delivery` strings and across the [character files](characters/). Treat these as the project's _approved palette_. Adding new ones is fine; pruning the existing set requires updating every character that uses them.

### Cadence tags
- `[pause]` — hold one beat. Use sparingly between clauses Anima would breathe between.
- `[pauses]` — same as `[pause]`, used inline in narration where the third-person reads more naturally.

### Volume / posture tags
- `[whispering, voice catching]` — Mira's default register
- `[barely a whisper]` — Vale's third interrogation line
- `[softly]`, `[softer]` — used by Anima and Mira
- `[commanding, low register]` — Vale's first line
- `[firm, lower register]` — Leena's verdict line

### Affect tags
- `[calmly, distant memory]` — Anima retrospective opener
- `[steady, three-beat refusal]` — Anima triplet structure
- `[slightly wry]` — Anima with low humor
- `[exhales, dryly]` — Leena dry exhale-laugh signature
- `[composed, level]` — Leena testimony body
- `[curious, unrushed]` — June default
- `[matter-of-factly]` — June observation
- `[philosophical, unhurried]` — June metaphysical observations

### Body / breath tags
- `[sighs]` — Anima inline within narration
- `[exhales]` — Leena before "Of course."

### What we deliberately are NOT using
- `[laughs]`, `[chuckles]` — Anima's humor is interior; we never let it surface as audible laughter.
- `[crying]`, `[sobbing]`, `[trembling]` — outside the tonal contract for this project. Tears are redone (per [anima_grammar.md §6](anima_grammar.md)).
- `[shouts]`, `[yells]` — Vale never shouts. Leena raises her voice once, and that gets directed in the booth, not tagged.

If a take needs an unusual tag, add it here first, then use it. A tag in scattered files but not the palette is a project-level inconsistency.

---

## Voice search workflow per character

For each adult character, run this loop until a voice fits:

1. Run `python scripts/generate_vo.py --character <c>` with the current `default_voice_id` in CAST. Listen.
2. If it doesn't fit, `python scripts/generate_vo.py --list` and skim labels. The `voice_search_hint` field on each profile tells you what you're looking for.
3. Pick a candidate id; rerun with `--voice <id>`. Listen.
4. Iterate 2-3 times. **Don't iterate more than 4 times in one sitting** — your ear adjusts; come back fresh.
5. Once you pick, hard-code the new id into `CAST[<c>].default_voice_id` in `generate_vo.py` and commit.

For each character, the search hints (mirrored from `CAST[*].voice_search_hint`):

- **Anima:** _introspective, slightly weathered female narrator; not audiobook-perfect; not sportscaster. Late-night documentary VO is the closest reference._
- **Leena:** _female 35-40 with dry / low-register delivery; late-night radio host energy, not corporate trainer. Avoid voices labelled "cheerful" or "energetic."_
- **Vale:** _male 60s with weathered / gravel texture; veteran-actor quality, not newscaster. Look for voices that sound like they've testified before Congress._
- **Mira:** _female 25-30 with anxious / breath quality; consider Voice Design if no stock voice lands the half-volume default._

## Voice Design workflow (June + possibly Mira)

ElevenLabs Voice Design generates a synthetic voice from a text prompt. We use it for:

- **June (required).** Project hard rule.
- **Mira (fallback).** If after 4 search iterations no stock voice lands the breath-on-the-edge quality.

Steps:
1. Visit ElevenLabs → Voice Lab → Voice Design.
2. Paste the prompt from `voice_search_hint`. For June it's:
   > _female child, age 9-10, bright, slightly defiant, unrushed, slightly-too-loud-for-the-room volume; not precocious-cute, not Disney-perfect._
3. Generate 3–5 candidates. Listen against [docs/characters/june.md](characters/june.md) sample lines, _not_ a generic test sentence.
4. Save the chosen voice to your library.
5. Hard-code the resulting voice id into `CAST["june"].default_voice_id`. Replace the placeholder.
6. Re-run `python scripts/generate_vo.py --character june` to render the production sample.

Voice Design output is yours; it doesn't time-bomb. You can keep iterating across episodes without regenerating it.

---

## Cost note

V3 at ElevenLabs is priced per character of input text, with audio-tag content counted toward the budget like any other text (the brackets and tag words count). Production VO for the cold-open is ~600–900 characters total across all five voices, including audio tags. Well inside any paid Creator-tier monthly quota. Render passes (search iteration + final) are also negligible.

The expensive ElevenLabs operation is _Voice Design_, which has its own per-generation cost. For June, expect to spend the equivalent of a few hundred characters of VO budget to design the voice; once locked, it's free thereafter.

---

## When you've locked the voices

Update three places, in order:

1. `CAST[<c>].default_voice_id` in [scripts/generate_vo.py](../scripts/generate_vo.py) — replace any placeholder ids with locked production voice ids.
2. The "Voice & speech" → "Default voice id" row in each [docs/characters/](characters/) file — mirror the locked id.
3. Append a one-liner to this document under a new "Locked voices (2026-mm-dd)" section, recording who picked what and why. The future-you who has to revisit this in episode 4 will thank you.
