# TC01 → TC02 Public Lineage

**Generated:** 2026-09-18T12:30:00Z  
**Audience:** Public release materials (draft — NOT AUTHORIZED)

---

## Lineage (public-safe)

```
ABIS-NORMATIVE-v0.2-TC01
  historical frozen normative candidate
  VALIDATED_WITH_KNOWN_LIMITATION
        │
        │  successor design & revalidation cycle
        │  (RI-001 → REQ-0038 clarification)
        ▼
ABIS-NORMATIVE-v0.2-TC02
  successor formal normative candidate
  VALIDATED_WITH_LIMITATIONS
  FROZEN
```

---

## TC01 — historical candidate

| Field | Public-safe description |
| --- | --- |
| **Identity** | ABIS-NORMATIVE-v0.2-TC01 |
| **Status** | FROZEN / VALIDATED_WITH_KNOWN_LIMITATION |
| **Role** | Historical validated candidate that established the v0.2 validation methodology |
| **Known limitation** | REQ-0038 preflight declaration allowed representation divergence (RI-001 / LIT-001) |

**Do not describe TC01 as:** invalid, withdrawn due to failure, deleted, replaced evidence, or a failed standard.

TC01 bytes and evidence remain preserved and authoritative for their historical scope.

---

## TC02 — successor candidate

| Field | Public-safe description |
| --- | --- |
| **Identity** | ABIS-NORMATIVE-v0.2-TC02 |
| **Status** | FORMAL NORMATIVE CANDIDATE / VALIDATED_WITH_LIMITATIONS / FROZEN |
| **Addresses** | RI-001 through canonical `interaction_constraints.preflight_required`, Interaction Context, and PGR semantics |
| **Evidence** | M-238 (candidate TVs), M-239 (implementations), M-240 (SLIT-001R), M-241–M-243 (closure & promotion) |

TC02 does **not** retroactively modify TC01. TC02 is **not** a final public normative standard unless separately authorized.

---

## Relationship to Public v0.1

| Layer | Identity | Role |
| --- | --- | --- |
| **Public v0.1** | Repository root Concept & Architecture Release | Informative framework; unchanged by TC02 promotion |
| **Normative candidate TC01** | `drafts/v0.2/` (frozen) | Historical v0.2 candidate cycle |
| **Normative candidate TC02** | `normative-candidates/ABIS-NORMATIVE-v0.2-TC02/` | Successor candidate cycle |

Public wording for version relationship requires **Human decision** (M-244 Q7).
