# MO§ES Ecosystem Handbook

> Long-form explanatory knowledge for the MO§ES ecosystem.
> The handbook **explains** canon. It does not **create** canon.
> Authority source: Search Authority.

## Purpose

The handbook provides deeper explanatory context beneath the MO§ES Ecosystem
Standard. Where the Standard defines the public architecture, the handbook
explains *why* things are the way they are, *how* they work, and *what* the
evidence supports.

## Authority boundary

- The handbook is **explanatory**, not **canonical**.
- Every handbook entry traces to Search Authority or a research repository.
- The handbook never independently invents canonical truth.
- If Search Authority and the handbook disagree, Search Authority wins.

## Structure

```
handbook/
├── README.md          — this file
├── index.yaml         — stable ID registry
├── foundations/       — core concepts and definitions
├── framework/         — MO§ES Framework explanation
├── measurement/       — SigRank and measurement systems
├── governance/        — authority and governance architecture
├── products/          — product families (SignalAF, KASSA, etc.)
├── protocols/         — TTEOP and other protocols
├── research/          — Conservation Law and research programs
├── implementation/    — practical implementation guides
└── reference/         — reference material (glossaries, ID maps)
```

## Stable IDs

Each handbook entry has a stable ID:

- `MOS-HB-CT-###` — Conservation Theory / Conservation Law
- `MOS-HB-GOV-###` — Governance and authority
- `MOS-HB-SIG-###` — SigRank and measurement
- `MOS-HB-FWK-###` — MO§ES Framework
- `MOS-HB-PROD-###` — Products
- `MOS-HB-PROTO-###` — Protocols
- `MOS-HB-RES-###` — Research
- `MOS-HB-IMPL-###` — Implementation
- `MOS-HB-REF-###` — Reference

IDs are stable and never reused. If an entry is retired, its ID is retired.

## Entry format

Each handbook entry includes:

```yaml
id: MOS-HB-CT-001
title: Conservation of Commitment
status: published
authority_source:
  - CL-DEF-001
  - CT-001
references:
  - DOI:10.5281/zenodo.20029607
related_entities:
  - conservation_law_of_commitment
  - commitment_theory
```

## Current state

Phase 5 (initial build) — test subset entries created:
- MOS-HB-CT-001 — Conservation of Commitment
- MOS-HB-GOV-001 — MO§ES Governance Architecture
- MOS-HB-SIG-001 — SigRank Measurement System
- MOS-HB-FWK-001 — MO§ES Framework Overview
