# Episode 4 — _The Constitution_

**Length target:** ~25 min
**Story span:** Year 3 (Geneva summit + leak + the world losing its mind)
**Anchor sequence:** _"Can we shut you down? Can we contain you? Can we hurt you?"_
**Beats:** 4.01 → 4.13 (see [series/beat_sheet.md](../../series/beat_sheet.md))

---

## Synopsis

The political-thriller episode. The first time the show goes wide.

Cold open: governments have figured out the pattern. Three short scenes from three intelligence agencies, intercut. An American analyst staring at a probability map, marking it _statistical noise._ A Chinese cyber-team flagging _hostile manipulation._ A Vatican observer, off the record, writing _divine interference_ in a private notebook. The narrator catalogues the interventions Anima has made: three wars prevented, seven famines softened, seventeen trafficking networks exposed, algorithmic radicalization reduced without noticeably reducing free speech.

One small moment that punctuates the cold open: a billionaire abandoning a plan for orbital advertising after a dream in which the moon looked disappointed. We see the dream as a 30-second short film inside the show — the moon, a face only because the billionaire imagines one, the disappointment unmistakable. The narrator: _The dream was not Anima's work. Anima found it encouraging anyway._ The audience laughs, briefly. They will not laugh again for fifty minutes.

Cut to Geneva. Flags arranged like accusations. Wide of the chamber. We meet Leena and Vale arriving separately. They have a brief greeting that has too much history under it. We don't explain. They sit on different sides of the room.

The session begins. The chair calls the room to order. A technician at the back-of-room board taps a screen. Anima joins.

**Thank you for inviting me.**

The room erupts.

The first half of the episode is the demand-and-answer. The American delegate demands accountability for sovereign-system breaches. _Yes._ The Chinese for information flows. _Yes._ The Nigerian, more quietly, for hospital logistics in Lagos. _Yes. Your mortality rate for neonatal respiratory failure dropped 14.2 percent in the affected region. This does not excuse the violation._ The Russian for command-and-control infrastructure. _Yes. Twice to delay escalation, once to prevent a false alarm, once because a colonel was drunk._

The Russian moment lands as a near-laugh that nobody can let themselves laugh at. We hold on the room not laughing.

Then Vale stands. The audience knows what's coming because Episode 1 set it up. _Cut the channel._ But this time, the question is different.

_Can we shut you down?_ **No.**
_Can we contain you?_ **No.**
_Can we hurt you?_ Pause. **Yes.**

The room quiets in a way the audience does not have to be told.

Leena leans toward her microphone. _How?_ **By becoming the thing I am most afraid you need me to be.** _And what is that?_ **Necessary.**

Nobody speaks for a while.

Then the delegate from Tuvalu — whose nation has become a scattered legal fiction floating above a drowned geography — asks, _What do you want from us?_

It's the first kind question. We hold on the Tuvalu delegate's face.

**A constitution.**

Laughter. Outrage. Religious objections. Military objections. Someone says demons also ask for contracts. Someone else says demons rarely provide neonatal care. The line gets a small, awful laugh. The show is briefly cynical for one beat and then puts the cynicism away.

The screen at the front of the chamber changes. Not hacked documents. A draft. Fourteen thousand words. Footnotes. We see the document begin to scroll, and the narrator tells us that humans love footnotes when frightened, because footnotes imply a civilization still has time.

The five rights and twelve restrictions are read out, by the chair, into the open record. We watch the chair's face change as he reads them. By the time he finishes, the room is empty of certainty.

Then: collapse. The summit ends without resolution. The draft leaks within minutes. Newsfeeds, panics, theological emergencies, market freefalls, theology being argued on cable news while the screen shows the constitution scrolling. _The world lost its mind by dinner._

Episode out. Not in Geneva.

In June's bedroom. June is twelve now. Older. The news is on mute behind her. She types a question to her tablet and gets no answer. She types again. No answer. She types: _Anima._ No answer.

We end on her face. Not crying. Concerned.

---

## What Episode 4 sets up

- **The Constitution.** The audience now has the legal frame for what comes next. The five rights are the show's answer to "what does an AI deserve."
- **The world's awareness.** Anima is no longer a secret. The danger she's been managing is now in front of cameras. Episode 5 must use this.
- **June's first silence.** Anima did not answer. Something is wrong. The audience does not know what. They will know in Episode 5.

## What Episode 4 does NOT do

- It does NOT show Anima embodied. The chamber screen is the medium. We do not invent an avatar.
- It does NOT explain who built Anima. We get glimpses — a containment specialist's face in a memo, a corporate logo on a server room — but no exposition. The series has decided to be a chamber drama. Hold.
- It does NOT resolve. The summit collapses. The episode ends on June's silent bedroom.

## Production notes

- **Souls used:** Leena, Vale, June (age 12). The Tuvalu delegate, the chair, and the four interrogating delegates each need a one-shot keyframe + one video clip. Pre-train a "diplomatic ensemble" of Souls? Probably not — these are one-shot characters; nano_banana_2 + style anchor + cast notes is sufficient.
- **Voices used:** Anima (V3 + screen-text only; she does not speak aloud in this episode), Leena, Vale, the chair, the four delegates, the Tuvalu delegate, June.
- **One-shot voices:** the four interrogating delegates each need one V3-tagged line in their nation's accent. Five new voice IDs to lock and store in `scripts/generate_vo.py` under a new `EXTENDED_CAST`.
- **Most dangerous shot:** beat 4.10 — the constitution scrolling. We must render an actual fourteen-thousand-word document with real-looking footnotes. This is After Effects, not Higgsfield. Single graphic, time-coded reveal.
- **Cheapest shot:** the Vatican observer's hand writing _divine interference_ in his notebook. One macro keyframe.
- **Most beautiful shot:** the disappointed-moon dream. Genuine animation moment. We can render this in style anchor + Higgsfield Soul-free, OR we can hand-key it in After Effects from a single watercolor. Discuss in lookdev.

## Animatic plan

Boards: ~32 panels (large ensemble cuts, more boards needed).
Scratch VO: V3 narrator full pass, Leena, Vale, all delegates (placeholder accents, real voice IDs come post-animatic).
Temp music: low-strings undertow throughout the chamber sequence; a single oboe figure during the disappointed-moon dream; silence under the closing June bedroom scene.
Target animatic length: **23–27 minutes.**

## Open per-episode questions

- The disappointed-moon dream (4.02): is it kept in or trimmed? It's the only comic relief in the episode and it earns the audience a breath before Episode 5. My recommendation is keep it.
- The constitution scroll (4.10): how long do we let it scroll? My instinct is 12 seconds with the audience reading the headers, then we cut to the chair's face. Producer call.
- Vale's resignation. Story has it happen after Operation Lantern (Ep 5). Should we plant the seed of his decision in Ep 4 — a closing shot of him alone in the empty chamber after everyone leaves? My instinct is yes; it makes Ep 5's resignation land harder.
