# Web

- Components: whatever the repo already uses comes first. For new React work, shadcn/ui (built on Base UI by default, or Radix) or React Aria. Vue has shadcn-vue on Reka UI; Svelte has shadcn-svelte on Bits UI.
- Styling follows the repo. For new work, Tailwind with design tokens as CSS variables.
- Use the platform before JavaScript: `<dialog>`, the popover API, `<details>`, native form validation, container queries, `:has()`, view transitions, scroll-driven animation, and anchor positioning. Check browser support against Baseline.
- Semantic HTML first, ARIA only to fill gaps, a keyboard path for every action, and visible focus.
- Responsive from 320px to wide screens, fluid type with `clamp()`, and media sized up front so nothing shifts.
- Speed is part of the design: fast first paint, no layout shift, and skeletons only where content is slow.
- One icon set, like Lucide or Phosphor.
- Dark mode through tokens and `prefers-color-scheme`; motion off under `prefers-reduced-motion`.
- Hit targets of at least 24 by 24 CSS pixels, larger for touch.
- Marketing pages follow the brand's art direction, not a stock hero, features grid, and testimonials.
- Vercel's Web Interface Guidelines are a good review checklist for web apps.
