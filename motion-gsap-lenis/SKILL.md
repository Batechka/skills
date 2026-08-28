---
name: motion-gsap-lenis
description: Design and implement purposeful web motion with Motion.dev, GSAP and Lenis. Use for React UI transitions, scroll narratives, smooth scrolling, and deciding which animation tool fits; do not add motion merely as decoration.
---

# Motion stack: Motion, GSAP, Lenis

Start from the job an animation performs: reveal a state change, preserve spatial continuity, guide a scroll narrative, or give direct feedback. Keep the interface fully usable and intelligible without animation.

## Select one primary tool

- Use CSS transitions/keyframes for isolated, predictable cosmetic feedback: hover, focus, opacity and color changes.
- Use **Motion.dev** for stateful React UI: entry/exit, dialogs, menus, tabs, reordering, gestures, shared-layout transitions, and simple in-view effects. Keep the animation close to the client component that owns its state.
- Use **GSAP + ScrollTrigger** for coordinated timelines, pinned scenes, scrubbed sequences, text/media choreography, SVG or canvas/WebGL synchronized to scroll. In React, scope and clean up every timeline and trigger using the official GSAP React pattern.
- Use **Lenis** only when a continuous, art-directed scroll feel or frame-accurate scroll synchronization is an actual part of the product experience. Do not add it to ordinary product surfaces just to make them feel premium.

Do not give the same interaction competing owners: a Motion-controlled transform should not also be driven by GSAP. Use one smooth-scroll engine per document. When Lenis and ScrollTrigger are both needed, synchronize their frame loop, update ScrollTrigger on Lenis scroll, and refresh after fonts, images, or layout-changing content settle.

## Quality bar

- Prefer `transform` and `opacity`; avoid perpetual layout/paint-heavy animation.
- Make motion interruptible when user input changes state. Clean up listeners, RAF loops, timelines and triggers on unmount.
- For React accordion/FAQ, dropdown, tabs, modal, and conditional content, use Motion layout transitions and `AnimatePresence` when an exit must be perceived. Do not rely on a visible `display: none` to `display: block` jump. Preserve correct ARIA state, focus behavior, Escape handling, and a usable no-motion state.
- Check repeat open/close and rapid pointer or keyboard interaction, not just the first transition. Small controls, arrows, and hover feedback should reinforce the action without delaying it.
- Respect `prefers-reduced-motion`: remove nonessential parallax, scrub, pinning and large transforms; preserve semantic feedback with short fades or no animation.
- Do not hijack nested scrolling, keyboard navigation, anchors, text selection, browser history, or focus restoration. Keep a native-scroll fallback.
- Test the real interaction on touch and a low-power viewport. Avoid scroll effects that obscure reading, delay controls, or make long pages tiring.

Read [the stack reference](references/stack.md) when implementing or reviewing the setup, especially for React lifecycle or GSAP–Lenis synchronization.
