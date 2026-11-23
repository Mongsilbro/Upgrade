#!/usr/bin/env python3
"""Check every .claude/skills/*/SKILL.md frontmatter.

Fails (exit 1) when frontmatter is not valid YAML, `name` is missing or differs
from the folder name, `description` is missing or over 200 characters (claude.ai
upload limit), or all descriptions together exceed 4,200 characters.
Run from the repository root: python3 -I scripts/check-skills.py
"""
import glob
import os
import sys

import yaml

PER_SKILL = 200
TOTAL = 4200  # "about 4,000" in CLAUDE.md step 9

errors, total = [], 0
files = sorted(glob.glob(".claude/skills/*/SKILL.md"))
for path in files:
    folder = os.path.basename(os.path.dirname(path))
    text = open(path, encoding="utf-8").read()
    parts = text.split("---", 2)
    if not text.startswith("---") or len(parts) < 3:
        errors.append(f"{path}: no frontmatter block")
        continue
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        errors.append(f"{path}: invalid YAML ({str(e).splitlines()[0]})")
        continue
    if meta.get("name") != folder:
        errors.append(f"{path}: name {meta.get('name')!r} != folder {folder!r}")
    desc = meta.get("description")
    if not isinstance(desc, str) or not desc.strip():
        errors.append(f"{path}: missing description")
        continue
    total += len(desc)
    if len(desc) > PER_SKILL:
        errors.append(f"{path}: description {len(desc)} chars > {PER_SKILL}")

if total > TOTAL:
    errors.append(f"all descriptions: {total} chars > {TOTAL}")
for e in errors:
    print("FAIL", e)
print(f"{len(files)} skills, descriptions {total} chars, {len(errors)} problem(s)")
sys.exit(1 if errors else 0)
