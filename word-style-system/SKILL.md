---
name: word-style-system
description: Apply the established Word Online interface rules to new or revised Word/document-service sites. Use for shared header, responsive layout, CTA, FAQ, and typography decisions; do not use for unrelated apps.
---

# Word Online Interface Standard

Use this standard when a site is a Word, DOCX, or document-creation service and the user asks to apply the established visual rules.

- Keep the logo at the left edge of the header. On desktop, center navigation against the full header viewport (not the free space between logo and actions). Place compact `Попробовать` and `Войти` controls on the right; use the real approved sign-in route when available.
- Keep actions compact: 36–40px tall, 14–18px horizontal padding, and short action labels. Do not use promotional CTA sentences in buttons.
- On small screens, retain the logo and primary action; move navigation into a keyboard-accessible menu. A visible header background and border are required above imagery or pale content.
- Let the first meaningful hero element be the H1. Do not put breadcrumbs, category labels, badges, or taxonomy above it. Keep it to two or three lines at normal viewport widths.
- Use `h1: clamp(32px, 4vw, 52px)`, `h2: clamp(26px, 3vw, 38px)`, `h3: clamp(20px, 2vw, 26px)`, and normal body copy at 16px/1.6 unless a compact UI label needs a smaller token.
- Use a shared content container equivalent to `width: min(1200px, calc(100% - 32px)); margin-inline: auto`. Ensure grid and flex children can shrink (`min-width: 0`), content wraps, images scale, and no page gets a horizontal scrollbar.
- Space ordinary desktop sections 48–64px apart and mobile sections 32–48px apart. Do not create empty visual spacers or use viewport-height sections without a product reason.
- End every content page as `FAQ → CTA → footer`. FAQ answers begin closed, exactly one answer may be open, and opening one closes another. Preserve a short opacity/height transition and honour `prefers-reduced-motion`.
- Use one visual language across shared components; do not change the page meaning or invent new content merely to fit a pattern.

Before handing off a site, test the shared components at 1440, 1024, 768, 390, and 320px. Check header centering, menu interaction, button labels and states, wrapping, the exclusive FAQ behavior, the CTA/footer ordering, focus visibility, and horizontal overflow.
