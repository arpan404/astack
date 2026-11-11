# Motion

Motion explains change: where something came from, where it went, what responded. Without that job, leave it out.

## When

- **Animate:** changes the user caused (expanding, opening a sheet, reordering), moves between related views where continuity helps, and feedback that confirms an action.
- **Nothing loops.** Live work shows as a still indicator with a running time, not a shimmer, pulse, or endless spinner.
- **Leave still:** frequent interactions, decorative page loads, staggered reveals, hover flourishes, parallax, looping attention-seekers, and anything that makes the user wait.

Marketing pages may carry more motion, like scroll reveals, when the brand asks for it. Product screens stay calm.

## How

- **Durations:** about 100ms for small feedback, 200 to 300ms for larger changes, 400ms at most for big moves. Entering runs slightly slower than exiting. Too long is the usual mistake.
- **Easing:** ease-out to enter, ease-in to exit, never linear. On Apple platforms use system springs and transitions; on Android, Material motion tokens and springs. Never hardcode curves the platform already defines.
- **Web:** animate `transform` and `opacity` only, never layout properties, and never `transition: all`.
- **Interruptible:** the user can act during an animation, and nothing waits for one to finish.
- **Never the only signal:** state changes also show in text, icon, or position.

## Stability

- Nothing jumps when data arrives: reserve space for async content and media up front. On the web, keep Cumulative Layout Shift at or below 0.1.
- No flicker between loading and loaded states, and no content that renders, disappears, and renders again.

## Reduced motion

When the user asks for reduced motion, replace movement with a fade or nothing, stop autoplay and loops, and leave blur unanimated.
