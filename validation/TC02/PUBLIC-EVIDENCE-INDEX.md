# TC02 Public Evidence Index

**Candidate:** ABIS-NORMATIVE-v0.2-TC02  
**Generated:** 2026-09-18T12:30:00Z  
**Status:** Draft index — artifacts referenced may not yet be public

---

## Purpose

Enable a third party to trace TC02 from candidate identity through validation evidence to Human promotion. References point to repository paths; M-244 does not publish them.

---

## 1. Candidate

| Artifact | Path | Hash / ID |
| --- | --- | --- |
| Promoted candidate (7 files) | `normative-candidates/ABIS-NORMATIVE-v0.2-TC02/` | `85edfa82da4ab90c1e43669d59bed8a811d6ab6aba2ea5b03142170d529f0025` |
| Candidate manifest | `…/CANDIDATE-MANIFEST.json` | per-file in BYTE-IDENTITY-LEDGER |
| Normative draft | `…/CANDIDATE-NORMATIVE-DRAFT.md` | — |
| Schema | `…/CANDIDATE-SCHEMA.json` | — |
| Test vectors | `…/CANDIDATE-TEST-VECTORS.json` | 18 TVs (TV-037–054) |
| Traceability | `…/CANDIDATE-TRACEABILITY.json` | — |
| Migration note | `…/CANDIDATE-MIGRATION-NOTE.md` | RI-001 / TC01→TC02 |
| SLIT design | `…/CANDIDATE-SLIT001R-DESIGN.md` | — |

---

## 2. Validation target (source of promoted bytes)

| Artifact | Path | Hash |
| --- | --- | --- |
| Validation target ID | ABIS-SUCCESSOR-M236-VT01 | — |
| Target snapshot | `validation-packages/M-237/target/` | `85edfa82…f0025` |
| Target manifest | `validation-packages/M-237/VALIDATION-TARGET-MANIFEST.json` | — |
| Validation package | `validation-packages/M-237/` | `69400ef8…f6f84f` |

---

## 3. Construction

| Artifact | Path | Hash |
| --- | --- | --- |
| Construction ID | ABIS-SUCCESSOR-CONSTRUCTION-M236 | `8af02434…b19446` |
| Construction files | `candidate-construction/M-236/` | — |

---

## 4. Independent candidate validation (M-238)

| Artifact | Path | Hash (report) |
| --- | --- | --- |
| Validator ledger | `validation-evidence/M238/VALIDATOR-LEDGER.json` | — |
| V1-openai report | `validation-evidence/M238/V1-openai/EVIDENCE-REPORT.md` | `f1e74477…eba18` |
| V2-anthropic report | `validation-evidence/M238/V2-anthropic/EVIDENCE-REPORT.md` | `3048d74d…f223c` |
| V3-xai report | `validation-evidence/M238/V3-xai/EVIDENCE-REPORT.md` | `054280d7…b9645` |
| Cross-validator synthesis | `validation-evidence/M238/CROSS-VALIDATOR-SYNTHESIS.md` | — |
| Execution matrix | `validation-evidence/M238/EXECUTION-EVIDENCE-MATRIX.json` | 54/54 PASS |

---

## 5. Independent implementations (M-239)

| Artifact | Path | Freeze hash |
| --- | --- | --- |
| Implementation A (Python) | `validation-evidence/M239/implementation-a/` | `8b9a868b…f7d2` |
| Implementation B (JavaScript) | `validation-evidence/M239/implementation-b/` | `b2c0ee09…c827` |
| Freeze ledger | `validation-evidence/M239/FREEZE-LEDGER.json` | — |
| Derivation comparison | `validation-evidence/M239/DERIVATION-COMPARISON.json` | — |

---

## 6. Live interoperability (M-240)

| Artifact | Path | Notes |
| --- | --- | --- |
| SLIT summary | `validation-evidence/M240/SLIT001R-EXECUTION-SUMMARY.json` | 24/24 PASS |
| Directional matrix | `validation-evidence/M240/SLIT001R-DIRECTIONAL-MATRIX.json` | — |
| E4 matrix | `validation-evidence/M240/E4-REQUIREMENT-MATRIX.json` | — |
| Interoperability report | `validation-evidence/M240/M-240-INTEROPERABILITY-REPORT.md` | — |
| RI-001 replay | `validation-evidence/M240/RI001-REPLAY-REPORT.md` | CLOSED_BY_SUCCESSOR_E4 |
| Raw exchanges | `validation-evidence/M240/raw/` | 24 bundles |

---

## 7. Evidence closure & Human governance

| Artifact | Path | Role |
| --- | --- | --- |
| M-241 closure | `governance/M-241/M-241-FINAL-REPORT.txt` | Evidence complete with limitations |
| Limitations | `governance/M-241/SUCCESSOR-LIMITATIONS.json` | 8 limitations |
| RI-001 closure | `governance/M-241/RI001-CLOSURE-REPORT.md` | Audit confirmed |
| M-242 Human review | `governance/M-242-HUMAN-SUCCESSOR-PROMOTION-REVIEW.md` | APPROVE_WITH_CONDITIONS |
| M-243 promotion | `governance/M-243/ABIS-NORMATIVE-v0.2-TC02-PROMOTION-RECORD.md` | TC02 identity bound |
| Promotion metadata | `governance/M-243/CANDIDATE-PROMOTION-METADATA.json` | Freeze + status |
| Evidence binding | `governance/M-243/TC02-EVIDENCE-BINDING.json` | Full chain |
| Hash ledger | `governance/M-243/PROMOTION-HASH-LEDGER.json` | Integrity anchors |

---

## 8. Historical context (TC01)

| Artifact | Path | Hash |
| --- | --- | --- |
| TC01 frozen candidate | `drafts/v0.2/` | `399b328d…736ee` |
| IVP01 package | `validation-packages/ABIS-NORMATIVE-v0.2-TC01-IVP01/` | `311c9fc5…f946` |
| LIT-001 / RI-001 origin | `validation-evidence/TC01/M-231E/`, `M-231F/` | Historical |

---

## 9. M-244 release-readiness (this package)

| Artifact | Path |
| --- | --- |
| Release basis | `governance/M-244/release-basis/` |
| Public validation claims | `TC02-PUBLIC-VALIDATION-CLAIMS.md` |
| Claim boundary | `TC02-RELEASE-CLAIM-BOUNDARY.md` |
| Limitation disclosure plan | `LIMITATION-DISCLOSURE-PLAN.json` |
