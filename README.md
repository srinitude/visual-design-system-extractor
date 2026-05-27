# Visual Design System Extractor

[![skills.sh](https://skills.sh/b/srinitude/visual-design-system-extractor)](https://skills.sh/s/srinitude/visual-design-system-extractor)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Validate](https://github.com/srinitude/visual-design-system-extractor/actions/workflows/validate.yml/badge.svg)](https://github.com/srinitude/visual-design-system-extractor/actions/workflows/validate.yml)

A portable Agent Skills package for extracting production-grade visual design systems from screenshots, moodboards, style frames, brand boards, product UI shots, and cinematic references.

The skill turns visual evidence into parser-valid YAML with a deterministic schema, grounded confidence labels, reusable design tokens, rare-but-evidence-backed typography candidates, and implementation notes for design-engineering workflows.

## Install

```bash
npx skills add srinitude/visual-design-system-extractor
```

To preview the skills exposed by this repository:

```bash
npx skills add srinitude/visual-design-system-extractor --list
```

## Use Cases

- Extract UI, brand, motion, cinematic, and implementation tokens from visual references.
- Convert reference images into a consistent YAML design-system contract.
- Preserve schema order, confidence labels, evidence boundaries, and not-applicable fields across runs.
- Validate generated YAML before returning it to downstream design or engineering tools.

## Package Structure

```text
visual-design-system-extractor/
|-- skills/
|   `-- visual-design-system-extractor/
|       |-- agents/
|       |   `-- openai.yaml
|       |-- references/
|       |   |-- agent-skills-compliance.md
|       |   `-- extraction-schema.md
|       |-- scripts/
|       |   |-- schema_tools.py
|       |   `-- validate_design_system_yaml.py
|       |-- requirements.txt
|       `-- SKILL.md
|-- skills-lock.json
|-- package.json
|-- README.md
|-- LICENSE
`-- NOTICE
```

## Validation

Validate the skill package:

```bash
skills-ref validate "$PWD/skills/visual-design-system-extractor"
```

Validate the bundled scripts:

```bash
python3 -m py_compile skills/visual-design-system-extractor/scripts/schema_tools.py skills/visual-design-system-extractor/scripts/validate_design_system_yaml.py
python3 skills/visual-design-system-extractor/scripts/schema_tools.py --help
uv run --with-requirements skills/visual-design-system-extractor/requirements.txt python skills/visual-design-system-extractor/scripts/validate_design_system_yaml.py --help
```

Validate a generated extraction:

```bash
python3 skills/visual-design-system-extractor/scripts/validate_design_system_yaml.py path/to/extraction.yaml
```

When `uv` is available, the same extraction validator can be run through the local environment:

```bash
uv run --with-requirements skills/visual-design-system-extractor/requirements.txt python skills/visual-design-system-extractor/scripts/validate_design_system_yaml.py path/to/extraction.yaml
```

The same checks run in GitHub Actions for pushes and pull requests.

## Requirements

- Python 3.9 or newer.
- PyYAML for YAML validation, installed from `skills/visual-design-system-extractor/requirements.txt`, through `uv`, or through an existing Python environment.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

Please keep changes focused on the portable skill package: update `skills/visual-design-system-extractor/SKILL.md` for runbook behavior, `skills/visual-design-system-extractor/references/` for long-form schema or compliance material, and `skills/visual-design-system-extractor/scripts/` for deterministic validation logic.

## Security

Report security concerns using the guidance in [SECURITY.md](SECURITY.md). Do not include secrets, private screenshots, credentials, or proprietary reference material in public issues.

## License

Licensed under the [Apache License, Version 2.0](LICENSE).
