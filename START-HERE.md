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
3. Use [`Cloud_Readiness_Assessment_Project_Plan.xlsx`](Cloud_Readiness_Assessment_Project_Plan.xlsx) — project plan template with milestones and RACI
4. Use [`Cloud_Readiness_Assessment_SoW.docx`](Cloud_Readiness_Assessment_SoW.docx) — SOW template to scope the engagement

---

### I am a VP, Director, or Alliance Partner

> I need to understand what this framework is and what it produces.

1. Open [`Cloud_Readiness_Accelerator_Rackspace_V1.1.pptx`](Cloud_Readiness_Accelerator_Rackspace_V1.1.pptx) — executive overview presentation
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
Application Scoping &       Cloud-Readiness-            AWS/Azure/GCP-Evaluation    Migration-Wave-Planning
  Profiling.xlsx              Assessment-v2.xlsx          -Template.xlsx              -Template.xlsx
Infrastructure-Profiling    Readiness-Scoring-          Hyperscaler-Decision-       Risk-Assessment-
  -Template.xlsx              Criteria-Template.xlsx      Matrix-Template.xlsx        Template.xlsx
Dependency-Mapping          Governance-Foundations-     Business-Case-Template      Governance-Model-
  -Template.xlsx               Alignment-Tool.xlsx         .xlsx                       Template.xlsx

Typical duration: 4-8 wks  Typical duration: 3-6 wks  Typical duration: 3-5 wks  Typical duration: 2-4 wks
```

Total typical engagement: 12–23 weeks

---

## Template Quick Reference

All templates are in [`Templates/`](Templates/). Pick by phase:

| Phase | Template | Purpose |
| --- | --- | --- |
| **Discovery** | `Application Scoping & Profiling - template.xlsx` | Capture app inventory, tech stack, VM/DB counts, cloud readiness |
| **Discovery** | `Infrastructure-Profiling-Template.xlsx` | Server specs, OS, hypervisor, DC location, storage |
| **Discovery** | `Dependency-Mapping-Template.xlsx` | App-to-app and app-to-infra dependency map |
| **Analysis** | `Cloud-Readiness-Assessment-v2.xlsx` | 5-dimension readiness scoring (Technical, Operational, Security, Financial, Business) |
| **Analysis** | `Readiness-Scoring-Criteria-Template.xlsx` | Scoring definitions and weighting guide |
| **Analysis** | `CRA - LITE Governance Foundations Alignment Tool - Template.xlsx` | Cloud governance maturity assessment |
| **Evaluation** | `Hyperscaler-Decision-Matrix-Template.xlsx` | Weighted scoring across AWS, Azure, GCP — produces primary recommendation |
| **Evaluation** | `AWS-Evaluation-Template.xlsx` | AWS TCO: On-Demand, 3-year RI, Savings Plans |
| **Evaluation** | `Azure-Evaluation-Template.xlsx` | Azure TCO: PAYG and 3-year RI, per region |
| **Evaluation** | `GCP-Evaluation-Template.xlsx` | GCP TCO: On-Demand and 3-year CUD |
| **Evaluation** | `Business-Case-Template.xlsx` | Full TCO comparison, ROI, NPV, on-prem vs cloud |
| **Planning** | `Migration-Wave-Planning-Template.xlsx` | Sequence apps into migration waves by priority |
| **Planning** | `Risk-Assessment-Template.xlsx` | Technical, licensing, data, and timeline risk register |
| **Planning** | `Governance-Model-Template.xlsx` | RACI, operating model, cloud governance design |
| **Reporting** | `Cloud_Readiness_Assessment_Report_Template_v3_Audited.docx` | Full assessment report (30-50 pages) |
| **Reporting** | `Cloud_Readiness_Assessment_Executive_Summary_Template_v3_Audited.pptx` | Executive summary deck for CTO/board |

---

## Reference Examples

Use these to calibrate what your outputs should look like:

| Folder | What It Contains | Use It To |
| --- | --- | --- |
| [`Examples/AWS Example/`](Examples/AWS%20Example/) | AWS MPA pricing files (3 regions), business case decks (lift-and-shift, DB refactoring, storage) | See how AWS TCO and business case outputs look |
| [`Examples/Azure Example -1/`](Examples/Azure%20Example%20-1/) | Azure Migrate assessments — PAYG and 3-year RI, across 3 regions (UK, Ireland, Germany) | See how Azure like-for-like and RI assessments look |

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

| Partner Program | How CRA Aligns |
| --- | --- |
| **Microsoft CAF** | CRA phases map to CAF stages: Strategy, Plan, Ready, Migrate, Govern |
| **Microsoft AMM** | CRA TCO outputs and hyperscaler recommendation support AMM funding requests |
| **AWS MAP** | CRA assessment phase maps to MAP Assess; outputs support deal registration |
| **Google PSO** | CRA Discovery and Analysis outputs align with Google Migration Center inputs |

---

## Need Help?

- **Something missing from a template?** Open an issue or see [`CONTRIBUTING.md`](CONTRIBUTING.md)
- **Questions about the methodology?** Read [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) first
- **Using this for a real engagement?** Read the phase guide for your current phase before starting

---

*Rackspace Cloud Solutions Architecture — Cloud Readiness Accelerator*  
*© Rackspace Technology. All rights reserved.*
