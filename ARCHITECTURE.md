# ABIS — Conceptual Architecture

**Version:** Public v0.1  
**Status:** Public concept release

---

## 1. Purpose

This document presents a **conceptual** view of where ABIS fits in agent-mediated business activity. It does not prescribe transport, execution sequence, implementation architecture, or internal decision mechanisms.

---

## 2. Conceptual flow

```text
Human Intent
    |
    v
AI Agent
    |
    v
Existing Protocol / Execution
    |
    v
Business
    |
    v
Business Interaction
    |
    v
Business Outcome
```

**This diagram is conceptual and does not prescribe a transport, execution sequence, implementation architecture, or internal decision mechanism.**

---

## 3. Layer explanation

| Layer | Role in this view |
| --- | --- |
| **Human Intent** | What a person or organization wants to accomplish in business terms |
| **AI Agent** | Software that acts to fulfill intent using available tools and systems |
| **Existing Protocol / Execution** | Established mechanisms such as messaging APIs, tool protocols, or REST services |
| **Business** | The operational domain (hospitality, commerce, public sector, etc.) |
| **Business Interaction** | The business-meaningful activity being attempted |
| **Business Outcome** | The business-meaningful result as intended and as observed |

---

## 4. ABIS focus

ABIS focuses on **Business Interaction** and **Business Outcome** representation across:

- different AI agents
- different protocols
- different business systems

ABIS does not sit inside the protocol or runtime layer. It is designed to describe business semantics that may be shared when multiple agents and systems participate in the same business activity.

---

## 5. Intended vs observed

At a conceptual level, ABIS distinguishes:

| Dimension | Meaning |
| --- | --- |
| **Intended** | What the business actor expected in business terms |
| **Observed** | What was actually achieved in business terms |

Technical success at the execution layer does not, by itself, establish business outcome alignment. ABIS is designed to make that distinction representable.

---

## 6. Multiple interactions

A single business purpose may involve multiple Business Interactions. Each interaction may have its own Business Outcome. ABIS is designed to support representing related interactions without prescribing orchestration, sequencing, or combination logic in this public release.

---

## 7. Relationship to existing protocols

```text
+--------------------------------------------------+
|  Business Interaction / Business Outcome (ABIS)  |
+--------------------------------------------------+
|  Agent logic, planning, tool use                 |
+--------------------------------------------------+
|  Protocols & APIs (e.g. MCP, A2A, REST, UCP)     |
+--------------------------------------------------+
|  Business systems & infrastructure               |
+--------------------------------------------------+
```

ABIS complements — does not replace — protocol and execution layers.

---

## 8. What this architecture does not include

- processing stages or internal pipelines
- state machines
- normalization or equivalence procedures
- conformance scoring
- detailed schemas
- reference implementation
- deployment topology

Those topics may be addressed in future public releases subject to maintainer review and disclosure policy.
