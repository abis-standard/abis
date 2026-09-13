# ABIS — Public Governance

**Version:** Public v0.1  
**Status:** Public concept release

---

## 1. Governance model (v0.1)

Public v0.1 operates under a **maintainer-reviewed** model:

| Activity | v0.1 approach |
| --- | --- |
| Public review | Issues and feedback welcome |
| Terminology discussion | Welcome via Issues |
| Use-case discussion | Welcome via Issues |
| Normative changes | Require maintainer review — not automatic |
| Architecture changes | Require maintainer review — not automatic |
| Specification changes | Not in scope for v0.1 repository |

---

## 2. Maintainer role

Maintainers are responsible for:

- reviewing proposed changes to core public documents
- enforcing the public disclosure boundary
- coordinating future normative releases
- determining when additional public material may be published

Maintainer contact and escalation paths will be published when the repository is made public on GitHub.

---

## 3. Contribution phases

### Phase 1 — Public v0.1 (current)

**Public Review / Industry Feedback**

Contributors may:

- open Issues with feedback
- propose terminology improvements
- share use cases and scenarios
- discuss scope and positioning

Contributors should not assume that feedback will be automatically merged into core documents.

### Future phases

Future public releases may include:

- normative specification drafts
- machine-readable artifacts
- reference examples (non-implementing)
- conformance program information

Each phase will be announced through the public roadmap and repository releases.

---

## 4. Disclosure boundary

All contributions to this public repository are subject to the **disclosure gate** defined in `.github/workflows/disclosure-gate.yml` and `public-allowlist.yml`.

Contributors must not submit:

- private implementation detail
- counsel or patent materials
- internal schemas or test vectors
- content copied from non-public ABIS repositories

**Default rule:** unknown material is not public until reviewed.

---

## 5. Decision principles

When evaluating public changes, maintainers aim to:

1. preserve protocol neutrality
2. avoid unsupported competitive claims
3. keep public v0.1 at a conceptual level
4. protect private implementation and legal material
5. maintain international readability

---

## 6. Licensing

License policy for this repository is **pending final review**. No license file is included in this public v0.1 release. See [NOTICE](NOTICE).

---

## 7. Related documents

| Document | Topic |
| --- | --- |
| [SCOPE.md](SCOPE.md) | In scope / out of scope |
| [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) | How to contribute |
| [ROADMAP.md](ROADMAP.md) | Planned public evolution |
| [public-allowlist.yml](public-allowlist.yml) | Allowed public files |
