---
name: accessibility
description: Use when building or reviewing UI code or when accessibility, a11y, ARIA, contrast, or screen readers come up. WCAG 2.2 AA.
---

# Accessibility (WCAG 2.2 AA)

Adapted from [affaan-m/ECC](https://github.com/affaan-m/ECC) (`skills/accessibility`, MIT, © 2026 Affaan Mustafa). Condensed, reworded, and corrected in places against the WCAG 2.2 text; see `UPGRADES.md` for the adoption record.

Apply this while writing UI, not as a pass afterwards.

## For each component

1. **Role.** What is it functionally — button, link, tab, checkbox? Use the native element or control for that role. Custom roles are a last resort, and then need keyboard handling too.
2. **Name.** Every interactive element has an accessible name. Icon-only controls get a text label; decorative images are hidden from assistive tech.
3. **State and value.** Checked, expanded, selected, disabled, current value are exposed programmatically, not only visually.
4. **Keyboard.** Reachable and operable without a pointer, in a sensible order, with a visible focus indicator that isn't covered by sticky headers or overlays.
5. **Changes.** Status messages that appear without a page change are announced (live region on web; an accessibility announcement on native).

## Numbers to meet

| Requirement | Threshold | WCAG |
|-------------|-----------|------|
| Text contrast | 4.5:1; 3:1 for large text | 1.4.3 |
| UI component and graphic contrast | 3:1 | 1.4.11 |
| Pointer target size (web) | at least 24×24 CSS px, or enough spacing | 2.5.8 |
| Touch target (native, platform guidance) | 44×44 pt iOS, 48×48 dp Android | — |
| Reflow | usable at 400% zoom / 320 CSS px wide without two-way scrolling | 1.4.10 |

Also: don't convey meaning by color alone (1.4.1); give dragging a single-pointer alternative (2.5.7); error messages say what is wrong and how to fix it in text (3.3.1, 3.3.3); don't ask for the same information twice in one flow (3.3.7).

## Platform mapping

| Need | Web | iOS (SwiftUI) | Android (Compose) |
|------|-----|---------------|-------------------|
| Name | `<label>`, visible text, `aria-label` | `.accessibilityLabel()` | `contentDescription` |
| Extra description | `aria-describedby` | `.accessibilityHint()` | — |
| Role | native element, else `role="…"` | `.accessibilityAddTraits()` | `Modifier.semantics { role = … }` |
| Live update | `aria-live="polite"` | post an announcement | `Modifier.semantics { liveRegion = … }` |

Check the platform documentation for exact current API names before relying on a row.

## Overlays

- A modal keeps focus inside while open, closes with Escape or an explicit close control, and returns focus to the element that opened it.
- Menus and dropdowns return focus to their trigger on close.

## Common mistakes

- A `<div>` or `<span>` with a click handler and no role or keyboard support.
- Red border as the only error signal.
- Alt text beginning "Image of…" — the role is already announced.
- `aria-label` on an element that already has clear visible text, replacing it with something different.
- Placeholder used as the only label.

## Before finishing

- [ ] Tab through the UI: everything reachable, order sensible, focus always visible.
- [ ] Every control has a name; icon-only buttons included.
- [ ] Contrast and target sizes meet the table.
- [ ] Modals and menus manage focus.
- [ ] Errors are explained in text.
- [ ] Layout survives zoom / large text.

Say what was checked and how. If nothing was run with a real screen reader or automated checker, say that rather than claiming compliance.

Reference: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/).
