#!/usr/bin/env python3
"""Check every skill against the repo's rules. Run: python3 scripts/check.py"""

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r'^"?\d+\.\d+\.\d+"?$')
DASHES = ("—", "–")
# A loaded skill is re-attached after compaction only up to 5,000 tokens, so the
# whole SKILL.md must fit well inside that. Words are a cheap proxy for tokens.
MAX_SKILL_WORDS = 2500
MAX_SKILL_LINES = 500

errors = []


def fail(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def parse_frontmatter(path):
    text = path.read_text()
    if not text.startswith("---\n"):
        fail(path, "missing frontmatter")
        return {}, {}, text
    head, _, body = text[4:].partition("\n---\n")
    keys, metadata, in_metadata = {}, {}, False
    for line in head.splitlines():
        if line.startswith("  ") and in_metadata:
            key, _, value = line.strip().partition(":")
            metadata[key.strip()] = value.strip()
            continue
        key, _, value = line.partition(":")
        keys[key.strip()] = value.strip()
        in_metadata = key.strip() == "metadata"
    return keys, metadata, body


def changed_skills():
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", "origin/main...HEAD"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return set()
    return {line.split("/")[0] for line in out.splitlines() if "/" in line}


def main_version(skill):
    try:
        text = subprocess.run(
            ["git", "show", f"origin/main:{skill}/SKILL.md"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except subprocess.CalledProcessError:
        return None
    match = re.search(r'^\s+version:\s*(\S+)', text, re.M)
    return match.group(1) if match else None


readme = (ROOT / "README.md").read_text() if (ROOT / "README.md").exists() else ""
changed = changed_skills()

skills = sorted(p.parent for p in ROOT.glob("*/SKILL.md"))
for skill in skills:
    path = skill / "SKILL.md"
    keys, metadata, body = parse_frontmatter(path)

    for key in keys:
        if key not in ALLOWED_KEYS:
            fail(path, f"frontmatter key '{key}' is outside the Agent Skills spec")
    if keys.get("name") != skill.name or not NAME_RE.match(skill.name):
        fail(path, "name must match the folder and be lowercase words joined by hyphens")
    description = keys.get("description", "")
    if not description.startswith("Use ") or len(description) > 1024:
        fail(path, "description must start with 'Use ' and stay under 1024 characters")
    if not SEMVER_RE.match(metadata.get("version", "")):
        fail(path, "metadata.version must be a semver string like \"1.2.0\"")
    if not metadata.get("author"):
        fail(path, "metadata.author is missing")

    words, lines = len(path.read_text().split()), path.read_text().count("\n")
    if words > MAX_SKILL_WORDS or lines > MAX_SKILL_LINES:
        fail(path, f"too long ({words} words, {lines} lines); move reference material out")

    for link in re.findall(r"\]\(((?:references|scripts|assets)/[^)]+)\)", body):
        if not (skill / link).exists():
            fail(path, f"links to missing file {link}")

    if not (skill / "agents" / "openai.yaml").exists():
        fail(path, "agents/openai.yaml is missing")
    if f"`{skill.name}`" not in readme:
        fail(path, "not listed in README.md")

    for file in skill.rglob("*"):
        if file.suffix in {".md", ".yaml"} and any(d in file.read_text() for d in DASHES):
            fail(file, "contains an em or en dash")

    if skill.name in changed:
        before = main_version(skill.name)
        if before is not None and before == metadata.get("version"):
            fail(path, f"changed since main but metadata.version is still {before}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"{len(skills)} skills pass")
