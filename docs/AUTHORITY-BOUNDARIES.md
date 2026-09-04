# Authority Boundaries

What the MO§ES Ecosystem Standard can and cannot say.

---

## What this standard owns

This standard is the **canonical public architecture and reference
standard** for the entire MO§ES ecosystem. It owns:

- **Ecosystem architecture** — the overall structure of the MO§ES
  ecosystem, how components relate, and what roles they play.
- **Component roles** — the classification of each component (framework,
  standard, protocol, product, platform, transport, tool, research, site,
  legacy, governance, infrastructure) and its primary role (authority,
  implementation, transport, projection, reference, evidence_source,
  legacy_source).
- **Relationships** — how components relate to each other within the
  ecosystem (authority chains, family memberships, protocol dependencies).
- **Public reference** — the canonical public overview that any external
  party can consult to understand the MO§ES ecosystem without
  reconstructing it from individual components.

This standard is a **governed public projection** of the Search Authority
master canon. It does not independently invent canonical truth. Every
claim traces to Search Authority.

---

## What this standard does NOT own

### Framework ontology

The MO§ES Framework owns the formal ontology, methodology, claims, laws,
epistemic states, and framework structure. This standard **references**
the framework; it does not redefine or re-interpret it.

- **Lives at:** https://github.com/SunrisesIllNeverSee/moses-framework
- **Reference:** [references/moses-framework.yaml](../references/moses-framework.yaml)

### Protocol semantics

TTEOP owns the measurement protocol semantics — the four telemetry
primitives (I/O/W/R), five derived metrics, telemetry envelope schema,
privacy modes, provenance levels, and conformance tests. This standard
says "TTEOP is the measurement protocol used here." It does not copy the
metric specification.

- **Lives at:** https://github.com/SunrisesIllNeverSee/otep-spec
- **Reference:** [references/tteop.yaml](../references/tteop.yaml)

### Product implementation

Each product owns its own implementation details. SignalAF, SigRank,
Upsilon, Signomy, CIVITAE, and other products define their own behavior
and extensions within the boundaries set by this standard. This standard
does not contain product source code.

### Internal canon structure

Search Authority owns its internal canon structure — how canon records
are stored, indexed, and governed internally. This standard projects
canon content publicly but does not replicate Search Authority's internal
organization.

- **Lives at:** private repository
- **Reference:** [references/search-authority.yaml](../references/search-authority.yaml)

---

## The clean distinction table

| Authority | What it is | What it owns | What it does NOT own |
|-----------|-----------|--------------|----------------------|
| **Search Authority** | Canonical truth database | All canonical truth: names, descriptions, relationships, approved public claims, terminology, entity identity, authority assignments | Public presentation, ecosystem architecture framing |
| **MO§ES Ecosystem Standard** (this standard) | Public explanation of the ecosystem | Ecosystem architecture, component roles, relationships, public reference | Framework ontology, protocol semantics, product implementation, internal canon structure |
| **MO§ES Framework** | Formal claims | Ontology, methodology, claims, laws, epistemic states, framework structure | Ecosystem architecture, protocol semantics, product behavior |
| **TTEOP** | Protocol | Token telemetry measurement protocol: primitives, metrics, envelope schema, privacy modes, provenance levels, conformance tests | Ecosystem architecture, framework claims, product implementation |
| **Ello Control** | Operational identity | repo_id, current repo/location, lifecycle, implementation relationship, deployment mapping | Canonical truth, framework claims, protocol semantics |

### Authority chain

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

Search Authority supplies approved canonical truth. This standard projects
it publicly. The MO§ES Framework supplies formal references. TTEOP supplies
protocol specifications. Ello Control supplies operational identity (where
things actually live).

---

## Information source authority levels

Not all information sources have the same authority. From highest to lowest:

### Level 1: Search Authority (master canon)

The sole master canon owner. All canonical truth derives from here. No
other source may independently invent canonical truth. Disputed claims in
Search Authority remain disputed in this standard — this standard does not
resolve them.

### Level 2: Canonical source authorities

- **MO§ES Framework** — canonical source for ontology, methodology, claims,
  and laws (`authority_class: canonical_source`).
- **TTEOP** — sole protocol specification authority for token telemetry
  measurement (`authority_class: protocol_specification`).

These are independently authoritative within their domains. This standard
references them but does not redefine them.

### Level 3: Public projection

- **This standard** — public projection of the master canon
  (`authority_class: public_projection`).
- **mos2es.com** — public site for MO§ES™.

Public projections present canonical truth publicly but do not create it.

### Level 4: Product implementation

- **SignalAF, SigRank, Upsilon** — products that implement and extend
  canonical truth within boundaries (`authority_class: product_implementation`).
- Products own their behavior and extensions but may not redefine protocol
  semantics, framework claims, or ecosystem authority.

### Level 5: Transport

- **tteop-mcp** — MCP transport over TTEOP (`authority_class: transport`).
- Transport layers provide access without defining semantics.

### Level 6: Legacy compatibility

- **sigrank-standard** — legacy predecessor, retained for compatibility
  (`authority_class: legacy_compatibility_source`).
- Legacy sources must not be presented as current standards.

### Level 7: Operational identity

- **Ello Control** — knows where components live
  (`authority_class: operational_identity`).
- Operational identity is not canonical truth. Ello Control knows where
  things live; it does not define what they mean.

---

## Governance rules

These rules come from Search Authority and apply to all authority-sensitive
material in this standard:

- Exactly ONE MO§ES entity. Never duplicate it.
- Canonical display: MO§ES™. Accepted prose: MO§ES. Aliases: mos2es, MOSES.
- Never render: MO§E§ or MO§E§™.
- Do NOT collapse Signomy and CIVITAE.
- SigRank evaluates AI operators, not AI models.
- The harness may measure authority, but it cannot manufacture authority.
- Automated systems may not promote claims into owner-approved truth.
- Archetype = shape. Class = scale/qualification. Rank = field position.
