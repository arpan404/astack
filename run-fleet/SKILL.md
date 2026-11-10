---
name: run-fleet
description: Use when splitting a batch of work, like many issues or a large plan, across parallel child agents.
argument-hint: "[issues, plan, or scope]"
---

# Run a fleet

You orchestrate; children do the work. In ace: `delegate`, `wait`, `agent_message`, `agents_status`, `question_answer`, `agent_cancel`, `thread_link_pr`.

## Plan

1. Collect the work and read each item in full.
2. Give each child one item, or several when they touch the same files. No two running children edit the same files or the same contract.
3. A wide change (a rename or contract change across packages) goes to one child and runs first. Work in its path waits until it merges.
4. Pick provider, model, and effort per child by size and risk: the strongest model for design-heavy or cross-cutting work, a cheaper one for small fixes. Follow the user's stated preferences, and check quota with `models`; start nothing on an account that's out of quota.
5. Show the plan (children, model per child, order) and start once the user approves, unless they said to go ahead.

## Brief

Each child starts with none of your context, so its task carries everything:

- Read `AGENTS.md` first.
- The goal, issue links, the areas involved, and what's out of scope.
- Workspace: a new worktree from the default branch, or the base the user names.
- Checks: the ones `AGENTS.md` names, scoped to what it touches.
- Delivery: commit with `write-commit`, push, and open a PR with `open-pr` that names its own model and effort. Those skills set the attribution rules; add none of your own.
- When blocked, ask (`clarify`) rather than guess.
- Report: what changed, checks run and their results, the PR URL, the pushed commit SHA, its model and effort, and anything left open.

Role names say what and where, like `Fix-412-cart-total`.

## Run

- Keep a tracker with one row per child: role, model, state, PR, SHA. Show it at each check-in.
- Collect results with `wait` or by ending the turn; never poll.
- Answer children's questions with `question_answer`, or pass them to the user. Steer with `agent_message`.
- A child that stalls, fails, or hits a usage limit gets resumed, or its task relaunches on another provider with the progress so far.
- Check each result against its brief before accepting it: the PR exists, the SHA is pushed, the checks are reported.
- Each PR then goes through `run-review-loop`, then `babysit-pr`.

Done when every item is merged (when the user asked for merging) or ready to merge, held for the user with a reason, or reported blocked. Finish with the tracker.
