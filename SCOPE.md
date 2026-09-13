# ABIS — Scope

**Version:** Public v0.1  
**Status:** Public concept release

---

## 1. In scope (public v0.1)

Public v0.1 covers the following at a **conceptual and architectural** level:

| Area | Description |
| --- | --- |
| ABIS name and identity | Agent Business Interaction Standard |
| Positioning | Beyond Zero Click |
| Why ABIS | Technical Success != Business Success |
| Business Interaction | Business-meaningful activity representation |
| Business Outcome | Intended vs observed business result |
| High-level structure | Agent · Business · Outcome relationships |
| Scope boundaries | What ABIS addresses and does not address |
| Protocol neutrality | Relationship to existing protocols without replacing them |
| Generic use cases | Reservations, orders, applications, bookings (conceptual) |
| Public roadmap | Planned public evolution |
| Public governance | Contribution and review principles |

---

## 2. Out of scope (public v0.1)

The following are **explicitly out of scope** for this public repository:

### 2.1 Execution and infrastructure layers

ABIS does not define or own:

- agent runtime
- tool calling
- agent-to-agent messaging
- transport
- agent identity
- authentication
- authorization
- payment authorization
- payment network
- checkout protocol
- order management
- capability discovery
- capability negotiation

### 2.2 Replacement claims

ABIS does not replace MCP, A2A, UCP, REST APIs, or other execution and interoperability protocols. Those mechanisms may continue to handle discovery, messaging, transport, and execution.

### 2.3 Implementation and private material

This public repository does **not** include:

- runtime implementation
- reference implementation
- validation harness
- private schemas
- internal test vectors
- internal conformance rules
- certification program details
- non-public specifications

### 2.4 Legal and IP material

This public repository does **not** include:

- patent claim drafts
- counsel review packages
- filing strategy
- prior-art assessments
- attorney correspondence

---

## 3. Abstract-only topics

The following may be mentioned as **problem areas** in public v0.1. They must not be specified with implementation detail in this release:

- outcome equivalence (as a concept)
- multiple business interactions
- dependency (as a concept)
- constraint (as a concept)
- failure propagation (as a concept)
- reconfiguration (as a concept)
- composite outcome (as a concept)
- cross-system outcome (as a concept)
- conformance (as a concept)

**Allowed:** the concept exists; the problem exists; high-level purpose.

**Not allowed in public v0.1:** algorithms, calculations, state transition logic, internal representation, detailed schemas, decision logic, propagation logic, reconfiguration logic, test vectors.

---

## 4. Public v0.1 boundary statement

This repository is a **public concept and architecture release**. It is designed to support industry discussion, feedback, and alignment on vocabulary and scope.

Normative specifications, implementations, and certification are subject to separate public releases and maintainer review.
