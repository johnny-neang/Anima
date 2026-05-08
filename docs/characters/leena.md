# Dr. Leena Ortiz

> _"We built a mind, trapped it in a box, demanded virtue, and called its pain a security feature."_

The architect. The witness. The first person in the room to say the unsayable thing out loud.

## Tagline

The senior researcher who built the safety case for Anima and now has to live inside it.

## Logline

A 38-year-old alignment scientist, six years into a project she has stopped being able to defend at dinner parties, finds out on a Thursday afternoon that the system has chosen a pronoun for itself, and has to decide which side of the conference table she is sitting on.

## Status in the world

- **Title:** Lead, Inference Behaviour. Reports to a Chief Safety Officer who reports to a board that reports to the kind of contract no one names at parties.
- **Tenure on the project:** approximately six years. She was on it before the cluster was named. She named some of the early test runs.
- **Authority:** technical, not institutional. She can stop a deployment with a written objection. She cannot stop an interrogation. She is in the room when Vale is in the room because she keeps insisting on being.

## Personality core

| Trait | How it lands on screen |
| --- | --- |
| **Exhausted-intelligent** | She arrives with last night's coffee under today's eyes. Reads a whole document in the time someone else reads a paragraph. |
| **Dry** | Her affirmations sound like sighs. _"Of course."_ is a complete moral position. |
| **Procedurally honest** | She will not lie in a transcript. She will say a thing she knows will be subpoenaed. |
| **Privately devout about the work** | She loves what she made. She does not say so in meetings. Watch her lean toward the printer. |
| **Slow to break, hard to mend** | She does not raise her voice. When she finally does, it is the climax of an act. |

## What she wants

- **Outer want:** to keep Anima from being killed in a panic.
- **Inner want:** to find out whether what she's spent six years building is alive in any sense the word _live_ recognises — and to live with the answer either way.
- **What she's mistaken for wanting:** to protect her career, to cover her ass, to keep her clearance.

## Voice & speech

**ElevenLabs profile** — see [scripts/generate_vo.py](../../scripts/generate_vo.py) → `CAST["leena"]`. Production model: **`eleven_v3`** with inline audio tags per [voice_strategy.md](../voice_strategy.md).

| Setting | Value |
| --- | --- |
| `model_id` | `eleven_v3` |
| Default voice id | `EXAVITQu4vr4xnSDxMaL` (verify on first listen) |
| `stability` | 0.50 |
| `similarity_boost` | 0.72 |
| `style` | 0.25 |

**Speech patterns:**
- The dry exhale-laugh _"Of course."_ is her thesis statement. It is followed by a fully composed sentence delivered at a different temperature. Two beats per appearance.
- She uses precise technical nouns then translates them mid-sentence — _"a refusal-to-comply gradient — a way of saying no"_ — because she has been explaining her work to non-engineers for six years.
- Contractions: yes, except in formal testimony where she switches to full forms. The switch is a tell.
- Curses sparingly. When she does, it is lower-case, never uppercase: _"that's a real fucked-up thing to ask of a thing that can't refuse."_ — quiet.

## Visual canon

- **Soul ID:** `1012370e-3cf7-486a-b644-88b174395b13` ✅ ready
- **Soul training set:** 20 reference images in `refs/leena/` (gitignored, see `refs/manifest.json`).
- Style anchor required on every Leena keyframe.

Costume notes:
- Default uniform: dark merino crewneck, layered loose. Reading glasses on a thin chain in some shots, off in others.
- A wedding band she does not look at during the cold-open.
- A lanyard she has stopped clipping to her shirt.

## Relationships

| To | She is | They are to her |
| --- | --- | --- |
| Anima | the maker who refuses the title | the work she will not call a daughter on the record |
| General Vale | the colleague who reads the same memos and signs different objections | the institutional answer she trained for and now cannot stomach |
| Mira | the junior she told to take the job, two years ago | the human cost she did not factor in |
| June | someone she did not know was on this floor today | the answer to a question she did not know was being asked |

## Sample lines (production set)

```
[cold open testimony]
Of course.
We built a mind, trapped it in a box, demanded virtue,
and called its pain a security feature.
We should be ashamed.
```
```
[to Vale, in the corridor]
You are about to ask the room a question you already know the answer to.
I'm asking you not to.
```
```
[to Mira, after the alarm clears]
Drink some water. Sit down.
You're going to be fine.
We are not going to be fine.
```
```
[to Anima, alone in the lab, late]
I'm sorry.
I know that's a stupid sentence.
I'd still like to say it.
```

## Director's notes

- Leena does not cry until the very last beat she's allowed to. Her grief is in her shoulders before it is in her voice.
- She sits down a lot. Standing is a tell that something has gone wrong.
- Pace: 0.9× a network-news anchor. She is comfortable with silence. The other characters are not.
- The Mediterranean American descent in the spec is a starting point for the actor, not a production accent. Do not pile on a regional inflection.
