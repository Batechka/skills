# Implementation reference

## Motion.dev

Use Motion's declarative React API for UI that follows component state. `AnimatePresence` owns exits; layout transitions belong to the components whose geometry changes. In Next.js, isolate Motion usage in a client component. Use `MotionConfig` or `useReducedMotion` to make reduced-motion behavior deliberate. Keep simple hover color changes in CSS rather than importing a runtime for them.

## GSAP

Build one timeline for a single authored beat rather than a set of unrelated timeouts. Use ScrollTrigger only when scroll is the meaningful input. Register plugins once, scope selectors to the component, and revert/kill created GSAP instances and ScrollTriggers on unmount. Refresh measurements once layout-critical assets and fonts finish loading—not repeatedly during ordinary animation.

## Lenis with GSAP

Add Lenis at the app shell only when it serves an intentional smooth-scroll experience. Create a single Lenis instance. If GSAP drives the animation frame, connect Lenis to that ticker and turn off GSAP lag smoothing where the official integration requires it. On Lenis scroll, call `ScrollTrigger.update()`; after an impactful layout change, call `ScrollTrigger.refresh()`.

Never use this integration inside a nested scrolling panel by default. Disable or reduce the enhanced scroll behavior for `prefers-reduced-motion`, and retain normal anchor and keyboard navigation.
