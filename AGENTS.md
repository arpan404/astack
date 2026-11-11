# astack

Agent skills for engineering work. Each top-level folder is one skill: `SKILL.md`, optional `references/`, and `agents/openai.yaml` for Codex.

Check: `python3 scripts/check.py`. Run it before every commit.

## Writing a skill

- Frontmatter holds only Agent Skills spec fields: `name`, `description`, `metadata` (with `author` and `version`), and optionally `license`, `compatibility`, `allowed-tools`. Harness-specific fields break strict validators and claude.ai uploads.
- The description says only when to use the skill, starts with "Use when", and puts the trigger first: listings truncate descriptions.
- The body works whether the harness loads it on demand or preloads it at startup (subagents with a `skills` list): standing instructions, no reliance on arguments or on a request having just happened.
- Keep `SKILL.md` short. After the conversation is summarized, a harness keeps only the first 5,000 tokens of each loaded skill, so the rules that matter most come first.
- Material only some tasks need goes in `references/`, linked from `SKILL.md` with when to read it, one level deep.
- Write for current frontier models: the bar, the judgment calls, and the gotchas, not commands they already know.
- No em or en dashes anywhere.

## Versions

Every change to a skill bumps its `metadata.version`: patch for wording, minor for new guidance, major when its behaviour changes. The check fails when a changed skill keeps main's version.

## Commits

No `Co-Authored-By` or AI attribution in commits. PR bodies end with one `Model:` line naming the model that wrote the change.
