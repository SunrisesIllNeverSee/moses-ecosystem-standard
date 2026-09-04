# SigRank Measurement System

> **Handbook ID**: MOS-HB-SIG-001
> **Authority sources**: SIGRANK-DEF-001
> **Status**: published

## What it is

SigRank is an operator evaluation system that measures AI **operators**
(not models) using telemetry primitives and derived metrics. It is the
measurement layer that operationalizes the Conservation Law's theoretical
foundation.

## What it measures

**Telemetry primitives** (4):
- `input` — tokens consumed
- `output` — tokens produced
- `cache_read` — cache hits
- `cache_write` — cache writes

**Derived metrics** (5):
- **Yield** — output efficiency
- **Leverage** — cache utilization
- **Velocity** — throughput rate
- **SNR** — signal-to-noise ratio
- **10xDEV** — deviation from 10x performance

## Taxonomy (three separate dimensions)

- **Archetype** = shape of the token cascade (convergent, kinetic, builder, etc.)
- **Class** = scale or qualification (NOT total token volume)
- **Rank** = field position relative to reference population

These are SEPARATE concepts. Do NOT redefine Class as total-token volume.

## Evidence level

- **Evidence level**: theoretical (definitions are canonical)
- **Confidence**: medium (empirical validation ongoing)

## What it is NOT

- SigRank evaluates **operators**, not **models**
- SigRank does NOT infer productivity or business outcomes from telemetry
- SigRank does NOT measure intelligence — it measures operator behavior
- Enterprise ideas are NOT automatically public canon

## Protocol

SigRank uses TTEOP (Token Telemetry Evaluation Operator Protocol) as its
sole interoperability protocol. The legacy `sigrank/0.1-draft` wire protocol
identifier remains as a compatibility alias.

## What depends on it

- SignalAF (distributes SigRank-ranked signals)
- The leaderboard (public operator rankings)
- TTEOP (wire protocol)

## References

- SigRank canon: Search Authority `canon/sigrank/canon.yaml`
- TTEOP spec: https://github.com/SunrisesIllNeverSee/tteop-spec
- Framework claim: CT-005 (MO§ES enforces commitment conservation)
