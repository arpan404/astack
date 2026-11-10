---
name: test-first
description: Use when building a feature or fixing a bug test-first (TDD, red-green).
---

# Test first

Red, then green, one vertical slice at a time.

## Seams

Tests live at seams: the public interface where behaviour is observable without reaching inside. Agree the seams with the user, or take them from the spec, before the first test. One seam is ideal; the highest available beats a deep internal one.

## The loop

1. **Red:** write one test for the next behaviour and run it. It fails for the right reason: the assertion, not an import or setup error.
2. **Green:** write the least code that passes it. Nothing for tests that don't exist yet.
3. Run the narrow test each cycle; at the end, run the checks the repo's `AGENTS.md` names.
4. Next slice, shaped by what the last cycle taught.

Refactor once the slice is green, never mid-cycle.

## Good tests

- Assert behaviour through the interface, so they survive refactors. Names read like the spec: "rejects an expired coupon".
- Expected values come from an independent source (a literal, a worked example, the spec), never recomputed the way the code computes them.
- Mock only at system edges: network, clock, randomness, third-party services. Prefer in-memory fakes at seams over mocks of internal collaborators.
- One test at a time. Writing every test up front tests imagined behaviour.

Done when every behaviour in scope has a test that was red before its code existed, and those checks pass.
