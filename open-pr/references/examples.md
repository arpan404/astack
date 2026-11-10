# Target PR

**Retry failed webhook deliveries with exponential backoff**

```markdown
Failed webhook deliveries now retry up to 5 times with backoff. Before, one failed attempt dropped the event, causing the missing orders in #482.

- Retries only on 5xx, 429, and timeouts. A 4xx fails at once: resending a bad payload won't fix it.
- New env var `WEBHOOK_MAX_RETRIES` (default 5).

Verified against a local endpoint returning 503, 503, then 200: delivered on attempt 3.

Risk: a slow receiver can hold a worker for up to 31s.

Closes #482
```
