# Reporting & Executive Presentation Templates Audit Specification

**Covers Epics:** 4D.1, 4D.2, 4D.4, 4D.5  
**Templates in scope:**
- `Templates/executive-reporting/cra-assessment-report-template-v3.docx` (4D.1, 4D.2)
- `Templates/executive-reporting/cra-executive-summary-v3.pptx` (4D.4)
- `Templates/04-planning/sow-template.docx` (4D.5)

**How to use this spec:** Open each template. Compare section structure against the required structure below. The assessment report and executive summary are the two documents the customer CTO reads — they must be board-quality. Every section that is present in the spec but missing from the template is a gap that must be filled before the next CRA engagement uses that template.

---

## 4D.1 — CRA Assessment Report (`cra-assessment-report-template-v3.docx`)

### Purpose

The primary written deliverable of the CRA engagement. Delivered to the customer CTO/CIO at the end of Phase 3. Must be fully self-contained — the reader should be able to understand the assessment scope, methodology, findings, and recommendation without any verbal briefing.

### Required Section Structure

Verify the DOCX template contains all sections below, in this order.

| Section | Required? | Content Expected | DMG Lesson |
| --- | --- | --- | --- |
| Cover Page | ✅ Required | Customer name, date, Rackspace logo, classification | — |
| Document Control | ✅ Required | Version, author, reviewer, approval status | — |
| Executive Summary (standalone) | ✅ Required | **1-page maximum** — see 4D.2 for spec | Lesson 9: board-extractable |
| Table of Contents | ✅ Required | Auto-generated, hyperlinked | — |
| 1. Engagement Scope | ✅ Required | In-scope applications, VMs, data centres, excluded systems | Lesson 1: scope variance |
| 2. Methodology | ✅ Required | CRA framework, discovery tooling used, data collection approach | — |
| 3. Infrastructure Discovery Summary | ✅ Required | VM count, OS breakdown, hypervisor, DC locations | — |
| 4. Utilisation Data Summary | ✅ Required | Collection period, coverage %, peak vs average, data quality grade | Lesson 6: utilisation gate |
| 5. Application Inventory Summary | ✅ Required | Application count, criticality breakdown, tech stack summary | — |
| 6. Dependency Analysis | ✅ Required | High-dependency apps, co-migration groups, latency-sensitive pairs | — |
| 7. Cloud Readiness Assessment | ✅ Required | Readiness score distribution (Cloud Ready / Cloud Friendly / Cloud Challenged / Blocked) with counts | — |
| 8. EoL / End-of-Support Analysis | ✅ Required | EoL OS count, EoL database versions, ESU cost impact | Lesson 8: EoL OS |
| 9. Licensing Analysis | ✅ Required | SQL Server / Windows AHB-eligible count, Oracle BYOL options, OSS risk flags | Lessons 3, 4 |
| 10. Cloud Comparison — All Three Clouds | ✅ Required | **Must treat all three clouds equally**; cost, compliance, technical fit | Lesson 9: evidence before recommendation |
| 11. TCO Analysis | ✅ Required | Three-year table: on-prem vs Azure vs AWS vs GCP; Year 1 dual-running | — |
| 12. Licensing Overlay | ✅ Required | AHB saving, Oracle BYOL saving, licensing-adjusted 3-year cost | — |
| 13. Partner Funding | ✅ Required | AMM / MAP / PSO eligibility, estimated funding value | Lesson 5: AMM timing |
| 14. Hyperscaler Scoring Matrix | ✅ Required | Weighted criteria table, scores per cloud, rationale | — |
| **15. Recommendation** | ✅ Required | **Must come AFTER sections 10–14** — never before | Lesson 9: evidence first |
| 16. Migration Approach (7Rs Summary) | ✅ Required | Estate view: Rehost / Replatform / Rearchitect / Repurchase / Retire / Retain | — |
| 17. Indicative Wave Plan | ✅ Required | 5-wave structure, Wave 0 PoC, critical apps in Wave 3+ | — |
| 18. Risk Register | ✅ Required | Technical, dependency, licensing, data, timeline risks | — |
| 19. Oracle Modernisation (if applicable) | Conditional | Include if Oracle RAC/EE in scope | Lesson 3 |
| 20. Part 2 Entry Point | ✅ Required | Part 2 scope, indicative cost ranges, next steps | — |
| Appendix A — VM Inventory Summary | ✅ Required | Aggregated counts by OS, hypervisor, size tier | — |
| Appendix B — Application Inventory Summary | ✅ Required | Full app list in table format | — |
| Appendix C — Scoring Methodology | ✅ Required | How readiness scores are calculated | — |
| Appendix D — Assumptions & Exclusions | ✅ Required | What was out of scope; what was assumed | — |
| Appendix E — Glossary | Recommended | CRA framework terms | — |

### Critical Validation: "Evidence Before Recommendation"

The recommendation section (Section 15) **must not appear before** sections 10–14 in the document. Verify the DOCX heading order matches the sequence above.

**If the current template has the recommendation before the TCO/scoring sections: restructure.**

### Section Length Guidelines

| Section | Guideline |
| --- | --- |
| Executive Summary | 1 page maximum — extractable for board |
| Sections 1–5 | 1–2 pages each |
| TCO Analysis (Section 11) | 2–4 pages including tables |
| Recommendation (Section 15) | 1 page: scoring table + 3–5 bullet rationale |
| Risk Register | 1 table (10–15 rows) |
| Full report target | 40–60 pages including appendices |

---

## 4D.2 — Board-Extractable Executive Narrative (add to `cra-assessment-report-template-v3.docx`)

### Why This Section Exists

The customer CTO needs to brief their board or CEO. They will not send the full 50-page report. They need a 1-page standalone that:
- States what was assessed (scope)
- States what was found (key findings)
- States what is recommended (primary cloud + rationale)
- States what happens next (Part 2 scope + indicative investment)
- Can be extracted from the report and read independently

### Required Content — Executive Summary Page

This section must appear immediately after the Cover Page and Document Control pages. It must be formatted to fit on a single A4/US Letter page.

#### Template Structure

```
[CUSTOMER NAME] Cloud Readiness Assessment — Executive Summary
Prepared by Rackspace Technology  |  [DATE]  |  CONFIDENTIAL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCOPE ASSESSED
[NUMBER] applications | [NUMBER] VMs | [NUMBER] data centre(s) | [DURATION]-week assessment

KEY FINDINGS
• [Finding 1 — most significant: e.g., "39% on-premises cost reduction achievable"]
• [Finding 2 — risk/opportunity: e.g., "340+ servers running EoL OS; ESU cost avoided in cloud"]
• [Finding 3 — licensing: e.g., "[X] SQL Server + [X] Windows Server AHB-eligible — saving £Xm/yr"]
• [Finding 4 — complexity: e.g., "[X] Oracle RAC clusters require specialist migration planning"]
• [Finding 5 — readiness: e.g., "[X]% of estate assessed as Cloud Ready or Cloud Friendly"]

RECOMMENDATION
Primary cloud: [HYPERSCALER] ([REGION])
Rationale: [3 sentences. Must reference TCO saving %, licensing advantage, and compliance alignment]
Secondary (DR / specific workloads): [HYPERSCALER]

THREE-YEAR FINANCIAL SUMMARY
On-premises status quo:  £ [X]M  (incl. ESU, hardware refresh, maintenance)
[Primary cloud] (3yr RI + AHB/BYOL):  £ [X]M
Saving:  £ [X]M  (  [X]%  )
Partner funding identified:  £ [X]M – £ [X]M  (AMM/MAP/PSO)

NEXT STEPS — PART 2 ENGAGEMENT
[Part 2 scope: 2–3 sentences]
Indicative investment: [RANGE]
Target start: [DATE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Engagement Lead: [NAME]  |  [EMAIL]  |  [PHONE]
```

### DMG Media UK — Populated Example

```
DMG Media UK Cloud Readiness Assessment — Executive Summary
Prepared by Rackspace Technology  |  May 2026  |  CONFIDENTIAL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCOPE ASSESSED
280 applications | 4,212 VMs | 2 data centres (Docklands + Sovereign House) | 16-week assessment

KEY FINDINGS
• 39% total cost reduction achievable on Azure (3-year RI + AHB applied)
• 340+ servers running Windows Server 2012 EoL OS; Azure ESU included free — £Xm on-prem cost avoided
• 1,200+ Windows Server + 347 SQL Server licences AHB-eligible; saving estimated £Xm/yr
• 18 Oracle RAC clusters identified; Oracle practice engagement underway
• 75% of estate assessed as Cloud Ready or Cloud Friendly

RECOMMENDATION
Primary cloud: Microsoft Azure (UK South primary / UK West DR)
Rationale: Azure delivers the highest 3-year TCO saving (39% vs 30% AWS / 34% GCP) driven
by Azure Hybrid Benefit on the customer's significant Windows/SQL Server estate. Azure UK South
holds FCA, ISO 27001, SOC 2 Type II, and UK data residency compliance required for regulated
media operations. Microsoft Unified Support and existing EA provide commercial continuity.
Secondary (DR / batch processing): AWS London (eu-west-2)

THREE-YEAR FINANCIAL SUMMARY
On-premises status quo:  £ [X]M  (incl. ESU, VMware renewal, DC facilities)
Microsoft Azure (3yr RI + AHB):  £ [X]M
Saving:  £ [X]M  (~39%)
Partner funding identified:  £800K – £1.2M  (Microsoft AMM confirmed eligible)

NEXT STEPS — PART 2 ENGAGEMENT
Part 2 covers: Landing Zone design, migration factory engagement, Wave 0 PoC (50 VMs),
Oracle RAC modernisation planning, and DC exit roadmap.
Indicative investment: [RANGE]
Target start: [DATE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Formatting Requirements

- Font: Segoe UI or Arial 10pt body, 8pt table text
- No more than one page when printed at A4
- Rackspace logo in top-right corner
- Classification label ("CONFIDENTIAL") in footer
- Section dividers (━━━) to allow easy sectioning
- This page must be independently readable — no cross-references to other sections

---

## 4D.4 — Executive Summary Presentation (`cra-executive-summary-v3.pptx`)

### Purpose

The Phase 3 playback deck presented to the customer CTO and their leadership team. This is the most important customer-facing moment in the CRA engagement. The slide flow must follow the "evidence before recommendation" principle without exception.

### Required Slide Structure (verify against current PPTX)

| Slide # | Slide Title | Required Content | Status to Check |
| --- | --- | --- | --- |
| 1 | Cover | Engagement name, customer name, date, Rackspace logo, classification | ✅ Likely present |
| 2 | Agenda | List of sections; time estimates for each if presenting live | ✅ Likely present |
| 3 | Engagement Scope | What was in scope: app count, VM count, DC count, duration; scope confidence level | Check: scope confidence |
| 4 | Assessment Methodology | CRA four-phase diagram; discovery tooling used; data quality summary | Check: tooling diagram |
| 5 | Infrastructure Summary | VM count by OS / hypervisor / size tier; DC locations; EoL OS flags | Check: EoL OS call-out |
| 6 | Application Landscape | App count by criticality; tech stack distribution; dependency complexity | Check: Oracle/OSS flags |
| 7 | Cloud Readiness Profile | Readiness score distribution chart: Cloud Ready / Cloud Friendly / Cloud Challenged / Blocked; call out key flags | ✅ Core deliverable |
| 8 | Three-Cloud Comparison | **All three clouds — equal treatment**; cost, technical fit, compliance comparison table | **Critical: no pre-recommendation** |
| 9 | TCO Analysis | Three-year comparison chart; on-prem vs Azure vs AWS vs GCP; Year 1 dual-running | Check: on-prem baseline includes ESU |
| 10 | Licensing Overlay | AHB impact (Windows + SQL); Oracle BYOL options; net TCO after licensing | Check: AHB included |
| 11 | Partner Funding | AMM / MAP / PSO eligibility table; estimated credit value; registration status | Check: this slide exists |
| 12 | Hyperscaler Scoring Matrix | Weighted criteria table with evidence column; scores for all three clouds; customer-agreed weights shown | **Evidence must precede recommendation** |
| **13** | **Recommendation** | **Primary cloud + region; rationale (3–5 bullets, each citing slide 9–12 data)** | **Must come AFTER slide 12** |
| 14 | Migration Approach | 7Rs estate view summary; wave plan overview; Wave 0 PoC definition | Check: wave plan exists |
| 15 | Risk Register | Top 10 risks in table format; RAG status; mitigation | Check: Oracle, data residency risks |
| 16 | Partner Funding & Timeline | AMM/MAP/PSO registration timeline; Part 2 start dependency | Lesson 5 |
| 17 | Part 2 Entry Point | Part 2 scope, indicative investment, timeline, next steps | Check: investment range included |
| 18 | Questions & Next Steps | CTA; immediate actions; who signs what by when | — |
| Appendix | Supporting Data | Detailed tables too large for main deck | — |

### Critical Validation Checks

Run these checks against the actual PPTX before use:

**Check 1 — Recommendation placement**
Open the slide deck. Find the first slide that says "Recommendation" or names a specific hyperscaler as "primary."  
This slide number must be ≥ 13.  
If the recommendation appears on slides 3–8: restructure immediately.

**Check 2 — Three-cloud equal treatment**
Slide 8 (Cloud Comparison) must show all three hyperscalers in equal columns. The comparison table must not use language that pre-judges the outcome ("Azure's superior compliance..."). Use neutral headings: "Azure | AWS | GCP".

**Check 3 — Evidence specificity**
On the Recommendation slide (13), each bullet must cite a specific data point:
- ✅ "Azure 3yr RI + AHB: 39% saving vs on-prem — see slide 9"
- ❌ "Azure offers the best value"

**Check 4 — Partner funding slide**
A dedicated partner funding slide (Slide 11) must exist. It must include AMM/MAP/PSO eligibility and estimated £/$ value. This is a Rackspace commercial differentiator — it must not be buried in appendix.

**Check 5 — Slide count**
18 slides is the target. A deck with <14 slides is missing critical evidence sections. A deck with >25 slides is too long for a CTO audience — move detail to appendix.

### Slide Design Standards

| Element | Standard |
| --- | --- |
| Font | Segoe UI (Microsoft stack) or Aktiv Grotesk (Rackspace brand) |
| Rackspace Red | #E31C3D — use for headers, call-out boxes, key figures |
| Background | White (#FFFFFF) body; dark (#1A1A1A or Rackspace Navy) cover |
| Charts | Bar charts for TCO comparison; horizontal bar for readiness distribution |
| Tables | Max 6 columns × 10 rows on a single slide |
| Animations | None — delivery is in PDF as well as PPTX |
| Speaker notes | Every slide must have speaker notes (2–4 sentences minimum) |
| Footer | Slide number + "CONFIDENTIAL — [Customer Name]" |

---

## 4D.5 — SOW Template (`sow-template.docx`)

### Purpose

The Statement of Work template is the commercial document signed by the customer before Phase 1 begins. It defines scope, deliverables, fees, timeline, and governance. A weak SOW creates scope disputes, fee compression, and customer expectation gaps mid-engagement.

### Required Sections — Gap Analysis

Compare `Templates/04-planning/sow-template.docx` against the DMG SOW (`SOW/DMG Cloud Readiness Assessment Part 1 - Rebaselined Objectives & Plan - 10 Apr 2026.docx`) and verify each section below is present and complete.

| Section | Required Content | Gap Check | DMG Lesson |
| --- | --- | --- | --- |
| 1. Engagement Overview | Rackspace + Customer, engagement name, start/end date, engagement type (Time & Materials / Fixed Fee) | Verify dates are placeholder fields | — |
| 2. Scope — Applications | Initial application count estimate, source of estimate (customer CMDB), scope confidence note | **Check: scope variance clause present?** | Lesson 1 |
| 3. Scope — Infrastructure | Initial VM/server count estimate, DC locations, OOB/DR included/excluded | — | Lesson 1 |
| 4. Scope — Exclusions | Explicit list: what is NOT covered (network detail, security architecture, application code review) | — | — |
| **5. Scope Variance Clause** | **"If the assessed estate exceeds the estimated count by more than 15%, a change control will be issued"** | **LIKELY MISSING — add this** | **Lesson 1: 57% variance** |
| 6. Deliverables | Named list of deliverables with description and phase; Phase 1 exit criteria | Verify Part 2 Entry Point is named | — |
| 7. Engagement Timeline | Phase 1–4 duration, hard gates, dependencies (CAB lead time noted?) | Check: CAB lead time referenced? | Lesson 2 |
| **8. Utilisation Data Gate** | **"Phase 3 cannot commence until a minimum of [X] weeks of clean CPU/RAM/storage/network utilisation data has been collected"** | **LIKELY MISSING — add this** | **Lesson 6** |
| 9. Customer Obligations | What the customer must provide: CMDB access, firewall changes, application owner availability | Check: firewall change is listed | Lesson 2 |
| 10. Fees | Fee structure, payment milestones, T&M rates if applicable | Placeholder: [RATE] | — |
| 11. Out-of-Scope Costs | Travel, expenses, tooling licences, third-party software | — | — |
| **12. Alliance Partner Clause** | **"Rackspace will pursue applicable partner funding (AMM/MAP/PSO) on behalf of the customer; deal registration will be completed before Part 2 SOW countersignature"** | **LIKELY MISSING — add this** | **Lesson 5** |
| 13. Governance | Weekly status reporting, steering committee cadence, issue escalation path | Check: escalation path named | — |
| 14. Intellectual Property | CRA methodology and templates remain Rackspace IP; deliverables belong to customer | — | — |
| 15. Assumptions | CMDB accuracy assumed; customer SME availability; network access | — | Lesson 1 |
| 16. Acceptance Criteria | What constitutes completion of each phase; how deliverables are accepted | Check: Phase 3 exit criteria defined | — |
| 17. Termination | Either party termination notice period | — | — |
| 18. Signatures | Customer and Rackspace authorised signatories; date | — | — |

### Three Critical Clauses to Add (Likely Missing)

**Clause 1 — Scope Variance (add to Section 5)**
```
Scope Variance Management: The estate scope provided by [Customer] is an estimate based on
[CMDB / customer-provided data / vCenter export] as at [DATE]. Rackspace will conduct an
independent VM count during Phase 1 Week 1. If the independently assessed estate exceeds the
estimated scope by more than 15%, Rackspace will issue a Change Control Notification within
5 business days. The engagement will continue at current scope until the Change Control is
agreed. Rackspace will not perform work materially outside the agreed scope without a signed
Change Control.
```

**Clause 2 — Utilisation Data Gate (add to Section 8)**
```
Phase 3 Commencement Gate: Phase 3 (Hyperscaler Evaluation and TCO Analysis) cannot commence
until a minimum of [14] calendar days of clean CPU, RAM, storage, and network utilisation data
has been collected from ≥90% of the in-scope VM estate. Rackspace will provide a weekly data
quality report to [Customer Contact]. If schedule pressure arises, Rackspace will present the
financial risk in writing: "A TCO model built on <14 days of data has ±30–50% accuracy vs.
±10–15% accuracy with ≥28 days of data."
```

**Clause 3 — Alliance Partner Registration (add to Section 12)**
```
Alliance Partner Funding: Rackspace will identify applicable hyperscaler partner funding programmes
(Microsoft Azure Migration and Modernisation / AWS Migration Acceleration Programme / Google Cloud
PSO Credits) at engagement start. Where the customer is eligible, Rackspace will initiate deal
registration with the relevant partner programme during Phase 1. Formal deal registration
submission will be completed before the Part 2 Statement of Work is countersigned by Rackspace.
This clause does not guarantee funding approval; it ensures registration is completed at the
earliest eligible stage.
```

---

*Template audit spec for CRA Framework v2.0 — Rackspace Cloud Solutions Architecture*
