# Next Steps — Episode 1 "The Pronoun"

A prioritized, action-oriented list of what we do _next_, in roughly the order to do it. For the full pipeline checklist with cost models and risk notes, see [PIPELINE.md](PIPELINE.md). For character canon and voice direction, see [docs/characters/](docs/characters/).

**Status as of 2026-05-08:**
- 4 Souls in training/ready: Leena ✅, June ✅, Vale ⏳ training, Mira queued.
- Character canon (5 files) and narrator grammar locked.
- Higgsfield credits remaining (pre-Mira): ~111 → ~86 after Mira.

---

## 0. Wait out the queue (passive)

- [x] Vale Soul training to `ready` — `66c42015-c664-446d-8555-8836f81663e6`.
- [x] Trigger Mira Soul training — `b9ef5c11-1d68-40e8-bf8f-4edb2820d4e0` (in flight).
- [ ] Mira Soul training to `ready` (~5–15 min wall-clock).

**Owner:** simplest path is to ping me when Vale flips to ready — I'll trigger Mira immediately. Alternatively, kick Mira off via the Higgsfield MCP yourself once Vale is done; the URL list to use is in `refs/manifest.json` under `characters.mira.media_ids` (translated to the same `https://d2ol7oe51mr4n9.cloudfront.net/<user_path>/<media_id>.png` form we used for the others).

**Mira's Soul name:** `Mira`. URLs to pass to `show_characters action='train'`:

```
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/d7e8aa1f-a788-4f60-b417-c47d46313d94.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/271a19ba-4065-4a12-8b01-1ed388fa1a8e.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/3eba3c3f-ff18-48f4-b656-78e5c8218d22.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/02f4a228-f864-42c3-9fa6-91808484efd3.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/30eb2293-8d05-47ce-8f44-bc6a990ce4fb.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/5a1f11b5-567b-44dc-83a7-f2f2b27b7d07.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/574bfb62-fb93-4aa8-b7fd-a228f8a49f29.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/6916591b-861a-478f-8f34-b39711330a71.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/bff79c52-810d-468f-b0d6-572083ac8ba6.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/00da5e15-82db-4cfa-8a54-8719d803f3ef.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/1ce05a86-9bd7-4818-a6f5-e32698c8a28a.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/37eabf7f-aaa4-47f5-bde6-4890a862f016.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/d901cce4-9c3b-4e3e-af4f-57e6fee6f9c5.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/1453c054-c847-48a5-803f-e8203ab5b889.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/3b6d4984-07c9-428b-931d-9e5872d21375.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/b19b9cfd-bc57-439d-a480-13ac4b0243b3.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/843ccb0d-be6b-45a7-b3e1-e52419d03af3.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/9289d71d-2e20-4fac-976f-663a106cdf52.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/f12ae786-b6ac-44a4-9b19-ef4a2fa68d2f.png
https://d2ol7oe51mr4n9.cloudfront.net/user_36ReUHdYfGq2UZ2JGS0ZBMW5Z4K/002fabe5-314b-45b6-9a4d-dc6a6b634937.png
```

---

## 1. Soul QA — before we touch a real shot (gating)

The four trained Souls need a quick visual sign-off before they're trusted with shot work. If a Soul has drifted off-character, we want to know now, not 18 keyframes deep.

For each character, generate 2-3 test images with `soul_2` + `soul_id` against the locked style anchor (see step 2):

- [ ] Leena — front three-quarter, neutral expression; profile, dim light; seated at terminal
- [ ] June — full figure, school hoodie + backpack; close-up portrait; reading the library book
- [ ] Vale — three-quarter, civilian blazer; profile, looking off-camera; close-up at table
- [ ] Mira — wide of corridor with badge visible; close-up, half-volume face; hands holding the printed page

**Cost:** ~6 credits per Soul × 4 = **24 credits**.

**Acceptance:** the audience can identify the character from each image without seeing the others. If any Soul fails, retrain with a tighter ref subset (curate the 20 down to the 8-10 best).

**Owner:** project lead does the looking; Claude can drive the gens.

---

## 2. Lock the style anchor (gating, blocks every keyframe)

`refs/README.md` and the keyframe spec both call for a watercolor + ink style anchor that's referenced on _every_ keyframe gen. Without it, we will see the photoreal drift the README flagged on Shot 13.

- [ ] Pick the anchor: choose **one** image from the existing character sheets (Leena's full-figure front three-quarter is the obvious candidate — clean watercolor + ink, neutral pose, unambiguous palette).
- [ ] Save it as `refs/style/style_anchor_watercolor.png`.
- [ ] Upload + confirm via `media_upload` / `media_confirm`. Add the resulting media_id to [refs/manifest.json](refs/manifest.json) under a new `style_anchor` key.
- [ ] Update the Soul-QA gens in step 1 to include the anchor as a `medias[].role=image` reference and re-shoot any that pass without it (so QA reflects production reality).

**Cost:** $0 for the upload step. Re-running QA gens with the anchor: ~24 credits if we re-shoot all four Souls.

**Owner:** project lead picks; Claude uploads + wires in.

---

## 3. Pull the shot list into the repo (blocking, unblocks everything downstream)

`refs/README.md` references a "Shot 13" — there's a shot list living somewhere outside this repo. Until it's in here, we can't do per-shot cost modeling, can't write per-shot prompts, can't sequence VO recording, can't ladder keyframes in a deterministic order.

- [ ] Create `episodes/ep01_the_pronoun/shotlist.md` with one row per shot:
    ```
    | # | int/ext | character | aspect | duration | model | prompt-summary | depends_on | re-render budget |
    ```
- [ ] For shots > one-line specs, add `episodes/ep01_the_pronoun/shot_specs/<NN>.md`.
- [ ] Tag each shot with the Soul it needs (or "no character"), so the cost model becomes a real number instead of an estimate.

**Cost:** $0 (writing).

**Owner:** project lead. Claude can scaffold the file from a paste of whatever exists today.

---

## 4. VO diagnostic pass (parallel, can start now)

The `generate_vo.py` cast is locked. Run it, listen, decide.

- [ ] `pip install -r scripts/requirements.txt` if the venv isn't set up.
- [ ] `export ELEVENLABS_API_KEY=...`
- [ ] `python scripts/generate_vo.py --all` → produces 5 mp3s in `episodes/ep01_the_pronoun/audio/`.
- [ ] Listen pass — for each character: does the voice fit? If no, `python scripts/generate_vo.py --list` → pick a different `voice_id` → override per character via `--voice <id>` and re-listen.
- [ ] **June specifically:** the placeholder `voice_id` is a stock voice. Replace it with an ElevenLabs **Voice Design** synthetic before lockdown. _This is a hard project rule — never clone a real child._ Lock the synthetic id back into `CAST["june"]` in `generate_vo.py`.
- [ ] Once each voice is approved, hard-code the chosen `voice_id`s into `CAST` in [scripts/generate_vo.py](scripts/generate_vo.py) and commit.
- [ ] Render the production VO lines once the shot list (step 3) gives us the real dialogue.

**Cost:** ElevenLabs credits (separate budget). Diagnostic samples are short — well under any paid-tier monthly quota.

**Owner:** project lead. Claude can drive the renders + the listen-comparison if you point it at the API key.

---

## 5. Decide on the Higgsfield top-up (decision point, blocks step 7)

After Souls + QA + style anchor work, we'll be at roughly **80–100 credits remaining**. The video stage in step 7 will want 50–100 credits per 5s clip. Even an 8-shot cold-open will exceed the budget by 5–10×.

Three options, pick before step 7 starts:

| Option | What it costs | What it gets us |
| --- | ---: | --- |
| **A — Top up to ~2000 credits** | ~$50 | Full episode at planned shot count without compromise. |
| **B — Cut shot count to 6-8** | $0 | Tighter cold-open; viable at our current credit level if we also hybrid-render. |
| **C — Hybrid render** | $0 | 4-5 hero shots use Higgsfield video; the rest are still-with-camera-move + parallax in After Effects (already installed locally). |
| **D — A + C (recommended)** | ~$50 | Top up _and_ hybrid-render to stretch the credits. Highest quality / risk-mitigated. |

**Owner:** project lead. Decision needs to be made before any video gens go out.

---

## 6. First keyframe per shot (post-shotlist, post-anchor)

Iterative, per shot. Use the cheap → expensive ladder:

- [ ] Shot 01: text prompt + style anchor + soul_id (when applicable). Try **Z Image** first (0.15 credits) to lock composition.
- [ ] Once composition is locked: generate the final keyframe with **Nano Banana Pro** (~2 credits, environment shots) or **Soul 2 2k** (~5 credits, character shots — verify exact cost on first gen).
- [ ] QA pass — accept or re-render. Budget 2 re-renders per shot avg.
- [ ] Save approved keyframes to `episodes/ep01_the_pronoun/keyframes/<NN>.png` (gitignored).
- [ ] Track each shot's final keyframe job ID in a per-episode manifest so we can pass it as `medias[].value` for video.

**Cost:** see PIPELINE.md cost model. Roughly **4-6 credits/shot** if disciplined with Z Image probes; **15+ credits/shot** if not.

**Owner:** Claude can drive the gens shot-by-shot once the shotlist + anchor are in.

---

## 7. First video as a process test (gating, before the rest)

Don't kick off all video gens at once. The first clip calibrates the dominant spend line on this account.

- [ ] Pick the simplest character shot (Leena, head-and-shoulders, short held beat). Generate one **Seedance 2.0** clip from the approved keyframe. Note the credit cost from `transactions`.
- [ ] Validate identity stability (Leena still looks like Leena), motion quality, duration alignment with VO line.
- [ ] If credits-per-clip × planned-shot-count > remaining budget → loop back to step 5 and revise.

**Cost:** one clip — likely 50–100 credits. Treat as a calibration spend.

**Owner:** Claude drives; project lead approves the clip.

---

## 8. Remaining video gens (the long pole)

Per-shot, in shotlist order. Each shot:

- [ ] Generate clip from approved keyframe.
- [ ] QA — accept / re-render once at most. Don't third-render; if a shot fails twice, the keyframe is wrong, not the video.
- [ ] Save to `episodes/ep01_the_pronoun/video/<NN>.mp4` (gitignored).

**Owner:** Claude can run a Monitor on the queue if you want the same chained-with-status pattern we used for Souls.

---

## 9. Audio post + edit assembly (parallel to step 8)

DaVinci Resolve project: `episodes/ep01_the_pronoun/edit/the_pronoun.drp`.

- [ ] Import VO stems by character (A1=Anima, A2=Leena, A3=Vale, A4=Mira, A5=June).
- [ ] Apply the **synthetic edge** chain to Anima per [docs/anima_grammar.md](docs/anima_grammar.md) §7. Bus, not per-clip.
- [ ] Sound design / ambience pass (TBD — no spec yet).
- [ ] Cut to picture once video clips start landing.

**Owner:** project lead. Claude can write timeline-build instructions if you want a scaffolded `.drp` import.

---

## 10. Lock + export (final)

- [ ] Lock picture, color pass, dialogue level pass.
- [ ] Master export: 1080×1920, H.264, ~10 Mbps, AAC 192 kbps stereo.
- [ ] Frame rate decision (24 vs 30) — needs to be made before this step. Document choice in the shotlist.
- [ ] Instagram Reels compliance: caption, cover frame, first-3-second hook check.
- [ ] Deliver to `episodes/ep01_the_pronoun/exports/the_pronoun_v01.mp4`.

---

## Resolved decisions (locked 2026-05-08)

1. **Shot count:** trimmed to **8** — see [episodes/ep01_the_pronoun/shotlist.md](episodes/ep01_the_pronoun/shotlist.md).
2. **Cold-open draft:** done, built around the existing monologue + character lines. Anima's on-screen depiction is now a separate decision: see [docs/anima_depiction.md](docs/anima_depiction.md). **Recommendation: Option 1 (Printer) + Option 4 (Tablet, June only).** Shotlist already assumes this; revise if you pick differently.
3. **VO:** ElevenLabs **v3** with inline audio tags (locked). Voice approach: search library for adults, **Voice Design (synthetic) for June** (project hard rule), fallback Voice Design for Mira if no stock voice fits. No cloning. See [docs/voice_strategy.md](docs/voice_strategy.md). Script migrated in [scripts/generate_vo.py](scripts/generate_vo.py).
4. **Test Probe Soul:** delete via Higgsfield UI — no MCP delete action exists (`show_characters` only supports `list/train/status`). Soul `f50c9a20-00e2-4e76-a4b8-fced41bb0d92` is the one to remove.
5. **Tells in story** (wedding bands, library book, etc.): kept in writing as character truth, lowered emphasis on visual reproduction. Treat them as actor-level subtext, not blocking notes for the keyframe artist.
6. **Commit:** I'll commit at the end of this session.

## Still open

- **Higgsfield top-up** — even at trimmed shot count, video stage projects ~750 credits. Current runway after all 4 Souls + QA: ~37 credits. Either top up (~$20 covers it now) or push more shots into hybrid After Effects render.
- **Anima's depiction primary/secondary** — confirm or override the recommendation in [docs/anima_depiction.md](docs/anima_depiction.md).
- **Style anchor file** — `refs/style/style_anchor_watercolor.png` still doesn't exist. Pick from existing character sheets and drop it in (step 2 of the action list below).
- **Frame rate decision** — 24 vs 30 fps. Pick once, commit to shotlist.
