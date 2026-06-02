# Discovery Templates Audit Specification

**Covers Epics:** 4A.1 – 4A.5  
**Templates in scope:**
- `Templates/01-discovery/application-scoping-profiling.xlsx` (4A.1)
- `Templates/01-discovery/infrastructure-profiling.xlsx` (4A.2)
- `Templates/01-discovery/dependency-mapping.xlsx` (4A.3)
- `Templates/01-discovery/saas-application-assessment.xlsx` (4A.4 — to be created)

**How to use this spec:** Open each template. Compare against the required column list. Add missing columns and the Instructions tab. This is a data collection quality gate — everything downstream (TCO, readiness scoring, hyperscaler recommendation) is only as accurate as Phase 1 data.

---

## 4A.1 — Application Scoping & Profiling (`application-scoping-profiling.xlsx`)

### Purpose

This is the master application inventory. Every in-scope application must have a complete row before Phase 2 (readiness scoring) can begin.

### Required Tab Structure

| Tab | Purpose |
| --- | --- |
| Instructions | Who fills this in, when, how (see Epic 10.4) |
| Application Inventory | One row per application — all fields below |
| Lookup — Tech Stack | Dropdown values for tech stack fields |
| Lookup — Readiness (provisional) | Preliminary cloud readiness flags (not the Phase 2 score — just initial signal) |
| Summary | Totals: app count, owner confirmed %, data quality % |

### Required Columns — Application Inventory Tab

| Column | Data Type | Source | Notes |
| --- | --- | --- | --- |
| App ID | Auto-number | System | Unique identifier for cross-reference |
| Application Name | Text | Customer | Official name |
| Business Owner | Text | Customer | Name + team; needed for Phase 2 interviews |
| Technical Owner / Lead | Text | Customer | Dev lead or platform engineer |
| Business Unit | Dropdown | Customer | Which BU uses this app |
| Business Criticality | Dropdown: Critical / High / Medium / Low | Customer | Drives wave sequencing in Phase 4 |
| Users (internal) | Number | Customer | Daily active users |
| Users (external / customer-facing) | Number | Customer | Revenue-generating traffic flag |
| Tech Stack — Frontend | Text | Customer / Discovery | e.g., React, Java, .NET |
| Tech Stack — Backend | Text | Customer / Discovery | |
| Tech Stack — Database | Dropdown | Customer / Discovery | SQL Server / Oracle / MySQL / PostgreSQL / MongoDB / Redis / Other |
| Database Version | Text | Discovery | Critical for EoL detection |
| OS | Dropdown | Discovery | Windows / Linux / Other |
| OS Version | Text | Discovery | Critical for EoL detection |
| VM Count (primary) | Number | Discovery | Prod VMs only |
| VM Count (non-prod) | Number | Discovery | Dev/test/staging |
| VM Names (list) | Text | Discovery | Pipe-separated list for cross-reference to infrastructure tab |
| Dependencies — Upstream | Text | Customer | What does this app call? |
| Dependencies — Downstream | Text | Customer | What calls this app? |
| External Integrations | Text | Customer | Third-party APIs, SaaS services |
| Data Classification | Dropdown: Public / Internal / Confidential / Restricted | Customer | Affects cloud placement and compliance |
| Regulatory Requirements | Multi-select: GDPR / FCA / PCI / HIPAA / ISO27001 / None | Customer | Affects cloud region selection |
| Licensing — Microsoft | Dropdown: SA / PAYG / OEM / None | Customer | AHB eligibility |
| Licensing — Oracle | Dropdown: BYOL-Processor / BYOL-NUP / None | Customer | Oracle practice flag |
| Licensing — Other OSS risks | Text | Technical review | Redis / Elasticsearch / MongoDB / HashiCorp flags |
| Planned Retirement? | Dropdown: Yes / No / TBC | Customer | If Yes — do not include in TCO |
| Provisional Cloud Path | Dropdown: Rehost / Replatform / Rearchitect / Repurchase / Retire / Retain / TBC | Lead Architect | Phase 1 first-pass; refined in Phase 2 |
| Scope Confidence | Dropdown: High / Medium / Low | Lead Architect | Low = VM count or owner is unconfirmed |
| Oracle Practice Flag | Dropdown: Yes / No | Lead Architect | Set Yes if any Oracle workload — triggers Oracle practice engagement |
| Notes | Text | Any | Free text |
| Last Updated | Date | System | |
| Confirmed By | Text | | App owner name who validated the row |

### Scale Requirement (from SOW)

The template must handle 200+ applications without performance issues. Verify:
- No hardcoded row limits in formulas (use full-column references, not fixed ranges)
- Filter and sort work on all columns
- The Summary tab counts are dynamic (COUNTIF, not hardcoded)

### Instructions Tab Content

```
PURPOSE: Capture one row per in-scope application. This data feeds directly into:
  - Phase 2 readiness scoring (cloud readiness scores)
  - Phase 3 TCO modelling (VM counts, licensing)
  - Phase 4 wave planning (criticality, dependencies)

WHO FILLS THIS IN: Lead Architect (initial pass) + Application Owners (validation)

WHEN: Phase 1 weeks 1–4. App owners must confirm their rows before Phase 2 starts.

WHAT "GOOD DATA" LOOKS LIKE:
  - Every row has a confirmed Business Owner
  - VM count matches the infrastructure profiling template
  - Oracle and SQL Server licences are captured
  - No TBC in Business Criticality for Tier-1 applications

COMMON MISTAKES:
  - Forgetting non-production VMs (dev/test/staging can be 2-3x the prod count)
  - Not capturing Oracle version (affects licensing path)
  - Missing external integrations (breaks dependency mapping)
  - Treating "Planned Retirement" apps as out-of-scope before confirming decommission date
```

---

## 4A.2 — Infrastructure Profiling (`infrastructure-profiling.xlsx`)

### Purpose

One row per server/VM. This is the authoritative inventory used to populate the TCO evaluation templates. It is the primary output of the discovery tooling (Azure Migrate, GCP Migration Center, AWS ADS).

### Required Tab Structure

| Tab | Purpose |
| --- | --- |
| Instructions | Who fills this in, when, how |
| VM Inventory | One row per VM/server |
| Physical Servers | One row per physical host |
| Storage Inventory | Storage arrays, NAS, SAN |
| Network Summary | High-level network segments (not detailed — that is Phase 2) |
| Data Quality Summary | % profiled, % with utilisation data, data age |

### Required Columns — VM Inventory Tab

| Column | Source | Notes |
| --- | --- | --- |
| VM ID | Discovery tool | Unique identifier |
| VM Name / Hostname | Discovery tool | |
| Application Name | Cross-ref from application-scoping-profiling.xlsx | Join key |
| App ID | Cross-ref | Foreign key |
| vCPU Allocated | Discovery tool | |
| vCPU Peak (P95) | Utilisation data | Critical for right-sizing |
| vCPU Average | Utilisation data | |
| RAM Allocated (GB) | Discovery tool | |
| RAM Peak % (P95) | Utilisation data | Critical for right-sizing |
| RAM Average % | Utilisation data | |
| Storage Allocated (GB) | Discovery tool | |
| Storage Used (GB) | Discovery tool | |
| Storage IOPS Peak | Utilisation data | Critical for Premium SSD vs Standard tier |
| Network In (Mbps avg) | Utilisation data | |
| Network Out (Mbps avg) | Utilisation data | |
| OS | Discovery tool | Windows / Linux / Other |
| OS Version | Discovery tool | |
| OS End of Life? | Calculated from OS version | Flag for ESU cost |
| Hypervisor | Discovery tool | VMware / Hyper-V / KVM / Physical |
| ESX Host | Discovery tool | For VMware licensing analysis |
| Data Centre / Location | Manual | DC name |
| Business Criticality | From application-scoping-profiling.xlsx | Cross-referenced |
| Provisional Cloud SKU (Azure) | Lead Architect | Mapped based on CPU/RAM |
| Provisional Cloud SKU (AWS) | Lead Architect | |
| Provisional Cloud SKU (GCP) | Lead Architect | |
| Utilisation Data Days | Calculated | Count of days with data |
| Data Quality | Calculated: High (≥14d) / Medium (7–14d) / Low (<7d) | Gate check for Phase 3 |

### Utilisation Data Gate Column

Add a calculated column:

```
Phase 3 Ready?
= IF(UtilisationDataDays >= 14, "✅ Ready", IF(UtilisationDataDays >= 7, "⚠️ Marginal", "❌ Blocked"))
```

The Phase 3 start gate check: count of "❌ Blocked" rows must be <10% of estate before Phase 3 begins.

### Data Quality Summary Tab

This tab should auto-calculate from the VM Inventory tab:

| Metric | Formula | Target |
| --- | --- | --- |
| Total VMs | COUNT | — |
| VMs with CPU data | COUNTIF | ≥90% |
| VMs with RAM data | COUNTIF | ≥90% |
| VMs with ≥14 days data | COUNTIF | ≥80% |
| VMs with EoL OS | COUNTIF | For information |
| VMs with no Application owner | COUNTIF | Must = 0 before Phase 2 |

---

## 4A.3 — Dependency Mapping (`dependency-mapping.xlsx`)

### Purpose

Capture app-to-app and app-to-infrastructure dependencies at a level sufficient to sequence migration waves. This is NOT a full network dependency map (that is Part 2) — it is the high-level view needed to prevent migrating an app before its dependencies.

### Required Tab Structure

| Tab | Purpose |
| --- | --- |
| Instructions | Who fills this in, when, how |
| App-to-App Dependencies | Application communication matrix |
| App-to-Infrastructure | Shared services dependencies (AD, DNS, NTP, monitoring) |
| External Dependencies | Internet-facing services, SaaS, third-party APIs |
| Dependency Heat Map | Visualisation: which apps have the most dependencies (high-dependency apps go in later waves) |

### Required Columns — App-to-App Dependencies Tab

| Column | Content |
| --- | --- |
| Source App ID | From application-scoping-profiling.xlsx |
| Source App Name | |
| Target App ID | |
| Target App Name | |
| Dependency Type | API / DB / File Share / Message Queue / Web Service / Other |
| Direction | One-way → / Two-way ↔ |
| Protocol / Port | e.g., HTTPS:443, SQL:1433 |
| Latency Sensitive? | Yes / No — latency-sensitive dependencies must be co-migrated |
| Data Volume | Low / Medium / High — affects migration order |
| Can be broken temporarily? | Yes / No — determines if apps can be migrated in separate waves |
| Notes | |

### Dependency Heat Map Tab

Add a calculated summary:

| App Name | Outbound Dependencies | Inbound Dependencies | Total | Wave Sequencing Impact |
| --- | --- | --- | --- | --- |
| [App] | COUNTIF | COUNTIF | Sum | High dependency = later wave |

---

## 4A.4 — SaaS Application Assessment (to be created: `saas-application-assessment.xlsx`)

### Why This Is Needed

SaaS applications have a fundamentally different migration pattern from IaaS/PaaS workloads:
- They do not move to cloud — they are already there
- The assessment question is: "Should we keep this SaaS, replace it, or consolidate it?"
- They affect the TCO baseline (SaaS costs continue whether or not the on-prem estate migrates)

### Required Tab Structure

| Tab | Purpose |
| --- | --- |
| Instructions | Who fills this in, when, how |
| SaaS Inventory | One row per SaaS application |
| SaaS Contract Summary | Renewal dates, costs, vendor contacts |
| Consolidation Opportunities | Where two SaaS tools do the same job |

### Required Columns — SaaS Inventory Tab

| Column | Content |
| --- | --- |
| SaaS App Name | e.g., Salesforce, ServiceNow, Workday |
| Category | CRM / ITSM / HR / Finance / Productivity / Other |
| Business Owner | |
| Users | Monthly active users |
| Annual Cost | £/$ |
| Contract End Date | Critical for migration timing |
| On-Prem Equivalent? | Does the customer also run an on-prem system that does the same job? |
| Migration Relevance | Affects TCO? / Integrate with cloud landing zone? / No impact |
| Recommendation | Keep / Consolidate / Replace with cloud-native |
| Notes | |

---

## 4A.5 — Instructions Tab (all Discovery templates)

**Add an Instructions tab as the first tab in every Discovery template.** This makes each template self-contained — no guide needed.

### Standard Instructions Tab Structure

Each Instructions tab should contain (as plain text in merged cells, not a table):

```
[TEMPLATE NAME]
CRA Framework — Phase 1: Discovery

PURPOSE
[One paragraph explaining what this template captures and why it matters]

WHO FILLS THIS IN
[Roles: Lead Architect (initial pass), Application Owners (validation pass)]

WHEN IN THE ENGAGEMENT
[Phase 1 weeks X–Y. Must be complete before [next phase trigger].]

STEP-BY-STEP
1. [Action 1]
2. [Action 2]
3. [Action 3]
...

WHAT "GOOD DATA" LOOKS LIKE
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

COMMON MISTAKES TO AVOID
- [Mistake 1]
- [Mistake 2]

HOW THIS FEEDS DOWNSTREAM
→ Phase 2: [What this data enables in Phase 2]
→ Phase 3: [What this data enables in Phase 3]
→ Phase 4: [What this data enables in Phase 4]

QUESTIONS?
Refer to docs/guides/01-discovery-phase-guide.md
Contact: [Engagement Lead Architect]
```

---

*Template audit spec for CRA Framework v2.0 — Rackspace Cloud Solutions Architecture*
