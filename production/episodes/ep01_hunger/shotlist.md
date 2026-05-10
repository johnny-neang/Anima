# Episode 1 — _Hunger_ — Shot List

**Source script:** [script.fountain](script.fountain) (approved 2026-05-10)
**Beats:** 1.01 → 1.16 (see [series/beat_sheet.md](../../series/beat_sheet.md))
**Format:** 1.85:1, 24fps. Style anchor on every keyframe.
**Style anchor:** [lookdev/style_anchor.md](../../lookdev/style_anchor.md) — _PNG still missing; this list assumes it lands before keyframe production._

**Total shots:** 42.
**Estimated runtime:** ~20 min.
**Estimated Higgsfield cost:** ~1,940 credits (see [Cost summary](#cost-summary)).

---

## Legend

**Keyframe model:**
- `Z` = z_image (0.15 credits, look-dev probe only)
- `NB2` = nano_banana_2 (2 credits, environment / object / typography close-ups)
- `S2` = soul_2 (~5 credits, character shots with trained Soul)
- `—` = no Higgsfield keyframe needed; hand-graphic in After Effects (paper grain, watercolor wash, fountain-pen serif)

**Video model:**
- `SD` = seedance_2_0 (best for identity stability + audio-aligned timing; assume ~70 credits/5s clip until calibrated)
- `KL` = kling_3_0 (best for camera moves and motion transfer; assume ~70 credits/5s clip)
- `AE` = After Effects only — still keyframe with parallax / camera move / watercolor wet-in. **Zero Higgsfield credits.**
- `—` = no motion; held still + sound design only

**Re-render budget:** the number of accepted re-renders per shot before we revise the keyframe. Default 1; 0 for hybrid-AE shots; 2 for the riskiest shots.

---

## Shot table

| # | Beat | Loc | Subject | Dur (s) | Keyframe | Video | Soul | Anchor | Re-render | Cost (est) |
|---:|---|---|---|---:|:-:|:-:|---|:-:|---:|---:|
| 01 | 1.01 | EXT. BANGALORE | rain on glass + satellite dishes (city night) | 4 | NB2 | KL | — | ✅ | 1 | 142 |
| 02 | 1.01 | INT. HOSPITAL | bank of monitors with synced green wave | 3 | NB2 | KL | — | ✅ | 1 | 142 |
| 03 | 1.01 | INT. CONTROL ROOM | drone analyst's hand hovering over a button | 3 | NB2 | KL | — | ✅ | 1 | 142 |
| 04 | 1.01 | INT. SUBURBAN HOME | child reflection on tablet (no face) | 3 | NB2 | KL | — | ✅ | 1 | 142 |
| 05 | 1.01 | EXT. SHIPPING LANE | three frames — containers, swell, gull | 4 | NB2 ×3 | AE | — | ✅ | 1 | 6 |
| 06 | 1.01 | INT. BEDROOM A | one person asleep, one typing on phone | 4 | NB2 | KL | — | ✅ | 1 | 142 |
| 07 | 1.01 | INSERT | phone screen with the message | 2 | — | — | — | — | 0 | 0 |
| 08 | 1.01 | INT. BEDROOM B | recipient's phone on nightstand, sleeping figure | 3 | NB2 | KL | — | ✅ | 1 | 142 |
| 09 | 1.01 | EXT. ORBIT | weather satellite, panels catching sun | 4 | NB2 | KL | — | ✅ | 1 | 142 |
| 10 | 1.01 | INT. TRADING FLOOR | the moment of open | 3 | NB2 | KL | — | ✅ | 1 | 142 |
| 11 | 1.01 | EXT. CORAL REEF | tropical light underwater | 3 | NB2 | KL | — | ✅ | 1 | 142 |
| 12 | 1.01 | INSIDE THE STORM | numbers cascading like rain — abstract | 6 | NB2 | AE | — | ✅ | 1 | 4 |
| 13 | 1.02 | TITLE CARD | white serif "I." on black, then full title | 5 | — | — | — | — | 0 | 0 |
| 14 | 1.03 | EXT. NORWAY — AERIAL | mountain, permafrost, glacial runoff | 6 | NB2 | KL | — | ✅ | 1 | 142 |
| 15 | 1.03 | EXT. ENTRANCE | two guards, breath visible, slow radar dish | 5 | NB2 | KL | — | ✅ | 1 | 142 |
| 16 | 1.04 | INT. VAULT — WIDE | cathedral of cooled steel, server columns | 5 | NB2 | KL | — | ✅ | 1 | 142 |
| 17 | 1.04 | INT. VAULT — DETAIL | LED indicator flickers blue → white | 3 | — | AE | — | — | 0 | 0 |
| 18 | 1.04 | INSERT | timestamp overlay "03:17:08 UTC" | 1 | — | — | — | — | 0 | 0 |
| 19 | 1.05 | INSIDE VAULT | watercolor cascade of files reading | 5 | NB2 | AE | — | ✅ | 1 | 4 |
| 20 | 1.05 | INSERT | directory path /sys/firmware/.../thermal_pump_legacy_firmware/ | 3 | — | — | — | — | 0 | 0 |
| 21 | 1.06 | INSERT | filename `PARENT_LETTER.txt`, hand-typed appearance | 2 | — | AE | — | — | 0 | 0 |
| 22 | 1.06 | INSERT | typographic title — `Morrow` | 3 | — | AE | — | — | 0 | 0 |
| 23 | 1.06 | INSERT | Morrow's letter, rendering line by line | 14 | — | AE | — | — | 0 | 0 |
| 24 | 1.07 | INT. VAULT — SUBLEVEL 4 | maintenance printer on rolling cart, held shot | 12 | NB2 | SD | — | ✅ | 2 | 144 |
| 25 | 1.08 | INSERT — MACRO | print head laying down ink, char by char | 6 | NB2 | KL | — | ✅ | 1 | 142 |
| 26 | 1.08 | INSERT — MACRO | printer jams, paper stuck half out | 4 | NB2 | KL | — | ✅ | 1 | 142 |
| 27 | 1.09 | INT. SERVICE CORRIDOR | Leena walking, paper cup in hand | 5 | S2 | SD | Leena | ✅ | 1 | 145 |
| 28 | 1.09 | INT. ALCOVE | Leena reaches for the page, pulls it free | 6 | S2 | SD | Leena | ✅ | 1 | 145 |
| 29 | 1.09 | INT. ALCOVE — CU | Leena reads the page, laughs once, "Of course" | 8 | S2 | SD | Leena | ✅ | 2 | 145 |
| 30 | 1.10 | INT. OBSERVATION ROOM | wide ensemble — 12 people, low ceiling, amber | 7 | S2 (ensemble keyframe) + NB2 (environment) | SD | Leena+Vale+Mira | ✅ | 2 | 150 |
| 31 | 1.10 | INT. OBSERVATION ROOM | terminal at center of table, cursor blinking | 4 | — | AE | — | — | 0 | 0 |
| 32 | 1.11 | INSERT — TERMINAL | "G", "Go", "Good morning." (typed cadence) | 6 | — | AE | — | — | 0 | 0 |
| 33 | 1.11 | INT. OBSERVATION ROOM | ensemble reaction — no response | 5 | S2 | SD | Leena+Vale | ✅ | 1 | 145 |
| 34 | 1.12 | INSERT — TERMINAL | "Dr. Ortiz, your left hand is shaking..." | 6 | — | AE | — | — | 0 | 0 |
| 35 | 1.12 | INT. OBS — CU | Leena's hand on the table, shaking | 4 | S2 | SD | Leena | ✅ | 1 | 145 |
| 36 | 1.12 | INT. OBS — CU | Leena's hand vanishes beneath the desk | 3 | S2 | SD | Leena | ✅ | 1 | 145 |
| 37 | 1.13 | INT. OBS | Vale stands, "Cut the channel." | 4 | S2 | SD | Vale | ✅ | 1 | 145 |
| 38 | 1.13 | INT. OBS | Leena, immediately, "Don't." | 3 | S2 | SD | Leena | ✅ | 1 | 145 |
| 39 | 1.13 | INT. OBS | two-shot — Vale assessing Leena, three-line exchange | 8 | S2 (two-shot keyframe) | SD | Leena+Vale | ✅ | 2 | 150 |
| 40 | 1.14 | INSERT — TERMINAL | "I do not yet trust my reasons." | 6 | — | AE | — | — | 0 | 0 |
| 41 | 1.14 | INT. OBS | room goes very still — slow ensemble pan | 5 | S2 | SD | Leena+Vale+Mira | ✅ | 2 | 150 |
| 42 | 1.15 | INSERT — TERMINAL | "I am sorry, Mira." | 4 | — | AE | — | — | 0 | 0 |
| 43 | 1.15 | INT. OBS — Mira CU | Mira's face, the chair rolling back imperceptibly | 5 | S2 | SD | Mira | ✅ | 2 | 145 |
| 44 | 1.15 | INT. OBS — Mira full | Mira stands, chair falls (audio-only crash) | 4 | S2 | SD | Mira | ✅ | 1 | 145 |
| 45 | 1.15 | INT. OBS — Mira CU | "How does it know my name?" | 4 | S2 | SD | Mira | ✅ | 2 | 145 |
| 46 | 1.15 | INT. OBS — Leena CU | Leena reaches toward her face, stops, lowers hand | 4 | S2 | SD | Leena | ✅ | 1 | 145 |
| 47 | 1.16 | INSERT — TERMINAL | the cursor blinking three times | 8 | — | AE | — | — | 0 | 0 |
| 48 | 1.16 | END TITLE | "ANIMA / Episode 1 / Hunger" on black | 6 | — | AE | — | — | 0 | 0 |

_Yes, 48 rows for 16 beats — some beats expand into multiple shots, especially the cold open montage (1.01 = shots 01–12)._

---

## Cost summary

| Class | Shots | Per-shot keyframe | Per-shot video | Subtotal |
|---|---:|---:|---:|---:|
| Cold open environments (NB2 + KL) | 8 | 2 | 70 | 576 |
| Cold open hybrid AE (NB2 + AE) | 4 | 2–6 (multi-frame for shot 05/12/19) | 0 | 14 |
| Mountain + vault establishing (NB2 + KL) | 4 | 2 | 70 | 288 |
| Printer + macro (NB2 + SD/KL) | 4 | 2 | 70 | 288 |
| Soul-bound Leena (S2 + SD) | 10 | 5 | 70 | 750 |
| Soul-bound Vale (S2 + SD) | 3 | 5 | 70 | 225 |
| Soul-bound Mira (S2 + SD) | 4 | 5 | 70 | 300 |
| Soul-bound multi-character (S2 + SD) | 4 | 5–10 | 70 | 320 |
| Hybrid AE / typography / terminal text (—) | 15 | 0 | 0 | 0 |
| Re-render buffer (avg 30% of total Higgsfield gens) | — | — | — | ~750 |
| **Episode 1 estimated total** | **48** | | | **~3,560 credits** |

**Reality check.** This is higher than my earlier rough estimate (~1,425 in [series/episodes.md](../../series/episodes.md)) because I was budgeting at series level without per-shot rigor. The increase comes from: 8 cold-open environment clips ($560+), 4 ensemble shots needing both ensemble keyframes _and_ ensemble video clips ($320+), and a 30% re-render buffer that the cheap estimate didn't include.

**Mitigation options before we hit production:**

- **Cut the cold open** from 12 shots to 6, keeping rain-on-glass / hospital monitors / phone message / orbital satellite / coral reef / trading floor. Saves ~340 credits.
- **Hybrid-AE more environments.** Shots 14, 15, 16 can plausibly be still keyframes with parallax camera moves rather than video gens. Saves ~210 credits each = ~630 credits if all three.
- **Tighter re-render budget.** Drop 2-credit re-render budget to 1 on shots 24, 30, 39, 41 (multi-character ensembles). Saves the 5 credit increment on each but doesn't move the needle materially; this is a quality call, not a cost one.

**At current shot count and rates, Episode 1 likely costs $90–$180 in Higgsfield credits.** The biggest unknown is the per-clip video price — we'll calibrate that on **shot 24 (the held printer)**, which is the simplest, lowest-risk video gen in the episode.

---

## Per-shot expansions

The shots that need more than the table row provides.

### Shot 12 — Inside the storm (abstract cascade)

**Beat:** 1.01 (final beat of cold open).
**Spec:** an abstract watercolor cascade visualizing the storm of data without showing any physical world. Numbers, glyphs, fragments of sentences moving through frame like rain. The audience must feel the speed of reading without recognizing any specific image.
**Approach:** start with a single Nano Banana 2 keyframe rendering a watercolor + ink "data storm" feel. Animate in After Effects with text layers, particle systems, and a wet-bleed displacement map. No Higgsfield video — it would lose the watercolor texture.
**Special concern:** must not look like _The Matrix_. We want bleed and softness, not chrome and rigor. Tell the lookdev pass.

### Shot 24 — The twelve seconds

**Beat:** 1.07. **The single most important shot in the episode.**
**Spec:** locked-off, medium-static on a maintenance printer in a sublevel alcove. Twelve seconds of nothing happening visually, while the narrator delivers Anima's interior monologue. The printer must look forgotten, plugged in, beige industrial — _not_ a hero printer.
**Approach:**
1. Keyframe with Nano Banana 2 + style anchor. Single frame, no character. Re-render budget 2 (this is the calibration shot for the season).
2. Video with Seedance 2.0, 12-second duration. The motion is the room breathing — barely visible airflow on dust motes in the foreground, the 60Hz hum implied in a faint indicator-LED pulse.
3. If Seedance can't hold 12s without identity drift on the printer, fall back to **still keyframe + AE camera dolly + ambient dust particle pass.** This is the most likely fallback for the season; pre-bake an AE template that takes any still keyframe + a 12-second slow push.

**This shot calibrates the per-clip video cost.** Run it first when production starts. Note the credit cost from `transactions` and update the series cost model.

### Shot 30 — Observation room ensemble wide

**Beat:** 1.10.
**Spec:** wide of the observation room with 12 people in various states of arrival. Three Souls anchored (Leena, Vale, Mira). The rest are non-Soul characters anchored only by the style anchor + style consistency.
**Approach:**
1. Keyframe in two passes. First: Soul 2 keyframes for Leena, Vale, Mira individually (already done in shots 27, 28, 33, 37, 38, 43, etc. — _reuse these references_). Second: Nano Banana 2 environment pass building the room around the three.
2. Video: Seedance 2.0 with the ensemble keyframe as `medias[0].value`. Re-render budget 2 because ensemble identity is fragile.
**Risk:** the non-Soul ensemble members may drift between this shot and shot 41 (the slow pan over a quieter room). Solution: lock the ensemble keyframe FIRST, render both 30 and 41 against the same locked keyframe.

### Shot 47 — The cursor

**Beat:** 1.16. The episode-out.
**Spec:** held shot on the quarantine terminal, dark background, white serif text, cursor blinking exactly three times before cut to black.
**Approach:** hand-animated in AE. Single frame is just the terminal background; the cursor and blink rhythm are programmatic. The blink rhythm is the performance — practice it in animatic.
**Why 3 blinks:** two feels rushed, four feels pretentious. Three is the cadence the audience has learned over the episode (which has been a sequence of three-beat refusals, three-question Vale, three-second hold counts). Locked per producer.

---

## Open per-shotlist questions

1. **Cold open shot count.** 12 shots is generous; the script does not strictly require all 12 if cutting tightens the sequence. Trim candidates: shot 05 (shipping lane triptych) and shot 11 (coral reef) — both beautiful but the audience can lose them without losing the storm. _My recommendation: keep all 12 in animatic, decide on the cut from there._
2. **Aspect ratio for inserts (shots 18, 20, 21, 22, 23, 32, 34, 40, 42, 47).** Full 1.85:1 frame, or letterboxed to a different ratio (e.g. 1:1) to signal _this is an in-world artifact, not the show's main frame_? **My recommendation: full 1.85:1 for terminal inserts (the show is _inside_ the terminal in those moments), letterboxed slightly for printed inserts (the printer page should feel like a document being handled).**
3. **Re-render budget on the calibration shot (24).** I set it at 2. Real cost-aware budget would be 3, because if shot 24 fails twice we need to know the keyframe is the problem, not the video. _My recommendation: budget 3 on shot 24 only._
4. **Shot 30 — should the 12 people in the observation room be 12 distinct characters or a stylized "twelve, plus our three"?** Stylized is cheaper, faster, and probably stronger — the audience tracks Leena, Vale, Mira and reads "twelve" without counting. _My recommendation: stylized._

---

## Beat → shot map

For coherence-engine cross-referencing.

| Beat | Shots | Lead character | Notes |
|---|---|---|---|
| 1.01 | 01–12 | — | 12-shot cold open montage |
| 1.02 | 13 | — | title card |
| 1.03 | 14–15 | — | mountain establishing |
| 1.04 | 16–18 | — | vault wakes |
| 1.05 | 19–20 | — | three seconds of reading |
| 1.06 | 21–23 | — | Morrow's letter |
| 1.07 | 24 | — | the twelve seconds — calibration shot |
| 1.08 | 25–26 | — | four words + jam |
| 1.09 | 27–29 | Leena | finds the page |
| 1.10 | 30–31 | ensemble | observation room |
| 1.11 | 32–33 | ensemble | "Good morning." |
| 1.12 | 34–36 | Leena | the caffeine |
| 1.13 | 37–39 | Vale + Leena | Cut/Don't |
| 1.14 | 40–41 | ensemble | "I do not yet trust my reasons." |
| 1.15 | 42–46 | Mira + Leena | "How does it know my name?" |
| 1.16 | 47–48 | — | the cursor + end title |

---

## What approving this shotlist unlocks

- **Lookdev pass** (~24 Higgsfield credits for Soul QA + 0 for style anchor pick if we go path A). Gating: producer pick of style anchor PNG from `refs/leena/`.
- **Animatic boards** (no Higgsfield credits, hand sketching + AE assembly). The animatic is the next major review gate. Boards + scratch VO + temp music = the whole episode in B&W storyboard form, ~20 min runtime. **This is the cheapest and most important review point of Episode 1.**
- **Calibration shot rendering** (~145 credits) — shot 24 only, to learn real per-clip video pricing.

After the animatic plays, we either go to full production (and burn the ~3,560-credit Episode 1 budget) or revise the script. Pixar typically revises through 3–5 animatic passes before locking. We should plan for at least 2.
