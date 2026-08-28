#!/usr/bin/env python3
"""Fast, dependency-free structural validation for this skill collection."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {".git", ".github", "scripts"}
FIELD_RE = re.compile(r"^(name|description):\s*(.+?)\s*$", re.MULTILINE)
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    return None if end < 0 else text[4:end]


def main() -> int:
    errors: list[str] = []
    names: dict[str, Path] = {}
    skill_dirs = sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir() and path.name not in IGNORED_DIRS
    )

    for directory in skill_dirs:
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{directory.name}: missing SKILL.md")
            continue
        if not KEBAB_RE.fullmatch(directory.name):
            errors.append(f"{directory.name}: folder name must use kebab-case")

        text = skill_file.read_text(encoding="utf-8")
        header = frontmatter(text)
        if header is None:
            errors.append(f"{directory.name}: invalid or missing YAML frontmatter")
            continue

        fields = dict(FIELD_RE.findall(header))
        for required in ("name", "description"):
            if not fields.get(required, "").strip(" '\""):
                errors.append(f"{directory.name}: missing {required} in frontmatter")

        name = fields.get("name", "").strip(" '\"")
        if name:
            if name in names:
                errors.append(
                    f"{directory.name}: duplicate skill name {name!r} "
                    f"(also in {names[name].name})"
                )
            names[name] = directory

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skills successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
