# Anima — Episode 1 "The Pronoun" Delivery Pipeline

Single source of truth for production state, blocking dependencies, and token-cost budget. Update this file as work moves through each stage.

**Last updated:** 2026-05-07
**Current branch:** `claude/short-film-instagram-clips-bwu2z`

---

## Budget snapshot

| Pool                  | Started | Spent so far | Remaining   | Notes |
| --------------------- | ------: | -----------: | ----------: | ----- |
| Higgsfield credits    |  200.00 |        63.26 |  **136.74** | basic plan; Leena Soul already trained |
| ElevenLabs credits    |     TBD |          TBD |         TBD | quota dependent on plan; check with `python scripts/generate_vo.py --list` |

**Higgsfield spend breakdown (2026-05-07):**
- 16.76 — pre-existing probes (Z Image / Face Swap / Nano Banana Pro)
- 25.00 — Soul training "Test Probe URL" (discovery cost — proved that `show_characters action='train'` requires the public CDN URL form, not the raw `media_id` UUID despite what the MCP description says). Soul `f50c9a20-00e2-4e76-a4b8-fced41bb0d92` is trained-but-useless (5 duplicates of one image); leave in account, do not generate against it.
- **25.00 — Leena Soul training ✅** `soul_id: 1012370e-3cf7-486a-b644-88b174395b13` — `status: ready`.

**Projected forward spend (locked-ish):**
- 25.00 — June Soul training (in flight as `5949fbd6-dbb4-4672-b6de-06e6a488ba47`, status: queued/training)
- 25.00 — General Vale Soul training (must trigger AFTER June reports ready; basic plan = 1 concurrent training)
- 25.00 — Mira Soul training (refs uploaded + confirmed in `refs/manifest.json`; **NOT triggered yet — needs your OK**, since this wasn't in the original spec and adds another 25 credits)

**Runway after all 4 Souls trained: ~61.74 credits.** That's not enough for the video stage on its own; see [Cost models](#cost-models) and [Decision points](#decision-points-before-video-stage-starts).

---

## Stage 0 — Pre-production specs

- [x] Voice cast spec — migrated to **ElevenLabs v3** with inline audio tags ([scripts/generate_vo.py](scripts/generate_vo.py))
- [x] [docs/voice_strategy.md](docs/voice_strategy.md) — V3 tag palette + per-character voice search/design strategy
- [x] Higgsfield Soul training pipeline doc ([refs/README.md](refs/README.md))
- [x] Reference image manifest + media_id tracking ([refs/manifest.json](refs/manifest.json))
- [x] Pipeline checklist (this file)
- [x] [`docs/anima_grammar.md`](docs/anima_grammar.md) — locked narrator voice grammar, V3 audio-tag palette in §10
- [x] [`docs/characters/`](docs/characters/) — five character canon files (anima, leena, vale, mira, june) + index
- [x] [`docs/anima_depiction.md`](docs/anima_depiction.md) — six on-screen depiction options for Anima (recommended primary: **Printer**; secondary: **Tablet (June only)**) — needs project-lead pick
- [x] Mira ref upload + Soul training (in flight)
- [x] Locked 8-shot trimmed cold-open: [`episodes/ep01_the_pronoun/shotlist.md`](episodes/ep01_the_pronoun/shotlist.md). Reduces video stage from ~1500 → ~750 credits.

## Stage 1 — Reference uploads & Soul training

| Character     | Refs | media_ids confirmed | Soul status        | soul_id |
| ------------- | ---: | ------------------: | ------------------ | ------- |
| Leena Ortiz   |   20 | ✅                  | **ready** ✅       | `1012370e-3cf7-486a-b644-88b174395b13` |
| June          |   20 | ✅                  | **ready** ✅       | `5949fbd6-dbb4-4672-b6de-06e6a488ba47` |
| General Vale  |   19 | ✅                  | **ready** ✅       | `66c42015-c664-446d-8555-8836f81663e6` |
| Mira          |   20 | ✅                  | **training** ⏳    | `b9ef5c11-1d68-40e8-bf8f-4edb2820d4e0` |

- [x] Upload 79 character refs across 4 characters (parallel curl, all HTTP 200)
- [x] Confirm 79 `media_id`s via `media_confirm` (status: uploaded)
- [x] Trigger Leena Soul training → `ready`
- [x] Trigger June Soul training → `ready`
- [x] Trigger Vale Soul training (in flight)
- [ ] Trigger Mira Soul training (after Vale reports ready)
- [ ] Per-Soul QA: generate 2-3 test images from each ready Soul + visual sign-off before any keyframe shot work begins. Cost: ~6 credits per Soul × 4.
- [ ] **Style anchor:** drop `refs/style/style_anchor_watercolor.png` (the locked watercolor + ink reference). Use as image input on every keyframe generation to prevent the photoreal drift the README flags about Shot 13. _Owner: TBD — pick from existing character sheets._

**Character canon:** see [docs/characters/](docs/characters/) — five locked character files (anima, leena, vale, mira, june) with personality traits, voice profile mirrors, sample lines, and director's notes. The narrator voice grammar is locked in [docs/anima_grammar.md](docs/anima_grammar.md).

## Stage 2 — Voice-over (ElevenLabs v3)

Driven by [scripts/generate_vo.py](scripts/generate_vo.py). Output goes to `episodes/ep01_the_pronoun/audio/` (gitignored). Strategy + tag palette: [docs/voice_strategy.md](docs/voice_strategy.md).

- [ ] `python scripts/generate_vo.py --all` — render every character's V3-tagged delivery + plain test_line.
- [ ] Listen pass per character: search ElevenLabs library if default doesn't fit (use `voice_search_hint` field); use Voice Design for June (required) and as fallback for Mira.
- [ ] Lock chosen voice ids back into `CAST` in `generate_vo.py`. Update the matching rows in [docs/characters/*.md](docs/characters/).
- [ ] Render the production VO lines (cold-open + per-shot dialogue from shotlist).
- [ ] Apply Anima's synthetic-edge post-process in DaVinci per [docs/anima_grammar.md §7](docs/anima_grammar.md).

**ElevenLabs cost note:** v3 charges by character of input text (audio tags counted). Cold-open VO ≈ 600–900 characters total across all five voices. Voice Design for June is a one-time per-generation cost. Easily inside any paid tier.

## Stage 3 — Storyboard / shot list

- [x] [`episodes/ep01_the_pronoun/shotlist.md`](episodes/ep01_the_pronoun/shotlist.md) — locked 8-shot cold-open with per-shot keyframe model, video model, Soul ID, re-render budget, V3-tagged VO line, and per-shot specs.
- [ ] Pick Anima's depiction primary + secondary from [docs/anima_depiction.md](docs/anima_depiction.md). The shotlist is built around **Option 1 (Printer) + Option 4 (Tablet, June only)** — confirm or revise.
- [ ] `episodes/ep01_the_pronoun/shot_specs/<NN>.md` per shot if any beat needs more than the shotlist row.

## Stage 4 — Keyframe generation (per shot)

Image generation per shot. Pick model per use:
- **Character shots** → `soul_2` with `soul_id` of the trained character + style-anchor image as ref (`medias[].role=image`). One image per shot.
- **Environment / object close-ups** → `nano_banana_2` with style anchor. Higher quality for printer close-ups, abstract weather frames, etc.
- **Look-dev probes** → `z_image` (0.15/gen) for cheap iteration before committing to soul_2 / nano_banana_2.

- [ ] First keyframe per shot — text prompt + style anchor + soul_id (when applicable).
- [ ] QA pass per keyframe — accept / re-render. Budget 2 re-renders per shot average.
- [ ] Save approved keyframes to `episodes/ep01_the_pronoun/keyframes/<NN>.png` (gitignored).
- [ ] Track per-shot keyframe job IDs in a manifest (so we can pass them as `value` in `medias[]` for the video step).

**Per-shot keyframe cost model:**
| Model         | Cost / gen | When to use |
| ------------- | ---------: | ----------- |
| `z_image`     |       0.15 | Cheap composition probe |
| `nano_banana_2` (Pro) |   2.00 | Final keyframes, environment shots |
| `soul_2` 2k   |       ~5*  | Character shots — *exact cost not in model registry; verify by spending 1 gen and checking transactions |

If we assume 15 shots, 1 final + 2 re-renders avg, mix of 2 nb-pro + 1 soul_2 per character shot: roughly **15 × 6 = ~90 credits**. That alone exceeds our remaining budget after Souls. **Mitigation:** start every shot with z_image probes (0.15 each → 7 free probes for 1 keyframe), only commit to soul_2/nano_banana_2 once composition is locked.

## Stage 5 — Video generation (per shot)

Image-to-video. Each clip turns one approved keyframe into a 5–10s shot.

- [ ] Pick model per shot:
  - **Character shots needing identity stability + audio** → `seedance_2_0` (reference-driven, strong identity)
  - **Multi-shot / motion-transfer / camera moves** → `kling3_0`
  - Verify cost & duration constraints before booking via `models_explore action='get' model_id='<id>'`
- [ ] Generate Shot 01 first as a process-test (don't kick off all shots at once).
- [ ] Approve / re-render. Budget 1 re-render per shot.
- [ ] Save approved clips to `episodes/ep01_the_pronoun/video/<NN>.mp4` (gitignored).

**Cost calibration TODO:** I haven't priced video gens yet on this account — first kick will reveal the per-clip credit cost via `transactions`. **Until calibrated, treat video as the dominant spend line.** Industry-typical Higgsfield video pricing is 50–100 credits per 5s clip; at that rate, 15 shots × 1.5 gens = ~1500 credits. **We do not have that budget on a basic plan.**
**Mitigation options:**
1. Top up Higgsfield credits before video stage.
2. Render fewer / shorter clips (cut shot count, lean on still-with-pan moves where possible).
3. Use Z Image + manual After Effects animation for some shots (we have AE 2026 installed locally per system info).

## Stage 6 — Audio post

- [ ] DaVinci Resolve project: `episodes/ep01_the_pronoun/edit/the_pronoun.drp`
- [ ] Import VO stems → apply Anima synthetic-edge bus.
- [ ] Sound design / ambience layer (no specific spec yet — TBD).
- [ ] Dialogue level pass, ducking, subtle reverb where the script implies space.

## Stage 7 — Edit & assembly

- [ ] Cut to picture in DaVinci: drop video clips on V1, VO on A1–A5 by character, ambience on A6.
- [ ] Lock picture.
- [ ] Color pass: keep the watercolor+ink LUT consistent; protect skin tones on Leena/Vale/June character shots.

## Stage 8 — Export & delivery

- [ ] Master export: 1080×1920 (Instagram 9:16), H.264, ~10 Mbps, AAC 192 kbps stereo.
- [ ] Frame-rate decision: 24 fps for cinematic feel vs 30 fps for IG default. Pick once, document in shotlist.
- [ ] Compliance: Instagram Reels caption / cover frame / first-3-seconds hook check.
- [ ] Deliver to `episodes/ep01_the_pronoun/exports/the_pronoun_v01.mp4`.
- [ ] Backup raw renders + project file outside the repo (gitignored).

---

## Cost models

### Higgsfield (per Episode, rough)

| Stage                                     | Quantity | Unit cost | Subtotal |
| ----------------------------------------- | -------: | --------: | -------: |
| Soul training × 3                         |        3 |        25 |       75 |
| Soul QA gens (3 per Soul)                 |        9 |       ~5 |       45 |
| Style-anchor probe gens                   |        4 |         2 |        8 |
| Keyframe probes (Z Image)                 |       30 |      0.15 |        ~5 |
| Final keyframes (mix nb-pro + soul_2)     |       15 |        ~4 |       60 |
| Re-renders (~2 per shot)                  |       30 |        ~4 |      120 |
| Video gens (assume seedance, 5s)          |       18 |       ~70 |     1260 |
| **Estimated Ep 1 total**                  |          |           |  **~1573** |

**Reality check vs. budget:**
- Available after current spend + Soul trainings: **~86 credits**
- Estimated need: **~1500+ credits**
- **Gap:** very large. The video stage is the killer.

### Decision points before video stage starts

Pick at least one before opening the credit faucet:

1. **Top up Higgsfield** to ~$50 / ~2000 credits.
2. **Cut shot count** — 6–8 shot cold-open instead of 15.
3. **Hybrid render** — only 4–5 hero shots use Higgsfield video; the rest are still-with-camera-move + parallax built in After Effects from the keyframe.
4. **Switch to Soul Cast** for some character shots (`budget` param, default 50 credits) which may bundle look-dev + character consistency more efficiently than soul_2 + manual reference passes.

---

## Risks / open questions

- ⚠️ **Concurrency limit:** basic plan = 1 Soul training in flight at a time. Budget ~30 min wall-clock to get all 3 Souls trained sequentially. Set a wakeup or check `show_characters action='status'` before each next trigger.
- ⚠️ **Style drift on Shot 13** (per `refs/README.md`) — solved by always passing `refs/style/style_anchor_watercolor.png` as a reference. Anchor file does not yet exist.
- ⚠️ **MCP description vs. behaviour for Soul training:** `images[]` accepts the public CDN URL form (`https://d2ol7oe51mr4n9.cloudfront.net/<user_path>/<media_id>.png`), NOT the raw `media_id` UUID despite what the description says. Documented in [refs/manifest.json](refs/manifest.json).
- ❓ **`docs/anima_grammar.md`** referenced by code, never committed. Need source.
- ❓ **Video model pricing** not yet probed on this account — first video gen calibrates the dominant spend line.
- ❓ **Mira character path** undecided (one-off vs. trained Soul).

---

## Quick commands

```bash
# Check Higgsfield balance
mcp: balance

# List all trained Souls
mcp: show_characters action="list"

# Check a specific Soul's training status
mcp: show_characters action="status" soul_id="1012370e-3cf7-486a-b644-88b174395b13"

# Generate VO samples for the whole cast
ELEVENLABS_API_KEY=... python scripts/generate_vo.py --all

# After Leena Soul reports ready, kick June Soul training (use URLs from refs/manifest.json)
mcp: show_characters action="train" name="June" images=[<june urls from manifest.json>]
```
