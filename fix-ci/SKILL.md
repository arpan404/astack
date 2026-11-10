---
name: fix-ci
description: Use when a CI pipeline, check, or deploy job is failing.
argument-hint: "[run, job, or PR]"
---

# Fixing CI

1. **Find the failure:** the failing run and job, through the host's CLI. Read the log from the first error, not the last line.
2. **Classify:** code (test, lint, type), environment (tool versions, cache, missing secret, runner image), or flake (passes on rerun, timing). Check whether the default branch fails the same way; then it predates this change.
3. **Reproduce locally** with the job's command and versions.
4. **Fix the cause.** Skipping or disabling tests, loosening lint rules, and adding retries all hide failures; do them only when the user agrees. For a flake, find the nondeterminism with `diagnose`.
5. **Push and watch** the rerun until it is green. Report the cause and the fix.

Missing secrets and permission errors can't be fixed from the repo: tell the user exactly what to set and where.
