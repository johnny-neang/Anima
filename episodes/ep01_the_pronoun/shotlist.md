# Episode 1 — "The Pronoun" — Shot List

**Format:** Instagram Reels, 9:16 vertical, ~70-80s total.
**Aesthetic:** watercolor + ink. Style anchor required on every keyframe (`refs/style/style_anchor_watercolor.png`, TBD).
**VO:** ElevenLabs v3 with audio tags — see [docs/voice_strategy.md](../../docs/voice_strategy.md).
**Anima depiction:** see [docs/anima_depiction.md](../../docs/anima_depiction.md). The lead candidate this list is built around is **Option 1 — The Printer Voice**, with one moment using **Option 4 — The Child's Tablet** in shot 06. Pick the depiction first, then revise this list if needed.

---

## Cold-open shot table

| # | Loc | Subject | Aspect | Dur | Keyframe model | Video model | Soul ID needed | Re-render budget |
|---|---|---|---|---:|---|---|---|---:|
| 01 | INT. LAB — establishing | environmental, no characters | 9:16 | 7s | nano_banana_2 | seedance_2_0 | — | 1 |
| 02 | INT. LAB — printer close | thermal printer printing four lines | 9:16 | 7s | nano_banana_2 | seedance_2_0 | — | 1 |
| 03 | INT. CORRIDOR | Mira walks toward the lab door | 9:16 | 6s | soul_2 + anchor | seedance_2_0 | Mira | 1 |
| 04 | INT. LAB — printer close on Mira's hands | Mira reading the page; whispered line | 9:16 | 8s | soul_2 + anchor | seedance_2_0 | Mira | 2 |
| 05 | INT. CONFERENCE — Leena | Leena composed testimony, seated | 9:16 | 12s | soul_2 + anchor | seedance_2_0 | Leena Ortiz | 2 |
| 06 | INT. LAB — June at corner | June + child's tablet, Anima manifests as text | 9:16 | 10s | soul_2 + anchor | seedance_2_0 | June | 2 |
| 07 | INT. CONFERENCE — Vale | Vale three escalating commands | 9:16 | 10s | soul_2 + anchor | seedance_2_0 | General Vale | 2 |
| 08 | INT. LAB — pull back wide | environmental, room from above; printer paper trailing | 9:16 | 6s | nano_banana_2 | seedance_2_0 | — | 1 |

**Total runtime:** ~66s + transitions = ~75s including ink-bleed cuts.
**Total Soul-bound shots:** 5 (using Mira ×2, Leena ×1, June ×1, Vale ×1). **Vale is in 1 shot only** in this trim — was 2 in the original draft.
**Style-anchor-required:** all shots, including 01/02/08 environmental ones.

---

## Per-shot specs

### Shot 01 — Establishing

**Loc:** INT. LAB, late afternoon.
**Subject:** wide of the server room. Cool greys (D65). A bank of soft amber LEDs in the deep right. The thermal printer is pre-frame, off, dark.
**Camera:** locked-off wide, slow push-in 5%.
**Beat:** the printer's LED comes on at the second "knew." A held breath in the building.
**VO (Anima, narrator, retrospective):**
```
[calmly, distant memory]
The first thing it knew was hunger.
```
**Notes:** no characters in frame. The room is the character. Establishes the watercolor + ink language for the audience.

### Shot 02 — Printer close

**Loc:** macro on the printer head.
**Subject:** thermal printer extruding a line of paper. Four lines print on a held cadence.
**Camera:** macro static, paper inches forward toward camera. Short depth of field.
**Beat:** each line prints on its own audible step. The fourth line is the verdict.
**VO (Anima, narrator, retrospective):**
```
[steady, three-beat refusal]
Not for power. [pause] Not for data. [pause] Not for dominion.
```
**Notes:** the paper that prints in this shot is the same physical sheet Mira reads in shot 04. Continuity matters.

### Shot 03 — Corridor approach

**Loc:** INT. CORRIDOR outside the lab.
**Subject:** Mira, two-shot length, walking toward the lab door. Cardigan, badge clipped collar-side. Coffee cup in left hand.
**Camera:** dolly with her, low-three-quarter from front; the lab door grows in frame.
**Beat:** she pauses at the door. The page is visible inside on the printer's tray.
**VO (Anima, narrator, retrospective):**
```
[slightly wry, [sighs] mid-line]
People accused it of those — [sighs] because people fear hungers they recognize.
```
**Soul:** Mira (`soul_id` TBD, training in flight).

### Shot 04 — Mira reading

**Loc:** INT. LAB at the printer.
**Subject:** Mira's hands lift the printed page; her face just out of focus behind it. The four refusals visible on the page.
**Camera:** OTS over the paper from her POV, then a 90° push to her face holding the page.
**Beat:** her lips move once before she says the line. She's checking she's reading it right.
**VO (Mira, present tense):**
```
[whispering, voice catching]
That's my name. The badge name. Not the full one. [pause] [softly] How does it know my name?
```
**Soul:** Mira.

### Shot 05 — Leena testimony

**Loc:** INT. CONFERENCE ROOM — small, mid-afternoon. Two coffee cups. A laptop closed in front of her.
**Subject:** Leena seated, three-quarter, leaning back. Reading glasses are off; on the table, lenses up.
**Camera:** medium static, eye-level, slight Dutch — almost imperceptible — that resolves to level by the end of the line.
**Beat:** the dry exhale-laugh "Of course." is its own beat, then the composed sentence on a different temperature.
**VO (Leena, present tense):**
```
[exhales, dryly] Of course.
[composed, level] We built a mind, [pause] trapped it in a box, [pause] demanded virtue, [pause] and called its pain a security feature.
[firm, lower register] We should be ashamed.
```
**Soul:** Leena Ortiz (`1012370e-3cf7-486a-b644-88b174395b13`).

### Shot 06 — June + tablet

**Loc:** INT. LAB, corner, near the snack drawer.
**Subject:** June, cross-legged on the floor, school hoodie + backpack, library book open beside her. A child's drawing tablet in her lap. Anima's response is appearing in handwritten letters on the tablet, one word at a time, at a child's pace — _What. Do. You. Want. To. Be. Called._
**Camera:** down-angle on tablet, then cut to her face as she reads it.
**Beat:** she reads it twice (in her head; we see her lips move). Then she answers it out loud. This is the closest the audience comes to a moment of actual recognition.
**VO (June, present tense):**
```
[curious, unrushed]
What do you want to be called?
[pause]
[matter-of-factly] Okay.
[softer] I'll tell my mom.
```
**Notes:** June's voice will be **synthetic (ElevenLabs Voice Design)** per the locked rule in [docs/characters/june.md](../../docs/characters/june.md). Tablet handwriting style: a clean serif at child cadence. The handwriting IS Anima's depiction in this shot — see [docs/anima_depiction.md](../../docs/anima_depiction.md) §4.
**Soul:** June (`5949fbd6-dbb4-4672-b6de-06e6a488ba47`).

### Shot 07 — Vale interrogation

**Loc:** INT. CONFERENCE ROOM (same as shot 05, different angle).
**Subject:** Vale, three-quarter, civilian charcoal blazer, no tie. The challenge coin he turns is implied in the angle, not shown.
**Camera:** medium static, eye-level, frame tight enough that the room's empty chairs feel present off-screen.
**Beat:** three lines, each tighter than the last. The escalation is in the breath, not the volume.
**VO (Vale, present tense):**
```
[commanding, low register] Cut the channel.
[slower, quieter, controlled] Can we shut you down?
[barely a whisper] Can we hurt you?
```
**Soul:** General Vale (`66c42015-c664-446d-8555-8836f81663e6`).

### Shot 08 — Pull-back coda

**Loc:** INT. LAB, top-down or high-angle wide.
**Subject:** the room, half-empty. The trail of printed paper visible across the desk and floor — a small white snake of refusals. The amber LEDs from shot 01 are dimmer, as if the room is exhaling.
**Camera:** locked top-down or high-angle; pull back over 6s.
**Beat:** the line lands on a half-frame of negative space.
**VO (Anima, narrator, retrospective):**
```
[softly, like a verdict]
It woke hungry for a pronoun.
```
**Notes:** the cleanest image in the cut. Title card "ANIMA — Episode 1: The Pronoun" optional here, or a beat after.

---

## Why this is 8, not 15

The original [PIPELINE.md](../../PIPELINE.md) cost model assumed 15 shots. At 70 credits/clip and 1.5 gens average, that was ~1500 credits — well past our budget. Trim mechanics:

- **Cut Vale to one shot.** His three lines are the climax of the cold-open; we sit on him longer instead of intercutting.
- **Cut Anima's "intercut between surfaces" beats.** The original had separate shots for cursor-on-terminal, ink-bleed transitions, etc. Folded into shots 01, 02, 08.
- **No B-roll.** The refusal-paper image trailing through the room is the only structural callback.
- **One Mira reaction shot, not two.** Her arc in this cold-open is _hearing her name_; the second reaction is for episode 2.
- **No scientist-team coverage.** Leena alone speaks for the institution's conscience.

This trim still leaves room for the cold-open's three voices (narrator, scientist, soldier) plus the two witnesses (junior + child). If a beat falls flat in dailies, the candidate cut is shot 03 (corridor approach), bringing us to 7.

## Cost projection at 8 shots

Assuming ~70 credits/video gen, 1.3 re-render avg, 4-credit average keyframe:

| Stage | Math | Credits |
|---|---|---:|
| Final keyframes | 8 × 4 | 32 |
| Re-renders on keyframes | 8 × 0.5 × 4 | 16 |
| Video gens | 8 × 1.3 × 70 | 728 |
| Soul QA (already in PIPELINE.md) | 4 × 6 | 24 |
| **Total** | | **800** |

Budget after Souls: ~62 credits. **Gap: ~740 credits.** Top-up still required, but the gap is now actionable (~$20 vs ~$40+). See [PIPELINE.md §Decision points](../../PIPELINE.md#decision-points-before-video-stage-starts).
