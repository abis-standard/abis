# ABIS — Core Concepts

**Version:** Public v0.1  
**Status:** Public concept release

---

## 1. Purpose

ABIS (Agent Business Interaction Standard) is an interoperability framework designed to provide a common way to represent **Business Interactions** and **Business Outcomes** across different AI agents, protocols, and business systems.

This document describes public v0.1 concepts only. It does not define normative requirements, internal schemas, or implementation mechanisms.

---

## 2. Master definition

**ABIS** (Agent Business Interaction Standard) is an interoperability framework designed to provide a common way to represent Business Interactions and Business Outcomes across different AI agents, protocols, and business systems.

**Beyond Zero Click** expresses the project direction: moving from click-level automation toward business-meaningful outcomes in agent-mediated workflows.

---

## 3. Core problem

**Technical Success != Business Success**

A successful technical execution does not necessarily mean that the intended business outcome has been achieved.

Agents and platforms often report success at the transport or tool-execution layer. Business stakeholders need a separate, shared way to describe whether the intended business result was achieved.

---

## 4. Primary concepts

### 4.1 Business Interaction

A business-meaningful unit of activity — independent of a specific agent implementation or wire format.

Examples at a conceptual level:

- reservation request
- order placement
- application submission
- appointment booking

### 4.2 Business Outcome

The business-meaningful result of an interaction — such as confirmed, pending, rejected, or fulfilled — as observed in business terms.

ABIS is designed to support distinguishing:

- intended business result
- observed business result

### 4.3 Agent, Protocol, Business System

| Term | Public v0.1 meaning |
| --- | --- |
| **AI Agent** | Software that acts on behalf of a user or organization to complete tasks |
| **Protocol** | An existing mechanism for messaging, tool use, or execution (for example MCP, A2A, REST) |
| **Business System** | A system of record or service that fulfills business operations |

ABIS does not redefine these layers. It focuses on business interaction and business outcome representation across them.

---

## 5. Abstract concepts (existence only)

The following topics are recognized as relevant problem areas for agent-mediated business activity. **Public v0.1 describes that these concerns exist.** It does not disclose algorithms, internal representations, decision logic, or implementation detail.

| Concept | Public v0.1 statement |
| --- | --- |
| Outcome Equivalence | Different execution paths may need to be understood at a business-outcome level |
| Multiple Business Interactions | One business purpose may involve several interactions |
| One Purpose → Multiple BI | A single intent may decompose into multiple business interactions |
| Dependency | Business interactions related to one purpose may depend on one another |
| Constraint | Business conditions may limit what constitutes an acceptable result |
| Failure Propagation | A failure in one interaction may affect related interactions |
| Reconfiguration | Related interactions may need to be adjusted when conditions change |
| Composite Outcome | Multiple individual outcomes may relate to one broader purpose |
| Cross-System Outcome | Outcomes may span more than one business system |
| Conformance | Organizations may need a way to assess alignment with ABIS concepts over time |

No calculation method, state machine, schema, or verification procedure is defined in this public release.

---

## 6. Protocol neutral

ABIS is **protocol neutral**. It is designed to apply across different agent and execution environments without requiring a single transport or messaging standard.

Existing protocols and APIs may serve as execution mechanisms. ABIS does not claim to replace them.

---

## 7. Audience

Public v0.1 is intended for:

- AI agent developers
- SaaS and platform providers
- system integrators
- enterprise and government technology teams
- standards and technology organizations

It is not positioned as a consumer application.

---

## 8. What this document does not contain

- normative specification text
- detailed schemas
- reference implementation
- certification rules
- private or counsel materials
- patent or filing materials
