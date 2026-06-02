# Part 2 Entry Point — Template Content Specification

**Document:** `Templates/executive-reporting/part2-entry-point-template.docx`  
**Purpose:** Build guide — every section below maps to one section of the Word document.  
**Target audience:** Senior Cloud Architects and Delivery Managers completing CRA Phase 4  
**Approx. length of finished DOCX:** 8–12 pages  
**Classification:** [CLIENT CONFIDENTIAL — replace with client name]

---

## HOW TO USE THIS CONTENT SPEC

This file is the authoring blueprint for `part2-entry-point-template.docx`.

1. Open a new Word document using the Rackspace standard DOCX template (`brand.rackspace.com`)
2. Work through each **SECTION** below in order
3. Replace all `[PLACEHOLDER]` text with engagement-specific content
4. Every section includes: Purpose, Required Content, Format, and a populated DMG Media UK example
5. Tables with `TEMPLATE ROW` labels: duplicate the row for each item in your engagement
6. Sections marked ⚠️ are **mandatory** — do not omit even if the data is incomplete; write "TBD — [reason]"

Sections marked 💡 are optional but strongly recommended for enterprise customers.

---

## DOCUMENT HEADER (Page 1 — Cover Page)

**Format:** Full-page cover; Rackspace branded

| Field | Content |
| --- | --- |
| Document Title | Cloud Readiness Assessment — Part 2 Entry Point |
| Customer Name | [CUSTOMER LEGAL ENTITY NAME] |
| Prepared By | [LEAD ARCHITECT NAME], Rackspace Technology |
| Engagement Reference | [ENGAGEMENT ID / SOW REFERENCE] |
| Date | [DD Month YYYY] |
| Document Version | 1.0 |
| Classification | Client Confidential |

**Footer on all pages:** [Customer Name] — Cloud Readiness Assessment Part 2 Entry Point — Rackspace Confidential

---

## SECTION 1 — EXECUTIVE SUMMARY ⚠️

**Purpose:** Give the CTO/CFO a one-page standalone summary they can extract for their board. If they read nothing else, they read this.

**Required content (in order):**

1. **One-sentence engagement statement** — what was assessed, by whom, over what period
2. **Estate summary** — total VMs/servers, application count, DC locations assessed
3. **Recommended hyperscaler** — primary + rationale in two sentences
4. **Three-year TCO summary** — on-prem baseline vs. recommended cloud (net saving / net increase + %)
5. **Partner funding identified** — AMM / MAP / PSO credits available (£/$ headline figure)
6. **Recommended next step** — one sentence describing what Part 2 is and the proposed start date

**Format:** Boxed "At a Glance" summary table + 2–3 paragraph narrative. Maximum 1 page.

**Example (DMG Media UK):**

> Rackspace Technology completed a Cloud Readiness Assessment of DMG Media UK's on-premises estate across two London data centres from February to May 2026. The assessment covered 4,212 virtual machines, 18 Oracle RAC clusters, and approximately 280 in-scope applications.
>
> **Primary recommendation:** Microsoft Azure (UK South primary, UK West DR). Azure was selected based on licensing cost advantage (AHB on 1,200+ Windows Server and 340+ SQL Server workloads), existing Microsoft Unified Support relationship, and strongest Tier-1 regulatory compliance posture for a UK media organisation.
>
> **Three-year TCO:** On-premises status quo: £18.4M. Azure (3-year RI, AHB applied): £11.2M. Net saving: **£7.2M (39%)** before AMM funding.
>
> **Partner funding:** Microsoft AMM eligibility identified — estimated £800K–£1.2M in funded migration services available subject to deal registration.
>
> **Recommended next step:** Proceed to CRA Part 2 (Migration Execution Planning) — proposed start Q3 2026 pending commercial sign-off.

---

## SECTION 2 — SCOPE OF PART 1 ASSESSMENT ⚠️

**Purpose:** Document what was assessed so Part 2 starts from a shared baseline with no ambiguity.

### 2.1 — Estate Summary Table

| Category | Count | Notes |
| --- | --- | --- |
| Virtual Machines (in scope) | [N] | [TEMPLATE ROW — add rows as needed] |
| Physical Servers | [N] | |
| Oracle RAC clusters | [N] | |
| SQL Server instances | [N] | |
| Applications profiled | [N] | |
| Data centres / locations | [N] | [Location names] |
| Assessment period | [Start date] – [End date] | [N] weeks |

**Example (DMG Media UK):** 4,212 VMs, 18 Oracle RAC, 340+ SQL Server, 280 applications, 2 DCs (London Docklands + Sovereign House), 16 weeks.

### 2.2 — What Was Out of Scope

List any assets explicitly excluded. This prevents scope creep in Part 2 or disputes about what was and was not assessed.

| Asset / Area | Reason Out of Scope |
| --- | --- |
| [TEMPLATE ROW] | [TEMPLATE ROW] |

**Example (DMG Media UK):** Network infrastructure redesign (flagged as Part 2 workstream); SaaS applications (separate SaaS rationalisation workstream); DR/BC detailed design (preliminary flags only in Part 1).

### 2.3 — Scope Variance Note ⚠️ (if applicable)

If scope grew during the engagement, document it here to protect Part 2 commercial baseline.

> "The original SOW estimated [N] in-scope VMs. Final assessed estate was [N] VMs — a [X]% variance. This variance was managed through [agreed mechanism: change control / extended timeline / additional resource]. The Part 2 SOW should be scoped against the final assessed figure of [N] VMs."

**Example (DMG Media UK):** Original SOW: 2,700 VMs. Final estate: 4,212 VMs. 57% variance. Managed through phased scope expansion with customer approval. Part 2 SOW must be scoped at 4,212 VMs.

---

## SECTION 3 — HYPERSCALER RECOMMENDATION ⚠️

**Purpose:** Document the recommendation with the evidence that supports it. "Evidence before recommendation" — always show the data first.

### 3.1 — Hyperscaler Scoring Summary

| Evaluation Criterion | Weighting | Azure | AWS | GCP | Notes |
| --- | --- | --- | --- | --- | --- |
| TCO (3-year, primary workloads) | [X]% | [Score/10] | [Score/10] | [Score/10] | [TEMPLATE ROW] |
| Licensing advantage (AHB / BYOL) | [X]% | | | | |
| Regulatory compliance posture | [X]% | | | | |
| Partner commercial (AMM / MAP / PSO) | [X]% | | | | |
| Technical fit (workload types) | [X]% | | | | |
| Strategic alignment (enterprise agreements) | [X]% | | | | |
| **Weighted Total** | **100%** | **[Score]** | **[Score]** | **[Score]** | |
| **Recommendation** | | **[PRIMARY]** | Secondary | Tertiary | |

### 3.2 — Recommendation Rationale

Write 3–5 bullet points, each citing a specific data point from the assessment:

- **Cost:** "[Primary cloud] TCO over 3 years is [£/$X] vs. on-prem [£/$Y] — a [Z]% saving, driven by [AHB / RI pricing / licensing overlay]."
- **Licensing:** "[N] SQL Server licences eligible for AHB — saving [£/$X] vs. PAYG. [N] Oracle workloads [recommended migration path: RDS / Exadata / native PaaS]."
- **Compliance:** "[Primary cloud] holds [specific certifications relevant to customer sector] required for [specific regulatory obligation]."
- **Partner funding:** "[AMM / MAP / PSO] funding eligibility identified — estimated [£/$X] available."
- **Strategic:** "[Primary cloud] aligns to existing [enterprise agreement / support contract / roadmap commitment]."

### 3.3 — Multi-Cloud Exceptions

Document any workloads that cannot move to the primary cloud:

| Application / Workload | Reason for Exception | Recommended Cloud | Notes |
| --- | --- | --- | --- |
| [TEMPLATE ROW] | [TEMPLATE ROW] | [TEMPLATE ROW] | |

---

## SECTION 4 — TCO SUMMARY ⚠️

**Purpose:** Present the financial case. Every figure must trace back to a tab in the TCO Excel model.

### 4.1 — Three-Year Cost Comparison

| Scenario | Year 1 | Year 2 | Year 3 | 3-Year Total | vs. On-Prem |
| --- | --- | --- | --- | --- | --- |
| On-premises (status quo) | £/$ [X] | £/$ [X] | £/$ [X] | £/$ [X] | Baseline |
| [Primary cloud] — Like-for-Like | £/$ [X] | £/$ [X] | £/$ [X] | £/$ [X] | [+/-X%] |
| [Primary cloud] — Optimised (RI / AHB / CUD) | £/$ [X] | £/$ [X] | £/$ [X] | £/$ [X] | [+/-X%] |
| [Primary cloud] — Optimised + Partner Credits | £/$ [X] | £/$ [X] | £/$ [X] | £/$ [X] | [+/-X%] |

> **Note on Year 1:** Year 1 includes dual-running costs (on-prem + cloud overlap during migration). See Section 4.2.

### 4.2 — Year 1 Dual-Running Forecast

Year 1 is typically the most expensive year because workloads run in both environments during migration. Document this explicitly to avoid budget shock.

| Cost Component | Amount | Notes |
| --- | --- | --- |
| On-premises costs (full year — decommission not yet complete) | £/$ [X] | |
| Cloud costs (partial year — wave 1 + 2 migrated) | £/$ [X] | |
| Migration tooling and licences | £/$ [X] | |
| Professional services (Part 2) | £/$ [X] | |
| **Year 1 Total (dual-running)** | **£/$ [X]** | |
| Year 1 Net (offset by AMM/MAP/PSO credits) | £/$ [X] | |

### 4.3 — Licensing Overlay

| Licence Type | Volume | Current Annual Cost | Cloud Path | Optimised Annual Cost | Saving |
| --- | --- | --- | --- | --- | --- |
| Windows Server (AHB eligible) | [N] | £/$ [X] | AHB + 3yr RI | £/$ [X] | £/$ [X] |
| SQL Server (AHB eligible) | [N] | £/$ [X] | AHB + 3yr RI | £/$ [X] | £/$ [X] |
| Oracle (BYOL) | [N] | £/$ [X] | BYOL on [VM/RDS/Exadata] | £/$ [X] | £/$ [X] |
| [Other — TEMPLATE ROW] | | | | | |
| **Licensing Total Saving** | | | | | **£/$ [X]** |

---

## SECTION 5 — PARTNER FUNDING ⚠️

**Purpose:** Quantify the commercial benefit of partner programmes. This is a key differentiator for Rackspace — we can identify and access funding that the customer cannot access directly.

### 5.1 — Partner Funding Summary Table

| Programme | Provider | Eligibility | Estimated Value | CRA Deliverables Required | Status |
| --- | --- | --- | --- | --- | --- |
| Azure Migration and Modernisation (AMM) | Microsoft | [Yes/No/TBC] | £/$ [X]–[Y] | MRA, inventory, business case, wave plan | [Not yet registered / Registered / Approved] |
| AWS Migration Acceleration Programme (MAP) | AWS | [Yes/No/TBC] | £/$ [X]–[Y] | MRA, inventory, business case, wave plan | [Not yet registered / Registered / Approved] |
| Google Cloud RAMP / PSO | Google | [Yes/No/TBC] | £/$ [X]–[Y] | GCAF assessment, discovery export, opportunity registration | [Not yet registered / Registered / Approved] |

**Action required:** Programme deal registration must be completed **before Part 2 SOW signature**. Registration after Part 2 start risks funding eligibility.

### 5.2 — AMM Pre-Qualification Checklist (if Azure primary)

Complete this before submitting the AMM request:

| Requirement | Status | Evidence |
| --- | --- | --- |
| Migration Readiness Assessment (MRA) complete | ✅ / ⬜ | CRA Phase 2 output |
| Validated infrastructure inventory | ✅ / ⬜ | Templates/01-discovery/ |
| Business case with 3-year TCO | ✅ / ⬜ | Templates/03-evaluation/business-case-tco-roi.xlsx |
| Migration wave plan (high level) | ✅ / ⬜ | Templates/04-planning/migration-wave-planner.xlsx |
| Azure as primary or co-primary cloud | ✅ / ⬜ | Hyperscaler recommendation |
| Rackspace registered in MSPP as Delivery Partner | ✅ / ⬜ | Rackspace Alliance Manager to confirm |

---

## SECTION 6 — MIGRATION APPROACH (HIGH LEVEL) ⚠️

**Purpose:** Give the customer confidence that Part 2 has a clear, credible plan — not a blank sheet.

### 6.1 — Recommended Migration Approach

| Phase | Workloads | Approach | Target Completion |
| --- | --- | --- | --- |
| Wave 0 — Proof of Concept | [N] VMs — [lowest risk workloads] | Rehost — IaaS lift-and-shift | [Month Year] |
| Wave 1 — Core Infrastructure | [N] VMs — [dev/test, non-critical] | Rehost — IaaS | [Month Year] |
| Wave 2 — Business Applications | [N] VMs — [business apps, mid-tier] | Rehost / Replatform | [Month Year] |
| Wave 3 — Tier-1 / Production | [N] VMs — [prod, customer-facing] | Rehost with optimisation | [Month Year] |
| Wave 4 — Oracle / Complex | [N] nodes — [Oracle RAC, legacy] | Replatform / Rearchitect | [Month Year] |
| Wave 5 — Decommission On-Prem | All | DC exit | [Month Year] |

> **Note:** Wave plan above is indicative. Part 2 will produce a detailed wave plan with application-level sequencing, dependency management, and cutover windows.

### 6.2 — 7Rs Estate View (High Level)

| Migration Pattern | Est. VM / App Count | Notes |
| --- | --- | --- |
| Rehost (lift-and-shift) | [N] ([X]%) | Majority of estate — low complexity |
| Replatform | [N] ([X]%) | PaaS-eligible (SQL → managed service, etc.) |
| Rearchitect / Refactor | [N] ([X]%) | Greenfield rebuild or containerisation candidates |
| Repurchase (SaaS) | [N] | Replace with SaaS equivalent |
| Retire | [N] | Confirmed decommission — do not migrate |
| Retain | [N] | Cannot migrate — regulatory / latency / dependency |
| Relocate | [N] | Move to different DC without cloud migration |

---

## SECTION 7 — RISK REGISTER (SUMMARY) ⚠️

**Purpose:** Document the top risks identified in Part 1 so Part 2 has a risk baseline. Do not defer this to Part 2 — risks identified now reduce surprises later.

| # | Risk | Category | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- | --- | --- |
| 1 | [TEMPLATE ROW — e.g., Oracle licensing cost overrun] | Licensing | [H/M/L] | [H/M/L] | [Action] |
| 2 | [TEMPLATE ROW — e.g., network redesign delays wave 1] | Technical | | | |
| 3 | [TEMPLATE ROW — e.g., scope variance from additional discovery] | Commercial | | | |
| 4 | [TEMPLATE ROW — e.g., CAB approval lead time for firewall changes] | Operational | | | |
| 5 | [TEMPLATE ROW] | | | | |

**DMG Media UK top risks:**

| # | Risk | Mitigation applied |
| --- | --- | --- |
| 1 | Oracle RAC decommission — 18 clusters, complex licensing | BYOL path modelled; Oracle account team engaged; RAC → single-instance path documented |
| 2 | Scope variance risk — estate grew 57% in Part 1 | Scope gate added at Part 2 SOW; change control mechanism agreed |
| 3 | Redis OSS → Enterprise — 140+ instances | Redis Enterprise Ltd commercial negotiation parallel-tracked |
| 4 | EoL OS (Windows 2012, RHEL 6) — 340+ servers | Extended Security Update (ESU) cost modelled; upgrade wave prioritised |
| 5 | CAB approval lead time — 5–10 business days per firewall change | CAB pre-engagement initiated in week 1 of Part 2 |

---

## SECTION 8 — ORACLE MODERNISATION 💡 (include if Oracle in estate)

**Purpose:** Oracle is frequently the highest-risk and highest-cost element of any migration. A named section prevents it from being buried in the wave plan.

### 8.1 — Oracle Estate Summary

| Workload | Version | Licence Model | VM / Node Count | Recommended Path | Est. Annual Saving |
| --- | --- | --- | --- | --- | --- |
| Oracle RAC | [version] | BYOL (Processor) | [N nodes] | Oracle DB on dedicated VM hosts (BYOL) → evaluate OCI in 24 months | [£/$X] |
| Oracle SE / EE standalone | [version] | BYOL | [N] | Rehost BYOL on [Azure / AWS / GCP] | [£/$X] |
| Oracle Forms / E-Business Suite | [version] | BYOL | [N] | Rehost IaaS — no PaaS alternative at scale | N/A |
| [TEMPLATE ROW] | | | | | |

### 8.2 — Oracle Licensing Flags

- ☐ Is Oracle licensing currently processor-based or NUP? (affects cloud core count)
- ☐ Does the customer have an Oracle Unlimited Licence Agreement (ULA)?
- ☐ Are any workloads eligible for Oracle database service inclusion in OCI? (changes hyperscaler recommendation)
- ☐ Has the customer engaged Oracle account management on cloud migration intent?

> **Rackspace Oracle practice note:** Engage the Rackspace Oracle DBA practice before committing Oracle licensing recommendations to the Part 2 SOW. Oracle licensing in the cloud has non-obvious traps (VMware soft-partitioning, cloud vCPU multipliers) that require specialist review.

---

## SECTION 9 — PART 2 ENGAGEMENT MODEL ⚠️

**Purpose:** Define what Part 2 is, what it costs, and what the customer is buying. This is the commercial close section.

### 9.1 — What Part 2 Delivers

| Deliverable | Description | Format |
| --- | --- | --- |
| Detailed migration wave plan | Application-level sequencing with dependencies, cutover windows, rollback plans | Excel + PPTX |
| Architecture blueprints | Landing zone design, network topology, IAM model for [primary cloud] | Visio / draw.io + DOCX |
| Migration runbooks | Wave-level runbooks for Rehost migrations; application-specific runbooks for complex workloads | DOCX |
| Oracle migration plan | Detailed Oracle estate migration path with licensing confirmation | DOCX |
| Governance framework | Operating model for cloud-first operations post-migration | DOCX |
| Programme governance | Programme board, weekly reporting, RAID log, change control | Ongoing |
| [Additional — TEMPLATE ROW] | | |

### 9.2 — Indicative Timeline

| Phase | Duration | Activities |
| --- | --- | --- |
| Foundation | Weeks 1–4 | Landing zone build, tooling deployment, Wave 0 PoC |
| Wave 1 | Weeks 5–12 | Dev/test + non-critical workloads |
| Wave 2 | Weeks 13–20 | Business applications |
| Wave 3 | Weeks 21–32 | Tier-1 / production |
| Wave 4 | Weeks 33–44 | Oracle / complex workloads |
| DC Exit | Weeks 45–52 | Decommission on-prem, final validation |

> **Note:** Timeline is indicative and based on [N] VMs and [N] waves. Actual timeline confirmed at Part 2 kick-off after detailed wave planning.

### 9.3 — Investment Summary

| Component | Indicative Range | Basis |
| --- | --- | --- |
| Professional services (Rackspace Part 2 delivery) | £/$ [X]–[Y] | Per SOW |
| Cloud consumption (Year 1 — post-migration) | £/$ [X]–[Y] | Per TCO model |
| Migration tooling (licences) | £/$ [X]–[Y] | |
| AMM / MAP / PSO funding offset | (£/$ [X]–[Y]) | Subject to programme approval |
| **Net Year 1 investment** | **£/$ [X]–[Y]** | **After partner funding** |

---

## SECTION 10 — NEXT STEPS ⚠️

**Purpose:** The customer must leave this document knowing exactly what happens next and who does what.

| # | Action | Owner | Target Date |
| --- | --- | --- | --- |
| 1 | Customer sign-off on Part 2 Entry Point | [Customer sponsor name] | [DD Month YYYY] |
| 2 | Rackspace issues Part 2 SOW for review | Rackspace Delivery Manager | [DD Month YYYY] |
| 3 | AMM / MAP / PSO deal registration | Rackspace Alliance Manager | Before SOW signature |
| 4 | Part 2 kick-off meeting (SAs + customer architects) | [Lead Architect] | [DD Month YYYY] |
| 5 | Landing zone decision confirmed (greenfield vs. existing) | [Customer CTO / Lead Architect] | [DD Month YYYY] |
| 6 | Oracle account management engagement | [Customer Oracle owner] | [DD Month YYYY] |
| [TEMPLATE ROW] | | | |

---

## DOCUMENT CONTROL

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 0.1 | [DD Month YYYY] | [Lead Architect] | Initial draft |
| 0.2 | [DD Month YYYY] | [Lead Architect] | Customer review feedback incorporated |
| 1.0 | [DD Month YYYY] | [Delivery Director] | Approved for customer presentation |

---

## APPENDIX A — GLOSSARY (optional but recommended for CTO audiences)

| Term | Definition |
| --- | --- |
| AMM | Azure Migration and Modernisation — Microsoft funded migration programme |
| AHB | Azure Hybrid Benefit — licence portability for Windows Server and SQL Server on Azure |
| CRA | Cloud Readiness Assessment — Rackspace four-phase assessment framework |
| CUD | Committed Use Discount — GCP equivalent of Reserved Instances |
| L4L | Like-for-Like — cloud sizing based on current on-prem specs without rightsizing |
| MAP | Migration Acceleration Programme — AWS funded migration programme |
| MRA | Migration Readiness Assessment — structured questionnaire required for AMM and MAP |
| Part 2 | CRA Phase 2 — migration execution; follows this Entry Point document |
| PSO | Professional Services Organisation — Google Cloud delivery partner programme |
| RAMP | Rapid Assessment & Migration Program — Google structured migration programme |
| RI | Reserved Instance — pre-committed compute pricing on AWS and Azure (1yr or 3yr) |
| 7Rs | Seven migration patterns: Rehost, Replatform, Rearchitect, Repurchase, Retire, Retain, Relocate |

---

*Content Specification for `Templates/executive-reporting/part2-entry-point-template.docx`*  
*Rackspace Cloud Solutions Architecture — CRA Framework v2.0*  
*© 2026 Rackspace Technology. All rights reserved.*
