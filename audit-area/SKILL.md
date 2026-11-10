---
name: audit-area
description: Use when asked to audit a feature, page, module, or whole app without changing it.
argument-hint: "[area]"
---

# Audit

Read-only: change nothing until the user picks what to fix.

1. **Scope:** the area, and what to audit in it: correctness, security, performance, UX, consistency, dead code. Take the user's list, or all of them.
2. **Map:** entry points, data flow, queries and mutations, permissions, external calls. Split a large area across read-only subagents, one per part.
3. **Find:** each finding has `file:line`, a concrete failure or cost, a severity, and a suggested fix. Verify each by reading the code or running something read-only, and drop what doesn't hold.
4. **Report:** ranked by severity and grouped by theme, with counts. Short enough to act on.
5. **Next,** on the user's pick: file issues with `file-issue`, or fix them with `run-fleet`.
