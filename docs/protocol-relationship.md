# ABIS and Existing Protocols

**Version:** Public v0.1

---

## Positioning

ABIS is **protocol neutral**. It is designed to describe Business Interaction and Business Outcome semantics across different AI agents, protocols, and business systems.

ABIS does **not** replace, supersede, or obsolete existing agent, messaging, or execution protocols.

---

## Layer model (conceptual)

```text
+--------------------------------------------------+
|  Business Interaction / Business Outcome (ABIS)  |
+--------------------------------------------------+
|  Agent planning, tool use, orchestration         |
+--------------------------------------------------+
|  Protocols & APIs (execution mechanisms)         |
+--------------------------------------------------+
|  Business systems & infrastructure               |
+--------------------------------------------------+
```

ABIS focuses on the top layer. Lower layers remain the responsibility of their respective specifications and implementations.

---

## Adjacent protocols (examples only)

The following are **examples** of existing or adjacent mechanisms. ABIS makes no claim about their current features, versions, ownership, adoption, or limitations.

| Mechanism | Typical role | ABIS relationship |
| --- | --- | --- |
| **MCP** | Tool and resource access for agents | May carry execution; ABIS describes business meaning of resulting activity |
| **A2A** | Agent-to-agent communication | May carry messaging; ABIS describes business interaction and outcome |
| **REST APIs** | HTTP-based service access | May fulfill business operations; ABIS describes business-level results |
| **UCP** | Checkout-oriented protocols | May handle commerce flows; ABIS describes business outcome of purchase interactions |

This table is illustrative. Other protocols and APIs may also serve as execution mechanisms.

---

## What ABIS does not do

ABIS does not:

- define tool schemas or message formats for MCP, A2A, or other protocols
- specify transport, authentication, or authorization
- handle capability discovery or negotiation
- process payments or manage orders
- claim that any existing protocol "cannot" represent business meaning

ABIS aims to complement the ecosystem by providing a business-level interoperability vocabulary.

---

## Integration pattern (conceptual)

A typical pattern — described conceptually only:

1. A user expresses business intent
2. An AI agent plans and acts using available protocols and APIs
3. Execution completes at the technical layer
4. Business systems produce operational results
5. Business Interaction and Business Outcome may be described in ABIS terms for reporting, auditing, or cross-system alignment

Public v0.1 does not define integration APIs, adapters, or mapping procedures.

---

## Design principle

**Separate execution from business meaning.**

Agents and platforms should be able to discuss whether the intended business result was achieved without conflating that question with transport success or tool completion.

---

## Further reading

- [../SCOPE.md](../SCOPE.md)
- [../ARCHITECTURE.md](../ARCHITECTURE.md)
- [business-interaction.md](business-interaction.md)
