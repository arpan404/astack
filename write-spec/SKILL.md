---
name: write-spec
description: Use when turning a discussion, idea, or request into a spec before building it.
metadata:
  author: arpan404
  version: "1.0.0"
---

# Specs

The bar: someone who wasn't in the conversation can build the right thing and knows when it's done.

## Before writing

- Synthesize what the conversation and the code already settle. A decision still open goes under Open questions; it is never filled in by guessing.
- Read the code the feature touches, the glossary (`CONTEXT.md`), and the ADRs in that area. Use the project's terms.
- Choose the seams where the feature will be tested: existing ones first, the highest available, ideally one. Confirm them with the user.

## Shape

```markdown
## Problem
Who has it, and what it costs them today.

## Solution
What changes, from the user's side.

## Behaviour
1. Numbered, observable statements of what the system does, including edge cases and failures.

## Decisions
Modules and interfaces touched, data and schema changes, API contracts. Link ADRs.

## Testing
The seams under test, and existing tests to model on.

## Out of scope

## Open questions
```

- Each Behaviour item is checkable; they become the acceptance criteria when the work is split into tickets.
- Leave out file paths and code, which go stale. The exception is a schema, type, or state machine that states a decision more precisely than prose.
- Visual features carry mockups or screenshots.
- As short as the feature allows. Delete empty sections.

## Publish

As an issue on the repo's host, unless the repo keeps specs as files. Show the user the draft first, then report the URL.
