# Why ABIS?

**Version:** Public v0.1

---

## The gap

AI agents are increasingly delegated to complete business tasks: book a table, place an order, submit a form, schedule an appointment.

When an agent reports success, stakeholders often interpret that as business success. In practice, the two are not always the same.

---

## Technical Success != Business Success

A successful technical execution does not necessarily mean that the intended business outcome has been achieved.

| What agents often report | What businesses need to know |
| --- | --- |
| Tool call completed | Was the reservation confirmed at the requested time? |
| HTTP 200 | Was the order accepted with the correct items and delivery window? |
| Task finished | Was the application received and registered correctly? |

Without a shared business-level vocabulary, each agent, platform, and business system describes results differently. Comparison, auditing, and cross-system coordination become difficult.

---

## What ABIS proposes

ABIS is designed to provide a common way to represent:

- **Business Interaction** — what business activity is being attempted
- **Business Outcome** — what was intended and what was observed in business terms

ABIS aims to sit above execution layers and complement existing protocols — not replace them.

---

## Who benefits

| Audience | Benefit |
| --- | --- |
| AI agent developers | Clearer contract for business-meaningful results |
| SaaS / platform providers | Shared vocabulary across integrations |
| System integrators | Easier alignment between agents and business systems |
| Enterprise / government | Auditable business outcome framing |
| Standards organizations | Neutral, protocol-independent discussion basis |

---

## What ABIS does not claim

ABIS does not claim to:

- solve all agent interoperability problems
- replace MCP, A2A, UCP, or REST
- define authentication, payment, or transport
- be a finished normative standard in v0.1

Public v0.1 is a **concept and architecture release** designed to start industry discussion with precise, neutral language.

---

## Next steps

- Read [business-interaction.md](business-interaction.md) and [business-outcome.md](business-outcome.md)
- See [examples/reservation.md](examples/reservation.md) for a generic scenario
- Review [../SCOPE.md](../SCOPE.md) for boundaries
