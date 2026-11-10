# Images

Visual changes need images: before and after for a PR, the current or broken state for an issue. Capture with any screenshot tool, same viewport and data, cropped to the change. Scrub secrets and personal data.

Upload only when the user asks, the remote already has a `pr-assets` branch, or the repo's docs say to. Commit each image to `pr-assets` (an orphan branch, never merged) as `<uuidv7>.<ext>`, writing through a temporary worktree so the working tree stays untouched. Embed it with the host's raw-file URL pinned to that commit's SHA.

Otherwise save the images outside the repo, put `_Screenshot pending: <file>_` where each belongs, keep a PR in draft, and list the files for the user.
