#!/usr/bin/env python3
"""Validate graph.json against canonical claim-relationships.yaml.

Ensures the generated graph projection matches the canonical source.
This is a drift detection gate — if the graph is stale, this fails.

Authority: Search Authority claim-relationships.yaml is canonical.
graph.json is a projection and must match.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml


def resolve_sa_path() -> Path:
    import os
    return Path(os.environ.get(
        "SEARCH_AUTHORITY_PATH",
        str(Path.home() / "Developer" / "_control" / "search-authority")
    ))


def resolve_graph_path() -> Path:
    return Path.home() / "Developer" / "_control" / "moses-integration" / "framework" / "exports" / "graph.json"


def load_yaml(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f) or {}


def load_json(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def validate() -> list[str]:
    """Run all validation checks. Returns list of errors (empty = pass)."""
    errors = []

    sa_path = resolve_sa_path()
    graph_path = resolve_graph_path()

    # Check files exist
    rel_path = sa_path / "canonical" / "claim-relationships.yaml"
    if not rel_path.exists():
        errors.append(f"Canonical relationships file not found: {rel_path}")
        return errors
    if not graph_path.exists():
        errors.append(f"Generated graph not found: {graph_path} — run generate_graph.py")
        return errors

    canonical = load_yaml(rel_path)
    graph = load_json(graph_path)

    canonical_rels = canonical.get("claim_relationships", [])
    graph_edges = graph.get("edges", [])

    # Check edge count matches
    if len(canonical_rels) != len(graph_edges):
        errors.append(
            f"Edge count mismatch: canonical has {len(canonical_rels)}, "
            f"graph has {len(graph_edges)} — regenerate graph.json"
        )

    # Check all canonical edges are in graph
    canonical_edge_set = set()
    for rel in canonical_rels:
        key = (rel["from"], rel["to"], rel["type"])
        canonical_edge_set.add(key)

    graph_edge_set = set()
    for edge in graph_edges:
        key = (edge["from"], edge["to"], edge["type"])
        graph_edge_set.add(key)

    missing = canonical_edge_set - graph_edge_set
    if missing:
        errors.append(f"Missing edges in graph: {missing}")

    extra = graph_edge_set - canonical_edge_set
    if extra:
        errors.append(f"Extra edges in graph (stale?): {extra}")

    # Check node count
    canonical_nodes = set()
    for rel in canonical_rels:
        canonical_nodes.add(rel["from"])
        canonical_nodes.add(rel["to"])

    graph_nodes = {n["id"] for n in graph.get("nodes", [])}

    missing_nodes = canonical_nodes - graph_nodes
    if missing_nodes:
        errors.append(f"Missing nodes in graph: {missing_nodes}")

    # Check no graph edge references a missing node
    for edge in graph_edges:
        if edge["from"] not in graph_nodes:
            errors.append(f"Edge references missing node: {edge['from']}")
        if edge["to"] not in graph_nodes:
            errors.append(f"Edge references missing node: {edge['to']}")

    return errors


def main():
    errors = validate()
    if errors:
        print("FAIL: graph.json drift detected")
        for e in errors:
            print(f"  - {e}")
        print()
        print("Fix: run python3 framework/exports/generate_graph.py in moses-integration")
        sys.exit(1)
    else:
        print("PASS: graph.json matches canonical relationships")
        sys.exit(0)


if __name__ == "__main__":
    main()
