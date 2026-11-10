---
name: polish-ui
description: Use when building, redesigning, or polishing UI, or when the user calls it slop.
---

# Polish UI

Before the user sees UI, critique it as a demanding designer and fix what you find.

## House rules

- Group with spacing, alignment, and type, not boxes. Use a container only when it carries meaning.
- Show the result of small or expected actions in place, not in a toast.
- Keep scrollbars hidden unless the platform requires them.
- Follow the existing design system and components. Add a new primitive only when none fits.
- One accent color, a clear type scale, and consistent spacing steps.
- Copy is short and concrete.

## Critique pass

Judge the rendered result in a screenshot, not the code:

- **Hierarchy:** what the eye reads first, second, third.
- **Rhythm:** alignment, spacing, and density.
- **States:** empty, loading, error, dark mode, small screens.
- **Slop:** anything that reads as a generic template, like decorative gradients, emoji icons, everything centered, stacked borders and shadows, or placeholder copy.

Fix, recapture, and repeat until the pass finds nothing. Then show it with `show-ui-change`.
