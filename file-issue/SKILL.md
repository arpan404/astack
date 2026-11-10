---
name: file-issue
description: Use when filing, drafting, or rewriting an issue, including bug reports, feature requests, and tasks.
argument-hint: "[bug|feature|task] [what happened or what is needed]"
---

# Issues

Works on any host. Use the host's CLI.

The bar: someone holding only the issue can start work without asking a single question.

## Before writing

- Search open and closed issues with a few phrasings. When a duplicate exists, propose commenting on it instead.
- Use the repo's issue template and pick from the repo's existing labels.
- Investigate before writing. For a bug, reproduce it or find the failing code, and capture the exact error, the commit, and the environment. Ask the user only for what you can't find.

## Writing

One problem per issue. Keep it short: a 1 or 2 sentence summary, then only what the reader needs to act.

**Title:** specific and searchable, naming the symptom and where it happens. "Checkout returns 500 when coupon code is lowercase", not "Checkout broken".

By type:

- **Bug:** steps to reproduce, expected vs actual with the exact error in a code block, environment and commit, impact. Point at the suspected cause with `file:line`, marked `Suspected:`.
- **Feature:** the problem and who has it, before the proposal. Alternatives considered. Acceptance criteria as a checklist of observable outcomes.
- **Task:** the goal and why now, what is in and out of scope, and a done-when checklist.

Anything visual (a UI bug, a layout or design request) needs images: read [`references/images.md`](references/images.md).

Keep facts apart from guesses. Trim logs to the relevant lines. Redact secrets, tokens, and personal data. Link related issues and PRs by number.

## Filing

Show the user the title, labels, and body. File only after they approve, unless they said to file directly. Pass the body from a file so newlines render, then report the issue URL.
