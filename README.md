# MO§ES Ecosystem Standard

**Canonical public architecture and reference standard for the MO§ES ecosystem.**

Owner: Deric J. McHenry / Ello Cello LLC
Status: v0.1-draft
Canonical display: MO§ES™. Accepted prose: MO§ES. Aliases: mos2es, MOSES. Never render: MO§E§.

## What this is

The MO§ES Ecosystem Standard is the **canonical public architecture and
reference standard** for the entire MO§ES ecosystem. It is a governed
public projection of the Search Authority master canon.

It is a **canonical information package**, not a product monorepo. It
contains references to ecosystem components, not copies of them.

## What this is not

- **Not** the MO§ES Framework (formal ontology, methodology, claims, laws)
- **Not** the SigRank Ecosystem Standard (one family within MO§ES)
- **Not** TTEOP (vendor-neutral measurement interoperability protocol)
- **Not** Search Authority (canonical internal authority)
- **Not** a product monorepo (does not contain product source code)

## Authority chain

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

## Repository structure

```
moses-ecosystem-standard/
├── README.md              — this file
├── STANDARD.md            — the standard (20 sections)
├── VERSION.yaml           — version metadata
├── CHANGELOG.md           — change history
├── LICENSE                — CC BY 4.0
├── AGENTS.md              — agent guidance
│
├── canon/                 — structured canonical information
│   ├── ecosystem.yaml     — ecosystem-level canonical info
│   ├── entities.yaml      — entity registry (projected from Search Authority)
│   ├── relationships.yaml — relationship graph
│   ├── terminology.yaml   — canonical terms
│   ├── authority-map.yaml — who owns what authority
│   └── sources.yaml       — source provenance
│
├── architecture/          — human-readable architecture documents
│   ├── ecosystem-architecture.md
│   ├── authority-architecture.md
│   ├── standards-and-protocols.md
│   └── public-surfaces.md
│
├── registry/              — machine-readable registries (references, not copies)
│   ├── components.yaml    — all components (unified view)
│   ├── standards.yaml     — standards
│   ├── protocols.yaml     — protocols
│   ├── frameworks.yaml    — frameworks
│   ├── products.yaml      — products
│   └── sites.yaml         — public sites
│
├── references/            — references to external authorities
│   ├── search-authority.yaml
│   ├── moses-framework.yaml
│   ├── sigrank-ecosystem-standard.yaml
│   ├── tteop.yaml
│   └── external-sources.yaml
│
├── machine/               — machine-readable standard metadata
│   ├── standard.json
│   ├── standard.yaml
│   └── standard.jsonld
│
├── validation/            — validation scripts
│   ├── validate-standard.py
│   ├── validate-authority-links.py
│   └── validate-canon-provenance.py
│
└── docs/                  — documentation
    ├── IMPLEMENTATION-GUIDE.md
    ├── AUTHORITY-BOUNDARIES.md
    └── PUBLICATION-RULES.md
```

## Quick reference

```
Search Authority        = canonical truth database
MO§ES Ecosystem Standard = canonical public explanation of the ecosystem
MO§ES Framework         = formal framework / ontology / claims
SigRank Ecosystem Standard = canonical public explanation of the SigRank family
TTEOP                   = technical interoperability protocol
Ello Control            = knows where all of them actually live
```
