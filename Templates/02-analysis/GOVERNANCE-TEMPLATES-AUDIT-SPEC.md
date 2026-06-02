# Governance, Risk & Cloud Maturity Templates Audit Specification

**Covers Epics:** 4E.1, 4E.2, 4E.3  
**Templates in scope:**
- `Templates/02-analysis/governance-foundations-alignment.xlsx` (4E.1)
- `Templates/04-planning/risk-assessment.xlsx` (4E.2)
- `Templates/04-planning/governance-model.xlsx` (4E.3 — new tab: RACI matrix)

**Supporting templates (Instructions tab coverage — Epic 10.4):**
- `Templates/02-analysis/cloud-readiness-scoring-v2.xlsx`
- `Templates/02-analysis/readiness-scoring-criteria.xlsx`
- `Templates/04-planning/migration-wave-planner.xlsx`

**How to use this spec:** Open each template. Compare against the required structure below. Governance and risk templates are often the last to be filled in during an engagement — but they are the first things a customer's internal audit team or security team will examine. Templates that are vague or missing categories will create scope disputes.

---

## 4E.1 — Governance Foundations Alignment Tool (`governance-foundations-alignment.xlsx`)

### Purpose

Assess the customer's current cloud governance maturity against industry frameworks (Microsoft CAF, AWS Well-Architected, Google Cloud Architecture Framework) and identify gaps that Part 2 must address. This is both a discovery deliverable and a scoping input for Part 2.

### Required Tab Structure

| Tab | Purpose |
| --- | --- |
| Instructions | Who fills this in, when, how |
| Governance Maturity Assessment | 6 domains × maturity scale scoring |
| CAF / WAF / GAF Alignment | Map current state to framework stages |
| Gap Register | Gaps identified, priority, Part 2 dependency |
| Cloud Readiness Blockers | Governance-level blockers that prevent cloud migration |
| Summary Dashboard | Traffic-light summary; executive-ready |

### Required Structure — Governance Maturity Assessment Tab

Score each domain on a 1–5 maturity scale. Use this as the standard starting structure.

**Maturity Scale:**
| Score | Label | Description |
| --- | --- | --- |
| 1 | Initial | No formal process; ad hoc |
| 2 | Developing | Basic processes exist; inconsistently applied |
| 3 | Defined | Documented processes; consistently applied |
| 4 | Managed | Measured and controlled; metrics exist |
| 5 | Optimising | Continuous improvement; benchmarked externally |

**Six Required Domains:**

| Domain | Sub-Areas to Assess | Cloud Migration Impact |
| --- | --- | --- |
| **Identity & Access Management** | AD/LDAP structure, MFA adoption, privileged access management, RBAC maturity | Low IAM maturity = cloud landing zone redesign needed in Part 2 |
| **Security & Compliance** | Vulnerability management, patching cadence, SIEM, DLP, regulatory certification status (ISO27001 / SOC2 / FCA / GDPR) | High compliance requirements → constrained cloud region selection |
| **Change Management** | CAB process, change lead time, emergency change rate, ITSM tooling (ServiceNow / Jira) | Long CAB lead times → Phase 1 delay risk (Lesson 2) |
| **Monitoring & Observability** | Current monitoring stack (Dynatrace / Datadog / SCOM / Prometheus), alerting coverage, log retention | Monitoring gap = must be scoped into Part 2 landing zone |
| **Cost Management** | FinOps maturity, chargeback/showback model, budget governance, cloud cost awareness | No cost management process → cloud spend overruns in Part 2 |
| **Operational Readiness** | RunBook maturity, disaster recovery testing frequency, RTO/RPO definitions, on-call process | DR gap = business continuity risk during migration waves |

**Columns per domain row:**

| Column | Content |
| --- | --- |
| Domain | From table above |
| Sub-Area | Specific aspect being scored |
| Current Maturity Score (1–5) | Lead Architect / customer workshop output |
| Evidence | What evidence supports the score |
| Target Maturity (post-Part 2) | What the customer needs for cloud operations |
| Gap | Target − Current |
| Priority | Critical / High / Medium / Low |
| Part 2 Dependency? | Yes / No — is closing this gap a Part 2 deliverable? |

### Required Structure — Gap Register Tab

| Column | Content |
| --- | --- |
| Gap ID | Auto-number |
| Domain | From Governance Maturity tab |
| Gap Description | What is missing or underdeveloped |
| Business Risk | What happens if this gap is not closed before migration |
| Recommended Action | Specific action: policy creation, tooling deployment, process design |
| Part 2 Workstream | Which Part 2 workstream addresses this |
| Priority | Critical (blocks migration) / High / Medium / Low |
| Estimated Effort | Days/weeks (rough order of magnitude) |

### Required Structure — Summary Dashboard Tab

This tab produces the executive slide input for the governance section of the Phase 3 playback.

| Row | Content |
| --- | --- |
| Overall Governance Maturity | Weighted average score (1–5) with RAG: Red <2.5 / Amber 2.5–3.5 / Green >3.5 |
| Identity & Access | Score + RAG + 1-line finding |
| Security & Compliance | Score + RAG + 1-line finding |
| Change Management | Score + RAG + 1-line finding |
| Monitoring & Observability | Score + RAG + 1-line finding |
| Cost Management | Score + RAG + 1-line finding |
| Operational Readiness | Score + RAG + 1-line finding |
| Migration Blockers | Count of Critical-priority gaps |
| Part 2 Dependencies | Count of gaps requiring Part 2 action |

### Instructions Tab Content

```
GOVERNANCE FOUNDATIONS ALIGNMENT TOOL
CRA Framework — Phase 2: Analysis

PURPOSE
Assess the customer's current IT governance maturity to identify gaps that could block or
slow cloud migration. This tool feeds the governance section of the Phase 3 executive playback
and scopes the governance workstreams for Part 2.

WHO FILLS THIS IN
Lead Architect (scoring framework) + Customer IT Director / Head of Platform (validation)
Complete during Phase 2 weeks 1–2 via workshop session (2–3 hours).

WHEN IN THE ENGAGEMENT
Phase 2, weeks 1–3. Must be complete before Phase 3 governance risk section can be drafted.

STEP-BY-STEP
1. Schedule a 2–3 hour governance workshop with the customer's IT Director or Head of Platform
2. Walk through each of the 6 domains; score collaboratively
3. Document evidence for each score (interview notes, policy documents, tool screenshots)
4. Identify gaps where Target Maturity > Current Maturity
5. Categorise each gap: Critical (blocks migration) / High / Medium / Low
6. Populate the Summary Dashboard tab
7. Present the Summary Dashboard in the Phase 3 playback

WHAT "GOOD DATA" LOOKS LIKE
- Every domain scored with specific evidence (not just interview impressions)
- At least one Part 2 dependency identified per low-scoring domain
- Change management CAB lead time documented (feeds Phase 1 timeline planning)

HOW THIS FEEDS DOWNSTREAM
→ Phase 3: Governance risk section of TCO model and executive report
→ Phase 4: Part 2 workstreams — landing zone design, IAM, monitoring, FinOps
→ SOW: Part 2 scope calibration (more governance gaps = larger Part 2 engagement)

QUESTIONS?
Refer to docs/guides/02-analysis-phase-guide.md
Contact: [Engagement Lead Architect]
```

---

## 4E.2 — Risk Assessment Template (`risk-assessment.xlsx`)

### Purpose

Capture and communicate the top risks to the CRA engagement and the subsequent migration. This is both a delivery governance tool (tracks engagement risks week-to-week) and a customer deliverable (presented in the Phase 3 risk register section).

### Required Tab Structure

| Tab | Purpose |
| --- | --- |
| Instructions | Who fills this in, when, how |
| Engagement Risk Register | Risks to Phase 1–4 delivery (delivery risks) |
| Migration Risk Register | Risks to the actual cloud migration (technical risks) |
| Closed Risks | Archive of risks that have been resolved |
| Risk Summary | RAG dashboard; top 5 risks for executive report |

### Required Columns — Engagement Risk Register Tab

| Column | Content |
| --- | --- |
| Risk ID | Auto-number (R-001, R-002, ...) |
| Risk Category | **See required categories below** |
| Risk Description | What could go wrong (1–2 sentences) |
| Likelihood | 1–5 (1=Very Low, 5=Very High) |
| Impact | 1–5 (1=Very Low, 5=Very High) |
| Risk Score | = Likelihood × Impact (auto-calculated) |
| RAG Status | Red (15–25) / Amber (5–14) / Green (1–4) |
| Current Controls | What is already in place to mitigate |
| Additional Mitigation | What else is planned |
| Owner | Risk owner (name + role) |
| Review Date | When this risk is next reviewed |
| Status | Open / Monitoring / Escalated / Closed |

### Required Risk Categories (must cover all of these)

These categories must exist as a dropdown in the Risk Category column. Missing categories mean those risk types won't be logged.

| Category | Why Required | DMG Example |
| --- | --- | --- |
| **Scope & Estimation** | 57% scope variance in DMG | "CMDB inaccuracy means VM count may be higher than SOW scope" |
| **Data Quality** | Utilisation gate | "Insufficient utilisation data collected for Phase 3 TCO accuracy" |
| **Technical — Dependency** | Co-migration risk | "Undiscovered app dependencies cause migration sequence failure" |
| **Technical — Licensing** | Oracle / Redis complexity | "Oracle RAC licensing in cloud not fully understood — cost overrun risk" |
| **Technical — EoL** | ESU cost / security | "340+ EoL OS servers create security risk during extended migration timeline" |
| **Regulatory & Compliance** | FCA / GDPR | "Data residency requirements restrict hyperscaler region selection" |
| **Schedule** | CAB lead time | "Customer CAB process adds 7+ business days to firewall change requests" |
| **Resource** | Architect availability | "Customer application owner availability below 50% in Phase 2" |
| **Commercial** | AMM registration | "Alliance partner deal registration not completed before Part 2 SOW" |
| **Stakeholder** | Executive buy-in | "Customer CTO change or budget freeze mid-engagement" |
| **Third-Party** | SaaS vendor, network carrier | "Key third-party vendor migration dependency not confirmed" |

### Required Risk Register — Minimum Pre-Populated Risks

The template should be shipped with these risks pre-populated (set to Amber/likelihood 3 by default) so new architects don't start from a blank register:

| Risk ID | Category | Description | Default Likelihood | Default Impact |
| --- | --- | --- | --- | --- |
| R-001 | Scope & Estimation | Customer-provided estate estimate is based on CMDB data that may be outdated. Actual VM count could exceed SOW scope by 15–30%. | 4 | 3 |
| R-002 | Data Quality | Discovery tooling firewall approval (CAB) may delay the start of utilisation data collection, compressing the Phase 3 data quality window. | 3 | 4 |
| R-003 | Technical — Licensing | Oracle workloads identified in inventory may have complex licensing implications (RAC, vCPU multipliers) not captured in initial TCO. | 3 | 4 |
| R-004 | Technical — Dependency | Application dependency mapping may be incomplete due to undocumented or informal integration patterns. | 3 | 3 |
| R-005 | Schedule | Phase 3 cannot start until minimum utilisation data is collected. If data collection is delayed, Phase 3 start date is at risk. | 3 | 4 |
| R-006 | Commercial | Alliance partner deal registration (AMM/MAP/PSO) must be completed before Part 2 SOW countersignature. Delayed registration risks Part 2 commercial timeline. | 2 | 3 |
| R-007 | Regulatory & Compliance | Regulatory requirements (GDPR, FCA, PCI) may restrict cloud region selection or require additional security controls in the landing zone. | 2 | 4 |

### Required Columns — Migration Risk Register Tab

The migration risk register uses the same columns as the engagement risk register but adds:

| Additional Column | Content |
| --- | --- |
| Migration Wave | Which wave (1–5) this risk applies to |
| Pre-Migration Action | What must be done before this wave starts to mitigate |
| Rollback Plan | What happens if this risk materialises during migration |

### Risk Summary Tab — Executive Output

| Row | Content |
| --- | --- |
| Overall Risk Profile | Count: Red / Amber / Green |
| Top 5 Risks | Risk ID + description + RAG + owner + due date |
| Closed Risks This Month | Count |
| New Risks This Month | Count |
| Risk Trend | ↑ Increasing / → Stable / ↓ Decreasing |

---

## 4E.3 — Governance Model & RACI Matrix (add tab to `governance-model.xlsx`)

### Purpose

Define who is responsible for each CRA activity and Part 2 delivery workstream. Prevents "we didn't know we owned that" disputes. The RACI must be agreed with the customer in Phase 1 or Phase 2 and shared at the Phase 1 kickoff meeting.

### Add Tab: `RACI Matrix`

#### CRA Engagement Roles

| Role | Internal/External | Description |
| --- | --- | --- |
| **Engagement Lead Architect** | Rackspace | Overall delivery accountability; customer-facing lead |
| **Platform Architect (Azure)** | Rackspace | Azure technical delivery |
| **Platform Architect (AWS/GCP)** | Rackspace | Multi-cloud evaluation support |
| **Delivery Manager / PM** | Rackspace | Schedule, risk, stakeholder management |
| **Pre-Sales Architect** | Rackspace | Pricing, commercial, Part 2 scoping |
| **Alliance Manager** | Rackspace | AMM/MAP/PSO deal registration |
| **Oracle Practice Lead** | Rackspace | Oracle RAC/EE licensing analysis (when applicable) |
| **Customer IT Director** | Customer | Customer-side technical decision-maker |
| **Customer App Owner(s)** | Customer | Application-specific data and validation |
| **Customer PM / Coordinator** | Customer | Internal coordination, SME scheduling |
| **Microsoft / AWS / GCP SE** | Partner | Hyperscaler technical validation (Phase 3) |

#### RACI Key

| Letter | Meaning |
| --- | --- |
| **R** | Responsible — does the work |
| **A** | Accountable — approves the output; one person max per row |
| **C** | Consulted — provides input before completion |
| **I** | Informed — notified after completion |

#### RACI Matrix — Phase 1 Activities

| Activity | Lead Arch | Platform Arch | Delivery Mgr | Pre-Sales | Alliance Mgr | Oracle Lead | Customer IT Dir | App Owners | Customer PM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Phase 1 Kickoff Meeting | A/R | C | C | C | I | I | C | I | I |
| Application Scoping Template (initial pass) | R | C | I | I | I | I | A | C | I |
| Application Owner Validation | C | I | C | I | I | I | A | R | C |
| Discovery Tooling Deployment | R | R | I | I | I | I | C | I | I |
| CAB Firewall Change Request | C | R | I | I | I | I | A | I | R |
| Infrastructure Profiling | R | R | I | I | I | I | C | C | I |
| Dependency Mapping | R | C | I | I | I | I | C | R | I |
| Oracle Flag — Practice Escalation | A | R | I | I | I | C | I | I | I |
| Alliance Partner Pre-Registration | I | I | I | C | R | I | I | I | I |
| Phase 1 Deliverables Review | A | C | C | I | I | I | R | I | I |
| Phase 1 Exit Gate Sign-Off | A | C | C | I | I | I | R | I | I |

#### RACI Matrix — Phase 2 Activities

| Activity | Lead Arch | Platform Arch | Delivery Mgr | Pre-Sales | Alliance Mgr | Oracle Lead | Customer IT Dir | App Owners | Customer PM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Governance Workshop | R | C | I | I | I | I | A | C | C |
| Cloud Readiness Scoring | R | R | I | I | I | C | C | C | I |
| Compliance Assessment | R | C | I | I | I | I | A | I | I |
| Oracle Practice Analysis | C | I | I | I | I | R | C | I | I |
| OSS Licence Risk Review | R | C | I | I | I | I | C | R | I |
| Phase 2 Deliverables Review | A | C | C | I | I | I | R | I | I |

#### RACI Matrix — Phase 3 Activities

| Activity | Lead Arch | Platform Arch | Delivery Mgr | Pre-Sales | Alliance Mgr | Oracle Lead | Customer IT Dir | App Owners | MS/AWS/GCP SE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TCO Modelling (Azure) | R | R | I | C | I | I | I | I | C |
| TCO Modelling (AWS) | R | R | I | C | I | I | I | I | C |
| TCO Modelling (GCP) | R | R | I | C | I | I | I | I | C |
| Licensing Overlay | R | C | I | C | I | R | C | I | I |
| AMM/MAP/PSO Credit Estimation | C | I | I | C | R | I | I | I | C |
| Hyperscaler Scoring Matrix | A/R | C | I | C | I | I | C | I | I |
| Weighting Agreement with Customer | R | I | I | I | I | I | A | I | I |
| Phase 3 Playback Presentation | A/R | C | C | I | C | I | R | I | I |

#### RACI Matrix — Phase 4 Activities

| Activity | Lead Arch | Platform Arch | Delivery Mgr | Pre-Sales | Alliance Mgr | Oracle Lead | Customer IT Dir | App Owners | Customer PM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Wave Plan Development | R | C | I | I | I | I | C | C | I |
| Risk Register (final) | R | C | I | I | I | I | C | I | I |
| Part 2 Entry Point Document | R | C | I | R | R | C | C | I | I |
| AMM/MAP/PSO Deal Registration | C | I | I | I | A/R | I | I | I | I |
| Part 2 SOW Development | C | I | I | A/R | C | I | C | I | I |
| Part 2 SOW Signature | I | I | I | I | I | I | A | I | I |

### Instructions Tab Content — Governance Model

```
GOVERNANCE MODEL & RACI MATRIX
CRA Framework — Phase 1: Setup / Phase 2: Analysis

PURPOSE
Define roles, responsibilities, and accountabilities for all CRA engagement activities. 
The RACI matrix prevents ownership gaps and "we didn't know we owned that" disputes 
mid-engagement. Share and agree with the customer at the Phase 1 kickoff meeting.

WHO FILLS THIS IN
Delivery Manager (initial framework) + Engagement Lead Architect (technical rows)
Reviewed and agreed with: Customer IT Director and Customer PM

WHEN IN THE ENGAGEMENT
Phase 1 kickoff meeting. Update at each phase boundary if roles change.

STEP-BY-STEP
1. Open the RACI Matrix tab
2. Add actual names (not just roles) in the column headers — update [Lead Arch] with the
   named lead architect, etc.
3. Review each row with the customer — confirm their A (Accountable) assignments
4. Flag any activity where the customer does not have an identified owner — these are risks
5. Add engagement-specific rows for any custom activities (e.g., Oracle practice escalation
   if Oracle is in scope)
6. Save and attach to the engagement kickoff pack

HOW THIS FEEDS DOWNSTREAM
→ Phase 2–4: Use RACI to identify who must attend each workshop or sign each deliverable
→ Risk Register: RACI gaps (rows with no A) become risks to log
→ Part 2 SOW: RACI carries forward and expands for Part 2 delivery team

QUESTIONS?
Refer to docs/guides/00-architect-onboarding-guide.md
Contact: [Engagement Lead Architect]
```

---

## Epic 10.4 — Instructions Tab Spec: Analysis Phase Templates

Add Instructions tabs to the following Analysis phase templates. Use the standard format from `Templates/01-discovery/DISCOVERY-TEMPLATES-AUDIT-SPEC.md` Section 4A.5.

### `cloud-readiness-scoring-v2.xlsx` — Instructions Tab

```
CLOUD READINESS SCORING TOOL
CRA Framework — Phase 2: Analysis

PURPOSE
Score each application against cloud readiness criteria. Output is used in the Phase 3
executive report and executive presentation to show the estate-level readiness profile
(Cloud Ready / Cloud Friendly / Cloud Challenged / Blocked).

WHO FILLS THIS IN
Lead Architect + Platform Architect (scoring) + Application Owners (validation)

WHEN IN THE ENGAGEMENT
Phase 2 weeks 1–3. Requires validated Phase 1 application and infrastructure inventory.
Can begin Phase 1 week 6 (parallelisation — see docs/guides/02-analysis-phase-guide.md).

STEP-BY-STEP
1. Import application list from application-scoping-profiling.xlsx
2. For each application, score against the 6 readiness criteria (Technical Fit,
   Dependencies, Data, Compliance, Licensing, Operational Readiness)
3. Run the automated scoring to produce a Cloud Readiness Grade
4. Flag any "Blocked" applications with a specific blocker description
5. Validate scores with application owners for Tier-1/Critical applications
6. Populate the Summary tab for the executive report

WHAT "GOOD DATA" LOOKS LIKE
- Every Critical/High application scored with evidence
- Blocked applications have a named blocker (not "complex")
- Oracle and Redis applications flagged for specialist review

HOW THIS FEEDS DOWNSTREAM
→ Phase 3: Readiness profile chart in executive report and presentation
→ Phase 4: Blocked applications become Wave 5 or Retain candidates
→ Part 2 SOW: Rearchitect/Repurchase apps drive Part 2 scope

QUESTIONS?
Refer to docs/guides/02-analysis-phase-guide.md
```

### `readiness-scoring-criteria.xlsx` — Instructions Tab

```
READINESS SCORING CRITERIA
CRA Framework — Phase 2: Analysis

PURPOSE
Defines the scoring criteria and weightings used in cloud-readiness-scoring-v2.xlsx.
This is the methodology reference — do not modify criteria mid-engagement without
documenting the change and reason in the Document Control tab.

WHO FILLS THIS IN
Lead Architect (initial setup) — agreed with customer at Phase 2 kickoff

WHEN IN THE ENGAGEMENT
Phase 2 week 1. Review with customer before scoring begins to confirm criteria
and weightings are appropriate for their sector and risk profile.

STEP-BY-STEP
1. Review the 6 scoring criteria and default weightings
2. Adjust weightings for sector (e.g., increase Compliance weighting for FCA/healthcare)
3. Document any weighting changes in the Document Control tab with rationale
4. Distribute to Phase 2 scoring team

HOW THIS FEEDS DOWNSTREAM
→ Phase 3: Weighting methodology presented in executive playback scoring slide
→ This document is referenced in Appendix C of the Phase 3 report

QUESTIONS?
Refer to docs/guides/02-analysis-phase-guide.md
```

---

## Epic 10.4 — Instructions Tab Spec: Planning Phase Templates

### `migration-wave-planner.xlsx` — Instructions Tab

```
MIGRATION WAVE PLANNER
CRA Framework — Phase 4: Planning

PURPOSE
Sequence all in-scope applications and infrastructure into migration waves. The wave
plan is a named Part 2 Entry Point deliverable. It drives the Part 2 migration factory
engagement scope and timeline.

WHO FILLS THIS IN
Lead Architect (initial draft) + Customer IT Director (validation)

WHEN IN THE ENGAGEMENT
Phase 4 weeks 1–3. Requires completed Phase 2 readiness scores and Phase 3 7Rs
classification. Can be drafted in parallel with Part 2 Entry Point document.

WAVE SEQUENCING PRINCIPLES
Wave 0 (PoC):   5–10% of estate; non-production; lowest complexity; no customer data
Wave 1:         Non-critical development/test environments; validate tooling
Wave 2:         Internal business applications; Medium criticality
Wave 3:         Core business applications; High criticality; well-tested dependencies
Wave 4:         Tier-1 / mission-critical; regulated data; Oracle/complex workloads
Wave 5:         Retained/deferred; DC exit final sweep

STEP-BY-STEP
1. Import application list and 7Rs classification from hyperscaler-decision-matrix.xlsx
2. Apply sequencing rules: Blocked → Wave 5/Retain; Retire → Wave 0 (decommission)
3. Group apps with hard dependencies into the same wave
4. Validate wave timing against business calendar (month-end batch, payroll, peak trading)
5. Estimate VM count and storage per wave
6. Present wave plan to customer for approval at Phase 4 playback

WHAT "GOOD DATA" LOOKS LIKE
- No Tier-1/Critical applications in Wave 0 or Wave 1
- Latency-sensitive dependency pairs in the same wave
- Wave 0 PoC includes a representative VM type for tooling validation

HOW THIS FEEDS DOWNSTREAM
→ Part 2 SOW: Wave plan is the primary scope input for Part 2 migration factory
→ Year 1 TCO: Wave plan drives the Year 1 dual-running cost model

QUESTIONS?
Refer to docs/guides/04-planning-phase-guide.md
```

### `governance-model.xlsx` — Instructions Tab

```
GOVERNANCE MODEL & RACI
CRA Framework — Phase 1: Kickoff / Phase 4: Planning

PURPOSE
Define roles, responsibilities, and accountabilities for the CRA engagement and the
subsequent Part 2 migration. Share with the customer at the Phase 1 kickoff meeting.

WHO FILLS THIS IN
Delivery Manager (RACI framework) + Lead Architect (technical rows)
Agreed with: Customer IT Director and Customer PM at kickoff

WHEN IN THE ENGAGEMENT
Phase 1 week 1. Update at each phase boundary if roles change.

STEP-BY-STEP
1. Add actual names to role columns (replace [Lead Arch] with the named architect)
2. Review RACI rows with the customer — confirm A (Accountable) assignments
3. Flag rows with no customer Accountable owner as risks
4. Attach to kickoff meeting pack and email for customer record
5. Update Governance Review tab at each phase boundary

HOW THIS FEEDS DOWNSTREAM
→ Phase 2–4: Use RACI to identify who must attend workshops or sign deliverables
→ Risk Register: RACI gaps become risks to log in risk-assessment.xlsx

QUESTIONS?
Refer to docs/guides/00-architect-onboarding-guide.md
```

---

*Template audit spec for CRA Framework v2.0 — Rackspace Cloud Solutions Architecture*
