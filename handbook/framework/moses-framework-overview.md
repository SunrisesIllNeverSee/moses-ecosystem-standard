# MO§ES Framework Overview

> **Handbook ID**: MOS-HB-FWK-001
> **Authority sources**: MO-DEF-001
> **Status**: published

## What it is

The MO§ES Framework is the formal framework that defines the ontology, laws,
and epistemic states underlying the MO§ES ecosystem. It lives in
`moses-framework/` and contains:

- **Claims registry** — 27 formal claims with epistemic states
- **Ontology** — definitions, primitives, relations
- **Intelligence taxonomy** — BI, AAI, SI classification
- **Intelligence Provenance** — tracing intelligence-bearing events
- **Measurement** — Micro Evals and evaluation framework
- **Prior art** — novelty and collision analysis

## Epistemic states

The Framework preserves its own epistemic states, which are SEPARATE from
Search Authority approval states:

| State | Meaning |
|-------|---------|
| DEFINED | True by construction (not empirical) |
| DERIVED | Follows logically from definitions |
| OBSERVED | Empirical support, not yet replicated |
| SUPPORTED | Replicated or scaled evidence |
| HYPOTHESIS | Testable, insufficient evidence |
| SPECULATIVE | Not yet testable |
| EXTERNAL | From external literature |

**Critical**: Framework status ≠ Search Authority status.
A claim can be DEFINED in the Framework and disputed in Search Authority.
Both states coexist and are both valid.

## Claim families

| Prefix | Domain | Count |
|--------|--------|-------|
| CT- | Commitment Theory core | 10 |
| INT- | Intelligence taxonomy | 6 |
| IP- | Intelligence Provenance | 3 |
| CONN- | Connection claims | 3 |
| PA- | Prior-art claims | 3 |
| MEAS- | Measurement claims | 2 |

## What it is NOT

- The Framework is NOT canonical truth — Search Authority is
- The Framework does NOT promote its claims to owner-approved status
- The Framework does NOT replace Search Authority's approval ledger
- The Framework's epistemic states are NOT collapsed into confidence levels

## References

- Framework repo: https://github.com/SunrisesIllNeverSee/moses-framework
- Claims registry: `claims/claims-registry.yaml`
- Ontology: `ontology/definitions.yaml`, `ontology/primitives.yaml`, `ontology/relations.yaml`
- Conservation Law paper: https://doi.org/10.5281/zenodo.20029607
