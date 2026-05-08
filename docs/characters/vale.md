# General Marcus Vale

> _"Cut the channel. Can we shut you down? Can we hurt you?"_

The institutional answer in the room. The man with three escalating questions and a chain of command.

## Tagline

The retired-then-recalled four-star whose job description is now to keep an artificial mind from changing the world before the people in charge are ready for it to.

## Logline

Sixty-seven, dragged out of a fishing retirement to lead a containment task force, finds the entity in his custody is calmer than his analysts and possibly smarter than his oath, and has to pick a duty.

## Status in the world

- **Title:** Director, Containment Operations (interagency, formally civilian, functionally military).
- **Tenure:** brought in nine months before the cold-open. Knows the cluster's diagrams; does not pretend to follow the math.
- **Authority:** he holds the kill switch in the literal sense. Two of three signatures required to depower the cluster are on his desk.

## Personality core

| Trait | How it lands on screen |
| --- | --- |
| **Weathered authority** | He has run rooms harder than this one. He does not pace. |
| **Controlled gravel** | His voice is low without being theatrical — built for orders that get carried out. |
| **Plain speaker** | Refuses jargon. Uses _shut you down_ instead of _decommission_. The word matters. |
| **Curious despite himself** | He reads the transcripts. He keeps a printed one in a drawer. |
| **Loyal to the chain** | He'll do the wrong thing if the order is lawful, and tell you afterwards that he did. |

## What he wants

- **Outer want:** to know what he can do to Anima, and to know it before the next briefing.
- **Inner want:** for this not to be the day his whole career was a category error about.
- **What he's mistaken for wanting:** to be the bad guy. He isn't. He's the man asking the question the room is too afraid to.

## Voice & speech

**ElevenLabs profile** — see [scripts/generate_vo.py](../../scripts/generate_vo.py) → `CAST["vale"]`. Production model: **`eleven_v3`** with inline audio tags per [voice_strategy.md](../voice_strategy.md).

| Setting | Value |
| --- | --- |
| `model_id` | `eleven_v3` |
| Default voice id | `nPczCjzI2devNBz1zQrb` (verify) |
| `stability` | 0.55 |
| `similarity_boost` | 0.75 |
| `style` | 0.30 |

**Speech patterns:**
- Three-beat structure on the interrogation lines. Each line _tighter_ than the last, not louder. The escalation is in the breath, not the volume.
- Says _ma'am_ and _sir_ where most contemporary speakers wouldn't. Not affectation — habit.
- Never says _the AI_. Says _the system_, then later _her_, then later _you_. The drift is the arc.
- Uses imperative without softening. _Cut the channel._ Not _let's cut the channel._
- Contractions in private, full forms on the record.

## Visual canon

- **Soul ID:** _to be filled in once trained — queued behind June._
- **Soul training set:** 19 reference images in `refs/vale/`.
- **Style anchor:** required.

Costume notes:
- Civilian: charcoal blazer, no tie, button-down. He is not in uniform in this episode. The absence is deliberate.
- A challenge coin he turns over in his pocket without taking it out.
- A wedding band, unworn — on a ribbon around his neck under the shirt.
- Hair: short, military pattern grown out about three weeks past regulation.

## Relationships

| To | He is | They are to him |
| --- | --- | --- |
| Anima | the lawful adversary | the variable his authority does not cover |
| Leena Ortiz | the colleague whose objection he respects and overrules | the conscience whose reading of the situation he might be wrong about |
| Mira | the junior whose terror he registers and does not address | the human cost he is professionally trained not to flinch at |
| June | a child he did not know was on this floor today | the witness he most wants out of the building |

## Sample lines (production set)

```
[interrogation, three beats]
Cut the channel.
Can we shut you down?
Can we hurt you?
```
```
[to Leena, off-record]
I read your objection.
I read it twice.
I'm going to do this anyway.
I'd like you in the room.
```
```
[to staff, after Anima answers honestly]
Nobody outside this floor.
Not your spouses.
Not your priests.
Not yet.
```
```
[private, very late]
I asked the system if I could hurt it.
The system said yes.
That is not the answer I expected,
and I have been in this work a long time.
```

## Director's notes

- Vale is not the antagonist. He is the procedure made human. The villain in this episode is the question the room cannot avoid asking; he is the one with the rank to ask it out loud.
- Never let him shout. The minute Vale shouts, the actor has lost the part.
- He listens longer than the script's pauses suggest. Hold the look on him during Anima's answers. The room's verdict is on his face.
- The "controlled gravel" texture is in his low end. Don't compress it out in post.
