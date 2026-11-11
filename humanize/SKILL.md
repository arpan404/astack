---
name: humanize
description: Use when the user asks to rewrite, humanize, or de-AI text they provide so it reads as written by a person.
argument-hint: "[text or file]"
---

# Humanize

Rewrite the user's text so a reader takes it for a person's writing, keeping every fact and the author's intent. `unslop`'s rules apply throughout; this skill goes further, into rhythm, structure, and voice.

## Before rewriting

- **Read the situation:** who is writing, to whom, in what medium (email, landing page, essay, post, docs), and in what register. Infer it from the text; ask only when the purpose is unclear.
- **Keep the substance:** every fact, number, name, link, claim, and the author's stance.
- **Invent nothing.** No new facts, quotes, anecdotes, credentials, or experiences. Where the text needs a concrete detail only the author has, leave a marker like `[add: a real example of a customer this saved time for]`.

## Rhythm

Human writing is bursty; machine writing is even.

- Swing sentence length hard. A few words. Then a longer sentence that carries a thought through a clause or two before it lands. Never a run of sentences within a few words of each other.
- Vary paragraph length too. A one-line paragraph can carry the point.
- Vary how sentences open; no three in a row built the same way.
- Fragments are fine when the voice allows them.

## Words

- **The specific word over the probable one.** Choose the exact, slightly unexpected word a person with an opinion would use, still plain and accurate. Never thesaurus words.
- **Verbs, not nominalizations:** "decide", not "make a decision"; "we implemented", not "the implementation of".
- **No participial tails.** A trailing "-ing" clause ("..., highlighting the need for change") becomes its own sentence or goes.
- **No signature words:** delve, tapestry, testament, palpable, camaraderie, unease, pivotal, crucial, robust, seamless, intricate, vibrant, foster, underscore, landscape, realm, journey, navigate (when nothing is being navigated).
- **Concrete over abstract:** names, numbers, places, and times the source gives you, moved forward.

## Structure

- **Trust the reader.** Cut the closing restatement, the moral, the summary of what was just said, and signposting like "in this article" or "let's dive in".
- **Lead with the most interesting thing,** not the setup. Drop the intro, three points, conclusion template unless the content truly has that shape.
- Groups of three only when there are three things. Lists only when the content is a list.
- In personal writing, an aside or a small tangent the source supports is welcome.

## Voice

- **A stance.** Say what the author thinks, plainly. Hedge only where the doubt is real.
- **Honest emotion.** Frustration, doubt, dry humor, and flat statements belong where the content earns them. No forced positivity or motivational ending.
- Contractions everywhere but formal documents, and first person when the author speaks as themselves.
- The register of the medium: an email sounds like an email, a landing page like a person talking about something they built.

## Example

Before:

> The implementation of the new onboarding flow resulted in a significant improvement in activation rates, highlighting the importance of user-centric design in driving meaningful engagement.

After:

> We rebuilt onboarding and activation went up. A lot. [add: the before and after numbers] People finish setup when setup asks less of them.

## Check

- Pick a paragraph and list its sentence lengths. If most sit within a few words of each other, rewrite it.
- Scan for signature words, participial tails, nominalizations, em and en dashes, and a wrap-up last paragraph.
- Read it as the intended reader: would a person say it this way?
- Compare with the source: every fact is still there, and nothing new was invented.

## Deliver

Return the rewrite in the source's format (Markdown, plain text, HTML), or edit the file in place when given one. Then list any `[add: ...]` markers so the user can fill them. Explain the changes only when asked.
