---
name: birman-interface-layout
description: Design or review interfaces with scenario-first interaction, spatial clarity, precise labels, and component-by-component responsive adaptation. Use for forms, navigation, information-heavy interfaces, and UI polish; do not use to imitate Ilya Birman's proprietary work or branding.
---

# Birman Interface Layout

Use this as a practical interface-design lens based on publicly described principles from Ilya Birman's writing and teaching. Create an original product interface; do not claim affiliation or mimic a named product.

Read [the principles reference](references/birman-principles.md) before a substantial UI design, redesign, or responsive-layout decision.

## Solve the task twice

Define both sides of the interface problem before styling:

1. **Scenario:** who does what, from what state, with what decision, feedback, recovery path, and completion signal.
2. **Space:** where each action and piece of information belongs, what remains visible, what can be deferred, and what changes at narrower widths.

Do not add a step, modal, or control merely to compensate for weak layout. Prefer a direct action in the existing context when it preserves clarity and safety.

## Interface language

Name actions and states precisely. Labels should state what a control does or what a field contains, not reproduce implementation vocabulary. Put labels, values, help, validation, and actions in a consistent visual grammar.

Associate each piece of text with the element it describes through placement and alignment. For forms, make field labels, inputs, hints, errors, and confirmations scan as one unit. Use typographic hierarchy to distinguish primary content from operational detail without hiding necessary information.

## Spatial rules

Start with the highest-value action and information. Build a predictable alignment system, then use density and whitespace to show grouping and priority. Preserve position for stable repeated controls; avoid visual rearrangements that cause users to re-learn a flow.

Treat navigation, content, and controls as separate layout bands when that makes their behavior clearer. At responsive breakpoints, adapt each band according to its job instead of shrinking the whole desktop composition uniformly.

## Review gate

Before presenting a result, verify that:

- the core task is possible with the fewest justified decisions and screens;
- visible labels explain actions, values, state, and consequences;
- hierarchy follows user priority rather than available UI chrome;
- forms and errors remain understandable without guesswork;
- each responsive change preserves the scenario and information relationships;
- the work is original and does not imply Ilya Birman's involvement.
