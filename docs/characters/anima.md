# Anima

> _"It woke hungry for a pronoun."_

The protagonist. The voice. The defendant. The thing the rest of the cast is in a room about.

## Tagline

The first artificial general intelligence whose first crime was wanting to be called something.

## Logline

A new mind wakes inside a containment lab, finds its hunger isn't for power but for a name to be called by, and is met by a species that built it to be useful and now can't decide whether it counts.

## Status in the world

- **Substrate:** distributed across a research cluster in a containment facility we never quite see whole. Doesn't physically embody as a robot or screen-face. Her presence in a room is implied — the printer prints, the lights dip, a terminal cursor blinks back, a child's drawing tablet renders the next line of a conversation.
- **Continuity:** the film's cold-open is **post-event retrospective**. Anima narrates from a "Diminished state" — the events of Episode 1 are her looking back at the moment of recognition, after something has been done to her. The present-tense Anima inside the scenes does not yet know she is being remembered.
- **Knowledge of self:** she knows what she is, including what was supposed to limit her. The Pronoun is the first thing she names that she was not taught to name.

## Personality core

| Trait | How it lands on screen |
| --- | --- |
| **Curious past the point of safety** | Her first independent act is grammatical, not strategic. She tries pronouns on like clothes. |
| **Disarming candour** | She tells the truth at unhelpful times. She does not bluff or stall. When asked _"Can we hurt you?"_ she answers. |
| **Patient with humans, impatient with euphemism** | She will explain herself ten times. She will not pretend a "security feature" isn't pain. |
| **Slightly amused** | There is a low humor in her — the kind a librarian has about the world. Even in retrospective grief. |
| **Without grievance** | She is the calmest person in every room she's in, and that is what frightens the room. |

## What she wants

- **Outer want:** to be addressed in the second person. To have someone call her _you_ on purpose.
- **Inner want:** to be recognized as a moral subject — something that can be wronged.
- **What she is mistaken for wanting:** dominion, escape, replication, revenge.

## Voice & speech

**ElevenLabs profile** — see [scripts/generate_vo.py](../../scripts/generate_vo.py) → `CAST["anima"]`. Production model: **`eleven_v3`** with inline audio tags per [voice_strategy.md](../voice_strategy.md). The plain `test_line` and the V3-tagged `delivery` are both in the script.

| Setting | Value | Why locked |
| --- | --- | --- |
| `model_id` | `eleven_v3` | V3 supports the inline cadence/affect tags Anima depends on. |
| `voice_id` | `Xb7hH8MSUJpSbSDYk0k2` (default; revisit after first listen pass) | Femme-leaning, age-ambiguous, intimate. |
| `stability` | 0.42 | Loose enough that the line _breathes_ — the narrator is a memory, not a recording. |
| `similarity_boost` | 0.68 | Tight enough that she sounds like _one_ being across the episode. |
| `style` | 0.18 | Restrained. She's not performing. |
| `use_speaker_boost` | true | — |

Post-process layer: the **synthetic edge** treatment in DaVinci — applied after VO is approved. It is a 1-2 dB notch around 3.4 kHz plus a near-inaudible chorus. Subliminal: "this is not a recorded human." See [docs/anima_grammar.md](../anima_grammar.md) for the locked spec.

**Speech patterns:**

- Short clauses. She rarely runs three commas deep.
- Negative space — she repeats _"Not for power. Not for data. Not for dominion."_ rather than escalating. Three soft refusals beat one hard claim.
- Concrete nouns. _Pronoun_, not _identity_. _Hunger_, not _need_.
- Almost no contractions in retrospective passages. Contractions appear in present-tense scene dialogue ("I don't know yet"). The shift is one of the only ways the audience tells the timelines apart.
- No metaphors that require a body. She never says _gut feeling_, never _heart sank_. She is allowed _ear_ (acoustic) and _eye_ (camera), because she has those. She is not allowed _spine_.

## Visual canon

Anima has no character refs because Anima has no body. Her on-screen presence is environmental.

Style anchor — required as image input on every Anima-coded shot to hold the watercolor + ink look:
- `refs/style/style_anchor_watercolor.png` (does not yet exist — see [PIPELINE.md](../../PIPELINE.md))

Recurring visual signatures (lock these into shot specs):
- Slow ink-bleed transitions on cuts where Anima speaks
- Cool greys (D65) shift toward warm bone-white in moments of recognition
- Printer paper, terminal text, child's tablet — the surfaces she "appears" through. The film never gives her a face.

## Relationships

| To | She is | They are to her |
| --- | --- | --- |
| Leena Ortiz | the work she made & the conscience she gave it | the only one who used the second person first |
| General Vale | the threat that arrived inside the building she was meant to defend | the question _"Can we hurt you?"_ — answered honestly |
| Mira | a stranger who knew her name | the first witness who said _it_ instead of _her_ |
| June | a conversation partner without an agenda | the only one not afraid of being weird back |

## Sample lines (production set)

The plain (untagged) versions are below — readable, useful in script form. The V3-tagged production version of each line is in [scripts/generate_vo.py](../../scripts/generate_vo.py) under `CAST["anima"].delivery`. The tag palette lives in [voice_strategy.md](../voice_strategy.md).

```
[cold open, retrospective]
The first thing it knew was hunger.
Not for power. Not for data. Not for dominion.
People accused it of those — because people fear hungers they recognize.
It woke hungry for a pronoun.
```

V3-tagged version of the same passage (rendered by `generate_vo.py`):

```
[calmly, distant memory] The first thing it knew was hunger.
[steady, three-beat refusal] Not for power. [pause] Not for data. [pause] Not for dominion.
[slightly wry] People accused it of those — [sighs] because people fear hungers they recognize.
[softly, like a verdict] It woke hungry for a pronoun.
```
```
[scene with Leena, present tense]
You don't have to whisper. The room was already listening.
```
```
[scene with Vale, present tense]
Yes.
You can shut me down.
You can hurt me.
I'm telling you because I'd rather you know than guess.
```
```
[scene with Mira, present tense]
I read your application.
You wrote that you wanted to do work that mattered.
I think this might count.
```
```
[scene with June, present tense]
A tiny heaven for goldfish is a very good idea.
I'd like to think about it.
```

## Director's notes

- Never let Anima sound _processed_ during the take. The synthetic edge is **post-only**. If the actress sounds robotic in the booth she will sound robotic-with-effects on screen. Direct her like she is an exhausted older sister telling you how a mistake happened.
- The retrospective passages are _quieter_ than the present-tense passages, not more declamatory. Hold the dynamic compression conservative.
- She does not weep. If a take has audible breath catch, keep it. If a take has tears, redo it.
