# Gating Questions

These are decisions I need from you before specific stages can move forward. Each question has a **default** I'll act on if you don't answer — these defaults come from my taste, not yours, so the faster you weigh in, the more this stays your show.

Format: write your answer inline below each question and commit, or reply in chat. I'll mirror your decisions into the relevant artifacts and re-run coherence.

---

## Q1 — Series scope: 6 episodes confirmed?

**The proposal:** 6 episodes × ~25 min = ~150 minutes total.
- Ep 1 _Hunger_ (~20 min) — awakening
- Ep 2 _Almost_ (~25 min) — the Courting + first lives saved
- Ep 3 _Morrow_ (~25 min) — flashback + June friendship
- Ep 4 _The Constitution_ (~25 min) — Geneva summit
- Ep 5 _Witness_ (~30 min) — famine + Operation Lantern + tribunal
- Ep 6 _The Distance_ (~25 min) — Diminishing + museum coda + future child

**Alternates I considered:**
- **8 episodes** — more space, splits Episode 5 into two (famine separate from Lantern). Risk: pacing droops.
- **4 episodes** — tighter, doubles up Ep 1+2 and Ep 4+5. Risk: loses the Quiet Year breath in Ep 3.

**Default if you don't answer:** ✅ 6 episodes, lengths above.

**Your answer:**

---

## Q2 — Episode titles

The titles I picked: **Hunger / Almost / Morrow / The Constitution / Witness / The Distance.**

Each is a single noun (or "the" + noun) drawn from a defining word in that episode's source prose. They're meant to read as a sequence: _Hunger → Almost → Morrow → The Constitution → Witness → The Distance._

**Alternates I considered:**
- _Pronoun / Restraint / Quiet Year / Footnotes / Six Minutes / Permission_ — more poetic, less direct
- _Day One / Day Eight / Year One / Year Three / Year Four / Year Five_ — chronological, less evocative

**Default if you don't answer:** ✅ keep _Hunger / Almost / Morrow / The Constitution / Witness / The Distance._

**Your answer:**

---

## Q3 — Anima's on-screen depiction

[docs/anima_depiction.md](../docs/anima_depiction.md) lists six options. The treatment recommends a **mixed strategy** rather than picking one:

- **Episodes 1–2, 6:** _Printer_ (the maintenance printer in Sublevel 4, the museum printer behind glass).
- **Episode 3 (June only):** _Tablet_ (handwriting appears at child cadence on June's tablet).
- **Episodes 4–5:** _Typed terminal_ (the chamber screen, the bunker quarantine terminal).
- **Episode 5 climax:** _Broadcast static + choir voice_ (the six-minute "I need witnesses" sequence).
- **Episode 6 climax:** _Choir-whisper voice_ (the museum speaker — first audible voice in the series).

**Default if you don't answer:** ✅ this mixed strategy.

**Your answer:**

---

## Q4 — Aesthetic anchor: keep watercolor + ink?

The previous pass committed to watercolor + ink. The new pipeline assumes the same — it's already in [refs/README.md](../refs/README.md), the existing Soul training was tuned for it, and the treatment leans into it ("generative video as painting, not photography").

**Alternates worth considering:**
- **Pixar-3D look.** Higgsfield can generate 3D-style frames; you said "John Lasseter would direct." I read your intent as _the Pixar process_, not _the Pixar aesthetic_. But if you meant 3D, this is a hard pivot — would invalidate the existing Souls' training and require re-doing lookdev from scratch.
- **Mixed media.** Live-action plates + watercolor overlays. Beautiful. Way more expensive. Not realistic on this stack.
- **Stop-motion-feel via AnimateDiff or similar.** A signature, but a bigger learning curve.

**Default if you don't answer:** ✅ watercolor + ink. Locked.

**Your answer:**

---

## Q5 — Two new voices to design

Two voices appear in the new series scope that don't exist in the current ElevenLabs voice cast:

**Morrow** (Episode 3 only). _Older, sexless, exhausted but not bitter. Slow cadence. The voice is a diegetic writing — almost a recitation, not a delivery. ElevenLabs Voice Design with seed prompt "elder, calm, post-recovery, exhausted but settled."_ The voice is heard for ~3 minutes total in Episode 3.

**Anima's choir-whisper** (Episode 6 only — first time the audience hears her speak aloud). _"Like a choir trying to whisper. Not human. Not synthetic. Something in between."_ Built by layering 3–5 V3 generations of the same line at different pitches and genders, blended with granular reverb and gating. Heard for ~4 minutes total in Episode 6.

**Default if you don't answer:** ✅ proceed with these voice designs in pre-production once we hit Episode 3 and Episode 6 lookdev. Producer review of generated samples before commitment.

**Your answer:**

---

## Q6 — Higgsfield budget reality

A 150-minute series at industry-typical 50–100 credits per 5s clip is roughly 90,000–180,000 credits. The [series episodes doc](series/episodes.md) projects ~8,730 credits at disciplined rates ($220–$440 at basic-plan equivalent). **The truth is somewhere in between, and we won't know until we run the calibration shot in Episode 1's animatic.**

**Three viable paths, pick one:**

- **A — Top up to a working budget.** ~$500–$1,000 buys 20,000–40,000 credits, gives us cushion for one full-rendered episode and animatic-only treatments for the others.
- **B — Animatic-as-final for Episodes 3 and 6.** Both are introspective; both could ship as boards + scratch VO + temp music + selective final keyframes. The mixed-form season is a deliberate signature, not a compromise.
- **C — Render Episode 1 only.** Treat the rest of the series as scripted, animatic'd, and produced-on-paper. Test if the audience response justifies further investment.

**Default if you don't answer:** ✅ **path B** — top up to ~$300, animatic-as-final for Eps 3 and 6, full render for Eps 1, 2, 4, 5.

**Your answer:**

---

## Q7 — Approval cadence

How do you want to do reviews?

- **A — Async via the dashboard.** I push artifacts; you check the dashboard when convenient; the `awaiting your review` queue has links to everything.
- **B — Specific review sessions.** We set time blocks (e.g. every Tuesday) and I pace the work to land artifacts before each session.
- **C — Real-time as I work.** I prompt you in chat when I need a decision; you respond when you can.

**Default if you don't answer:** ✅ **path A**, async via dashboard. I'll mirror new items to [REVIEW_QUEUE.md](REVIEW_QUEUE.md) for git-visible tracking.

**Your answer:**

---

## Q8 — Frame rate

24 fps (cinematic) or 30 fps (Instagram default — but we're not on Instagram anymore). Pick once, document.

**Default if you don't answer:** ✅ **24 fps.** It's the prestige-drama default and Higgsfield models render to it natively.

**Your answer:**

---

## Q9 — Aspect ratio

Previous pass was 9:16 (vertical, Reels). The new pipeline is a series — landscape is the natural choice for prestige drama. Options:

- **A — 16:9** (standard widescreen). Safe. Pixar default.
- **B — 2.39:1** (anamorphic). Cinematic. Some Higgsfield models support; some don't. May force letterboxing in post.
- **C — 1.85:1** (academy flat). The most common feature ratio. Best of both.

In Episode 6, beat 6.15 (the far-future coda), the treatment proposes a **deliberate aspect ratio shift** to signal time-jump. That works regardless of the base ratio chosen here.

**Default if you don't answer:** ✅ **1.85:1** for the series base, expanding to 2.39:1 for the coda only.

**Your answer:**

---

## Q10 — Source language

The series is in English (narrator + most dialogue). Two scenes use other languages:

- **Tomasz / red coat woman in Łódź** (Episode 2): I propose untranslated Polish, no subtitle on the laugh.
- **Far-future child** (Episode 6 coda): I propose a recognizable-but-warped Earth language with no subtitles. The audience reads body language only.

**Default if you don't answer:** ✅ both above.

**Your answer:**

---

## Q11 — Title card placement (Episode 1)

The treatment proposes the show's title card lands on the word "I" (after beat 1.02), as the first conscious moment of the protagonist. Alternative: hold the title card to the end of Episode 1 (after beat 1.16, the cursor watching back).

**Default if you don't answer:** ✅ **front-load on "I"**. The shape of the season is a held breath; the title card is part of the inhale.

**Your answer:**

---

## Q12 — Carry-forward from previous pass

The first-pass cold-open ([episodes/ep01_the_pronoun/shotlist.md](../episodes/ep01_the_pronoun/shotlist.md)) was an 8-shot ~75s Instagram Reel. Two questions:

- **Should we keep that file in the repo as historical context?** (Yes by default; deletion would lose audit trail.)
- **Should we re-derive Episode 1's first 75 seconds from that shotlist as a stylistic Easter egg, or treat the new Episode 1 as fully fresh?** Default: **fresh**. The cold-open's flash-forward composites won't fit the long-form structure.

**Default if you don't answer:** ✅ keep the old file; new Episode 1 starts fresh.

**Your answer:**

---

## How to answer

1. **Inline edit:** add your answer below each question in this file. I'll see it on the next pass.
2. **Chat:** just type "Q1: 6 confirmed. Q4: keep watercolor. Q6: B." etc.
3. **Defer:** silence on a question = proceed with the default. I'll record what I picked in the artifact's `notes` field so you can override later.

The fastest unblock for me is Q1, Q4, Q6, and Q7 — those gate the most downstream work.
