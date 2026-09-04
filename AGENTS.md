# MO§ES Ecosystem Standard — Agent Rules

## What this repo is

This is the **canonical public architecture and reference standard** for the
entire MO§ES ecosystem. It is a governed public projection of the Search
Authority master canon.

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
# Validate the component registry YAML parses
python3 -c "import yaml; yaml.safe_load(open('registry/components.yaml'))"

# Validate the SPEC.md sections are present
python3 -c "
import re
with open('SPEC.md') as f:
    content = f.read()
sections = re.findall(r'^## (\d+\. .+)$', content, re.MULTILINE)
assert len(sections) >= 20, f'Expected 20 sections, found {len(sections)}'
print(f'OK: {len(sections)} sections found')
"
```

## Git behavior

- Prefer small, intentional commits.
- Do not force-push the default branch.
- This is a public repo — be conservative about what goes in.

## Files

```
README.md              — overview and quick reference
SPEC.md                — the standard (20 sections)
LICENSE                — CC BY 4.0
AGENTS.md              — this file
registry/
  components.yaml      — machine-readable component registry
```
