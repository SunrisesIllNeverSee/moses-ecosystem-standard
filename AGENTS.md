# MO§ES Ecosystem Standard — Agent Rules

## What this repo is

This is the **canonical public architecture and reference standard** for the
entire MO§ES ecosystem. It is a governed public projection of the Search
Authority master canon.

It is a **canonical information package**, not a product monorepo. It
contains references to ecosystem components, not copies of them.

It answers: **What is the MO§ES ecosystem, what components belong to it,
what roles do they have, how do they relate, and which authority governs
each type of information?**

It does **not** answer: what is true (Search Authority), what are the
framework's claims (MO§ES Framework), what are the protocol semantics
(TTEOP), or how products are implemented (each product repo).

## Authority

- **Search Authority** is the canonical internal authority. This standard
  is a governed public projection of that canon.
- This standard **does not independently invent canonical truth**. Every
  claim traces to Search Authority.
- Disputed claims in Search Authority remain disputed here — this standard
  does not resolve them.

## Information sources

```
                    SEARCH AUTHORITY
                 approved canonical truth
                         │
                         ▼
               MO§ES ECOSYSTEM STANDARD
                public canonical overview
                   ▲        ▲        ▲
                   │        │        │
             formal refs   specs   implementation identity
                   │        │        │
         MO§ES Framework  TTEOP   Ello Control
```

- **Search Authority** supplies: canonical names, approved descriptions,
  canonical relationships, approved public claims, terminology, entity
  identity, authority assignments.
- **MO§ES Framework** supplies: formal framework references, claim IDs,
  ontology concepts, framework version, formal status. The standard
  references those; it does not absorb ownership of them.
- **TTEOP** supplies: protocol identity, protocol version, protocol role,
  canonical protocol URL. The standard says "TTEOP is the measurement
  protocol used here." It does not copy the metric specification.
- **Ello Control** supplies: repo_id, current repo/location, lifecycle,
  implementation relationship, deployment mapping. This is operational
  identity, not canonical truth.

## Governance rules (from Search Authority)

- Exactly ONE MO§ES entity. Never duplicate it.
- Canonical display: MO§ES™. Accepted prose: MO§ES. Aliases: mos2es, MOSES.
- Never render: MO§E§ or MO§E§™.
- Do NOT collapse Signomy and CIVITAE.
- Archetype = shape. Class = scale/qualification. Rank = field position.
- SigRank evaluates AI operators, not AI models.
- The harness may measure authority, but it cannot manufacture authority.
- Automated systems may not promote claims into owner-approved truth.

## Before modifying authority-sensitive material

Before modifying any of the following, load the relevant canon context:

- ecosystem relationships
- entity definitions
- terminology
- authority architecture
- product boundaries

Load context with:

```bash
export SEARCH_AUTHORITY_PATH="${SEARCH_AUTHORITY_PATH:-$HOME/Developer/_control/search-authority}"
python3 "$SEARCH_AUTHORITY_PATH/canon_cli.py" context ecosystem
python3 "$SEARCH_AUTHORITY_PATH/canon_cli.py" context moses
python3 "$SEARCH_AUTHORITY_PATH/canon_cli.py" context sigrank
```

If the canon repository is unavailable, **do not invent canonical context** —
ask the owner.

## What is NOT authority-sensitive

- YAML formatting fixes
- Typo corrections
- README updates that don't change canonical claims
- Test infrastructure

## Validation

```bash
python3 validation/validate-standard.py
python3 validation/validate-authority-links.py
python3 validation/validate-canon-provenance.py
```

## Git behavior

- Prefer small, intentional commits.
- Do not force-push the default branch.
- This is a public repo — be conservative about what goes in.

## Repository structure

```
README.md              — overview
STANDARD.md            — the standard (20 sections)
VERSION.yaml           — version metadata
CHANGELOG.md           — change history
LICENSE                — CC BY 4.0
AGENTS.md              — this file
canon/                 — structured canonical information
architecture/          — human-readable architecture documents
registry/              — machine-readable registries (references, not copies)
references/            — references to external authorities
machine/               — machine-readable standard metadata
validation/            — validation scripts
docs/                  — documentation
```


## Filesystem MCP — REQUIRED for file operations

This is a core framework/search/ello/product repository. When performing
file operations, prefer the Filesystem MCP tools over ad-hoc shell commands:

- `list_directory` / `directory_tree` — structured directory traversal
- `search_files` — glob-pattern file search within allowed paths
- `read_multiple_files` — batch file reads (failures do not stop the batch)
- `edit_file` with `dryRun: true` — preview structural changes before applying

Allowed paths: ~/Developer, ~/.config/devin, ~/.config/sigrank, ~/Desktop

For single-file reads and edits, native tools are acceptable. For multi-file
operations, directory exploration, and structural changes, use the Filesystem MCP.
