# Cross-Provider Multi-Outcome — L2 Validation Evidence

**Milestone:** `RND-013C-MILESTONE-CPX-L2`  
**Status:** ACHIEVED / FROZEN  
**Document type:** Experimental validation / R&D evidence summary (public-safe)  
**Validation level:** L2 — Sandbox / Provider-Backed

---

## Scope

This record summarizes **controlled L2 research evidence**. It is **not** part of the ABIS normative specification and does **not** change **ABIS-NORMATIVE-v0.2-TC02**.

**Validated provider surfaces (controlled experiment):**

- Duffel **Test Mode**
- Square **Sandbox**

ABIS R&D used these surfaces in a controlled validation experiment. This document does **not** imply provider endorsement, certification, or universal compatibility.

**Promotion basis (internal governance ID, public reference only):** experiment `RND-013C-CPX-DUF-SQR-001`, **ATTEMPT-5** series.

---

## Objective (plain language)

One higher-level travel-and-payment task required **two independently evaluated business outcomes** from **two independent provider surfaces**: travel arrangement and payment. Each outcome was evaluated on its own evidence; a composite result was determined only after both legs were considered under a predeclared higher-level objective.

Protected implementation details are not disclosed in this public summary.

---

## Results

### CASE-A — positive composition

| Leg | Determination |
| --- | --- |
| Travel arrangement outcome | **MATCH** |
| Payment outcome | **MATCH** |
| **Composite** | **CBX_SATISFIED** |

### CASE-B — execution success vs outcome success

| Item | Result |
| --- | --- |
| Provider-side execution | **Successful** on both legs |
| Travel arrangement outcome | **MATCH** |
| Payment outcome | **MISMATCH** |
| **Composite** | **CBX_NOT_SATISFIED** |

**Key observation:** `EXECUTION_SUCCESS_OUTCOME_MISMATCH` — both provider-side executions can complete successfully while the requested business outcome as a whole is still **not** satisfied.

### CASE-C — partial evaluation safety

| Leg | Determination |
| --- | --- |
| Travel arrangement outcome | **MATCH** |
| Payment outcome | **NOT_EVALUATED** (payment leg intentionally not executed) |
| **Composite** | **CBX_NOT_EVALUABLE** |

When a required provider leg is intentionally not evaluated, the evaluation preserves that absence rather than treating the overall task as successful.

---

## Established claim (bounded)

| Claim | Status |
| --- | --- |
| **CROSS_PROVIDER_MULTI_OUTCOME** | **ESTABLISHED_AT_L2_WITHIN_VALIDATED_SCOPE** |
| **MULTI_PROVIDER_REPRODUCIBILITY** (separate 3-provider L2 milestone) | **ESTABLISHED_AT_L2_WITHIN_VALIDATED_SCOPE** |

These claims apply only to the stated **L2 sandbox/test-mode** research scope.

---

## Limitations (accepted)

- Validation was conducted in **controlled Test Mode / Sandbox** environments only.
- This is **not** production validation or real-world multi-outcome validation.
- This does **not** establish universal provider compatibility.
- Evidence packaging has known limitations (for example, per-leg raw integrity tooling gaps on one provider leg in the internal audit); conclusions remain bounded to the audited ATTEMPT-5 series.
- **No provider endorsement** is implied.

---

## What this evidence does **not** establish

- Production validation  
- Real-world Multi-Outcome validation  
- L3 validation (**L3: NOT AUTHORIZED**)  
- Certification  
- ABIS conformance by the providers  
- Provider endorsement  
- Universal provider compatibility  

---

## Related public materials

| Resource | Link |
| --- | --- |
| ABIS public specification repository | [github.com/abis-standard/abis](https://github.com/abis-standard/abis) |
| ABIS Reference Runtime | [github.com/abis-standard/abis-reference-runtime](https://github.com/abis-standard/abis-reference-runtime) |
| ABIS validation (website) | [abis.coaretail.com/ja/validation](https://abis.coaretail.com/ja/validation) |
| TC02 validation evidence (separate program) | [validation/TC02/](../TC02/) |

**ABIS-NORMATIVE-v0.2-TC02:** unchanged by this milestone.
