---
name: show-ui-change
description: Use when a UI change needs to be seen in the running app, with before and after screenshots for approval.
---

# Show a UI change

The user judges UI by seeing it, so show the real thing.

1. **Run the real app** (web, desktop, or simulator) with realistic data, using the repo's dev command and the harness's browser or device tools.
2. **Capture** before (base branch) and after (your branch) for every screen and state the change touches: light and dark, a narrow and a wide size, and the hover, empty, loading, and error states involved.
3. **Check your own captures** for misalignment, overflow, truncation, contrast, and dark-mode breaks. Fix and recapture before showing anything.
4. **Show** them inline as before and after pairs, one line per pair on what changed.
5. **Iterate** on what the user flags until they approve.

Approval gates merging. Attach the approved images to the PR as `open-pr` describes.
