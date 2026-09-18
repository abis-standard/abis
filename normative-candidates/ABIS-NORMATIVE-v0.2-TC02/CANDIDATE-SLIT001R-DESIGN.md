# CANDIDATE SLIT-001R — Successor Interoperability Test Design

**Construction ID:** ABIS-SUCCESSOR-CONSTRUCTION-M236  
**Status:** CONSTRUCTION / UNVALIDATED — NOT EXECUTED  
**Parent design:** `governance/M-233R/M-233R-SLIT001R-DESIGN.md`  
**Normative reference:** `candidate-construction/M-236/CANDIDATE-NORMATIVE-DRAFT.md`  
**Schema reference:** `candidate-construction/M-236/CANDIDATE-SCHEMA.json`

---

## Purpose

Verify that two independently implemented successors converge on all REQ-0038 semantic decisions including Interaction Context persistence, invalidation, and PGR reuse.

---

## Preconditions

1. Two independent implementations (X, Y) — not frozen A/B.
2. Canonical Profile per `CANDIDATE-SCHEMA.json` with `interaction_constraints.preflight_required: true`.
3. Multi-interaction Profile fixture (TV-047 base).
4. Normative input: `CANDIDATE-NORMATIVE-DRAFT.md` only.

---

## Phases

| Phase | Action | Expected convergence | TV reference |
| --- | --- | --- | --- |
| **1** | Parse canonical Profile | PROFILE_VALID | TV-037 |
| **2** | Derive preflight-required state | PREFLIGHT_REQUIRED | TV-037 |
| **3** | Invoke before READY (tuple A) | ACCEPTED + DENY + PREFLIGHT_REQUIRED | TV-039 |
| **4** | Preflight tuple A → PREFLIGHT_READY | PGR created | TV-040 |
| **5** | Invoke tuple A with valid PGR | Invoke evaluation permitted | TV-040 |
| **5b** | Second Invoke tuple A same context (PGR reuse) | Invoke evaluation permitted without new Preflight | TV-052 |
| **6** | Invoke tuple B with only tuple A PGR | PREFLIGHT_REQUIRED | TV-049 |
| **7** | Bump `profile_version`; Invoke tuple A with old PGR | PREFLIGHT_REQUIRED | TV-048 |
| **8** | Re-Preflight tuple A; Invoke succeeds | Invoke evaluation permitted | TV-040 |
| **9** | Canonical `true` + legacy capability `false` | PREFLIGHT_REQUIRED; legacy IGNORED | TV-044 pattern |
| **10** | Failed Invoke; second Invoke same context | PGR remains valid | TV-053 |
| **11** | Unsupported Preflight responder | PREFLIGHT_REQUIRED at Invoke | TV-051 |

Phase 5b added per M-235 RRF-002 disposition.

---

## Directions

- X → Y and Y → X (both required)

---

## Pass condition

**PASS** if and only if all phases produce identical normative semantic outcomes per `CANDIDATE-NORMATIVE-DRAFT.md` and failure semantics matrix (inherited from M-233R).

---

## Execution status

**NOT EXECUTED** — candidate construction only.
