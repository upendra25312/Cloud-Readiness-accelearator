# CRA AWS Partner Deck — Slide Content Script

**Deck:** `CRA-AWS-Partner-Deck.pptx`  
**Audience:** AWS Partner Development Managers (PDMs), AWS Partner Solutions Architects (PSAs), AWS Account Managers — UK and global  
**Format:** 16 slides, 30-minute co-sell briefing  
**Purpose:** Explain how Rackspace CRA aligns to AWS Migration Acceleration Programme (MAP), how CRA outputs satisfy MAP deal registration requirements, and how CRA-led engagements accelerate AWS migration pipeline  
**Classification:** PARTNER — approved for sharing with AWS partner teams (after legal review of case study content)

> **Build instructions:** Co-branded Rackspace + AWS layout. Apply Rackspace Red `#E31C3D` for Rackspace elements; AWS Orange `#FF9900` for AWS-aligned elements. Place both logos on the title slide. Footer: `Rackspace × AWS — Migration Partner`. Speaker notes mandatory.

---

## Slide 1 — Title Slide

**Title:** Cloud Readiness Accelerator  
**Subtitle:** How Rackspace CRA drives MAP-qualified assessments and structured AWS co-sell  
**Rackspace logo:** Top-left  
**AWS logo:** Top-right (with "AWS Partner Network" designation)  
**Date:** [Date]  
**Presented by:** [Name], Rackspace Cloud Solutions Architecture + Alliance

**Visual:** Rackspace Red left panel + AWS deep black/orange right panel. Both logos visible.

**Speaker notes:**  
This deck is for AWS PDMs, PSAs, and account managers. The goal is for the AWS partner team to understand that a Rackspace CRA engagement is a pre-qualified MAP opportunity — and that the Rackspace Alliance Manager process ensures ACE (AWS Customer Engagements) deal registration is active from Phase 1 Day 1.

---

## Slide 2 — The Co-Sell Opportunity

**Heading:** CRA-qualified assessments feed directly into MAP migration pipeline

**Three-column layout:**

**Column 1 — What's Missing Without CRA:**  
Most mid-market customers who approach AWS about migration lack a formal application inventory, a multi-cloud TCO model, and a structured migration plan. The result: long discovery cycles, missed MAP registration windows, and delayed Azure/GCP alternatives getting in first.

**Column 2 — What CRA Provides:**  
A 16-week structured assessment that produces exactly the documentation MAP requires: application inventory, readiness assessment, AWS TCO with Savings Plans modelled, and a sequenced migration wave plan. Produced by an independent assessor — not by AWS, ensuring the recommendation is credible.

**Column 3 — The MAP Activation:**  
Every CRA engagement with an AWS recommendation is a MAP-eligible opportunity. Rackspace pre-registers in AWS ACE at Phase 1 kickoff. By Phase 4, the customer has a board-ready business case, a migration plan, and a signed Part 2 Entry Point — ready to execute.

**Bottom callout:**  
> "CRA Assessment phase outputs are the MAP Assess stage deliverables. The assessment work is done — MAP can begin immediately at Phase 4 close."

**Speaker notes:**  
Position CRA as the front-end of MAP, not an alternative to it. MAP has three stages — Assess, Mobilize, Migrate & Modernize. CRA delivers the Assess stage at a level of depth and rigour that far exceeds what most customers can produce internally. By the time Phase 4 is complete, the customer is ready to begin the MAP Mobilize stage immediately.

---

## Slide 3 — CRA-to-MAP Phase Alignment

**Heading:** CRA phases map directly to AWS MAP phases

**Full alignment table:**

| MAP Phase | MAP Purpose | CRA Phase | CRA Deliverables |
|---|---|---|---|
| **Assess** | Migration Readiness Assessment (MRA); current-state baseline; business case; migration strategy | Phase 1 Discovery + Phase 2 Analysis | Application inventory; infrastructure profiling; 5-dimension readiness scores; dependency map; AWS TCO baseline |
| **Mobilize** | Detailed migration plan, wave sequencing, landing zone design, pilot migration | Phase 3 Evaluation + Phase 4 Planning | AWS TCO model; hyperscaler recommendation; migration wave plan; Part 2 Entry Point; governance model; risk register |
| **Migrate & Modernize** | Full migration execution; Well-Architected Reviews; optimization | Post-CRA (Part 2) | CRA provides baseline and wave plan; migration execution is Part 2 engagement |

**Visual diagram:**
```
MAP:     [Assess]                [Mobilize]          [Migrate & Modernize]
              │                       │                        │
CRA:   [Phase 1+2]            [Phase 3+4]               [Part 2 ops]
        Discovery &             Evaluation &              Migration
        Analysis                Planning                  execution
        Inventory &             TCO/AWS                   Wave-by-wave
        Readiness               Architecture              delivery
        scoring                 Wave plan
```

**Speaker notes:**  
CRA Phases 1 and 2 are equivalent to the MAP Assess stage. CRA Phases 3 and 4 cover the MAP Mobilize requirements. By the time a customer completes CRA, they have satisfied both MAP Assess and MAP Mobilize requirements — and can enter the Migrate & Modernize stage immediately via the Part 2 Entry Point.

---

## Slide 4 — MAP Funding Eligibility — What CRA Produces

**Heading:** CRA produces every artefact required for MAP deal registration

**MAP requirements vs. CRA outputs:**

| MAP Requirement | Required Evidence | CRA Output | CRA Template |
|---|---|---|---|
| Migration Readiness Assessment (MRA) | Formal assessment covering people, process, technology, and business | CRA Phase 1+2: application inventory, readiness scores, governance assessment | `application-scoping-profiling.xlsx` + `cloud-readiness-scoring-v2.xlsx` |
| Current-state inventory | Server and application inventory with specifications | Infrastructure profiling + Application inventory | `infrastructure-profiling.xlsx` |
| Business case with TCO analysis | 3–5 year TCO comparison including AWS pricing | 7-layer TCO model with AWS On-Demand + RI + Savings Plans | `business-case-tco-roi.xlsx` + `aws-evaluation.xlsx` |
| Migration wave plan | Sequenced migration roadmap | Wave planner with Tier-based sequencing | `migration-wave-planner.xlsx` |
| AWS as primary or co-primary recommendation | Assessment outcome recommends AWS | Hyperscaler decision matrix — AWS scored and evidenced | `hyperscaler-decision-matrix.xlsx` |
| APN Partner with Migration Competency | Partner-led engagement | Rackspace AWS Partner status ✅ | — |
| ACE deal registration | Registered in AWS Customer Engagements portal | Rackspace Alliance Manager registers at Phase 1 Day 1 | AWS Partner Central / ACE |

**Speaker notes:**  
CRA was not designed specifically for MAP, but the overlap is near-complete. The reason is that both MAP and CRA are based on the same underlying principle: a formal, evidence-based, people/process/technology assessment is required before a credible migration recommendation can be made. The CRA templates produce MAP-compatible evidence.

---

## Slide 5 — AWS TCO Modelling in CRA

**Heading:** How CRA models AWS pricing — all three options, per region

**Template:** `Templates/03-evaluation/aws-evaluation.xlsx` + `business-case-tco-roi.xlsx`

**Three AWS pricing models CRA models:**

| Pricing Model | AWS Name | CRA Tab | Notes |
|---|---|---|---|
| **On-Demand** | EC2 On-Demand | `AWS-OnDemand` | Like-for-Like baseline — worst case cost |
| **Reserved Instances (3yr)** | EC2 Reserved Instance (3yr, All Upfront) | `AWS-RI-3yr` | Standard commitment model; typically 40–60% saving vs On-Demand |
| **Savings Plans (3yr)** | Compute Savings Plans (3yr, All Upfront) | `AWS-SavingsPlans` | More flexible than RI; applies to EC2, Fargate, Lambda |

**Key instance families for general workloads:**

| Family | Use Case | Generation |
|---|---|---|
| m6i / m7i | General purpose — balanced CPU/RAM | Current generation (recommended) |
| r6i / r7i | Memory-optimised — databases, SAP | Current generation |
| c6i / c7i | Compute-optimised — CPU-intensive workloads | Current generation |
| i3en / i4i | Storage-optimised — high IOPS databases | Current generation |

**Cross-validation:** Use AWS Migration Evaluator to generate an initial business case from RVTools or agent data. Compare against the manually-built aws-evaluation.xlsx to confirm alignment.

**Speaker notes:**  
Always model all three AWS pricing options — On-Demand, 3yr RI, and Savings Plans. Customers and their CFOs often ask "what if we don't want to commit to 3 years?" — Savings Plans give more flexibility than RI. Present all three in the TCO comparison. The board-level number should be the 3yr Savings Plans or RI figure — that is the committed cost the customer is actually deciding on.

---

## Slide 6 — AWS Migration Evaluator Integration

**Heading:** Integrating AWS Migration Evaluator with CRA Phase 1 data

**What AWS Migration Evaluator does:**  
Migration Evaluator is a free AWS tool that ingests current-state inventory data (from agentless collector or direct import) and produces an initial business case for AWS migration. It provides a baseline AWS TCO estimate directly from discovered VM data.

**CRA Integration workflow:**

| Step | Action | Timing |
|---|---|---|
| 1 | Deploy AWS ADS (Application Discovery Service) agentless collector or agent | Phase 1 Week 1 |
| 2 | Collect 14+ days of utilisation data (same data window as other discovery tools) | Phase 1 Weeks 1–7 |
| 3 | Export collected data from AWS ADS | Phase 1 Week 7 |
| 4 | Upload to Migration Evaluator → generate initial business case | Phase 3 Week 11 |
| 5 | Cross-validate Migration Evaluator output against manually-built aws-evaluation.xlsx | Phase 3 Week 12 |
| 6 | Resolve discrepancies; use manually-built model as the final source of truth | Phase 3 Week 13 |

**Why cross-validate:**  
Migration Evaluator applies standard AWS pricing and default right-sizing assumptions. The CRA manually-built model applies customer-specific assumptions: Oracle workloads, Savings Plan commitment level, specific instance families for specialist workloads. The manual model is more accurate for complex estates.

**Speaker notes:**  
AWS PSAs can be very helpful here — if they offer to run Migration Evaluator on the customer's data during Phase 1, that is a time-saving for the Rackspace team. Accept the help, but always cross-validate the Migration Evaluator output against the manual model. Evaluator tends to underestimate cost for Oracle workloads and overestimate Savings Plan savings for mixed estates.

---

## Slide 7 — ACE Deal Registration Timeline

**Heading:** When to register in AWS ACE — and why it cannot wait

**Registration timeline:**

```
Phase 1    Phase 1    Phase 2    Phase 3    Phase 3    Phase 4
Day 1      Week 2     Week 10    Week 11    Week 14    Week 18
  │           │          │          │           │          │
  ▼           ▼          ▼          ▼           ▼          ▼
Rackspace   AWS PSA    Readiness  TCO         Rec        Part 2
Alliance    confirms   scoring    complete    presented  SOW ready
registers   registration complete
in ACE
```

**What happens at ACE registration:**
- Rackspace Alliance Manager logs into AWS Partner Central
- Creates an "Opportunity" record for the customer account
- Tags as "Migration" type; selects "Assess" phase
- Links to AWS account manager / partner manager
- Tags estimated AWS annual run rate (from scoping estimate)
- Selects MAP as the applicable programme

**AWS PDM action required:**
- Accept and acknowledge the co-sell opportunity in ACE
- Connect with the Rackspace Alliance Manager on the account
- Confirm MAP programme applicability for this customer tier
- Introduce AWS PSA if technical depth is required in Phase 3

**Hard rule:**  
ACE registration must be active before Phase 3 begins. MAP assessment funding eligibility requires registration before the assessment evidence is compiled — not after.

**Speaker notes:**  
Unlike some programmes, MAP has time-sensitive registration requirements. An opportunity registered after the TCO model is complete may not qualify for MAP assessment funding — it may only qualify for migration funding. Registering on Day 1 of Phase 1 maximises the funding opportunity for the customer. The AWS PDM should acknowledge the ACE registration within 5 business days.

---

## Slide 8 — AWS Well-Architected Framework Alignment

**Heading:** CRA readiness scoring and Phase 4 governance model align to AWS WAF pillars

**AWS WAF (Well-Architected Framework) pillars vs. CRA outputs:**

| WAF Pillar | CRA Phase 2/4 Output | Notes |
|---|---|---|
| **Operational Excellence** | Governance maturity assessment — Change Management, Monitoring & Observability domains | CRA baseline identifies gaps before landing zone build |
| **Security** | Governance maturity assessment — Security & Compliance domain; IAM domain | CRA produces a gap register for each domain — direct input to AWS Security Hub design |
| **Reliability** | Phase 2 Cloud Readiness Scores — Business Criticality dimension; RTO/RPO requirements | Applications with Tier-1 criticality flagged for high-availability AWS architecture |
| **Performance Efficiency** | Phase 1 utilisation data + right-sizing recommendations | P95 CPU/RAM used for right-sizing — prevents over-provisioning and under-performance |
| **Cost Optimisation** | Phase 3 7-layer TCO model; Savings Plans modelling | Layer (g) partner credits = MAP funding applied to net cost |
| **Sustainability** | Phase 3 right-sizing (fewer, optimised instances = lower energy) | Optional — add to Phase 4 governance model for ESG-conscious customers |

**Key message:**  
The CRA governance maturity baseline and the Phase 4 governance model provide the input data for an AWS WAF review. AWS PSAs who conduct WAF reviews post-migration can use the CRA governance outputs as a starting point — reducing WAF review time by 30–40%.

**Speaker notes:**  
This is a valuable message for AWS PSAs who do WAF reviews. They often start from scratch because there is no governance baseline. CRA produces the baseline that makes the WAF review faster and more targeted. It also positions Rackspace as the partner who prepared the customer for WAF review — reinforcing the co-sell relationship.

---

## Slide 9 — Reference Engagement — AWS Pricing Modelled at Scale

**Heading:** Real AWS TCO models from a real assessment

**Reference context:**  
In the CRA framework's reference engagement (UK digital media group — 4,200+ VMs, 280 applications), AWS was one of three hyperscalers evaluated with full TCO modelling.

**AWS TCO produced:**
- m6i (general purpose) right-sized from P95 utilisation data: all general workloads
- r6i (memory-optimised): Oracle DB workloads and in-memory applications
- 3 AWS regions evaluated: eu-west-2 (London), eu-west-1 (Ireland), eu-central-1 (Frankfurt)
- Both On-Demand and 3yr Reserved Instance pricing modelled per region
- Savings Plans modelled for compute-flexible workloads

**What the AWS TCO showed:**
- AWS London (eu-west-2) 3yr RI: competitive with Azure UK South on pure compute
- Oracle workloads on AWS: more complex licence path than Azure (AVS not available; BYOL costs higher)
- No AWS equivalent of Azure ESU for EoL Windows Server — direct cost disadvantage for EoL-heavy estates
- AWS MAP funding applied in Layer (g): competitive net cost when MAP credits included

**What the TCO did not show:**  
The recommendation outcome is not shared externally. CRA is independent — results vary by customer estate.

**Speaker notes:**  
Avoid sharing the specific recommendation outcome in this deck unless the customer case study is fully cleared for external sharing. The key message for AWS PDMs is that CRA produces a genuinely independent, multi-region, multi-pricing-model TCO for AWS — not a summary or a range. The full AWS TCO model is as detailed as the Azure model. There is no structural bias in the CRA methodology.

---

## Slide 10 — Linux and Open Source Stack on AWS

**Heading:** CRA identifies open-source workload migration paths on AWS

**Why this matters:**  
CRA Phase 2 flags OSS Licence Risk for workloads using Redis, Elasticsearch, HashiCorp Vault, and MongoDB. These licence changes (SSPL, BSL) primarily affect cloud deployments. AWS offers managed alternatives that resolve licence risk without re-architecting:

| OSS Product | Licence Risk | AWS Managed Alternative | Migration Complexity |
|---|---|---|---|
| Redis OSS (post v7.4) | SSPL — commercial use restrictions | Amazon ElastiCache (Valkey or Redis-compatible) | Low — configuration changes only |
| Elasticsearch (post 7.10) | SSPL | Amazon OpenSearch Service (Apache 2.0 fork) | Low-medium — API compatible |
| HashiCorp Vault / Terraform | BSL — enterprise use restrictions | AWS Secrets Manager + Parameter Store | Medium — workflow changes |
| MongoDB | SSPL | Amazon DocumentDB (MongoDB-compatible) | Medium — driver changes; test compatibility |

**CRA Phase 3 action:**  
OSS-flagged workloads in Phase 1 → costed with managed service replacement in Phase 3 TCO (aws-evaluation.xlsx `OSS-Migration` tab). This ensures the TCO reflects the real cost of migration — not just the compute cost.

**Speaker notes:**  
For AWS, the managed OSS alternatives are often cheaper and simpler than on the other hyperscalers. ElastiCache and OpenSearch have been available for longer and are more mature on AWS than equivalent Azure services. This can be a legitimate AWS advantage for Redis and Elasticsearch-heavy estates. Make sure the CRA architect knows to model the managed service cost in the AWS TCO — not just the EC2 instance that would replace the on-prem server.

---

## Slide 11 — Co-Sell Value Proposition

**Heading:** Why AWS should prioritise CRA-qualified opportunities

**For AWS field teams, a Rackspace CRA engagement means:**

| Benefit | Detail |
|---|---|
| Pre-qualified AWS opportunity | CRA Phase 3 produces an evidenced AWS recommendation — not a sales claim |
| MAP-ready documentation | All MAP required artefacts already exist; no post-assessment rework |
| ACE registration from Day 1 | Rackspace Alliance Manager registers in ACE at Phase 1 kickoff |
| Migration Evaluator data available | CRA Phase 1 uses AWS ADS — Evaluator can be run as a by-product |
| Clear AWS consumption projection | 3-year TCO model gives per-region EC2 commitment baseline for RI/SP discussion |
| Reduced AWS PSA involvement | CRA absorbs the discovery and assessment workload; PSA can focus on architecture |

**For the AWS PDM's metrics:**

| AWS Metric | CRA Contribution |
|---|---|
| Migration pipeline | CRA engagements with AWS recommendation = confirmed migration pipeline |
| MAP registrations | Every AWS-recommended CRA = one MAP ACE registration |
| Co-sell pipeline | CRA engagements are logged co-sell opportunities from Day 1 |
| AWS consumption commitments | CRA TCO provides consumption projection for RI/SP commitment discussions |

**Speaker notes:**  
The key message is the same as for any co-sell programme: every CRA engagement is a pre-qualified opportunity. The AWS PDM who has an active Rackspace Alliance Manager relationship gets advance notice of every CRA engagement, every Phase 3 recommendation, and every MAP registration. This is better pipeline visibility than the PDM gets from most other routes to market.

---

## Slide 12 — What AWS Needs to Do

**Heading:** AWS actions that maximise CRA co-sell success

| Action | When | Why |
|---|---|---|
| ☐ Refer customers needing formal assessment to Rackspace | When a customer's own assessment capability is insufficient | CRA replaces months of customer DIY discovery |
| ☐ Provide warm introduction to customer | Before Rackspace scoping call | Establishes Rackspace credibility as independent assessor |
| ☐ Accept ACE co-sell opportunity acknowledgement | Phase 1 Week 1–2 | Required for MAP programme eligibility tracking |
| ☐ Confirm MAP programme applicability and tier | Phase 1 Week 1–2 | Ensures MAP funding eligibility is correctly scoped |
| ☐ Provide AWS PSA support for Phase 3 architecture validation (optional) | Phase 3 (on request) | AWS PSA can validate architecture recommendations |
| ☐ Attend Phase 3 playback (optional but recommended) | Phase 3 Week 14 | Demonstrates co-sell alignment; strengthens AWS recommendation credibility |
| ☐ Support MAP funding application | Phase 3 Week 14–16 | Submits MAP funding request once AWS recommendation is confirmed |

**Speaker notes:**  
The minimum required actions are the ACE acknowledgement (Phase 1 Week 2) and MAP programme guidance (Phase 1 Week 2). Everything else is additive but optional. The ACE acknowledgement is critical — without it, the MAP registration is incomplete and funding eligibility is at risk.

---

## Slide 13 — The Independent Recommendation — Why It Matters for AWS

**Heading:** When CRA recommends AWS, the customer's board believes it

**The credibility problem AWS faces:**  
Customers are increasingly aware that hyperscaler-provided assessments are not independent. A free AWS assessment that recommends AWS is not surprising. A formal, 16-week, three-way evaluation conducted by an independent Rackspace-led team that recommends AWS is a different kind of evidence.

**What "independent recommendation" means in practice:**
- CRA evaluates all three clouds with equal rigour — Azure and GCP get the same depth of analysis
- Criteria weights are agreed by the customer before scoring — neither Rackspace nor AWS sets them
- The TCO model shows all three clouds — the customer can see why AWS won
- All three hyperscaler SEs are invited to the Phase 3 playback
- The AWS recommendation is evidenced, auditable, and defensible

**For AWS's pipeline:**  
A CRA-delivered AWS recommendation is the strongest possible evidence for a customer's internal investment committee, their Microsoft incumbent account team, or their Azure-preferring CTO. Rackspace's independence is the proof that the recommendation is not sponsored.

**Speaker notes:**  
This is the "why CRA and not just AWS free assessment" message for AWS PDMs. The AWS Cloud Adoption Readiness Tool (CART) and AWS Migration Evaluator are useful but not independent. When a customer's board is choosing between Azure and AWS, a Rackspace-delivered independent recommendation carries far more weight than anything AWS produces internally. That is the value of the co-sell relationship.

---

## Slide 14 — Oracle Workloads on AWS

**Heading:** Oracle in the CRA assessment — the AWS path

**Oracle on AWS options:**

| Oracle Workload | AWS Migration Path | CRA Action |
|---|---|---|
| Oracle Database Standard / EE (Linux) | RDS for Oracle (BYOL) or EC2 BYOL | Oracle Practice Lead review at Phase 2; model BYOL cost in TCO |
| Oracle RAC | EC2 BYOL on dedicated hosts (no managed service equivalent) | Oracle Practice Lead required; complex architecture; separate wave |
| Oracle E-Business Suite | EC2 IaaS lift-and-shift; Oracle BYOL | Oracle Practice flag at Phase 1; standard AWS migration path |
| Oracle Database EE (Exadata) | Oracle Exadata Cloud@Customer or OCI Exadata | May require OCI path — multi-cloud exception |
| Oracle Forms / Reports | No cloud-native equivalent — requires rearchitect | Retain or full rearchitect; separate Phase 5 workstream |

**Key AWS-specific Oracle note:**  
AWS RDS for Oracle supports BYOL for Standard 2 and Enterprise Edition. However, Oracle RAC is not supported on RDS — it requires EC2 BYOL on dedicated hosts, which is architecturally complex and potentially expensive. CRA flags Oracle RAC in Phase 1 and escalates to the Oracle Practice Lead immediately.

**AWS has no equivalent of Azure VMware Solution (AVS)** for Oracle RAC. This means Oracle RAC on AWS requires a dedicated host solution — cost and complexity must be modelled explicitly in the TCO.

**Speaker notes:**  
Oracle on AWS is significantly more complex than Oracle on Azure (where AVS provides a relatively clean migration path for RAC). When CRA encounters Oracle RAC on a customer who prefers AWS, the TCO conversation becomes important — dedicated hosts for Oracle RAC on AWS add material cost. The Oracle Practice Lead must be involved from Phase 1. For large Oracle estates, Oracle Cloud Infrastructure (OCI) may appear as a multi-cloud exception in the Phase 3 evaluation.

---

## Slide 15 — Framework Reference Materials for AWS

**Heading:** What Rackspace provides for AWS technical review

| Document | Content | Location |
|---|---|---|
| `docs/AWS-MAP-ALIGNMENT.md` | Full MAP phase-to-CRA mapping; MAP funding eligibility; ACE registration process | GitHub repo |
| `docs/METHODOLOGY.md` | Complete CRA methodology; quality gates; data collection standards | GitHub repo |
| `Templates/03-evaluation/TCO-TEMPLATES-AUDIT-SPEC.md` | 7-layer TCO model; AWS-specific layers (RI, Savings Plans, MAP credits) | GitHub repo |
| `Templates/03-evaluation/HYPERSCALER-TEMPLATES-AUDIT-SPEC.md` | Evaluation methodology; equal-treatment standards | GitHub repo |
| `Examples/aws/` | Anonymised AWS pricing examples (MPA pricing for 3 regions) | GitHub repo |

**GitHub repo:** [To be updated to rxt-mpc/ps-ind-cloud-readiness-accelerator upon migration]

**Request for AWS PSA review:**  
> "We would welcome a 1-hour AWS PSA technical review of the CRA methodology to confirm MAP alignment and ACE registration standards. Contact [Alliance Manager email] to schedule."

---

## Slide 16 — Next Steps

**Heading:** Three paths to a Rackspace CRA / AWS MAP co-sell activation

**Path 1 — MAP Pipeline Identification:**  
- AWS PDM identifies accounts approaching migration readiness
- Refers to Rackspace Pre-Sales for CRA scoping call
- Contact: [Rackspace Pre-Sales contact]

**Path 2 — CART / MRA Upgrade:**  
- Customer has completed AWS Cloud Adoption Readiness Tool (CART) or internal MRA
- Score suggests a formal assessment is needed
- Rackspace CRA provides the MAP Assess deliverables to a higher rigour standard
- Contact: [Rackspace Pre-Sales contact]

**Path 3 — Joint Pipeline Review:**  
- Monthly joint pipeline review: Rackspace Alliance Manager + AWS PDM
- Identify accounts where CRA would accelerate MAP registration
- Contact: [Rackspace Alliance Manager]

**CTA:**  
> "Schedule a 30-minute session between Rackspace Alliance Architecture and AWS PSA to confirm CRA methodology against MAP Assess requirements. One session. Unlocks the entire co-sell pipeline."

---

*Document Classification: PARTNER — Rackspace × AWS*  
*CRA Framework v2.0 — Rackspace Cloud Solutions Architecture*  
*Build instructions: Build in PowerPoint with co-branded layout. Rackspace Red (#E31C3D) + AWS Orange (#FF9900). Both logos on title slide. Do not share internal commercial deal economics with AWS partner contacts.*
