# Anima — Production Pipeline (Lasseter Cut v1)

> _"You can't pretty-picture your way out of a story problem."_
> — John Lasseter, Director (this project)

This is the **second pass** at producing _Anima_. The first pass (everything outside `production/`) aimed at a single 75-second Instagram Reel cold-open. That work isn't lost — the trained character Souls, the world bible, the V3 voice tags, and the source story all carry forward. But the form was wrong for the material. _The Second Dawn_ wants to be a **series**, not a clip.

This pipeline is built around the way Pixar makes a feature, adapted for an AI-driven generative stack.

## The five Pixar principles this pipeline encodes

1. **Story is everything.** No keyframe, no Soul gen, no video clip happens until the story works on the page.
2. **Story Trust over committee.** The director (me, in the Lasseter chair) drives. The producer (you) is the only person whose approval is binding. Notes from the Trust are gifts, not orders.
3. **Plussing.** Every artifact is a draft of every other artifact. The treatment gets better when the script gets better. The script gets better when the animatic gets better. **Nothing is final until the master is delivered.**
4. **The animatic is the movie.** We cut a black-and-white storyboard reel of every episode — boards + scratch VO + temp music — _before_ we spend a single Higgsfield credit on a video clip. If it doesn't play in animatic, the clip won't save it.
5. **Authenticity in the world.** The watercolor + ink language, the V3 narrator grammar, the character canon — these aren't decoration. They're the rules. They're locked. Production exists to serve them.

## The pipeline (eleven stages)

Each episode flows through these stages in order. Each gate requires producer approval before the next gate opens.

| # | Stage | Artifact | Tools | Owner | Approval gate? |
|---|---|---|---|---|---|
| 1 | **Logline** | [series/logline.md](series/logline.md) | — | Director | ✅ |
| 2 | **Treatment** | [series/treatment.md](series/treatment.md) | — | Director | ✅ |
| 3 | **Series breakdown** | [series/episodes.md](series/episodes.md) | — | Director | ✅ |
| 4 | **Episode synopsis (1 page)** | `episodes/<ep>/synopsis.md` | — | Director | ✅ |
| 5 | **Episode outline (beats)** | `episodes/<ep>/outline.md` | — | Director | ✅ |
| 6 | **Script** | `episodes/<ep>/script.fountain` | — | Director | ✅ |
| 7 | **Shotlist** | `episodes/<ep>/shotlist.md` | — | Director | ✅ |
| 8 | **Animatic** (boards + scratch VO + temp music) | `episodes/<ep>/animatic/` | ElevenLabs (scratch), local sketch tool, DaVinci | Director | ✅ **largest gate** |
| 9 | **Lookdev** (style anchor + character keyframe tests + environment plates) | [lookdev/](lookdev/) | Higgsfield (Soul 2 / Nano Banana 2 / Z Image) | Director | ✅ |
| 10 | **Production** (final keyframes + video gens + final VO) | `episodes/<ep>/production/` | Higgsfield + ElevenLabs | Director | ✅ per-episode |
| 11 | **Post** (sound design + edit + color + master) | `episodes/<ep>/post/` + `episodes/<ep>/delivery/` | DaVinci, After Effects | Director | ✅ per-episode |

**The animatic gate (stage 8) is non-negotiable.** It's where Pixar saves itself from expensive mistakes. We watch the whole episode in storyboard form before we render anything that costs credits. If the cut doesn't work, we go back to script.

## Coherence (the ripple engine)

Pixar's pipeline is monolithic by people; ours has to be monolithic by file. When you change a character's voice in [docs/characters/mira.md](../docs/characters/mira.md), every artifact downstream of Mira — every shotlist with Mira in it, every script line, every ElevenLabs voice render — needs to re-review. We track this via a **coherence registry** ([coherence/registry.yaml](coherence/registry.yaml)) that declares each artifact's authority and dependencies, and a checker ([coherence/coherence.py](coherence/coherence.py)) that flags downstream artifacts as `STALE` when an upstream changes.

Run `python production/coherence/coherence.py --check` to print the stale list. It's also rendered prominently on the dashboard.

## The dashboard

The producer-facing surface lives in [dashboard/](dashboard/). It's a single static HTML file regenerated from the coherence registry + git log. Open it locally:

```bash
python production/dashboard/generate.py
open production/dashboard/index.html
```

Three sections:
- **Awaiting your approval** — gates blocking on the producer (you).
- **Series matrix** — episodes × stages, color-coded.
- **Stale artifacts** — what coherence flagged.

## What's in this directory

```
production/
├── README.md              ← you are here
├── DIRECTOR.md            ← Lasseter's statement of intent
├── REVIEW_QUEUE.md        ← live list of items awaiting your review
├── QUESTIONS.md           ← gating decisions I need from you
├── series/                ← series-level creative spine
│   ├── logline.md
│   ├── one_pager.md
│   ├── treatment.md
│   ├── beat_sheet.md
│   └── episodes.md
├── episodes/              ← per-episode work
│   ├── ep01_hunger/
│   ├── ep02_almost/
│   ├── ep03_morrow/
│   ├── ep04_constitution/
│   ├── ep05_witness/
│   └── ep06_distance/
├── lookdev/               ← visual canon: style anchor, characters, environments
├── coherence/             ← ripple engine
│   ├── registry.yaml
│   └── coherence.py
└── dashboard/             ← producer-facing UI
    ├── generate.py
    ├── styles.css
    └── index.html
```

## Source documents (locked, referenced from inside `production/`)

These predate this pipeline and remain canonical:

- [docs/story.md](../docs/story.md) — _The Second Dawn_, the source prose.
- [docs/characters/](../docs/characters/) — character canon (Anima, Leena, Vale, Mira, June).
- [docs/anima_grammar.md](../docs/anima_grammar.md) — narrator voice rules.
- [docs/anima_depiction.md](../docs/anima_depiction.md) — six options for Anima's on-screen presence.
- [docs/voice_strategy.md](../docs/voice_strategy.md) — V3 voice palette per character.
- [refs/manifest.json](../refs/manifest.json) — Higgsfield Soul IDs (Leena, June, Vale, Mira all `ready`).
- [scripts/generate_vo.py](../scripts/generate_vo.py) — ElevenLabs V3 cast pipeline.

The previous-pass cold-open ([episodes/ep01_the_pronoun/shotlist.md](../episodes/ep01_the_pronoun/shotlist.md)) is preserved for reference. It will be re-derived from the new shotlist for Episode 1 once we get there.
