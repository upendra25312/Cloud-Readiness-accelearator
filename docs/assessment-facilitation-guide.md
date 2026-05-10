# Assessment Facilitation Guide

**Version:** 2.0  
**Authors:** Cloud Architecture Teams — Microsoft, AWS, Google Cloud  
**Audience:** Cloud Architects, Pre-Sales Engineers, Consulting Leads

---

## Overview

This guide provides facilitators with step-by-step instructions for running the [Cloud Readiness Assessment](../assessments/cloud-readiness-assessment.md) workshop with an enterprise customer or internal team.

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

### Pre-Read Materials (Send to Participants)
- Cloud Readiness Assessment questionnaire (blank copy)
- Organization's current cloud strategy document (if available)
- Current infrastructure overview / IT landscape summary

---

## Workshop Format

### Recommended Format
- **Duration:** Full day (6–7 hours) or two half-day sessions
- **Mode:** In-person preferred; virtual acceptable (Microsoft Teams, Zoom)
- **Facilitator:** Lead Cloud Architect or Pre-Sales Architect
- **Scribe:** Project Manager or Associate Architect

### Agenda (Full Day)

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

1. Compile scores from all domain scorecards
2. Enter into [readiness scorecard template](../templates/readiness-scorecard.md)
3. Calculate domain % scores and overall maturity level
4. Identify top 5 gaps (lowest-scoring questions by domain)
5. Draft recommended 90-day action plan with owners

### Report Sections (Deliverable)
- Executive Summary (1 page)
- Domain-by-Domain Findings (scored + narrative)
- Heat Map (visual maturity by domain)
- Top Gaps and Priority Recommendations
- Proposed Cloud Readiness Roadmap (90-day + 12-month)

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

*Reference: [Cloud Readiness Assessment](../assessments/cloud-readiness-assessment.md) | [Readiness Scorecard Template](../templates/readiness-scorecard.md) | [Pre-Sales Playbook](../presales/presales-playbook.md)*
