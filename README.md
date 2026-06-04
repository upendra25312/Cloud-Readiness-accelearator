# Cloud Readiness Accelerator

> **Enterprise-grade, vendor-neutral cloud assessment framework** — four-phase methodology, 35+ battle-tested templates, multi-cloud TCO models, and a structured hyperscaler decision framework. Built by Rackspace Technology cloud architects and validated on real enterprise engagements.

[![Framework Version](https://img.shields.io/badge/Framework-v2.0-0078D4?style=flat-square)](./Templates)
[![Hyperscalers](https://img.shields.io/badge/Clouds-AWS%20%7C%20Azure%20%7C%20GCP-orange?style=flat-square)](#supported-hyperscalers)
[![Templates](https://img.shields.io/badge/Templates-35%2B-green?style=flat-square)](./Templates)
[![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)](./LICENSE)

---

## Table of Contents

- [Overview](#overview)
- [Why This Accelerator](#why-this-accelerator)
- [Four-Phase Methodology](#four-phase-methodology)
- [Template Catalog](#template-catalog)
- [Examples & Case Studies](#examples--case-studies)
- [Quick Start](#quick-start)
- [Supported Hyperscalers](#supported-hyperscalers)
- [Repo Structure](#repo-structure)
- [Contributing](#contributing)

---

## Overview

The **Cloud Readiness Accelerator (CRA)** is a structured, repeatable framework for enterprise cloud readiness assessments. It provides consulting teams, enterprise architects, and pre-sales engineers with a complete toolkit to:

- **Discover and profile** an organisation's full infrastructure estate — on-premises, virtualised, and SaaS
- **Score cloud readiness** across technical, governance, and commercial dimensions
- **Evaluate and compare** AWS, Azure, and GCP using consistent, weighted criteria
- **Build board-ready business cases** with validated TCO models, ROI projections, and risk registers
- **Deliver executive-quality outputs** — assessment reports, executive summaries, and migration roadmaps

This accelerator compresses what typically takes months into a structured 6–12 week engagement, giving clients a defensible, data-driven recommendation they can act on.

---

## Why This Accelerator

Most cloud assessments fail for one of three reasons: they lack rigour, they are vendor-biased, or they cannot translate technical findings into commercial language the board can approve. The CRA solves all three.

| Problem | CRA Solution |
|---|---|
| Inconsistent discovery scope | Standardised infrastructure and application profiling templates covering VMs, networking, storage, SaaS, and dependencies |
| Vendor-biased evaluation | Three-way hyperscaler scoring matrix with configurable, weighted criteria — no vendor wins by default |
| TCO models that do not survive scrutiny | Multi-region pricing workbooks with PAYG, Reserved Instance, and Hybrid Benefit scenarios, validated against real Azure and AWS pricing |
| No governance baseline | Governance Foundations Alignment template maps current state to Well-Architected Frameworks across all three clouds |
| Weak executive narrative | Boardroom-ready PowerPoint and Word templates pre-built for the Rackspace brand and white-label use |
| Scope creep and commercial risk | SOW templates and PS Margin Calculator protect engagement profitability from day one |

### Validated at Scale

The CRA framework was applied to the **DMG Media UK** cloud readiness engagement — one of the UK's largest digital media groups (Daily Mail Group Trust). Key outcomes:

- **4,212 VMware VMs** discovered across 10 vCenter instances — 57% above initial SoW scope
- Full three-way hyperscaler evaluation (AWS, Azure, GCP) completed in one engagement cycle
- Azure UK South selected as primary recommendation with board-level sign-off
- Complete business case including 3-year TCO, RI vs PAYG vs AHB modelling across three UK/EU regions

---

## Four-Phase Methodology

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     CLOUD READINESS ACCELERATOR — v2.0                       │
├──────────────┬──────────────┬──────────────┬──────────────┬──────────────────┤
│  PHASE 1     │  PHASE 2     │  PHASE 3     │  PHASE 4     │  OUTPUTS         │
│  Discovery   │  Analysis    │  Evaluation  │  Planning    │  (all phases)    │
├──────────────┼──────────────┼──────────────┼──────────────┼──────────────────┤
│ • Infra      │ • Readiness  │ • Hyperscaler│ • Migration  │ • CRA Report     │
│   profiling  │   scoring    │   decision   │   wave plan  │ • Exec summary   │
│ • App scoping│ • Governance │   matrix     │ • Governance │ • TCO model      │
│ • Dependency │   alignment  │ • TCO / ROI  │   model      │ • Cloud strategy │
│   mapping    │ • Risk       │   modelling  │ • Risk reg.  │   presentation   │
│ • SaaS audit │   baseline   │ • Pricing    │ • SOW / next │                  │
│              │              │   scenarios  │   phase      │                  │
└──────────────┴──────────────┴──────────────┴──────────────┴──────────────────┘
```

### Phase 1 — Discovery

Establish the ground truth of the client's infrastructure, application, and SaaS estate. This phase eliminates scope surprises and ensures downstream TCO models are grounded in real data.

**Deliverables:** Infrastructure inventory, application portfolio, dependency map, SaaS assessment

### Phase 2 — Analysis

Score the estate against cloud readiness dimensions. Identify blockers, risks, and governance gaps. Establish a baseline that the recommendations in Phase 3 are anchored to.

**Deliverables:** Readiness scoring workbook, governance alignment report, risk baseline

### Phase 3 — Evaluation

Evaluate AWS, Azure, and GCP against weighted client criteria. Model TCO across pricing tiers and regions. Produce a vendor-neutral recommendation with supporting commercial evidence.

**Deliverables:** Hyperscaler decision matrix, TCO model (three clouds, three pricing tiers), business case

### Phase 4 — Planning

Translate the recommendation into an actionable roadmap. Design the governance model, wave plan, and risk register. Package the engagement for the next phase or for client hand-off.

**Deliverables:** Migration wave planner, governance model, risk register, Phase 2 SOW

---

## Template Catalog

### Phase 1 — Discovery Templates

| Template | Format | Purpose |
|---|---|---|
| [Infrastructure Profiling](./Templates/01-discovery/infrastructure-profiling.xlsx) | Excel | Full VM estate capture — compute, memory, storage, OS, virtualisation platform |
| [Application Scoping & Profiling](./Templates/01-discovery/application-scoping-profiling.xlsx) | Excel | Application inventory, criticality, dependencies, migration complexity classification |
| [Dependency Mapping](./Templates/01-discovery/dependency-mapping.xlsx) | Excel | Network and application dependency matrix — identifies tightly coupled workloads |
| [SaaS Application Assessment](./Templates/01-discovery/saas-application-assessment.xlsx) | Excel | SaaS estate audit — vendor, contract, cloud-native alternative, consolidation opportunity |

### Phase 2 — Analysis Templates

| Template | Format | Purpose |
|---|---|---|
| [Cloud Readiness Scoring v2](./Templates/02-analysis/cloud-readiness-scoring-v2.xlsx) | Excel | Weighted scoring across technical, operational, security, and commercial readiness dimensions |
| [Readiness Scoring Criteria](./Templates/02-analysis/readiness-scoring-criteria.xlsx) | Excel | Scoring rubrics and definitions — ensures consistent assessment across engagements |
| [Governance Foundations Alignment](./Templates/02-analysis/governance-foundations-alignment.xlsx) | Excel | Maps client governance posture to AWS WAF, Azure CAF, and GCP Cloud Architecture Framework |

### Phase 3 — Evaluation Templates

| Template | Format | Purpose |
|---|---|---|
| [Hyperscaler Decision Matrix](./Templates/03-evaluation/hyperscaler-decision-matrix.xlsx) | Excel | Configurable weighted scoring matrix — evaluates AWS, Azure, GCP across client-defined criteria |
| [Hyperscaler Weighted Selection Criteria](./Templates/03-evaluation/hyperscaler-weighted-selection-criteria.xlsx) | Excel | Pre-built criteria library with recommended weightings for common client profiles |
| [Business Case & TCO / ROI Model](./Templates/03-evaluation/business-case-tco-roi.xlsx) | Excel | Three-year TCO comparison with CAPEX/OPEX analysis, break-even, and ROI projection |
| [AWS Evaluation Workbook](./Templates/03-evaluation/aws-evaluation.xlsx) | Excel | AWS-specific sizing, pricing, and feature evaluation |
| [Azure Evaluation Workbook](./Templates/03-evaluation/azure-evaluation.xlsx) | Excel | Azure-specific sizing with PAYG, 3-yr RI, AHB, and multi-region scenarios |
| [GCP Evaluation Workbook](./Templates/03-evaluation/gcp-evaluation.xlsx) | Excel | GCP-specific sizing and pricing model |
| [Azure Calculator Walkthrough](./Templates/03-evaluation/azure-calculator-walkthrough.pptx) | PowerPoint | Step-by-step guide for Azure Pricing Calculator — use in client workshops |

### Phase 4 — Planning Templates

| Template | Format | Purpose |
|---|---|---|
| [Migration Wave Planner](./Templates/04-planning/migration-wave-planner.xlsx) | Excel | Workload grouping by wave, sequencing, dependencies, and timeline |
| [Governance Model](./Templates/04-planning/governance-model.xlsx) | Excel | Cloud governance framework — policies, RACI, cost management, security baseline |
| [Governance Workshop Schedule](./Templates/04-planning/governance-workshop-schedule.docx) | Word | Workshop agenda and facilitation guide for governance design sessions |
| [Risk Assessment](./Templates/04-planning/risk-assessment.xlsx) | Excel | Risk register with likelihood/impact scoring, mitigations, and ownership |
| [Executive Summary Data](./Templates/04-planning/executive-summary-data.xlsx) | Excel | Aggregated data model that feeds the executive summary PowerPoint |
| [SOW Template](./Templates/04-planning/sow-template.docx) | Word | Statement of Work template for Phase 2 / migration engagement |

### Executive Reporting Templates

| Template | Format | Purpose |
|---|---|---|
| [CRA Assessment Report v3](./Templates/executive-reporting/cra-assessment-report-template-v3.docx) | Word | Full Phase 1 assessment report — 40+ page structured report template |
| [CRA Phase 1 Report Template](./Templates/executive-reporting/cra-phase1-report-template.docx) | Word | Condensed Phase 1 report template for shorter-format engagements |
| [CRA Executive Summary v3](./Templates/executive-reporting/cra-executive-summary-v3.pptx) | PowerPoint | Board-ready executive summary deck — 12–15 slides, Rackspace branded |
| [CRA Executive Summary Template](./Templates/executive-reporting/cra-executive-summary-template.pptx) | PowerPoint | White-label executive summary template |
| [Cloud Strategy (Generic)](./Templates/executive-reporting/cloud-strategy-generic.pptx) | PowerPoint | Generic cloud strategy narrative deck — adaptable to any client |
| [Microsoft Solution Assessment](./Templates/executive-reporting/ms-solution-assessment.pptx) | PowerPoint | Microsoft-aligned solution assessment output — maps to MS Solution Assessment programme |

---

## Examples & Case Studies

### DMG Media UK — Azure Cloud Readiness Assessment

**The flagship reference engagement.** DMG Media UK (part of DMGT — Daily Mail Group Trust) engaged Rackspace Technology to assess their VMware estate across two UK data centres and deliver a board-level cloud recommendation.

| Metric | Value |
|---|---|
| VMs Discovered | 4,212 across 10 vCenter instances |
| Active Non-VDI VMs | 3,617 |
| Scope Variance (vs SoW) | +57% — 1,317 VMs above original scope |
| OS Diversity | 40+ distinct operating systems |
| End-of-Life OS Risk | 224 active VMs on unsupported OS |
| Storage Estate | 764 TB allocated, 46% utilised |
| Discovery Tool | GCP Migration Center |
| **Outcome** | **Azure UK South — primary hyperscaler recommendation** |

**Available in:** [`Examples/media-news/`](./Examples/media-news/)

- [DMG Media UK Case Study](./Examples/media-news/dmg-media-uk-case-study.md)
- DMG CRA Executive Summary (PowerPoint)
- DMG CRA Phase 1 Report (Word)
- DMG Cost Model — PAYG/RI/AHB (Excel)

### AWS Pricing Examples

Real-world AWS MPA pricing models across multiple regions and workload profiles.

**Available in:** [`Examples/aws/`](./Examples/aws/)

- AWS Business Case — Lift & Shift
- AWS Business Case — DB Refactoring
- MPA Pricing Models — 3 regions, with/without DB workloads

### Azure Pricing Examples

Multi-region Azure cost assessments with PAYG, 3-year Reserved Instance, and Azure Hybrid Benefit modelling.

**Available in:** [`Examples/azure/`](./Examples/azure/)

- Azure Cost Models — UK South, North Europe, Germany West Central
- Three pricing tiers: PAYG, RI, AHB
- Cost Models Summary workbook

### Microsoft Alliance Example

**Available in:** [`Examples/Azure Example/`](./Examples/Azure%20Example/)

- Hyperscaler Decision Matrix (completed — Microsoft)
- Microsoft Unified support proposal (PowerPoint)
- DMG RFP response artefacts

---

## Quick Start

### For a New Engagement

**Week 1–2: Discovery Setup**
1. Share [`infrastructure-profiling.xlsx`](./Templates/01-discovery/infrastructure-profiling.xlsx) with the client infrastructure team
2. Initiate application scoping with [`application-scoping-profiling.xlsx`](./Templates/01-discovery/application-scoping-profiling.xlsx)
3. Run a dependency workshop using [`dependency-mapping.xlsx`](./Templates/01-discovery/dependency-mapping.xlsx)
4. Complete SaaS audit with [`saas-application-assessment.xlsx`](./Templates/01-discovery/saas-application-assessment.xlsx)

**Week 3–4: Analysis**
5. Score the estate in [`cloud-readiness-scoring-v2.xlsx`](./Templates/02-analysis/cloud-readiness-scoring-v2.xlsx)
6. Facilitate governance alignment workshop using [`governance-foundations-alignment.xlsx`](./Templates/02-analysis/governance-foundations-alignment.xlsx)

**Week 5–6: Evaluation**
7. Complete hyperscaler scoring in [`hyperscaler-decision-matrix.xlsx`](./Templates/03-evaluation/hyperscaler-decision-matrix.xlsx)
8. Build the TCO model in [`business-case-tco-roi.xlsx`](./Templates/03-evaluation/business-case-tco-roi.xlsx)
9. Run the Azure/AWS/GCP evaluation workbooks for your recommended cloud

**Week 7–8: Planning & Reporting**
10. Build the executive summary in [`cra-executive-summary-v3.pptx`](./Templates/executive-reporting/cra-executive-summary-v3.pptx)
11. Produce the full assessment report using [`cra-assessment-report-template-v3.docx`](./Templates/executive-reporting/cra-assessment-report-template-v3.docx)
12. Draft the Phase 2 SOW using [`sow-template.docx`](./Templates/04-planning/sow-template.docx)

### For Pre-Sales

Start with the [Hyperscaler Decision Matrix](./Templates/03-evaluation/hyperscaler-decision-matrix.xlsx) and the [Business Case & TCO Model](./Templates/03-evaluation/business-case-tco-roi.xlsx). Review the [DMG Media UK case study](./Examples/media-news/dmg-media-uk-case-study.md) for a reference narrative.

### For Alliance Partners (Microsoft / AWS / Google Cloud)

The [Microsoft Solution Assessment template](./Templates/executive-reporting/ms-solution-assessment.pptx) maps CRA outputs to the Microsoft Solution Assessment programme. The [Hyperscaler Decision Matrix](./Templates/03-evaluation/hyperscaler-decision-matrix.xlsx) is designed to be shared with hyperscaler alliance teams during co-sell motions.

---

## Supported Hyperscalers

| Cloud | Evaluation Template | Pricing Examples | Alliance Artefacts |
|---|---|---|---|
| **Microsoft Azure** | [`azure-evaluation.xlsx`](./Templates/03-evaluation/azure-evaluation.xlsx) | [`Examples/azure/`](./Examples/azure/) | [`ms-solution-assessment.pptx`](./Templates/executive-reporting/ms-solution-assessment.pptx) |
| **Amazon Web Services** | [`aws-evaluation.xlsx`](./Templates/03-evaluation/aws-evaluation.xlsx) | [`Examples/aws/`](./Examples/aws/) | MPA pricing models |
| **Google Cloud** | [`gcp-evaluation.xlsx`](./Templates/03-evaluation/gcp-evaluation.xlsx) | — | GCP Migration Center (discovery) |

The [Hyperscaler Decision Matrix](./Templates/03-evaluation/hyperscaler-decision-matrix.xlsx) evaluates all three clouds against configurable, weighted criteria. It is designed to be auditable — every score is documented, every weight is client-set.

---

## Repo Structure

```
Cloud-Readiness-Accelerator/
│
├── Templates/                          # All assessment and reporting templates
│   ├── 01-discovery/                   # Phase 1: Infrastructure & application discovery
│   ├── 02-analysis/                    # Phase 2: Readiness scoring & governance
│   ├── 03-evaluation/                  # Phase 3: Hyperscaler evaluation & TCO
│   ├── 04-planning/                    # Phase 4: Migration planning & SOW
│   └── executive-reporting/            # Board-ready reports and presentations
│
├── Examples/                           # Completed examples from real engagements
│   ├── aws/                            # AWS MPA pricing models (multi-region)
│   ├── azure/                          # Azure cost models (PAYG, RI, AHB, multi-region)
│   ├── Azure Example/                  # Microsoft alliance co-sell artefacts
│   ├── media-news/                     # DMG Media UK — reference engagement outputs
│   └── case study example/             # CRA Phase 1 report example (anonymised)
│
├── SOW/                                # Statement of Work and commercial artefacts
│   ├── Cloud Readiness Assessment      # Phase 1 rebaselined objectives & plan
│   └── PS Margin Calculator            # Engagement commercial modelling
│
└── .github/                            # GitHub configuration
    ├── ISSUE_TEMPLATE/                 # Bug, feature, and question templates
    ├── workflows/                      # CI/CD: validation and release pipelines
    └── PULL_REQUEST_TEMPLATE.md        # PR contribution template
```

---

## Contributing

This accelerator is maintained by the Rackspace Technology Cloud Solutions Architecture practice. Contributions are welcome from Rackspace architects, alliance partners, and the wider community.

**To contribute:**

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-improvement`
3. Make your changes following the template standards in each phase folder
4. Submit a pull request using the [PR template](./.github/PULL_REQUEST_TEMPLATE.md)

**For bugs or feature requests**, open an issue using the appropriate [issue template](./.github/ISSUE_TEMPLATE/).

**Commercial use**: The PS Margin Calculator and SOW templates contain Rackspace commercial frameworks. Contact your Rackspace alliance or commercial team before adapting these for external use.

---

## About Rackspace Technology

This accelerator was built and is maintained by the **Cloud Solutions Architecture** practice at [Rackspace Technology](https://www.rackspace.com). Rackspace is a leading end-to-end multicloud technology services company, serving thousands of customers globally across AWS, Azure, and Google Cloud.

For enquiries about the Cloud Readiness Accelerator or to engage Rackspace for a cloud assessment, contact your Rackspace account team or visit [rackspace.com](https://www.rackspace.com).

---

*Cloud Readiness Accelerator — Rackspace Technology Cloud Solutions Architecture*
*Framework version 2.0 | Last updated June 2026*
