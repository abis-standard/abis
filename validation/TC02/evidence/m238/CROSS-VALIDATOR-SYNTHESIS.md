# M-238 Cross-Validator Synthesis

**Generated:** 2026-09-18T11:18:01Z

## Validator summary

| Validator | Provider | Verdict | Report SHA-256 |
| --- | --- | --- | --- |
| V1-openai | OpenAI | PASS_WITH_FINDINGS | f1e744770a217561ceb5d4405df2a8b6990e4ee938f0f82d1561a1e4ca6eba18 |
| V2-anthropic | Anthropic | PASS_WITH_FINDINGS | 3048d74dfbf8c7c6e209377ae939cceb3272b8449dba48acd7dfd0689bbf223c |
| V3-xai | xAI | PASS_WITH_FINDINGS | 054280d74a72fd8792d2076837238c168d5e57f47aaf565580090a92917b9645 |

## Semantic derivation agreement

All three validators independently derived identical semantics from `target/CANDIDATE-NORMATIVE-DRAFT.md`:

- Canonical path: `interaction_constraints.preflight_required` (boolean)
- Omission → `PREFLIGHT_NOT_REQUIRED`
- `false` → `PREFLIGHT_NOT_REQUIRED`
- Malformed non-boolean → `PROFILE_INVALID` (REQ-0038-M)
- Legacy A/B representations → `IGNORED_FOR_REQ0038`
- Critical extension without capability → `PROFILE_INVALID`
- Interaction Context: `(profile_binding, preflight_gate_key)`
- PGR reuse within same context; invalidation on version/tuple mismatch
- Unsupported required Preflight → `ACCEPTED + DENY + PREFLIGHT_REQUIRED`

## TV execution matrix

All 18 TVs (TV-037–TV-054) **ACTUALLY_EXECUTED** by all three validators with **PASS** verdicts.
See `EXECUTION-EVIDENCE-MATRIX.json`.

## Dimension cross-validator results

| Dimension | Result |
| --- | --- |
| RRF-002 (PGR reuse) | PASS |
| RRF-003 (unsupported required) | PASS |
| Interaction Context | PASS |
| Malformed declaration | PASS |
| Legacy conflict | PASS |
| Critical extension | PASS |
| Schema/text | PASS |
| ABIS boundary | PASS |
| SLIT-001R | READY_FOR_FUTURE_EXECUTION |

## Evidence levels

| Level | Established | Basis |
| --- | --- | --- |
| E1 | YES | Static normative/schema review (all validators) |
| E2 | YES | jsonschema structural validation |
| E3 | YES | Package-bound semantic evaluator execution (all TVs, all validators) |
| E4 | NO | No cross-independent-implementation interoperability |

## Normalized findings

- **CVF-001** (INFORMATIONAL, REPLICATED): Package-bound evaluator only — not live responder
- **CVF-002** (INFORMATIONAL, REPLICATED): E4 not claimable from validator agreement

## LIT-019

Retained unchanged: initial INCONCLUSIVE; raw NOT PRESERVED; harness/fixture fix only; A/B UNCHANGED.

## Protected artifacts

- TC-01 unchanged: YES
- IVP01 unchanged: YES
- M-236 construction hash: verified
- M-237 validation target/package: verified

## Cross-validator candidate result

**VALIDATED_WITH_FINDINGS_FOR_NEXT_INTEROP_STAGE**

Non-blocking informational findings only (E3 limitation, no E4). No material candidate defect demonstrated.
