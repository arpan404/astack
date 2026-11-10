---
name: design-modules
description: Use when designing module interfaces and seams, or finding code to deepen.
---

# Module design

Aim for deep modules: a lot of behaviour behind a small interface. Callers get leverage, maintainers get locality, and tests cross the same interface callers do.

## Vocabulary

- **Module:** anything with an interface and an implementation, at any scale.
- **Interface:** everything a caller must know: types, invariants, ordering, errors, config, performance.
- **Seam:** where an interface lives; behaviour changes there without editing callers.
- **Adapter:** a concrete thing that satisfies an interface at a seam.
- **Depth:** behaviour available per unit of interface a caller has to learn.

## Principles

- **Deletion test:** delete the module in your head. If complexity vanishes, it was a pass-through; if it reappears across callers, it earns its place.
- One adapter is a hypothetical seam; two make it real. Add a seam only where something varies, or at a system edge for tests.
- Accept dependencies, return results, and keep side effects at the edges.
- Fewer methods, simpler parameters, more hidden inside.
- The interface is the test surface. Needing to test past it means the module is the wrong shape.

## Designing an interface

Design it twice: sketch two or three radically different interfaces, in parallel subagents when available. Compare them on depth, locality, and seam placement, and recommend one.

## Finding what to deepen

Look for shallow and pass-through modules, logic duplicated across callers, one change that touches many files, and tests that mock internals. Present ranked candidates with the change and its payoff. The user picks; then design it. Record hard-to-reverse choices with `record-decision`.
