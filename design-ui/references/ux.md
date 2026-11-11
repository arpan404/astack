# Interaction

The default is direct: people act on the thing itself, see the result at once, and can take it back.

## Instead of a form

- **Direct manipulation:** drag to reorder, resize, or move. Toggle state where it's shown. Keep the object visible while it changes.
- **Edit in place:** click a value to edit it; Enter or blur saves, Escape cancels. A modal only for an edit that needs several related fields at once.
- **Create in context:** a new item appears where it will live, ready to type into, instead of on a "New item" page.
- **Smart defaults:** prefill from context, the last choice, or the most common case. Ask only for what can't be inferred.
- **Progressive disclosure:** the common path stays visible; advanced options sit one step away.
- **Recognition over recall:** show recent items, suggestions, and options. Search with typeahead.
- **Undo over confirm:** routine and reversible actions happen at once and offer undo. Confirm only what is irreversible and costly, with buttons named by outcome: "Delete project" and "Keep project", never "Yes" and "No".
- **Optimistic updates:** show the change immediately; on failure, roll back and say so where it happened.
- **Stay on the page:** search, previews, and quick edits open in place (a palette, popover, or side panel) instead of navigating away.
- **Tabular data entry** behaves like a spreadsheet: cells edit in place, arrow keys and Tab move between them, and paste fills many at once.
- **Accelerators:** keyboard shortcuts for frequent actions, shown beside their menu items, and a command palette on desktop and web apps. Newcomers can ignore them.

## Layout of a task

- Primary content first. Decoration never pushes the task below the fold.
- Controls sit next to what they act on.
- Fewer choices per step. Split a task into steps only when the steps are truly sequential.
- Frequent targets large and close; destructive actions away from common ones.

## Stability and consistency

- Live updates never move what the user is reading or working on: scroll position, selection, focus, and in-progress input all hold.
- One pattern per kind of action across the product. A single action shows directly instead of hiding in a menu.
- Each fact shows in one place.

## Feedback

- Feedback lives next to its cause: a pressed state at once, a saved value in place, a validation message under its field.
- Toasts only for passive confirmations that need nothing from the user, and never for errors. Nothing important disappears on a timer.
- Modals only for decisions that must be made before continuing, one at a time.
- **Loading:** under a second, nothing beyond the pressed state. One to ten seconds, a spinner for a part of the screen, or a skeleton that matches the real layout for a whole page. Over ten seconds or for uploads, a progress bar with an estimate. Say what is loading.
- **Errors:** next to the cause, specific, blame-free, with the fix. Keep what the user entered. Use an icon or text along with color.
- **Empty states:** say why it's empty and offer the action that fills it, in place. Never show "No results" while still loading.

## Scope

Build what was asked. Every extra control, setting, badge, banner, or screen costs attention and maintenance. Make product decisions with good defaults instead of exposing them as settings. Suggest additions to the user rather than shipping them.
