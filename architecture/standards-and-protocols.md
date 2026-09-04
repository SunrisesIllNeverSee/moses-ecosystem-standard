# Standards and Protocols

> Part of the [MO§ES Ecosystem Standard](../STANDARD.md).
> Version: `moses-ecosystem/0.1-draft`

This document describes the standards and protocols used within the MO§ES
ecosystem: what each one is, what version it is, what authority it holds,
how they relate to each other, and what version-pinning requirements apply
to products.

---

## MO§ES Ecosystem Standard (this standard)

| Field | Value |
|-------|-------|
| **Name** | MO§ES Ecosystem Standard |
| **Version** | `moses-ecosystem/0.1-draft` |
| **Status** | Draft — not yet a frozen standard |
| **Role** | Canonical public ecosystem architecture and reference |
| **Authority** | Governed projection of Search Authority |
| **Repository** | https://github.com/SunrisesIllNeverSee/moses-ecosystem-standard |
| **License** | CC BY 4.0 |

This standard is the canonical public architecture and reference standard
for the entire MO§ES ecosystem. It is a governed public projection of the
Search Authority master canon. It is a canonical information package, not a
product monorepo.

### What this standard owns

- Ecosystem architecture and component taxonomy
- Authority relationships between ecosystem components
- Product families and their roles
- Public sites, surfaces, and identifiers
- Canonical terminology
- Versioning and conformance rules

### What this standard does not own

- TTEOP protocol semantics (owned by TTEOP)
- MO§ES Framework ontology (owned by the Framework)
- Search Authority internal canon structure (owned by Search Authority)
- Product implementation details (owned by each product)

---

## TTEOP

| Field | Value |
|-------|-------|
| **Name** | TTEOP — Token Telemetry Evaluation Operator Protocol |
| **Protocol version** | `tteop/0.1-draft` |
| **Status** | Draft |
| **Role** | Sole interoperability protocol authority for token telemetry |
| **Legacy alias** | `sigrank/0.1-draft` (resolves to `tteop/0.1-draft`) |
| **Repository** | otep-spec repo (see references/tteop.yaml) |
| **npm package** | tteop-spec |
| **DOI (version)** | 10.5281/zenodo.22180349 |
| **DOI (concept)** | 10.5281/zenodo.22180348 |

TTEOP is the vendor-neutral measurement interoperability protocol for the
MO§ES ecosystem. It is independently authoritative for its protocol
semantics. This standard may reference TTEOP but may not redefine it.

### What TTEOP owns

- Protocol identity and version
- Telemetry primitives: `input` (I), `output` (O), `cache_write` (W),
  `cache_read` (R) — four non-negative integer token counts
- Protocol semantics and metric definitions
- Privacy requirements for telemetry

### Legacy alias

The version string `sigrank/0.1-draft` is a **legacy alias** that resolves
to `tteop/0.1-draft`. Products and references that still carry the legacy
alias should migrate to the canonical `tteop/` prefix. The alias exists for
compatibility, not for independent versioning.

---

## sigrank-standard (legacy)

| Field | Value |
|-------|-------|
| **Name** | sigrank-standard |
| **Status** | LEGACY PREDECESSOR — superseded by TTEOP |
| **Role** | Compatibility and migration evidence only |
| **Authority class** | `legacy_compatibility_source` |

sigrank-standard is the legacy predecessor of TTEOP. It has been superseded.
It is retained for compatibility and migration evidence only. It must not
be presented as a current standard.

### Legacy rules

- No component may present `sigrank-standard` or the `sigrank/0.1-draft`
  identifier as a current standard.
- The legacy alias `sigrank/0.1-draft` resolves to `tteop/0.1-draft` for
  compatibility.
- References to sigrank-standard should be accompanied by a note that it is
  superseded.

---

## Relationship between standards

The MO§ES ecosystem contains three distinct standards/protocols that are
often confused. They are not interchangeable.

| Standard/Protocol | Domain | Authority |
|-------------------|--------|-----------|
| **MO§ES Ecosystem Standard** (this) | Ecosystem architecture | Public projection of Search Authority |
| **TTEOP** | Measurement protocol | Sole protocol specification authority |
| **sigrank-standard** (legacy) | Legacy predecessor | Compatibility only, superseded |

### Ecosystem architecture vs. measurement protocol

The MO§ES Ecosystem Standard describes the *whole ecosystem*: what
components exist, what roles they have, how they relate, and which
authority governs each. TTEOP describes *one protocol*: how token telemetry
is measured and interoperated. The standard references TTEOP as the
measurement protocol; it does not copy or redefine TTEOP's semantics.

### Ecosystem architecture vs. legacy

sigrank-standard was a predecessor that has been superseded by TTEOP. It is
retained for compatibility and migration evidence. It is not a current
standard and must not be presented as one.

### Measurement protocol vs. legacy

TTEOP is the current protocol. sigrank-standard is the superseded
predecessor. The legacy alias `sigrank/0.1-draft` resolves to
`tteop/0.1-draft` so that older references continue to work, but no new
component should adopt the legacy identifier.

---

## Version pinning requirements

Products that use TTEOP must pin **exact** TTEOP versions. This is a
conformance requirement, not a recommendation.

### Why exact pinning

TTEOP is a measurement protocol. If a product's TTEOP version drifts, its
measurements are not comparable to other products' measurements. Exact
pinning ensures that every product in the ecosystem is measuring against
the same protocol version at any given time.

### What "exact" means

- Products must pin a specific version (e.g. `0.1.5-draft`), not a range.
- Products must not use floating versions (`^`, `~`, `latest`).
- When TTEOP releases a new version, products must consciously update their
  pin; the pin does not auto-advance.

### Conformance

A component conforms to this standard when:

1. It correctly identifies its role in the ecosystem architecture.
2. It traces its canonical claims to Search Authority.
3. If it uses TTEOP, it implements TTEOP through a version-pinned
   implementation profile and does not redefine TTEOP semantics.
4. It uses canonical terminology correctly.
5. It does not present legacy identifiers as current standards.

---

## Current pinned versions

| Component | Dependency | Pinned version |
|-----------|------------|----------------|
| @sigrank/cascade | tteop-spec | `0.1.5-draft` (exact) |
| sigrank-mcp | @sigrank/cascade | `0.2.1` (exact) |
| sigrank-mcp | tteop-spec | `0.1.5-draft` (exact) |
| tteop-mcp | tteop-spec | `0.1.5-draft` (exact) |

All pins are exact. No component in the ecosystem uses a floating TTEOP
version.

### How to read this table

- `@sigrank/cascade` is the SigRank product facade. It pins `tteop-spec` at
  `0.1.5-draft` exactly.
- `sigrank-mcp` is the product tooling. It pins `@sigrank/cascade` at
  `0.2.1` exactly, and also pins `tteop-spec` at `0.1.5-draft` exactly
  (because it depends on the protocol directly, not only transitively).
- `tteop-mcp` is the MCP transport layer over TTEOP. It pins `tteop-spec`
  at `0.1.5-draft` exactly.

---

## Versioning policy

- **Major version bumps** indicate breaking changes to the ecosystem
  architecture or authority structure.
- **Minor version bumps** indicate additive changes (new components, new
  relationships).
- **Draft versions** are not frozen and may change without notice.
- **Frozen versions** are tagged and receive a DOI.

### Current ecosystem identifiers

| Identifier | Value | Role |
|------------|-------|------|
| MO§ES Ecosystem Standard | `moses-ecosystem/0.1-draft` | This standard's version |
| TTEOP | `tteop/0.1-draft` | Current protocol version |
| sigrank/0.1-draft | legacy alias → `tteop/0.1-draft` | Legacy compatibility |

---

## See also

- [Ecosystem Architecture](ecosystem-architecture.md) — the component
  taxonomy and family structure these standards govern.
- [Authority Architecture](authority-architecture.md) — the authority
  classes and chains, including the measurement authority chain.
- [STANDARD.md §8 Standards and Protocols](../STANDARD.md#8-standards-and-protocols)
- [STANDARD.md §15 Versioning](../STANDARD.md#15-versioning)
- [registry/standards.yaml](../registry/standards.yaml) and
  [registry/protocols.yaml](../registry/protocols.yaml) — machine-readable
  registries (when available).
