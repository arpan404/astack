---
name: babysit-pr
description: Use when watching a PR through checks, review, and conflicts until it merges.
metadata:
  author: arpan404
  version: "1.0.0"
---

# Babysit a PR

Carry one PR from open to merged so the user doesn't have to watch it.

## Each pass

1. **Sync:** when the base has moved, update the branch the way the repo does (rebase or merge). Resolve conflicts keeping both sides' intent, then rerun the checks.
2. **Checks:** failing goes to `fix-ci`; pending means wait.
3. **Review:** handle every new comment: fix and push, or reply with reasons when you disagree. Resolve the threads you've handled. When the PR gets agent review, run `run-review-loop`.
4. **Ready** means checks green, no open blocking comments, and the approvals the repo requires.

Between passes, wait with the harness's wake-up or scheduling tools, sized to what you're waiting on: minutes for checks, longer for human review. Never a tight polling loop.

## Merge

- Merge only when the user asked for it. A PR that changes UI also waits for the user's approval of its screenshots (`show-ui-change`).
- Use the merge method recent merges in the repo used.
- After merging: delete the remote branch and link the PR to the thread (`thread_link_pr` in ace). Remove the local branch and worktree when the user asked for cleanup.

Stop and ask when a conflict needs a product decision, a reviewer asks for a change you believe is wrong, or checks fail for reasons outside the PR (secrets, infrastructure).

Report the final state, the merge commit, and anything left for the user.
