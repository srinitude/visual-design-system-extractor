# Agent Skills Compliance Reference

Source refresh date: 2026-05-17.

Use this reference only when editing, reviewing, packaging, or validating this skill. Do not load it during ordinary visual extraction runs.

## Source Inventory

- Agent Skills URL map: https://agentskills.io/
- Canonical documentation index: https://agentskills.io/llms.txt
- Format specification: https://agentskills.io/specification
- Creator best practices: https://agentskills.io/skill-creation/best-practices
- Description optimization: https://agentskills.io/skill-creation/optimizing-descriptions
- Output evaluation: https://agentskills.io/skill-creation/evaluating-skills
- Script guidance: https://agentskills.io/skill-creation/using-scripts
- Anthropic guide: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf

## Compliance Rules For This Package

- The skill directory must contain `SKILL.md` exactly, with YAML frontmatter followed by Markdown.
- The frontmatter `name` must be `visual-design-system-extractor` and must match the parent directory.
- The frontmatter `description` must stay under 1024 characters and must include both when to use the skill and what it produces.
- Use `compatibility` only for real runtime requirements. This skill uses it because deterministic validation depends on Python 3.9+ and PyYAML through `uv` with `requirements.txt` or an installed environment.
- Keep support-file paths relative to the skill root: `references/extraction-schema.md`, `scripts/schema_tools.py`, and `scripts/validate_design_system_yaml.py`.
- Keep `SKILL.md` under 500 lines and roughly under 5000 tokens. Move schema detail and compliance research into `references/`.
- Additional files are allowed when they directly support the skill. The `agents/openai.yaml` file is client metadata and must stay aligned with the skill's frontmatter.

## Portable Best Practices Adopted

- Use progressive disclosure: frontmatter for triggering, `SKILL.md` for the runbook, `references/` for long schemas, and `scripts/` for deterministic mechanics.
- Start from real use cases: reference-image analysis, design-token extraction, valid YAML output, rare-but-grounded font selection, and implementation-ready design-system contracts.
- Be prescriptive where the task is fragile. YAML validity, key order, duplicate-key rejection, required sections, and rare-font structure are enforced by scripts rather than prose alone.
- Prefer defaults over menus. The default path is skeleton generation, one-pass fill, validator run, repair, and final raw YAML.
- Use procedures instead of generic quality claims. The skill states the exact sequence, files, commands, and validation gate.
- Keep the skill composable and platform-aware. The main instructions do not assume one host client except where local validation tools are explicitly required.
- Validate with concrete evidence before claiming success. Package validation should include frontmatter checks, script compile checks, skeleton parse checks, and positive and negative YAML fixtures.

## Determinism Checklist

- The skeleton from `scripts/schema_tools.py skeleton` parses as YAML.
- Every comprehensive extraction preserves the skeleton's top-level order and nested key order.
- Every required top-level section is present.
- Not-applicable fields use the standard object shape, not `null`.
- `source_analysis.observed`, `source_analysis.inferred`, and `source_analysis.speculative` stay separated.
- `typography.font_families.rare_unique_candidates` is non-empty and every candidate has all validator-required fields.
- The validator rejects markdown fences, tabs, duplicate keys, missing or extra top-level sections, wrong top-level order, malformed not-applicable objects, invalid confidence labels, common UI defaults as rare candidates, and missing rare-font candidate fields.
