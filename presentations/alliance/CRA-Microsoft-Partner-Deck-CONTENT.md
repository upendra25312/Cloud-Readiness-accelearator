# CRA Microsoft Partner Deck — Slide Content Script

**Deck:** `CRA-Microsoft-Partner-Deck.pptx`  
**Audience:** Microsoft Partner Development Managers (PDMs), Microsoft STU (Solution Technical Unit) Architects, Microsoft Field Sales — UK and global  
**Format:** 18 slides, 30-minute co-sell briefing  
**Purpose:** Explain how Rackspace CRA aligns to Microsoft CAF, how CRA outputs satisfy AMM programme requirements, and why Rackspace-led CRA engagements are the most effective path for Azure-recommended customer assessments  
**Classification:** PARTNER — approved for sharing with Microsoft partner teams (after legal review of case study content)

> **Build instructions:** Co-branded Rackspace + Microsoft layout. Apply Rackspace Red `#E31C3D` for Rackspace elements; Microsoft Azure Blue `#0078D4` for Microsoft-aligned elements. Place both logos on the title slide. Footer: `Rackspace × Microsoft — Cloud Partner Alliance`. Speaker notes are mandatory.

---

## Slide 1 — Title Slide

**Title:** Cloud Readiness Accelerator  
**Subtitle:** How Rackspace CRA drives Azure-first outcomes, AMM funding eligibility, and structured co-sell with Microsoft  
**Rackspace logo:** Top-left  
**Microsoft logo:** Top-right (with "Microsoft Partner" designation)  
**Date:** [Date]  
**Presented by:** [Name], Rackspace Cloud Solutions Architecture + Alliance

**Visual:** Rackspace Red left panel + Azure Blue right panel, split vertically. Both logos clearly visible.

**Speaker notes:**  
Open by establishing the co-sell context. This deck is for Microsoft partner managers and STU architects — it explains the Rackspace CRA framework specifically through the lens of Azure alignment and AMM eligibility. The goal is for the Microsoft team to be confident that CRA-delivered assessments produce the right artefacts for AMM deal registration and produce credible Azure recommendations.

---

## Slide 2 — The Co-Sell Opportunity

**Heading:** Every structured assessment is a co-sell opportunity waiting to be activated

**Three-column layout:**

**Column 1 — The Gap We Fill:**  
Microsoft SMART Assessment takes 15 minutes and identifies Azure fit at a surface level. For organisations with 50+ applications, a complex estate, or Oracle / SAP workloads, SMART is a top-of-funnel signal — not a decision-making tool. Rackspace CRA is what happens next.

**Column 2 — The Rackspace Role:**  
Rackspace is the independent trusted advisor. We have no hyperscaler quota — our recommendation follows the data. When the data points to Azure (which it does for most Microsoft-heavy estates with AHB opportunity), customers receive a credible, evidence-based Azure recommendation that Microsoft can confidently co-sell with.

**Column 3 — The Microsoft Value:**  
CRA-delivered assessments produce all documentation required for AMM (Azure Migration and Modernisation) programme funding eligibility. Every CRA engagement with an Azure recommendation is a pre-qualified AMM conversation. Pre-registration at Phase 1 kickoff maximises funding eligibility.

**Bottom callout:**  
> "SMART generates the lead. CRA qualifies it. AMM funds the migration. Rackspace delivers it."

**Speaker notes:**  
This is the co-sell value chain in one sentence. The Microsoft PDM's role in a CRA engagement is to ensure AMM registration is active from Phase 1 kickoff. The Rackspace Alliance Manager will pre-register — but the Microsoft field team needs to acknowledge the registration and confirm the customer relationship status. A CRA that ends with an Azure recommendation and no AMM registration leaves money on the table for the customer and a missed co-sell metric for Microsoft.

---

## Slide 3 — CRA-to-CAF Alignment Map

**Heading:** CRA phases map directly to Microsoft Cloud Adoption Framework stages

**Full alignment table:**

| CAF Stage | CAF Purpose | CRA Phase | CRA Deliverables That Satisfy It |
|---|---|---|---|
| **Strategy** | Cloud motivation, business outcomes, justification | Pre-engagement scoping | Business drivers workshop; scope statement; stakeholder alignment |
| **Plan** | Application inventory, digital estate rationalisation | Phase 1 Discovery + Phase 2 Analysis | Application inventory; infrastructure profiling; 5-dimension readiness scores; dependency map |
| **Ready** | Landing zone design; architecture review; skills readiness | Phase 3 Evaluation | Right-sizing recommendations; Azure architecture alignment; AHB model; AMM eligibility screen |
| **Migrate** | Migration wave execution | Phase 4 Planning | Migration wave plan; Part 2 Entry Point; risk register; governance charter |
| **Govern** | Cloud governance policies, cost management | Phase 4 Planning (governance output) | Governance model; RACI; operating model design |
| **Manage** | Operational baseline, business commitments | Post-CRA (Part 2 operations) | Baseline for ongoing managed services handoff |

**Visual diagram:**
```
CAF:     [Strategy]    [Plan]         [Ready]        [Migrate]      [Govern/Manage]
              │            │               │               │                │
CRA:   [Pre-Scope]   [Ph1+Ph2]        [Ph3]           [Ph4]          [Part 2 Ops]
         SoW +         Discovery       Evaluation      Wave Plan       MS Managed
         Drivers       Analysis        TCO + AMM       Risk + Gov      Services
                       Inventory       Recommendation  Part 2 SOW
```

**Speaker notes:**  
This alignment is the key conversation for Microsoft PDMs. When they say "does this assessment satisfy our CAF methodology standards?" — this slide is the answer. The CRA deliverables map to every CAF stage, and the Phase 1+2 outputs specifically match the CAF Plan stage requirements for AMM deal registration. Share the full alignment document (`docs/MICROSOFT-CAF-ALIGNMENT.md`) for the technical deep dive.

---

## Slide 4 — AMM Funding Eligibility — What CRA Produces

**Heading:** CRA produces every artefact required for AMM programme eligibility

**AMM requirements vs. CRA outputs:**

| AMM Requirement | AMM Evidence Type | CRA Output | CRA Template |
|---|---|---|---|
| Documented assessment methodology | Process documentation | CRA METHODOLOGY.md + phase guides | `docs/METHODOLOGY.md` |
| Application and infrastructure inventory | Current-state data | Application inventory + Infrastructure profiling | `application-scoping-profiling.xlsx` + `infrastructure-profiling.xlsx` |
| Multi-dimensional readiness assessment | Readiness scoring | 5-dimension cloud readiness scores per application | `cloud-readiness-scoring-v2.xlsx` |
| TCO / ROI analysis | Financial model | 7-layer TCO: Azure, AWS, GCP comparison | `business-case-tco-roi.xlsx` |
| Azure as primary recommendation | Recommendation documentation | Hyperscaler decision matrix + assessment report | `hyperscaler-decision-matrix.xlsx` + report |
| Migration wave plan | Migration roadmap | Sequenced application migration plan | `migration-wave-planner.xlsx` |
| Partner co-sell designation | Partner status | Rackspace Microsoft partner status ✅ | Rackspace partner tier documentation |

**Key message:**  
A CRA-delivered assessment does not require additional documentation to support an AMM funding request. The templates are already structured to produce AMM-compatible outputs. No post-assessment rework.

**Speaker notes:**  
This is the slide that simplifies the AMM conversation. Microsoft PDMs often spend time checking whether a partner's assessment output meets AMM requirements. CRA was designed with AMM outputs in mind — every required piece of evidence has a named template. Bring `docs/MICROSOFT-CAF-ALIGNMENT.md` to any Microsoft PDM technical review.

---

## Slide 5 — Azure Hybrid Benefit in the CRA TCO Model

**Heading:** AHB is modelled explicitly — not forgotten

**What is Azure Hybrid Benefit (AHB)?**  
AHB is a Microsoft licensing benefit that allows organisations with active Software Assurance (SA) on Windows Server or SQL Server to use those licences in Azure — eliminating the licence cost from the Azure VM or SQL managed service price.

**Impact in a typical mid-market estate:**

| Licence Type | Typical saving with AHB | Requirement |
|---|---|---|
| Windows Server Standard/Datacenter | 15–40% VM cost reduction | Active SA on Windows Server licences |
| SQL Server Standard | ~70% cost reduction per core | Active SA on SQL Server Standard licences |
| SQL Server Enterprise | ~70% cost reduction per core | Active SA on SQL Server Enterprise licences |

**How CRA models AHB:**

1. Phase 1 Discovery: Infrastructure profiling captures all Windows Server and SQL Server versions and licence types
2. Phase 3 Evaluation: AHB eligibility screened (requires active SA confirmation from customer)
3. TCO Licensing Overlay tab: separate rows for PAYG vs. AHB scenarios per VM type
4. Customer receives both scenarios — PAYG (worst case) and AHB (best case for Azure)

**Important:**  
AHB saving is only available in Azure. AWS and GCP do not have an equivalent programme for Windows or SQL Server licences. For Microsoft-heavy estates, this creates a legitimate structural cost advantage for Azure in the TCO model.

**Speaker notes:**  
For Microsoft-heavy estates, AHB can be a decisive factor in the hyperscaler recommendation. A customer with 300 SQL Server Enterprise instances has a massive licence cost that disappears in Azure (with SA) but remains in AWS or GCP. Make sure Rackspace are modelling both scenarios and that the Microsoft account team has confirmed SA status with the customer before the CRA Phase 3 TCO is finalised. SA status confirmation is ideally done at Phase 1 scoping — not in Phase 3.

---

## Slide 6 — SMART to CRA Handoff Process

**Heading:** How to convert a SMART assessment into a Rackspace CRA engagement

**Step-by-step handoff:**

| Step | Action | Owner | Timing |
|---|---|---|---|
| 1 | Customer completes Microsoft SMART Assessment | Customer (facilitated by Microsoft SE) | Pre-engagement |
| 2 | SMART score review: Amber or below → CRA trigger | Microsoft SE + Rackspace Pre-Sales | Within 1 week of SMART result |
| 3 | Rackspace Pre-Sales conducts scoping call (1 hr) | Rackspace Pre-Sales Architect | Within 1 week of SMART result |
| 4 | Rackspace produces CRA scoping proposal | Rackspace Pre-Sales | Within 5 business days |
| 5 | Microsoft SE introduces Rackspace to customer (warm handoff) | Microsoft SE | With scoping proposal delivery |
| 6 | Customer SOW signed → CRA begins | Customer + Rackspace | Week 0 |
| 7 | Rackspace Alliance Manager pre-registers AMM opportunity | Rackspace Alliance Manager | Week 0 / Day 1 |
| 8 | Microsoft PDM confirms deal registration and customer relationship | Microsoft PDM | Week 1 |
| 9 | Phase 3 playback: recommendation presented to customer | Rackspace Lead Architect | Week 14 |
| 10 | AMM funding application submitted (if Azure recommended) | Rackspace Alliance + Microsoft PDM | Week 14–16 |

**Key success factor:**  
Microsoft SE must provide a warm introduction — not just a referral email. The customer's trust in Rackspace as an independent evaluator is established through the Microsoft relationship. A cold introduction is significantly less effective.

**Speaker notes:**  
The warm handoff is the most important part of this process. Customers trust Rackspace's independence because their Microsoft contact has introduced them. If the customer perceives Rackspace as "Microsoft's preferred partner," they will be less confident in a non-Azure recommendation. The framing must always be: "Rackspace evaluates all three clouds independently — we just happen to find Azure is the best fit for many Microsoft-heavy estates."

---

## Slide 7 — The AMM Pre-Registration Timeline

**Heading:** When to register — and why timing is critical

**Timeline diagram:**

```
Phase 1    Phase 1    Phase 1    Phase 2    Phase 3    Phase 3    Phase 4
Day 1      Week 2     Week 7     Week 10    Week 11    Week 14    Week 18
  │           │          │          │           │          │          │
  ▼           ▼          ▼          ▼           ▼          ▼          ▼
Alliance    Microsoft  Alliance  Readiness  TCO         Rec        Part 2
Manager     PDM        Manager   scoring    complete    presented  SOW ready
registers   confirms   status    complete
in MSPP     registration check
```

**Why Day 1 registration is critical:**

Some Microsoft AMM programmes require the opportunity to be registered before the assessment is complete — not after. Registering in Week 14 (after the recommendation is already made) may reduce or eliminate funding eligibility.

**What happens at registration:**
- Rackspace Alliance Manager logs into Microsoft Partner Center (MSPP)
- Creates an "Opportunity" in the co-sell section
- Links to customer account and Microsoft account team
- Selects "Migration and Modernisation Assessment" as activity type
- Tags estimated Azure consumption commitment (from scoping estimate)

**Microsoft PDM action required:**
- Acknowledge and accept the co-sell opportunity in MSPP
- Confirm alignment with their customer account manager (CAM)
- Provide AMM programme guidance for this customer's account tier

**Speaker notes:**  
Every Microsoft PDM should have the Rackspace Alliance Manager's contact before Phase 1 begins. The Alliance Manager is the single point of contact for AMM registration. If the Microsoft PDM does not know who the Rackspace Alliance Manager is, they cannot support the co-sell. Establish this relationship at the scoping workshop — not at Phase 3.

---

## Slide 8 — Reference Engagement — Azure Recommendation at Scale

**Heading:** A real engagement. A real Azure recommendation. AMM-eligible.

**Client profile:**  
A UK digital media group — one of the UK's largest publishing organisations  
VMware on-premises estate, 2 UK data centres, 10 vCenter instances

**Assessment scope:**

| Metric | Figure |
|---|---|
| VMs assessed | 4,200+ |
| Applications scoped | 280 |
| Oracle RAC clusters identified | 18 |
| EoL OS instances (Windows Server 2012/R2) | 224 |
| Redis OSS instances identified (licence review) | 140+ |
| Governance maturity domains assessed | 6 |

**Phase 3 Outcome:**
- 3-way TCO model: Azure UK South vs AWS eu-west-2 (London) vs GCP europe-west2
- Azure AHB modelled: significant SQL Server and Windows Server licence saving
- EoL OS ESU modelled: Azure ESU (free) vs AWS/GCP ESU (paid) — material cost difference
- Oracle workloads: separate AVS (Azure VMware Solution) path identified for Oracle RAC
- **Primary recommendation: Microsoft Azure UK South**
- **AMM eligibility confirmed and pre-registered**

**Speaker notes:**  
Do not name the customer unless this has been cleared by legal. Reference as "a UK digital media group." The key message for Microsoft PDMs is that this engagement produced a credible, evidence-backed Azure recommendation after a genuine 3-way evaluation — and it was pre-registered for AMM. This is the engagement template for co-sell. Every Microsoft-facing CRA engagement should follow this model.

---

## Slide 9 — EoL OS — The Azure Cost Advantage That Gets Missed

**Heading:** Extended Security Updates for EoL Windows and SQL in Azure — FREE

**What most customers do not know:**

Microsoft provides Extended Security Updates (ESU) for Windows Server 2012/R2 and SQL Server 2012/2014 **for free** when running in Azure. Running the same EoL OS on AWS or GCP requires the customer to purchase Microsoft ESU — which can cost £100–£200 per server per year.

**TCO impact for a 200-EoL-server estate:**

| Scenario | Azure | AWS or GCP |
|---|---|---|
| ESU cost (per server/year) | £0 (included in Azure) | £100–£200 (paid to Microsoft) |
| ESU cost for 200 servers over 3 years | £0 | £60K–£120K additional cost |
| Where it appears in CRA TCO | Licensing Overlay tab — Azure ESU saving row | Licensing Overlay tab — ESU cost row |

**CRA Action:**  
Every EoL OS flagged in Phase 1 infrastructure profiling must be modelled in the Phase 3 Licensing Overlay. The Azure ESU saving row is as important as the AHB saving row.

**Partner messaging:**  
> "If your customer has Windows Server 2012 or SQL Server 2012 in their estate, Azure is structurally cheaper than AWS or GCP for those specific workloads — before you even include AHB. Make sure the Rackspace TCO model captures this."

**Speaker notes:**  
Microsoft PDMs should proactively flag this to customers who have EoL OS in their estate. Many customers are considering ESU purchases from Microsoft anyway — they may not realise those costs disappear in Azure. This is a legitimate financial argument for Azure that belongs in the TCO model. If the Rackspace team misses it in the TCO, the Microsoft SE should flag it.

---

## Slide 10 — The Hyperscaler Evaluation Protocol

**Heading:** How Rackspace ensures Azure recommendations are credible and defensible

**The evaluation standard:**

Customers and Microsoft account teams sometimes ask: "How do I know the recommendation wasn't pre-determined?" The Rackspace CRA answer:

1. **Criteria weights are agreed in writing by the customer before any scoring begins** — not after
2. **All three clouds are scored with equal rigour** — there is an AWS evaluation, a GCP evaluation, and an Azure evaluation in every Phase 3 deliverable
3. **Every score has a documented evidence reference** — not "expert judgment"
4. **The recommendation slide follows the evidence slides** — never precedes them
5. **All three hyperscaler SEs are invited to the Phase 3 playback** — this is standard practice, not optional

**What this means for Microsoft:**

When Azure is the recommendation, it is because:
- Azure scored highest on the customer-agreed weighted criteria
- The Azure TCO (including AHB and ESU savings) was the most compelling financial case
- Azure was not pre-selected — it was evidenced

This makes the Azure recommendation defensible to the customer's board, their procurement team, and any internal challenge from AWS or GCP advocates.

**Speaker notes:**  
Some Microsoft PDMs are initially concerned that inviting AWS and GCP SEs to the Phase 3 playback will undermine the Azure recommendation. The opposite is true — it strengthens it. When a customer sees all three hyperscalers in the room and the recommendation still points to Azure, they are significantly more confident in the decision. The Azure recommendation becomes unassailable.

---

## Slide 11 — Co-Sell Value Proposition

**Heading:** Why Microsoft should prioritise CRA-qualified opportunities

**For Microsoft field teams, a Rackspace CRA engagement means:**

| Benefit | Detail |
|---|---|
| Pre-qualified Azure opportunity | CRA Phase 3 produces an evidenced Azure recommendation — not a sales claim |
| AMM-ready documentation | All AMM required artefacts already exist; no post-assessment scramble |
| Accelerated migration timeline | Phase 4 wave plan is ready; Part 2 can begin within 2 weeks of assessment |
| Structured customer relationship | 16-week engagement means deeper customer relationship than a SMART scan |
| Azure consumption visibility | CRA TCO model gives a clear 3-year Azure consumption projection |
| Reduced Microsoft STU involvement | CRA absorbs the assessment workload; STU can focus on architecture validation |

**For the Microsoft PDM's metrics:**

| Microsoft Metric | CRA Contribution |
|---|---|
| Azure consumption commitments | CRA TCO provides the consumption baseline for Azure Reserved Instance discussions |
| AMM deal registrations | Every Azure-recommended CRA = one AMM registration |
| Co-sell pipeline | CRA engagements are logged co-sell opportunities from Day 1 |
| Partner engagement | CRA is a structured partner-led engagement — trackable in MSPP |

**Speaker notes:**  
Position this for the PDM's own metrics. Every Microsoft PDM has an AMM registration target and a co-sell pipeline target. A Rackspace CRA engagement that ends in an Azure recommendation and an AMM registration is a direct contribution to both. The PDM should want to see as many Rackspace CRA engagements as possible — and should be proactively referring SMART amber/red customers to Rackspace.

---

## Slide 12 — What Microsoft Needs to Do

**Heading:** Microsoft actions that maximise CRA co-sell success

**Checklist for Microsoft PDM / SE:**

| Action | When | Why |
|---|---|---|
| ☐ Refer SMART Amber/Red customers to Rackspace | Immediately after SMART result | Top-of-funnel lead generation for CRA |
| ☐ Provide warm introduction to customer (not cold email) | Before Rackspace scoping call | Establishes Rackspace independence and credibility |
| ☐ Confirm SA status for AHB eligibility | At scoping workshop | Enables accurate TCO modelling in Phase 3 |
| ☐ Acknowledge AMM deal registration in MSPP | Phase 1 Week 1 | Required for AMM funding eligibility |
| ☐ Provide AMM programme guidance for this account | Phase 1 Week 1–2 | Confirms funding tier and programme requirements |
| ☐ Attend Phase 3 playback (optional but recommended) | Phase 3 Week 14 | Shows co-sell alignment; strengthens Azure recommendation credibility |
| ☐ Support AMM funding application | Phase 3 Week 14–16 | Submits funding request once Azure recommendation is confirmed |

**Speaker notes:**  
The two critical actions are the AMM registration acknowledgement (Phase 1 Week 1) and the SA status confirmation for AHB (at scoping). Both are quick actions that have major financial impact. If either is missed, the customer loses access to potentially significant funding. The Microsoft PDM's involvement in Phase 1 is light — but it must happen.

---

## Slide 13 — Framework Reference Materials

**Heading:** What Rackspace provides for Microsoft technical review

**Available for Microsoft partner review:**

| Document | Content | Location |
|---|---|---|
| `docs/MICROSOFT-CAF-ALIGNMENT.md` | Full CAF stage-to-CRA mapping; AMM eligibility table; AHB modelling guidance | GitHub repo |
| `docs/METHODOLOGY.md` | Complete CRA methodology; phase durations; quality gates | GitHub repo |
| `Templates/03-evaluation/TCO-TEMPLATES-AUDIT-SPEC.md` | 7-layer TCO model structure; Azure-specific layers (AHB, ESU) | GitHub repo |
| `Templates/03-evaluation/HYPERSCALER-TEMPLATES-AUDIT-SPEC.md` | Hyperscaler evaluation methodology; equal-treatment standards | GitHub repo |
| `docs/DMG-MEDIA-UK-LESSONS-LEARNED.md` | Reference engagement lessons; Azure recommendation context | Private repo (internal) |

**GitHub repo:** [To be updated to rxt-mpc/ps-ind-cloud-readiness-accelerator upon migration]

**Request for Microsoft PDM review:**  
> "We would welcome a 1-hour Microsoft PDM technical review of the CRA methodology to confirm CAF alignment and AMM eligibility standards are met. Contact [Alliance Manager email] to schedule."

**Speaker notes:**  
The methodology documentation is public (GitHub). Invite the Microsoft STU architect to review MICROSOFT-CAF-ALIGNMENT.md and METHODOLOGY.md. A Microsoft PDM technical sign-off on CRA as an AMM-qualifying methodology would be a significant co-sell enabler — it removes any remaining friction from AMM registration conversations.

---

## Slide 14 — The Oracle and AVS Conversation

**Heading:** Oracle workloads in Azure — the AVS path

**The Oracle challenge in Azure:**  
Oracle RAC and Oracle Database Enterprise Edition have specific licensing requirements in Azure. Microsoft's Azure VMware Solution (AVS) provides an Oracle-supported migration path that preserves existing Oracle licence terms without requiring Oracle BYOL renegotiation.

**AVS (Azure VMware Solution) in CRA:**

| Scenario | Recommendation | CRA Template |
|---|---|---|
| Oracle RAC (standard) | AVS migration + Oracle Practice specialist engagement | Phase 4 wave plan — Wave 5+ specialist path |
| Oracle E-Business Suite | Evaluate: AVS or Azure-native (Oracle DB on Azure IaaS) | Oracle Practice Lead input required at Phase 2 |
| Oracle Database on standard VMs | Azure IaaS BYOL or Oracle DB on Azure | Licence Overlay tab — Oracle rows |
| Oracle SE2 on Linux | Standard Azure IaaS migration | No AVS required |

**Key message for Microsoft:**  
When CRA identifies Oracle RAC in a customer estate, Rackspace engages the Oracle Practice Lead in Phase 1. AVS is the standard recommendation for Oracle RAC workloads targeting Azure. This keeps Oracle workloads in the Azure estate rather than being retained on-premises or routed to OCI.

**Speaker notes:**  
Oracle workloads are the most complex piece of the hyperscaler recommendation for Azure. Microsoft's AVS offering is an important tool here — it preserves existing Oracle licence investments while migrating to Azure. Make sure the Microsoft STU architect is aware that Rackspace CRA includes an Oracle escalation path in Phase 1, and that AVS is modelled in Phase 3 where applicable. This is a conversation to have early — Oracle analysis takes 4–6 weeks.

---

## Slide 15 — Multi-Cloud Exceptions in an Azure-Primary Recommendation

**Heading:** How we handle workloads that cannot go to Azure

**Multi-cloud exceptions worksheet:**  
`Templates/03-evaluation/hyperscaler-decision-matrix.xlsx` → `Multi-Cloud-Exceptions` tab

**Common exceptions in Azure-primary engagements:**

| Workload Type | Reason It Cannot Go to Azure | Alternative Path |
|---|---|---|
| Oracle RAC (if AVS not viable) | Oracle licence terms; customer prefers OCI | Oracle Cloud Infrastructure (OCI) — retained in Phase 5+ |
| Low-latency applications to GCP data | Customer has GCP-hosted partner/customer systems requiring <5ms | Retain on-prem or consider GCP secondary |
| Regulatory data sovereignty | Specific data must remain in a non-Azure jurisdiction | Evaluate alternative Azure region or secondary cloud |
| SaaS applications | Already in a non-Azure SaaS (e.g., Salesforce, ServiceNow) | Repurchase/retain — exclude from primary cloud TCO |
| Oracle Forms applications | No cloud equivalent — requires rearchitecting or maintaining on-prem | Retain or full rearchitect — separate workstream |

**Key message:**  
A multi-cloud or hybrid recommendation is not a failed evaluation — it is an accurate one. Documenting exceptions transparently strengthens the credibility of the primary Azure recommendation.

**Speaker notes:**  
Microsoft PDMs sometimes worry about "partial Azure" recommendations. The reality is that a transparent recommendation that says "Azure for 95% of the estate, OCI for Oracle RAC workloads" is far more credible and defensible than a recommendation that forces everything to Azure and glosses over Oracle. The customer's board will respect the nuance — and the Azure consumption will still be substantial.

---

## Slide 16 — Governance and Cloud Readiness for Azure

**Heading:** Phase 2 governance assessment prepares the customer for Azure landing zone design

**Azure-specific governance outputs from CRA Phase 2:**

| CRA Governance Domain | Azure Landing Zone Implication | Microsoft Reference |
|---|---|---|
| Identity & Access Management | Azure Active Directory (Entra ID) design; RBAC model for Azure subscriptions | CAF Landing Zone: Identity Management |
| Security & Compliance | Azure Security Centre (Defender for Cloud) readiness; Microsoft Sentinel integration | CAF Landing Zone: Security Baseline |
| Change & Release Management | Azure DevOps / GitHub Actions for cloud deployment pipelines | CAF: Platform Automation |
| Monitoring & Observability | Azure Monitor / Log Analytics workspace design | CAF Landing Zone: Management |
| Cost Management (FinOps) | Azure Cost Management + Billing; tagging strategy for chargeback | CAF: Governance: Cost Management |
| Operations Readiness | Azure Update Manager; Azure Automation | CAF Landing Zone: Management Baseline |

**Key message:**  
The CRA governance maturity assessment produces a baseline that directly informs the Azure Landing Zone design. By Phase 4, the customer has a gap register across all 6 governance domains that maps to CAF landing zone design decisions. This eliminates the "design the landing zone from scratch" step that typically delays migration starts.

**Speaker notes:**  
This is a significant co-sell message for Microsoft STU architects. The CAF landing zone design conversation is often a bottleneck — customers do not know what governance decisions to make before they can start building in Azure. CRA Phase 2 produces the baseline that answers those questions. The STU architect can take the CRA governance output and directly begin landing zone design without running a separate assessment.

---

## Slide 17 — Rackspace's Microsoft Partnership

**Heading:** Why Rackspace is Microsoft's preferred partner for CRA-led engagements

**Partnership credentials:**

| Credential | Detail |
|---|---|
| Microsoft Partner designation | [Current Rackspace Microsoft Partner tier] |
| Azure Expert MSP | [If applicable] — validated Microsoft Azure managed services capability |
| AMM registration capability | Qualified to register and execute AMM assessments and migrations |
| CRA-to-AMM pipeline | Structured process to convert every CRA engagement to an AMM registration |
| CAF-aligned methodology | Documented CAF stage-to-CRA phase mapping (see `docs/MICROSOFT-CAF-ALIGNMENT.md`) |
| UK market presence | Rackspace Cloud Solutions Architecture — UK-based delivery team |
| Oracle Practice | Dedicated Oracle practice for Oracle-to-Azure migrations (AVS + IaaS paths) |

**What Rackspace commits to in co-sell:**
- Alliance Manager on Phase 1 kickoff call — every engagement
- AMM pre-registration within 5 business days of SOW signature
- Microsoft PDM invited to Phase 3 playback
- Azure recommendation documented and shared with Microsoft account team at Phase 3
- AMM documentation package prepared and submitted within 10 business days of recommendation

**Speaker notes:**  
This slide establishes Rackspace's credibility as a Microsoft partner — not just as a methodology provider. The key differentiators are the Alliance Manager process (Day 1 registration), the Oracle practice (for mixed estates), and the CAF alignment documentation. These are the three things that make Rackspace the partner of choice for complex assessment-led engagements.

---

## Slide 18 — Next Steps — Starting a CRA Co-Sell Conversation

**Heading:** Three ways to activate a Rackspace CRA opportunity with Microsoft

**Path 1 — SMART Referral:**  
- Microsoft SE completes SMART with a customer and score is Amber/Red
- SE refers to Rackspace Pre-Sales Architect for CRA scoping call
- Contact: [Rackspace Pre-Sales contact email/name]

**Path 2 — Joint Pipeline Review:**  
- Rackspace and Microsoft PDM review joint pipeline monthly
- Identify accounts where a formal cloud assessment would accelerate Azure commitment
- Rackspace Pre-Sales Architect attends joint account planning session
- Contact: [Rackspace Alliance Manager email/name]

**Path 3 — Inbound from Customer:**  
- Customer approaches Microsoft directly for cloud readiness help
- Microsoft SE recommends Rackspace CRA as the assessment approach
- Warm introduction email from Microsoft SE to Rackspace
- Contact: [Rackspace Pre-Sales contact]

**Framework repository:**  
[GitHub repo URL — to be updated to rxt-mpc/ps-ind-cloud-readiness-accelerator]

**CTA:**  
> "Schedule a 30-minute technical briefing between Rackspace Alliance Architecture and Microsoft STU to validate CRA against CAF and AMM requirements. This is the one session that unlocks co-sell activation."

---

## Appendix — AMM Registration Quick Reference

| Step | Action | Owner | Portal |
|---|---|---|---|
| 1 | Rackspace identifies customer as AMM-eligible at scoping | Rackspace Pre-Sales | — |
| 2 | Rackspace Alliance Manager registers opportunity | Rackspace Alliance Manager | MSPP Partner Center |
| 3 | Microsoft PDM acknowledges and accepts co-sell | Microsoft PDM | MSPP Partner Center |
| 4 | CRA Phase 1–3 executed; Azure recommendation confirmed | Rackspace Lead Architect | — |
| 5 | AMM documentation package assembled from CRA deliverables | Rackspace Alliance | CRA templates |
| 6 | AMM funding application submitted | Rackspace + Microsoft PDM | AMM programme portal |

---

*Document Classification: PARTNER — Rackspace × Microsoft*  
*CRA Framework v2.0 — Rackspace Cloud Solutions Architecture*  
*Build instructions: This document is the slide content script for `CRA-Microsoft-Partner-Deck.pptx`. Build in PowerPoint using a co-branded Rackspace + Microsoft layout. Rackspace Red (#E31C3D) + Azure Blue (#0078D4). Both logos on title slide. Remove internal commercial figures (deal economics) before sharing with Microsoft partner contacts.*
