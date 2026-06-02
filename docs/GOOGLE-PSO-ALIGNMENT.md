# Rackspace CRA — Google Cloud PSO & Migration Center Alignment

**Version:** 1.0  
**Date:** June 2026  
**Audience:** Google Cloud Partner Managers, Alliance Architects, Rackspace Pre-Sales  
**Purpose:** Maps Rackspace CRA phases to the Google Cloud Adoption Framework (GCAF) stages and identifies CRA outputs that support Google Cloud PSO engagements, Migration Center assessments, and partner migration credit eligibility

---

## Executive Summary

The Rackspace Cloud Readiness Accelerator (CRA) aligns structurally to the Google Cloud Adoption Framework (GCAF) and integrates with Google Cloud's Migration Center tooling. CRA Phase 1–4 deliverables map directly to the GCAF Assess and Plan stages and produce the technical assessment outputs required for Google Cloud PSO engagement qualification and partner migration credit eligibility.

This document is the reference guide for Rackspace–Google Cloud co-sell conversations. It enables Google Cloud partner managers to confirm CRA as a qualifying assessment methodology and enables Rackspace delivery teams to identify GCP migration credit opportunities during scoping.

---

## 1. GCAF Stage-to-CRA Phase Mapping

| GCAF Stage | GCAF Purpose | CRA Phase | CRA Deliverables That Satisfy It |
|---|---|---|---|
| **Assess** | Evaluate current workloads, identify cloud fit, establish baseline TCO | **Phase 1: Discovery** + **Phase 2: Analysis** | Application inventory, infrastructure profiling, 5-dimension readiness scores, dependency map, cloud fit assessment |
| **Plan** | Design target architecture, build migration business case, define wave plan | **Phase 3: Evaluation** + **Phase 4: Planning** | GCP TCO model, hyperscaler recommendation, migration wave plan, landing zone design guidance, governance model |
| **Deploy** | Landing zone build, foundation infrastructure, initial wave migration | Post-CRA (Part 2) | CRA provides the deployment specifications; landing zone build is a separate Part 2 workstream |
| **Optimize** | Cost optimization, SRE practices, finops, Well-Architected Review | Post-CRA (Part 2 ongoing) | CRA TCO model provides the cost optimization baseline; ongoing optimization is a managed services function |

### Visual Mapping

```
GCAF:    Assess                  Plan                  Deploy / Optimize
           │                       │                          │
           ▼                       ▼                          ▼
CRA:   [Phase 1+2]           [Phase 3+4]               [Part 2 ops]
        Discovery &            Evaluation &              Landing zone
        Analysis               Planning                  build and
        Inventory &            GCP TCO                   migration
        Readiness              Architecture              execution
        scoring                Wave plan
```

---

## 2. GCP Migration Credits & PSO Funding

### What GCP Requires for Partner Migration Credits

Google Cloud provides migration credits and PSO funding for qualified partner-led migration engagements. Eligibility typically requires:

| GCP Requirement | Required Evidence | Satisfied By |
|---|---|---|
| Formal migration assessment | Documented, repeatable assessment methodology | CRA METHODOLOGY.md + phase guides |
| Current-state infrastructure inventory | Server and application inventory with specifications | CRA Phase 1: application-scoping-profiling.xlsx + infrastructure-profiling.xlsx |
| Cloud readiness assessment | Multi-dimensional analysis of workload cloud fit | CRA Phase 2: cloud-readiness-scoring-v2.xlsx |
| GCP TCO analysis | Cost comparison with GCP as a modelled option | CRA Phase 3: gcp-evaluation.xlsx + business-case-tco-roi.xlsx |
| Migration wave plan | Sequenced application migration roadmap | CRA Phase 4: migration-wave-planner.xlsx |
| Qualified Google Cloud Partner | Partner-led engagement by Google Cloud Partner | Rackspace Google Cloud Partner status ✅ |
| Opportunity registration | Engagement registered in Google Partner Advantage portal | Must be registered by Rackspace PDM at engagement start |

### GCP Funding Tiers (Reference)

| Tier | Scope | Typical Support |
|---|---|---|
| Assessment credits | Migration assessment (CRA Phase 1–2 equivalent) | Google Cloud credits to offset assessment tooling costs |
| Migration credits | Active migration to GCP (Part 2) | GCP credits applied against consumed compute during migration |
| PSO co-delivery | Google Cloud PSO co-delivery on large or strategic accounts | PSO resource hours at reduced or no cost |

> **Important:** Google Cloud programme terms, credit amounts, and eligibility criteria change periodically. Always verify with your Google Cloud PDM at engagement start. The above is reference-only.

### When to Screen for GCP Credit Eligibility

**Screening must happen at SoW scoping — not after the assessment is complete.** Complete the following before the SoW is signed:

- [ ] Is GCP a likely primary or co-primary recommendation for this customer?
- [ ] Does the customer have an active Google Cloud account or a committed migration workload?
- [ ] Is the infrastructure footprint above GCP's minimum threshold for credit programmes?
- [ ] Has Rackspace registered this opportunity in Google Partner Advantage?
- [ ] Is the Google Cloud field account team aware of this engagement?
- [ ] Does the customer have any Google Workspace or Google Cloud-adjacent workloads that create a natural GCP affinity?

---

## 3. Google Migration Center Integration

Google Migration Center (MC) is Google's SaaS-based migration assessment and planning tool (formerly Migrate for Compute Engine and StratoZone). CRA supports Migration Center as a primary discovery source for GCP-primary or GCP-competitive engagements:

| CRA Phase | Migration Center Integration Point |
|---|---|
| Phase 1: Discovery | Migration Center collector agent or agentless discovery can be deployed as the primary discovery source; outputs (VM specs, OS, utilization) feed directly into CRA infrastructure-profiling.xlsx |
| Phase 2: Analysis | Migration Center portfolio view provides cloud fit scores (Fit for GCE, GKE, or Cloud SQL) that supplement CRA 5-dimension readiness scores |
| Phase 3: Evaluation | Migration Center TCO reports provide GCP-native pricing that is cross-referenced against CRA gcp-evaluation.xlsx; CUDs (Committed Use Discounts) are modelled in both |
| Phase 4: Planning | Migration Center wave plan is an optional parallel track to CRA migration-wave-planner.xlsx for GCP-primary recommendations |

### Migration Center Deployment (Phase 1 Callout)

The Migration Center discovery collector requires:
- vCenter Server 6.5 or later (or VMware ESXi 6.5+) with read-only access
- Outbound HTTPS to googleapis.com on port 443
- CAB approval for firewall changes (allow 5–10 business days — build into Phase 1 schedule)
- Migration Center provides detailed utilization data when collection runs for minimum 1 week (2 weeks recommended for CRA accuracy)

---

## 4. Google Cloud Well-Architected Framework (WAF) Alignment

CRA Phase 3 and Phase 4 outputs align to the five Google Cloud Architecture Framework pillars:

| GC Architecture Framework Pillar | CRA Output That Addresses It |
|---|---|
| **Operational Excellence** | Governance model (governance-model.xlsx) — RACI, operating model, Google Cloud resource hierarchy design |
| **Security, Privacy, and Compliance** | 5-dimension readiness scoring (dimension 3: Security/Compliance) — includes data residency, encryption, IAM, DLP requirements |
| **Reliability** | Dependency mapping + migration wave plan — DR strategy, RPO/RTO targets per application, regional failover design |
| **Cost Optimization** | GCP TCO model (gcp-evaluation.xlsx) — On-Demand + 3-year CUD comparison; Committed Use Discount eligibility per workload |
| **Performance Optimization** | Right-sizing recommendations from infrastructure profiling; GCE machine family mapping (General Purpose, Compute Optimized, Memory Optimized) |

A full Google Cloud Architecture Review is a separate engagement; CRA provides the input data and initial assessment that informs its scope.

---

## 5. StratoZone / Google Cloud Rapid Assessment & Migration Program (RAMP)

Google Cloud RAMP is a structured migration programme for eligible customers. CRA aligns to RAMP's discovery and assessment requirements:

| RAMP Stage | CRA Alignment |
|---|---|
| RAMP Discovery | CRA Phase 1 application and infrastructure inventory satisfies RAMP's current-state baseline requirements |
| RAMP Assessment | CRA Phase 2 readiness scoring maps to RAMP's cloud fit assessment; Migration Center data supplements where available |
| RAMP Business Case | CRA Phase 3 business-case-tco-roi.xlsx satisfies RAMP's TCO and business justification requirements |
| RAMP Migration Plan | CRA Phase 4 migration-wave-planner.xlsx satisfies RAMP's wave planning requirements |

---

## 6. GCE Machine Family Mapping (Phase 3 Callout)

GCP TCO modelling requires selecting the appropriate machine family. CRA Phase 3 evaluation guidance:

| On-Premises Workload Type | Recommended GCE Machine Family | CRA Template Mapping |
|---|---|---|
| General-purpose compute (web, app servers) | N-series (N2, N2D) | gcp-evaluation.xlsx: General Purpose tab |
| High-memory databases (SAP, Oracle, SQL) | M-series (M2, M3) | gcp-evaluation.xlsx: Memory Optimized tab |
| Compute-intensive (CI/CD, batch, HPC) | C-series (C2, C3) | gcp-evaluation.xlsx: Compute Optimized tab |
| High storage I/O (large databases, analytics) | Z3 (storage-optimized) | gcp-evaluation.xlsx: Storage Optimized tab |
| Cost-sensitive/dev/test workloads | E2 (shared-core) | gcp-evaluation.xlsx: Economy tab |

Committed Use Discount (CUD) eligibility: 1-year and 3-year CUDs apply to N, M, and C series machines. CRA gcp-evaluation.xlsx models both On-Demand and 3-year CUD scenarios.

---

## 7. GCP Pre-Delivery Checklist

Use this checklist at engagement kick-off to confirm CRA delivery will satisfy GCP alignment and credit requirements:

### Phase 1 (Discovery) — GCAF Assess Stage
- [ ] Application inventory will be produced using CRA templates (scoping-profiling.xlsx, infrastructure-profiling.xlsx)
- [ ] Google Migration Center collector deployed (or RVTools/Azure Migrate used as alternative) if GCP is in scope
- [ ] Utilization data collection minimum 2 weeks confirmed in project schedule
- [ ] GCP migration credit eligibility screening completed with Google PDM; opportunity registered

### Phase 2 (Analysis) — GCAF Assess Stage
- [ ] 5-dimension readiness scoring applied to all in-scope applications
- [ ] Data residency requirements confirmed (EU, UK, US) — Google Cloud region selection depends on this
- [ ] GCE machine family mapping confirmed for primary workload types

### Phase 3 (Evaluation) — GCAF Plan Stage
- [ ] GCP TCO modelled across at least 2 regions with On-Demand + 3-year CUD variants
- [ ] Migration Center portfolio/TCO report obtained and cross-referenced against CRA gcp-evaluation.xlsx
- [ ] Hyperscaler decision matrix completed with GCP scored against AWS and Azure
- [ ] Business case includes on-prem status quo, Year 1 dual-running, and 3-year cloud cost
- [ ] GCP RAMP deliverables package confirmed with Google Cloud field team if RAMP-eligible

### Phase 4 (Planning) — GCAF Plan Stage
- [ ] Migration wave plan aligned to Google Cloud Landing Zone (resource hierarchy, VPC design, IAM)
- [ ] Governance model references Google Cloud Organizations, Folders, IAM, and Cloud Cost Management
- [ ] Part 2 entry point document produced with GCP-specific execution checklist

---

## 8. Reference Engagement: DMG Media UK

The DMG Media UK engagement (June 2026) is the CRA framework's reference implementation. GCP was evaluated as part of the 3-way hyperscaler assessment and served as the primary discovery tool:

| Criterion | DMG Outcome |
|---|---|
| Migration Center usage | Google Migration Center (formerly StratoZone) was the primary discovery tool for the engagement |
| GCP evaluation | GCP scored in hyperscaler decision matrix; evaluated for UK South region (europe-west2) |
| GCP outcome | Azure UK South selected as primary; GCP remained a viable option for specific containerisation and BigQuery use cases |
| Data residency | UK data residency confirmed — GCP europe-west2 (London) used for GCP modelling |
| CUD modelling | 3-year CUD pricing modelled alongside Azure 3-year RI and AWS Savings Plans |

Full case study: [Examples/media-entertainment/dmg-media-uk-case-study.md](../Examples/media-entertainment/dmg-media-uk-case-study.md)

---

## 9. Related Documents

| Document | Location | Purpose |
|---|---|---|
| CRA Methodology | [docs/METHODOLOGY.md](METHODOLOGY.md) | Full four-phase assessment model |
| Discovery Phase Guide | [docs/guides/01-discovery-phase-guide.md](guides/01-discovery-phase-guide.md) | Phase 1 delivery guide |
| GCP Evaluation Template | `Templates/03-evaluation/gcp-evaluation.xlsx` | On-Demand + 3-year CUD TCO model |
| Business Case Template | `Templates/03-evaluation/business-case-tco-roi.xlsx` | Full TCO comparison with GCP modelling |
| Hyperscaler Decision Matrix | `Templates/03-evaluation/hyperscaler-decision-matrix.xlsx` | Weighted 3-way evaluation |
| Microsoft CAF Alignment | [docs/MICROSOFT-CAF-ALIGNMENT.md](MICROSOFT-CAF-ALIGNMENT.md) | CRA alignment to Microsoft CAF and AMM programme |
| AWS MAP Alignment | [docs/AWS-MAP-ALIGNMENT.md](AWS-MAP-ALIGNMENT.md) | CRA alignment to AWS Migration Acceleration Programme |
| DMG Case Study | [Examples/media-entertainment/dmg-media-uk-case-study.md](../Examples/media-entertainment/dmg-media-uk-case-study.md) | Reference engagement using Google Migration Center as primary discovery tool |

---

*Rackspace Technology — Cloud Solutions Architecture*  
*For Google Cloud partner alignment queries, contact your Rackspace Alliance Partner Manager.*  
*© 2026 Rackspace Technology. All rights reserved.*
