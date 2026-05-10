# Assessment Facilitation Guide

**Version:** 2.0  
**Authors:** Cloud Architecture Teams — Microsoft, AWS, Google Cloud  
**Audience:** Cloud Architects, Pre-Sales Engineers, Consulting Leads

---

## Overview

This guide provides facilitators with step-by-step instructions for running cloud readiness assessment workshops with enterprise customers or internal teams. It covers two complementary assessments:

1. **Cloud Readiness Assessment (CRA)** — [assessments/cloud-readiness-assessment.md](../assessments/cloud-readiness-assessment.md): Multi-cloud, 6-domain organizational maturity assessment
2. **Microsoft SMART Assessment** — [assessments/smart-migration-assessment.md](../assessments/smart-migration-assessment.md): Azure-specific, 10-category migration readiness assessment (aligned to Microsoft CAF)

**Recommended approach for Azure migrations:** Run both. Start with the 15-minute online [SMART tool](https://learn.microsoft.com/en-us/assessments/Strategic-Migration-Assessment/) to generate a Microsoft-curated report, then use this facilitation guide to run the deeper discovery workshops for both CRA and SMART.

---

## Preparation (1 Week Before)

### Stakeholder Mapping

Identify and invite the right participants for each assessment domain:

| Domain | Recommended Participants |
|---|---|
| Strategy & Business Alignment | CIO, CTO, VP Digital Transformation, Finance Lead |
| Organization & Skills | HR / Learning & Development, CCoE Lead, IT Director |
| Platform & Technical Readiness | Cloud Architect, Infrastructure Lead, DevOps Lead |
| Security & Compliance | CISO, Security Architect, Compliance Officer |
| Governance & Financial Management | FinOps Lead, Finance Manager, Cloud Platform Lead |
| Operations & Resilience | SRE/Ops Lead, NOC Manager, BCDR Lead |

For **SMART-specific categories**, ensure these additional participants are available:

| SMART Category | Key Participant |
|---|---|
| Business Strategy | CEO/CIO/CFO — business strategy owner |
| Partner Support | Procurement Lead, IT Vendor Manager |
| Business Case | CFO, Finance Director |
| Technical Skilling | HR/L&D, IT Training Manager |

### Pre-Read Materials (Send to Participants)
- Cloud Readiness Assessment questionnaire (blank copy)
- SMART Assessment overview: [assessments/smart-migration-assessment.md](../assessments/smart-migration-assessment.md)
- Organization's current cloud strategy document (if available)
- Current infrastructure overview / IT landscape summary
- Request participants **complete the online SMART tool** at [learn.microsoft.com/en-us/assessments/Strategic-Migration-Assessment/](https://learn.microsoft.com/en-us/assessments/Strategic-Migration-Assessment/) before the workshop

---

## Workshop Format

### Option A: Combined CRA + SMART Deep-Dive (Recommended for Azure migrations)

- **Duration:** Full day (7–8 hours) or two half-day sessions
- **Mode:** In-person preferred; virtual acceptable (Microsoft Teams, Zoom)
- **Facilitator:** Lead Cloud Architect or Pre-Sales Architect
- **Scribe:** Project Manager or Associate Architect
- **Pre-work:** Participants complete online SMART tool before the session

### Option B: CRA Only (Multi-cloud / cloud-agnostic)

- **Duration:** Full day (6–7 hours)
- **Suitable for:** Organizations assessing multi-cloud or AWS/GCP-primary workloads

### Agenda (Option A — Full Day, Azure Focus)

| Time | Session | Assessment Coverage |
|---|---|---|
| 09:00–09:30 | Introduction, objectives, review SMART online report | SMART Overview |
| 09:30–10:15 | Business Strategy + Business Case deep-dive | SMART Cat. 1, 4 · CRA Domain 1 |
| 10:15–10:30 | Break | |
| 10:30–11:00 | Partner Support + Technical Skilling | SMART Cat. 2, 6 · CRA Domain 2 |
| 11:00–12:00 | Discovery & Assessment + Migration Plan + Execution | SMART Cat. 3, 5, 8 · CRA Domain 3 |
| 12:00–13:00 | Lunch Break | |
| 13:00–14:00 | Landing Zone readiness | SMART Cat. 7 · CRA Domain 3, 4 |
| 14:00–14:45 | Security & Compliance | CRA Domain 4 |
| 14:45–15:30 | Governance (policies, cost management) | SMART Cat. 9 · CRA Domain 5 |
| 15:30–16:00 | Management & Operations | SMART Cat. 10 · CRA Domain 6 |
| 16:00–16:30 | Scoring, heat map, preliminary findings | All |
| 16:30–17:00 | Priority action plan and next steps | All |

### Agenda (Option B — CRA Only, Full Day)

| Time | Session | Domain |
|---|---|---|
| 09:00–09:30 | Introduction, objectives, methodology overview | All |
| 09:30–10:30 | Domain 1: Strategy & Business Alignment | Executive |
| 10:30–11:30 | Domain 2: Organization & Skills Readiness | IT/HR Leaders |
| 11:30–12:00 | Domain 3 (Part 1): Portfolio & Technical Architecture | Technical |
| 12:00–13:00 | Lunch Break | |
| 13:00–14:00 | Domain 3 (Part 2): IaC, DevOps, Operating Model | Technical |
| 14:00–15:00 | Domain 4: Security & Compliance | CISO/Security |
| 15:00–15:45 | Domain 5: Governance & Financial Management | FinOps/Finance |
| 15:45–16:30 | Domain 6: Operations & Resilience | Ops/SRE |
| 16:30–17:00 | Scoring, Debrief, Preliminary Findings | All |

---

## Facilitation Tips

### Scoring Guidance

When scoring each question (1–5), use these anchor definitions:

| Score | Description |
|---|---|
| **1** | Not started / Ad-hoc / No formal process |
| **2** | Defined and documented but not consistently applied |
| **3** | Consistently applied across most teams and workloads |
| **4** | Measured and actively managed; continuous improvement in place |
| **5** | Optimized, automated, and industry-leading practice |

**Important:** Scores should reflect **current state**, not aspirational targets.

### Common Pitfalls to Avoid
- **Over-scoring:** Participants naturally rate their organization higher; probe with specific evidence ("Can you show me an example of this process?")
- **Single-voice dominance:** Ensure all stakeholder perspectives are captured, not just the most senior voice in the room
- **Skipping sub-questions:** All questions contribute to the final score; don't skip even if they seem obvious
- **Confusion between "plans" and "practice":** A plan that exists but is not implemented scores **2**, not **4**

---

## Scoring & Report Generation

### CRA Scoring
1. Compile scores from all domain scorecards
2. Enter into [readiness scorecard template](../templates/readiness-scorecard.md) — CRA section
3. Calculate domain % scores and overall maturity level
4. Identify top 5 gaps (lowest-scoring questions by domain)
5. Draft recommended 90-day action plan with owners

### SMART Scoring
1. Review the automatically generated SMART online report (from the pre-work)
2. Record SMART category scores (0–100) in the [readiness scorecard template](../templates/readiness-scorecard.md) — SMART section
3. Supplement with workshop findings from the [SMART Assessment Guide](../assessments/smart-migration-assessment.md)
4. Identify any SMART categories scoring below 60 — these are blockers that must be addressed before migration proceeds
5. Map SMART remediation actions to accelerator resources (see the SMART assessment guide for per-category links)

### Report Sections (Combined Deliverable)
- Executive Summary (1 page): CRA maturity level + SMART Readiness Index (SRI)
- SMART Category Scores — radar/spider chart (10 categories)
- CRA Domain Scores — bar chart (6 domains)
- Combined Heat Map (visual maturity across all dimensions)
- Top Gaps and Priority Recommendations (linked to accelerator remediation resources)
- Proposed Migration Roadmap (90-day + 12-month), with SMART gate criteria

---

## Post-Assessment Next Steps

| Action | Owner | Timeline |
|---|---|---|
| Share draft findings with customer | Facilitator | Within 3 business days |
| Customer review and feedback | Customer Champion | Within 5 business days |
| Final report delivered | Facilitator | Within 10 business days |
| Roadmap prioritization workshop | Joint team | Within 2 weeks of final report |
| Begin Phase 1 actions | Customer + Partner | Per agreed roadmap |

---

*Reference: [Cloud Readiness Assessment](../assessments/cloud-readiness-assessment.md) | [SMART Migration Assessment](../assessments/smart-migration-assessment.md) | [Readiness Scorecard Template](../templates/readiness-scorecard.md) | [Pre-Sales Playbook](../presales/presales-playbook.md)*
