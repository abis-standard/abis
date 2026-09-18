# TC02 Technical Change Summary (TC01 → TC02)

**Candidate:** ABIS-NORMATIVE-v0.2-TC02  
**Parent:** ABIS-NORMATIVE-v0.2-TC01  
**Root issue:** RI-001 — REQ-0038 preflight declaration underspecification  
**Generated:** 2026-09-18T12:30:00Z  
**Status:** Public-safe draft — NOT AUTHORIZED

---

## Why TC02 exists

TC01 validation (LIT-001) showed that two independent implementations could reach **different REQ-0038 gating decisions** for the same Profile because `preflight_required` had no canonical representation. RI-001 recorded this as a specification gap, not an implementation defect alone.

TC02 introduces successor normative semantics and validation evidence to close RI-001 under tested scope.

---

## Primary technical changes

### 1. Canonical preflight declaration (REQ-0038-A)

**TC01:** No canonical `preflight_required` field in profile schema.  
**TC02:** `interaction_constraints.preflight_required` (boolean) is the authoritative declaration.

- `true` → PREFLIGHT_REQUIRED (PROFILE_WIDE)
- `false` or omitted → PREFLIGHT_NOT_REQUIRED
- Non-boolean when `interaction_constraints` present → PROFILE_INVALID

### 2. Legacy encoding treatment (REQ-0038-E)

Historical Implementation A (`capabilities.interaction_constraints.preflight_required`) and Implementation B (extension URI) encodings are **IGNORED_FOR_REQ0038**. Only the canonical path governs successor semantics.

### 3. Interaction Context & PGR model (REQ-0038-C family)

TC02 adds normative PGR (Preflight Gate Record) semantics:

- Invoke blocked without valid PGR when preflight required (REQ-0038-C)
- PGR created only by PREFLIGHT_READY (REQ-0038-C2)
- PGR invalidated on profile_binding change (REQ-0038-C3)
- PGR reuse within same Interaction Context (REQ-0038-C4)

### 4. DENY surface & scope (REQ-0038-G, REQ-0038-S)

Explicit DENY behavior for missing PGR and PROFILE_WIDE preflight scope when `preflight_required` is true.

### 5. Unsupported-required behavior (REQ-0038-F area)

Critical extensions without capability → PROFILE_INVALID (E3 evidence; not separately exercised in M-240 SLIT).

### 6. Validation expansion

- 18 successor test vectors (TV-037–054) — M-238: 54/54 PASS across 3 validators
- SLIT-001R: 12 phases × 2 directions = 24/24 PASS — M-240
- Two new independent implementations frozen before cross-test — M-239

---

## What did not change

- TC01 frozen bytes and historical evidence
- Public v0.1 Concept & Architecture materials at repository root
- Certification status (none)
- Claim that all REQ-0038 sub-requirements reached E4

---

## Sub-requirements not reaching E4 in TC02

REQ-0038-B, REQ-0038-D, REQ-0038-F, REQ-0038-M, REQ-0038-S2 — various E3 or partial coverage only. REQ-0038-N remains E1 (informative) only.

See `TC02-PUBLIC-VALIDATION-CLAIMS.md` for claim boundaries.
