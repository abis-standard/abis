# ABIS — Public Terminology

**Version:** Public v0.1  
**Status:** Public concept release

This glossary defines terms as used in the public v0.1 release. These definitions are conceptual. They are not normative specification language.

---

## Core terms

### ABIS

**Agent Business Interaction Standard** — an interoperability framework designed to provide a common way to represent Business Interactions and Business Outcomes across different AI agents, protocols, and business systems.

### Beyond Zero Click

Project tagline expressing direction toward business-meaningful outcomes in agent-mediated workflows, beyond click-level or transport-level success signals.

### Business Interaction

A business-meaningful unit of activity — such as a reservation, order, or application — represented independently of a specific agent runtime or wire protocol.

### Business Outcome

The business-meaningful result of a Business Interaction — such as confirmed, pending, rejected, or fulfilled — described in business terms rather than transport or tool status alone.

### AI Agent

Software that acts on behalf of a user or organization to complete tasks, often using tools, APIs, or messaging protocols.

### Protocol

An existing mechanism for messaging, tool invocation, or execution between agents and systems. Examples include MCP, A2A, REST APIs, and checkout-oriented protocols. ABIS does not define or replace protocols.

### Business System

A system of record or operational service that fulfills business operations — such as a reservation system, commerce platform, or case management system.

---

## Distinction terms

### Technical Success

Completion of an execution step at the technical layer — for example, a successful API response or completed tool call.

### Business Success

Achievement of the intended business result — which may differ from technical success.

### Intended (business)

What was expected in business terms before or during an interaction.

### Observed (business)

What was actually achieved in business terms after execution.

---

## Abstract concepts (names only)

The following terms name **problem areas** recognized by the project. Public v0.1 does not define their internal mechanics.

| Term | Public v0.1 usage |
| --- | --- |
| Outcome Equivalence | The question of whether different results represent the same business outcome |
| Multiple Business Interactions | More than one interaction related to a business purpose |
| Dependency | A relationship where one interaction may rely on another |
| Constraint | A business condition that limits acceptable results |
| Failure Propagation | The possibility that failure in one interaction affects others |
| Reconfiguration | The possibility of adjusting related interactions when conditions change |
| Composite Outcome | An outcome that relates to multiple interactions or sub-results |
| Cross-System Outcome | An outcome that spans more than one business system |
| Conformance | Alignment with ABIS concepts over time, as may be assessed in future programs |

---

## Terms not used as ABIS-owned in v0.1

The following remain outside ABIS scope and are not redefined by this glossary:

- Agent Runtime
- Tool Calling
- Transport
- Authentication
- Authorization
- Payment Authorization
- Capability Discovery
- Capability Negotiation

---

## Usage notes

- Prefer **Business Interaction** and **Business Outcome** over informal synonyms when writing about ABIS.
- Do not use patent, counsel, or internal milestone identifiers in public materials.
- Public v0.1 terminology may evolve based on industry feedback and maintainer review.
