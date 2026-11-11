# Android

- Jetpack Compose with Material 3 (`androidx.compose.material3`). Use Material 3 Expressive through `MaterialExpressiveTheme` when the project's library version supports it; check the current stable release first.
- Material components before custom ones: scaffold, app bars, navigation bar and rail, floating action button, bottom sheets, search bar, button groups, loading indicators.
- Dynamic color from the user's wallpaper unless the brand forbids it. Build the color scheme from tokens, never scattered hex values.
- Edge to edge, with window insets handled, and predictive back supported.
- Adaptive layouts for phones, foldables, and tablets, driven by window size classes (list and detail, supporting pane).
- Material motion, kept off screens people use quickly and often, and reduced when the system asks.
- Material Symbols for icons, touch targets of at least 48dp, TalkBack labels, and layouts that survive 200% font scale.
- XML Views only for legacy screens; the Views component library is in maintenance mode.

## Mobile patterns

- Apps targeting Android 16 are always edge to edge, and predictive back animates by default. Keep drag targets out of the gesture insets.
- A navigation bar on compact windows, a navigation rail on medium and wider.
- Every gesture has a visible alternative, and haptics follow their system meanings.
