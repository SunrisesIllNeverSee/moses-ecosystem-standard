# Publication Rules

Rules for publishing and updating the MO§ES Ecosystem Standard.

---

## Version policy

### Version string

This standard uses the version string `moses-ecosystem/0.1-draft`.
See `VERSION.yaml` for the current version metadata.

### Version categories

| Category | Meaning | Stability |
|----------|---------|-----------|
| **Draft** | Work in progress. Not frozen. | May change without notice. |
| **Minor** | Additive changes (new components, new relationships). | Backward-compatible. |
| **Major** | Breaking changes to ecosystem architecture or authority structure. | Not backward-compatible. |
| **Frozen** | Tagged release. Receives a DOI. | Will not change; only superseded. |

### Current status

The current version is **draft**. It is not frozen and may change without
notice. Frozen versions are tagged and receive a DOI.

### Version bump rules

- **Draft → Draft**: No version bump required for incremental work.
- **Draft → Frozen**: Owner approval required. Tag the release. Assign a DOI.
- **Frozen → Minor**: New draft begins at the next minor version.
- **Minor → Major**: Breaking change to architecture or authority structure.
  Requires owner approval.

---

## Change process

### Step 1: Load canon context

Before modifying any authority-sensitive material, load the relevant canon
context from Search Authority:

```bash
export SEARCH_AUTHORITY_PATH="${SEARCH_AUTHORITY_PATH:-$HOME/Developer/_control/search-authority}"
python3 "$SEARCH_AUTHORITY_PATH/canon_cli.py" context ecosystem
python3 "$SEARCH_AUTHORITY_PATH/canon_cli.py" context moses
python3 "$SEARCH_AUTHORITY_PATH/canon_cli.py" context sigrank
```

If the canon repository is unavailable, **do not invent canonical context**.
Ask the owner.

### Step 2: Update canon/ files

Update the structured canonical information as needed:

- `canon/entities.yaml` — entity registry (projected from Search Authority)
- `canon/relationships.yaml` — relationship graph
- `canon/terminology.yaml` — canonical terms
- `canon/authority-map.yaml` — who owns what authority
- `canon/sources.yaml` — source provenance
- `canon/ecosystem.yaml` — ecosystem-level canonical info

Every entity, relationship, and terminology entry must have `source_refs`
tracing to Search Authority.

### Step 3: Update registry/ files

Update the machine-readable registries:

- `registry/components.yaml` — all components (unified view)
- `registry/standards.yaml` — standards
- `registry/protocols.yaml` — protocols
- `registry/frameworks.yaml` — frameworks
- `registry/products.yaml` — products
- `registry/sites.yaml` — public sites

Every registry entry's `authority_owner` must trace to Search Authority
or another known authority.

### Step 4: Update STANDARD.md

Update the human-readable standard document. STANDARD.md must always have
exactly 20 numbered sections.

### Step 5: Run validation

Run all three validation scripts:

```bash
python3 validation/validate-standard.py --verbose
python3 validation/validate-authority-links.py --verbose
python3 validation/validate-canon-provenance.py --verbose
```

All three must exit 0. Fix any errors before proceeding.

### Step 6: Update VERSION.yaml and CHANGELOG.md

- Bump the version in `VERSION.yaml` if appropriate.
- Update `last_updated` date.
- Add a changelog entry to `CHANGELOG.md`.

### Step 7: Commit

Prefer small, intentional commits. Do not force-push the default branch.
This is a public repo — be conservative about what goes in.

---

## What requires owner approval

The following changes require explicit owner approval before they may be
committed:

### Entity identity

Any change to how an entity is defined, named, or identified:
- Adding a new entity
- Removing an entity
- Changing an entity's canonical name or aliases
- Changing an entity's authority_class

### Relationships

Any change to how entities relate:
- Adding a new relationship
- Removing a relationship
- Changing the type or direction of a relationship

### Terminology

Any change to canonical terms:
- Adding a new canonical term
- Removing a term
- Changing a term's definition or status
- Promoting a term to `owner_approved` status

### Authority assignments

Any change to who owns what authority:
- Adding or removing an authority class
- Changing which entity owns an authority class
- Changing the authority chain

### Why owner approval is required

These changes affect canonical truth. Search Authority is the sole master
canon owner. Automated systems may not promote claims into owner-approved
truth. The harness may measure authority, but it cannot manufacture
authority.

---

## What does NOT require owner approval

The following changes do not require owner approval:

- **Formatting fixes** — YAML formatting, whitespace, line wrapping
- **Typo corrections** — spelling and grammar fixes that do not change
  canonical claims
- **README updates** — documentation that does not change canonical claims
- **Adding references to new repos** — adding a pointer to a newly created
  repository that already has an approved entity identity
- **Test infrastructure** — validation scripts, CI configuration
- **Machine-readable metadata** — keeping `machine/standard.yaml`,
  `machine/standard.json`, and `machine/standard.jsonld` in sync with
  `VERSION.yaml`

### Governance rules still apply

Even for non-authority-sensitive changes, the governance rules from Search
Authority must be observed:

- Exactly ONE MO§ES entity. Never duplicate it.
- Canonical display: MO§ES™. Accepted prose: MO§ES. Aliases: mos2es, MOSES.
- Never render: MO§E§ or MO§E§™.
- Do NOT collapse Signomy and CIVITAE.
- SigRank evaluates AI operators, not AI models.

---

## DOI assignment for frozen versions

### When to assign a DOI

A DOI is assigned when a version is **frozen** — tagged as a release and
declared stable. Draft versions do not receive DOIs.

### How to assign a DOI

1. **Owner approves** the freeze.
2. **Tag the release** in git (e.g., `v0.1.0`).
3. **Assign a DOI** via Zenodo (or the owner's chosen DOI provider).
4. **Update `VERSION.yaml`** with the DOI.
5. **Update `machine/standard.yaml`, `machine/standard.json`, and
   `machine/standard.jsonld`** with the DOI.
6. **Update `references/external-sources.yaml`** with the new DOI entry.
7. **Update `CHANGELOG.md`** noting the freeze and DOI.
8. **Run validation** to confirm consistency.
9. **Commit and push** the tag.

### DOI persistence

Once assigned, a DOI is permanent. Frozen versions do not change. A new
frozen version receives a new DOI. The concept DOI (if assigned) groups
all version DOIs for the standard.

### Existing DOIs in the ecosystem

| Entity | DOI | Type |
|--------|-----|------|
| TTEOP version | 10.5281/zenodo.22180349 | Version DOI |
| TTEOP concept | 10.5281/zenodo.22180348 | Concept DOI |
| Conservation Law paper | 10.5281/zenodo.20029607 | Paper DOI |
| Commitment Theory V.1 | 10.5281/zenodo.20031715 | Version DOI |
| Commitment Theory V2 | 10.5281/zenodo.21069704 | Version DOI |

See [references/external-sources.yaml](../references/external-sources.yaml)
for the complete list of DOIs, patents, and trademarks.
