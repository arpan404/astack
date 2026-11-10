# PR examples

## Small change

**Title:** Add open-pr and file-issue skills

```markdown
Adds `open-pr` and `file-issue`, the first skills in the new workflow set. Both are host-neutral: the agent uses whichever CLI the repo's host needs.

- `open-pr` keeps PR bodies short enough to read in one pass.
- `file-issue` shows a draft before posting unless told to file directly.
- Each skill has `agents/openai.yaml` so Codex shows a display name.
```

No headings, no verification section: nothing behavioural changed, so there is nothing to show.

## Larger change

**Title:** Retry failed webhook deliveries with exponential backoff

```markdown
Failed webhook deliveries now retry up to 5 times with backoff. Before, one failed attempt dropped the event, causing the missing orders in #482.

- Retries only on 5xx, 429, and timeouts. A 4xx fails at once: resending a bad payload won't fix it.
- Backoff goes 1s, 2s, 4s, 8s, 16s.
- New env var `WEBHOOK_MAX_RETRIES` (default 5).

Verified against a local endpoint returning 503, 503, then 200: delivered on attempt 3.

Risk: a slow receiver can hold a worker for up to 31s. Fine at current volume; revisit above about 50 webhooks per second.

Closes #482
```

Still no headings: each part is one line or one short list, so a label at the start of the line is enough. The only explanation is for the decision a reviewer would question (why 4xx is skipped).

## Weak

**Title:** Update webhook.ts

```markdown
## Summary
This PR updates the webhook logic to improve reliability and robustness.

## Changes
- Modified webhook.ts
- Updated tests
- Added a new environment variable

## Testing
- All tests pass
- Created by following the PR workflow
```

It reads like a filled-in form. The title names a file. The summary fits any PR and gives no reason or issue. The bullets repeat the file list from the diff. The testing lines are what CI already says plus a note about the process, and the real risk (workers waiting longer) is missing.
