# Rackspace CRA — AWS Migration Acceleration Programme Alignment

**Version:** 1.0  
**Date:** June 2026  
**Audience:** AWS Partner Managers, Alliance Architects, Rackspace Pre-Sales  
**Purpose:** Maps Rackspace CRA phases to AWS MAP phases and identifies CRA outputs that satisfy AWS Migration Acceleration Programme (MAP) deal registration and funding requirements

---

## Executive Summary

The Rackspace Cloud Readiness Accelerator (CRA) is structurally aligned to the AWS Migration Acceleration Programme (MAP). CRA Phase 1–4 deliverables map directly to the MAP Assess and Mobilize stages and produce the technical assessment outputs required for MAP funding eligibility and deal registration.

This document is the reference guide for Rackspace–AWS co-sell conversations. It enables AWS partner managers to confirm CRA as a qualifying assessment methodology and enables Rackspace delivery teams to identify MAP funding eligibility during scoping.

---

## 1. AWS MAP Phase-to-CRA Phase Mapping

| MAP Phase | MAP Purpose | CRA Phase | CRA Deliverables That Satisfy It |
|---|---|---|---|
| **Assess** | Migration Readiness Assessment (MRA); baseline current-state inventory; business case; initial migration strategy | **Phase 1: Discovery** + **Phase 2: Analysis** | Application inventory, infrastructure profiling, 5-dimension readiness scores, dependency map, MRA-equivalent readiness baseline |
| **Mobilize** | Detailed migration plan, wave sequencing, skills readiness, landing zone design, pilot migration | **Phase 3: Evaluation** + **Phase 4: Planning** | AWS TCO model, hyperscaler recommendation, migration wave plan, Part 2 entry point, governance model, risk register |
| **Migrate & Modernize** | Full migration execution; optimization; Well-Architected Reviews | Post-CRA (Part 2) | CRA provides the baseline and wave plan; migration execution is a separate Part 2 engagement |

### Visual Mapping

```
MAP:     Assess                  Mobilize              Migrate & Modernize
           │                        │                          │
           ▼                        ▼                          ▼
CRA:   [Phase 1+2]            [Phase 3+4]               [Part 2 ops]
        Discovery &             Evaluation &              Migration
        Analysis                Planning                  execution
        Inventory &             TCO/AWS                   Wave-by-wave
        Readiness               architecture              Handoff to
        scoring                 Wave plan                 delivery team
                                Risk register
```

---

## 2. MAP Funding Eligibility

### What MAP Requires

AWS Migration Acceleration Programme provides funding and support for migration engagements delivered by qualified AWS Partners. Eligibility requires:

| MAP Requirement | Required Evidence | Satisfied By |
|---|---|---|
| Migration Readiness Assessment (MRA) | Formal assessment of current state covering people, process, technology, and business | CRA Phase 1 + Phase 2: application inventory, infrastructure profiling, 5-dimension readiness scores |
| Current-state inventory | Server and application inventory with specifications | CRA Phase 1: application-scoping-profiling.xlsx + infrastructure-profiling.xlsx |
| Business case with TCO analysis | 3–5 year TCO comparison including AWS pricing | CRA Phase 3: business-case-tco-roi.xlsx + aws-evaluation.xlsx |
| Migration wave plan | Sequenced migration roadmap | CRA Phase 4: migration-wave-planner.xlsx |
| AWS as primary or co-primary recommendation | Assessment outcome identifies AWS as a recommended platform | CRA Phase 3: hyperscaler-decision-matrix.xlsx (AWS scored and evidenced) |
| APN Partner with Migration Competency | Partner-led engagement by qualified AWS partner | Rackspace AWS Partner status ✅ |
| ACE deal registration | Opportunity registered in AWS Customer Engagements (ACE) portal | Must be registered by Rackspace PDM at engagement start |

### MAP Funding Tiers (Reference)

| Tier | Scope | Typical Support |
|---|---|---|
| MAP Assess | Migration Readiness Assessment only (CRA Phase 1–2) | Credits and/or cash funding toward assessment delivery cost |
| MAP Mobilize | Planning and landing zone (CRA Phase 3–4) | AWS credits toward proof-of-concept and infrastructure build |
| MAP Migrate | Active migration execution (Part 2) | Cash funding based on workload type and migration complexity |

> **Important:** MAP programme terms, funding amounts, and eligibility criteria change annually. Always verify with your AWS PDM (Partner Development Manager) at engagement start. The above is reference-only.

### When to Screen for MAP Eligibility

**Screening must happen at SoW scoping — not after the assessment is complete.** Complete the following checklist before the SoW is signed:

- [ ] Is AWS a likely primary or co-primary recommendation for this customer?
- [ ] Does the customer have an active AWS account or a committed workload migration?
- [ ] Is the infrastructure footprint above the MAP minimum threshold (typically 50+ servers or equivalent cloud spend)?
- [ ] Does Rackspace have an active ACE opportunity registered for this engagement?
- [ ] Is the AWS field account team aware of this engagement?
- [ ] Does the customer have SQL Server, Windows Server, or Oracle licences that benefit from AWS licensing programmes (License Included vs. BYOL)?

Identifying MAP eligibility at scoping reduces effective delivery cost and strengthens the customer business case.

---

## 3. AWS Migration Hub Integration

AWS Migration Hub is the central tracking service for migrations to AWS. CRA supports Migration Hub as a planning and tracking integration point:

| CRA Phase | Migration Hub Integration Point |
|---|---|
| Phase 1: Discovery | AWS Application Discovery Service (ADS) agentless collector can be deployed as a discovery source alongside CRA manual templates; ADS outputs feed into application-scoping-profiling.xlsx |
| Phase 2: Analysis | Migration Hub import tool accepts inventory data exported from CRA templates (CSV format); enables Migration Hub portfolio view at no additional cost |
| Phase 3: Evaluation | AWS Migration Evaluator generates TCO estimates that supplement CRA aws-evaluation.xlsx; Evaluator outputs can be imported as a data point into the business case |
| Phase 4: Planning | Migration wave plan from CRA migration-wave-planner.xlsx can be manually entered into Migration Hub for tracking during Phase 2 (Mobilize) execution |

### AWS Application Discovery Service (Phase 1 Callout)

The AWS ADS agentless collector requires:
- vCenter Server 5.5 or later with read-only service account access
- Outbound HTTPS to AWS Migration Hub endpoint on port 443
- CAB approval for firewall changes (allow 5–10 business days — build into Phase 1 schedule)
- ADS does not collect application-level data by default; agent-based discovery needed for application dependency mapping

CRA Phase 1 guidance explicitly accounts for ADS lead time alongside Azure Migrate and GCP Migration Center tooling.

---

## 4. AWS Migration Evaluator Integration

Migration Evaluator (formerly TSO Logic) provides AWS-native TCO modelling. CRA incorporates Evaluator output as a calibration source:

| Evaluator Output | How CRA Uses It |
|---|---|
| Directional business case (free quick assessment) | Cross-check against CRA aws-evaluation.xlsx PAYG pricing |
| Detailed evaluator report | Input to CRA business-case-tco-roi.xlsx as AWS pricing validation layer |
| On-premises cost modelling | Validates CRA on-prem baseline in business-case-tco-roi.xlsx |
| Reserved Instance and Savings Plans modelling | Mapped to CRA aws-evaluation.xlsx 3-year RI tab |

Evaluator is AWS-only. CRA's multi-cloud TCO model (aws-evaluation.xlsx, azure-evaluation.xlsx, gcp-evaluation.xlsx) provides the hyperscaler comparison that Evaluator cannot.

---

## 5. AWS Well-Architected Framework Alignment

CRA Phase 3 and Phase 4 outputs align to the six AWS Well-Architected Framework pillars:

| WAF Pillar | CRA Output That Addresses It |
|---|---|
| **Operational Excellence** | Governance model (governance-model.xlsx) — RACI, operating model, tagging strategy |
| **Security** | 5-dimension readiness scoring (dimension 3: Security/Compliance) — includes IAM, encryption at rest/transit, compliance requirements |
| **Reliability** | Dependency mapping + migration wave plan — DR strategy, RPO/RTO targets per application |
| **Performance Efficiency** | Right-sizing recommendations from infrastructure profiling + TCO model (optimised tier vs L4L) |
| **Cost Optimization** | Business case TCO model — 3-year RI vs Savings Plans vs On-Demand; MAP credits overlay tab |
| **Sustainability** | Not explicitly modelled in CRA v1 — noted for inclusion in v2 (decommission of on-prem reduces energy footprint) |

A full AWS Well-Architected Review (WAR) is a separate engagement; CRA provides the input data and initial assessment that informs a WAR scope.

---

## 6. MAP Pre-Delivery Checklist

Use this checklist at engagement kick-off to confirm CRA delivery will satisfy MAP alignment and funding requirements:

### Phase 1 (Discovery) — MAP Assess Stage
- [ ] Application inventory will be produced using CRA templates (scoping-profiling.xlsx, infrastructure-profiling.xlsx)
- [ ] AWS Application Discovery Service (or equivalent) deployed if AWS is primary recommendation
- [ ] Utilization data collection minimum 2 weeks confirmed in project schedule
- [ ] MAP eligibility screening completed with AWS PDM; ACE opportunity registered

### Phase 2 (Analysis) — MAP Assess Stage
- [ ] 5-dimension readiness scoring applied to all in-scope applications
- [ ] Licence inventory completed (SQL Server BYOL vs License Included; Oracle licence model)
- [ ] Migration Readiness Assessment (MRA) equivalent outputs confirmed in project deliverables list

### Phase 3 (Evaluation) — MAP Mobilize Stage
- [ ] AWS TCO modelled across at least 2 regions with On-Demand + 3-year RI + Savings Plans variants
- [ ] Migration Evaluator report obtained and cross-referenced against CRA TCO model
- [ ] Hyperscaler decision matrix completed with AWS scored against Azure and GCP
- [ ] Business case includes on-prem status quo, Year 1 dual-running, and 3-year cloud cost
- [ ] MAP deliverables package confirmed with AWS field team

### Phase 4 (Planning) — MAP Mobilize Stage
- [ ] Migration wave plan aligned to AWS Landing Zone Accelerator or Control Tower landing zone design
- [ ] Governance model references AWS Control Tower, AWS Organizations, and AWS Cost Explorer
- [ ] Part 2 entry point document produced with AWS-specific execution checklist

---

## 7. Reference Engagement: DMG Media UK

The DMG Media UK engagement (June 2026) is the CRA framework's reference implementation. AWS was evaluated as part of the 3-way hyperscaler assessment:

| Criterion | DMG Outcome |
|---|---|
| MAP alignment | CRA Phases 1–2 produced MRA-equivalent outputs; AWS scored in hyperscaler decision matrix |
| AWS pricing model | AWS MPA pricing modelled across 3 regions (Frankfurt, Ireland, London) — files in Examples/aws/ |
| AWS outcome | Azure UK South selected as primary; AWS retained as secondary consideration for specific workloads |
| Licence review | SQL Server and Windows Server licences reviewed; AWS BYOL and License Included both modelled |
| Business case | AWS 3-year RI pricing included in multi-cloud comparison in business-case-tco-roi.xlsx |

Reference AWS pricing examples: [Examples/aws/](../Examples/aws/)

Full case study: [Examples/media-entertainment/dmg-media-uk-case-study.md](../Examples/media-entertainment/dmg-media-uk-case-study.md)

---

## 8. Related Documents

| Document | Location | Purpose |
|---|---|---|
| CRA Methodology | [docs/METHODOLOGY.md](METHODOLOGY.md) | Full four-phase assessment model |
| Discovery Phase Guide | [docs/guides/01-discovery-phase-guide.md](guides/01-discovery-phase-guide.md) | Phase 1 delivery guide |
| AWS Evaluation Template | `Templates/03-evaluation/aws-evaluation.xlsx` | On-Demand + 3-year RI + Savings Plans TCO model |
| Business Case Template | `Templates/03-evaluation/business-case-tco-roi.xlsx` | Full TCO comparison with MAP-ready outputs |
| Hyperscaler Decision Matrix | `Templates/03-evaluation/hyperscaler-decision-matrix.xlsx` | Weighted 3-way evaluation |
| Microsoft CAF Alignment | [docs/MICROSOFT-CAF-ALIGNMENT.md](MICROSOFT-CAF-ALIGNMENT.md) | CRA alignment to Microsoft CAF and AMM programme |
| GCP PSO Alignment | [docs/GOOGLE-PSO-ALIGNMENT.md](GOOGLE-PSO-ALIGNMENT.md) | CRA alignment to Google Cloud PSO and Migration Center |
| AWS MPA Pricing Examples | [Examples/aws/](../Examples/aws/) | Real MPA pricing examples across 3 regions |
| DMG Case Study | [Examples/media-entertainment/dmg-media-uk-case-study.md](../Examples/media-entertainment/dmg-media-uk-case-study.md) | Reference engagement with multi-cloud evaluation outcome |

---

*Rackspace Technology — Cloud Solutions Architecture*  
*For AWS partner alignment queries, contact your Rackspace Alliance Partner Manager.*  
*© 2026 Rackspace Technology. All rights reserved.*
