# CRA Technical Overview — Slide Content Script

**Deck:** `CRA-Technical-Overview.pptx`  
**Audience:** Rackspace Solutions Architects, Cloud Engineers, Delivery Leads — internal and technical partner audiences  
**Format:** 25 slides, 60-minute deep-dive session  
**Purpose:** Provide a complete technical and methodological understanding of the CRA framework: how each phase works, which tools are used, which templates are involved, what the quality gates are, and how to navigate common delivery challenges  
**Classification:** INTERNAL / PARTNER — suitable for sharing with Microsoft, AWS, and GCP technical teams once legal review complete

> **Build instructions:** Apply Rackspace Red `#E31C3D` for headings. Use Aktiv Grotesk Bold for headings. Footer: `© 2026 Rackspace Technology — CRA Framework v2.0`. Include slide numbers bottom-right. This deck is dense — use 12pt body text for tables. Speaker notes are mandatory on every slide.

---

## Slide 1 — Title Slide

**Title:** Cloud Readiness Accelerator — Technical Framework Overview  
**Subtitle:** Methodology, templates, tooling, and delivery guide for CRA practitioners  
**Presented by:** [Your Name], Rackspace Cloud Solutions Architecture  
**Date:** [Date]  
**Version:** CRA Framework v2.0

**Speaker notes:**  
This is a practitioner deck, not a sales deck. Audience is SAs, delivery architects, or technical alliance partners. The goal is full framework literacy — someone who completes this session should be able to lead a Phase 1 kickoff the following Monday without further briefing.

---

## Slide 2 — Agenda

**Heading:** What we will cover today

1. Framework architecture — phases, gates, and parallelisation model (5 min)
2. Phase 1 Deep Dive — Discovery tooling, data collection, quality gates (10 min)
3. Phase 2 Deep Dive — Readiness scoring, governance workshop, OSS flag (10 min)
4. Phase 3 Deep Dive — TCO 7-layer model, hyperscaler matrix, recommendation protocol (15 min)
5. Phase 4 Deep Dive — Wave planning, risk register, Part 2 Entry Point (10 min)
6. Templates — the 15 critical files and what each produces (5 min)
7. Failure modes — DMG Media UK lessons learned (5 min)

**Speaker notes:**  
Set expectations: this is a 60-minute session. There are 25 slides. The Phase 3 section is the densest and most important — do not rush it. The failure modes section at the end is the most practically valuable — it is based on a real engagement, not theory.

---

## Slide 3 — Framework Architecture

**Heading:** Four phases, two gates, one parallelisation point

**Full framework diagram:**

```
PHASE 1: DISCOVERY        PHASE 2: ANALYSIS      PHASE 3: EVALUATION     PHASE 4: PLANNING
  Weeks 1–7                 Weeks 6–10               Weeks 11–14              Weeks 11–20
  ─────────────────         ──────────────────        ─────────────────        ─────────────────
  Azure Migrate /           Cloud readiness           7-layer TCO model        Migration wave
  GCP Migration             scoring (5 dims)          per hyperscaler          plan
  Center /                  Governance maturity       Hyperscaler decision     Risk register
  AWS ADS                   assessment                matrix + scoring         Governance model
  VM + app + network        Dependency                Recommendation           Part 2 Entry
  utilisation data          analysis                  with evidence            Point
  App inventory             OSS licence flags

     PARALLELISATION POINT: Phase 2 starts at Phase 1 Week 6
                │                           │
                ▼                           ▼
            GATE 1:                      GATE 2:
       ≥14 days clean               Alliance partner deal
       utilisation data             registration complete
       before Phase 3               before Part 2 SOW
```

**Key architectural decisions (bullet list):**
- Phases 1 and 2 run in parallel from Week 6 — do not wait for Phase 1 to complete
- Gate 1 is hard and non-negotiable — it protects the integrity of all Phase 3 TCO modelling
- Gate 2 is pre-commercial — Alliance Manager must pre-register before countersignature

**Speaker notes:**  
The parallelisation point at Week 6 is the most commonly missed timing decision. Many architects wait for Phase 1 to fully complete before starting Phase 2 readiness scoring. This wastes 4–6 weeks. By Week 6, you have enough inventory data to begin readiness scoring on the first cohort of applications. Phase 2 can run alongside the remaining Phase 1 data collection.

---

## Slide 4 — Phase 1 Discovery — What You Are Doing

**Heading:** Phase 1 is a data quality project, not a documentation project

**Core objective:**  
Produce a complete, accurate, and validated inventory of every server, application, dependency, and licensing obligation in scope — with ≥14 days of clean CPU, RAM, storage, and network utilisation data from ≥90% of in-scope VMs.

**Three workstreams running simultaneously:**

| Workstream | Lead | Output |
|---|---|---|
| Infrastructure discovery tooling | Platform Architect (cloud-specific) | VM specs, OS, hypervisor, utilisation data, storage I/O |
| Application inventory | Engagement Lead Architect | Application workbook: tech stack, DB, VM count, readiness flag, dependencies |
| Dependency mapping | Engagement Lead Architect + App Owners | Dependency heat map: Tier-1 dependencies, tightly-coupled clusters |

**Speaker notes:**  
The three workstreams must run simultaneously. The common failure mode is to serialise them — finish infrastructure discovery, then do application inventory, then do dependencies. This costs 4–6 weeks. The application workshops (for dependency mapping) can happen at Week 2 while the tooling is still collecting data in the background.

---

## Slide 5 — Phase 1 Discovery — Tooling Selection

**Heading:** Choose the right discovery tool for the target hyperscaler

**Discovery tooling comparison:**

| Tool | Hyperscaler | Deployment | Data collected | Output to CRA |
|---|---|---|---|---|
| **Azure Migrate** | Azure primary | Agent or agentless (vCenter connector) | CPU, RAM, storage, network, OS, apps, dependencies | infrastructure-profiling.xlsx source data |
| **AWS Application Discovery Service (ADS)** | AWS primary | Agent-based (Discovery Agent) or agentless (Agentless Connector) | Server config, performance, network connections | aws-evaluation.xlsx input |
| **GCP Migration Center** | GCP primary | VM Manager agent or import from spreadsheet | CPU, RAM, storage, OS, running workloads | gcp-evaluation.xlsx input |
| **RVTools** | All hyperscalers | VMware utility — no agent needed | VMware inventory export: VMs, CPU, RAM, datastores, networks | Cross-validation with all three tools |

**Critical note:**  
Run **RVTools** export on Day 1 regardless of target hyperscaler. This gives you an instant VMware inventory to cross-validate against discovery tool output. Discrepancies between RVTools and discovery tool output indicate either incomplete agent deployment or shadow VMs.

**Firewall requirements — must submit CAB on Day 1:**

| Tool | Outbound requirement |
|---|---|
| Azure Migrate | TCP 443 from appliance to Azure URLs |
| AWS ADS | TCP 443 from collector to AWS endpoints |
| GCP Migration Center | TCP 443 from collector to googleapis.com |

**Speaker notes:**  
The CAB request is the single biggest schedule risk in Phase 1. In enterprise organisations with change management processes, a firewall change can take 5–15 business days to approve. If you do not submit the CAB request on Day 1, you will be waiting for firewall approval while the clock is running. Do not wait until the appliance is deployed before submitting the CAB — submit it on Day 1 based on the target URLs, even before the appliance is live.

---

## Slide 6 — Phase 1 Discovery — The Application Inventory

**Heading:** The application inventory is the source of truth for every downstream deliverable

**Template:** `Templates/01-discovery/application-scoping-profiling.xlsx`

**25 required columns (key columns highlighted):**

| Column | Description | Why Critical |
|---|---|---|
| Application Name | Official application name | Primary key — all other templates reference this |
| Business Owner | Named owner — not a team | Drives governance workshop invitations in Phase 2 |
| Application Tier | Tier 1 (mission-critical) / 2 / 3 | Drives wave sequencing in Phase 4 |
| Primary VM Count | Number of VMs supporting this application | Feeds TCO model and scope validation |
| Database Type | Oracle / SQL Server / PostgreSQL / MySQL / NoSQL | **Oracle flag — escalate immediately if Oracle RAC/EE** |
| Oracle Practice Flag | Yes / No | If Yes: engage Oracle Practice Lead in Phase 1 Week 2 |
| OSS Licence Risk Flag | Yes / No / Review | Redis OSS, Elasticsearch, HashiCorp Vault — licence change risk |
| Scope Confidence | High / Medium / Low | Data from CMDB = Low; data from actual tooling = High |
| Cloud Readiness (P1 estimate) | Preliminary score from Phase 1 data | Used to prioritise Phase 2 readiness scoring |
| Dependency Cluster | Cluster ID (groups tightly-coupled apps) | Cannot separate these in wave planning |

**Key quality rules:**
- Every application must have a named Business Owner — "IT Team" is not acceptable
- Oracle RAC or Oracle EE flag → Oracle Practice Lead engaged same day
- OSS Licence Risk flagged → Commercial Legal or Oracle/OSS specialist engaged Phase 2
- Scope Confidence "Low" → cross-validate with tooling before Phase 3

**Speaker notes:**  
The Oracle practice flag is the most important column in this workbook. Any Oracle RAC or Oracle EE finding in Phase 1 should trigger an immediate escalation to the Oracle Practice Lead — the same day, not when Phase 3 starts. Oracle licensing analysis takes 4–6 weeks. If you start it in Phase 3, it becomes the critical path blocker for your TCO model.

---

## Slide 7 — Phase 1 Discovery — Data Quality Gate

**Heading:** GATE 1 — Phase 3 cannot start without this

**Gate criteria:**

| Criterion | Minimum Threshold | Measured In |
|---|---|---|
| Utilisation data collection period | ≥14 days continuous clean data | Days from first clean collection to gate check |
| VM coverage | ≥90% of in-scope VMs reporting | % of VMs with utilisation data vs. total in RVTools export |
| CPU data quality | P95 values available for ≥90% of VMs | Checked in infrastructure-profiling.xlsx Data Quality tab |
| RAM data quality | P95 values available for ≥90% of VMs | Same |
| Storage I/O data | Available for VMs flagged as I/O-sensitive | At minimum for databases and high-IOPS workloads |

**Why the gate is hard:**

> "TCO right-sizing is only as accurate as the utilisation data it is based on. Using 6 days of data instead of 14 produces right-sizing recommendations with ±30–50% error. An error of that magnitude in a 3-year TCO model for a 500-VM estate is a £2M–£5M range — not an acceptable board-level business case."

**How to hold the gate under pressure:**

When customers push to "skip the data window":
1. Quantify the risk in writing: "Based on current data quality, TCO estimates have ±X% accuracy. At [estate size], that represents a potential £[amount] variance in the business case."
2. Offer an interim: share Phase 1 discovery report (application inventory, dependency map) while data collection continues
3. Document the customer's decision if they override the gate — not Rackspace's recommendation

**Speaker notes:**  
This is a real conversation you will have on most engagements. The customer has a board date. The programme manager wants to show progress. The commercial director wants to "move to numbers." The data window is the line you do not move. The DMG Media UK engagement had this exact conversation — the data window was held, and the TCO model was accurate. Engagements where the window is shortened produce inaccurate TCO models that the customer then disputes in Phase 4.

---

## Slide 8 — Phase 2 Analysis — Readiness Scoring

**Heading:** Phase 2 Analysis — Five dimensions. One readiness score. Per application.

**Template:** `Templates/02-analysis/cloud-readiness-scoring-v2.xlsx`

**5-dimension scoring model:**

| Dimension | Scale | What Low Score Means |
|---|---|---|
| **Technical Complexity** | 1 (complex) – 5 (simple) | Legacy OS, custom middleware, tightly-coupled architecture, bare-metal requirements |
| **Business Criticality** | 1 (critical) – 5 (non-critical) | RTO < 4hrs, RPO < 1hr, zero-downtime migration required, regulatory significance |
| **Data Sensitivity** | 1 (highly sensitive) – 5 (non-sensitive) | PII, financial data, FCA-regulated data, GDPR data with sovereignty constraints |
| **Dependency Risk** | 1 (high dependency) – 5 (low dependency) | Many tightly-coupled dependencies, cannot migrate independently, on-prem latency requirements |
| **Licence Risk** | 1 (high risk) – 5 (low risk) | Oracle RAC, Oracle EE, IBM ILMT, Windows Server (without AHB), SAP |

**Composite score mapping:**

| Composite Score (mean of 5 dims) | Readiness Category | Default Migration Path |
|---|---|---|
| 4.0–5.0 | Cloud Ready | Rehost (lift-and-shift) |
| 3.0–3.9 | Cloud Friendly | Replatform (minor changes) |
| 2.0–2.9 | Cloud Challenged | Rearchitect (significant effort) |
| 1.0–1.9 | Blocked | Retain on-prem or specialist path |

**Speaker notes:**  
The individual dimension scores are as important as the composite. An application that scores 5/5 on 4 dimensions but 1/5 on Licence Risk is "Cloud Challenged" overall — the licence risk alone can make the application economically or legally unmovable. Always review dimension-level scores, not just the composite. Any Licence Risk score of 1 or 2 requires Oracle or Commercial Practice Lead involvement before Phase 3 TCO is built.

---

## Slide 9 — Phase 2 Analysis — Governance Workshop

**Heading:** Phase 2 Analysis — The governance maturity assessment

**Template:** `Templates/02-analysis/governance-foundations-alignment.xlsx`

**6 governance domains and what you assess:**

| Domain | Assessment Focus | Key Questions |
|---|---|---|
| **Identity & Access Management (IAM)** | RBAC (Role-Based Access Control) maturity, MFA, privileged access management | Does the customer use RBAC today? Are service accounts managed? Is MFA enforced? |
| **Security & Compliance** | Policy enforcement, DLP (Data Loss Prevention), SIEM (Security Information and Event Management), vulnerability management | Can they enforce security policy at scale in cloud? Is cloud included in their vulnerability programme? |
| **Change & Release Management** | CAB process maturity, CI/CD capability, approval gates | Do they have automated deployment pipelines? Will cloud changes go through the same CAB? |
| **Monitoring & Observability** | Current monitoring stack, alerting, log management, ITSM (IT Service Management) integration | Can they monitor cloud workloads with existing tools? Do they have an on-call process for cloud? |
| **Cost Management (FinOps)** | Budget visibility, showback/chargeback, cost allocation tagging strategy | Who owns cloud spend? Does IT have a budget model for variable cloud costs? |
| **Operations Readiness** | Run book documentation, SLA management, knowledge transfer plan | Are current operations documented? Do they have skills to operate cloud workloads? |

**Maturity scale:**

| Level | Label | Description |
|---|---|---|
| 1 | Initial | Ad-hoc, undocumented, dependent on individuals |
| 2 | Developing | Partial processes, inconsistently applied |
| 3 | Defined | Documented, consistently applied across most areas |
| 4 | Managed | Metrics-driven, improving over time |
| 5 | Optimising | Continuous improvement, automation-first |

**Speaker notes:**  
The governance workshop is a 2–3 hour session with the customer's IT Director. Do not send a spreadsheet in advance — this is a conversation, not a survey. The goal is an honest baseline, not a flattering picture. Low scores in IAM and FinOps are common and expected. They become inputs to the Phase 4 governance recommendations, not criticisms of the customer's team.

---

## Slide 10 — Phase 2 Analysis — OSS Licence Risk Flags

**Heading:** Phase 2 — The commercial licence time bomb you must not miss

**Why this matters — the licence change landscape:**

Several widely-used open-source software (OSS) products changed their licensing model in 2023–2024, creating potential commercial obligations for cloud deployments:

| Product | Licence Change | Cloud Migration Risk |
|---|---|---|
| **Redis OSS** (post v7.4) | SSPL / RSALv2 — requires paid Redis licence for commercial use | Any Redis instance in scope requires licence review before cloud deployment |
| **Elasticsearch** (post 7.10) | SSPL — similar restrictions | Check if customer uses elastic.co's Elasticsearch or the AWS/GCP-managed fork (OpenSearch / Elastic Cloud) |
| **HashiCorp Vault / Terraform** | BSL — commercial use restrictions | Enterprise licence may be required for cloud automation at scale |
| **MongoDB** | SSPL — cloud deployment restrictions | Validate which version and what managed service alternative applies |

**Action trigger:**  
Any OSS Licence Risk Flag in the application inventory → immediate commercial review in Phase 2 before TCO is built. A TCO model that does not include OSS re-licensing costs is incomplete and will create budget surprises.

**Alternatives to recommend (where applicable):**
- Redis OSS → Azure Cache for Redis (Microsoft-licensed) / AWS ElastiCache / Memorystore
- Elasticsearch → OpenSearch (Apache 2.0 licensed) / Elastic Cloud
- HashiCorp Vault → Azure Key Vault / AWS Secrets Manager (if not vault-specific features needed)

**Speaker notes:**  
This is a real DMG Media UK finding. The engagement identified 140+ Redis instances. Had this been missed and the customer deployed Redis OSS at scale in Azure without a paid licence, the commercial exposure would have been significant. The OSS flag column in the application inventory exists specifically because of this engagement. Flag it in Phase 1, resolve the licence question in Phase 2, and model the correct cost in Phase 3.

---

## Slide 11 — Phase 3 Evaluation — TCO Architecture

**Heading:** The 7-layer TCO model — why each layer exists

**Template:** `Templates/03-evaluation/business-case-tco-roi.xlsx`

**Layer-by-layer breakdown:**

| Layer | Tab Name | What It Calculates | Common Mistake |
|---|---|---|---|
| **(a) Like-for-Like** | `L4L-Baseline` | Cloud cost of running exact current spec on cloud | Using rounded estimates instead of actual P95 utilisation |
| **(b) Optimised** | `Optimised-Rightsized` | Cloud cost using right-sized instances based on P95 utilisation | Using P50 (median) instead of P95 — underestimates required size |
| **(c) Delta** | Calculated | Layer b minus layer a | Presenting this as "the saving" without showing layers d–g |
| **(d) Licensing Overlay** | `Licensing-Overlay` | SQL AHB, Windows AHB, Oracle BYOL, third-party | Omitting Oracle BYOL licensing premium/saving |
| **(e) On-Prem Status Quo** | `OnPrem-StatusQuo` | Current hardware + DC + maintenance + software over 3 years | Using standard depreciation without including hardware refresh cycle |
| **(f) Year 1 Dual-Running** | `Year1-DualRunning` | Cloud ramp-up + remaining on-prem during migration overlap | Omitting parallel environment costs (the most common budget shock) |
| **(g) Partner Credits** | `Partner-Credits` | AMM / MAP / PSO funding applied to net cost | Building the board case without this — largest "headline number" driver |

**3-year summary output:**  
The `TCO-Summary` tab produces the board-level number: 3-year net cost cloud (post-partner funding) vs. 3-year on-prem status quo.

**Speaker notes:**  
Walk through why each layer is included. The most important message is that layers a–c only tell part of the story. Layers d–g are where the compelling numbers are — and where most free hyperscaler assessment tools stop. Layer (e) on-prem status quo is often the most surprising for customers: when they see their actual 3-year on-prem cost (including the hardware refresh they know is coming and the VMware licence renewal), the cloud cost comparison changes significantly.

---

## Slide 12 — Phase 3 Evaluation — Hyperscaler Pricing Sources

**Heading:** Where to get current pricing — and what to watch for

**Azure Pricing:**

| Resource | URL | Notes |
|---|---|---|
| Azure Pricing Calculator | https://azure.microsoft.com/en-us/pricing/calculator/ | Primary source; use for D/E-series (Dsv5, Esv5) for general workloads |
| Azure Migrate Cost Estimate | Embedded in Azure Migrate portal | Cross-validate with calculator — Migrate uses current published rates |
| Azure Hybrid Benefit Calculator | https://azure.microsoft.com/en-us/pricing/hybrid-benefit/ | Critical for SQL Server-heavy estates — typically 30–40% saving on SQL |

**AWS Pricing:**

| Resource | URL | Notes |
|---|---|---|
| AWS Pricing Calculator | https://calculator.aws/pricing/2/home | Use for m6i (general purpose), r6i (memory-optimised) family comparison |
| AWS Migration Evaluator | https://aws.amazon.com/migration-evaluator/ | Generates a business case based on actual on-prem data |
| AWS Savings Plans Calculator | Embedded in Cost Explorer | Model 1-year and 3-year savings plans |

**GCP Pricing:**

| Resource | URL | Notes |
|---|---|---|
| GCP Pricing Calculator | https://cloud.google.com/products/calculator | Use for n2-standard (general), n2-highmem (memory) families |
| GCP Migration Center | https://cloud.google.com/migration-center/docs | Import RVTools export directly; produces right-sizing recommendations |

**Important:** Cloud pricing changes quarterly. Validate all pricing at the start of Phase 3. Do not use pricing captured more than 90 days ago.

**Speaker notes:**  
Cross-validate the Migrate/Migration Center pricing outputs against the manual calculators — they sometimes diverge due to reserved instance discounts being pre-applied or not. Always document the pricing source and date in the TCO workbook. If a customer challenges a TCO number 6 months later, you need to be able to show the source and explain any price changes.

---

## Slide 13 — Phase 3 Evaluation — Licensing Overlay Deep Dive

**Heading:** The licensing overlay — where the real money is

**Template:** `Templates/03-evaluation/business-case-tco-roi.xlsx` → `Licensing-Overlay` tab

**SQL Server and Windows — Azure Hybrid Benefit (AHB):**

| Licence Type | PAYG Cloud Cost | With AHB | Saving |
|---|---|---|---|
| SQL Server Standard (per core) | ~$146/month (example) | ~$0/month (bring own licence) | ~$146/month per 2-core pack |
| SQL Server Enterprise (per core) | ~$584/month (example) | ~$0/month (bring own licence) | ~$584/month per 2-core pack |
| Windows Server Datacenter | Included in VM cost | Excluded (AHB applied) | 15–40% VM cost reduction |

**Azure Hybrid Benefit eligibility criteria:**
- Customer must have active Software Assurance (SA) on their SQL Server or Windows Server licences
- SQL Server Developer and Express editions do not qualify
- AHB can be applied to Azure VMs, Azure SQL Managed Instance, and Azure SQL Database

**Oracle — BYOL (Bring Your Own Licence):**

| Oracle Licence Type | Cloud Impact | CRA Action |
|---|---|---|
| Oracle SE2 / EE (standard) | BYOL available on Azure, AWS, GCP | Validate licence mobility clauses with Oracle |
| Oracle RAC | Requires OCI or specific AWS/Azure configurations | Escalate to Oracle Practice Lead — complex |
| Oracle NUP (Named User Plus) | Count does not change — cloud neutral | Validate named user count against cloud deployment |
| Oracle ULA (Unlimited Licence Agreement) | Cloud deployment may or may not be in scope | Legal/Oracle specialist review required |

**Speaker notes:**  
For a Microsoft-heavy estate (Windows Server + SQL Server), AHB can represent 15–25% of the total 3-year TCO. This is not a marginal saving — it is often the difference between cloud being cheaper or more expensive than on-prem. Every CRA engagement must model both the PAYG and AHB scenarios in the TCO, and the AHB scenario must be clearly labelled as "requires active Software Assurance." If the customer does not have SA, the AHB saving is not available.

---

## Slide 14 — Phase 3 Evaluation — Hyperscaler Decision Matrix

**Heading:** The recommendation must follow the evidence — always

**Template:** `Templates/03-evaluation/hyperscaler-decision-matrix.xlsx`

**9 required tabs:**

| Tab | Purpose |
|---|---|
| `Criteria-Weights` | Customer-agreed weighting for each evaluation criterion — agreed BEFORE scoring |
| `Azure-Evaluation` | Azure-specific scores with evidence references |
| `AWS-Evaluation` | AWS-specific scores with evidence references |
| `GCP-Evaluation` | GCP-specific scores with evidence references |
| `Comparative-Matrix` | Side-by-side weighted scores across all three |
| `7Rs-Estate-View` | Each application classified: Rehost/Replatform/Rearchitect/Repurchase/Retire/Retain/Relocate |
| `Multi-Cloud-Exceptions` | Applications that cannot go to primary cloud — documented with rationale |
| `Worked-Example` | Anonymised DMG Media UK scoring (for reference and calibration) |
| `Instructions` | How to use this workbook — read before scoring |

**Critical validation rules before presenting the recommendation:**

1. **Criteria weights were agreed in writing before scoring** — not after
2. **All three hyperscalers were scored** — never eliminate one before the matrix is complete
3. **Every score has an evidence reference** — "expert judgment" is not evidence
4. **Recommendation slide comes AFTER the evidence slides** in the customer playback deck
5. **The matrix score and the recommendation are consistent** — if Azure scores highest, the recommendation is Azure

**Speaker notes:**  
The "evidence before recommendation" principle is the most important quality rule in the entire framework. If a customer sees the recommendation on slide 4 and the evidence on slides 12–15, they will correctly conclude the recommendation was pre-determined. The recommendation must be the conclusion, not the premise. In the DMG Media UK engagement, an early draft of the deck had the recommendation early — it was restructured before the customer saw it.

---

## Slide 15 — Phase 3 Evaluation — The Recommendation Protocol

**Heading:** How to present a hyperscaler recommendation credibly

**The structure that works:**

| Section | Content | Notes |
|---|---|---|
| Evidence: TCO Analysis | Layer-by-layer cost comparison across all 3 clouds | Present all 3 — do not pre-filter |
| Evidence: Licensing Overlay | AHB / BYOL impact per cloud | Show the licence-adjusted numbers |
| Evidence: Partner Funding | AMM / MAP / PSO by cloud | Confirm which programmes are available for each |
| Evidence: Readiness Scores | Application portfolio fit for each cloud | Show Blocked / Challenged counts per cloud |
| Evidence: Hyperscaler Matrix | Weighted scores by agreed criteria | Show all 3 side-by-side |
| **Recommendation** | **Primary + secondary cloud + rationale** | **Comes after all evidence — never before** |
| Risk Register | Risks associated with recommended path | Balances the recommendation |
| Migration Waves | High-level wave plan for recommended path | Shows it is executable |
| Next Steps / Part 2 | Part 2 Entry Point presentation | Commercial handoff |

**Equal treatment rule:**  
All three clouds must be represented with equal depth in the evidence sections. If Azure is the recommendation, AWS and GCP must still appear in the TCO comparison and the decision matrix with full scores — not as token entries.

**Speaker notes:**  
This structure is the one that survives customer scrutiny. The DMG engagement followed this structure. Microsoft, AWS, and GCP representatives were invited to the Phase 3 playback — all three were in the room. Having all three present is the strongest possible signal that the evaluation was objective. Recommend inviting all three hyperscaler SEs to the Phase 3 playback as standard practice.

---

## Slide 16 — Phase 4 Planning — Migration Wave Design

**Heading:** Phase 4 Planning — How to sequence 280 applications into a migration programme

**Template:** `Templates/04-planning/migration-wave-planner.xlsx`

**Wave sequencing principles:**

| Wave | Characteristics | Typical Applications |
|---|---|---|
| **Wave 0** | Proof of Concept — non-production, 5–10% of estate, 8–12 weeks | Dev/Test environments; simple Tier-3 apps with no dependencies; not Tier-1 |
| **Wave 1** | Cloud Ready, low dependency, Tier-3 | Internal tools, dev environments, simple web apps |
| **Wave 2** | Cloud Friendly, low-medium complexity | Mid-tier applications, some dependencies, medium RTO requirements |
| **Wave 3** | Cloud Challenged or medium-high complexity | Custom middleware, complex dependencies, tighter RTO requirements |
| **Wave 4** | Tier-1 business-critical applications | ERP, CRM, core business systems — migrate only after waves 1–3 validated |
| **Wave 5+** | Retained, Oracle specialist, multi-cloud exceptions | Applications that need special handling or are staying on-prem |

**Hard rules:**
- **Do not put Tier-1 applications in Wave 0** — this is a PoC, not a migration
- **Do not put Oracle RAC clusters in Wave 1** — Oracle specialist migration path required
- **Dependency clusters must move together** — never split a tightly-coupled cluster across waves

**What the wave plan document contains:**
- Application name, tier, readiness score, target cloud, target region, wave assignment
- Wave 0 PoC success criteria (defined before Wave 0 starts)
- Estimated migration duration per wave (weeks)
- Resource model per wave (Rackspace FTEs + customer FTEs)
- Rollback plan per wave (what happens if the wave fails)

**Speaker notes:**  
The hardest conversation in Phase 4 is moving a customer's favourite application out of Wave 0. They will say "let's start with our SAP system so we can prove the value." SAP in Wave 0 is a recipe for a very expensive failed PoC. Wave 0 must be low-risk, low-complexity, and easily reversible. Save the complex workloads for when the migration tooling and processes have been validated on simpler applications.

---

## Slide 17 — Phase 4 Planning — Risk Register

**Heading:** Phase 4 Planning — Eleven risk categories you must cover

**Template:** `Templates/04-planning/risk-assessment.xlsx`

**11 required risk categories with default examples:**

| Category | Example Risk | Default Likelihood | Default Impact |
|---|---|---|---|
| **Scope** | Estate larger than scoped in SoW | High (4) | High (4) |
| **Data Quality** | Utilisation data < 14 days clean | Medium (3) | Critical (5) |
| **Dependency** | Undocumented application dependencies block wave sequencing | Medium (3) | High (4) |
| **Licensing** | Oracle EE licence not cloud-portable | Medium (3) | Critical (5) |
| **End-of-Life OS** | Windows Server 2012 / RHEL 6 ESU commitment required | High (4) | High (4) |
| **Regulatory** | Data sovereignty constraint blocks primary cloud region | Low (2) | Critical (5) |
| **Schedule** | Customer CAB approval delays Phase 1 by ≥2 weeks | Medium (3) | Medium (3) |
| **Resource** | Customer IT resource unavailable for Phase 2 workshops | Medium (3) | Medium (3) |
| **Commercial** | Partner deal registration missed before Part 2 SOW | Low (2) | High (4) |
| **Stakeholder** | CTO changes during assessment — recommendation re-presented | Low (2) | Medium (3) |
| **Third-Party** | Oracle Practice Lead availability delays Phase 2 | Medium (3) | Medium (3) |

**Risk scoring:** Likelihood × Impact = Risk Score. Score ≥ 9 = Red; 6–8 = Amber; ≤ 5 = Green.

**Speaker notes:**  
Pre-populate the risk register with these 11 default risks in every engagement. They are all real — every one has been encountered in a CRA engagement. Adjust the likelihood and impact scores based on what you know about the specific customer. The Oracle licensing risk and the scope risk are the two most commonly underestimated risks in mid-market assessments.

---

## Slide 18 — Phase 4 Planning — Part 2 Entry Point

**Heading:** The Part 2 Entry Point — the most commercially important deliverable

**Template:** `Templates/executive-reporting/part2-entry-point-template.docx`

**10 required sections:**

| # | Section | Key Content |
|---|---|---|
| 1 | Executive Summary | 1-page: what was assessed, what was found, what is recommended |
| 2 | Engagement Overview | Rackspace methodology summary, team structure |
| 3 | Hyperscaler Recommendation | Copy from Phase 3 report — do not re-derive |
| 4 | TCO Summary | 3-year net cost from Phase 3 TCO model (post-partner funding) |
| 5 | Partner Funding | AMM/MAP/PSO eligibility confirmed; registration status |
| 6 | Proposed Migration Scope | Application count by wave, complexity distribution |
| 7 | Indicative Timeline | Phase-by-phase (Mobilise → Wave 0 → Wave 1 → etc.) |
| 8 | Governance and Risk Summary | Top-5 risks from Phase 4 risk register |
| 9 | Oracle / Specialist Workloads | If applicable — separate workstream and timeline |
| 10 | Investment Summary | Part 2 fixed-fee investment, net of partner funding |

**Hard rule:**  
Alliance Manager must confirm AMM/MAP/PSO deal registration status before Section 5 is written. Do not write estimated partner funding into the document if registration is not confirmed.

**GATE 2 reminder:**  
Alliance partner deal registration must be COMPLETE before Rackspace countersigns the Part 2 SOW. Check with the Alliance Manager before preparing Section 5.

**Speaker notes:**  
Section 3 (hyperscaler recommendation) must be copied directly from the Phase 3 report — not summarised, reworded, or abbreviated. If the customer asks for a change to the recommendation between Phase 3 and Phase 4, that is a scope change and must go through formal change control. The Part 2 Entry Point is a commercial document that the customer's CEO or CFO may sign. It must be precisely consistent with what was presented in the Phase 3 playback.

---

## Slide 19 — The 15 Critical Templates

**Heading:** These 15 templates produce every CRA deliverable

| # | Template | Phase | What It Produces |
|---|---|---|---|
| 1 | `application-scoping-profiling.xlsx` | Phase 1 | Application inventory, Oracle flags, readiness estimate |
| 2 | `infrastructure-profiling.xlsx` | Phase 1 | VM specs, OS, utilisation data, Data Quality Summary |
| 3 | `dependency-mapping.xlsx` | Phase 1 | App-to-app and app-to-infra dependency heat map |
| 4 | `cloud-readiness-scoring-v2.xlsx` | Phase 2 | 5-dimension readiness scores per application |
| 5 | `governance-foundations-alignment.xlsx` | Phase 2 | Governance maturity scores, 6 domains, 1–5 scale |
| 6 | `risk-assessment.xlsx` | Phase 2+4 | Risk register, 11 categories, likelihood × impact |
| 7 | `azure-evaluation.xlsx` | Phase 3 | Azure TCO: PAYG + RI + AHB overlay |
| 8 | `aws-evaluation.xlsx` | Phase 3 | AWS TCO: On-Demand + RI + Savings Plans |
| 9 | `gcp-evaluation.xlsx` | Phase 3 | GCP TCO: On-Demand + 3yr CUDs |
| 10 | `business-case-tco-roi.xlsx` | Phase 3 | 7-layer TCO: all 3 clouds, all layers, 3yr summary |
| 11 | `hyperscaler-decision-matrix.xlsx` | Phase 3 | Weighted scores, 7Rs classification, recommendation |
| 12 | `migration-wave-planner.xlsx` | Phase 4 | Wave sequence, timeline, resource model, rollback plan |
| 13 | `governance-model.xlsx` | Phase 4 | RACI matrix, operating model, governance charter |
| 14 | `cra-assessment-report-template-v3.docx` | Phase 3 | Full assessment report (40–60 pages) |
| 15 | `cra-executive-summary-v3.pptx` | Phase 3 | Executive summary deck (18 slides) |

**Speaker notes:**  
Know these 15 templates well. Every CRA deliverable traces back to one or more of them. The most important are 1, 2, 10, 11, and 15 — these are the five files that go to the customer's board. Templates 1–9 are working documents that feed into them.

---

## Slide 20 — Common Failure Modes — DMG Media UK Lessons

**Heading:** Nine lessons from a real engagement — in your framework now

**Lessons summary (brief — expanded in `docs/DMG-MEDIA-UK-LESSONS-LEARNED.md`):**

| # | Lesson | Impact if Missed | Template/Process Updated |
|---|---|---|---|
| 1 | Scope variance: 57% more VMs than SoW | Budget overrun; renegotiation risk | Scope variance clause in SoW; confidence scoring in application-scoping |
| 2 | CAB request: not submitted Day 1 | 2-week delay to Phase 1 data collection | Phase 1 kickoff checklist — CAB on Day 1 |
| 3 | Oracle RAC found in Phase 1 Week 5 | Oracle analysis delayed Phase 3 by 6 weeks | Oracle Practice Flag column in application inventory |
| 4 | Redis OSS licence change discovered in Phase 3 | TCO model incomplete; re-work required | OSS Licence Risk column in application inventory |
| 5 | AMM not pre-registered at Phase 1 | Customer missed AMM funding eligibility | AMM registration in Phase 1 kickoff; Alliance Manager on Day 1 call |
| 6 | Utilisation data window shortened under pressure | TCO accuracy compromised | Gate 1 hard requirement; written escalation process |
| 7 | Phase 2 not started until Phase 1 complete | 4-week delay to overall timeline | Parallelisation model: Phase 2 starts at Phase 1 Week 6 |
| 8 | EoL OS not flagged until Phase 3 | ESU costs missed in TCO; licensing re-work | EoL OS column in infrastructure-profiling; EoL flag in risk register |
| 9 | Recommendation before evidence | Customer challenged recommendation credibility | Evidence-before-recommendation rule; deck structure validation checklist |

**Speaker notes:**  
This is the most important slide in the deck for practitioners. Every one of these lessons resulted in a concrete change to the framework. When a new architect asks "why is the OSS flag column in the application inventory?" — this is why. The framework improves with every engagement. After your next CRA engagement, identify one new lesson and embed it.

---

## Slide 21 — The Alliance Manager's Role

**Heading:** The Alliance Manager is a Phase 1 team member — not a Phase 3 afterthought

**Common mistake:** Alliance Manager is briefed at Phase 3 when the recommendation is known. By then, deal registration windows for AMM/MAP/PSO may have closed.

**Required Alliance Manager involvement by phase:**

| Phase | Required Action | Timing |
|---|---|---|
| Pre-engagement (SoW scoping) | Screen for AMM/MAP/PSO eligibility; advise on deal registration requirements | Before SoW is signed |
| Phase 1 Kickoff | Pre-register the opportunity in Microsoft MSPP / AWS ACE / Google Partner Advantage | Day 1 of Phase 1 |
| Phase 1 Week 2 | Confirm registration is active and acknowledge received from hyperscaler partner team | Week 2 |
| Phase 3 (recommendation complete) | Update deal registration with actual recommended cloud and scope | Week 14 (immediately after recommendation) |
| Phase 4 (Part 2 Entry Point) | Confirm deal registration status for Section 5 of Part 2 Entry Point | Before Part 2 Entry Point is shared with customer |

**Hard gate:**  
AMM/MAP/PSO registration MUST be complete before Rackspace countersigns the Part 2 SOW.

**Speaker notes:**  
The Alliance Manager must be on the Phase 1 kickoff call. Not "briefed before." On the call. This is the one practice change that has the highest commercial impact — missing AMM registration cost a real engagement access to potential seven-figure funding. The customer was understandably frustrated. This is now a hard requirement in the CRA framework.

---

## Slide 22 — EoL Operating Systems — Don't Miss This

**Heading:** End-of-Life (EoL) OS — the cost item that appears from nowhere in Phase 3

**Template:** `Templates/01-discovery/infrastructure-profiling.xlsx` → `EoL-OS-Flag` column

**Critical EoL OS landscape:**

| OS | EoL Date | Cloud Options | Cost Implication |
|---|---|---|---|
| Windows Server 2012/R2 | Oct 2023 | Extended Security Updates (ESU) available in Azure (free) | In Azure: ESU free until 2026. In AWS/GCP: customer must pay Microsoft ESU |
| Windows Server 2019 | Jan 2029 | Standard support | Minimal immediate impact |
| RHEL 6 | Nov 2020 | RHEL ELS (Extended Life Cycle Support) | Additional Red Hat support subscription required |
| Ubuntu 18.04 LTS | Apr 2023 | Ubuntu Pro available | Ubuntu Pro subscription required for ESU |
| SQL Server 2012/2014 | Jul 2022 / Jul 2024 | ESU available in Azure (free) | In Azure: ESU free. In AWS/GCP: pay Microsoft ESU |

**Key Azure advantage:**  
Windows Server 2012 and SQL Server 2012/2014 ESU is **free** when running in Azure. This can represent a significant 3-year saving for customers with large EoL Windows or SQL estates — and it belongs in the Licensing Overlay (Layer d) of the TCO model.

**Action:**  
Flag all EoL OS instances in Phase 1 → include in risk register → model ESU cost (or Azure ESU saving) in Phase 3 TCO licensing overlay.

**Speaker notes:**  
This is another common TCO gap. If a customer has 200 Windows Server 2012 VMs, the ESU cost difference between Azure (free) and AWS or GCP (paid ESU to Microsoft) can be £300K–£500K over 3 years. This is a legitimate Azure cost advantage that must appear in the TCO model. Do not omit it because it appears to favour Azure — present the evidence and let the data drive the recommendation.

---

## Slide 23 — Quality Assurance Checklist Before Customer Playback

**Heading:** Before you present Phase 3 to the customer — 10 checks

**Pre-playback QA checklist:**

| # | Check | Template/Location |
|---|---|---|
| ☐ 1 | ≥14 days clean utilisation data confirmed for ≥90% of VMs | infrastructure-profiling.xlsx Data Quality tab |
| ☐ 2 | All 7 TCO layers populated for each cloud | business-case-tco-roi.xlsx — no blank rows |
| ☐ 3 | Pricing validated against calculator source this week | business-case-tco-roi.xlsx source date field |
| ☐ 4 | AHB eligibility confirmed (SA status verified) | Licensing-Overlay tab — AHB Yes/No confirmed |
| ☐ 5 | Oracle licensing reviewed by Oracle Practice Lead | Email sign-off from Oracle Practice |
| ☐ 6 | OSS licence flags resolved — all modelled in TCO | Licensing-Overlay tab — OSS rows complete |
| ☐ 7 | Hyperscaler matrix weights agreed in writing by customer | Criteria-Weights tab — customer sign-off email filed |
| ☐ 8 | All three clouds scored with evidence references | Azure/AWS/GCP Evaluation tabs — no blank evidence fields |
| ☐ 9 | Recommendation slide comes AFTER evidence slides | Deck slide order checked: Rec ≥ Slide 13 |
| ☐ 10 | AMM/MAP/PSO registration confirmed by Alliance Manager | Email from Alliance Manager filed |

**Speaker notes:**  
This checklist is not optional before presenting to a customer CTO. A missing check is a quality failure. If you cannot complete all 10 checks, delay the playback — do not present with incomplete evidence. The two most commonly missed are check 9 (recommendation slide order) and check 10 (Alliance Manager confirmation).

---

## Slide 24 — Repo Structure — Where Everything Lives

**Heading:** The CRA framework repository — your navigation guide

```
CRA Framework Root
│
├── README.md                    ← Start here (external audiences)
├── START-HERE.md                ← Start here (new CRA practitioners)
├── docs/
│   ├── METHODOLOGY.md           ← Framework design principles
│   ├── MICROSOFT-CAF-ALIGNMENT.md
│   ├── AWS-MAP-ALIGNMENT.md
│   ├── GOOGLE-PSO-ALIGNMENT.md
│   └── guides/
│       ├── 00-architect-onboarding-guide.md  ← 30-min onboarding
│       ├── 01-discovery-phase-guide.md        ← Phase 1 delivery guide
│       ├── 02-analysis-phase-guide.md         ← Phase 2 delivery guide
│       ├── 03-evaluation-phase-guide.md       ← Phase 3 delivery guide
│       └── 04-planning-phase-guide.md         ← Phase 4 delivery guide
│
├── Templates/
│   ├── 01-discovery/            ← application-scoping, infrastructure-profiling, dependency-mapping
│   ├── 02-analysis/             ← cloud-readiness-scoring, governance-foundations-alignment
│   ├── 03-evaluation/           ← TCO models (azure/aws/gcp), hyperscaler-decision-matrix, business-case
│   ├── 04-planning/             ← migration-wave-planner, risk-assessment, governance-model, sow
│   └── executive-reporting/     ← cra-assessment-report-v3.docx, cra-executive-summary-v3.pptx
│
├── presentations/
│   ├── executive/               ← leadership and customer overview decks
│   ├── technical/               ← this deck; technical onboarding
│   └── alliance/                ← Microsoft, AWS, GCP partner decks
│
└── Examples/
    ├── aws/                     ← anonymised AWS pricing examples
    ├── azure/                   ← anonymised Azure evaluation examples
    └── media-entertainment/     ← DMG Media UK case study
```

**Speaker notes:**  
Every architect should bookmark START-HERE.md and the 00-architect-onboarding-guide. The Templates folder is the daily working folder during an engagement. The docs/guides folder is the reference during delivery. Use the phase guide for the active phase — it tells you what to do this week, which templates to open, and what the quality standards are.

---

## Slide 25 — Summary and Key Takeaways

**Heading:** What you should be able to do now

**Five capabilities (each with a reference):**

1. **Lead a Phase 1 kickoff** — knowing to submit the CAB request on Day 1, escalate Oracle in Week 1–2, and start Phase 2 at Week 6  
   *Reference: `docs/guides/01-discovery-phase-guide.md`*

2. **Explain the 7-layer TCO model** to a CFO without using internal jargon — and explain why layers d–g matter more than layers a–c  
   *Reference: `Templates/03-evaluation/TCO-TEMPLATES-AUDIT-SPEC.md`*

3. **Run a credible hyperscaler evaluation** with customer-agreed criteria weights and evidence-referenced scores — and present the recommendation after the evidence  
   *Reference: `Templates/03-evaluation/HYPERSCALER-TEMPLATES-AUDIT-SPEC.md`*

4. **Hold Gate 1** when a customer pushes to skip the utilisation data window — using the quantified accuracy argument, not just methodology rules  
   *Reference: `docs/guides/03-evaluation-phase-guide.md`*

5. **Escalate Oracle, OSS, and EoL OS findings** at the right moment — not when they become critical path blockers  
   *Reference: `docs/DMG-MEDIA-UK-LESSONS-LEARNED.md`*

**Closing statement:**  
> "The framework is only as good as the architects who use it with rigour. Every gate exists because someone pushed through it and paid the price on a real engagement. The gates are the framework."

---

## Appendix A — Glossary of CRA-Specific Terms

| Term | Definition |
|---|---|
| L4L | Like-for-Like — migrating exact current VM specification to cloud without right-sizing |
| AHB | Azure Hybrid Benefit — Microsoft programme allowing BYOL for Windows Server and SQL Server in Azure |
| BYOL | Bring Your Own Licence — use an existing on-premises licence in a cloud environment |
| RI | Reserved Instance — 1- or 3-year cloud compute commitment (AWS); similar to Azure Reserved VM Instances |
| CUD | Committed Use Discount (GCP) — GCP equivalent of Reserved Instances |
| AMM | Azure Migration and Modernisation — Microsoft partner funding programme for migration engagements |
| MAP | Migration Acceleration Programme — AWS partner funding programme for migration engagements |
| PSO | Professional Services Organisation — GCP professional services; migration credits available |
| RAMP | Rapid Migration Programme — GCP structured migration acceleration programme |
| EoL | End of Life — operating system or software version no longer receiving standard security updates |
| ESU | Extended Security Updates — paid extension of security patches for EoL Microsoft products |
| FinOps | Cloud Financial Operations — practice of optimising cloud spend through financial management |
| CMDB | Configuration Management Database — record of IT assets; often incomplete or out of date |
| CAF | Microsoft Cloud Adoption Framework — Microsoft's structured cloud adoption methodology |
| WAF | AWS Well-Architected Framework — AWS's framework for evaluating architecture quality |
| GCAF | Google Cloud Adoption Framework — GCP's equivalent adoption methodology |
| RTO | Recovery Time Objective — maximum acceptable time to restore a system after failure |
| RPO | Recovery Point Objective — maximum acceptable data loss in time |
| MRA | Migration Readiness Assessment — AWS MAP's equivalent of CRA Phase 1+2 |
| NUP | Oracle Named User Plus — Oracle licensing model based on number of named users |
| ULA | Oracle Unlimited Licence Agreement — Oracle contract allowing unlimited deployment for a fixed term |

---

*Document Classification: INTERNAL / PARTNER — Rackspace Technology*  
*CRA Framework v2.0 — Rackspace Cloud Solutions Architecture*  
*Build instructions: This document is the slide content script for `CRA-Technical-Overview.pptx`. Build in PowerPoint using the official Rackspace PPTX template. This is a reference deck — not all slides need to be presented in every session. Select the relevant sections based on audience.*
