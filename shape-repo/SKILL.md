---
name: shape-repo
description: Use when creating a repo or auditing one for agentic development, tooling, CI/CD, and caching.
argument-hint: "[new|audit] [stack or goal]"
---

# Repo setup

The bar: an agent can make a change and prove it works with one fast command, and a human approves anything risky before it lands.

## Process

1. **Survey.** Read the repo: languages, frameworks, package managers, host, CI, agent docs, and how long checks take. For a new repo, get the product, stack constraints, and deploy target from the user.
2. **Research.** Look up current practice for the detected stack in primary sources: official docs, the tools' own repos, release notes. Cover versions, layout conventions, lint and format, test runner, and the caching and incremental features each tool supports. Treat your memory of versions as stale.
3. **Propose.** List changes ranked by value to agents and humans against cost, with measured or estimated time saved where speed is the point. The user picks. For an audit, stop here.
4. **Apply** in small PRs, one concern each, through `open-pr`. Ask before touching branch protection, permissions, secrets, or anything outside the repo.

Done when the chosen changes are merged or open as PRs, and `check` passes from a clean clone.

## What good looks like

**Agent loop**

- One `check` command runs format, lint, typecheck, and tests. It is fast enough to run after every change, deterministic, and points failures at `file:line`. Narrower commands run one test or one package.
- Pinned toolchain and lockfiles. A clean clone sets up with one command. `.env.example` lists every variable.
- A short `AGENTS.md`, with `CLAUDE.md` linked to it, holding the commands, only the conventions the code can't show, and where ADRs and the glossary (`CONTEXT.md`) live so agents read them before changing that area.
- Code grouped by feature, tests beside the code, small modules with clear interfaces. Generated code is marked and kept out of edits.
- Strict types and lint rules as guardrails, set to error.
- Conventional, well-documented frameworks that models know well. Explicit code over magic.

**Human in the loop**

- Protected default branch with required review and checks.
- CODEOWNERS on risky areas: auth, payments, migrations, infra, CI.
- Agent permissions allow checks and reads, and require approval for deploys, migrations, deletes, and pushes to the default branch. Hooks block destructive commands.

**Speed and cost**

Measure first: time each step of `check`, the build, and CI (use recent run history), and find the slowest. Then research what this stack's own tools offer to cut them: incremental builds and typechecking, lint and test caches, dependency and build caches, remote caches, affected-only runs, sharding. For each candidate, estimate the time or CI minutes saved against the cost to adopt and maintain it, and propose only those that pay off. CI runs the same `check` as local, so every gain speeds up both the agent loop and the pipeline.
