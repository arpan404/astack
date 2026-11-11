# Apple platforms

- SwiftUI first, with UIKit or AppKit where SwiftUI falls short. Standard components (navigation stacks, tab views, toolbars, sheets, lists, forms, menus, search) pick up Liquid Glass and system behavior on their own. Custom lookalikes don't, and they age badly with each OS release.
- Liquid Glass belongs to the navigation and control layer that floats above content: bars, toolbars, tab bars, floating controls. Content itself (lists, cards, backgrounds) stays solid. Never stack glass on glass.
- A custom control in that layer uses the system glass APIs and button styles, never a hand-made blur and gradient.
- Content runs edge to edge under the bars. Respect safe areas and use the system's scroll edge effects.
- Test with Reduce Transparency, Increase Contrast, Reduce Motion, the largest Dynamic Type size, and each Liquid Glass appearance setting the OS offers.
- SF Symbols for icons, the system font, and semantic colors with the app's tint.
- Platform idioms: swipe actions, context menus, sheets with detents, large titles, pull to refresh. On iPad, sidebars and multiple columns. On Mac, menu bar commands, keyboard shortcuts, and pointer states.
- Hit targets of at least 44 by 44 points.
- Check the current Human Interface Guidelines and Apple's "Adopting Liquid Glass" docs for the OS version you target.

## Mobile patterns

- The tab bar is for navigation, never actions: always visible, labelled, with no disabled tabs. It can shrink on scroll.
- Sheets one at a time, with a grabber and swipe to dismiss, and Done paired with Cancel. Long flows go full screen.
- Clear glass only over rich media, with the content dimmed beneath it when bright.
- Every gesture has a visible alternative, like a delete button beside swipe to delete. Leave system gestures alone.
- Haptics only in their system meanings (success, warning, selection), sparingly, and never as the only signal.
- Keep frequent targets away from the screen corners.
