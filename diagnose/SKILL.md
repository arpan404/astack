---
name: diagnose
description: Use when debugging a hard bug, flaky failure, or performance regression.
---

# Diagnose

No theory and no fix until a loop goes red on this bug.

1. **Loop.** Build one command that reproduces the user's exact symptom: a failing test, a curl script, a CLI run on a fixture, a headless browser script, a replayed trace, a throwaway harness, a fuzz loop, a bisect script, or a diff between two versions. Make it tight: seconds, deterministic (pin time, seed randomness, isolate the network). For a flaky bug, raise the reproduction rate with loops, stress, and parallel runs until it's debuggable. If no loop is possible, stop, list what you tried, and ask for access, a captured artifact, or permission to instrument.
   Done when you have run the command and watched it go red on the user's symptom, not a nearby one.
2. **Minimise.** Cut inputs, steps, and config one at a time while it stays red, until every remaining piece is load-bearing.
3. **Hypothesise.** Rank 3 to 5 causes, each with a falsifiable prediction: "if X, then changing Y makes it disappear". Share the list with the user; continue if they're away.
4. **Probe.** One variable at a time. A debugger first, then targeted logs tagged with a unique prefix like `[DEBUG-a4f2]` so cleanup is one search. For performance: baseline, profile, bisect.
5. **Fix.** Turn the minimal repro into a failing test at a seam that exercises the real pattern. Watch it fail, fix, watch it pass, then rerun the original loop. If no seam can capture the bug, report that as a finding.
6. **Clean up.** Remove tagged logs and harnesses. State the root cause in the commit or PR.

Redact secrets from anything you show.
