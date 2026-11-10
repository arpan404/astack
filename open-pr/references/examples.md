# PR examples

## Target

**Title:** Retry failed webhook deliveries with exponential backoff

```markdown
## Summary
Failed webhook deliveries now retry up to 5 times with backoff. Before, one failed attempt dropped the event, causing the missing orders in #482.

Closes #482

## Changes
- Retries only on 5xx, 429, and timeouts. A 4xx fails at once: resending a bad payload won't fix it.
- Backoff goes 1s, 2s, 4s, 8s, 16s.
- New env var `WEBHOOK_MAX_RETRIES` (default 5).

## Verification
Local endpoint returning 503, 503, then 200: delivered on attempt 3.

## Risks
A slow receiver can hold a worker for up to 31s. Fine at current volume; revisit above about 50 webhooks per second.
```

The summary alone tells the reviewer what changed and why. The only explanation is for the decision a reviewer would question (why 4xx is skipped).

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
```

The title names a file. The summary fits any PR and gives no reason or issue. Changes repeats the file list from the diff. "All tests pass" is what CI already says, and the real risk (workers waiting longer) is missing.
