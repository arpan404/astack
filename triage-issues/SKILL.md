---
name: triage-issues
description: Use when triaging, labelling, or sorting incoming issues or external PRs.
argument-hint: "[issue, PR, or 'what needs attention']"
---

# Triage

Every triaged item carries one category (`bug`, `enhancement`) and one state:

- `needs-triage`: not yet evaluated
- `needs-info`: waiting on the reporter
- `ready-for-agent`: fully specified; an agent can do it unattended
- `ready-for-human`: needs human judgement, access, or manual testing
- `wontfix`: will not be done

Map these to the repo's existing labels. Create missing labels only after the user agrees.

## What needs attention

List unlabeled items, `needs-triage`, and `needs-info` items the reporter has answered since, oldest first, one line each. The user picks.

## Triaging one item

1. **Read everything:** body, comments, labels, prior triage notes, and the diff for a PR. Never re-ask what's answered.
2. **Check the code:** is it already implemented (search by concept, not the reporter's wording), or a duplicate?
3. **Verify the claim:** reproduce a bug from its steps; run a PR's tests. Report confirmed, failed, or not enough detail.
4. **Recommend** a category and state with reasons, then wait for the user.
5. **Apply:**
   - `ready-for-agent` or `ready-for-human`: comment a brief with what to build, why, acceptance criteria, and where in the code by concept rather than path. For human work, say why it can't be delegated.
   - `needs-info`: comment what's established and specific questions for the reporter.
   - `wontfix`: close with the reason, pointing to the existing code when it's already built.

When the user names a state directly ("move #42 to ready-for-agent"), confirm and apply without the full pass.
