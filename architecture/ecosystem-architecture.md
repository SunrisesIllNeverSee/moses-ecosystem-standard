# Ecosystem Architecture

> Part of the [MO§ES Ecosystem Standard](../STANDARD.md).
> Version: `moses-ecosystem/0.1-draft`

This document describes the architecture of the MO§ES ecosystem: how
information flows, what principles govern it, how components are organized
into families, how they are classified, and what roles they play.

---

## Information source diagram

The MO§ES ecosystem is not a single repository or a single authority. It is
a governed information architecture in which several distinct sources each
supply a different kind of truth. The MO§ES Ecosystem Standard sits at the
center as the **public canonical overview**, projected downward from Search
Authority and informed laterally by three operational sources.

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

### What each arrow means

- **Search Authority → MO§ES Ecosystem Standard.** Search Authority is the
  sole master canon. The standard is a governed public projection of that
  canon. Every canonical claim in the standard traces upward to Search
  Authority; the standard does not independently invent truth.
- **MO§ES Framework → MO§ES Ecosystem Standard.** The Framework supplies
  formal framework references, claim IDs, ontology concepts, framework
  version, and formal status. The standard references those; it does not
  absorb ownership of them.
- **TTEOP → MO§ES Ecosystem Standard.** TTEOP supplies protocol identity,
  protocol version, protocol role, and canonical protocol URL. The standard
  says "TTEOP is the measurement protocol used here." It does not copy the
  metric specification.
- **Ello Control → MO§ES Ecosystem Standard.** Ello Control supplies
  repo_id, current repo/location, lifecycle, implementation relationship,
  and deployment mapping. This is **operational identity**, not canonical
  truth. Ello Control knows where things live; it does not define what they
  mean.

The three lateral sources are peers of each other, not subordinates. None
of them may override Search Authority, and none of them may override the
others within the others' domains.

---

## Architecture principles

### 1. Single authority source

Search Authority is the canonical internal authority. This standard is a
governed public projection of that canon. No ecosystem component may
independently invent canonical truth; all canonical claims trace to Search
Authority.

### 2. Separation of concerns

Framework, standards, protocols, and products are distinct layers with
distinct owners. The MO§ES Framework owns ontology and claims. TTEOP owns
protocol semantics. Products own their own behavior and extensions. This
standard owns the public ecosystem architecture. No layer absorbs another
layer's responsibility.

### 3. No independent truth

No ecosystem component — not a product, not a platform, not a transport
layer, not a tool, not a site — may independently invent canonical truth.
If a claim is canonical, it traces to Search Authority. If it is not in
Search Authority, it is not canonical here.

### 4. Protocol independence

TTEOP is independently authoritative for its protocol semantics. Ecosystem
standards (including this one) may reference TTEOP but may not redefine it.
Products implement TTEOP through version-pinned implementation profiles;
they do not reinterpret the protocol.

### 5. One MO§ES entity

There is exactly one MO§ES™ entity. It may appear in multiple graph
positions (governance role, trademark holder, ecosystem namesake) but it is
never duplicated, forked, or split. Canonical display is MO§ES™; accepted
prose is MO§ES; aliases are mos2es and MOSES. Never render MO§E§ or
MO§E§™.

---

## Family structure

The MO§ES ecosystem is organized into families. A family is a coherent
group of components that share a domain, a measurement concern, or a
governance relationship.

### MO§ES Framework family

The MO§ES Framework family contains the formal ontology, methodology,
claims, laws, epistemic states, and framework structure.

| Component | Type | Role |
|-----------|------|------|
| MO§ES Framework | framework | canonical_source |
| Commitment Theory | research | evidence_source |
| Conservation Law of Commitment | research | evidence_source |
| KASSA | research | evidence_source |

The Framework family is the formal/theoretical axis of the ecosystem. It
owns what the ecosystem *means*; it does not own how the ecosystem is
*measured* or *implemented*.

### SigRank family

The SigRank family is the AI operator evaluation and measurement ecosystem.
SigRank evaluates AI **operators**, not AI models.

| Component | Type | Role |
|-----------|------|------|
| SignalAF | product | projection |
| SigRank | product | projection |
| Upsilon | product | implementation |
| Yield (Υ) | metric | reference |

Product boundaries within the SigRank family:

- SigRank is the public leaderboard/proof surface, not the measurement
  engine (that is Upsilon).
- Upsilon is the measurement engine, not the leaderboard (that is SigRank).
- Upsilon is **not** the same as Yield. Yield is a metric inside Upsilon:
  Υ = (R × O) / I².
- SignalAF is the distribution surface, not the governance authority.

### Other families

| Family | Members | Notes |
|--------|---------|-------|
| Signomy | Signomy | Platform governed by MO§ES™. Independently resolvable. |
| CIVITAE | CIVITAE | Constitutional AI ecosystem governed by MO§ES™. Independently resolvable. |

Signomy and CIVITAE are independently resolvable platforms governed by
MO§ES™. They must **not** be collapsed into a single entity.

---

## Component taxonomy

Every ecosystem component has exactly one component type.

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

---

## Role classification

Each component has exactly one primary role and may have secondary roles.

| Role | Meaning |
|------|---------|
| `authority` | Owns canonical truth for its domain |
| `implementation` | Implements canonical truth |
| `transport` | Provides transport/access without defining semantics |
| `projection` | Public projection of internal canon |
| `reference` | Reference implementation or fixture |
| `evidence_source` | Provides evidence for canonical claims |
| `legacy_source` | Superseded, retained for compatibility |

### How type and role relate

Type describes *what kind of thing* a component is. Role describes *what
authority function* it performs. A product (type) can be an implementation
(role) of a protocol. A transport (type) is always a transport (role) by
definition, because it carries semantics without defining them. A standard
(type) is typically a projection (role) of an internal canon.

---

## See also

- [Authority Architecture](authority-architecture.md) — who owns what kind
  of truth, and the authority chains for ecosystem and measurement.
- [Standards and Protocols](standards-and-protocols.md) — version strings,
  version pinning, and the relationship between this standard, TTEOP, and
  the legacy sigrank-standard.
- [Public Surfaces](public-surfaces.md) — the public sites and the core
  invariant every MO§ES surface should satisfy.
- [STANDARD.md §3 Ecosystem Architecture](../STANDARD.md#3-ecosystem-architecture)
- [STANDARD.md §5 Component Taxonomy](../STANDARD.md#5-component-taxonomy)
