# Business Interaction

**Version:** Public v0.1

---

## Definition

A **Business Interaction** is a business-meaningful unit of activity expressed in a way that is independent of a specific AI agent implementation, runtime, or wire protocol.

---

## Examples (conceptual)

| Domain | Business Interaction (conceptual) |
| --- | --- |
| Hospitality | Restaurant reservation request |
| Commerce | Purchase order placement |
| Public sector | Permit or benefit application |
| Healthcare | Appointment booking |
| Travel | Flight or hotel booking request |

These examples illustrate business meaning. They are not normative schemas or API definitions.

---

## What a Business Interaction includes (conceptually)

At a high level, a Business Interaction may be described in terms of:

- the **business activity** being attempted
- the **business context** relevant to the request (for example party size, date, product category)
- the **participants** at a business level (customer, provider, agent acting on behalf)

Public v0.1 does not define a fixed schema, field list, or serialization format.

---

## What a Business Interaction is not

A Business Interaction is **not**:

- a tool call name or API endpoint
- a transport message
- an authentication credential
- a payment authorization
- a runtime execution step

Those belong to protocol and infrastructure layers. ABIS is designed to describe business meaning that may be associated with activity across those layers.

---

## Relationship to agents and protocols

A **Business Interaction** is a business-level concept. It describes business-meaningful activity that arises across AI agents, protocols, and business systems — not a step that occurs after a business system completes an operation.

```text
Human Intent
    |
    v
AI Agent  <----->  Protocol / Execution  <----->  Business System
    |                        |                          |
    +------------------------+--------------------------+
                             |
                             v
              Business Interaction (business-level activity
              across agent, protocol, and business system)
```

ABIS focuses on representing this business-level interaction — not on how the agent discovers tools, sends messages, or how a business system fulfills operations internally.

---

## Multiple interactions

One business purpose may involve multiple Business Interactions. For example, organizing a business trip may involve separate interactions for flight, hotel, and ground transportation. Each may be described independently while relating to a shared purpose.

Public v0.1 does not define how multiple interactions are linked, sequenced, or combined.

---

## Further reading

- [business-outcome.md](business-outcome.md)
- [protocol-relationship.md](protocol-relationship.md)
- [examples/reservation.md](examples/reservation.md)
