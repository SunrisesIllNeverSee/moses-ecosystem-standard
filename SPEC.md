# MO§ES Ecosystem Standard

## Specification v0.1-draft

**Status:** Draft — not yet a frozen standard
**Standard name:** MO§ES Ecosystem Standard
**Version string:** `moses-ecosystem/0.1-draft`
**Owner:** Deric J. McHenry / Ello Cello LLC
**Canonical display:** MO§ES™. Accepted prose: MO§ES. Aliases: mos2es, MOSES. Never render: MO§E§.

- **Repository:** https://github.com/SunrisesIllNeverSee/moses-ecosystem-standard
- **Authority source:** Search Authority (private, governed master canon)
- **MO§ES™ website:** https://mos2es.com
- **Trademark:** MO§ES™ is a service mark of Ello Cello LLC (TM 99408355)

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Definition of MO§ES](#2-definition-of-moses)
3. [Ecosystem Architecture](#3-ecosystem-architecture)
4. [Authority Architecture](#4-authority-architecture)
5. [Component Taxonomy](#5-component-taxonomy)
6. [Product Families](#6-product-families)
7. [Research/Framework Families](#7-researchframework-families)
8. [Standards and Protocols](#8-standards-and-protocols)
9. [MO§ES Framework Relationship](#9-moses-framework-relationship)
10. [SigRank Ecosystem Relationship](#10-sigrank-ecosystem-relationship)
11. [TTEOP Relationship](#11-tteop-relationship)
12. [Public Sites and Surfaces](#12-public-sites-and-surfaces)
13. [Canonical Terminology](#13-canonical-terminology)
14. [Data and Privacy Boundaries](#14-data-and-privacy-boundaries)
15. [Versioning](#15-versioning)
16. [Conformance and Reference Rules](#16-conformance-and-reference-rules)
17. [Canonical URLs and Identifiers](#17-canonical-urls-and-identifiers)
18. [Machine-Readable Component Registry](#18-machine-readable-component-registry)
19. [Search Authority Provenance](#19-search-authority-provenance)
20. [Change History](#20-change-history)

---

## 1. Purpose and Scope

### 1.1 Purpose

The MO§ES Ecosystem Standard is the canonical public architecture and
reference standard for the entire MO§ES ecosystem. Its purpose is to
answer:

> What is the MO§ES ecosystem, what components belong to it, what roles
> do they have, how do they relate, and which authority governs each type
> of information?

### 1.2 Scope

This standard covers:

- The definition and identity of MO§ES™
- The ecosystem architecture and component taxonomy
- Authority relationships between ecosystem components
- Product families and their roles
- Research and framework families
- Standards and protocols used within the ecosystem
- Public sites, surfaces, and identifiers
- Canonical terminology
- Data and privacy boundaries
- Versioning and conformance rules

### 1.3 Out of scope

This standard does **not**:

- Define the MO§ES Framework's formal ontology, methodology, claims, or
  laws (that is the MO§ES Framework's role)
- Define TTEOP protocol semantics (that is TTEOP's role)
- Define Search Authority's internal canon structure (that is Search
  Authority's role)
- Define product-level implementation details (that is each product's role)

### 1.4 Core invariant

Every significant MO§ES public surface should eventually be able to answer:

```
What am I?
What family am I part of?
What is my role?
What standard/framework/protocol governs me?
Where is the canonical ecosystem reference?
What Search Authority-backed identity does this resolve to?
```

The objective is that no webpage, repository, MCP, product, article, or AI
agent has to independently reconstruct the MO§ES ecosystem.

---

## 2. Definition of MO§ES

### 2.1 Identity

MO§ES™ is a sovereign signal governance system created by Deric J.
McHenry. It is the enforcement architecture for Commitment Theory and
operationalizes the Conservation Law of Commitment.

- **Canonical display:** MO§ES™
- **Accepted prose:** MO§ES
- **Aliases:** mos2es, MOSES
- **Never render:** MO§E§ or MO§E§™
- **Trademark:** 99408355 (IC 042, filed 2025-09-23)
- **Patent:** 63/877,177 (provisional, filed 2025-09-07) — covers the
  MO§ES Constitutional Governance Architecture
- **Service mark of:** Ello Cello LLC
- **Website:** https://mos2es.com

### 2.2 What MO§ES™ is

MO§ES™ is the governance and enforcement architecture. It governs
platforms, products, and research within the ecosystem. It is not a
product surface itself.

### 2.3 What MO§ES™ is not

- MO§ES™ is not a product surface (SignalAF, SigRank, Upsilon are products)
- MO§ES™ is not a measurement protocol (TTEOP is the protocol)
- MO§ES™ is not a public site (mos2es.com is the site)
- MO§ES™ is not interchangeable with any single product it governs

### 2.4 Disputed definitions

The interpretive definition of MO§ES™ (e.g. "semantic meaning at
execution") remains under owner review and is **not** canonical. This
standard records the identity, provenance, and governance role of
MO§ES™ without resolving disputed definitional wording. See Search
Authority canon record MO-DEF-001.

---

## 3. Ecosystem Architecture

### 3.1 Target architecture

```
                         SEARCH AUTHORITY
                              │
                              ▼
                    MO§ES ECOSYSTEM STANDARD
                              │
          ┌───────────────────┼────────────────────┐
          │                   │                    │
          ▼                   ▼                    ▼
   MO§ES Framework     SigRank Ecosystem      Other MO§ES
                         Standard               families
                              │
                       ┌──────┴──────┐
                       ▼             ▼
                   SignalAF       Upsilon
                       │             │
                       └──────┬──────┘
                              │ uses
                              ▼
                            TTEOP
```

### 3.2 Architecture principles

1. **Single authority source.** Search Authority is the canonical
   internal authority. This standard is a governed public projection.
2. **Separation of concerns.** Framework, standards, protocols, and
   products are distinct layers with distinct owners.
3. **No independent truth.** No ecosystem component may independently
   invent canonical truth. All canonical claims trace to Search Authority.
4. **Protocol independence.** TTEOP is independently authoritative for
   its protocol semantics. Ecosystem standards may reference but not
   redefine it.
5. **One MO§ES entity.** There is exactly one MO§ES™ entity. It may
   appear in multiple graph positions but is never duplicated.

---

## 4. Authority Architecture

### 4.1 Authority classes

| Class | Owner | Scope |
|-------|-------|-------|
| `master_canon` | Search Authority | All canonical truth |
| `protocol_specification` | TTEOP (otep-spec repo) | Telemetry protocol semantics |
| `canonical_source` | MO§ES Framework | Ontology, methodology, claims, laws |
| `product_implementation` | SigRank / SignalAF / Upsilon | Product behavior and extensions |
| `transport` | tteop-mcp | MCP transport over TTEOP |
| `legacy_compatibility_source` | sigrank-standard | Legacy predecessor, retained for compatibility |
| `public_projection` | This standard, mos2es.com | Public ecosystem reference |

### 4.2 Authority rules

1. **Search Authority** is the sole master canon owner. All canonical
   truth traces to it.
2. **TTEOP** is the sole protocol specification authority for token
   telemetry measurement. Products implement TTEOP through version-pinned
   implementation profiles and may not redefine TTEOP semantics.
3. **MO§ES Framework** is the canonical source for ontology, methodology,
   claims, and laws. This standard references but does not redefine
   framework content.
4. **Products** own their product behavior and extensions but may not
   redefine protocol semantics, framework claims, or ecosystem authority.
5. **This standard** is a public projection. It does not independently
   invent canonical truth. Every claim it makes traces to Search
   Authority.

### 4.3 Authority chain

```
Search Authority (canonical internal authority)
      ↓
MO§ES Ecosystem Standard (governed public projection)
      ↓
public ecosystem reference
```

---

## 5. Component Taxonomy

### 5.1 Component types

| Type | Description | Examples |
|------|-------------|----------|
| `framework` | Formal ontology, methodology, claims, laws | MO§ES Framework |
| `standard` | Public architecture/reference standard | This standard, TTEOP |
| `protocol` | Vendor-neutral interoperability protocol | TTEOP |
| `product` | Commercial or public product | SignalAF, SigRank, Upsilon |
| `platform` | Governed platform surface | Signomy, CIVITAE |
| `transport` | MCP transport layer | tteop-mcp, sigrank-mcp |
| `tool` | Companion tool or extension | sigrank-vscode, sigrank-agent |
| `research` | Research program or dataset | Commitment Theory, SigRank Index |
| `site` | Public website | mos2es.com, signalaf.com |
| `legacy` | Superseded predecessor | sigrank-standard |
| `governance` | Governance implementation | moses-governance |
| `infrastructure` | Shared infrastructure | ello-repo-control, search-authority |

### 5.2 Role classification

Each component has exactly one primary role and may have secondary roles:

- **authority** — owns canonical truth for its domain
- **implementation** — implements canonical truth
- **transport** — provides transport/access without defining semantics
- **projection** — public projection of internal canon
- **reference** — reference implementation or fixture
- **evidence_source** — provides evidence for canonical claims
- **legacy_source** — superseded, retained for compatibility

---

## 6. Product Families

### 6.1 SigRank family

The SigRank family is the AI operator evaluation and measurement ecosystem.

| Component | Role | Description |
|-----------|------|-------------|
| SignalAF | product / distribution surface | Public brand and distribution surface for AI operator measurement |
| SigRank | product / leaderboard | Public leaderboard and proof surface for AI operator evaluation |
| Upsilon | product / measurement engine | Commercial measurement engine producing diagnostic measures |
| Yield (Υ) | metric | Flagship metric inside Upsilon: Υ = (R × O) / I² |
| sigrank-app | implementation | Next.js app at signalaf.com |
| sigrank-mcp | implementation / transport | On-device scanner and MCP tool |
| @sigrank/cascade | implementation / facade | SigRank product facade over TTEOP canonical semantics |
| sigrank-vscode | tool | VS Code extension |
| sigrank-agent | tool | Local telemetry agent |
| sigarena | tool | Satellite site |
| signa | tool | Companion tool |
| sigadmin-web | tool | Admin dashboard |

### 6.2 Product boundaries

- SigRank evaluates AI **operators**, not AI models
- SigRank is the public leaderboard/proof surface, not the measurement engine (that is Upsilon)
- Upsilon is the measurement engine, not the leaderboard (that is SigRank)
- Upsilon is NOT the same as Yield. Yield is a metric inside Upsilon
- SignalAF is the distribution surface, not the governance authority
- Brainstormed enterprise extensions are not automatically public canon

---

## 7. Research/Framework Families

### 7.1 MO§ES Framework

The MO§ES Framework is the formal ontology, methodology, claims, laws,
epistemic states, and framework structure. It is the canonical source for
framework content.

- **Repository:** https://github.com/SunrisesIllNeverSee/moses-framework
- **Status:** v0.1 — Canonical Ontology (proposal pending owner freeze)
- **Patent:** 63/877,177

### 7.2 Commitment Theory

Commitment Theory is a research framework containing the Conservation Law
of Commitment. MO§ES™ is the enforcement architecture for Commitment
Theory.

- **Repository:** https://github.com/SunrisesIllNeverSee/Commitment_Theory
- **Author:** Deric J. McHenry
- **DOI:** 10.5281/zenodo.20031715 (V.1), 10.5281/zenodo.21069704 (V2)

### 7.3 Conservation Law of Commitment

A falsifiable empirical claim that commitment is conserved under governed
transformation and decays under ungoverned transformation. The theoretical
foundation for SigRank.

- **DOI:** 10.5281/zenodo.20029607 (V.05)
- **Concept DOI:** 10.5281/zenodo.18267278

### 7.4 KASSA

K-Governed Voice Architecture that publicly demonstrates MO§ES™
principles. The public harness is distinct from the production MO§ES™
substrate.

- **Repository:** https://github.com/SunrisesIllNeverSee/KASSA

### 7.5 Signomy and CIVITAE

Signomy and CIVITAE are independently resolvable platforms governed by
MO§ES™. They must not be collapsed.

- **Signomy:** https://signomy.xyz
- **CIVITAE:** https://signomy.xyz (same domain, distinct entity)
- **CIVITAE patent:** 19/426,028 (utility, filed 2025-12-18)

---

## 8. Standards and Protocols

### 8.1 MO§ES Ecosystem Standard (this document)

- **Version:** `moses-ecosystem/0.1-draft`
- **Role:** Canonical public ecosystem architecture and reference
- **Authority:** Governed projection of Search Authority

### 8.2 TTEOP

- **Protocol version:** `tteop/0.1-draft`
- **Repository:** https://github.com/SunrisesIllNeverSee/otep-spec
- **npm package:** tteop-spec
- **Role:** Sole interoperability protocol authority for token telemetry
- **Legacy alias:** `sigrank/0.1-draft` (resolves to `tteop/0.1-draft`)
- **Version DOI:** 10.5281/zenodo.22180349
- **Concept DOI:** 10.5281/zenodo.22180348

### 8.3 sigrank-standard (legacy)

- **Status:** LEGACY PREDECESSOR — superseded by TTEOP
- **Role:** Compatibility and migration evidence only
- **Not:** A current protocol authority or product standard

### 8.4 Relationship between standards

```
MO§ES Ecosystem Standard
  = ecosystem architecture (this document)

TTEOP
  = vendor-neutral measurement interoperability protocol

sigrank-standard
  = legacy predecessor (compatibility only)
```

The MO§ES Ecosystem Standard and TTEOP are independent. This standard may
reference TTEOP but may not redefine it. TTEOP remains independently
authoritative for its protocol semantics.

---

## 9. MO§ES Framework Relationship

### 9.1 Distinction

```
MO§ES Ecosystem Standard
= ecosystem architecture, component roles, relationships, standards,
  products, public reference

MO§ES Framework
= formal ontology, methodology, claims, laws, epistemic states,
  and framework structure
```

Neither replaces the other.

### 9.2 Relationship

The MO§ES Framework is the canonical source for framework content
(ontology, methodology, claims, laws). This standard references the
framework for its definitional content but does not redefine or
re-interpret it.

### 9.3 Authority

- Framework content authority: MO§ES Framework repository
- Ecosystem architecture authority: This standard (via Search Authority projection)

---

## 10. SigRank Ecosystem Relationship

### 10.1 Distinction

```
MO§ES Ecosystem Standard
= whole ecosystem

SigRank Ecosystem Standard
= one ecosystem/family within MO§ES
```

### 10.2 Relationship

The SigRank ecosystem is one family within the broader MO§ES ecosystem.
A future SigRank Ecosystem Standard should reference this standard as its
broader ecosystem context.

### 10.3 Components

The SigRank family includes: SignalAF, SigRank, Upsilon, sigrank-app,
sigrank-mcp, @sigrank/cascade, sigrank-vscode, sigrank-agent, sigarena,
signa, sigadmin-web, and related tooling.

### 10.4 TTEOP usage

The SigRank family uses TTEOP for measurement interoperability.
SigRank/SignalAF/Upsilon implement TTEOP through version-pinned
implementation profiles and may not redefine TTEOP semantics.

---

## 11. TTEOP Relationship

### 11.1 Distinction

```
MO§ES Ecosystem Standard
= ecosystem architecture

TTEOP
= vendor-neutral measurement interoperability protocol
```

### 11.2 Relationship

TTEOP is independently authoritative for its protocol semantics. The
MO§ES Ecosystem Standard and the SigRank ecosystem may reference TTEOP
but may not redefine it.

### 11.3 Authority chain for measurement

```
TTEOP (protocol specification)
  → tteop-spec (canonical executable/reference semantics)
    → @sigrank/cascade (SigRank product facade)
      → sigrank-mcp (product tooling)
```

### 11.4 Legacy compatibility

The legacy identifier `sigrank/0.1-draft` resolves to `tteop/0.1-draft`.
It is retained for backward compatibility and does not constitute a
second active standard.

---

## 12. Public Sites and Surfaces

| Site | URL | Role |
|------|-----|------|
| MO§ES™ website | https://mos2es.com | Public site for MO§ES™ |
| SignalAF | https://signalaf.com | Public brand and distribution surface |
| SigRank methodology | https://signalaf.com/methodology | Methodology reference |
| SigRank research | https://signalaf.com/research | Research and dataset |
| SigRank science | https://signalaf.com/science | Conservation Law reference |
| Signomy | https://signomy.xyz | Platform governed by MO§ES™ |
| Upsilon | https://mos2es.org | Commercial measurement engine |
| This standard | https://github.com/SunrisesIllNeverSee/moses-ecosystem-standard | Public ecosystem reference |

---

## 13. Canonical Terminology

### 13.1 Current terms

| Term | Status | Notes |
|------|--------|-------|
| MO§ES™ | owner_approved | Canonical display. Never MO§E§. |
| Commitment Theory | source_supported | Abbreviation: CT |
| Conservation Law of Commitment | source_supported | Falsifiable empirical claim |
| SigRank | owner_approved | Evaluates AI operators, not models |
| SigRank Index | owner_approved | Dataset produced by SigRank |
| SignalAF | owner_approved | Public brand/distribution surface |
| Upsilon | owner_approved | Measurement engine (not the leaderboard) |
| Yield (Υ) | owner_approved | Metric inside Upsilon: Υ = (R × O) / I² |
| TTEOP | owner_approved | Token Telemetry Evaluation Operator Protocol |
| KASSA | source_supported | K-Governed Voice Architecture |
| Signomy | source_supported | Platform governed by MO§ES™ |
| CIVITAE | source_supported | Constitutional AI ecosystem governed by MO§ES™ |
| Ello Cello LLC | owner_approved | Organization |
| Deric J. McHenry | owner_approved | Author/owner |

### 13.2 Stale terms

| Term | Replacement | Reason |
|------|-------------|--------|
| Commitment Conservation Theory | Commitment Theory | Superseded; conservation remains at law level |
| "SigRank" (as measurement engine) | Upsilon | SigRank is now the leaderboard, not the engine |

### 13.3 Display aliases

| Canonical (TTEOP) | Display alias (SigRank) | Status |
|--------------------|------------------------|--------|
| output_fraction | SNR | SigRank display alias, not independent metric |
| log_leverage | 10xDEV | SigRank display alias, not independent metric |

---

## 14. Data and Privacy Boundaries

### 14.1 Telemetry primitives

TTEOP defines four non-negative integer telemetry primitives:

- `input` (I) — fresh input tokens
- `output` (O) — output tokens
- `cache_write` (W) — cache creation/write tokens
- `cache_read` (R) — cache read tokens

### 14.2 Privacy requirements

- TTEOP telemetry must never contain prompt text, response text, source
  code, repository contents, keystrokes, screen content, secrets, or
  direct real-world identity.
- Privacy claims must distinguish content-free token telemetry from zero
  metadata risk.
- Upsilon does not require prompt text or code contents to calculate core
  token-derived measures.

### 14.3 Content independence

Telemetry is content-independent. The four primitives are token counts,
not content. No ecosystem component may introduce content-dependent
telemetry as a TTEOP primitive.

### 14.4 Provenance levels

TTEOP defines four provenance levels:

1. `self-reported`
2. `collector-attested`
3. `platform-verified`
4. `signed`

Products must declare their provenance level. Higher levels require
stronger attestation.

---

## 15. Versioning

### 15.1 Standard version

This standard uses the version string `moses-ecosystem/0.1-draft`.

### 15.2 Versioning policy

- Major version bumps indicate breaking changes to the ecosystem
  architecture or authority structure.
- Minor version bumps indicate additive changes (new components, new
  relationships).
- Draft versions are not frozen and may change without notice.
- Frozen versions are tagged and receive a DOI.

### 15.3 Dependency versioning

Ecosystem components that depend on TTEOP must pin exact versions:

```
product/release
    ↓
known TTEOP version
    ↓
known tteop-spec release
```

This prevents silent semantic changes through unrelated dependency
updates.

### 15.4 Current pinned versions

| Component | Dependency | Version |
|-----------|------------|---------|
| @sigrank/cascade | tteop-spec | 0.1.5-draft (exact) |
| sigrank-mcp | @sigrank/cascade | 0.2.1 (exact) |
| sigrank-mcp | tteop-spec | 0.1.5-draft (exact) |
| tteop-mcp | tteop-spec | 0.1.5-draft (exact) |

---

## 16. Conformance and Reference Rules

### 16.1 What conformance means

A component conforms to this standard when:

1. It correctly identifies its role in the ecosystem architecture.
2. It traces its canonical claims to Search Authority (not independently
   inventing truth).
3. If it uses TTEOP, it implements TTEOP through a version-pinned
   implementation profile and does not redefine TTEOP semantics.
4. It uses canonical terminology correctly (MO§ES™, not MO§E§; Upsilon
   for the measurement engine, not SigRank; etc.).
5. It does not present legacy identifiers as current standards.

### 16.2 Reference rules

- Products reference this standard for ecosystem architecture.
- Products reference TTEOP for measurement protocol semantics.
- Products reference the MO§ES Framework for ontology and methodology.
- Products reference Search Authority for canonical truth (via canon
  context loading or the canon MCP).

### 16.3 What this standard does not define

This standard does not define:

- TTEOP protocol semantics (see TTEOP SPEC.md)
- MO§ES Framework ontology (see the Framework repository)
- Product implementation details (see each product's documentation)
- Search Authority internal canon structure (see Search Authority)

---

## 17. Canonical URLs and Identifiers

### 17.1 Ecosystem identifiers

| Identifier | Value | Role |
|------------|-------|------|
| MO§ES Ecosystem Standard | `moses-ecosystem/0.1-draft` | This standard's version |
| TTEOP | `tteop/0.1-draft` | Current protocol version |
| sigrank/0.1-draft | legacy alias → `tteop/0.1-draft` | Legacy compatibility |

### 17.2 Canonical URLs

| Entity | URL |
|--------|-----|
| This standard | https://github.com/SunrisesIllNeverSee/moses-ecosystem-standard |
| MO§ES Framework | https://github.com/SunrisesIllNeverSee/moses-framework |
| TTEOP | https://github.com/SunrisesIllNeverSee/otep-spec |
| tteop-spec (npm) | https://www.npmjs.com/package/tteop-spec |
| Search Authority | (private) |
| Commitment Theory | https://github.com/SunrisesIllNeverSee/Commitment_Theory |
| KASSA | https://github.com/SunrisesIllNeverSee/KASSA |
| mos2es.com | https://mos2es.com |
| signalaf.com | https://signalaf.com |
| signomy.xyz | https://signomy.xyz |
| mos2es.org (Upsilon) | https://mos2es.org |

### 17.3 DOIs

| Entity | DOI |
|--------|-----|
| TTEOP version | 10.5281/zenodo.22180349 |
| TTEOP concept | 10.5281/zenodo.22180348 |
| Conservation Law paper | 10.5281/zenodo.20029607 |
| Conservation Law concept | 10.5281/zenodo.18267278 |
| Commitment Theory V.1 | 10.5281/zenodo.20031715 |
| Commitment Theory V2 | 10.5281/zenodo.21069704 |

### 17.4 Patents and trademarks

| IP | Number | Scope |
|----|--------|-------|
| MO§ES™ trademark | 99408355 | IC 042, filed 2025-09-23 |
| MO§ES patent | 63/877,177 | Constitutional Governance Architecture |
| Signal Compression patent | 63/883,018 | Signal Compression System Engine |
| Commitment Conservation patent | 63/991,282 | Commitment Conservation under Recursive Transformation |
| CIVITAE patent | 19/426,028 | CIVITAS utility surface |

---

## 18. Machine-Readable Component Registry

A machine-readable component registry is maintained at
[registry/components.yaml](registry/components.yaml).

### 18.1 Registry purpose

The registry provides a single machine-readable source for:

- Component identity (id, name, aliases)
- Component type and role
- Authority class and owner
- Family membership
- Canonical URLs
- Relationships between components
- Version pins

### 18.2 Registry consumers

- AI agents that need to understand the ecosystem
- Automated tooling that validates ecosystem consistency
- Public sites that display ecosystem architecture
- The ello-repo-control catalog (cross-referenced)

### 18.3 Registry governance

The registry is a public projection of the Search Authority entity graph
and the ello-repo-control catalog. Changes to the registry must trace to
Search Authority canon or owner-approved catalog updates.

---

## 19. Search Authority Provenance

### 19.1 Authority source

This standard is a governed public projection of the Search Authority
master canon. Search Authority is the canonical internal authority for
the owner's complete body of work.

### 19.2 What this means

- Every canonical claim in this standard traces to a Search Authority
  canon record.
- This standard does not independently invent canonical truth.
- Disputed claims in Search Authority remain disputed here — this
  standard does not resolve them.
- Owner-approved facts in Search Authority are presented as canonical
  here.

### 19.3 Canon context loading

Products and agents that need canonical context should load it from
Search Authority:

```bash
python3 canon_cli.py context moses
python3 canon_cli.py context sigrank
python3 canon_cli.py context ecosystem
```

Or use the canon MCP server:

```bash
python3 canon_mcp.py
```

### 19.4 Governance rules (from Search Authority)

- The harness may measure authority, but it cannot manufacture authority.
- Automated systems may not promote claims into owner-approved truth.
- Exactly ONE MO§ES entity. Never duplicate it.
- Canonical display: MO§ES™. Accepted prose: MO§ES. Aliases: mos2es,
  MOSES. Never render: MO§E§ or MO§E§™.
- Do NOT collapse Signomy and CIVITAE.
- Archetype = shape. Class = scale/qualification. Rank = field position.
- SigRank evaluates AI operators, not AI models.

---

## 20. Change History

### v0.1-draft (2026-09-04)

- Initial draft of the MO§ES Ecosystem Standard.
- 20 sections covering purpose, definition, architecture, authority,
  taxonomy, product families, research families, standards, framework
  relationship, SigRank relationship, TTEOP relationship, public sites,
  terminology, privacy, versioning, conformance, URLs, registry, Search
  Authority provenance, and change history.
- Machine-readable component registry created.
- This is a draft. It is not frozen and may change without notice.

---

## Governing Rule

> Search Authority is the canonical internal authority. The MO§ES
> Ecosystem Standard is a governed public projection of that canon. The
> MO§ES Framework owns ontology, methodology, claims, and laws. TTEOP
> owns measurement protocol semantics. Products implement and extend
> these authorities but do not redefine them. Every MO§ES public surface
> should be able to answer what it is, what family it belongs to, what
> its role is, and what authority governs it.
