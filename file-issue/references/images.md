# Images

Visual changes (UI, layout, styling, charts, rendered output) need images in the body. A PR shows before and after. An issue shows the broken state.

## Capture

- Use whatever screenshot or browser tool the session has.
- Before comes from the base branch, after from the PR branch, with the same viewport and data, cropped to the change. Use a short GIF or video for interactions and animations.
- Check every image for secrets, tokens, and personal data before it leaves the machine.

## Upload only when allowed

Upload when either holds:

- the user asked you to upload images, or
- the repo already allows it: a `pr-assets` branch exists on the remote (`git ls-remote --heads origin pr-assets`), or the repo's agent docs or contributing guide say to upload images.

Otherwise go to Hand off.

## Upload

- **GitHub:** commit the images to `pr-assets`, an orphan branch that is never merged. Create the branch only when the user asked for uploads. Leave the working tree and the PR branch untouched: write through a temporary worktree. Store files under a folder named after the PR branch or the issue, like `fix-empty-cart/before.png`. Link by commit SHA so the link survives later pushes: `![Before](https://github.com/<owner>/<repo>/blob/<sha>/<path>?raw=true)`.
- **GitLab:** upload through the project uploads API and paste the markdown it returns.
- **Other hosts:** use the host's attachment API if it has one; otherwise hand off.

## Hand off

When you can't upload, save the images outside the repo and put a visible placeholder where each belongs: `_Screenshot pending: before.png_`. Open a PR as a draft; for an issue, include the list with the draft you show the user. Your final message lists each file path and where it goes.

Done when every image is embedded by link, or the user has the list of files to attach.
