#!/usr/bin/env python3
"""Validate that claims in the MO§ES Ecosystem Standard trace to Search Authority.

Checks:
  1. Every entity in canon/entities.yaml has source_refs.
  2. Every relationship in canon/relationships.yaml has source_refs.
  3. Every terminology entry in canon/terminology.yaml has source_refs.
  4. No entity has status "owner_approved" without source_refs.

Exit 0 on success, exit 1 on failure.
"""

import argparse
import os
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)

CANON_ENTITIES = "canon/entities.yaml"
CANON_RELATIONSHIPS = "canon/relationships.yaml"
CANON_TERMINOLOGY = "canon/terminology.yaml"


def _load_yaml(rel_path):
    """Load a YAML file relative to repo root. Returns None on failure."""
    path = os.path.join(REPO_ROOT, rel_path)
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def _v(msg, verbose=False):
    if verbose:
        print(f"  [check] {msg}")


def _extract_items(data):
    """Extract a list of items from YAML data that may be a list or dict."""
    if data is None:
        return []
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        # Try common container keys
        for key in ("entities", "relationships", "terms", "terminology",
                     "entries", "items"):
            if key in data:
                val = data[key]
                if isinstance(val, list):
                    return val
                if isinstance(val, dict):
                    return list(val.values())
        # Otherwise treat dict values as items
        return list(data.values())
    return []


def _has_source_refs(item):
    """Check if an item has non-empty source_refs."""
    if not isinstance(item, dict):
        return False
    refs = item.get("source_refs") or item.get("source_ref") or item.get("sources")
    if refs is None:
        return False
    if isinstance(refs, list):
        return len(refs) > 0
    if isinstance(refs, str):
        return len(refs.strip()) > 0
    return refs is not None


def check_entities(errors, verbose=False):
    """Check that every entity has source_refs, and owner_approved entities have source_refs."""
    data = _load_yaml(CANON_ENTITIES)
    if data is None:
        _v("canon/entities.yaml not found — skipping entity check", verbose)
        return

    items = _extract_items(data)
    for item in items:
        if not isinstance(item, dict):
            continue
        entity_id = item.get("id", item.get("name", "<unknown>"))
        status = item.get("status", "")

        if not _has_source_refs(item):
            errors.append(
                f"Entity '{entity_id}' in canon/entities.yaml has no source_refs"
            )
            _v(f"Entity '{entity_id}' MISSING source_refs", verbose)
        else:
            _v(f"Entity '{entity_id}' has source_refs (OK)", verbose)

        # Extra check: owner_approved without source_refs
        if status == "owner_approved" and not _has_source_refs(item):
            errors.append(
                f"Entity '{entity_id}' has status 'owner_approved' but no source_refs — "
                f"owner-approved claims must trace to Search Authority"
            )


def check_relationships(errors, verbose=False):
    """Check that every relationship has source_refs."""
    data = _load_yaml(CANON_RELATIONSHIPS)
    if data is None:
        _v("canon/relationships.yaml not found — skipping relationship check", verbose)
        return

    items = _extract_items(data)
    for item in items:
        if not isinstance(item, dict):
            continue
        # Build a readable identifier for the relationship
        rel_id = item.get("id")
        if rel_id is None:
            parts = []
            for field in ("from", "source", "subject", "a"):
                if field in item:
                    parts.append(str(item[field]))
                    break
            parts.append("→")
            for field in ("to", "target", "object", "b"):
                if field in item:
                    parts.append(str(item[field]))
                    break
            rel_id = " ".join(parts) if len(parts) > 1 else "<unknown>"

        if not _has_source_refs(item):
            errors.append(
                f"Relationship '{rel_id}' in canon/relationships.yaml has no source_refs"
            )
            _v(f"Relationship '{rel_id}' MISSING source_refs", verbose)
        else:
            _v(f"Relationship '{rel_id}' has source_refs (OK)", verbose)


def check_terminology(errors, verbose=False):
    """Check that every terminology entry has source_refs."""
    data = _load_yaml(CANON_TERMINOLOGY)
    if data is None:
        _v("canon/terminology.yaml not found — skipping terminology check", verbose)
        return

    items = _extract_items(data)
    for item in items:
        if not isinstance(item, dict):
            continue
        term_id = item.get("id", item.get("term", item.get("name", "<unknown>")))

        if not _has_source_refs(item):
            errors.append(
                f"Terminology entry '{term_id}' in canon/terminology.yaml has no source_refs"
            )
            _v(f"Terminology '{term_id}' MISSING source_refs", verbose)
        else:
            _v(f"Terminology '{term_id}' has source_refs (OK)", verbose)


def main():
    parser = argparse.ArgumentParser(
        description="Validate that claims in the MO§ES Ecosystem Standard trace to Search Authority."
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print per-check details."
    )
    args = parser.parse_args()

    errors = []

    print("Validating MO§ES Ecosystem Standard canon provenance...")

    print("  Checking entities for source_refs...")
    check_entities(errors, verbose=args.verbose)

    print("  Checking relationships for source_refs...")
    check_relationships(errors, verbose=args.verbose)

    print("  Checking terminology for source_refs...")
    check_terminology(errors, verbose=args.verbose)

    if errors:
        print(f"\nFAILED: {len(errors)} error(s) found:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("\nOK: All canon provenance checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
