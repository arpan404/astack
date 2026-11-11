# Cross-platform

Each platform should feel native: navigation, back behavior, sheets, type, and haptics follow the host OS. Share logic and tokens, not identical pixels, unless the brand demands one look everywhere.

- **React Native:** Expo UI (`@expo/ui`) renders real SwiftUI and Jetpack Compose components, so controls get Liquid Glass and Material 3 for free. Prefer it to JavaScript reimplementations for pickers, sliders, menus, switches, and sheets, wrapped in its `Host`. Use the native navigation Expo Router provides. Check the current Expo SDK docs first.
- **Flutter:** Material 3 on Android, Cupertino or the `.adaptive` constructors on iOS. A Material look on iOS only when the brand is custom everywhere.
- **Compose Multiplatform:** Material 3 shared across targets, with native iOS screens where platform feel matters most.
