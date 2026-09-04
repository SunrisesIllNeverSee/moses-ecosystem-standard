# Authority Architecture

> Part of the [MO§ES Ecosystem Standard](../STANDARD.md).
> Version: `moses-ecosystem/0.1-draft`

This document describes the authority architecture of the MO§ES ecosystem:
which authority classes exist, who owns each one, what rules govern them,
how authority chains flow, what each information source supplies, and how
the sources differ in function.

---

## Authority classes

The MO§ES ecosystem recognizes seven authority classes. Each class has a
single owner and a defined scope. No component may claim authority outside
its class.

| Class | Owner | Scope |
|-------|-------|-------|
| `master_canon` | Search Authority | All canonical truth |
| `protocol_specification` | TTEOP (otep-spec repo) | Telemetry protocol semantics |
| `canonical_source` | MO§ES Framework | Ontology, methodology, claims, laws |
| `product_implementation` | SigRank / SignalAF / Upsilon | Product behavior and extensions |
| `transport` | tteop-mcp | MCP transport over TTEOP |
| `legacy_compatibility_source` | sigrank-standard | Legacy predecessor, retained for compatibility |
| `public_projection` | This standard, mos2es.com | Public ecosystem reference |

### What "authority class" means

An authority class is a *kind of truth*. Protocol semantics are a different
kind of truth than ontology claims, which are a different kind of truth
than product behavior. The class system prevents any single component from
claiming ownership over a kind of truth it does not own.

---

## Authority rules

1. **Search Authority is the sole master canon owner.** All canonical
   truth — names, descriptions, relationships, terminology, entity
   identity, authority assignments — traces to Search Authority. No other
   source may promote a claim into canonical truth.

2. **TTEOP is the sole protocol authority.** TTEOP owns token telemetry
   measurement protocol semantics. No product, standard, or transport
   layer may redefine TTEOP semantics. Products implement TTEOP through
   version-pinned implementation profiles.

3. **MO§ES Framework is the canonical source for ontology.** The Framework
   owns ontology, methodology, claims, laws, epistemic states, and
   framework structure. This standard references the Framework; it does not
   redefine or re-interpret it.

4. **Products own behavior but not protocol/framework semantics.** Products
   (SignalAF, SigRank, Upsilon) own their product behavior and extensions.
   They may not redefine protocol semantics, framework claims, or ecosystem
   authority.

5. **This standard is a public projection.** The MO§ES Ecosystem Standard
   is a governed public projection of Search Authority. It does not
   independently invent canonical truth. Disputed claims in Search
   Authority remain disputed here; the standard does not resolve them.

### Governance rules (from Search Authority)

- The harness may measure authority, but it cannot manufacture authority.
- Automated systems may not promote claims into owner-approved truth.
- Exactly ONE MO§ES entity. Never duplicate it.
- Canonical display: MO§ES™. Accepted prose: MO§ES. Aliases: mos2es,
  MOSES. Never render: MO§E§ or MO§E§™.
- Do NOT collapse Signomy and CIVITAE.
- SigRank evaluates AI operators, not AI models.

---

## Authority chain: ecosystem

The ecosystem authority chain flows from the internal master canon outward
to the public reference.

```
Search Authority
  (master canon, private/governed)
        │
        ▼
MO§ES Ecosystem Standard
  (public projection, this repository)
        │
        ▼
Public reference
  (mos2es.com, downstream consumers, AI agents)
```

Search Authority is the source. The MO§ES Ecosystem Standard is the
governed projection. Everything downstream — public sites, product
documentation, AI agents, third-party references — should resolve back
through this standard to Search Authority, not around it.

---

## Authority chain: measurement

The measurement authority chain flows from the protocol specification down
through the executable reference to the product facade to the product
tooling.

```
TTEOP
  (protocol specification)
        │
        ▼
tteop-spec
  (canonical executable / reference semantics)
        │
        ▼
@sigrank/cascade
  (SigRank product facade)
        │
        ▼
sigrank-mcp
  (product tooling)
```

Each layer implements or wraps the layer above it. No layer redefines the
semantics of the layer above. TTEOP defines the protocol; tteop-spec
provides the canonical executable reference; @sigrank/cascade is the
product facade that consumes it; sigrank-mcp is the tooling that exposes
it. Authority flows downward; implementation detail flows downward too, but
semantic authority never flows upward.

---

## What each information source supplies

### Search Authority

```
canonical names
approved descriptions
canonical relationships
approved public claims
terminology
entity identity
authority assignments
```

Search Authority is the canonical truth database. It is private and
governed. It is the sole source of canonical truth for the ecosystem.

### MO§ES Framework

```
formal framework references
claim IDs
ontology concepts
framework version
formal status
```

The MO§ES Framework is the formal framework, ontology, and claims source.
The standard references the Framework; it does not absorb ownership of the
Framework's content.

### TTEOP

```
protocol identity
protocol version
protocol role
canonical protocol URL
```

TTEOP is the technical interoperability protocol. The standard says "TTEOP
is the measurement protocol used here." It does not copy the metric
specification.

### Ello Control

```
repo_id
current repo/location
lifecycle
implementation relationship
deployment mapping
```

Ello Control supplies operational identity — where things live, what their
lifecycle state is, how implementations relate to each other, and how
deployments are mapped. This is **operational identity, not canonical
truth**. Ello Control knows where things live; it does not define what they
mean.

---

## The clean distinction

The four information sources are often confused. The distinction is clean:

| Source | Function | Analogy |
|--------|----------|---------|
| **Search Authority** | Canonical truth database | The private master records |
| **MO§ES Ecosystem Standard** | Canonical public explanation | The published public overview |
| **MO§ES Framework** | Formal framework / ontology / claims | The formal theory |
| **TTEOP** | Technical interoperability protocol | The wire protocol |
| **Ello Control** | Knows where things live | The operations ledger |

Search Authority defines what is true. The MO§ES Ecosystem Standard
explains the ecosystem publicly. The MO§ES Framework formalizes the theory.
TTEOP defines how measurement interoperates. Ello Control tracks where
everything actually lives. None of these substitutes for another.

---

## See also

- [Ecosystem Architecture](ecosystem-architecture.md) — the information
  source diagram, architecture principles, family structure, and component
  taxonomy.
- [Standards and Protocols](standards-and-protocols.md) — version strings
  and version pinning for the protocol authority chain.
- [STANDARD.md §4 Authority Architecture](../STANDARD.md#4-authority-architecture)
- [canon/authority-map.yaml](../canon/authority-map.yaml) — machine-readable
  authority map (when available).
