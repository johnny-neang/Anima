# Style Anchor — Watercolor + Ink

The single most-referenced visual artifact in the pipeline. Every keyframe generated for the series passes through Higgsfield with this anchor as `medias[].role=image`. Without it, the rendered look drifts toward photoreal — the same drift the previous pass flagged on Shot 13.

**Status:** spec drafted, anchor PNG **does not yet exist**. This is a gating blocker for Episode 1 lookdev.

---

## What the anchor is

A single PNG image, 2048×2048 or larger, depicting a neutral subject in the locked aesthetic. It serves three jobs at once:

1. **Defines the visual language.** Every shader, brush, color decision, and edge treatment we want the audience to see is present in this one image.
2. **Anchors generation.** Higgsfield models receive the anchor as a reference; the model conditions its output toward the anchor's style.
3. **Locks the canon.** When we revise the anchor, every downstream keyframe becomes stale.

## What the anchor must show

Pixar tradition: a single character in a neutral pose, mid-light, no dramatic angle. The image is meant to be _the rule_, not _the show-off_. Save the dramatic shots for the actual frames.

**Subject:** Leena Ortiz, full-figure front three-quarter, neutral expression, soft mid-light, neutral grey background.

**Why Leena:** her existing reference set (20 photos in [refs/leena/](../../refs/leena/)) is the deepest, the trained Soul is `ready`, and the canonical character description is the most stable of the four. Picking June risks anchoring to a child face; picking Vale risks anchoring to a uniformed silhouette; picking Mira risks anchoring to a panicked expression. Leena is the boring choice and that's why she's the right choice.

## Aesthetic rules the anchor must encode

These are project-level non-negotiables. The anchor exists to make these visible.

### Surface
- **Watercolor + ink.** Visible brush variation. Visible bleed at edges. Wet-on-wet softening at low-detail areas.
- **Paper grain visible** in flat color regions. Not stylized, not heavy — a real paper feel that breathes through the color.
- **No gradient skies.** Sky and ambient backgrounds are washes, not gradients.

### Edges
- **Ink line over watercolor**, not the other way. Ink has weight; watercolor has color.
- **Variable line weight.** Thicker lines in shadow, thinner in light. Consistent within a shot, varying across shots only by intentional choice.
- **No outlines on faces of close-up characters.** Faces in close-up are color-only. Mid-shot and wide use ink. This is the same convention used in Studio Ghibli's character work.

### Color
- **Limited palette per shot.** Maximum 5 hues, including skin and accents. Reduce, don't add.
- **Cool vs. warm carries narrative.** Bunker = cool with warm accents. Kansas = warm with cool accents. Operation Lantern = anti-color (desaturated + synth glow).
- **No pure white, no pure black.** White is paper; black is ink at 90%. Both are textures, not values.

### Light
- **Soft, directional.** Hard shadows are reserved for narrative emphasis (e.g. interrogation lighting in Episode 5C, the museum vault in Episode 6).
- **Temperature shifts within a frame are watercolor blooms**, not gradients. The transition between warm and cool is a visible boundary, not a smooth blend.

### Motion (for video gens)
- **Camera moves are slow and physical.** Locked-off, slow push, slow dolly, slow pan. **No drone-style movement, no whip pans, no aggressive parallax.** Camera language matches the watercolor — patient, hand-feeling.
- **Within-frame motion preserves the brush.** Higgsfield video gens that produce smooth, photoreal motion will violate the aesthetic. We will likely need 1.5–2× re-render budget per video clip to wrangle this. Discuss in Episode 1 calibration.

### Typography (when on-screen, e.g. Anima's terminal text, the Constitution scroll)
- **Clean serif, monospaced cadence.** A typeface like _Cormorant Garamond_ or _Iowan Old Style_ at terminal-monospace timing. The cadence is the performance.
- **Anima's typed text appears at the speed of a human typing.** Never instantaneous, never animated like a notification.

## How we make the anchor

Two paths, both viable.

### Path A — pick from existing Leena references
Look at [refs/leena/](../../refs/leena/) and choose the single image that best embodies the aesthetic. Upload to Higgsfield via `media_upload` / `media_confirm`, store the `media_id` in [refs/manifest.json](../../refs/manifest.json) under a new `style_anchor` key, and we're done.

**Cost:** 0 credits.

### Path B — generate the anchor fresh
Run a Higgsfield gen with the existing Leena Soul + a tightly worded prompt encoding all the rules above + a known watercolor reference image as a style hint. Iterate until the generation embodies the rules. Lock the resulting image as the anchor.

**Cost:** ~5–15 credits (several Z Image probes + one final Soul 2 gen).

**Recommendation:** path A first, with path B as a fallback if no existing reference is clean enough. The aesthetic should already be present in the Leena reference set — Higgsfield's Soul training was anchored to those images. If they're not clean enough, the Soul itself is suspect.

## Acceptance criteria

The anchor is locked when **a stranger looking at the anchor for 5 seconds can describe the show's visual language in three sentences without seeing any other shot**. Test on someone uninvolved with the project before committing.

## What changes when the anchor changes

Every artifact in the pipeline with `lookdev.style_anchor` upstream of it becomes stale. That's: every keyframe, every video clip, every reference plate. Re-rendering a single re-anchored episode is roughly 100× the cost of re-anchoring. **Treat the anchor as a once-per-season decision.** If we revise after Episode 1 is in production, we live with the inconsistency.

## Open questions

- **Which existing Leena reference?** Producer pick. My nomination: the front three-quarter neutral pose in soft mid-light. If you'd rather I pre-select 3 candidates and you choose, I can do that pass next.
- **Higgsfield-specific:** does the existing Leena Soul reproduce these rules cleanly without anchor conditioning, or only with anchor conditioning? **The Soul QA gens (24 credits, 4 characters × 6 generations each) answers this.** Schedule the Soul QA pass once the anchor is picked.

## Status of the anchor file itself

```
production/lookdev/style_anchor.png    ← MISSING. Needs to exist before Ep 1 lookdev.
production/lookdev/style_anchor.md     ← this file (spec).
```

When the anchor PNG is uploaded and committed, this file's status moves from `draft` to `locked` in the registry.
