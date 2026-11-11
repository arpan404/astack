# What agents get wrong

These are the failures agents make most, drawn from user reviews of agent-built UI and from published research. Check every item before showing anything.

## Interaction

1. **Everything is a form.** Create and edit pages or modals where the item could be edited in place. Fix: edit in place, create in context, and a spreadsheet-like grid for entering tabular data.
2. **Leaving the page for small things.** Search, previews, and quick edits that navigate away. Fix: open them in place, in a palette, popover, or side panel.
3. **Confirming routine actions.** Fix: do it at once and offer undo. Confirm only the irreversible.
4. **Toasts for errors, or for results already visible.** Fix: feedback in the control that was used; errors next to their cause.
5. **Dead ends.** Missing empty, loading, error, offline, or partial states.
6. **Gesture-only actions** with no visible way to do the same thing.
7. **Inconsistent action patterns.** A "..." menu in one table and inline actions in another, or a menu holding a single item. Fix: one pattern per kind of action, and single actions shown directly.

## Scope and clutter

8. **Unrequested additions:** features, settings, filters, floating buttons, stub buttons, stats on every page, onboarding, tips.
9. **Narration:** eyebrow pills above headings, subtitles restating titles, "Here you can...", hint lines under controls, a title repeated in the header and the page.
10. **Technical leaks:** IDs, raw status values, field names, internal states, or the prompt itself showing in the interface.
11. **Meaningless structure:** numbered markers (01, 02) on things that aren't a sequence, status dots that map to nothing, sections of one item.

## Visual

12. **Boxes everywhere:** everything in a card, cards inside cards, each settings group wrapped in a bordered box. Fix: space, weight, hairlines, one surface step. The opposite failure is stripping every container until the page has no anchors.
13. **One-side coloured accent borders** on cards, callouts, or rows.
14. **Depth on the wrong things:** shadows or 3D on content, buttons, or selected rows, and glow in dark mode.
15. **Decorative colour:** gradients (purple above all), tinted or bluish backgrounds, several bright accents, colour that means no state.
16. **Emoji as icons,** mixed or colourful icon sets, and icon-only buttons without a tooltip.
17. **The template look:** untouched library defaults, a centered hero with stats and a feature grid, or the house palettes models default to (cream with a serif and terracotta; near-black with one acid accent).
18. **One-off values:** stray radii, paddings, and sizes; corners rounder than the rest of the app; unwanted padding.
19. **Visible or doubled scrollbars.**

## Motion and stability

20. **Looping status animation:** shimmer, pulse, endless spinners. Fix: a still indicator and a running time.
21. **Slow, choppy, or entertaining transitions,** and animations that collide with page transitions.
22. **Instability:** layout shift, rows flickering on live updates, scroll position jumping while content streams, a first click that moves the layout and needs a second.

## Platform

23. **Custom chrome where the platform has native:** navigation bars, modals, sheets, pickers.
24. **Fake glass:** blur and gradients instead of the system material, glass on content or on glass, and solid surfaces where translucency is turned on.
25. **Ignored device rules:** safe areas, device corner curves, back gestures, text size settings.
26. **Desktop squeezed onto phones:** cut-off components, headers wider than the screen, truncated values.

## Copy

27. **Robotic or over-explaining text,** words above the audience's level, or one language when the audience works in another.
