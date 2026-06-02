# CRA Architect Onboarding Guide

**Version:** 1.0  
**Time to complete:** 30 minutes  
**Target reader:** Any Rackspace Cloud Architect or Solutions Engineer picking up the CRA framework for the first time  
**No prior briefing needed** — this guide is fully self-contained

---

## What You Will Know After 30 Minutes

After completing this guide you will be able to:

1. Explain the CRA framework to a customer in 60 seconds
2. Open the right template for any engagement phase
3. Know which tools generate which deliverables
4. Understand where DMG Media UK (the reference engagement) fits at each phase
5. Identify which alliance partner programme applies to a given customer

---

## Part 1 — What Is the CRA Framework? (5 min)

The Cloud Readiness Accelerator (CRA) is a **four-phase assessment methodology** that takes a customer from "we are thinking about cloud" to "we have a signed migration statement of work."

It is **not** a migration framework. It produces the evidence and the business case that justifies the migration — and the Part 2 Entry Point document that kicks off the migration.

### The Four Phases

```
Phase 1: Discovery (7 weeks)
    └─ What do you have?
       Tools: Azure Migrate / GCP Migration Center / AWS ADS
       Deliverable: validated infrastructure inventory + utilisation data

Phase 2: Analysis (4 weeks — parallelised with back half of Phase 1)
    └─ What shape is it in?
       Tools: Cloud Readiness Scoring, Governance Alignment Tool
       Deliverable: cloud readiness scores, gaps, maturity assessment

Phase 3: Evaluation (3 weeks)
    └─ Where should it go?
       Tools: Azure / AWS / GCP evaluation templates, Hyperscaler Decision Matrix
       Deliverable: three-cloud TCO comparison + hyperscaler recommendation

Phase 4: Planning (6 weeks)
    └─ How do we get there?
       Tools: Migration Wave Planner, Risk Assessment, Business Case template
       Deliverable: Part 2 Entry Point — the commercial handoff to migration
```

**Total elapsed time (parallelised):** ~16 weeks for a mid-market engagement (1,000–5,000 VMs)

### The Two Hard Gates

These are non-negotiable. Do not skip them or your engagement will fail.

| Gate | Where | Why |
| --- | --- | --- |
| Phase 3 cannot start until Phase 1 has collected ≥2 weeks of clean utilisation data | End of Phase 1 | Right-sizing without utilisation data produces costs that are wrong by 30–50% |
| Part 2 SOW cannot be signed until partner funding deal registration is complete | End of Phase 4 | AMM / MAP / PSO registration after SOW signature risks losing the funding |

---

## Part 2 — The Repository Structure (5 min)

Everything you need is in one GitHub repository. The folder structure mirrors the four phases.

```
/
├── README.md                   ← Start here if you are a VP or Director
├── START-HERE.md               ← Start here if you are a Cloud Architect
├── docs/
│   ├── METHODOLOGY.md          ← Full phase methodology (v2.0 — authoritative)
│   ├── FRAMEWORK-INDEX.md      ← Map of all docs and templates
│   ├── guides/
│   │   ├── 00-architect-onboarding-guide.md    ← This file
│   │   ├── 01-discovery-phase-guide.md         ← How to run Phase 1
│   │   ├── 02-analysis-phase-guide.md          ← How to run Phase 2
│   │   ├── 03-evaluation-phase-guide.md        ← How to run Phase 3
│   │   └── 04-planning-phase-guide.md          ← How to run Phase 4 + SOW
│   ├── AWS-MAP-ALIGNMENT.md    ← Use this when AWS is primary or co-primary
│   ├── GOOGLE-PSO-ALIGNMENT.md ← Use this when GCP is primary or co-primary
│   └── MICROSOFT-CAF-ALIGNMENT.md ← Use this when Azure is primary or co-primary
├── Templates/
│   ├── 01-discovery/           ← Phase 1 templates
│   ├── 02-analysis/            ← Phase 2 templates
│   ├── 03-evaluation/          ← Phase 3 templates
│   ├── 04-planning/            ← Phase 4 templates
│   └── executive-reporting/    ← Final deliverable templates
├── Examples/
│   ├── azure/                  ← Azure assessment examples
│   ├── aws/                    ← AWS MPA pricing examples
│   └── media-entertainment/    ← DMG Media UK case study
└── presentations/
    ├── executive/              ← Leadership and customer decks
    └── alliance/               ← Microsoft / AWS / GCP partner decks
```

**The five files every architect must read before starting an engagement:**

| # | File | Time | What It Gives You |
| --- | --- | --- | --- |
| 1 | `START-HERE.md` | 5 min | Orientation — what to open first |
| 2 | `docs/METHODOLOGY.md` | 15 min | Phase durations, gate criteria, delivery model |
| 3 | Phase guide for your current phase | 15 min | Step-by-step execution guide |
| 4 | Relevant alliance alignment doc | 10 min | Partner programme eligibility and requirements |
| 5 | `Examples/media-entertainment/dmg-media-uk-case-study.md` | 20 min | Real engagement — what good looks like |

---

## Part 3 — Which Templates Do You Use When? (7 min)

### Phase 1 — Discovery

| Template | When | Purpose |
| --- | --- | --- |
| `Templates/01-discovery/application-scoping-profiling.xlsx` | Week 1–2 | Capture application inventory: name, owner, tech stack, VM count, dependencies |
| `Templates/01-discovery/infrastructure-profiling.xlsx` | Week 1–3 | Capture server/VM specs: CPU, RAM, storage, OS, hypervisor, location |
| `Templates/01-discovery/dependency-mapping.xlsx` | Week 2–4 | Map app-to-app and app-to-infra dependencies |

**Discovery tooling:**

| Customer direction | Tool to deploy | Notes |
| --- | --- | --- |
| Azure primary | Azure Migrate — agentless collector | Requires CAB approval for firewall rule; allow 5–10 business days lead time |
| GCP primary | Google Migration Center | Requires vCenter 6.5+, port 443 outbound; 2-week collection minimum |
| AWS primary | AWS Application Discovery Service (ADS) | Agentless collector; same CAB constraint as Azure Migrate |
| Multi-cloud / tool-agnostic | Movere / RVTools + manual profiling | Use when customer has restrictions on installing cloud vendor tooling |

> **Lesson from DMG Media UK:** Initiate CAB approval in week 1 of the engagement. Do not wait until the tooling is ready to request the firewall rule. A 5–10 business day delay in week 3 can push Phase 1 past its planned end date.

### Phase 2 — Analysis

| Template | When | Purpose |
| --- | --- | --- |
| `Templates/02-analysis/cloud-readiness-scoring-v2.xlsx` | Week 1 of Phase 2 | Score each application on cloud readiness across 6 dimensions |
| `Templates/02-analysis/readiness-scoring-criteria.xlsx` | Reference | Scoring criteria definition — what earns each score |
| `Templates/02-analysis/governance-foundations-alignment.xlsx` | Week 2–3 | Cloud governance maturity baseline |

**Phase 2 parallelisation rule:** Phase 2 can start approximately 1 week before Phase 1 ends, but only once the infrastructure inventory is validated (not before). You need the inventory to score cloud readiness. You do not need final utilisation data.

### Phase 3 — Evaluation

| Template | When | Purpose |
| --- | --- | --- |
| `Templates/03-evaluation/azure-evaluation.xlsx` | Week 1–2 | Azure sizing: PAYG and 3-year RI side-by-side, per region |
| `Templates/03-evaluation/aws-evaluation.xlsx` | Week 1–2 | AWS sizing: On-Demand + 3-year RI + Savings Plans |
| `Templates/03-evaluation/gcp-evaluation.xlsx` | Week 1–2 | GCP sizing: On-Demand + 3-year CUD |
| `Templates/03-evaluation/hyperscaler-decision-matrix.xlsx` | Week 2–3 | Weighted scoring across all 3 clouds; generates primary recommendation |
| `Templates/03-evaluation/business-case-tco-roi.xlsx` | Week 2–3 | Three-year TCO with licensing overlay and partner credits |

> **Do not run a single-hyperscaler evaluation.** Even when the customer has already decided (e.g., "we are Azure"), model all three. A documented comparison with a clear recommendation is more defensible than "we only looked at one." It also protects Rackspace commercially if the customer later claims the recommendation was biased.

### Phase 4 — Planning

| Template | When | Purpose |
| --- | --- | --- |
| `Templates/04-planning/migration-wave-planner.xlsx` | Week 1–2 | Sequence workloads into migration waves based on dependencies and risk |
| `Templates/04-planning/risk-assessment.xlsx` | Week 1–2 | Identify and score technical, licensing, operational, and timeline risks |
| `Templates/04-planning/governance-model.xlsx` | Week 2–3 | Define cloud operating model post-migration |
| `Templates/04-planning/sow-template.docx` | Week 4–6 | Generic CRA Part 1 SOW — basis for Part 2 SOW scoping |
| `Templates/executive-reporting/part2-entry-point-template.docx` | Week 5–6 | **Critical path** — the commercial handoff document |

---

## Part 4 — Alliance Partner Programmes (5 min)

Every CRA engagement should identify which partner programme applies. This is a commercial obligation, not optional — it directly reduces the customer's net migration cost.

### Quick Decision Table

| If primary cloud is... | Programme to pursue | Deal registration timing | Registration portal |
| --- | --- | --- | --- |
| Azure | AMM (Azure Migration and Modernisation) | Before Part 2 SOW signature | MSPP / Rackspace Alliance Manager |
| AWS | MAP (Migration Acceleration Programme) | At SoW scoping — not post-assessment | ACE portal (APN Customer Engagements) |
| GCP | RAMP / PSO co-delivery | At opportunity creation | Google Partner Advantage portal |

**Funding ranges (indicative — validate with Alliance Manager for current rates):**

| Programme | Typical funded value | What it covers |
| --- | --- | --- |
| Azure AMM | £500K–£2M+ depending on estate size | Funded professional services credits for migration delivery |
| AWS MAP | $100K–$500K+ | Funded Mobilize phase delivery; migration credits |
| GCP RAMP/PSO | $50K–$300K | Assessment credits; PSO co-delivery on migration |

> **Lesson from DMG Media UK:** Azure AMM eligibility was identified at the end of Phase 4. If it had been identified at Phase 1 and registered immediately, the deal registration would have been fully complete before the Part 2 SOW was drafted. Always check AMM/MAP/PSO eligibility at engagement start, not end.

**For detailed programme alignment:** Read the relevant doc before your first customer meeting on partner programmes:
- Azure: [`docs/MICROSOFT-CAF-ALIGNMENT.md`](../MICROSOFT-CAF-ALIGNMENT.md)
- AWS: [`docs/AWS-MAP-ALIGNMENT.md`](../AWS-MAP-ALIGNMENT.md)
- GCP: [`docs/GOOGLE-PSO-ALIGNMENT.md`](../GOOGLE-PSO-ALIGNMENT.md)

---

## Part 5 — The DMG Media UK Reference Engagement (5 min)

Read the case study at `Examples/media-entertainment/dmg-media-uk-case-study.md`. The summary below tells you what to look for.

### What Made It Complex

| Factor | Detail | Lesson |
| --- | --- | --- |
| Scope variance | 2,700 VMs in SOW → 4,212 VMs final (57% growth) | Scope gate at Part 2 SOW is non-negotiable |
| Oracle RAC | 18 clusters — highest cost and highest migration risk | Engage Oracle practice and Oracle account team in Phase 1, not Phase 3 |
| EoL OS | 340+ Windows 2012, RHEL 6 servers | ESU cost must be modelled in TCO; EoL servers are a migration urgency driver |
| Redis OSS | 140+ instances — commercial licence implications | Third-party licensing flags must be surfaced in Phase 2 scoring |
| GCP discovery | GCP Migration Center was the primary discovery tool | 2-week minimum collection window was the critical path for Phase 3 start |

### What the Output Looked Like

| Deliverable | Result |
| --- | --- |
| Primary recommendation | Microsoft Azure (UK South + UK West DR) |
| Three-year TCO saving | ~39% vs. on-prem status quo (AHB + 3yr RI applied) |
| Partner funding identified | Microsoft AMM eligibility confirmed |
| Assessment duration | ~16 weeks (parallelised) |
| Part 2 Entry Point | Issued; Part 2 SOW scoping in progress |

---

## Part 6 — Common Mistakes to Avoid (3 min)

These are the patterns that slow down or derail CRA engagements. Learn from DMG rather than repeating them.

| Mistake | Why It Happens | How to Avoid |
| --- | --- | --- |
| Starting Phase 3 before utilisation data is clean | Pressure from customer to "get to the numbers quickly" | Enforce the hard gate. Show the customer that without 2 weeks of data, the sizing will be wrong by 30–50% — costing them more in the long run |
| Under-scoping the estate | Customer gives a ballpark number; architect assumes it is accurate | Assume the real estate is 20–30% larger than the customer's initial estimate. Scope the SOW accordingly |
| Single-cloud evaluation | Customer has a strong preference | Always model all three. Document the comparison. Your recommendation is only defensible if alternatives were considered |
| Leaving licensing overlay to Phase 4 | Feels like detail work | Start the Oracle and SQL Server licence count in Phase 1. Licensing has a 20–35% impact on TCO — it is not a detail |
| Missing AMM/MAP/PSO deal registration timing | Not on the delivery team's radar | Add deal registration to the Phase 1 kickoff checklist. It is an Alliance Manager action, but the delivery team must trigger it |
| Oracle expert not engaged until Phase 4 | Oracle feels like "later" | Oracle RAC migration is 3–4x more complex than a standard workload. Engage the Oracle practice at Phase 1 |

---

## Quick Reference — Phase Durations

| Phase | Mid-Market Default | Small Engagement | Enterprise |
| --- | --- | --- | --- |
| Phase 1 — Discovery | **7 weeks** | 5–6 weeks | 9–10 weeks |
| Phase 2 — Analysis | **4 weeks** (parallel with Phase 1 back half) | 3 weeks | 5–6 weeks |
| Phase 3 — Evaluation | **3 weeks** | 2 weeks | 4 weeks |
| Phase 4 — Planning | **6 weeks** | 3–4 weeks | 8–10 weeks |
| **Total (parallelised)** | **~16 weeks** | ~10 weeks | ~22 weeks |

> All durations from `docs/METHODOLOGY.md` v2.0 — audited against DMG Media UK actuals.

---

## Your First Day Checklist

- [ ] Read `START-HERE.md` (5 min)
- [ ] Read `docs/METHODOLOGY.md` Sections 1–3 (15 min)
- [ ] Read this guide end to end (30 min)
- [ ] Open the phase guide for your current engagement phase
- [ ] Read `Examples/media-entertainment/dmg-media-uk-case-study.md` (20 min)
- [ ] Identify which alliance programme applies — read the relevant alignment doc
- [ ] Check: has CAB approval been initiated for discovery tooling?
- [ ] Check: has alliance deal registration been triggered with the Alliance Manager?

---

*Rackspace Cloud Solutions Architecture — CRA Framework v2.0*  
*Questions: contact the CRA practice lead or raise an issue at the GitHub repository*
