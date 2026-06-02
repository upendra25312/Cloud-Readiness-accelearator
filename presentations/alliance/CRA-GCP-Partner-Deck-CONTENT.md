# CRA GCP Partner Deck — Slide Content Script

**Deck:** `CRA-GCP-Partner-Deck.pptx`  
**Audience:** Google Cloud Partner Development Managers (PDMs), Google Cloud Partner Sales Engineers (PSEs), Google Cloud Customer Engineers (CEs) — UK and global  
**Format:** 16 slides, 30-minute co-sell briefing  
**Purpose:** Explain how Rackspace CRA aligns to the Google Cloud Adoption Framework (GCAF), how CRA outputs support GCP PSO (Professional Services Organisation) engagement qualification and migration credit eligibility, and how CRA-led engagements accelerate GCP migration pipeline  
**Classification:** PARTNER — approved for sharing with Google Cloud partner teams (after legal review of case study content)

> **Build instructions:** Co-branded Rackspace + Google Cloud layout. Apply Rackspace Red `#E31C3D` for Rackspace elements; Google Cloud Blue `#4285F4` for GCP-aligned elements. Place both logos on the title slide. Footer: `Rackspace × Google Cloud — Migration Partner`. Speaker notes mandatory.

---

## Slide 1 — Title Slide

**Title:** Cloud Readiness Accelerator  
**Subtitle:** How Rackspace CRA aligns to Google Cloud's migration methodology and PSO programme requirements  
**Rackspace logo:** Top-left  
**Google Cloud logo:** Top-right (with "Google Cloud Partner" designation)  
**Date:** [Date]  
**Presented by:** [Name], Rackspace Cloud Solutions Architecture + Alliance

**Visual:** Rackspace Red left panel + Google Cloud multi-colour accent on right. Both logos visible.

**Speaker notes:**  
This deck is for Google Cloud PDMs, PSEs, and CEs. The goal is for the Google partner team to understand that a Rackspace CRA engagement produces the assessment deliverables that GCP PSO and RAMP (Rapid Migration Programme) require — and that the Rackspace Alliance Manager process ensures partner opportunity registration is active from Phase 1.

---

## Slide 2 — The Co-Sell Opportunity

**Heading:** CRA-qualified assessments are the front-end of GCP PSO migration engagements

**Three-column layout:**

**Column 1 — The Gap:**  
Mid-market customers interested in Google Cloud often lack the structured assessment capability to produce a board-ready business case, a multi-cloud comparison, and a migration plan. They complete Google Migration Center assessments but do not know how to translate the output into an investment decision.

**Column 2 — What CRA Provides:**  
A 16-week structured assessment that produces the GCAF Assess and Plan stage deliverables to a rigour level that supports GCP PSO engagement qualification and migration credit eligibility. Produced by an independent Rackspace team — ensuring the GCP recommendation is credible and defensible.

**Column 3 — The GCP Activation:**  
Every CRA engagement with a GCP recommendation generates a PSO-qualified opportunity. Rackspace pre-registers in Google Partner Advantage at Phase 1 kickoff. By Phase 4, the customer has a board-ready GCP business case, a migration wave plan, and a signed Part 2 Entry Point.

**Bottom callout:**  
> "CRA delivers the GCAF Assess and Plan stages. GCP PSO and RAMP can begin at Phase 4 close — no additional discovery required."

**Speaker notes:**  
Position CRA as the GCAF Assess + Plan stage executor. Google Cloud's migration framework (GCAF) has four stages: Assess, Plan, Deploy, Optimise. CRA covers the first two. By the time Phase 4 is complete, the customer is ready to begin Deploy — the GCP PSO engagement and RAMP programme can start immediately.

---

## Slide 3 — CRA-to-GCAF Alignment Map

**Heading:** CRA phases map directly to Google Cloud Adoption Framework stages

**Full alignment table:**

| GCAF Stage | GCAF Purpose | CRA Phase | CRA Deliverables |
|---|---|---|---|
| **Assess** | Evaluate current workloads; identify cloud fit; establish baseline TCO | Phase 1 Discovery + Phase 2 Analysis | Application inventory; infrastructure profiling; 5-dimension readiness scores; dependency map; GCP cloud fit assessment |
| **Plan** | Design target architecture; build migration business case; define wave plan | Phase 3 Evaluation + Phase 4 Planning | GCP TCO model; hyperscaler recommendation; migration wave plan; landing zone design guidance; governance model |
| **Deploy** | Landing zone build; foundation infrastructure; initial wave migration | Post-CRA (Part 2) | CRA provides deployment specifications; landing zone build is separate Part 2 workstream |
| **Optimise** | Cost optimisation; SRE practices; FinOps; Architecture Framework review | Post-CRA (ongoing) | CRA TCO model provides cost optimisation baseline; ongoing is managed services |

**Visual diagram:**
```
GCAF:    [Assess]                [Plan]             [Deploy]     [Optimise]
              │                      │                   │              │
CRA:   [Phase 1+2]           [Phase 3+4]          [Part 2 ops]  [Ongoing]
        Discovery &            Evaluation &          Landing       FinOps +
        Analysis               Planning              zone build    SRE +
        Inventory &            GCP TCO               Migration     WAR
        Readiness              Architecture           execution
        scoring                Wave plan
```

**Speaker notes:**  
CRA Phases 1 and 2 are the GCAF Assess stage executed at full rigour. Phases 3 and 4 are the GCAF Plan stage. Google Cloud PDMs and PSEs can confidently position CRA as the front-end of a GCP engagement that ends with the customer entering Deploy — and deploying PSO and RAMP resources immediately at Phase 4 close.

---

## Slide 4 — GCP Migration Credits and PSO Funding

**Heading:** CRA produces the evidence required for GCP migration credit eligibility

**GCP requirements vs. CRA outputs:**

| GCP Requirement | Required Evidence | CRA Output | CRA Template |
|---|---|---|---|
| Formal migration assessment | Documented, repeatable assessment methodology | CRA METHODOLOGY.md + phase guides | `docs/METHODOLOGY.md` |
| Current-state infrastructure inventory | Server and application inventory with specifications | Infrastructure profiling + Application inventory | `infrastructure-profiling.xlsx` |
| Cloud readiness assessment | Multi-dimensional workload cloud fit analysis | 5-dimension readiness scores per application | `cloud-readiness-scoring-v2.xlsx` |
| GCP TCO analysis | Cost comparison with GCP as a modelled option | 7-layer TCO: GCP On-Demand + 3yr CUDs + PSO credits | `business-case-tco-roi.xlsx` + `gcp-evaluation.xlsx` |
| Migration wave plan | Sequenced application migration roadmap | Wave planner with Tier-based sequencing | `migration-wave-planner.xlsx` |
| Qualified Google Cloud Partner | Partner-led engagement | Rackspace Google Cloud Partner status ✅ | — |
| Opportunity registration | Registered in Google Partner Advantage portal | Rackspace Alliance Manager registers at Phase 1 Day 1 | Google Partner Advantage |

**Speaker notes:**  
The overlap between CRA outputs and GCP migration credit requirements is near-complete. The key difference from AWS MAP and Azure AMM is that GCP programme eligibility and funding amounts are more account-specific and vary more year to year. The Rackspace Alliance Manager should confirm current GCP programme terms with the Google Cloud PDM at engagement start — not assume the programme structure from prior engagements.

---

## Slide 5 — GCP Migration Center Integration

**Heading:** CRA Phase 1 uses Google Migration Center — natively

**What Google Migration Center does:**  
Migration Center is Google Cloud's free discovery and assessment tool. It ingests inventory data from agent-based collection, RVTools export, or direct API integration — and produces GCP-specific right-sizing recommendations, TCO estimates, and fit analysis.

**CRA Integration workflow:**

| Step | Action | Timing |
|---|---|---|
| 1 | Deploy GCP Migration Center collector or VM Manager agent | Phase 1 Week 1 |
| 2 | Collect 14+ days of utilisation data (same window as other tools) | Phase 1 Weeks 1–7 |
| 3 | Export collected data; import to Migration Center dashboard | Phase 1 Week 7 |
| 4 | Run Migration Center GCP right-sizing analysis | Phase 3 Week 11 |
| 5 | Export Migration Center GCP pricing estimate | Phase 3 Week 11 |
| 6 | Cross-validate against manually-built gcp-evaluation.xlsx | Phase 3 Week 12 |
| 7 | Resolve discrepancies; manually-built model is source of truth for complex workloads | Phase 3 Week 13 |

**Alternatively — RVTools import:**  
Migration Center accepts direct RVTools VMware export. If Azure Migrate is the primary discovery tool, use the RVTools export to populate Migration Center in parallel — no additional agent deployment required.

**Speaker notes:**  
Google Migration Center is the most straightforward discovery tool to integrate with CRA because it accepts RVTools imports directly. If the customer's primary discovery tool is Azure Migrate, the same RVTools export can populate Migration Center without running a separate GCP collector. This reduces the discovery tooling overhead significantly and still produces a GCP-native right-sizing output.

---

## Slide 6 — GCP CUD and On-Demand Pricing in the CRA TCO Model

**Heading:** How CRA models GCP pricing — two options, per region

**Template:** `Templates/03-evaluation/gcp-evaluation.xlsx` + `business-case-tco-roi.xlsx`

**Two GCP pricing models CRA models:**

| Pricing Model | GCP Name | CRA Tab | Notes |
|---|---|---|---|
| **On-Demand** | Pay-as-you-go | `GCP-OnDemand` | Like-for-Like baseline |
| **Committed Use Discounts (3yr)** | 3-year CUD | `GCP-CUD-3yr` | Typically 37–55% saving vs On-Demand; resource-based (CPU/RAM) or spend-based |

**Key GCP instance families:**

| Family | Use Case | Generation |
|---|---|---|
| n2-standard | General purpose | Current generation (recommended) |
| n2-highmem | Memory-optimised | Current generation |
| n2-highcpu | Compute-optimised | Current generation |
| c3-standard | Latest generation general purpose | Latest generation |
| m3-ultramem / m3-megamem | Memory-intensive (SAP HANA, Oracle) | High-memory |

**CUD vs. AWS RI vs. Azure Reserved:**  
GCP CUDs are resource-based commitments (commit to a number of CPU/RAM resources for a region, not a specific instance type). This gives more flexibility than AWS Reserved Instances (instance-specific) but less flexibility than AWS Savings Plans. Model accordingly.

**Speaker notes:**  
GCP CUDs apply to specific regions and resource types — they are not as flexible as AWS Savings Plans. When modelling CUDs, you need to know which region the customer will use (typically europe-west2 for UK) and what the CPU/RAM mix will be. The manually-built gcp-evaluation.xlsx should use actual P95 right-sized CPU/RAM from the infrastructure profiling data — not rounded estimates. Migration Center will produce a CUD estimate, but cross-validate against the manual model.

---

## Slide 7 — Partner Opportunity Registration Timeline

**Heading:** Registering in Google Partner Advantage — when and how

**Registration timeline:**

```
Phase 1    Phase 1    Phase 2    Phase 3    Phase 3    Phase 4
Day 1      Week 2     Week 10    Week 11    Week 14    Week 18
  │           │          │          │           │          │
  ▼           ▼          ▼          ▼           ▼          ▼
Rackspace   GCP PDM    Readiness  TCO         Rec        Part 2
Alliance    confirms   scoring    complete    presented  SOW ready
registers   opportunity complete
in Partner  in Partner
Advantage   Advantage
```

**Registration process in Google Partner Advantage:**
- Rackspace Alliance Manager logs into Google Partner Advantage portal
- Creates a "Deal Registration" or "Opportunity" for the customer account
- Tags as "Migration" type; selects assessment phase
- Links to Google Cloud account team
- Enters estimated annual GCP consumption (from scoping estimate)
- Selects applicable programme (PSO credits, RAMP)

**GCP PDM action required:**
- Acknowledge and accept the partner opportunity registration
- Connect with the Rackspace Alliance Manager on the account
- Confirm PSO credit or RAMP programme eligibility for this customer
- Introduce Google Cloud PSE if architecture depth is needed in Phase 3

**Speaker notes:**  
Google Partner Advantage registration requirements and funding programme structures change more frequently than AWS MAP or Azure AMM. The Rackspace Alliance Manager should always confirm current programme terms with the Google Cloud PDM at Phase 1 kickoff — not assume the structure from a prior engagement. GCP programme terms are also more geography-specific than AWS or Azure programmes.

---

## Slide 8 — Google Cloud Architecture Framework Alignment

**Heading:** CRA governance assessment baseline aligns to GCAF Architecture Framework pillars

**Google Cloud Architecture Framework pillars vs. CRA outputs:**

| GCAF Pillar | CRA Phase 2/4 Output | Impact on GCP Deployment |
|---|---|---|
| **System Design** | Cloud Readiness Scores — Technical Complexity dimension; dependency mapping | Identifies applications requiring rearchitecting for GCP; dependency clusters that must colocate |
| **Operational Excellence** | Governance maturity assessment — Change Management domain | Gap register for GCP Cloud Operations Suite readiness; SRE practice maturity |
| **Security, Privacy, Compliance** | Governance maturity — Security & Compliance domain; data sensitivity scoring | GCP Security Command Center baseline; BeyondCorp / Zero Trust readiness |
| **Reliability** | Cloud Readiness Scores — Business Criticality dimension; RTO/RPO | Applications requiring multi-region or zonal redundancy in GCP |
| **Cost Optimisation** | Phase 3 7-layer TCO model; CUD modelling | Layer (g) GCP migration credits applied to net cost |
| **Performance** | Phase 1 P95 utilisation data; right-sizing recommendations | GCP instance family selection based on actual utilisation |

**Speaker notes:**  
Google Cloud PSEs who conduct Architecture Framework reviews post-migration can use the CRA governance outputs as a baseline. The CRA Phase 2 governance assessment answers the same questions that the GCAF Architecture Framework review would ask at the start of a PSO engagement. This reduces the PSO pre-engagement discovery time and allows the PSE to go deeper on GCP-specific design decisions.

---

## Slide 9 — RAMP Programme Alignment

**Heading:** How CRA positions customers for RAMP (Rapid Migration Programme)

**What is RAMP?**  
GCP Rapid Migration Programme (RAMP) is a structured Google Cloud migration acceleration programme that provides funding, technical resources, and programme management support for large-scale GCP migrations.

**RAMP typical eligibility criteria:**
- Significant GCP consumption commitment (varies by market and programme year)
- Qualified Google Cloud Partner leading the migration
- Formal migration plan and wave structure
- Typically targeting large-scale migrations (500+ VMs or enterprise-grade workloads)

**How CRA Phase 4 satisfies RAMP prerequisites:**

| RAMP Prerequisite | CRA Output |
|---|---|
| Formal migration assessment complete | CRA Phases 1–3 complete; Phase 3 playback delivered |
| GCP as primary recommendation | Hyperscaler decision matrix confirms GCP recommendation |
| Migration wave plan | `migration-wave-planner.xlsx` — sequenced, time-bound, resource-modelled |
| Programme management structure | RACI matrix from `governance-model.xlsx` |
| Customer commitment to GCP | Part 2 Entry Point + signed customer SOW |
| Google Cloud Partner engaged | Rackspace Partner Advantage registration active |

**Speaker notes:**  
RAMP typically requires a larger estate and a higher GCP consumption commitment than PSO credits. For mid-market customers (200–500 VMs), PSO credits are the more likely programme. For enterprise customers (500+ VMs, significant workloads), RAMP is the target. The Rackspace Alliance Manager should screen for RAMP eligibility at scoping and confirm with the GCP PDM — the programme requirements are specific.

---

## Slide 10 — Linux, Containers, and Open Source on GCP

**Heading:** GCP's open-source strength — and how CRA surfaces it

**Why this matters:**  
CRA Phase 2 flags OSS Licence Risk for Redis, Elasticsearch, HashiCorp Vault, and MongoDB. GCP has strong managed service alternatives for all of these — and in several cases, GCP's managed services are more mature than equivalents on Azure or AWS:

| OSS Product | Licence Risk | GCP Managed Alternative | Notes |
|---|---|---|---|
| Redis OSS (post v7.4) | SSPL | Memorystore for Redis / Memorystore for Valkey | GCP's Memorystore is fully managed; Redis-compatible |
| Elasticsearch (post 7.10) | SSPL | Elastic on GCP (Marketplace) or Vector Search | GCP has native Elastic partnership; clean migration path |
| HashiCorp Vault | BSL | Secret Manager / Berglas | GCP-native secrets management; no licence concerns |
| MongoDB | SSPL | Cloud Firestore / MongoDB Atlas on GCP | MongoDB Atlas available on GCP Marketplace |
| Kafka | No licence risk | Pub/Sub + Dataflow | GCP's Pub/Sub is the natural Kafka alternative |

**CRA Phase 3 action:**  
OSS-flagged workloads costed using GCP managed service pricing in gcp-evaluation.xlsx `OSS-Migration` tab. This ensures TCO reflects real migration costs including OSS licence resolution.

**CRA Containers / Kubernetes note:**  
For workloads flagged as "Cloud Friendly" (Replatform) in Phase 2, CRA Phase 3 models containerisation cost on Google Kubernetes Engine (GKE). GKE is often the most capable managed Kubernetes service — this can be a legitimate GCP advantage for containerisation-ready workloads.

**Speaker notes:**  
GCP's open-source ecosystem relationships (Elastic, MongoDB Atlas on GCP, HashiCorp on GCP Marketplace) are a genuine differentiator. For customers with large Redis, Elasticsearch, or Kafka footprints, GCP's managed services are competitive options. Make sure the CRA Phase 3 architect is modelling the GCP managed service cost — not just the GCE instance that would replace the on-prem server.

---

## Slide 11 — Reference Engagement — GCP Modelled at Scale

**Heading:** GCP was evaluated at full depth in a real CRA engagement

**Reference context:**  
In the CRA framework's reference engagement (UK digital media group — 4,200+ VMs, 280 applications), GCP was one of three hyperscalers evaluated with full TCO modelling.

**GCP TCO produced:**
- n2-standard (general purpose) right-sized from P95 utilisation: all general workloads
- n2-highmem (memory-optimised): database and in-memory workloads
- 3 GCP regions evaluated: europe-west2 (London), europe-west1 (Belgium), europe-west4 (Netherlands)
- Both On-Demand and 3yr CUD pricing modelled per region
- Memorystore modelled for Redis workloads (140+ instances)
- GKE pricing modelled for containerisation-eligible applications

**What the GCP TCO showed:**
- GCP europe-west2 (London) CUD: competitive on general compute vs Azure and AWS
- Memorystore for Redis: resolution of OSS licence risk at manageable cost uplift
- GKE for containerisable workloads: lower operational overhead than self-managed Kubernetes on EC2 or Azure VMs
- GCP migration credits (Layer g): applied to net cost in the board-level summary

**Recommendation outcome:** Not shared externally. CRA is independent — results vary by estate.

**Speaker notes:**  
The key message for GCP PDMs is that GCP was evaluated with the same depth as Azure and AWS — not as a token alternative. GCP's results in this engagement were competitive in several areas, particularly for containerisation-ready workloads and for Redis/OSS workloads via Memorystore. The CRA framework does not bias against GCP — it models what the data shows.

---

## Slide 12 — Co-Sell Value Proposition

**Heading:** Why GCP should prioritise CRA-qualified opportunities

| Benefit | Detail |
|---|---|
| Pre-qualified GCP opportunity | CRA Phase 3 produces an evidenced GCP recommendation — not a sales claim |
| PSO/RAMP-ready documentation | All programme prerequisite artefacts exist; no post-assessment rework |
| Partner registration from Day 1 | Rackspace Alliance Manager registers in Partner Advantage at Phase 1 kickoff |
| Migration Center data available | CRA Phase 1 uses GCP Migration Center — data is already in GCP's tooling |
| Clear GCP consumption projection | 3-year TCO model gives per-region CUD commitment baseline |
| Reduced Google PSE involvement | CRA absorbs the discovery and assessment workload |

**For the GCP PDM's metrics:**

| GCP Metric | CRA Contribution |
|---|---|
| Migration pipeline | CRA engagements with GCP recommendation = confirmed migration pipeline |
| PSO/RAMP registrations | Every GCP-recommended CRA = one partner programme registration |
| Co-sell pipeline | CRA engagements are logged co-sell opportunities from Day 1 |
| GCP consumption | CRA TCO provides consumption projection for CUD discussion |

---

## Slide 13 — What GCP Needs to Do

**Heading:** GCP actions that maximise CRA co-sell success

| Action | When | Why |
|---|---|---|
| ☐ Refer customers needing formal multi-cloud assessment | When customer is comparing GCP to Azure/AWS | CRA produces independent, evidenced GCP recommendation |
| ☐ Provide warm customer introduction | Before Rackspace scoping call | Establishes Rackspace credibility as independent assessor |
| ☐ Acknowledge partner opportunity in Partner Advantage | Phase 1 Week 1–2 | Required for PSO/RAMP programme tracking |
| ☐ Confirm PSO credit or RAMP eligibility | Phase 1 Week 1–2 | Scopes funding opportunity correctly from Phase 1 |
| ☐ Share Migration Center access if not already deployed | Phase 1 | Accelerates GCP-specific data collection |
| ☐ Provide Google Cloud PSE for Phase 3 architecture validation (optional) | Phase 3 | PSE can validate GCP architecture recommendations |
| ☐ Attend Phase 3 playback (recommended) | Phase 3 Week 14 | Demonstrates co-sell alignment; strengthens GCP recommendation credibility |

---

## Slide 14 — The Independent Recommendation — GCP Credibility

**Heading:** A CRA-delivered GCP recommendation is unassailable

**The challenge GCP faces:**  
Many mid-market enterprises default to Azure because they have an existing Microsoft EA and their CTO has strong Microsoft relationships. A GCP recommendation that comes from Google is dismissed as sales pressure. A GCP recommendation that comes from an independent Rackspace-led, multi-cloud evaluation is a different conversation.

**What the CRA process provides:**
- Customer agrees the evaluation criteria and weights before any scoring begins
- All three clouds are scored with equal depth — Azure and AWS get the same rigour
- GCP wins where GCP is genuinely the best fit: containerisation, data analytics, OSS workloads, AI/ML
- The recommendation follows the evidence — it is not pre-determined
- All three hyperscaler SEs are in the room at the Phase 3 playback

**For a customer's Microsoft-aligned CTO:**  
"Rackspace ran a 16-week independent assessment. They evaluated Azure, AWS, and GCP. The data shows GCP is the right answer for our containerisation and analytics workloads." This is a different conversation than any Google sales rep can have.

**Speaker notes:**  
For GCP, the credibility problem is more acute than for Azure or AWS because many organisations default to Azure through inertia. A CRA-delivered GCP recommendation bypasses the "you're just saying that because you're Google" objection. It also helps Google account teams in accounts where they have not previously won compute workloads — the evidence trail from CRA gives them something concrete to work with.

---

## Slide 15 — GCP for AI/ML and Analytics Workloads

**Heading:** CRA surfaces GCP's advantage for data, analytics, and AI/ML workloads

**Phase 2 flagging in CRA:**  
Application inventory Phase 1 captures data platform and analytics workloads. Phase 2 readiness scoring applies extra criteria to these workloads:
- Data processing volume and frequency
- Current analytics stack (Spark, Hadoop, custom ETL)
- Machine learning / AI models in production
- Real-time vs batch processing requirements

**Where GCP has a structural advantage in CRA TCO:**

| Workload Type | GCP Advantage | CRA Template |
|---|---|---|
| Apache Spark / Hadoop | Dataproc — fully managed, auto-scaling | Phase 3 TCO — Dataproc vs. EC2 Spark vs. Azure HDInsight |
| Data warehouse (Teradata, Oracle DW) | BigQuery — serverless, no infrastructure cost | Phase 3 TCO — BigQuery vs. Azure Synapse vs. Redshift |
| AI/ML training and inference | Vertex AI — integrated MLOps; TPU access | Phase 4 planning — AI/ML modernisation workstream |
| Real-time event streaming | Pub/Sub + Dataflow — Kafka alternative | Phase 3 TCO — managed streaming vs. self-managed Kafka |

**CRA action:**  
Applications flagged as data platform or analytics workloads in Phase 2 are modelled with GCP managed service alternatives in Phase 3. BigQuery and Dataproc pricing is compared against equivalent Azure and AWS services in the TCO model. For customers with significant data workloads, this comparison often shows a strong GCP cost advantage.

**Speaker notes:**  
This is GCP's clearest area of competitive advantage in the CRA framework. BigQuery is genuinely cheaper than Synapse Analytics or Redshift for large analytics workloads — and Dataproc is more cost-effective than equivalent managed Spark on Azure or AWS. Make sure the CRA architect is modelling BigQuery and Dataproc in the GCP TCO for any customer with significant data or analytics workloads. If they are not, the GCP TCO will understate GCP's cost advantage.

---

## Slide 16 — Next Steps

**Heading:** Three paths to a Rackspace CRA / GCP co-sell activation

**Path 1 — Migration Center Assessment Upgrade:**  
- Customer has used GCP Migration Center for an initial assessment
- Needs a formal, board-ready multi-cloud business case
- Rackspace CRA takes the Migration Center data and builds the complete GCAF Assess + Plan deliverables
- Contact: [Rackspace Pre-Sales contact]

**Path 2 — GCP Pipeline Identification:**  
- GCP PDM identifies accounts with data, analytics, or containerisation workloads where GCP has an advantage
- Refers to Rackspace Pre-Sales for CRA scoping call
- Rackspace CRA ensures the TCO explicitly models BigQuery, Dataproc, GKE vs. alternatives
- Contact: [Rackspace Alliance Manager]

**Path 3 — Joint Pipeline Review:**  
- Monthly joint pipeline review: Rackspace Alliance Manager + GCP PDM
- Identify accounts where CRA would accelerate partner programme registration
- Contact: [Rackspace Alliance Manager]

**Framework repository:**  
[GitHub repo URL — to be updated to rxt-mpc/ps-ind-cloud-readiness-accelerator upon migration]

**CTA:**  
> "Schedule a 30-minute session between Rackspace Alliance Architecture and Google Cloud PSE to confirm CRA methodology against GCAF and PSO programme requirements."

---

## Appendix — GCP Service Mapping Reference

| CRA Workload Category | On-Premises Technology | GCP Managed Service | Notes |
|---|---|---|---|
| General compute | VMware VMs | GCE (n2, c3 families) | Direct VM migration via Migrate to VMs |
| Container platform | Docker / Kubernetes | GKE Autopilot | Managed K8s — no infrastructure to manage |
| Data warehouse | Teradata, Oracle DW, SQL Server DW | BigQuery | Serverless; no infrastructure cost |
| Spark/Hadoop analytics | On-prem Hadoop cluster | Dataproc | Fully managed; ephemeral clusters |
| Redis caching | Redis OSS | Memorystore for Redis / Valkey | Resolves OSS licence risk |
| Message queuing | Kafka, RabbitMQ | Pub/Sub + Dataflow | Event-driven architecture |
| Secrets management | HashiCorp Vault | Secret Manager | Resolves BSL licence concern |
| AI/ML platforms | On-prem GPU cluster | Vertex AI + Cloud TPU | MLOps platform + hardware |
| Object storage | NAS/SAN/NetApp | Cloud Storage | Lowest-cost GCP storage |
| Database (PostgreSQL) | PostgreSQL on VM | Cloud SQL / AlloyDB | AlloyDB for high-performance PostgreSQL |
| Database (Oracle) | Oracle EE/SE2 | Cloud SQL (if SE2) or Bare Metal Solution | Oracle RAC → Bare Metal Solution |

---

*Document Classification: PARTNER — Rackspace × Google Cloud*  
*CRA Framework v2.0 — Rackspace Cloud Solutions Architecture*  
*Build instructions: Build in PowerPoint with co-branded layout. Rackspace Red (#E31C3D) + Google Cloud Blue (#4285F4). Both logos on title slide. Do not share internal commercial deal economics with GCP partner contacts.*
