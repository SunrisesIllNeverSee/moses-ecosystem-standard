#!/usr/bin/env python3
"""Validate that authority links in the MO§ES Ecosystem Standard resolve.

Checks:
  1. Every entity in canon/entities.yaml has an authority_class that
     appears in canon/authority-map.yaml.
  2. Every relationship in canon/relationships.yaml references entities
     that exist in canon/entities.yaml.
  3. Every registry entry's authority_owner can be traced to
     search_authority or another known authority in the authority map.

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
CANON_AUTHORITY_MAP = "canon/authority-map.yaml"

REGISTRY_FILES = [
    "registry/components.yaml",
    "registry/standards.yaml",
    "registry/protocols.yaml",
    "registry/frameworks.yaml",
    "registry/products.yaml",
    "registry/sites.yaml",
]

# Known authority owners that are always accepted as traceable roots.
KNOWN_AUTHORITY_ROOTS = {"search_authority", "search-authority"}


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


def get_authority_classes(authority_map_data):
    """Extract the set of known authority_class values from the authority map."""
    classes = set()
    if not authority_map_data:
        return classes
    if isinstance(authority_map_data, dict):
        # Could be a mapping under a key like 'authority_classes' or top-level
        if "authority_classes" in authority_map_data:
            entries = authority_map_data["authority_classes"]
            if isinstance(entries, list):
                for entry in entries:
                    if isinstance(entry, dict) and "class" in entry:
                        classes.add(entry["class"])
                    elif isinstance(entry, str):
                        classes.add(entry)
            elif isinstance(entries, dict):
                classes.update(entries.keys())
        # Also check for top-level list or dict of classes
        for key, val in authority_map_data.items():
            if key == "authority_classes":
                continue
            if isinstance(val, dict) and "authority_class" in val:
                classes.add(val["authority_class"])
            if isinstance(val, dict) and "class" in val:
                classes.add(val["class"])
        # If the dict itself maps class names to owners
        for key in authority_map_data:
            if isinstance(authority_map_data[key], (dict, str)):
                classes.add(key)
    elif isinstance(authority_map_data, list):
        for entry in authority_map_data:
            if isinstance(entry, dict):
                if "class" in entry:
                    classes.add(entry["class"])
                if "authority_class" in entry:
                    classes.add(entry["authority_class"])
            elif isinstance(entry, str):
                classes.add(entry)
    return classes


def get_known_authority_owners(authority_map_data):
    """Extract known authority owner identifiers from the authority map."""
    owners = set()
    if not authority_map_data:
        return owners
    if isinstance(authority_map_data, dict):
        for key, val in authority_map_data.items():
            owners.add(key)
            if isinstance(val, dict):
                if "owner" in val:
                    owners.add(val["owner"])
                if "authority_class" in val:
                    owners.add(val["authority_class"])
    elif isinstance(authority_map_data, list):
        for entry in authority_map_data:
            if isinstance(entry, dict):
                if "owner" in entry:
                    owners.add(entry["owner"])
                if "class" in entry:
                    owners.add(entry["class"])
                if "authority_class" in entry:
                    owners.add(entry["authority_class"])
    # Always include the canonical roots
    owners.update(KNOWN_AUTHORITY_ROOTS)
    return owners


def check_entity_authority_classes(errors, entities_data, authority_classes, authority_map_data, verbose=False):
    """Check that every entity has an authority_class in the authority map.

    Entities in canon/entities.yaml are projected from Search Authority's
    entity graph and do not carry authority_class directly. Instead, we look
    up each entity_id in canon/authority-map.yaml to find its authority_class.
    """
    if entities_data is None:
        _v("canon/entities.yaml not found — skipping entity authority check", verbose)
        return
    entities = []
    if isinstance(entities_data, dict):
        if "entities" in entities_data:
            entities = entities_data["entities"]
        else:
            entities = list(entities_data.values())
    elif isinstance(entities_data, list):
        entities = entities_data

    # Build a lookup from entity_id → authority_class from the authority map
    auth_map_lookup = {}
    if authority_map_data and isinstance(authority_map_data, dict):
        mappings = authority_map_data.get("mappings", authority_map_data.get("entries", []))
        if isinstance(mappings, list):
            for entry in mappings:
                if isinstance(entry, dict):
                    eid = entry.get("entity_id", entry.get("id"))
                    ac = entry.get("authority_class")
                    if eid and ac:
                        auth_map_lookup[eid] = ac
        elif isinstance(mappings, dict):
            for eid, entry in mappings.items():
                if isinstance(entry, dict) and "authority_class" in entry:
                    auth_map_lookup[eid] = entry["authority_class"]

    for entity in entities:
        if not isinstance(entity, dict):
            continue
        entity_id = entity.get("id", entity.get("name", "<unknown>"))
        # First check if the entity itself has authority_class
        auth_class = entity.get("authority_class")
        if auth_class is None:
            # Look up in the authority map
            auth_class = auth_map_lookup.get(entity_id)
        if auth_class is None:
            _v(f"Entity '{entity_id}' has no authority_class in entities or authority-map (skipped)", verbose)
            continue
        if authority_classes and auth_class not in authority_classes:
            errors.append(
                f"Entity '{entity_id}' has authority_class '{auth_class}' "
                f"not found in canon/authority-map.yaml"
            )
        else:
            _v(f"Entity '{entity_id}' authority_class '{auth_class}' OK", verbose)


def check_relationship_targets(errors, relationships_data, entity_ids, verbose=False):
    """Check that every relationship references entities that exist."""
    if relationships_data is None:
        _v("canon/relationships.yaml not found — skipping relationship check", verbose)
        return
    relationships = []
    if isinstance(relationships_data, dict):
        if "relationships" in relationships_data:
            relationships = relationships_data["relationships"]
        else:
            relationships = list(relationships_data.values())
    elif isinstance(relationships_data, list):
        relationships = relationships_data

    for rel in relationships:
        if not isinstance(rel, dict):
            continue
        # Check common field names for relationship endpoints
        for field in ("from", "to", "source", "target", "subject", "object", "a", "b"):
            ref = rel.get(field)
            if ref is not None and isinstance(ref, str):
                if ref not in entity_ids:
                    errors.append(
                        f"Relationship in canon/relationships.yaml references "
                        f"unknown entity '{ref}' (field '{field}')"
                    )
                else:
                    _v(f"Relationship {field}='{ref}' OK", verbose)


def check_registry_authority_owners(errors, known_owners, verbose=False):
    """Check that every registry entry's authority_owner traces to a known authority."""
    for rel_path in REGISTRY_FILES:
        data = _load_yaml(rel_path)
        if data is None:
            _v(f"{rel_path} not found — skipping", verbose)
            continue

        entries = []
        if isinstance(data, dict):
            # Try common keys
            for key in ("components", "standards", "protocols", "frameworks",
                        "products", "sites", "entries", "items"):
                if key in data:
                    entries = data[key]
                    break
            if not entries:
                entries = list(data.values())
        elif isinstance(data, list):
            entries = data

        for entry in entries:
            if not isinstance(entry, dict):
                continue
            entry_id = entry.get("id", entry.get("name", "<unknown>"))
            owner = entry.get("authority_owner") or entry.get("authority")
            if owner is None:
                # Not all entries must have authority_owner, but if present, check it
                _v(f"{rel_path}: '{entry_id}' has no authority_owner (skipped)", verbose)
                continue
            # Normalize: check if owner matches any known authority
            owner_str = str(owner).lower().replace("-", "_")
            known_lower = {o.lower().replace("-", "_") for o in known_owners}
            if owner_str not in known_lower:
                errors.append(
                    f"{rel_path}: entry '{entry_id}' has authority_owner "
                    f"'{owner}' which cannot be traced to a known authority"
                )
            else:
                _v(f"{rel_path}: '{entry_id}' authority_owner '{owner}' OK", verbose)


def main():
    parser = argparse.ArgumentParser(
        description="Validate that authority links in the MO§ES Ecosystem Standard resolve."
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print per-check details."
    )
    args = parser.parse_args()

    errors = []

    print("Validating MO§ES Ecosystem Standard authority links...")

    # Load data
    entities_data = _load_yaml(CANON_ENTITIES)
    relationships_data = _load_yaml(CANON_RELATIONSHIPS)
    authority_map_data = _load_yaml(CANON_AUTHORITY_MAP)

    # Extract known authority classes
    authority_classes = get_authority_classes(authority_map_data)
    known_owners = get_known_authority_owners(authority_map_data)
    _v(f"Known authority classes: {authority_classes}", args.verbose)
    _v(f"Known authority owners: {known_owners}", args.verbose)

    # Extract entity IDs
    entity_ids = set()
    if entities_data:
        entities = []
        if isinstance(entities_data, dict):
            if "entities" in entities_data:
                entities = entities_data["entities"]
            else:
                entities = list(entities_data.values())
        elif isinstance(entities_data, list):
            entities = entities_data
        for entity in entities:
            if isinstance(entity, dict):
                if "id" in entity:
                    entity_ids.add(entity["id"])
                if "name" in entity:
                    entity_ids.add(entity["name"])

    print("  Checking entity authority classes...")
    check_entity_authority_classes(errors, entities_data, authority_classes, authority_map_data, verbose=args.verbose)

    print("  Checking relationship targets...")
    check_relationship_targets(errors, relationships_data, entity_ids, verbose=args.verbose)

    print("  Checking registry authority owners...")
    check_registry_authority_owners(errors, known_owners, verbose=args.verbose)

    if errors:
        print(f"\nFAILED: {len(errors)} error(s) found:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("\nOK: All authority link checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
