---
name: site-delivery-qa
description: Build and finish frontend pages through a safe inspect–implement–run–visual-QA–fix–recheck cycle. Use when creating, redesigning, or materially changing a web UI; it complements existing design, motion, SEO, responsive, and browser-QA skills rather than replacing them.
---

# Site delivery QA

Use this as the delivery coordinator for a user-facing web change. Preserve the project's existing stack and project rules. This skill is not a mandate to install a design system or rewrite the current UI.

## 1. Inspect before changing anything

- Read repository instructions and inspect the nearest matching page, components, tokens/theme, styles, and package manager files.
- Check `package.json`, lockfile, component folders, and configuration before proposing Tailwind, shadcn/ui, Lucide, Motion, or Playwright. Reuse an equivalent existing library; add a dependency only when the needed capability is absent and the requested implementation needs it.
- Keep routes, anchor IDs, form names, analytics hooks, working SEO metadata, and existing accessible behavior unless the user explicitly changes them.

## 2. Build with a deliberate visual system

- Establish or reuse tokens for type, spacing, color, borders, radii, focus rings, and responsive containers. Do not scatter unexplained one-off values.
- Use hierarchy, whitespace, grid alignment, and one coherent accent strategy to make the primary task obvious.
- Treat cards as a semantic grouping tool, not a default layout. Vary section composition when it improves scanning, while retaining the same tokens and type system.
- Reject generic AI styling: equal-card section after equal-card section, decoration without meaning, arbitrary gradients/shadows, oversized type without content reason, excessive rounding, low-contrast blue-on-blue surfaces, and copied component-library defaults.
- Build complete states: hover, focus-visible, active, disabled where relevant, loading/empty/error/long-text states, and keyboard access.

## 3. Motion only where it explains change

- Use CSS for simple feedback. Use Motion in React for accordion/FAQ, dropdown, tabs, modal, layout and presence transitions when it is already installed or its addition is justified. Use GSAP only for authored timeline or scroll work.
- Do not switch interactive content with `display: none` / `display: block` when an exit or size transition is part of the experience. Use opacity/transform plus an appropriate layout or height transition; use `AnimatePresence` for React exit states.
- Make accordion, FAQ, dropdown, tabs, modal, buttons, arrows, hover effects, and resizable UI interruptible. Provide reduced-motion behavior and never animate merely for decoration.

## 4. Run, inspect, repair, recheck

1. Run the project’s relevant build, typecheck, lint, or test command when available.
2. Start the local app using its documented command. If browser tooling is available, use it for visual and interaction QA; otherwise state the limitation rather than claiming visual verification.
3. Inspect the primary route at **320, 375, 768, 1024, and a desktop width**. Test the whole page, not just the hero.
4. Exercise each changed interaction: open/close, keyboard focus and Escape where applicable, repeat clicks/taps, navigation, and long content. Check for console errors and failed requests.
5. Fix the issues found in the same scoped surface, then repeat the affected checks. Stop after the surface is clean or report a concrete external blocker; do not run open-ended cosmetic passes.

At each viewport, reject horizontal overflow, clipped controls, overlay collisions, broken grids, wrapped primary CTAs, oversized headings, unstable layout, and inaccessible touch/focus behavior.

## 5. Final quality gates

- Review hierarchy, spacing rhythm, alignment, type scale/measure, contrast, buttons, cards, FAQ, navbar, footer, icons/arrows, and responsive composition.
- Keep semantic HTML: meaningful landmark structure, one logical H1, ordered H2–H6, labels, accessible names, and content available to crawlers without unnecessary client-only rendering.
- Preserve or add only justified SEO fundamentals: unique title and description, canonical when the stack supports it, Open Graph, descriptive image `alt`, relevant internal links, and truthful Schema.org. Do not modify robots, sitemap, redirects, production indexability, or schema claims without explicit authorization.
- Watch Core Web Vitals: avoid unnecessary JavaScript, reserve media dimensions, keep the LCP path light, and avoid layout shifts.

For specialized depth, load the existing `impeccable` skill for visual polish, `responsive-audit` for breakpoint diagnosis, `browser-qa`/`playwright` for real-browser checks, `motion-gsap-lenis` for implementation choices, and `seo` for a full SEO review.
