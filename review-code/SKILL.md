---
name: review-code
description: Use when reviewing a branch, PR, or uncommitted changes.
metadata:
  author: arpan404
  version: "1.0.0"
---

# Review

1. **Pin the base:** the ref or PR the user names, else the merge-base with the default branch. Stop early if the diff is empty.
2. **Gather sources:** the spec (issues linked from commits or the PR, or a spec file), and the standards (`AGENTS.md`, contributing guide, lint config, ADRs in the touched areas).
3. **Review on three axes,** each in its own subagent when available so one axis doesn't bias another:
   - **Correctness:** bugs, unhandled edge cases, races, security holes, data loss, swallowed errors. Each finding names a concrete failure: this input or state produces this wrong result.
   - **Spec:** requirements missing or partial, behaviour nobody asked for, requirements implemented wrongly. Quote the spec line.
   - **Standards:** breaches of documented rules and ADRs, citing the rule. Then design smells as judgement calls: unclear names, duplication, pass-through modules, speculative generality, one change scattered across many files. Skip what tooling already enforces.
4. **Verify** each finding against the surrounding code before reporting it. Drop what doesn't hold.

## Report

Per axis, most severe first: `file:line`, the problem, the failure or rule, and a suggested fix. End with the count per axis and the worst finding in each. Change no code unless the user asks.
