# Public Sites and Surfaces

> Part of the [MO§ES Ecosystem Standard](../STANDARD.md).
> Version: `moses-ecosystem/0.1-draft`

This document describes the public sites and surfaces of the MO§ES
ecosystem: what sites exist, what entity each represents, what role each
plays, the core invariant every public surface should satisfy, and the
publication rules that govern them.

---

## Public sites

| Site | URL | Role | Entity represented |
|------|-----|------|--------------------|
| MO§ES™ website | https://mos2es.com | Public site for MO§ES™ | MO§ES™ (the governance entity) |
| SignalAF | https://signalaf.com | Public brand and distribution surface | SignalAF (product) |
| Signomy | https://signomy.xyz | Platform governed by MO§ES™ | Signomy (platform) |
| Upsilon | https://mos2es.org | Commercial measurement engine | Upsilon (product) |
| This standard | https://github.com/SunrisesIllNeverSee/moses-ecosystem-standard | Public ecosystem reference | MO§ES Ecosystem Standard (this standard) |

### Notes on each site

**mos2es.com** is the public website for MO§ES™ itself — the governance and
enforcement architecture. It is not a product surface. It represents the
MO§ES™ entity directly.

**signalaf.com** is the public brand and distribution surface for SignalAF.
SignalAF is a product (the distribution surface), not the governance
authority.

**signomy.xyz** is the public site for Signomy, a platform governed by
MO§ES™. Signomy is independently resolvable and must not be collapsed with
CIVITAE.

**mos2es.org** is the public site for Upsilon, the commercial measurement
engine. Upsilon is the measurement engine, not the leaderboard (that is
SigRank) and not the same as Yield (Yield is a metric inside Upsilon).

**The standard repository** is the public ecosystem reference. It is this
repository. It is a canonical information package, not a product monorepo.

---

## Core invariant

Every significant MO§ES public surface should eventually be able to answer
six questions:

```
1. What am I?
2. What family am I part of?
3. What is my role?
4. What standard/framework/protocol governs me?
5. Where is the canonical ecosystem reference?
6. What Search Authority-backed identity does this resolve to?
```

### Why this invariant exists

The objective is that no webpage, repository, MCP, product, article, or AI
agent has to independently reconstruct the MO§ES ecosystem. If every public
surface can answer these six questions, then any consumer — human or
machine — can trace any surface back to canonical truth without guessing.

### What "answer" means

An answer is not a vague gesture toward MO§ES™. An answer is a resolvable
reference:

1. **What am I?** — A concrete identity (e.g. "SignalAF, the public brand
   and distribution surface").
2. **What family am I part of?** — A named family (e.g. "the SigRank
   family").
3. **What is my role?** — A role from the role classification (e.g.
   `projection`, `implementation`, `transport`).
4. **What standard/framework/protocol governs me?** — Specific version
   strings (e.g. `moses-ecosystem/0.1-draft`, `tteop/0.1-draft`).
5. **Where is the canonical ecosystem reference?** — A URL pointing to this
   standard repository.
6. **What Search Authority-backed identity does this resolve to?** — A
   traceable path back to a Search Authority canon record.

---

## Publication rules summary

> The full publication rules live in
> [docs/PUBLICATION-RULES.md](../docs/PUBLICATION-RULES.md).

### What publication rules govern

Publication rules govern how MO§ES ecosystem information is published to
public surfaces. They ensure that public surfaces do not independently
invent canonical truth and that they trace back to the correct authorities.

### Key principles

1. **No independent canonical truth on public surfaces.** A public surface
   may not invent canonical names, descriptions, relationships, or
   terminology. All canonical content traces to Search Authority.

2. **Correct authority attribution.** A public surface must attribute
   canonical claims to the correct authority class. Protocol semantics
   attribute to TTEOP. Ontology claims attribute to the MO§ES Framework.
   Ecosystem architecture attributes to this standard. Product behavior
   attributes to the product.

3. **Canonical terminology.** Public surfaces must use canonical
   terminology correctly. MO§ES™ for canonical display, MO§ES for prose.
   Never MO§E§. SigRank evaluates AI operators, not AI models. Do not
   collapse Signomy and CIVITAE.

4. **Version visibility.** Public surfaces that depend on TTEOP should make
   their pinned TTEOP version discoverable.

5. **Legacy handling.** Public surfaces must not present legacy
   identifiers (e.g. `sigrank-standard`, `sigrank/0.1-draft`) as current
   standards. Legacy identifiers may appear with a note that they are
   superseded.

6. **Resolvability.** Every public surface should resolve to a
   Search Authority-backed identity. A surface that cannot answer the core
   invariant questions is not yet a conforming MO§ES public surface.

---

## See also

- [Ecosystem Architecture](ecosystem-architecture.md) — the component
  taxonomy and family structure these surfaces represent.
- [Authority Architecture](authority-architecture.md) — the authority
  classes and chains these surfaces trace back to.
- [STANDARD.md §12 Public Sites and Surfaces](../STANDARD.md#12-public-sites-and-surfaces)
- [registry/sites.yaml](../registry/sites.yaml) — machine-readable site
  registry (when available).
- [docs/PUBLICATION-RULES.md](../docs/PUBLICATION-RULES.md) — full
  publication rules (when available).
