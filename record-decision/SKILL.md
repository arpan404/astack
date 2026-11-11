---
name: record-decision
description: Use when making, changing, or checking for architecture decisions (ADRs).
metadata:
  author: arpan404
  version: "1.0.0"
---

# Decisions

An ADR stops the next engineer, human or agent, from undoing a choice they don't understand.

## Find what's already decided

Before changing architecture, swapping a dependency, moving a boundary, or recording a new decision, check the ADRs.

1. **Locate them:** the folder `AGENTS.md` names, else common homes like `docs/adr/`, `docs/decisions/`, or `adr/`. No folder means no recorded decisions.
2. **Scan titles:** file names carry the topic, so listing the folder is often enough.
3. **Search contents** for the terms of the area you're touching: module names, technologies, domain words, and their synonyms.
4. **Read matches in full,** and follow any `Amended by` or `Superseded by` links to what is current.

## Act on what you find

- **Change fits the ADR:** proceed, and cite it where it helps a reviewer ("per ADR 004").
- **Change conflicts with the ADR:** stop and tell the user which ADR, what it decided, and how the change breaks it. Then either reshape the change to fit, or, if the user agrees the decision should change, supersede it with a new ADR in the same PR. The ADR is never quietly ignored.
- **Code already contradicts the ADR:** report the drift to the user. Leave both code and ADR as they are until the user says which one is right.
- **No ADR, but the choice is significant:** offer to record one.

## When to record

Record a decision only when all three hold:

1. **Hard to reverse:** changing course later costs real time.
2. **Surprising without context:** a reasonable reader would assume the opposite.
3. **A real tradeoff:** there were genuine alternatives, chosen between for specific reasons.

Typical cases: architectural shape, lock-in technology (database, auth, hosting), boundaries between parts of the system, constraints the code can't show (compliance, contracts), and deliberate deviations from the obvious path. When a decision fails the test, a code comment or the PR body is its home.

## Where

Use the repo's existing ADR folder, or create `docs/adr/` with the first ADR.

Name files `<number>_<snake_case_title>.md`: a sequential number, zero-padded to at least three digits, like `001_language_choice.md`; past 999 it simply grows, like `1000_programming_architecture.md`. Take the next number after the highest on the latest remote default branch. If a merge brings in an ADR with the same number, renumber yours before merging.

## Format

```markdown
# 004: Use Postgres for the write model

Status: Accepted. Date: 2026-11-10. Decided by: <who>. Supersedes [ADR 002](002_dynamodb_for_orders.md).

## Context
## Options considered
## Decision
## Consequences
## Tests
```

What each part carries:

- **Title:** the number and the decision stated as a rule.
- **Header line:** status, date, who decided, and links to any ADR it amends or supersedes, naming the specific decisions it changes ("Amends ADR 002, decision 1").
- **Context:** the prior state and the forces that made this a decision now. Evidence over adjectives: measurements, incidents with dates, hard constraints, and what can't be known.
- **Options considered:** each real alternative with why it lost, and why the chosen one won. One or two lines each.
- **Decision:** numbered decisions, each opening with a bold one-line rule followed by its detail. When amending, say what stays unchanged.
- **Consequences:** what gets easier, what gets harder, what is now required, and the costs accepted knowingly.
- **Tests:** the tests or checks that pin the decision, so a change that breaks it fails. Omit when there are none.

Length follows the decision: a narrow one needs a few lines per section. Write for a reader who has none of this conversation.

## Status and change

- `Proposed` while under discussion, `Accepted` once the user agrees.
- Accepted ADRs are never rewritten. A new ADR either **amends** specific decisions of an old one or **supersedes** it whole. The old ADR's status line gains `Amended by <link>` or `Superseded by <link>`; that is the only edit an old ADR gets.
- Commit the ADR with the change it governs, so the PR shows both.
