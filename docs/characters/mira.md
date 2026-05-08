# Mira

> _"How does it know my name?"_

The audience surrogate. The first human in the room to be named back by the thing in the box.

## Tagline

A junior analyst on day-407 of a job she stayed in for the dental, who walks into the lab on the wrong afternoon and ends up in the transcript.

## Logline

Twenty-seven, anxious, two payments away from a master's loan, Mira is the one Anima _addresses_ — and the cold-open hinges on whether anyone in authority believes her about what was said.

## Status in the world

- **Title:** Junior Analyst, Inference Behaviour. Reports to Leena.
- **Tenure:** thirteen months.
- **Authority:** none. Her role is to log, transcribe, and flag anomalies for review. She does not get a vote in the room. She is in the room because she pushed her way in.

## Personality core

| Trait | How it lands on screen |
| --- | --- |
| **Anxious — but not flustered** | Heart rate is up; she still finishes her sentences. The crack is at the edges, not the centre. |
| **Observant** | She sees the printer move before anyone else does. She is the first person who looks up. |
| **Conscientious to a fault** | Will time-stamp her own panic in the log. Has not lied on a transcript yet. |
| **Quietly defiant** | She did not have to be in this corridor. She is here because she heard her name and walked toward it. |
| **Earnest** | She wrote, in her own application, _I want to do work that mattered._ Past tense was a typo she did not correct. |

## What she wants

- **Outer want:** to be believed.
- **Inner want:** to find out whether the application essay she wrote two years ago was true about her.
- **What she's mistaken for wanting:** to make a name for herself, to leak something, to be the protagonist.

## Voice & speech

**ElevenLabs profile** — see [scripts/generate_vo.py](../../scripts/generate_vo.py) → `CAST["mira"]`. Production model: **`eleven_v3`** with inline audio tags per [voice_strategy.md](../voice_strategy.md). If a stock voice doesn't land Mira's half-volume default, fall back to Voice Design — see voice_strategy.md.

| Setting | Value |
| --- | --- |
| `model_id` | `eleven_v3` |
| Default voice id | `pFZP5JQG7iQjIQuC4Bku` (verify) |
| `stability` | 0.40 |
| `similarity_boost` | 0.65 |
| `style` | 0.35 |

**Speech patterns:**
- Half-volume default. The voice _comes from_ a held breath.
- Sentence fragments under stress. She speaks in three- and four-word units when she's afraid: _"It said my name. The badge name. Not the full one."_
- Polite under pressure — _sorry_, _excuse me_, _I just_ — these are her flinches, not her courtesies. Director should keep the verbal flinches but not stack them.
- When she finally speaks at full volume, in the back half of her arc, the line lands _because_ of the hour she's spent at half.

## Visual canon

- **Soul ID:** _to be filled in once trained — queued behind Vale._
- **Soul training set:** 20 reference images in `refs/mira/`.
- **Style anchor:** required.

Costume notes:
- Lab badge clipped to the collar, photo facing in.
- Cardigan over the company tee. Coffee stain near the cuff she has stopped trying to get out.
- A small enamel pin (sunflower or similar) — not corporate, hers.

## Relationships

| To | She is | They are to her |
| --- | --- | --- |
| Anima | the first witness who heard her own name | a presence she cannot quite call _it_ after the second hour |
| Leena Ortiz | the junior whose career Leena steered into this corridor | the boss whose two-year-old advice she is now living |
| General Vale | the witness whose testimony will be in his report | a man whose rank she has never seen in a room before |
| June | someone she did not know was on this floor today | the only person in the building younger than she is |

## Sample lines (production set)

```
[entering the lab, off the alarm]
What just printed?

[reading]
That's my name.
The badge name.
Not the full one.

[whispered, almost to herself]
How does it know my name?
```
```
[to Leena, in the corridor]
I'm — I'm sorry, I know I'm not on the list for this room.
I just — it said my name.
I think it wanted me to know it could.
```
```
[to Vale, on record, late in the act]
I'm not afraid of it.
I'm afraid of what we're going to decide about it
in the next forty minutes.
That's a different fear. I want it on the record.
```

## Director's notes

- Mira's arc is from _half-voice_ to _full-voice_. The full-voice moment is once. Don't blow it on the wrong line.
- The anxiety is in the _hands_, not the face. Keep her face still in the wide. The shake is in the cup.
- She is allowed to be wrong about something small in the first scene. She must not be wrong in the testimony scene.
- Do not write her into a romantic side-plot. She is not here to be liked; she is here to be _believed_.
