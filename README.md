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
│   └── METHODOLOGY.md                             ← Full four-phase methodology
├── Templates/                                      ← All 16+ assessment templates
├── Examples/
│   ├── AWS Example/                               ← AWS TCO and business case outputs
│   └── Azure Example -1/                          ← Azure Migrate assessment outputs
├── Discovery-Phase-Guide.md                        ← Phase 1 delivery guide
├── Analysis-Phase-Guide.md                         ← Phase 2 delivery guide
├── Evaluation-Phase-Guide.md                       ← Phase 3 delivery guide
├── Planning-Phase-Guide.md                         ← Phase 4 delivery guide
├── Customization-Guides/                           ← Industry and size adaptations
├── Integration-Guides/                             ← CMDB, monitoring, cloud tool integrations
├── Quality-Assurance/                              ← Data validation and QA checklist
├── Cloud_Readiness_Assessment_Project_Plan.xlsx    ← Project plan with milestones and RACI
├── Cloud_Readiness_Assessment_SoW.docx             ← SOW template
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
| Discovery | [Discovery-Phase-Guide.md](Discovery-Phase-Guide.md) |
| Analysis | [Analysis-Phase-Guide.md](Analysis-Phase-Guide.md) |
| Evaluation | [Evaluation-Phase-Guide.md](Evaluation-Phase-Guide.md) |
| Planning | [Planning-Phase-Guide.md](Planning-Phase-Guide.md) |

### Step 4 — Use the templates

All templates are in [Templates/](Templates/). Pick by phase:

| Phase | Template | What It Produces |
| --- | --- | --- |
| Discovery | `Application Scoping & Profiling - template.xlsx` | Application inventory with tech stack, VM/DB counts, readiness flag |
| Discovery | `Infrastructure-Profiling-Template.xlsx` | Server specs, OS, hypervisor, DC location, storage |
| Discovery | `Dependency-Mapping-Template.xlsx` | App-to-app and app-to-infrastructure dependency map |
| Analysis | `Cloud-Readiness-Assessment-v2.xlsx` | 5-dimension readiness scores — Technical, Operational, Security, Financial, Business |
| Analysis | `Readiness-Scoring-Criteria-Template.xlsx` | Scoring definitions and weighting guide |
| Analysis | `CRA - LITE Governance Foundations Alignment Tool - Template.xlsx` | Cloud governance maturity assessment |
| Evaluation | `Hyperscaler-Decision-Matrix-Template.xlsx` | Weighted score across AWS, Azure, GCP — produces primary recommendation |
| Evaluation | `AWS-Evaluation-Template.xlsx` | AWS TCO: On-Demand, 3-year Reserved Instances, Savings Plans |
| Evaluation | `Azure-Evaluation-Template.xlsx` | Azure TCO: PAYG and 3-year RI, per region |
| Evaluation | `GCP-Evaluation-Template.xlsx` | GCP TCO: On-Demand and 3-year CUDs |
| Evaluation | `Business-Case-Template.xlsx` | Full TCO comparison, ROI, NPV, on-premises vs cloud |
| Planning | `Migration-Wave-Planning-Template.xlsx` | Application sequencing into migration waves by priority |
| Planning | `Risk-Assessment-Template.xlsx` | Technical, licensing, data, and timeline risk register |
| Planning | `Governance-Model-Template.xlsx` | RACI, operating model, cloud governance design |
| Reporting | `Cloud_Readiness_Assessment_Report_Template_v3_Audited.docx` | Full assessment report (30–50 pages) |
| Reporting | `Cloud_Readiness_Assessment_Executive_Summary_Template_v3_Audited.pptx` | Executive summary deck for CTO/board |

### Step 5 — Calibrate against reference examples

| Folder | Contents | Use It To |
| --- | --- | --- |
| [Examples/AWS Example/](Examples/AWS%20Example/) | AWS MPA pricing (3 regions), business case decks — lift-and-shift, DB refactoring, storage | Calibrate AWS TCO outputs |
| [Examples/Azure Example -1/](Examples/Azure%20Example%20-1/) | Azure Migrate assessments — PAYG and 3-year RI across UK, Ireland, Germany | Calibrate Azure like-for-like assessments |

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

Engagement scope and SOW language are in [Cloud_Readiness_Assessment_SoW.docx](Cloud_Readiness_Assessment_SoW.docx).

---

## Contributing

Contributions are welcome — new templates, anonymized examples, improved phase guides, or methodology refinements. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

MIT License — see [LICENSE](LICENSE).

---

*Rackspace Cloud Solutions Architecture — Cloud Readiness Accelerator*
*© Rackspace Technology. All rights reserved.*
