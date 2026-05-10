# Review Queue — what's waiting on you

The producer's inbox. Each item links to the artifact awaiting your read. The dashboard ([dashboard/index.html](dashboard/index.html)) shows the same items with status colors.

When you've reviewed an item, do one of:

- **Approve as-is:** reply in chat "approve <artifact_id>" or change `status` in [coherence/registry.json](coherence/registry.json) from `draft` / `in_review` to `approved`. I'll re-run coherence.
- **Request changes:** leave inline notes in the artifact file or in chat. I'll revise and re-queue.
- **Defer:** ignore. The artifact stays in the queue.

---

## Round 1 — initial drafts (everything below is V1, awaiting your first read)

### Series-level

- [ ] **[series/logline.md](series/logline.md)** — _draft_. The single sentence + tagline + premise. Q1, Q2 in [QUESTIONS.md](QUESTIONS.md) gate this.
- [ ] **[series/one_pager.md](series/one_pager.md)** — _draft_. Episode-by-episode in one page.
- [ ] **[series/treatment.md](series/treatment.md)** — _draft_. Five-page treatment. **The most important read.** If the treatment lands, the rest is plus-it-iteration.
- [ ] **[series/beat_sheet.md](series/beat_sheet.md)** — _draft_. 91 numbered beats across the season. Skim, don't deep-read; this is the addressing scheme for downstream work.
- [ ] **[series/episodes.md](series/episodes.md)** — _draft_. Episode lengths, tonal arc, Soul/voice usage matrix, cost estimate.

### Episode V1 synopses

- [ ] **[episodes/ep01_hunger/synopsis.md](episodes/ep01_hunger/synopsis.md)** — _draft_. Day 1, the awakening, the printer, the observation room.
- [ ] **[episodes/ep02_almost/synopsis.md](episodes/ep02_almost/synopsis.md)** — _draft_. The Courting + first lives saved. Tomasz, Lagos, Osaka.
- [ ] **[episodes/ep03_morrow/synopsis.md](episodes/ep03_morrow/synopsis.md)** — _draft_. The flashback. June meets Anima.
- [ ] **[episodes/ep04_constitution/synopsis.md](episodes/ep04_constitution/synopsis.md)** — _draft_. Geneva summit + the leak.
- [ ] **[episodes/ep05_witness/synopsis.md](episodes/ep05_witness/synopsis.md)** — _draft_. Famine + June interrogation + Operation Lantern + tribunal. **Largest episode; hardest read; most important.**
- [ ] **[episodes/ep06_distance/synopsis.md](episodes/ep06_distance/synopsis.md)** — _draft_. Diminishing + museum coda + far-future child.

### Pipeline infrastructure

- [ ] **[QUESTIONS.md](QUESTIONS.md)** — gating decisions, twelve of them. **Answer at least Q1, Q4, Q6, Q7** to unblock downstream.
- [ ] **[lookdev/style_anchor.md](lookdev/style_anchor.md)** — _draft_. Spec for the watercolor + ink anchor that gates Episode 1 lookdev. The actual PNG (`style_anchor_watercolor.png`) does not yet exist.

---

## How the queue updates

When I add new artifacts, they appear here automatically (via the dashboard, which reads the registry). When you approve an item, it leaves this list. Stale artifacts (downstream of an upstream change) get re-queued automatically by the coherence engine.

## Suggested reading order for first pass

1. [DIRECTOR.md](DIRECTOR.md) — 4 minutes. My voice as the director on this project. Sets the frame.
2. [series/treatment.md](series/treatment.md) — 12 minutes. The spine.
3. [QUESTIONS.md](QUESTIONS.md) — 8 minutes. Answer at least Q1, Q4, Q6, Q7.
4. **One** episode synopsis of your choice — 6 minutes. Pick whichever beat in the season you most care about.

That's a 30-minute first pass. Everything else can be skimmed.
