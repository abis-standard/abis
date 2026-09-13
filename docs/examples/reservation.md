# Example — Generic Restaurant Reservation

**Version:** Public v0.1  
**Type:** Conceptual illustration only

This example is **not** a normative schema, API definition, or verification procedure.

---

## Scenario

A user asks an AI agent to make a restaurant reservation.

### Intended business conditions

| Attribute | Value |
| --- | --- |
| Time | 19:00 |
| Party size | 4 people |
| Seating preference | Non-smoking |

---

## What happens at the technical layer

The agent invokes available tools or APIs. The business system accepts the request. The agent reports **technical success** — the request was submitted and acknowledged.

From a transport or tool perspective, the task appears complete.

---

## What is observed at the business layer

After execution, the actual reservation record shows:

| Attribute | Observed value |
| --- | --- |
| Time | 21:30 |
| Party size | 4 people |
| Seating | Smoking section |

---

## The distinction

| Layer | Assessment |
| --- | --- |
| Technical | Request accepted — technical success |
| Business | Time and seating do not match intent — business outcome misaligned |

**Technical success does not necessarily establish that the intended business outcome was achieved.**

---

## What ABIS is designed to support (conceptually)

ABIS is designed to make it possible to represent:

- the **intended** business conditions (19:00, 4 people, non-smoking)
- the **observed** business result (21:30, 4 people, smoking)
- the distinction between technical completion and business alignment

Public v0.1 does **not** define:

- how to compare intended and observed values
- how to classify the result
- any scoring, weighting, or decision procedure
- any data schema or serialization format

---

## Why this example matters

Reservation scenarios appear simple but expose a recurring pattern in agent-mediated business activity: execution layers optimize for completion signals, while business actors evaluate results in domain terms.

ABIS proposes shared vocabulary for that distinction across agents, protocols, and business systems.

---

## Related reading

- [../why-abis.md](../why-abis.md)
- [../business-outcome.md](../business-outcome.md)
- [../../ARCHITECTURE.md](../../ARCHITECTURE.md)
