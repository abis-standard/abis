# Candidate Migration Note — REQ-0038 Preflight Declaration

**Construction ID:** ABIS-SUCCESSOR-CONSTRUCTION-M236  
**Status:** INFORMATIVE (unless explicitly designated normative elsewhere)  
**NOT NORMATIVE · NOT FROZEN · NOT PROMOTED · NOT PUBLIC**

---

## 1. TC-01 historical behavior

Under frozen TC-01 (`ABIS-NORMATIVE-v0.2-TC01`):

- REQ-0038 states Invoke MAY proceed without prior Preflight unless the selected Profile explicitly requires Preflight.
- `profile.schema.json` does **not** define a canonical `preflight_required` field.
- M-231E LIT-001 demonstrated bidirectional REPRESENTATION_DIVERGENCE between frozen implementations.

---

## 2. Implementation A historical representation

**Encoding:** `capabilities.interaction_constraints.preflight_required` (boolean)

**Successor treatment:** **IGNORED_FOR_REQ0038**

Implementation A encoding does not define successor REQ-0038 semantics. Publishers MUST add canonical `interaction_constraints.preflight_required` to declare requirement.

---

## 3. Implementation B historical representation

**Encoding:** `extensions["https://example.test/abis/ext/interaction/preflight-required"]` (or vendor URI variant)

**Successor treatment:** **IGNORED_FOR_REQ0038**

Implementation B encoding does not define successor REQ-0038 semantics.

---

## 4. Successor canonical representation

```json
"interaction_constraints": {
  "preflight_required": true
}
```

- `true` → PREFLIGHT_REQUIRED (PROFILE_WIDE)
- `false` or omitted → PREFLIGHT_NOT_REQUIRED
- Non-boolean when `interaction_constraints` present → PROFILE_INVALID

---

## 5. Migration steps (informative)

1. Identify Profiles currently using A or B legacy encodings.
2. Add `interaction_constraints.preflight_required` with intended boolean value.
3. Remove reliance on legacy encodings for REQ-0038 gating (legacy MAY remain in document but is ignored).
4. If heterogeneous Preflight policy exists within one Profile, split into separate Profiles per REQ-0038-S2.
5. Re-verify with SLIT-001R (or successor) after candidate validation.

---

## 6. Backward compatibility

| Aspect | Risk |
| --- | --- |
| Legacy-only Profiles | MEDIUM — treated as PREFLIGHT_NOT_REQUIRED until canonical field added |
| PROFILE_WIDE lock | MEDIUM — may require Profile splits |
| PGR semantics | New normative addition — implementations must adopt PGR model |

---

## 7. LIT-019 limitation (retained)

Initial execution INCONCLUSIVE; raw not preserved; harness/fixture fix only; Implementation A/B unchanged; rerun PASS; VALID_WITH_LIMITATION.
