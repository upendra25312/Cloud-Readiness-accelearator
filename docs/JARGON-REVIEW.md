# CRA Framework — Internal Jargon Review

**Epic:** 2.10 — Review all docs for internal jargon; replace with external-facing language  
**Scope:** All public-facing documents in `docs/`, `Templates/`, `presentations/`, `README.md`, `START-HERE.md`  
**Applies to:** Documents that will be shared externally (GitHub public repo, partner sharing)  
**Does NOT apply to:** `_internal-only/`, `docs/DMG-MEDIA-UK-LESSONS-LEARNED.md` (internal reference only), audit spec files (`.md` files in `Templates/`)

---

## Category 1 — Repo-Specific References (Must Fix Before External Sharing)

These references to the temporary working GitHub repo must be updated before sharing with partners or publishing to the `rxt-mpc/` private repo.

| Current Text | Replace With | Files to Check |
| --- | --- | --- |
| `upendra25312/Cloud-Readiness-accelearator` | `rxt-mpc/ps-ind-cloud-readiness-accelerator` | README.md, all badge URLs (5 badges) |
| `github.com/upendra25312/` | `github.com/rxt-mpc/` | README.md, CONTRIBUTING.md, SECURITY.md |
| `upendra25312@gmail.com` | Official Rackspace contact email | SECURITY.md, CONTRIBUTING.md |

**When to apply:** During private repo migration (see Milestone Schedule). Do NOT apply to current working repo yet.

---

## Category 2 — Undefined Acronyms (Fix Immediately — Affects All Audiences)

Every acronym must be spelled out on first use in each document. External audiences (customers, Microsoft SEs, AWS SAs) will not know these.

### Acronyms requiring first-use definition

| Acronym | Full form | Notes |
| --- | --- | --- |
| **CRA** | Cloud Readiness Assessment | Define in every doc on first use: "Cloud Readiness Assessment (CRA)" |
| **AMM** | Azure Migration and Modernisation programme | "Microsoft AMM (Azure Migration and Modernisation)" |
| **MAP** | AWS Migration Acceleration Programme | "AWS MAP (Migration Acceleration Programme)" |
| **PSO** | Google Cloud Professional Services Organisation credits | "GCP PSO (Professional Services Organisation) credits" — some docs say just "PSO credits" with no expansion |
| **RAMP** | GCP Rapid Migration Programme | Define on first use: "RAMP (Rapid Migration Programme)" |
| **SMART** | SMART Assessment (Microsoft Solution Assessment) | Spell out on first use; include footnote: "SMART is Microsoft's pre-sales assessment methodology" |
| **CAF** | Microsoft Cloud Adoption Framework | Define: "Microsoft CAF (Cloud Adoption Framework)" |
| **WAF** | AWS Well-Architected Framework | Define: "AWS WAF (Well-Architected Framework)" |
| **GAF** | Google Cloud Architecture Framework | Define: "Google GAF (Cloud Architecture Framework)" |
| **AHB** | Azure Hybrid Benefit | Define: "Azure Hybrid Benefit (AHB)" — customers know the concept, not always the acronym |
| **BYOL** | Bring Your Own Licence | Define: "BYOL (Bring Your Own Licence)" |
| **RI** | Reserved Instance | Define: "Reserved Instance (RI)" or "3-year Reserved Instance" |
| **CUD** | Committed Use Discount (GCP) | Define: "GCP Committed Use Discount (CUD)" |
| **L4L** | Like-for-Like (baseline migration scenario) | Define: "like-for-like (L4L) baseline" — this is internal consulting jargon |
| **MRA** | Migration Readiness Assessment (AWS) | Define if used |
| **ITSM** | IT Service Management | Define if used |
| **CMDB** | Configuration Management Database | Define: "CMDB (Configuration Management Database)" |
| **RBAC** | Role-Based Access Control | Define on first use |
| **DLP** | Data Loss Prevention | Define on first use |
| **SIEM** | Security Information and Event Management | Define on first use |
| **FinOps** | Cloud Financial Operations | "FinOps (Cloud Financial Operations)" — increasingly well-known but not universal |
| **RTO/RPO** | Recovery Time Objective / Recovery Point Objective | Define both on first use |
| **IPAM** | IP Address Management | Define on first use |
| **NUP** | Named User Plus (Oracle licensing) | Define: "Oracle Named User Plus (NUP) licensing" |
| **ULA** | Unlimited Licence Agreement (Oracle) | Define: "Oracle ULA (Unlimited Licence Agreement)" |
| **ESU** | Extended Security Updates (Microsoft) | Define: "Extended Security Updates (ESU)" |
| **EoL** | End of Life | Use "End of Life (EoL)" — not just "EoL" without context |
| **MSPP** | Microsoft Partner Portal | Define if used externally |
| **7Rs** | 7 migration patterns (Rehost, Replatform, etc.) | Always include the pattern names on first use |
| **SoW / SOW** | Statement of Work | Spell out on first use in customer-facing docs |
| **PoC** | Proof of Concept | Define: "Proof of Concept (PoC)" |
| **IaaS / PaaS / SaaS** | Infrastructure/Platform/Software as a Service | These are widely known but spell out on first use in customer decks |

### Files most likely to have undefined acronyms (check these first)

1. `README.md` — first document any external reader sees
2. `START-HERE.md` — entry point for new users
3. `docs/METHODOLOGY.md` — uses many technical acronyms
4. `docs/guides/01-discovery-phase-guide.md` through `04-planning-phase-guide.md`
5. `docs/MICROSOFT-CAF-ALIGNMENT.md`, `docs/AWS-MAP-ALIGNMENT.md`, `docs/GOOGLE-PSO-ALIGNMENT.md`

---

## Category 3 — Rackspace-Internal Jargon (Replace for External Docs)

Language that is meaningful inside Rackspace but confusing or off-putting to external audiences.

| Internal Jargon | External-Facing Replacement | Context |
| --- | --- | --- |
| "Expert team decision" | [Delete — internal session artifacts] | Legacy file reference |
| "Epic 4B.1" | Remove epic numbers from customer-facing docs (keep in internal TODO tracker only) | Epic numbers appear in some guide files — acceptable in internal docs, not in customer deliverables |
| "v2.0 audit note" | Update the actual content; remove the "audit note" label | These appear as inline comments in phase guides |
| "rxt-mpc" | "Rackspace internal repository" or just remove | Not relevant to customer or partner audiences |
| "Upendra" (as author reference) | "Rackspace Cloud Solutions Architecture" | Phase guide footers, lesson learned doc |
| "DMG engagement" (bare) | "DMG Media UK engagement" or "a UK media engagement" | Ensure full customer name on first use |
| "Part 2" (unexplained) | "Part 2 migration engagement" on first use | External readers don't know CRA has two parts |
| "Rackspace SA" | "Rackspace Solutions Architect" | Spell out role on first use |
| "SMART tool" | "Microsoft SMART Assessment tool" | Needs hyperscaler context |
| "Hard gate" | "Mandatory prerequisite" or "phase gate requirement" | "Hard gate" is internal delivery language |
| "SOW critical path" | "Engagement-critical deliverable" | "SOW critical path" is internal project management jargon |
| "RVTools export" | "VMware inventory export (using RVTools)" | Not all customers know RVTools |
| "Phase guide" | "Delivery guide" or "engagement guide" | "Phase guide" is fine for internal use; for customer-facing docs, "delivery guide" is clearer |

---

## Category 4 — Tone & Register (Apply to Customer-Facing Deliverables)

These are not jargon issues but tone issues. Customer-facing documents (reports, presentations, Part 2 Entry Point) must use a different register than internal guides.

| Avoid | Use Instead | Why |
| --- | --- | --- |
| "We found that..." | "The assessment identified..." | Active first-person implies subjective opinion |
| "You should consider..." | "Rackspace recommends..." | Vague obligation; use specific recommendation |
| "It appears that..." | "The data shows..." or "Analysis confirms..." | Hedging language undermines credibility |
| "Going forward..." | Remove — just state the action | Filler phrase |
| "At the end of the day..." | Remove — just state the conclusion | Filler phrase |
| "Leverage" (as verb) | "Use" | Overused consulting jargon |
| "Synergies" | Specific description | Vague |
| "Best-in-class" | Specific differentiator | Unsubstantiated superlative |
| "World-class" | Specific differentiator | Same |
| "Holistic" | "Comprehensive" or specific scope | Overused |
| "Robust" | Specific capability description | Vague |
| "Moving the needle" | Specific metric | Cliché |
| "Low-hanging fruit" | "Quick wins" or name the specific items | Cliché |

---

## Category 5 — File-by-File Fix List

### Priority 1 — Fix Before Any External Sharing

| File | Issues to Fix | Estimated Effort |
| --- | --- | --- |
| `README.md` | Badge URLs (Category 1); CRA acronym on first use; "Hard gate" → "phase gate requirement" | 30 min |
| `START-HERE.md` | "Part 2" explained; acronyms on first use | 20 min |
| `docs/METHODOLOGY.md` | "Hard gate" language; L4L defined; 7Rs on first use | 30 min |
| `docs/guides/01-discovery-phase-guide.md` | CAB, CMDB, RVTools on first use; "v2.0 audit note" inline comments | 45 min |
| `docs/guides/02-analysis-phase-guide.md` | Cloud Readiness scoring explained; OSS on first use | 30 min |
| `docs/guides/03-evaluation-phase-guide.md` | L4L, RI, AHB, BYOL on first use; AMM/MAP/PSO expanded | 45 min |
| `docs/guides/04-planning-phase-guide.md` | 7Rs, wave plan, Part 2 explained | 30 min |

### Priority 2 — Fix Before Partner Sharing (Post Legal Review)

| File | Issues to Fix | Estimated Effort |
| --- | --- | --- |
| `docs/MICROSOFT-CAF-ALIGNMENT.md` | AMM fully expanded; MSPP explained | 20 min |
| `docs/AWS-MAP-ALIGNMENT.md` | MAP, MRA fully expanded | 20 min |
| `docs/GOOGLE-PSO-ALIGNMENT.md` | PSO, RAMP, CUD fully expanded | 20 min |
| `CONTRIBUTING.md` | Repo URL (Category 1 — when migrating) | 15 min |
| `SECURITY.md` | Contact email (Category 1) | 5 min |

### Priority 3 — Review During Release 1.1 Polish

| File | Issues to Fix |
| --- | --- |
| `docs/DMG-MEDIA-UK-LESSONS-LEARNED.md` | Internal doc — no changes needed; just confirm it stays internal-only |
| `docs/guides/00-architect-onboarding-guide.md` | Internal guide — review for "Hard gate" → "phase gate requirement" in external-facing sections |
| Template audit spec `.md` files | Internal use — no external jargon review needed |

---

## Category 6 — Specific Inline Comments to Remove from Phase Guides

The phase guides contain inline "v2.0 audit note" comments that were added during the template review. These are useful for development but should be cleaned up before the guides are used in customer or partner contexts.

Search for and review (remove or convert to proper documentation):

```
v2.0 audit note
TODO:
PLACEHOLDER
[FILL IN]
[TBD]
[ADD]
```

Run this search on all files in `docs/guides/`:
- `grep -r "v2.0 audit note\|TODO:\|PLACEHOLDER\|\[FILL IN\]\|\[TBD\]\|\[ADD\]" docs/guides/`

Replace with actual content, or remove if the note is no longer relevant.

---

## Execution Checklist

Work through this checklist when doing the jargon review pass:

- [ ] **README.md** — Category 1 URLs, Category 2 acronyms, Category 3 jargon
- [ ] **START-HERE.md** — Category 2, Category 3
- [ ] **docs/METHODOLOGY.md** — Category 2, Category 3, Category 6 inline comments
- [ ] **docs/guides/01-discovery-phase-guide.md** — Category 2, Category 6
- [ ] **docs/guides/02-analysis-phase-guide.md** — Category 2, Category 6
- [ ] **docs/guides/03-evaluation-phase-guide.md** — Category 2, Category 6
- [ ] **docs/guides/04-planning-phase-guide.md** — Category 2, Category 6
- [ ] **docs/MICROSOFT-CAF-ALIGNMENT.md** — Category 2
- [ ] **docs/AWS-MAP-ALIGNMENT.md** — Category 2
- [ ] **docs/GOOGLE-PSO-ALIGNMENT.md** — Category 2
- [ ] **CONTRIBUTING.md** — Category 1 (on repo migration)
- [ ] **SECURITY.md** — Category 1 (on repo migration)

---

*CRA Framework v2.0 — Internal Jargon Review Guide — Rackspace Cloud Solutions Architecture*
