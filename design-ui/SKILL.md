---
name: design-ui
description: Use when designing, building, reviewing, or polishing UI and UX on any platform, including web, iOS, Android, and cross-platform apps.
metadata:
  author: arpan404
  version: "1.0.0"
---

# Design UI

The bar: someone who knows the domain uses it without stopping to think, it feels native to its platform, and nothing on screen is there to decorate, explain, or show off.

## Principles

1. **Every element shows something the user acts on.** If it only decorates or describes the interface, it goes.
2. **Direct, not form-driven.** People act on the thing itself: edit in place, drag, select, type where the result appears. A form is for new information the user brings, nothing else.
3. **Build what was asked.** No extra features, settings, filters, badges, stats, banners, or buttons. Suggest them to the user instead.
4. **Domain words, no commentary.** Labels use the words of the people who do this work. No implementation terms, and no prose explaining the screen.
5. **One place per fact.** Each piece of state shows once: in the row, the header, or the detail, never all three.
6. **Hierarchy one step at a time.** Size, weight, ink tier, or surface: one device per distinction. Group with space and weight, never boxes inside boxes.
7. **Colour means something.** Neutral ink everywhere; colour only for state, the one accent on the primary action, and brand marks.
8. **Still, not busy.** Motion confirms an action or moves something into place. Nothing loops, flickers, or jumps.
9. **Native grammar.** Each platform gets its own navigation, controls, materials, and gestures, built from its own components.
10. **Few values, everywhere.** Every colour, radius, gap, size, and curve comes from tokens. A one-off value is a bug.
11. **Correct before pretty.** Whatever the screen says about state is true right now.

## Process

1. **Understand the job.** Who uses it, what they're trying to get done, how often, on which device, and in which language. Read the project's design docs and tokens (a `DESIGN.md`, a design language, a theme file); they override this skill wherever they speak.
2. **Shape the flow before the screens.** The fewest steps from intent to done, where results appear, what people manipulate directly, and every state: empty, loading, error, partial, offline, long text, many items. Read [`references/ux.md`](references/ux.md), and [`references/forms.md`](references/forms.md) when a form is truly the right tool.
3. **Reuse.** Inventory the project's components, tokens, and icons. Reach for the project's components, then the platform's, then an established library, and build by hand last. Dialogs, menus, comboboxes, date pickers, tabs, drag and drop, and virtualized lists always come from a library or the platform. Read the platform reference: [Apple](references/apple.md), [Android](references/android.md), [web](references/web.md), or [cross-platform](references/cross-platform.md). Check current docs too; design systems change every year.
4. **Build** with [`references/visual.md`](references/visual.md), [`references/motion.md`](references/motion.md), and [`references/copy.md`](references/copy.md).
5. **Critique** until it passes (below).
6. **Show** it with `show-ui-change`.

For a redesign or a large new surface, show a mockup or two or three directions before building. Take ideas from products the user points to without copying their look; the result should be recognisably this product.

## Redesigning existing UI

Audit before touching: what works stays. Change what was asked, and keep behaviour, data, routes, and shortcuts unless told otherwise. List anything you'd remove and let the user decide; nothing disappears silently.

## Critique

Render it with realistic data at real sizes (390, 768, and 1440 wide for web; phone and tablet for mobile), in light and dark, and judge the screenshots:

- Can a newcomer to this domain finish the main task without reading any help?
- Does every element show something actionable? Is anything narrating, duplicated, or unrequested?
- Is the main content first, with one obvious primary action?
- Are edits direct, with results showing in place?
- Is every state present, and does nothing shift, flicker, or jump scroll position?
- Does it feel native to the platform?
- Do all values come from tokens?
- Is the copy in domain words, with verbs on buttons, and free of jargon and AI voice?
- Is it accessible: contrast, focus, labels, hit targets, text scaling, reduced motion and transparency?
- Does it pass every item in [`references/anti-patterns.md`](references/anti-patterns.md)?

Fix, re-render, and repeat until every answer is yes.
