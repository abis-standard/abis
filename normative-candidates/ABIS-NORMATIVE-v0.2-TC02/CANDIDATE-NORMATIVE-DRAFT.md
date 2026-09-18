# ABIS Successor Normative Candidate — REQ-0038 Clarification

**Construction ID:** ABIS-SUCCESSOR-CONSTRUCTION-M236  
**Parent baseline:** ABIS-NORMATIVE-v0.2-TC01 (`drafts/v0.2/`)  
**Status:** CONSTRUCTION / UNVALIDATED  
**NOT NORMATIVE · NOT FROZEN · NOT PROMOTED · NOT PUBLIC**

**Traceability:** RI-001 → CR-PROPOSAL-001 → M-232 → M-233R → M-235 APPROVE_WITH_CONDITIONS

---

## 1. Scope of this candidate

This candidate applies **only** the M-235-approved design basis to REQ-0038 and directly dependent Profile/Preflight/Invoke semantics. All other TC-01 normative content is inherited unchanged from the parent baseline unless explicitly modified herein.

**Authorized change surface:** REQ-0038 and REQ-0038-A through REQ-0038-G, REQ-0038-M, REQ-0038-S, REQ-0038-S2, REQ-0038-N, REQ-0038-E, REQ-0038-F.

---

## 2. Base requirement (unchanged)

> **REQ-0038** (Invoke, MAY): process Invoke without prior Preflight unless the selected Profile explicitly requires Preflight.

---

## 3. Canonical declaration

> **REQ-0038-A** (Profile, MUST): A Profile that requires Preflight before Invoke MUST declare `interaction_constraints.preflight_required` with boolean value `true`.

> **REQ-0038-B** (Profile, MUST NOT): A Profile MUST NOT use `capabilities`, `extensions`, or any encoding other than `interaction_constraints.preflight_required` as the authoritative declaration of Preflight requirement for REQ-0038.

Schema: `schemas/profile/profile.schema.json` — property `interaction_constraints`.

---

## 4. PROFILE_WIDE scope

> **REQ-0038-S** (Profile, MUST): When `preflight_required` is `true`, Preflight is mandatory before Invoke for every entry in `advertised_interactions` and every `execution_class` allowed therein.

> **REQ-0038-S2** (Profile, MUST NOT): A Profile MUST NOT set `preflight_required: true` if any advertised interaction is intended to permit Invoke without Preflight. Heterogeneous Preflight policy MUST use separate Profiles (distinct `profile_kind` or `profile_version`).

Per-interaction override, Profile default + override, and Option D semantics are **not** in scope.

---

## 5. Boolean semantics

| `preflight_required` | Semantics |
| --- | --- |
| `true` | **PREFLIGHT_REQUIRED** |
| `false` | **PREFLIGHT_NOT_REQUIRED** |
| omitted | **PREFLIGHT_NOT_REQUIRED** |

> **REQ-0038-N** (Informative boundary): Preflight RECOMMENDED in lifecycle prose is not a third gating state. UNSUPPORTED Preflight capability is a responder limitation, not a `preflight_required` value.

---

## 6. Interaction Context

**Interaction Context** is the semantic correlation scope within which a recorded `PREFLIGHT_READY` outcome remains authoritative for Invoke admission gating.

Interaction Context is **not** a transport session, HTTP connection, workflow instance, execution-engine state, or provider-specific session identifier.

**CONTEXT_IDENTITY_MINIMUM:**

```
Interaction Context = (profile_binding, preflight_gate_key)

profile_binding = (abis_version, profile_kind, profile_version)
preflight_gate_key = (vertical, operation, execution_class)
```

`profile_binding` identifies the governing Profile revision in effect. `preflight_gate_key` identifies the advertised interaction tuple.

---

## 7. Preflight Gate Record (PGR)

A **Preflight Gate Record** records that `PREFLIGHT_READY` was received for a specific Interaction Context under a governing Profile.

> **REQ-0038-C** (Invoke responder, MUST): When `preflight_required` is `true`, the Invoke responder MUST NOT process an Invoke unless a valid Preflight Gate Record exists for the Invoke's `(profile_binding, preflight_gate_key)`.

> **REQ-0038-C2** (Invoke responder, MUST): A Preflight Gate Record is created only by a conforming Preflight Response with `preflight_state: PREFLIGHT_READY` for the matching `preflight_gate_key` under the current `profile_binding`.

> **REQ-0038-C3** (Invoke responder, MUST): A Preflight Gate Record is invalidated when `profile_version`, `profile_kind`, or `abis_version` of the governing Profile changes.

> **REQ-0038-C4** (Invoke responder, MAY): A valid Preflight Gate Record MAY satisfy multiple Invoke attempts for the same Interaction Context until invalidated per REQ-0038-C3.

> **REQ-0038-D** (Invoke responder, MAY): When `preflight_required` is `false` or `interaction_constraints` is omitted, Invoke MAY proceed without prior Preflight.

**PGR reuse** is approved for candidate construction and future validation. It has **not** been independently validated at M-236.

**Temporal validity:** No ABIS TTL is defined. External changes (availability, price, inventory, authorization, business policy) do not invalidate ABIS PGR. External execution MAY independently reject or fail. PREFLIGHT_READY MUST NOT imply execution or business success (REQ-0007).

---

## 8. Invoke rejection surface

> **REQ-0038-G** (Invoke responder, MUST): When Invoke is blocked for missing or invalid Preflight Gate Record, the Invoke response MUST have `transport_status: ACCEPTED`, `execution_disposition.policy: DENY`, and `execution_disposition.reason: PREFLIGHT_REQUIRED`.

---

## 9. Malformed declaration

> **REQ-0038-M** (Profile consumer, MUST): If `interaction_constraints` is present but `preflight_required` is not a boolean, the Profile MUST be treated as **PROFILE_INVALID**. The consumer MUST NOT derive REQ-0038 gating from that Profile.

**MALFORMED_DECLARATION_OUTCOME:** PROFILE_INVALID (single outcome; no Invoke-time alternate path).

---

## 10. Unsupported required Preflight

When a Profile validly declares `preflight_required: true` but the responder cannot support the required Preflight contract:

- No Preflight Gate Record can be created.
- Invoke without valid PGR MUST be blocked per REQ-0038-C and REQ-0038-G.
- Observable outcome: `PREFLIGHT_REQUIRED` (indistinguishable from missing READY).

This is distinct from **PROFILE_INVALID** (malformed declaration) and from Preflight **NOT_ADVERTISED**.

---

## 11. Canonical authority and legacy

> **REQ-0038-E** (Invoke responder, MUST): REQ-0038 gating MUST be derived only from `interaction_constraints.preflight_required`. Legacy encodings MUST be **IGNORED_FOR_REQ0038**:
>
> - Implementation A: `capabilities.interaction_constraints.preflight_required`
> - Implementation B: vendor extension URI (e.g. `extensions[.../preflight-required]`)

> **REQ-0038-F** (Profile consumer, MUST): If a Profile contains a critical extension without declared capability per REQ-0013, the Profile MUST be treated as **PROFILE_INVALID** regardless of `interaction_constraints`.

**CONFLICT_RULE:** CANONICAL_WINS for REQ-0038 gating.

---

## 12. Declaration processing order

1. Schema validation (`profile.schema.json`)
2. Critical extension validity (REQ-0013 / REQ-0038-F) → PROFILE_INVALID
3. Malformed canonical field (REQ-0038-M) → PROFILE_INVALID
4. Canonical `preflight_required` interpretation
5. Legacy encodings IGNORED_FOR_REQ0038 (REQ-0038-E)
6. Unknown non-critical extensions ignored (REQ-0012)
7. Invoke-time PGR evaluation (REQ-0038-C, C2–C4, G)

---

## 13. ABIS boundary (preserved)

- Capability → Decision → Interaction → Outcome
- Execution / Protocol / Transport = EXTERNAL
- Native Result ≠ Outcome
- Interaction Context is semantic correlation for REQ-0038 gating only
- Profile selection/resolution remains external to ABIS

---

## 14. Inherited TC-01 deltas summary

| TC-01 artifact | Change |
| --- | --- |
| `CONTRACT-PROFILE-PREFLIGHT.md` | Add §1.6 `interaction_constraints`; add REQ-0038-A–F, S, S2, N |
| `INTERACTION-LIFECYCLE.md` | Clarify §3 PGR gating when Profile requires Preflight |
| `schemas/profile/profile.schema.json` | Add optional `interaction_constraints` object |
| `registries/field-registry.json` | Add F-0113 `interaction_constraints` (candidate) |

No other TC-01 artifacts modified in this candidate.
