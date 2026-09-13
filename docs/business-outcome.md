# Business Outcome

**Version:** Public v0.1

---

## Definition

A **Business Outcome** is the business-meaningful result of a Business Interaction — described in terms that matter to the business actor, not only to the execution layer.

---

## Intended vs observed

ABIS is designed to support distinguishing:

| Dimension | Question |
| --- | --- |
| **Intended** | What did the business actor expect? |
| **Observed** | What was actually achieved in business terms? |

Technical success — such as a completed tool call or successful API response — does not by itself answer whether the intended business outcome was achieved.

---

## Example outcome states (conceptual)

The following are **illustrative business descriptions**, not normative enums or schemas:

| State (conceptual) | Meaning |
| --- | --- |
| Confirmed | Business request accepted as specified |
| Pending | Business request received but not yet finalized |
| Rejected | Business request declined |
| Fulfilled | Business obligation completed |
| Unknown | Business result not yet determinable |

Public v0.1 does not mandate these labels or define how they are determined.

---

## Why this matters

Business stakeholders evaluate success in business terms:

- Was the reservation at the requested time and party size?
- Was the correct product delivered to the correct address?
- Was the application registered with the correct case reference?

Agents and platforms that report only technical success can create a false sense of completion. ABIS is designed to support an explicit, shared concern for business outcome representation in interoperability discussions.

---

## Relationship to technical signals

```text
Technical layer          Business layer
─────────────────        ─────────────────
Request accepted    ≠    Reservation confirmed at requested conditions
HTTP 200            ≠    Order fulfilled as specified
Tool completed      ≠    Application registered correctly
```

ABIS does not define how to map technical signals to business outcomes. That mapping is a separate concern that may involve business rules, system-specific interpretation, and human review.

---

## Abstract related concepts

Future public work may address — at a conceptual level only in v0.1:

- whether different observed results represent the same business outcome (outcome equivalence as a problem area)
- outcomes that span multiple systems (cross-system outcome as a problem area)
- outcomes related to multiple interactions (composite outcome as a problem area)

No algorithm, schema, or decision procedure is defined in this document.

---

## Further reading

- [why-abis.md](why-abis.md)
- [examples/reservation.md](examples/reservation.md)
- [../ARCHITECTURE.md](../ARCHITECTURE.md)
