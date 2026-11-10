---
name: open-pr
description: Use when opening, updating, or rewriting the description of a pull request or merge request.
argument-hint: "[base-branch]"
---

# Pull requests

"PR" here covers pull requests and merge requests on any host. Use the host's CLI.

The bar: a reviewer understands the PR in under a minute and can merge it with confidence.

## The branch

- Match the repo: base branch, branch naming, PR template, and title style from recent merged PRs.
- The branch holds only this change, is current with the remote base, and passes whatever checks the repo has. If it mixes unrelated work or is too large to review in one sitting, propose a split before opening.
- One PR per branch. If one exists, update it in place and keep its draft or ready state.

## Title

Imperative, 72 characters or fewer, naming the behaviour or capability that changes rather than the files touched. Use a conventional prefix (`feat:`, `fix:`) only when the repo does.

## Body

Write it the way a senior engineer writes to a teammate: plain prose, why first, then what. It reads in one pass and fits on one screen.

The shape scales with the change. A small PR is a short paragraph and a few bullets, with no headings. Add headings only when a large PR has parts a reviewer needs to find.

- **Opening:** 1 or 2 sentences, under 50 words, saying what changes and why. Pull the motivation from the conversation; the diff can't show it.
- **Bullets:** up to 5, one line each, covering what the diff doesn't make obvious: decisions, tradeoffs, anything a reviewer would question.
- **Verification:** only behavioural evidence, such as a bug reproduced then fixed, a targeted test for the changed behaviour, or a manual scenario and its observed result. When there is none, leave it out; CI already reports tests, lint, and typecheck.
- **Risks:** migrations, breaking changes, new config, rollout steps. Only when real.
- Link issues with the host's closing keyword (`Closes #N`), or a plain reference when the PR only touches them.

A repo template overrides this shape: keep its headings and checklists and fill them with specifics. Longer material (benchmarks, design notes) goes in a collapsed `<details>` block at the end.

Write about the change itself, never about how the PR was produced. Describe the net change, not attempts that were later undone. Use repo-relative paths. When rewriting an existing body, keep images and anything the author wrote by hand. The body carries no attribution lines or tool footers.

[`references/examples.md`](references/examples.md) shows the target length and tone next to a weak PR.

## Mechanics

- Pass the body from a file so newlines render.
- Open as a draft when checks fail or the work is unfinished.
- Asking for a PR authorizes pushing its branch. Push to the default branch or force-push only when the user asks; rewrite pushed history with `--force-with-lease`.
- Finish by reporting the PR URL.
