---
name: plan-work
description: Use when breaking a spec, plan, or large change into issues or tickets.
metadata:
  author: arpan404
  version: "1.0.0"
---

# Planning work

The bar: an agent in a fresh session can pick up any ticket, finish it in one sitting, and verify it on its own.

## Slicing

- **Vertical slices.** Each ticket is a tracer bullet: a narrow but complete path through every layer it needs (schema, API, UI, tests), demoable alone.
- **Prefactor first.** When a refactor makes the change easy, it is its own ticket at the front.
- **Size:** one fresh context window, one reviewable PR.
- **Wide refactors** (one mechanical change across many call sites) run expand, migrate, contract: add the new form beside the old, move callers over in batches that each keep CI green, then delete the old form.
- **Too many unknowns to slice:** the first tickets are decisions or spikes that unblock the rest.
- Every ticket names the tickets that block it. Unblocked tickets can run in parallel.

## Ticket shape

Title, what to build (end-to-end behaviour from the user's side), acceptance criteria as a checklist (from the spec's Behaviour items), blocked by, and a link to the parent spec. No file paths.

## Review and publish

1. Show the breakdown as a numbered list: title, blockers, what each delivers. Ask whether the granularity and blocking edges are right, and iterate until the user approves.
2. Publish in dependency order so blockers have real IDs. Use the host's native sub-issue or blocking links where it has them. Touch the parent only to link it.
3. Report the ticket URLs and which tickets can start now.
