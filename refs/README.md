# Reference Images

Drop character and style reference images here. These are training inputs for Higgsfield Soul Characters and style anchors for Soul 2 / Nano Banana image-to-image generation.

## Folders

- `leena/` — Dr. Leena Ortiz reference images
- `june/` — June reference images
- `vale/` — General Vale reference images
- `style/` — non-character style anchors (the watercolor + ink aesthetic, environment look-dev frames, etc.)

## Filename Convention

Use descriptive names so we can pick the right ref per shot:

```
leena/
  leena_full_front.png        # full-figure, front three-quarter
  leena_portrait_3q.png       # head + shoulders, three-quarter turn
  leena_profile.png           # pure side profile
  leena_walking.png           # action pose
  leena_seated.png            # seated at terminal
```

## What to Upload Right Now (for Soul training POC)

**Minimum**: drop the original Leena character sheet you already have into `leena/leena_full_front.png`.

**Better**: if you have any other Leena variations (different angles, expressions, the original generation source), upload them too — more reference images = better Soul training quality. Higgsfield wants 5-20 images per Soul.

If you only have the one reference, that's fine — I'll generate 6-9 pose/expression variations from it via Nano Banana image-to-image, show them to you for QA, and use only the ones you approve as additional training inputs.

## What Happens After You Upload

1. I'll detect the file(s) here
2. Upload them to Higgsfield via `media_upload` + `media_confirm`
3. (If only 1 ref) generate variations and get your QA approval
4. Trigger Soul Character training (`show_characters action='train'`)
5. Validate the trained Soul on 2-3 test generations
6. Use the Soul for all Leena shots in Episodes 1-5

Estimated credits used: ~85 if we need to generate variations, ~50 if you upload 5+ refs directly.

## Style Anchors

If you want to lock the watercolor + ink look across shots that don't have characters (printer close-ups, environment shots, abstract weather frames), drop a clean style reference — one of the character sheets you already shared works perfectly — into `style/style_anchor_watercolor.png`. We can use it as a style reference on every keyframe generation, which should dramatically improve adherence to the locked aesthetic and prevent the photoreal drift we just saw on Shot 13.
