#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "PyYAML>=6.0,<7",
# ]
# ///
"""Validate visual design system extraction YAML."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyYAML is required. Run with `uv run scripts/validate_design_system_yaml.py ...` "
        "or install PyYAML for your Python environment."
    ) from exc


REQUIRED_TOP_LEVEL = [
    "meta",
    "source_analysis",
    "confidence_scores",
    "design_principles",
    "brand_identity",
    "character_identity",
    "art_direction",
    "visual_language",
    "color_system",
    "typography",
    "spacing",
    "layout",
    "grid_system",
    "sizing",
    "borders",
    "radii",
    "shadows",
    "gradients",
    "materials",
    "textures",
    "lighting",
    "motion",
    "animation",
    "camera",
    "composition",
    "environment",
    "setting",
    "wardrobe",
    "props",
    "iconography",
    "illustration_style",
    "photography_style",
    "cinematic_style",
    "rendering_style",
    "surface_treatment",
    "accessibility",
    "interaction_design",
    "ui_patterns",
    "sound_design",
    "narrative_tone",
    "emotional_palette",
    "worldbuilding",
    "styling_rules",
    "dos_and_donts",
    "token_dependencies",
    "dynamic_tokens",
    "responsive_rules",
    "state_variants",
    "platform_adaptations",
    "ai_generation_prompts",
    "implementation_notes",
]

COMMON_UI_FAMILIES = {
    "arial",
    "avenir",
    "helvetica",
    "inter",
    "lato",
    "montserrat",
    "open sans",
    "poppins",
    "roboto",
    "sf pro",
    "system-ui",
}

CONFIDENCE_VALUES = {"low", "medium", "high"}


class UniqueKeySafeLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def construct_mapping_without_duplicates(
    loader: UniqueKeySafeLoader,
    node: yaml.nodes.MappingNode,
    deep: bool = False,
) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            mark = key_node.start_mark
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeySafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_mapping_without_duplicates,
)


def load_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def count_key(node: Any, target: str) -> int:
    if isinstance(node, dict):
        return sum(1 for key in node if key == target) + sum(
            count_key(value, target) for value in node.values()
        )
    if isinstance(node, list):
        return sum(count_key(item, target) for item in node)
    return 0


def path_join(parent: str, key: str) -> str:
    return f"{parent}.{key}" if parent else key


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_recursive_shapes(node: Any, path: str, errors: list[str]) -> None:
    if isinstance(node, dict):
        if "confidence" in node and node["confidence"] not in CONFIDENCE_VALUES:
            errors.append(
                f"{path_join(path, 'confidence')} must be one of: "
                + ", ".join(sorted(CONFIDENCE_VALUES))
                + "."
            )

        if node.get("applicability") == "not_applicable":
            if node.get("confidence") not in CONFIDENCE_VALUES:
                errors.append(
                    f"{path or 'root'} not-applicable object must include confidence "
                    "as low, medium, or high."
                )
            if not is_non_empty_string(node.get("inference_basis")):
                errors.append(
                    f"{path or 'root'} not-applicable object must include a non-empty "
                    "inference_basis."
                )

        for key, value in node.items():
            validate_recursive_shapes(value, path_join(path, str(key)), errors)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            validate_recursive_shapes(item, f"{path}[{index}]", errors)


def validate(data: Any, text: str, min_confidence_markers: int) -> list[str]:
    errors: list[str] = []
    stripped = text.strip()

    if "```" in text:
        errors.append("Output contains markdown code fences; return raw YAML only.")

    if "\t" in text:
        errors.append("Output contains tab characters; use spaces for YAML indentation.")

    if data is None:
        errors.append("YAML document is empty.")
        return errors

    if not isinstance(data, dict):
        errors.append("YAML root must be a mapping/object.")
        return errors

    missing = [key for key in REQUIRED_TOP_LEVEL if key not in data]
    if missing:
        errors.append("Missing required top-level sections: " + ", ".join(missing))

    extras = [key for key in data if key not in REQUIRED_TOP_LEVEL]
    if extras:
        errors.append("Unexpected top-level sections: " + ", ".join(map(str, extras)))

    present_required = [key for key in data if key in REQUIRED_TOP_LEVEL]
    expected_present = [key for key in REQUIRED_TOP_LEVEL if key in data]
    if present_required != expected_present:
        errors.append(
            "Top-level section order must match the canonical schema order exactly."
        )

    null_sections = [key for key in REQUIRED_TOP_LEVEL if key in data and data[key] is None]
    if null_sections:
        errors.append(
            "Top-level sections must not be bare null placeholders: "
            + ", ".join(null_sections)
        )

    source_analysis = data.get("source_analysis")
    if not isinstance(source_analysis, dict):
        errors.append("source_analysis must be a mapping.")
    else:
        for key in ("observed", "inferred", "speculative"):
            value = source_analysis.get(key)
            if not isinstance(value, list):
                errors.append(f"source_analysis.{key} must be a list.")
        source_inventory = source_analysis.get("source_inventory")
        if not isinstance(source_inventory, dict):
            errors.append("source_analysis.source_inventory must be a mapping.")
        else:
            for key in (
                "images",
                "visible_text",
                "visible_interfaces",
                "visible_people_or_characters",
                "visible_environments",
                "visible_brand_marks",
            ):
                if not isinstance(source_inventory.get(key), list):
                    errors.append(f"source_analysis.source_inventory.{key} must be a list.")
        evidence_boundaries = source_analysis.get("evidence_boundaries")
        if not isinstance(evidence_boundaries, dict):
            errors.append("source_analysis.evidence_boundaries must be a mapping.")
        else:
            for key in (
                "directly_observed",
                "inferred_from_visual_cues",
                "low_confidence_extrapolations",
            ):
                if not isinstance(evidence_boundaries.get(key), list):
                    errors.append(f"source_analysis.evidence_boundaries.{key} must be a list.")

    confidence_scores = data.get("confidence_scores")
    if not isinstance(confidence_scores, dict) or not confidence_scores:
        errors.append("confidence_scores must be a non-empty mapping.")

    typography = data.get("typography")
    if not isinstance(typography, dict):
        errors.append("typography must be a mapping.")
    else:
        font_families = typography.get("font_families")
        if not isinstance(font_families, dict):
            errors.append("typography.font_families must be a mapping.")
        else:
            rare_candidates = font_families.get("rare_unique_candidates")
            if not isinstance(rare_candidates, list) or not rare_candidates:
                errors.append(
                    "typography.font_families.rare_unique_candidates must be a non-empty list."
                )
            else:
                required_candidate_fields = [
                    "family",
                    "role",
                    "classification",
                    "fallback_stack",
                    "pairs_well_with",
                    "visual_grounding",
                    "rarity_reason",
                    "pairing_logic",
                    "use_constraints",
                    "confidence",
                    "inference_basis",
                ]
                for index, candidate in enumerate(rare_candidates):
                    if not isinstance(candidate, dict):
                        errors.append(
                            "typography.font_families.rare_unique_candidates"
                            f"[{index}] must be a mapping."
                        )
                        continue
                    for field in required_candidate_fields:
                        if field not in candidate:
                            errors.append(
                                "typography.font_families.rare_unique_candidates"
                                f"[{index}] missing required field: {field}"
                            )
                    for field in (
                        "family",
                        "role",
                        "classification",
                        "visual_grounding",
                        "rarity_reason",
                        "pairing_logic",
                        "use_constraints",
                        "confidence",
                        "inference_basis",
                    ):
                        if field in candidate and not is_non_empty_string(candidate[field]):
                            errors.append(
                                "typography.font_families.rare_unique_candidates"
                                f"[{index}].{field} must be a non-empty string."
                            )
                    if (
                        "confidence" in candidate
                        and candidate["confidence"] not in CONFIDENCE_VALUES
                    ):
                        errors.append(
                            "typography.font_families.rare_unique_candidates"
                            f"[{index}].confidence must be one of: "
                            + ", ".join(sorted(CONFIDENCE_VALUES))
                            + "."
                        )
                    family = candidate.get("family")
                    if (
                        is_non_empty_string(family)
                        and family.strip().lower() in COMMON_UI_FAMILIES
                    ):
                        errors.append(
                            "typography.font_families.rare_unique_candidates"
                            f"[{index}].family must be rare or distinctive, not a common UI default."
                        )
                    for field in ("fallback_stack", "pairs_well_with"):
                        if field in candidate and (
                            not isinstance(candidate[field], list)
                            or not candidate[field]
                            or not all(is_non_empty_string(item) for item in candidate[field])
                        ):
                            errors.append(
                                "typography.font_families.rare_unique_candidates"
                                f"[{index}].{field} must be a non-empty list of strings."
                            )

    confidence_count = count_key(data, "confidence")
    if confidence_count < min_confidence_markers:
        errors.append(
            f"Expected at least {min_confidence_markers} confidence markers; "
            f"found {confidence_count}."
        )

    validate_recursive_shapes(data, "", errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate production-grade visual design system extraction YAML.",
    )
    parser.add_argument("input", help="YAML file to validate, or '-' for stdin.")
    parser.add_argument(
        "--min-confidence-markers",
        type=int,
        default=5,
        help="Minimum recursive count of `confidence` keys. Default: 5.",
    )
    args = parser.parse_args()

    text = load_text(args.input)
    try:
        data = yaml.load(text, Loader=UniqueKeySafeLoader)
    except (yaml.YAMLError, yaml.constructor.ConstructorError) as exc:
        print(f"Invalid YAML: {exc}", file=sys.stderr)
        return 1

    errors = validate(data, text, args.min_confidence_markers)
    result = {
        "valid": not errors,
        "errors": errors,
        "required_sections": len(REQUIRED_TOP_LEVEL),
        "confidence_markers": count_key(data, "confidence") if isinstance(data, dict) else 0,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
