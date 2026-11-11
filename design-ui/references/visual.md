# Visual

## Hierarchy

- Neighbours differ by one step of one device: size, weight, ink tier, or surface. Never two devices for one distinction.
- Ink tiers: primary (read this), secondary, meta (time, counts, paths), and faint (decoration only, never words). Show attention with brightness rather than bold.
- One primary action per surface.

## Grouping

- Separate with space, weight, and hairlines first; a surface step when that isn't enough. Never a card inside a card, or a bordered box inside a strip or sheet.
- Cards are for self-contained items that each lead somewhere. Data people compare or scan goes in a list or table.
- Gaps on a 4-point grid: small inside a group, large between groups.
- Merge groups of one. A page needs some anchors; stripping every container leaves it feeling empty.

## Colour

- Neutral surfaces and ink in true greys. Dark mode is its own design, near black, never inverted or tinted blue.
- Colour has three jobs: state (one hue per state, used for nothing else, never alone), the single accent for the primary action and selection, and brand marks in their own colours.
- No decorative gradients, glows, or second accent.
- Contrast: text at least 4.5:1, icons and large text at least 3:1, on every surface, including over glass.

## Materials and depth

- Three surfaces: background for content, raised for sheets, dialogs, and popovers, and glass only for controls floating over content where the platform uses it. Never glass on glass or on a scrolling area.
- Shadows only lift floating layers. Buttons, rows, and selections stay flat.

## Shape

- A short radius scale and nothing outside it, with a corner no larger than the padding beside it.
- Nested shapes are concentric: inner radius equals outer radius minus the inset.
- Follow the platform: on iOS, containers concentric with the device corners and capsule controls.

## Type

- The platform's system font unless the brand sets one. A few roles (title, body, meta, caption) in two weights. Monospace only for code, commands, and paths.
- Tabular figures for numbers that line up or tick, and body lines of 45 to 75 characters.

## Icons

- One icon set, one weight per context, monochrome. Logos keep their own colours.
- Every icon-only control has an accessible label and a tooltip naming its action.

## Density

- Fixed row heights so lists line up. A compact mode removes padding, never hierarchy.
- Scrollbars stay hidden unless the platform requires them, and an axis never gets two.

## Tokens

Every value comes from the token set. When none fits, add a token rather than a one-off.
