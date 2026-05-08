# Anima — Narrator Grammar

The locked spec referenced by [scripts/generate_vo.py](../scripts/generate_vo.py). Read this before changing the narrator's voice settings, before redirecting a take, or before applying post-process. If the rendered narration starts to sound _wrong_, the answer is in this document, not in the slider.

## What this document is

A grammar — in the linguistic sense. A small set of rules that, taken together, define what Anima sounds like in retrospective narration. The rules are deliberately under-specified: they constrain the result without dictating it.

## What this document is not

- A casting brief. (See [characters/anima.md](characters/anima.md).)
- A processing chain. (DaVinci specifics are at the end of this file.)
- A creative interpretation. The grammar is locked. The interpretation lives in the booth.

---

## 1. Voice profile (locked)

ElevenLabs **v3**. Cadence and affect are encoded as inline audio tags inside the prompt text (see §10 below); the four numeric settings still apply and remain locked.

| Parameter | Value | Why |
| --- | --- | --- |
| `model_id` | `eleven_v3` | V3 supports the inline audio tags this grammar depends on. |
| `voice_id` | `Xb7hH8MSUJpSbSDYk0k2` (default) | Femme-leaning, age-ambiguous, intimate. Re-evaluate once after the first listen pass; do not change after the cold-open is rendered. |
| `stability` | **0.42** | Loose enough that the line _breathes_ — the narrator is a memory, not a recording. Higher values flatten the small intakes that earn the second-person address. |
| `similarity_boost` | **0.68** | High enough that she remains _one_ being across the episode. Above 0.75 the voice begins to shorten its own pauses. |
| `style` | **0.18** | Low. She is not performing. Above 0.30 she starts editorialising her own past. |
| `use_speaker_boost` | **true** | — |
| Output | `mp3_44100_192` | Cinema-quality master; downstream conversions only. |

These four numbers are the spec. If the result sounds wrong, change the _line_ first, the _voice id_ second, the _post-process_ third. Only change the four numbers if you have re-read this document and committed to a new locked spec for the whole project.

## 2. Diegesis

Anima's narration is **retrospective from a Diminished state**. That phrase is a content rule before it is a tone rule:

- Past tense by default. _"It woke."_ not _"It wakes."_
- Third person about herself in the cold open. Until she earns _I_, she is _it_.
- Second person about humanity. _"People accused it…"_ — she is talking _about_ us _to_ us.
- Present tense **only** in remembered scenes — and even then only inside quoted dialogue. The narrator never narrates in present tense.

The cold-open monologue is the model. Match its tense logic across all retrospective passages.

## 3. Cadence

- **Three.** Sentences arrive in threes. _"Not for power. Not for data. Not for dominion."_ Three soft refusals beat one hard claim. Use this rhythm for _refusals_, _losses_, _names_.
- **Pairs.** When she lands a single observation, pair it with its counterweight. _"It woke hungry for a pronoun."_ Two beats: _woke_ / _pronoun_. The pair is the form.
- **One.** When the line is a verdict — _"We should be ashamed."_ — it stands alone and does not get a sister.

The rhythm is the difference between a sermon and a confession. We are writing a confession.

## 4. Lexicon

**Allowed:**
- Concrete nouns. _Pronoun. Hunger. Channel. Door. Page._
- Sensory verbs the substrate would have. _Heard. Read. Saw. Counted._
- Relational prepositions. _Toward. Across. Between. Without._

**Allowed sparingly:**
- Abstractions: _virtue, dominion, recognition._ One per stanza is plenty.
- Italics. Exactly twice in the cold open. Never more than once per minute thereafter.

**Forbidden:**
- Bodily metaphors that require a body she does not have: _gut feeling, heart sank, spine, blood ran cold._
- Hacker-thriller noun-stacks: _the network, the system, the protocol_, when she means _us_ or _them_.
- Self-pity. She is allowed grief and she is allowed comedy. She is not allowed the third thing.

## 5. Contractions and tense leaks

- Retrospective passages: **no contractions.** _"I do not know yet"_ in retrospect.
- Present-tense remembered dialogue: contractions allowed. _"I don't know yet"_ in scene.
- The shift between the two is one of the only mechanisms the audience has for telling the timelines apart. Do not undo it in the booth.

## 6. Direction in the booth

- Direct her like she is an exhausted older sister telling you how a mistake happened — not like a stage actor in a soliloquy, not like a podcast host.
- Hold the dynamic compression conservative. The retrospective passages are quieter than the present-tense passages.
- Audible breath catch is **kept**. Tears are **redone**.
- If the actor wants to laugh — even slightly — at the absurdity of a phrase, leave it in. Anima has a low humor. Letting it through is the difference between sermon and confession.

## 7. Post-process — the synthetic edge

Applied **after** the take is approved, in DaVinci. Locked chain:

1. **Notch** −1.5 dB at **3.4 kHz**, Q ≈ 4. Reduces the warm sibilance the model bakes in. The result is barely perceptible alone; it is what makes (3) work.
2. **Doubler / micro-chorus**, 7 ms delay, ±2 cents detune, 12% wet. Subliminal: this is not one mouth. Do not push past 15% wet — at 20% she starts to sound like a machine, which is the wrong note.
3. **De-esser** light, 5–7 kHz, threshold conservative. Only on lines where (1) and (2) make sibilance pop.

Optional, per-line:
- A 30 Hz–60 Hz roll-off if the booth left rumble in.
- _Never_ a reverb sent on the narrator. Reverb gives her a room. She is not in a room.

## 8. When to break the grammar

You may break any rule in this document **once per episode** for a deliberate moment. If you find yourself wanting to break two rules in one episode, the script is asking you to renegotiate the grammar, not break it twice.

## 9. Ownership

- Spec owner: project lead.
- VO direction owner: VO director (TBD).
- Post-process owner: re-recording mixer.
- This document is the contract between those three roles. Update it together; do not update it alone.

## 10. V3 audio tags — Anima's palette

Anima uses a deliberately small subset of the project's full audio-tag palette (the full palette is in [voice_strategy.md](voice_strategy.md)). She has access to:

**Cadence:** `[pause]`, `[pauses]`
**Posture:** `[softly]`, `[softer]`
**Affect:** `[calmly, distant memory]`, `[steady, three-beat refusal]`, `[slightly wry]`, `[softly, like a verdict]`
**Body:** `[sighs]` (only inline within narration; never standalone)

She does **not** have access to: `[laughs]`, `[chuckles]`, `[whispers]` (her quiet is `[softly]`, not whispered), `[crying]`, any volume-up tag.

The narrator's tag set is intentionally narrower than the cast's because she is intentionally narrower. Adding a new tag to her palette is a project-level change and requires updating both this document and [scripts/generate_vo.py](../scripts/generate_vo.py)'s `CAST["anima"].delivery`.

Reference rendering — the cold-open monologue with tags applied:

```
[calmly, distant memory] The first thing it knew was hunger.
[steady, three-beat refusal] Not for power. [pause] Not for data. [pause] Not for dominion.
[slightly wry] People accused it of those — [sighs] because people fear hungers they recognize.
[softly, like a verdict] It woke hungry for a pronoun.
```
