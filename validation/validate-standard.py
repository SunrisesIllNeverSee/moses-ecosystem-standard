#!/usr/bin/env python3
"""Validate the MO§ES Ecosystem Standard's internal consistency.

Checks:
  1. VERSION.yaml parses as valid YAML.
  2. STANDARD.md has exactly 20 numbered sections.
  3. All registry YAML files parse.
  4. All reference YAML files parse.
  5. All canon YAML files parse.
  6. machine/standard.yaml and machine/standard.json agree on version.

Exit 0 on success, exit 1 on failure.
"""

import argparse
import json
import os
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(1)

# Resolve repo root relative to this script.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)

EXPECTED_SECTION_COUNT = 20

REGISTRY_FILES = [
    "registry/components.yaml",
    "registry/standards.yaml",
    "registry/protocols.yaml",
    "registry/frameworks.yaml",
    "registry/products.yaml",
    "registry/sites.yaml",
]

REFERENCE_FILES = [
    "references/search-authority.yaml",
    "references/moses-framework.yaml",
    "references/tteop.yaml",
    "references/sigrank-ecosystem-standard.yaml",
    "references/external-sources.yaml",
]

CANON_FILES = [
    "canon/ecosystem.yaml",
    "canon/entities.yaml",
    "canon/relationships.yaml",
    "canon/terminology.yaml",
    "canon/authority-map.yaml",
    "canon/sources.yaml",
]


def _v(msg, verbose=False):
    """Print a message only if --verbose is set."""
    if verbose:
        print(f"  [check] {msg}")


def check_version_yaml(errors, verbose=False):
    """Check that VERSION.yaml parses."""
    path = os.path.join(REPO_ROOT, "VERSION.yaml")
    if not os.path.exists(path):
        errors.append(f"VERSION.yaml not found at {path}")
        return
    try:
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            errors.append("VERSION.yaml did not parse to a dict/mapping")
            return
        _v(f"VERSION.yaml parsed OK: version={data.get('version')}", verbose)
    except yaml.YAMLError as e:
        errors.append(f"VERSION.yaml failed to parse: {e}")
    except Exception as e:
        errors.append(f"VERSION.yaml could not be read: {e}")


def check_standard_sections(errors, verbose=False):
    """Check that STANDARD.md has exactly 20 numbered sections."""
    path = os.path.join(REPO_ROOT, "STANDARD.md")
    if not os.path.exists(path):
        errors.append(f"STANDARD.md not found at {path}")
        return
    try:
        with open(path, "r") as f:
            content = f.read()
    except Exception as e:
        errors.append(f"STANDARD.md could not be read: {e}")
        return

    import re
    # Match lines like "## 1. Purpose and Scope" through "## 20. Change History"
    section_pattern = re.compile(r"^## \d+\. ", re.MULTILINE)
    matches = section_pattern.findall(content)
    count = len(matches)
    if count != EXPECTED_SECTION_COUNT:
        errors.append(
            f"STANDARD.md has {count} numbered sections, "
            f"expected {EXPECTED_SECTION_COUNT}"
        )
    else:
        _v(f"STANDARD.md has {count} sections (OK)", verbose)


def check_yaml_files(file_list, label, errors, verbose=False):
    """Check that a list of YAML files all parse."""
    for rel_path in file_list:
        path = os.path.join(REPO_ROOT, rel_path)
        if not os.path.exists(path):
            errors.append(f"{label} file not found: {rel_path}")
            continue
        try:
            with open(path, "r") as f:
                yaml.safe_load(f)
            _v(f"{rel_path} parsed OK", verbose)
        except yaml.YAMLError as e:
            errors.append(f"{rel_path} failed to parse: {e}")
        except Exception as e:
            errors.append(f"{rel_path} could not be read: {e}")


def check_machine_version_agreement(errors, verbose=False):
    """Check that machine/standard.yaml and machine/standard.json agree on version."""
    yaml_path = os.path.join(REPO_ROOT, "machine", "standard.yaml")
    json_path = os.path.join(REPO_ROOT, "machine", "standard.json")

    yaml_version = None
    json_version = None

    if os.path.exists(yaml_path):
        try:
            with open(yaml_path, "r") as f:
                yaml_data = yaml.safe_load(f)
            yaml_version = yaml_data.get("version") if isinstance(yaml_data, dict) else None
        except Exception as e:
            errors.append(f"machine/standard.yaml could not be parsed: {e}")
    else:
        errors.append("machine/standard.yaml not found")

    if os.path.exists(json_path):
        try:
            with open(json_path, "r") as f:
                json_data = json.load(f)
            json_version = json_data.get("version")
        except Exception as e:
            errors.append(f"machine/standard.json could not be parsed: {e}")
    else:
        errors.append("machine/standard.json not found")

    if yaml_version and json_version:
        if yaml_version != json_version:
            errors.append(
                f"Version mismatch: standard.yaml has '{yaml_version}', "
                f"standard.json has '{json_version}'"
            )
        else:
            _v(f"Version agreement OK: {yaml_version}", verbose)


def main():
    parser = argparse.ArgumentParser(
        description="Validate the MO§ES Ecosystem Standard's internal consistency."
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print per-check details."
    )
    args = parser.parse_args()

    errors = []

    print("Validating MO§ES Ecosystem Standard internal consistency...")

    print("  Checking VERSION.yaml...")
    check_version_yaml(errors, verbose=args.verbose)

    print("  Checking STANDARD.md sections...")
    check_standard_sections(errors, verbose=args.verbose)

    print("  Checking registry YAML files...")
    check_yaml_files(REGISTRY_FILES, "registry", errors, verbose=args.verbose)

    print("  Checking reference YAML files...")
    check_yaml_files(REFERENCE_FILES, "reference", errors, verbose=args.verbose)

    print("  Checking canon YAML files...")
    check_yaml_files(CANON_FILES, "canon", errors, verbose=args.verbose)

    print("  Checking machine/ version agreement...")
    check_machine_version_agreement(errors, verbose=args.verbose)

    if errors:
        print(f"\nFAILED: {len(errors)} error(s) found:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("\nOK: All internal consistency checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
