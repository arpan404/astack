# astack

Agent skills for engineering work: shipping PRs, planning, debugging, review, running fleets of agents, UI and UX, and writing. They follow the open Agent Skills format, so they work in Claude Code, Codex, Cursor, and other harnesses.

## Install

```sh
npx skills add arpan404/astack -g
```

Pick skills with `-s <name>` and harnesses with `-a <agent>`. Update later with `npx skills update -g`.

## Skills

### Shipping

- `open-pr`: Use when opening, updating, or rewriting the description of a pull request or merge request.
- `file-issue`: Use when filing, drafting, or rewriting an issue, including bug reports, feature requests, and tasks.
- `write-commit`: Use when committing changes or writing a commit message.
- `babysit-pr`: Use when watching a PR through checks, review, and conflicts until it merges.
- `fix-ci`: Use when a CI pipeline, check, or deploy job is failing.

### Planning

- `write-spec`: Use when turning a discussion, idea, or request into a spec before building it.
- `plan-work`: Use when breaking a spec, plan, or large change into issues or tickets.
- `clarify`: Use when a request is ambiguous, a choice is costly to get wrong, or the user asks to be questioned on a plan.
- `record-decision`: Use when making, changing, or checking for architecture decisions (ADRs).
- `prototype`: Use when building throwaway code to answer a design or UI question.

### Building and review

- `test-first`: Use when building a feature or fixing a bug test-first (TDD, red-green).
- `diagnose`: Use when debugging a hard bug, flaky failure, or performance regression.
- `review-code`: Use when reviewing a branch, PR, or uncommitted changes.
- `run-review-loop`: Use when work should be reviewed by another agent and fixed until it's ready to merge.
- `design-modules`: Use when designing module interfaces and seams, or finding code to deepen.
- `audit-area`: Use when asked to audit a feature, page, module, or whole app without changing it.
- `triage-issues`: Use when triaging, labelling, or sorting incoming issues or external PRs.

### Agent orchestration

- `run-fleet`: Use when splitting a batch of work, like many issues or a large plan, across parallel child agents.

### Repos

- `shape-repo`: Use when creating a repo or auditing one for agentic development, tooling, CI/CD, and caching.

### UI and UX

- `design-ui`: Use when designing, building, reviewing, or polishing UI and UX on any platform, including web, iOS, Android, and cross-platform apps.
- `show-ui-change`: Use when a UI change needs to be seen in the running app, with before and after screenshots for approval.

### Writing

- `unslop`: Use for any prose a person will read, including replies, docs, PRs, issues, commit messages, and code comments.
- `humanize`: Use when the user asks to rewrite, humanize, or de-AI text they provide so it reads as written by a person.

## Versions

Each skill carries its own `metadata.version`, bumped on every change. Contributing rules are in [AGENTS.md](AGENTS.md).
