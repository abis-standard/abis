# TC02 Release Notes — INTERNAL DRAFT

> **STAGED — NOT YET PUBLISHED**  
> Public release of ABIS-NORMATIVE-v0.2-TC02 has **not** been authorized (M-242, M-243, M-244).

---

## Candidate identity

| Field | Value |
| --- | --- |
| **Candidate ID** | ABIS-NORMATIVE-v0.2-TC02 |
| **Status** | FORMAL NORMATIVE CANDIDATE |
| **Validation** | VALIDATED_WITH_LIMITATIONS |
| **Freeze** | FROZEN |
| **Hash** | `85edfa82da4ab90c1e43669d59bed8a811d6ab6aba2ea5b03142170d529f0025` |
| **Parent** | ABIS-NORMATIVE-v0.2-TC01 |

---

## What changed (summary)

TC02 addresses **RI-001**: REQ-0038 preflight declaration interoperability.

Key successor changes:

- Canonical `interaction_constraints.preflight_required` boolean declaration
- Legacy encodings ignored for REQ-0038 gating
- Interaction Context and PGR (Preflight Gate Record) semantics
- Expanded test vectors and SLIT-001R live interoperability evidence

See `TC02-CHANGE-SUMMARY.md` for technical detail.

---

## Why it changed

TC01 LIT-001 demonstrated bidirectional representation divergence between independent implementations for the same Profile — root cause: REQ-0038 underspecification. Successor design (OPTION C revised, M-233R) was Human-approved (M-235) and validated through M-240.

---

## Validation evidence

| Evidence | Result |
| --- | --- |
| 3 independent validators (M-238) | 54/54 PASS |
| 2 independent implementations (M-239) | 18/18 local TVs each; frozen |
| SLIT-001R live interop (M-240) | 24/24 PASS |
| RI-001 | CLOSED_BY_SUCCESSOR_E4 |
| E4 (scoped) | 10 requirement axes established |

**This is not certification or production validation.**

---

## Known limitations

8 limitations retained (7 ACCEPTED, 1 ACCEPTED_WITH_FUTURE_ACTION):

- E4 not entire candidate surface (LIM-001)
- Controlled test implementations only (LIM-002)
- No transport/protocol validation (LIM-003)
- **No public third-party implementation interoperability (LIM-004)**
- Historical LIT-019 limitation on TC01 first-run evidence (LIM-006)
- REQ-0038-D/F/M not in M-240 SLIT (LIM-007)
- REQ-0038-N informative only (LIM-008)

Full plan: `LIMITATION-DISCLOSURE-PLAN.json`

---

## Relationship to TC01

TC01 remains **FROZEN / VALIDATED_WITH_KNOWN_LIMITATION**. TC02 is the authorized successor candidate. TC01 is not invalid or deleted.

See `TC01-TC02-PUBLIC-LINEAGE.md`.

---

## Relationship to Public v0.1

Public v0.1 (Concept & Architecture Release) at repository root is **unchanged**. TC02 publication does not automatically change Public v0.1 version numbering. Human decision required (M-244 Q7).

---

## Evidence links (placeholders)

| Resource | Location |
| --- | --- |
| Candidate files | `[TBD: public path if authorized]` |
| Validation summary | `TC02-VALIDATION-SUMMARY.md` |
| Evidence index | `TC02-PUBLIC-EVIDENCE-INDEX.md` |
| Claim boundary | `TC02-RELEASE-CLAIM-BOUNDARY.md` |
| Promotion record | `governance/M-243/ABIS-NORMATIVE-v0.2-TC02-PROMOTION-RECORD.md` |

---

## Authorization status

| Field | Value |
| --- | --- |
| PUBLIC_RELEASE_STATUS | STAGED_NOT_PUBLISHED |
| CERTIFICATION_AUTHORIZED | NO |
| NORMATIVE_FINAL_STANDARD_AUTHORIZED | NO |
