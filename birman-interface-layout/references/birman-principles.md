# Interface and screen-layout principles

This is a concise interpretation of public material by and about Ilya Birman. It is not a replacement for his books or courses, and it does not reproduce their text.

## Scenario and space

An interface can be examined as both a scenario and a spatial composition. A good layout supports the intended sequence of decisions. A poor spatial solution can introduce unnecessary steps even when the interaction logic is otherwise sound.

## Interface language

Controls, labels, values, hints, errors, and states form a language. Repeated roles should have repeated treatment. Text must tell the user what is happening and what an action changes, rather than expose internal terminology.

## Forms

Fields are units: label, entry, help, validation, and value must remain visibly associated. Align their baselines and spacing consistently. Keep error messages local to the affected field and state the next useful action.

## Adaptive screens

Responsive work is not a uniform scale-down. Consider each page band or "floor" separately: navigation, primary action area, content, supporting panels, and utilities may require different adaptation rules. Preserve task flow and readable content before retaining desktop geometry.

## Information hierarchy

Give primary actions and decisions prominence. Secondary information may be quieter, but not ambiguous. When user attention is split, change the structure or sequence instead of relying on decoration to resolve the conflict.
