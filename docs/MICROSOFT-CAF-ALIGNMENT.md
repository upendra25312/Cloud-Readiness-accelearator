# Rackspace CRA — Microsoft Cloud Adoption Framework Alignment

**Version:** 1.0  
**Date:** June 2026  
**Audience:** Microsoft Partner Managers, Alliance Architects, Rackspace Pre-Sales  
**Purpose:** Maps Rackspace CRA phases to Microsoft CAF stages and identifies CRA outputs that satisfy Azure Migration and Modernisation (AMM) funding requirements

---

## Executive Summary

The Rackspace Cloud Readiness Accelerator (CRA) is structurally aligned to the Microsoft Cloud Adoption Framework (CAF). CRA Phase 1–4 deliverables map directly to the CAF Strategy → Plan → Ready → Migrate stages and produce the technical assessment outputs required for Microsoft Azure Migration and Modernisation (AMM) programme funding eligibility.

This document is the reference guide for Rackspace–Microsoft co-sell conversations. It enables Microsoft partner managers to confirm CRA as a qualifying assessment methodology and enables Rackspace delivery teams to identify AMM funding eligibility during scoping.

---

## 1. CAF Stage-to-CRA Phase Mapping

| CAF Stage | CAF Purpose | CRA Phase | CRA Deliverables That Satisfy It |
|---|---|---|---|
| **Strategy** | Define cloud motivation, business outcomes, business justification | Pre-engagement scoping | Business drivers workshop, scope statement, stakeholder alignment (inputs to SoW) |
| **Plan** | Application inventory, digital estate rationalization, initial migration plan | **Phase 1: Discovery** + **Phase 2: Analysis** | Application inventory, infrastructure profiling, 5-dimension readiness scores, dependency map |
| **Ready** | Landing zone design, architecture review, skills readiness | **Phase 3: Evaluation** | Right-sizing recommendations, Azure architecture alignment, Azure Hybrid Benefit model, AMM eligibility screening |
| **Migrate** | Migration wave execution | **Phase 4: Planning** | Migration wave plan, Part 2 entry point, risk register, governance charter |
| **Govern** | Cloud governance policies, cost management | Phase 4 Planning (governance output) | Governance model template, RACI, operating model design |
| **Manage** | Operational baseline, business commitments | Post-CRA (Part 2 operations) | CRA provides the baseline; ongoing operations model handed to managed services |

### Visual Mapping

```
CAF:     Strategy       Plan            Ready          Migrate        Govern/Manage
           │              │               │               │                │
           ▼              ▼               ▼               ▼                ▼
CRA:   [Pre-scope]  [Phase 1+2]      [Phase 3]       [Phase 4]       [Part 2 ops]
        SoW &        Discovery &      Evaluation      Planning         Handoff to
        Business     Analysis         TCO/Azure       Wave plan        managed
        Drivers      Inventory &      architecture    Migration        services
                     Readiness        AMM screen      roadmap
                     scoring
```

---

## 2. AMM Funding Eligibility

### What AMM Requires

Microsoft Azure Migration and Modernisation (AMM) provides funding for migration engagements delivered by qualified Microsoft partners. Funding eligibility requires the partner to demonstrate:

| AMM Requirement | Required Evidence | Satisfied By |
|---|---|---|
| Qualified assessment methodology | Documented, repeatable assessment process | CRA METHODOLOGY.md + phase guides |
| Current-state inventory | Application and infrastructure inventory | CRA Phase 1: application-scoping-profiling.xlsx + infrastructure-profiling.xlsx |
| Readiness assessment | Multi-dimensional readiness scoring | CRA Phase 2: cloud-readiness-scoring-v2.xlsx |
| TCO/ROI analysis | 3–5 year cost comparison with cloud alternative | CRA Phase 3: business-case-tco-roi.xlsx |
| Azure as primary recommendation | Hyperscaler evaluation with Azure recommended | CRA Phase 3: hyperscaler-decision-matrix.xlsx |
| Migration wave plan | Sequenced application migration roadmap | CRA Phase 4: migration-wave-planner.xlsx |
| Partner co-sell status | Active Microsoft co-sell designation | Rackspace Microsoft co-sell status ✅ |

### AMM Funding Tiers (Reference)

| Tier | Scope | Typical Funding |
|---|---|---|
| Assessment funding | Cloud readiness assessment only (CRA Phase 1–4) | Up to $25K USD (varies by market and programme year) |
| Migration funding | Active migration execution (Part 2) | Varies by workload type and Azure consumption commitment |
| Modernisation funding | PaaS refactoring, containerisation, data platform | Additional funding stack on top of migration tier |

> **Important:** AMM programme terms, funding amounts, and eligibility criteria are updated annually by Microsoft. Always verify with your Microsoft PDM (Partner Development Manager) at engagement start. The above figures are reference-only.

### When to Screen for AMM Eligibility

**Screening must happen at SoW scoping — not after the assessment is complete.** The AMM pre-qualification checklist should be completed before the SoW is signed:

- [ ] Is Azure the likely primary recommendation (or is it a genuine multi-cloud evaluation)?
- [ ] Does the customer have Windows Server or SQL Server licences eligible for Azure Hybrid Benefit?
- [ ] Is the customer's infrastructure footprint above the AMM minimum threshold?
- [ ] Does Rackspace have an active co-sell relationship with the customer's Microsoft account team?
- [ ] Is the Microsoft field team aware of this engagement?

Identifying AMM eligibility at scoping — rather than post-assessment — can reduce the effective Rackspace engagement cost and strengthen the business case for customer sign-off. (The DMG Media UK engagement identified AMM eligibility late; this is now a named lesson learned in the framework.)

---

## 3. SMART Assessment Integration

Microsoft's SMART Assessment tool and Rackspace CRA are complementary, not competitive. The integration model:

| Stage | Tool | Purpose | Output |
|---|---|---|---|
| Pre-sales screening | Microsoft SMART | Free 15-minute Azure readiness check | Initial Azure readiness signal; talking points for first Rackspace call |
| Scoping call | Rackspace CRA templates | Scope and price the CRA engagement | SoW with defined deliverables and timeline |
| Formal assessment | Rackspace CRA (Phase 1–4) | Full multi-cloud readiness assessment | 30–50 page assessment report + board business case |
| Post-assessment | Azure Migrate | Cloud-native migration execution tracking | VM assessment reports, dependency analysis, Azure cost estimates |

SMART outputs can be referenced in Phase 3 (Evaluation) as an additional Azure compatibility data point, but they do not replace CRA's vendor-neutral multi-cloud evaluation. SMART is Azure-only and self-service; CRA is cloud-neutral and formally deliverable.

---

## 4. Azure Migrate Integration

Azure Migrate is the Microsoft-native discovery and assessment tool. CRA supports Azure Migrate as a discovery source alongside GCP Migration Center and RVTools:

| CRA Phase | Azure Migrate Integration Point |
|---|---|
| Phase 1: Discovery | Azure Migrate appliance can be deployed as the primary discovery source; outputs feed directly into CRA application-scoping and infrastructure-profiling templates |
| Phase 3: Evaluation | Azure Migrate assessment outputs (PAYG, 3-year RI, AHB) feed into CRA's azure-evaluation.xlsx TCO model |
| Phase 3: Evaluation | Azure Migrate dependency analysis supplements CRA dependency mapping for Azure-primary recommendations |

### Azure Migrate Appliance Deployment (Phase 1 Callout)

The Azure Migrate appliance requires:
- Outbound HTTPS to Azure on port 443
- CAB approval for firewall rule changes (allow 5–10 business days — build into Phase 1 schedule)
- Service account with read-only vCenter access and WMI/SSH access to target machines
- vCenter version ≥ 6.5

This lead time is the most common cause of Phase 1 delays. CRA Phase 1 guidance explicitly accounts for it.

---

## 5. Azure Hybrid Benefit (AHB) — Modelling in Phase 3

AHB is one of the most significant TCO levers for customers with existing Microsoft licences. CRA's Phase 3 evaluation models AHB explicitly:

| Licence Type | AHB Saving | CRA Model |
|---|---|---|
| Windows Server Standard (with active SA) | Convert Windows VM to Azure at no OS cost | Captured in azure-evaluation.xlsx as AHB variant |
| Windows Server Datacenter (with active SA) | Up to 180 VMs covered per licence | Captured in AHB pricing tab |
| SQL Server Standard/Enterprise (with active SA) | Up to 55% discount on Azure SQL / SQL MI | Modelled in business-case-tco-roi.xlsx licensing overlay tab |

CRA TCO outputs clearly separate AHB-impacted and non-AHB pricing to make the licence benefit explicit in the business case.

---

## 6. CAF Align Checklist — Pre-Delivery

Use this checklist at engagement kick-off to confirm CRA delivery will satisfy CAF alignment and AMM eligibility requirements:

### Phase 1 (Discovery) — CAF Plan Stage
- [ ] Application inventory will be produced using CRA templates (scoping-profiling.xlsx, infrastructure-profiling.xlsx)
- [ ] Azure Migrate appliance (or equivalent) deployed and CAB tickets submitted
- [ ] Utilization data collection minimum 2 weeks confirmed in project schedule
- [ ] AMM eligibility screening completed with Microsoft PDM

### Phase 2 (Analysis) — CAF Plan Stage
- [ ] 5-dimension readiness scoring applied to all in-scope applications
- [ ] Windows Server and SQL Server licence inventory completed (AHB qualification)
- [ ] Compliance and data residency requirements documented (UK/EU if applicable)

### Phase 3 (Evaluation) — CAF Ready Stage
- [ ] Azure TCO modelled across at least 2 regions with PAYG + 3-year RI + AHB variants
- [ ] Hyperscaler decision matrix completed with Azure scored against AWS and GCP
- [ ] Business case includes on-prem status quo, Year 1 dual-running, and 3-year cloud cost
- [ ] AMM deliverables package confirmed with Microsoft field team

### Phase 4 (Planning) — CAF Migrate Stage
- [ ] Migration wave plan aligns to Azure landing zone design (hub-spoke or Azure Virtual WAN)
- [ ] Governance model references Azure Policy, Defender for Cloud, and Cost Management
- [ ] Part 2 entry point document produced with Azure-specific execution checklist

---

## 7. Reference Engagement: DMG Media UK

The DMG Media UK engagement (June 2026) is the CRA framework's reference implementation for Microsoft CAF and AMM alignment:

| Criterion | DMG Outcome |
|---|---|
| CAF alignment | Phases 1–4 delivered; output mapped to CAF Strategy → Migrate |
| AMM eligibility | Identified during engagement; qualification confirmed with Microsoft UK field team |
| AHB opportunity | Significant Windows Server and SQL Server estate — AHB modelled in TCO (material saving) |
| Azure Hybrid Benefit saving | Included in board business case |
| Azure recommendation | Azure UK South primary; North Europe DR/secondary |
| Outcome | AMM funding eligibility confirmed; Rackspace co-sell deal registered |

Full case study: [Examples/media-entertainment/dmg-media-uk-case-study.md](../Examples/media-entertainment/dmg-media-uk-case-study.md)

---

## 8. Related Documents

| Document | Location | Purpose |
|---|---|---|
| CRA Methodology | [docs/METHODOLOGY.md](METHODOLOGY.md) | Full four-phase assessment model |
| Discovery Phase Guide | [docs/guides/01-discovery-phase-guide.md](guides/01-discovery-phase-guide.md) | Phase 1 delivery guide |
| Azure Evaluation Template | `Templates/03-evaluation/azure-evaluation.xlsx` | PAYG + 3-year RI + AHB TCO model |
| Business Case Template | `Templates/03-evaluation/business-case-tco-roi.xlsx` | Full TCO comparison with AMM-ready outputs |
| Hyperscaler Decision Matrix | `Templates/03-evaluation/hyperscaler-decision-matrix.xlsx` | Weighted 3-way evaluation |
| AWS MAP Alignment | [docs/AWS-MAP-ALIGNMENT.md](AWS-MAP-ALIGNMENT.md) | CRA alignment to AWS Migration Acceleration Programme |
| GCP PSO Alignment | [docs/GOOGLE-PSO-ALIGNMENT.md](GOOGLE-PSO-ALIGNMENT.md) | CRA alignment to Google Cloud PSO and Migration Center |
| DMG Case Study | [Examples/media-entertainment/dmg-media-uk-case-study.md](../Examples/media-entertainment/dmg-media-uk-case-study.md) | Reference engagement with AMM eligibility outcome |

---

*Rackspace Technology — Cloud Solutions Architecture*  
*For Microsoft partner alignment queries, contact your Rackspace Alliance Partner Manager.*  
*© 2026 Rackspace Technology. All rights reserved.*
