---
name: run-review-loop
description: Use when work should be reviewed by another agent and fixed until it's ready to merge.
argument-hint: "[PR or branch]"
---

# Review loop

An author and a reviewer on a different provider iterate until the reviewer finds nothing blocking.

## Setup

- **Author:** the agent that wrote the change and pushes the fixes. When that's you, you fix the findings yourself.
- **Reviewer:** a read-only child started with `delegate`, on a different provider and model family from the author so their blind spots don't overlap.
- **Reviewer brief:** the PR or branch and its base, the spec or issue, `AGENTS.md`, and the `review-code` standard. Findings ranked blocking, should-fix, or minor, each with `file:line`, the failure it causes, and a fix. Nothing tooling already enforces. The reviewer reads and runs read-only commands; it never edits, commits, or pushes.

## Rounds

1. The reviewer reviews and reports its findings.
2. Send them to the author word for word with `agent_message`: fix blocking and should-fix findings, explain any it disagrees with, push, and report the pushed commit SHA.
3. The reviewer re-reviews at that SHA. It gives each earlier finding a verdict (fixed, partial, not fixed, regressed) and reviews only what changed since.
4. Repeat until no blocking or should-fix findings remain. A disagreement the two can't settle goes to the user.

After three rounds without converging, stop and bring the open findings to the user.

Done when the reviewer's last round says ready to merge pending checks. Report the rounds, the final SHA, and any minor findings left. Merging belongs to `babysit-pr`.
