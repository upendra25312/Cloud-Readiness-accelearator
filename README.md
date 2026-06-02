# Cloud Readiness Accelerator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A complete, reusable toolkit for delivering professional cloud readiness assessments. Built by Rackspace Cloud Solutions Architecture for use across any enterprise cloud engagement.

---

## What It Is

The **Cloud Readiness Accelerator (CRA)** gives a delivery team everything needed to scope, execute, and report a cloud readiness engagement — from first customer meeting to a board-ready recommendation. It packages a proven four-phase methodology with the templates, scoring tools, and reporting formats that make each phase repeatable and auditable.

The framework is cloud-agnostic and hyperscaler-agnostic. It supports AWS, Azure, and GCP evaluations and aligns to Microsoft CAF/AMM, AWS MAP, and Google PSO programme requirements.

---

## The Four Phases

```text
Discovery          →  Analysis           →  Evaluation          →  Planning
─────────────────     ─────────────────     ─────────────────     ─────────────────
Application          Readiness scoring      TCO modelling         Migration waves
inventory            across 5 dimensions    (AWS, Azure, GCP)     Risk register
Infrastructure       Gap identification     Hyperscaler           Governance model
profiling            Cloud maturity         decision matrix       Part 2 entry point
Dependency           workshop outputs       Business case         
mapping                                     ROI / NPV             

4–8 weeks            3–6 weeks              3–5 weeks             2–4 weeks
```

Total typical engagement: 12–23 weeks

---

## What Is in This Repository

```text
├── START-HERE.md                                   ← Start here — 5-minute orientation
├── docs/
│   ├── METHODOLOGY.md                             ← Full four-phase methodology
│   ├── guides/
│   │   ├── 01-discovery-phase-guide.md            ← Phase 1 delivery guide
│   │   ├── 02-analysis-phase-guide.md             ← Phase 2 delivery guide
│   │   ├── 03-evaluation-phase-guide.md           ← Phase 3 delivery guide
│   │   └── 04-planning-phase-guide.md             ← Phase 4 delivery guide
│   ├── integration/                               ← CMDB, monitoring, cloud tool integrations
│   ├── customization/                             ← Industry and size adaptations
│   ├── governance/                                ← Data validation and QA checklist
│   └── reference/                                 ← Azure CAF and other reference PDFs
├── presentations/
│   ├── executive/                                 ← CRA overview decks (v0, v1, v1.1)
│   └── alliance/                                  ← Azure AMM delivery guide, Rackspace × Microsoft funding enablement
├── Templates/
│   ├── 01-discovery/                              ← Application inventory, infra profiling, dependency mapping
│   ├── 02-analysis/                               ← Readiness scoring, governance foundations
│   ├── 03-evaluation/                             ← TCO models (AWS/Azure/GCP), hyperscaler decision matrix, business case
│   ├── 04-planning/                               ← Migration waves, risk register, governance model, SOW
│   └── executive-reporting/                       ← Assessment report and executive summary templates
├── Examples/
│   ├── aws/                                       ← AWS MPA pricing (3 regions) and business case examples
│   └── azure/                                     ← Azure Migrate assessments — PAYG and 3-year RI across 3 regions
├── docs/reference/cra-project-plan-template.xlsx   ← Project plan with milestones and RACI
├── Templates/04-planning/sow-template.docx         ← SOW template
├── CLOUD-READINESS-ACCELERATOR-PLAN.md             ← Framework strategy and roadmap
├── CLOUD-READINESS-ACCELERATOR-PRD.md              ← Full requirements and quality standards
├── CHANGELOG.md                                    ← Version history
└── CONTRIBUTING.md                                 ← How to contribute
```

---

## How to Use It

### Step 1 — Orient yourself

Read [START-HERE.md](START-HERE.md). It maps the entire framework in 5 minutes and shows where every file fits.

### Step 2 — Understand the methodology

Read [docs/METHODOLOGY.md](docs/METHODOLOGY.md). It defines entry criteria, activities, exit criteria, and deliverables for each of the four phases.

### Step 3 — Open the phase guide for your current phase

| Phase | Guide |
| --- | --- |
| Discovery | [docs/guides/01-discovery-phase-guide.md](docs/guides/01-discovery-phase-guide.md) |
| Analysis | [docs/guides/02-analysis-phase-guide.md](docs/guides/02-analysis-phase-guide.md) |
| Evaluation | [docs/guides/03-evaluation-phase-guide.md](docs/guides/03-evaluation-phase-guide.md) |
| Planning | [docs/guides/04-planning-phase-guide.md](docs/guides/04-planning-phase-guide.md) |

### Step 4 — Use the templates

All templates are in [Templates/](Templates/), organised by phase:

| Phase | Template | What It Produces |
| --- | --- | --- |
| Discovery | `01-discovery/application-scoping-profiling.xlsx` | Application inventory with tech stack, VM/DB counts, readiness flag |
| Discovery | `01-discovery/infrastructure-profiling.xlsx` | Server specs, OS, hypervisor, DC location, storage |
| Discovery | `01-discovery/dependency-mapping.xlsx` | App-to-app and app-to-infrastructure dependency map |
| Analysis | `02-analysis/cloud-readiness-scoring-v2.xlsx` | 5-dimension readiness scores — Technical, Operational, Security, Financial, Business |
| Analysis | `02-analysis/readiness-scoring-criteria.xlsx` | Scoring definitions and weighting guide |
| Analysis | `02-analysis/governance-foundations-alignment.xlsx` | Cloud governance maturity assessment |
| Evaluation | `03-evaluation/hyperscaler-decision-matrix.xlsx` | Weighted score across AWS, Azure, GCP — produces primary recommendation |
| Evaluation | `03-evaluation/aws-evaluation.xlsx` | AWS TCO: On-Demand, 3-year Reserved Instances, Savings Plans |
| Evaluation | `03-evaluation/azure-evaluation.xlsx` | Azure TCO: PAYG and 3-year RI, per region |
| Evaluation | `03-evaluation/gcp-evaluation.xlsx` | GCP TCO: On-Demand and 3-year CUDs |
| Evaluation | `03-evaluation/business-case-tco-roi.xlsx` | Full TCO comparison, ROI, NPV, on-premises vs cloud |
| Planning | `04-planning/migration-wave-planner.xlsx` | Application sequencing into migration waves by priority |
| Planning | `04-planning/risk-assessment.xlsx` | Technical, licensing, data, and timeline risk register |
| Planning | `04-planning/governance-model.xlsx` | RACI, operating model, cloud governance design |
| Planning | `04-planning/sow-template.docx` | SOW template — scope, deliverables, pricing model |
| Reporting | `executive-reporting/cra-assessment-report-template-v3.docx` | Full assessment report (30–50 pages) |
| Reporting | `executive-reporting/cra-executive-summary-v3.pptx` | Executive summary deck for CTO/board |

### Step 5 — Calibrate against reference examples

| Folder | Contents | Use It To |
| --- | --- | --- |
| [Examples/aws/](Examples/aws/) | AWS MPA pricing (3 regions — Frankfurt, Ireland, London), business case decks — lift-and-shift, DB refactoring, storage | Calibrate AWS TCO outputs |
| [Examples/azure/](Examples/azure/) | Azure Migrate assessments — PAYG and 3-year RI across UK South, North Europe, Germany West Central | Calibrate Azure like-for-like assessments |

---

## Alliance Partner Alignment

| Partner Programme | Alignment |
| --- | --- |
| Microsoft Cloud Adoption Framework (CAF) | CRA phases map to CAF stages: Strategy → Plan → Ready → Migrate → Govern |
| Microsoft Azure Migration and Modernisation (AMM) | CRA TCO outputs and hyperscaler recommendation directly support AMM funding submissions |
| AWS Migration Acceleration Programme (MAP) | CRA Assessment phase maps to MAP Assess; outputs satisfy MAP deal registration requirements |
| Google Cloud PSO / Migration Center | CRA Discovery and Analysis outputs align with Google Migration Center input requirements |

---

## Scope and Quality Standards

Full requirements are in [CLOUD-READINESS-ACCELERATOR-PRD.md](CLOUD-READINESS-ACCELERATOR-PRD.md).

Delivery scope, business case, and roadmap are in [CLOUD-READINESS-ACCELERATOR-PLAN.md](CLOUD-READINESS-ACCELERATOR-PLAN.md).

Engagement scope and SOW language are in [Templates/04-planning/sow-template.docx](Templates/04-planning/sow-template.docx).

---

## Contributing

Contributions are welcome — new templates, anonymized examples, improved phase guides, or methodology refinements. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

MIT License — see [LICENSE](LICENSE).

---

*Rackspace Cloud Solutions Architecture — Cloud Readiness Accelerator*
*© Rackspace Technology. All rights reserved.*
