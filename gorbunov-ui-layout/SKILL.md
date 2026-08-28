---
name: gorbunov-ui-layout
description: Design or review web UI with typographic hierarchy, modular layout, anchor objects, and meaning-first editorial clarity. Use for information-dense pages, landing pages, services, editorial interfaces, and UI polish; do not use to imitate Bureau Gorbunov's proprietary works or branding.
---

# Gorbunov Ui Layout

Use this as a craft lens inspired by publicly described layout principles from Artem Gorbunov's typography and layout teaching. Build an original interface around the product's content, not a visual imitation of a particular Bureau project.

Read [the principles reference](references/gorbunov-principles.md) before making a substantial UI decision.

## Working method

Start from meaning. Identify the primary user task, the main message, supporting evidence, controls, and secondary information. Establish the reading order before choosing decoration, imagery, or animation.

Choose the page's anchor objects: elements that should stabilize perception, such as a headline, a key figure, a primary illustration, navigation, or a principal action. Align the rest of the composition to these anchors rather than centering every block by habit.

Make a compact layout system before implementation:

- a column or modular grid appropriate to the content;
- type roles for display, heading, body, metadata, labels, and controls;
- a spacing scale with a clear distinction between relationships inside a module and between separate modules;
- rules for images, captions, links, and controls.

## Layout and type decisions

Treat body text as a readable rectangle and headings as directional lines. Keep prose at a comfortable measure; do not force text into a shape that damages reading just to make a grid look symmetrical. Let a headline wrap intentionally, and ensure it still states the core idea when scanned alone.

Use proximity, alignment, whitespace, type contrast, and restrained color to show relationships. Cards, borders, shadows, and decorative labels need a semantic job; remove them if whitespace or alignment carries the hierarchy better.

Build modules that can stand on their own: each needs an intelligible internal order, but its external spacing must make its relationship to neighboring modules unambiguous. Avoid equal visual weight for unequal content.

For responsive layouts, preserve reading order and anchors while changing the geometry. Check long Russian words, content expansion, touch targets, and table/list reflow; do not simply shrink desktop proportions.

## Review gate

Before presenting a result, verify that:

- the main message, action, and supporting material are distinguishable at a glance;
- every repeated spacing and type role follows the system;
- captions, links, controls, and metadata remain subordinate without becoming illegible;
- text, images, and controls are visually connected to the content they describe;
- the design remains original and does not claim Bureau Gorbunov affiliation.
