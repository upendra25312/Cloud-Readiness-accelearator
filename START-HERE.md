# Start Here — Cloud Readiness Accelerator

> **Read time: 5 minutes.** This is the only file you need to read before using the framework.

---

## What Is This?

The **Rackspace Cloud Readiness Accelerator (CRA)** is a complete, reusable toolkit for delivering professional cloud readiness assessments. It gives you:

- A proven **four-phase methodology** (Discovery → Analysis → Evaluation → Planning)
- **30+ templates** for every assessment deliverable — application inventory, TCO models, hyperscaler decision matrix, risk register, executive reports
- **Reference examples** showing what real assessment outputs look like
- **Executive presentations** ready for VP/CIO and alliance partner audiences

Use it to scope, deliver, and report a cloud readiness engagement — from first customer meeting to board-ready recommendation.

---

## Jump to Your Role

### I am a Cloud Architect or Cloud Engineer

> I need to deliver a cloud readiness assessment for a customer.

1. Read [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) — understand the four phases and what you deliver in each
2. Open [`docs/guides/01-discovery-phase-guide.md`](docs/guides/01-discovery-phase-guide.md) — start here for Phase 1 activities
3. Go to [`Templates/`](Templates/) — pick the templates for your current phase (see map below)
4. See [`Examples/`](Examples/) — real assessment outputs to calibrate your own work

---

### I am a Delivery Manager or Practice Lead

> I need to scope an engagement, set milestones, and ensure quality.

1. Read [`CLOUD-READINESS-ACCELERATOR-PLAN.md`](CLOUD-READINESS-ACCELERATOR-PLAN.md) — strategy, scope, and what the framework produces
2. Read [`CLOUD-READINESS-ACCELERATOR-PRD.md`](CLOUD-READINESS-ACCELERATOR-PRD.md) — full requirements and quality standards
3. Use [`docs/reference/cra-project-plan-template.xlsx`](docs/reference/cra-project-plan-template.xlsx) — project plan template with milestones and RACI
4. Use [`Templates/04-planning/sow-template.docx`](Templates/04-planning/sow-template.docx) — SOW template to scope the engagement

---

### I am a VP, Director, or Alliance Partner

> I need to understand what this framework is and what it produces.

1. Open [`presentations/executive/cra-overview-v1.1.pptx`](presentations/executive/cra-overview-v1.1.pptx) — executive overview presentation
2. Read [`CLOUD-READINESS-ACCELERATOR-PLAN.md`](CLOUD-READINESS-ACCELERATOR-PLAN.md) — business case, market positioning, and roadmap
3. See [`README.md`](README.md) — full framework overview with alliance partner alignment

---

## The Four-Phase Framework

```text
Phase 1: Discovery          Phase 2: Analysis           Phase 3: Evaluation         Phase 4: Planning
─────────────────────       ─────────────────────       ─────────────────────       ─────────────────────
What you do:                What you do:                What you do:                What you do:
• Application inventory     • Score readiness across    • Build TCO models for      • Define migration waves
• Infrastructure profiling    5 dimensions                AWS, Azure, GCP           • Create risk register
• Dependency mapping        • Identify gaps and risks   • Run hyperscaler           • Design governance model
• SaaS assessment           • Cloud maturity workshop     decision matrix           • Write Part 2 entry point

Key templates:              Key templates:              Key templates:              Key templates:
application-scoping-        cloud-readiness-            aws-evaluation.xlsx         migration-wave-
  profiling.xlsx              scoring-v2.xlsx           azure-evaluation.xlsx         planner.xlsx
infrastructure-             readiness-scoring-          gcp-evaluation.xlsx         risk-assessment.xlsx
  profiling.xlsx              criteria.xlsx             hyperscaler-decision-       governance-model.xlsx
dependency-mapping.xlsx     governance-foundations-       matrix.xlsx
                              alignment.xlsx            business-case-tco-roi.xlsx

Typical duration: 7 wks    Typical duration: 4 wks    Typical duration: 3 wks    Typical duration: 6 wks
```

Total typical engagement: 16–20 weeks (mid-market)

---

## Template Quick Reference

All templates are in [`Templates/`](Templates/). Pick by phase:

| Phase | Template | Purpose |
| --- | --- | --- |
| **Discovery** | `Templates/01-discovery/application-scoping-profiling.xlsx` | Capture app inventory, tech stack, VM/DB counts, cloud readiness |
| **Discovery** | `Templates/01-discovery/infrastructure-profiling.xlsx` | Server specs, OS, hypervisor, DC location, storage |
| **Discovery** | `Templates/01-discovery/dependency-mapping.xlsx` | App-to-app and app-to-infra dependency map |
| **Analysis** | `Templates/02-analysis/cloud-readiness-scoring-v2.xlsx` | 5-dimension readiness scoring (Technical, Operational, Security, Compliance, Business) |
| **Analysis** | `Templates/02-analysis/readiness-scoring-criteria.xlsx` | Scoring definitions and weighting guide |
| **Analysis** | `Templates/02-analysis/governance-foundations-alignment.xlsx` | Cloud governance maturity assessment |
| **Evaluation** | `Templates/03-evaluation/hyperscaler-decision-matrix.xlsx` | Weighted scoring across AWS, Azure, GCP — produces primary recommendation |
| **Evaluation** | `Templates/03-evaluation/aws-evaluation.xlsx` | AWS TCO (Total Cost of Ownership): On-Demand, 3-year Reserved Instances (RI), Savings Plans |
| **Evaluation** | `Templates/03-evaluation/azure-evaluation.xlsx` | Azure TCO: PAYG and 3-year RI, per region; includes Azure Hybrid Benefit (AHB) overlay |
| **Evaluation** | `Templates/03-evaluation/gcp-evaluation.xlsx` | GCP TCO: On-Demand and 3-year Committed Use Discounts (CUD) |
| **Evaluation** | `Templates/03-evaluation/business-case-tco-roi.xlsx` | Full 7-layer TCO comparison, ROI, NPV, on-prem vs cloud |
| **Planning** | `Templates/04-planning/migration-wave-planner.xlsx` | Sequence apps into migration waves by priority |
| **Planning** | `Templates/04-planning/risk-assessment.xlsx` | Technical, licensing, data, and timeline risk register |
| **Planning** | `Templates/04-planning/governance-model.xlsx` | RACI (Responsible, Accountable, Consulted, Informed) matrix, operating model, cloud governance design |
| **Reporting** | `Templates/executive-reporting/cra-assessment-report-template-v3.docx` | Full assessment report (30–50 pages) |
| **Reporting** | `Templates/executive-reporting/cra-executive-summary-v3.pptx` | Executive summary deck for CTO/board |

---

## Reference Examples

Use these to calibrate what your outputs should look like:

| Folder | What It Contains | Use It To |
| --- | --- | --- |
| [`Examples/aws/`](Examples/aws/) | AWS MPA pricing (3 regions — Frankfurt, Ireland, London), business case decks (lift-and-shift, DB refactoring, storage) | See how AWS TCO and business case outputs look |
| [`Examples/azure/`](Examples/azure/) | Azure Migrate assessments — PAYG and 3-year RI across UK South, North Europe, Germany West Central | See how Azure like-for-like and RI assessments look |

---

## Key Reference Documents

| Document | What It Is |
| --- | --- |
| [`README.md`](README.md) | Full framework overview — read after this file |
| [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) | Detailed four-phase methodology with entry/exit criteria |
| [`CLOUD-READINESS-ACCELERATOR-PLAN.md`](CLOUD-READINESS-ACCELERATOR-PLAN.md) | Strategic plan: business case, architecture, GitHub strategy |
| [`CLOUD-READINESS-ACCELERATOR-PRD.md`](CLOUD-READINESS-ACCELERATOR-PRD.md) | Product requirements: functional, non-functional, quality standards |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to contribute templates, examples, or improvements |

---

## Alliance Partner Alignment

| Partner Programme | How CRA Aligns |
| --- | --- |
| **Microsoft CAF (Cloud Adoption Framework)** | CRA phases map to CAF stages: Strategy, Plan, Ready, Migrate, Govern |
| **Microsoft AMM (Azure Migration and Modernisation)** | CRA TCO (Total Cost of Ownership) outputs and hyperscaler recommendation support AMM funding requests |
| **AWS MAP (Migration Acceleration Programme)** | CRA assessment phase maps to MAP Assess; outputs support deal registration in AWS ACE (AWS Customer Engagements) |
| **Google Cloud PSO (Professional Services Organisation) credits** | CRA Discovery and Analysis outputs align with Google Migration Center inputs; supports PSO and RAMP (Rapid Migration Programme) eligibility |

---

## Need Help?

- **Something missing from a template?** Open an issue or see [`CONTRIBUTING.md`](CONTRIBUTING.md)
- **Questions about the methodology?** Read [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) first
- **Using this for a real engagement?** Read the phase guide for your current phase before starting

---

*Rackspace Cloud Solutions Architecture — Cloud Readiness Accelerator*  
*© Rackspace Technology. All rights reserved.*
