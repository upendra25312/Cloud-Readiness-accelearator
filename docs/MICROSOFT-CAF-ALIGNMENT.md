# Rackspace CRA — Microsoft Cloud Adoption Framework Alignment

**Version:** 1.0  
**Date:** June 2026  
**Audience:** Microsoft Partner Managers, Alliance Architects, Rackspace Pre-Sales  
**Purpose:** Maps Rackspace CRA phases to Microsoft CAF stages and identifies CRA outputs that satisfy Azure Migration and Modernisation (AMM) funding requirements

---

## Rackspace Microsoft Partner Designation

Rackspace holds the following Microsoft partner designations, which are relevant to CRA co-sell and AMM funding conversations:

| Designation | Relevance to CRA |
|---|---|
| **Azure Expert MSP** | Highest Microsoft managed-services partner tier; confirms delivery capability for AMM-qualifying assessments |
| **Azure Migration and Modernization Advanced Specialization** | Confirms validated competency in Azure migration assessments — required for higher AMM funding tiers |
| **Microsoft AI Cloud Partner Programme — Solutions Partner** | Enables co-sell designation and Partner Center deal registration for co-sell incentives |

> Always confirm current designation status with the Rackspace Microsoft Alliance Manager before presenting to a Microsoft PDM. Designations are renewed annually and the above may have been updated since this document was last revised.

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
| **Migrate** | Migration wave execution | **Phase 4: Planning** | Migration wave plan, Part 2 entry point, risk register, governance charter. **Oracle RAC workloads:** Oracle Database@Azure (OCI/Azure interconnect) is the primary path for Oracle RAC/Exadata in Azure; AVS is the path for Solaris and VMware lift workloads only. |
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

### AMM Funding Mechanism

AMM funding is **not** a flat-fee payment. It is delivered through Microsoft's Partner Investment Engine (PIE) as co-investment credits applied against the partner's qualifying delivery costs or against the customer's Azure consumption commitment. The process:

1. Rackspace Alliance Manager registers the opportunity in **Microsoft Partner Center** (Solutions Partner deal registration — ACE) **before the SoW is signed**
2. Rackspace submits qualifying CRA deliverables to the Microsoft PDM as AMM evidence
3. Microsoft approves the PIE claim; funding is applied as credits (against Rackspace billing or Azure consumption) — not as a direct payment
4. Migration and modernisation funding tiers unlock additional credits tied to Azure consumption milestones post-assessment

### AMM Funding Tiers (Reference)

| Tier | Scope | Typical Co-investment |
|---|---|---|
| Assessment co-investment | Cloud readiness assessment only (CRA Phase 1–4) | Variable — based on approved scope and market; PDM to confirm at engagement start |
| Migration co-investment | Active migration execution (Part 2) | Tied to Azure consumption commitment; varies by workload type |
| Modernisation co-investment | PaaS refactoring, containerisation, data platform | Additional tier stacked on top of migration co-investment |

> **Important:** AMM programme terms, funding structure, and eligibility criteria are updated annually by Microsoft. The co-investment value and mechanism vary by market, partner designation tier, and programme year. Always verify with your Microsoft PDM and the Rackspace Microsoft Alliance Manager at engagement start. Do not quote specific dollar amounts to customers without PDM confirmation.

### When to Screen for AMM Eligibility

**Screening must happen at SoW scoping — not after the assessment is complete.** The AMM pre-qualification checklist should be completed before the SoW is signed:

- [ ] Is Azure the likely primary recommendation (or is it a genuine multi-cloud evaluation)?
- [ ] Does the customer have Windows Server or SQL Server licences eligible for Azure Hybrid Benefit?
- [ ] Does the customer have EoL OS VMs (Windows Server 2008/2012, SQL Server 2012/2014) eligible for free Azure Extended Security Updates?
- [ ] Is the customer's infrastructure footprint above the AMM minimum threshold?
- [ ] Does Rackspace have an active co-sell relationship with the customer's Microsoft account team?
- [ ] Is the Microsoft field team aware of this engagement?
- [ ] **Has the Rackspace Microsoft Alliance Manager registered this opportunity in Microsoft Partner Center (Solutions Partner deal registration) before the SoW is signed?** Deal registration must precede SoW signature — AMM co-investment is not available retroactively.
- [ ] Is the Rackspace Microsoft Alliance Manager confirmed as the ACE opportunity owner in Partner Center?

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

### SMART-to-CRA Handoff Protocol

Microsoft PDMs need an operationalised handoff, not just a positioning statement. The four-step protocol:

| Step | Action | Owner | Target SLA |
|---|---|---|---|
| 1 | Customer completes SMART; SMART score is amber or red | Customer / Microsoft PDM | At time of SMART completion |
| 2 | Microsoft PDM contacts Rackspace Alliance Manager with customer name, SMART score, and account team details | Microsoft PDM → Rackspace Alliance Manager | Within 2 business days of SMART result |
| 3 | Rackspace Alliance Manager confirms co-sell eligibility; schedules joint scoping call with customer | Rackspace Alliance Manager | Within 3 business days of PDM contact |
| 4 | Rackspace registers opportunity in Partner Center (ACE); joint scoping call completed; CRA SoW drafted | Rackspace Alliance Manager + Pre-Sales | Within 10 business days of SMART result |

> A SMART score of green does not eliminate CRA opportunity — SMART is self-service and Azure-only. Green SMART scores on VMware-heavy estates (>500 VMs) or complex database environments frequently understate migration complexity. Use CRA scoping templates to determine whether a formal assessment is warranted regardless of SMART colour.

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
| **Extended Security Updates — Windows Server 2008/2012** | **3 years of free ESU on Azure** (no additional charge; customer must be on paid support or have active SA) | **Flag all EoL OS VMs in Phase 1 Data Quality Report; quantify ESU cost avoidance vs. AWS/GCP in TCO model** |
| **Extended Security Updates — SQL Server 2012/2014** | **3 years of free ESU on Azure** | **Captured in business-case-tco-roi.xlsx licensing overlay tab; model as Azure-only saving** |

> **ESU is frequently the most significant Year 1 Azure financial advantage for customers with EoL operating systems.** On AWS and GCP, customers must purchase ESU separately from Microsoft or accept the compliance and security exposure. At scale (50+ EoL VMs), this is often worth more than the AHB saving in Year 1. Always quantify it explicitly in Phase 3 and include it in the executive business case.

CRA TCO outputs clearly separate AHB-impacted, ESU-impacted, and non-AHB pricing to make the full licence benefit explicit in the business case.

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
- [ ] Landing zone design references the **Azure Landing Zone (ALZ) Accelerator** as the starting point — see [ALZ Accelerator documentation](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/alz-overview) and [ALZ Bicep reference implementation](https://github.com/Azure/ALZ-Bicep). ALZ Accelerator is the Microsoft-standard CAF-aligned enterprise landing zone; custom designs should be justified as deviations from ALZ, not the other way around.
- [ ] Oracle RAC migration path confirmed: **Oracle Database@Azure** (OCI/Azure interconnect, GA in UK South and North Europe) is the primary path for Oracle RAC and Exadata workloads. Azure VMware Solution (AVS) is the path for Solaris and VMware-only lift workloads.
- [ ] Governance model references Azure Policy, Microsoft Defender for Cloud, Azure Cost Management, and the **Microsoft FinOps Toolkit**
- [ ] Part 2 entry point document produced with Azure-specific execution checklist
- [ ] Alliance partner deal registration confirmed in Microsoft Partner Center before Part 2 SoW is issued

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
