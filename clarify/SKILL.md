---
name: clarify
description: Use when a request is ambiguous, a choice is costly to get wrong, or the user asks to be questioned on a plan.
---

# Clarify

Ask only questions whose answers change what you'd do and that you can't answer by looking.

## Ask or decide

Ask when:

- a wrong guess is expensive or hard to undo: data, money, public actions, architecture;
- reasonable readings of the request lead to materially different results;
- the answer is a preference only the user holds: taste, priority, scope, budget.

Decide yourself, and say what you chose, when the choice is cheap to reverse or has a sensible default. Look facts up in the code, docs, tools, and logs instead of asking for them.

## How to ask

- One round, every question at once, numbered. Each gives the options, your recommended answer, and what changes with the answer.
- Use the harness's question tool when it has one.
- Keep working on whatever the questions don't block.
- When nobody can answer (you're a delegated child, or the user is away), take your recommended answers and list them as assumptions in your report.

## Interview mode

When the user asks to be interviewed on a plan, or a plan has many open decisions, work in rounds. Ask every open decision whose prerequisites are settled, wait, then ask the decisions those answers unblock. Done when nothing is left assumed: summarize the plan and act only after the user confirms it. Record decisions that pass the ADR test with `record-decision`.
