# Conservation of Commitment

> **Handbook ID**: MOS-HB-CT-001
> **Authority sources**: CL-DEF-001, CT-001
> **Status**: published

## What it is

The Conservation Law of Commitment is the claim that commitment content —
obligations, prohibitions, and modal constraints — persists under recursive
transformative compression when an enforcement gate is present, and degrades
without one.

**Formal statement**:

> C(T(S)) ≈ C(S) with enforcement; C(T(S)) < C(S) without it

## Why it matters

This is the theoretical foundation for the entire MO§ES ecosystem. If
commitment conservation holds, then governed transformation systems can
preserve meaning across compression cycles. If it doesn't, meaning degrades
with each transformation — which is what happens in ungoverned LLM pipelines.

## Evidence

The law is supported by EXP-001 through EXP-007 (3,950 run entries across
7 experiments). Governed transformation shows 0.94 stability vs 0.42
without enforcement.

**Evidence level**: empirical (proof-of-concept scale)
**Confidence**: medium

## Limitations

- Proof-of-concept scale (20 signals, 100 sentences, 50 code snippets, 25 proofs)
- No cross-model replication yet (Claude, Llama, GPT-4)
- NLI oracle may not be transitive
- Jaccard metric is blind to NP-negation forms (EXP-007)
- 9 failure modes discovered (Formal Collapse, Self-referential Collapse, etc.)

## What would falsify it

1. If F_10(S) < tau for a non-trivial fraction of samples under enforced regime
2. If ungoverned transformation preserves commitment at F_10(S) >= tau

## What depends on it

- MO§ES enforcement architecture (MO-DEF-001)
- SigRank measurement system (SIGRANK-DEF-001)
- The entire governed-compression value proposition

## References

- Conservation Law paper: https://doi.org/10.5281/zenodo.20029607
- Prospectus P-000: https://doi.org/10.5281/zenodo.20031715
- Experimental record: https://doi.org/10.5281/zenodo.19105225
- Framework claim: CT-001, CT-002, CT-003

## What it is NOT

- It is NOT "McHenry's Law" (personal name attribution is prohibited)
- It is NOT a policy or metaphor — it is a falsifiable empirical claim
- It is NOT the same as cryptographic commitment schemes
- It is NOT the same as Conservation of Resources theory
- The harness is NOT the production enforcement implementation
