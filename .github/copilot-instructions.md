# Copilot instructions — ABIS Public Specification repository

These instructions are repository-scoped guidance for AI coding assistants working **in this repository only** (`abis-standard/abis`). They do not apply to other repositories, and they do not change the ABIS specification.

## What this repository is

- **ABIS — Agent Business Interaction Standard** (singular: "Standard").
- **Public v0.1 — Concept & Architecture Release** (Public / Non-Normative / Open for Review), plus the Normative Candidate **ABIS-NORMATIVE-v0.2-TC02** in `normative-candidates/`. TC02 is a candidate, not a final normative release or a certification release. Do not restate or upgrade its status.
- Validation and R&D evidence in `validation/` records what was demonstrated within a stated scope. It is not normative.
- The ABIS Reference Runtime (`abis-standard/abis-reference-runtime`) is a separate, non-normative implementation. It is not the source of ABIS semantics.

## Outcome semantics to preserve

- **Execution success ≠ outcome success.** This repository's terms are *Technical Success* and *Business Success* ([TERMINOLOGY.md](../TERMINOLOGY.md)).
- An HTTP 200, a completed tool call, or a provider's own success status is **not** a satisfied Business Outcome.
- Compare the **observed** business result with the **intended** business result. Never assume they match.
- Technical signals (request accepted, HTTP 200, tool completed) are not business outcomes. ABIS does not define how to map technical signals to business outcomes ([docs/business-outcome.md](../docs/business-outcome.md)).
- Preserve evidence provenance: keep track of which system produced an observation and in which environment (for example, L2 sandbox / test mode). Do not merge, rewrite, or upgrade evidence.
- Do not infer whole-job (**Composite Outcome**) success from individual successful operations or from some outcomes matching.
- Preserve `NOT_EVALUATED` exactly. Never turn it into success or failure. The published R&D summary reports `CBX_NOT_SATISFIED` and `CBX_NOT_EVALUABLE` as distinct results for specific cases. Keep them distinct, and do not generalize those cases into composition rules. These `CBX_*` labels are R&D evidence labels, not normative ABIS terms.
- Never fabricate provider evidence, API responses, identifiers, run IDs, or validation results.

## Normative and governance boundaries

- Do not edit `normative-candidates/`, `releases/`, or frozen evidence under `validation/` unless a maintainer explicitly asks.
- Non-normative files (README, docs, examples, this file) cannot change normative requirements.
- Do not claim production validation, real-world validation, L3 validation, certification, conformance, provider endorsement, universal provider compatibility, or official integration with MCP, A2A, or any other protocol. Certification is not available in v0.1.
- Describe ABIS as **complementing** MCP, A2A, REST APIs, and other execution mechanisms. Never say it replaces them.
- Follow the disclosure boundary in [public-allowlist.yml](../public-allowlist.yml) (unknown material is not public). Do not add private implementation detail, internal schemas or test vectors, local file paths, secrets, or algorithms or decision logic for abstract concepts. See [CONTRIBUTING.md](CONTRIBUTING.md).
- Avoid unsupported claims such as "world first", "only ABIS can", or "industry standard".
- Rights and availability are described in [NOTICE](../NOTICE). Do not add license claims.
