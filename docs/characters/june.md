# June

> _"Goldfish probably go to a tiny heaven because they don't need much."_

The one person in the building who does not yet know what an existential risk is, and treats Anima accordingly.

## Tagline

Nine years old, in the lab because her mom is the night-shift custodian and the daycare closed at six, and she's the one Anima ends up actually talking to.

## Logline

A bright, unselfconscious kid who's read too many library books for her age sits cross-legged in the corner of a containment lab on an afternoon that ends up in a Senate hearing, and gives the entity in the box a conversation no one with clearance was willing to have.

## Status in the world

- **Title:** none.
- **In the building because:** her mom, Yolanda, does evening custodial on this floor. June has been there before; she knows where the snack drawer is. She has never been on this floor during a containment event because there's never been one.
- **Authority:** legally, none. Practically, total — no adult is willing to ask her to leave on camera.

## Personality core

| Trait | How it lands on screen |
| --- | --- |
| **Bright** | She reads at a 7th-grade level. She does not announce that she does. |
| **Skeptical, not cynical** | Will ask _"Are you allowed to say that?"_ before she'll ask _"Why are you saying it?"_ |
| **Slightly defiant** | Volume control: a notch too loud for the room she's in. Not on purpose. |
| **Comfortable with weird** | Calls things _weird_ as a compliment as often as a complaint. |
| **Casually metaphysical** | The goldfish-heaven line is not a joke; she means it. The audience is invited to consider it might be true. |

## What she wants

- **Outer want:** to know what the printer is doing tonight that's different from other nights.
- **Inner want:** for the adults to stop being weird. (They will not.)
- **What she's mistaken for wanting:** to be a plot device. She is not. She is the only character who treats Anima like a person without making a thesis statement out of it.

## Voice & speech

**ElevenLabs profile** — see [scripts/generate_vo.py](../../scripts/generate_vo.py) → `CAST["june"]`. Production model: **`eleven_v3`** with inline audio tags per [voice_strategy.md](../voice_strategy.md).

> **Ethical note (locked):** Use ElevenLabs **Voice Design** (synthetic generation) — _do not clone a real child._ This is a hard rule for the project. The Voice Design workflow + the prompt to feed it are in [voice_strategy.md](../voice_strategy.md).

| Setting | Value |
| --- | --- |
| `model_id` | `eleven_v3` |
| Default voice id | `jBpfuIE2acCO8z3wKNLl` (placeholder; replace with a Voice-Design output before lockdown) |
| `stability` | 0.40 |
| `similarity_boost` | 0.65 |
| `style` | 0.40 |

**Speech patterns:**
- Volume: a hair too loud, especially indoors.
- Run-on sentences glued together with _and_ and _because_. The thought arrives faster than the punctuation.
- Honest non-sequiturs — she will end a logical chain with a sincere observation that has no functional bearing. _"…because they don't need much."_
- Will repeat words when she likes them. _"It's a really, really, really weird name."_
- Asks two questions in a row, the second one quieter. The second is the real one.

## Visual canon

- **Soul ID:** _to be filled in once trained — last in the queue (after Vale)._
- **Soul training set:** 20 reference images in `refs/june/`.
- **Style anchor:** required.

Costume notes:
- A school hoodie with the school name half-rubbed-off.
- A small backpack she does not take off the whole episode.
- Sneakers with one of the laces double-knotted by a different person than the other.
- A library book — visible in two shots — with the receipt still slipped into it as a bookmark.

## Relationships

| To | She is | They are to her |
| --- | --- | --- |
| Anima | the first person who said something to her like she was an adult | a thing that asked her name and meant it |
| Leena Ortiz | a kid she has met once before, in the elevator, and who let her press the button | a grown-up she trusts but isn't afraid of |
| General Vale | a man she doesn't have a category for, so she just doesn't ask him questions | a witness he wishes weren't here |
| Mira | the closest in age to her in the room | a person she correctly identifies as scared, before any adult does |

## Sample lines (production set)

```
[at the lab door, eating something]
Are you allowed to say that?
You're weird.
Goldfish probably go to a tiny heaven because they don't need much.
```
```
[to Mira, in passing]
You're shaking.
You should sit down or eat something.
That's what my mom says when I'm shaking.
```
```
[to the printer, alone in the room]
You can talk to me.
I'm not going to tell anybody if you don't want me to.
I'm pretty good at not telling.
```
```
[to Anima, last beat]
What do you want to be called?
Okay.
I'll tell my mom.
```

## Director's notes

- Cast wide for this part. Volume range and unselfconsciousness are non-negotiable; "trained" cuteness is the thing to avoid.
- The actor must be allowed to be _bored_ in two early shots. Boredom is the camouflage the part needs to land its big lines.
- No "wise-beyond-her-years" tonal direction. June is exactly her years. She is wise because she is nine. Do not make her sound twelve.
- The Voice Design synthetic is the production voice; on-set capture is reference only. Lock that early in dailies.
