# Implementation Guide

How to use the MO§ES Ecosystem Standard in practice.

---

## Who should read this

This guide is for:

- **Product maintainers** building components within the MO§ES ecosystem
  (SignalAF, SigRank, Upsilon, Signomy, CIVITAE, etc.)
- **Tool authors** creating MCP servers, VS Code extensions, or agents
  that interact with MO§ES components
- **Researchers** working with Commitment Theory, the Conservation Law,
  or SigRank evaluation methodology
- **Integrators** connecting external systems to the MO§ES ecosystem
- **Contributors** to this standard itself

If you are building anything that references MO§ES, SigRank, TTEOP, or
related components, this guide explains how to do it correctly.

---

## How to reference this standard from a product

Every MO§ES ecosystem component should be able to answer:

```
What am I?
What family am I part of?
What is my role?
What standard/framework/protocol governs me?
Where is the canonical ecosystem reference?
What Search Authority-backed identity does this resolve to?
```

### Referencing the standard

Link to the canonical repository and version:

```
Standard: MO§ES Ecosystem Standard
Version:  moses-ecosystem/0.1-draft
URL:      https://github.com/SunrisesIllNeverSee/moses-ecosystem-standard
```

### Referencing the machine-readable metadata

Use the files in `machine/` for programmatic access:

- `machine/standard.yaml` — YAML representation
- `machine/standard.json` — JSON representation
- `machine/standard.jsonld` — JSON-LD (schema.org) representation

### Referencing component registries

Use the files in `registry/` to discover ecosystem components:

- `registry/components.yaml` — all components (unified view)
- `registry/standards.yaml` — standards
- `registry/protocols.yaml` — protocols
- `registry/frameworks.yaml` — frameworks
- `registry/products.yaml` — products
- `registry/sites.yaml` — public sites

These are **references to** components, not copies of them. They contain
pointers and metadata, not source code or protocol specifications.

---

## How to load Search Authority canon context

Before modifying any authority-sensitive material (entity definitions,
relationships, terminology, authority architecture, product boundaries),
load the relevant canon context from Search Authority.

### Prerequisites

Search Authority is a private repository. Set the path:

```bash
export SEARCH_AUTHORITY_PATH="${SEARCH_AUTHORITY_PATH:-$HOME/Developer/_control/search-authority}"
```

### Loading canon contexts

```bash
python3 "$SEARCH_AUTHORITY_PATH/canon_cli.py" context ecosystem
python3 "$SEARCH_AUTHORITY_PATH/canon_cli.py" context moses
python3 "$SEARCH_AUTHORITY_PATH/canon_cli.py" context sigrank
```

Available contexts: `moses`, `sigrank`, `ecosystem`, `commitment_theory`,
`conservation_law`, `kassa`, `signomy`, `civitae`.

### If Search Authority is unavailable

If the canon repository is unavailable, **do not invent canonical context**.
Ask the owner. Automated systems may not promote claims into owner-approved
truth.

---

## How to validate conformance

Run the three validation scripts from the repository root:

```bash
# Internal consistency: VERSION.yaml, STANDARD.md sections, YAML parsing,
# machine/ version agreement
python3 validation/validate-standard.py

# Authority links: entity authority classes, relationship targets,
# registry authority owners
python3 validation/validate-authority-links.py

# Canon provenance: source_refs on entities, relationships, terminology
python3 validation/validate-canon-provenance.py
```

Use `--verbose` for per-check details:

```bash
python3 validation/validate-standard.py --verbose
```

All three scripts exit 0 on success and exit 1 on failure.

### What conformance means

A component conforms to this standard when:

1. It correctly identifies its role in the ecosystem architecture.
2. It traces its canonical claims to Search Authority.
3. If it uses TTEOP, it implements TTEOP through a version-pinned
   implementation profile and does not redefine TTEOP semantics.
4. It uses canonical terminology correctly.
5. It does not present legacy identifiers as current standards.

---

## How to add a new component to the registry

1. **Load the relevant canon context** from Search Authority (see above).
   Do not invent canonical context if Search Authority is unavailable.

2. **Add the component to `registry/components.yaml`** with the following
   minimum fields:
   ```yaml
   - id: component-id
     name: Component Name
     type: product          # framework, standard, protocol, product, platform, etc.
     role: implementation   # authority, implementation, transport, projection, etc.
     authority_class: product_implementation
     authority_owner: search-authority
     source_refs:
       - search-authority:context:record-id
   ```

3. **Add to the type-specific registry** if applicable:
   - Products → `registry/products.yaml`
   - Frameworks → `registry/frameworks.yaml`
   - Standards → `registry/standards.yaml`
   - Protocols → `registry/protocols.yaml`
   - Sites → `registry/sites.yaml`

4. **Update `canon/entities.yaml`** if the component is a new entity.
   Every entity must have `source_refs` tracing to Search Authority.

5. **Update `canon/relationships.yaml`** if the component has new
   relationships with existing entities. Every relationship must have
   `source_refs`.

6. **Update `canon/terminology.yaml`** if the component introduces new
   canonical terms.

7. **Run validation:**
   ```bash
   python3 validation/validate-standard.py
   python3 validation/validate-authority-links.py
   python3 validation/validate-canon-provenance.py
   ```

8. **Commit** with a clear message describing the addition.

### Governance rules to observe

- Exactly ONE MO§ES entity. Never duplicate it.
- Canonical display: MO§ES™. Accepted prose: MO§ES. Aliases: mos2es, MOSES.
- Never render: MO§E§ or MO§E§™.
- Do NOT collapse Signomy and CIVITAE.
- SigRank evaluates AI operators, not AI models.
- The harness may measure authority, but it cannot manufacture authority.
- Automated systems may not promote claims into owner-approved truth.

---

## Version pinning requirements

### Standard version

This standard uses the version string `moses-ecosystem/0.1-draft`.
See `VERSION.yaml` for current metadata.

### Versioning policy

- **Major** version bumps indicate breaking changes to the ecosystem
  architecture or authority structure.
- **Minor** version bumps indicate additive changes (new components, new
  relationships).
- **Draft** versions are not frozen and may change without notice.
- **Frozen** versions are tagged and receive a DOI.

### Pinned dependency versions

Products that depend on TTEOP must pin to exact versions:

| Component | Dependency | Version |
|-----------|------------|---------|
| @sigrank/cascade | tteop-spec | 0.1.5-draft (exact) |
| sigrank-mcp | @sigrank/cascade | 0.2.1 (exact) |
| sigrank-mcp | tteop-spec | 0.1.5-draft (exact) |
| tteop-mcp | tteop-spec | 0.1.5-draft (exact) |

### Protocol version

TTEOP uses the version string `tteop/0.1-draft`. The legacy alias
`sigrank/0.1-draft` resolves to `tteop/0.1-draft`. Do not present the
legacy alias as a current standard.
