---
name: write-commit
description: Use when committing changes or writing a commit message.
metadata:
  author: arpan404
  version: "1.0.0"
---

# Commits

- One logical change per commit. Stage only its files; split unrelated work into separate commits.
- Run the checks the repo's `AGENTS.md` names first.
- **Subject:** imperative, 72 characters or fewer, no trailing period, naming the change. Use a prefix like `feat:` only when `git log` shows the repo does.
- **Body,** when the why isn't obvious from the subject: why the change was made, then what changed at a high level, wrapped at 72. Reference issues.
- Trailers follow the repo's `AGENTS.md`. When it names none, add none: no `Co-Authored-By` and no tool or AI attribution.
- Amend or rewrite pushed commits only when the user asks.
