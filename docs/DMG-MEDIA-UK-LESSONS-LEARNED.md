# CRA Lessons Learned — DMG Media UK Engagement

**Engagement:** Cloud Readiness Assessment Part 1  
**Customer:** DMG Media UK (Daily Mail Group Trust)  
**Delivery Period:** February – May 2026  
**Lead Architect:** Rackspace Cloud Solutions Architecture  
**Document Version:** 1.0  
**Classification:** Internal — Rackspace Delivery Teams

---

## Purpose

This document captures the lessons learned from the DMG Media UK CRA engagement for use in:

1. Onboarding new architects to the CRA framework
2. Scoping future CRA engagements (SOW calibration)
3. Improving CRA templates and phase guides (feedback loop)
4. Alliance partner briefings — what a real media-sector engagement looks like

For the full case study narrative, see `Examples/media-entertainment/dmg-media-uk-case-study.md`.

---

## Engagement at a Glance

| Parameter | Value |
| --- | --- |
| Customer sector | Media & Entertainment (UK national press) |
| Estate assessed | 4,212 VMs, 18 Oracle RAC clusters, 347 SQL Server instances, 280 applications |
| Data centres | 2 × London (Docklands + Sovereign House) |
| Discovery tooling | GCP Migration Center (primary), Azure Migrate (validation) |
| Primary recommendation | Microsoft Azure (UK South + UK West DR) |
| Three-year saving | ~39% vs. on-prem status quo (AHB + 3yr RI applied) |
| Partner funding identified | Microsoft AMM eligibility confirmed |
| Assessment duration | ~16 weeks (parallelised) |

---

## Lesson 1 — Scope Estimation: Assume the Customer's CMDB Is Wrong

**What happened:** The original SOW was scoped at 2,700 VMs. The actual assessed estate was 4,212 VMs — a 57% variance discovered incrementally across Phase 1 weeks 2–5.

**Why it happened:** The customer's CMDB had not been updated in 18 months. Shadow IT and business-unit-managed infrastructure were not in the initial count. DR and test environments were initially treated as out-of-scope but had to be profiled to determine migration approach.

**Impact:** Phase 1 extended beyond original timeline. Phase 3 TCO and Phase 4 wave planning both had to be rescoped mid-engagement.

**What to do differently:**

- Add 20–30% buffer to any customer-provided estate estimate when scoping the SOW
- Add explicit scope variance language to the SOW: "If the assessed estate exceeds the estimated count by more than 15%, a change control will be issued"
- In Phase 1 week 1: cross-reference the customer's CMDB against network IPAM data, vCenter inventory, and physical DC records — discrepancies are diagnostic, not unusual
- Initiate a preliminary asset discovery scan in week 1 (using RVTools or Azure Migrate agentless) to get an independent VM count before committing to a final SOW scope

**Template impact:** Epic 4A.1 (application scoping template) should include a "scope confidence" field — High / Medium / Low — so the architect documents their confidence in the customer's estate estimate at engagement start.

---

## Lesson 2 — CAB Lead Time: Start the Firewall Change Request in Week 1

**What happened:** Azure Migrate and GCP Migration Center both require outbound firewall rules to be opened to cloud service endpoints. The request went to the customer's Change Advisory Board (CAB) in week 3 — after tooling was set up and ready to deploy. CAB approval took 7 business days, pushing the effective discovery start to week 4.5.

**Why it happened:** The delivery team treated CAB approval as a "when the tool is ready" action rather than a "day 1 parallel track" action.

**Impact:** Phase 1 stretched from 6 weeks to 7 weeks (planned minimum). The utilisation collection window was compressed, creating risk to the Phase 3 hard gate.

**What to do differently:**

- Add CAB lead time to the Phase 1 kick-off agenda: identify the customer's change control process and lead time on day 1
- Submit the firewall change request in week 1, not when the appliance is deployed
- Required ports: Azure Migrate → 443 outbound to Azure endpoints; GCP Migration Center → 443 outbound to migration.googleapis.com; AWS ADS → 443 outbound to arsenal.us-east-1.amazonaws.com
- If CAB process is lengthy (>5 business days), initiate a manual RVTools / CSV export as a parallel data track so Phase 1 is not blocked while awaiting firewall approval

**Phase guide impact:** This lesson is now documented in `docs/guides/01-discovery-phase-guide.md` Phase Duration section (v2.0 audit note).

---

## Lesson 3 — Oracle: Engage the Oracle Practice in Phase 1, Not Phase 3

**What happened:** 18 Oracle RAC clusters were identified in the infrastructure inventory but not escalated to the Oracle DBA practice until Phase 3 when TCO modelling began. The Oracle practice review took 3 weeks to complete licensing analysis — compressing Phase 3 to its hard minimum.

**Why it happened:** Oracle workloads were treated as "just another server profile" in Phase 1 and Phase 2. The complexity of Oracle RAC licensing in the cloud (processor-based licensing, vCPU multipliers, VMware soft-partitioning rules) was not flagged as requiring specialist input until the TCO model stalled.

**Impact:** Phase 3 TCO was delayed by 3 weeks. The Oracle licensing recommendation was the last section to be finalised before Phase 3 playback.

**What to do differently:**

- When Oracle RAC, Oracle EE, or Oracle Forms appears in the Phase 1 inventory, escalate to the Oracle practice immediately — in Phase 1, not Phase 3
- Oracle licensing questions to answer in Phase 1: (a) Is licensing processor-based or NUP? (b) Does the customer have a ULA? (c) Are any workloads on VMware (soft-partitioning rules apply)? (d) Has Oracle been notified of cloud migration intent?
- Oracle RAC → Cloud migration path options must be scoped before Phase 3 TCO is started: BYOL on dedicated host (Azure/AWS), Oracle DB Service on OCI, or RAC → single-instance migration
- Allow a minimum of 4 weeks for Oracle licensing analysis in Phase 3 if the estate has more than 5 Oracle clusters

**Template impact:** Epic 4A.1 (application scoping template) should flag Oracle workloads with a "requires Oracle practice review" indicator. Epic 4B.7 (licensing overlay tab) must include Oracle as a first-class row.

---

## Lesson 4 — Third-Party Licensing: Redis OSS → Enterprise Is a Commercial Negotiation

**What happened:** 140+ Redis OSS instances were identified in Phase 1. During Phase 2 readiness scoring, it became apparent that the customer was using Redis in production at a scale that Redis Ltd. would classify as requiring a Redis Enterprise commercial licence in a cloud-hosted environment.

**Why it happened:** Redis OSS → Redis Enterprise licence transition is not well-known outside of specialist engineers. The application scoping template had no flag for "open-source software with commercial cloud restrictions."

**Impact:** The TCO model had to include Redis Enterprise licencing costs in the baseline. The Phase 2 readiness score for Redis-dependent applications dropped as a result. Commercial negotiations with Redis Ltd. were initiated as a parallel workstream.

**What to do differently:**

- During Phase 2 readiness scoring, flag any application using open-source software with known cloud commercial restrictions: Redis, Elasticsearch/OpenSearch, MongoDB, HashiCorp Vault (BSL licence change 2023), Confluent/Kafka
- Add a "third-party OSS licencing risk" flag to the application scoping template
- For Redis specifically: if the customer has >50 Redis instances in production, initiate a Redis Ltd. account conversation in Phase 2 to understand commercial options before Phase 3 TCO is finalised

---

## Lesson 5 — Alliance Partner Registration Timing: Register Before Part 2 SOW Signature

**What happened:** Microsoft AMM eligibility was identified at the end of Phase 4. The AMM deal registration was initiated but was not complete when the Part 2 SOW discussion began.

**Why it happened:** The delivery team treated AMM registration as a "Phase 4 action" — done after the recommendation was finalised. The Rackspace Alliance Manager was not engaged until the Part 2 Entry Point document was drafted.

**Impact:** The Part 2 SOW commercial timeline was extended by 2 weeks waiting for AMM registration confirmation. In a competitive situation, this gap would represent a risk.

**What to do differently:**

- Add AMM/MAP/PSO eligibility check to the Phase 1 kickoff checklist — not Phase 4
- Engage the Alliance Manager at engagement start: share the customer name, estate size, and likely primary cloud direction
- Formal registration requires the MRA, inventory, and business case — but the Alliance Manager can pre-register the opportunity in week 1 and complete the formal submission when the Phase 3 deliverables are ready
- For Azure engagements: AMM deal registration must be in the MSPP portal before the Part 2 SOW is countersigned by Rackspace — not before the customer signs, but before Rackspace countersigns

**Phase guide impact:** This lesson is now documented in `docs/guides/04-planning-phase-guide.md` as an action in the Part 2 Entry Point section.

---

## Lesson 6 — Utilisation Data: The Phase 3 Hard Gate Is Non-Negotiable

**What happened:** After the CAB delay (Lesson 2), there was internal pressure to start Phase 3 TCO modelling before the full 4-week utilisation collection window was complete. The pressure came from both the customer (eager to see numbers) and commercial scheduling (Part 2 SOW target date).

**Why it happened:** The 2-week minimum utilisation data requirement was documented in METHODOLOGY.md but was not prominently surfaced to the delivery team or the customer at engagement start.

**Impact:** Phase 3 was started 2 weeks after the first week of utilisation data was available (not the full 4 weeks). The initial TCO model had to be revised when the additional 3 weeks of data showed significantly higher peak utilisation than the first week captured. The revision required a Phase 3 re-run and a customer re-presentation.

**What to do differently:**

- State the utilisation data gate explicitly in the Phase 1 kickoff meeting: "Phase 3 cannot start until we have [target] weeks of clean CPU/RAM/network/storage data"
- Include the utilisation collection window on the engagement project plan as a named dependency line
- For customers with month-end batch processing or payroll cycles (all enterprise customers): the minimum window must include at least one full month-end cycle — typically 4 weeks, not 2
- When there is schedule pressure: show the customer the risk in financial terms — "a TCO model built on 1 week of data has ±30–50% accuracy; a model built on 4 weeks has ±10–15% accuracy. The difference could be £Xm in the business case."

**Phase guide impact:** This lesson is now documented in `docs/guides/03-evaluation-phase-guide.md` Phase Duration section (hard gate note) and in `docs/guides/01-discovery-phase-guide.md` example output section.

---

## Lesson 7 — Parallelisation: Phase 2 Can Start Before Phase 1 Ends

**What happened:** In the original engagement plan, Phase 2 was scheduled to start after Phase 1 completion. A mid-engagement schedule review identified that Phase 2 only requires a validated inventory (available by week 5 of Phase 1) — not the completed utilisation dataset.

**What was done:** Phase 2 was started in Phase 1 week 6, overlapping the final week of Phase 1. Application-owner interviews, compliance reviews, and criticality classification were completed in parallel with the final utilisation data collection.

**Impact (positive):** This saved approximately 3 weeks of elapsed engagement time with no quality trade-off. Phase 3 start was brought forward by 3 weeks.

**What to do from the start:**

- Plan Phase 2 start at Phase 1 week 6 (7-week Phase 1) or Phase 1 week 4 (6-week Phase 1) — not after Phase 1 completion
- The only dependency is a validated infrastructure inventory — not utilisation data, not final Phase 1 report
- Resource plan accordingly: Phase 2 analysts must be available before Phase 1 ends

**Phase guide impact:** This lesson is now documented in `docs/guides/02-analysis-phase-guide.md` Phase Duration section (v2.0 audit note).

---

## Lesson 8 — EoL OS: Extended Security Updates Must Be in the TCO

**What happened:** 340+ servers were identified running Windows Server 2012 (EoL October 2023) and RHEL 6 (EoL November 2020). These servers were eligible for Extended Security Updates (ESU) in Azure but not in their on-premises state.

**Why it matters for TCO:** The on-premises status quo TCO must include the cost of either (a) ESU licences for continued Windows 2012 support or (b) OS upgrade projects. In Azure, Windows 2012 ESU is included free with the VM — a named financial benefit.

**What to do differently:**

- Flag EoL OS servers in Phase 1 profiling immediately — do not wait for Phase 2 readiness scoring
- Include ESU cost in the on-premises status quo TCO baseline (it is a real current-state cost, not a future cost)
- In the Azure TCO model, show ESU as a cost avoided (free in Azure) — this is a genuine Azure advantage for estates with high EoL OS density
- EoL OS density also drives migration urgency: a customer with 300+ EoL servers has a security compliance risk that makes the migration business case stronger regardless of cost savings

---

## Lesson 9 — Executive Presentation: "Evidence Before Recommendation" Is Non-Negotiable

**What happened:** An early internal draft of the Phase 3 playback deck started with the recommendation ("Azure") on slide 3, then presented the scoring data. Customer feedback in review was that the recommendation felt "pre-determined" and the scoring felt like it was constructed to justify a foregone conclusion.

**Why it matters:** The credibility of the entire CRA depends on the recommendation being seen as the output of an objective process — not a Rackspace commercial preference.

**What to do differently:**

- The recommendation slide must come after the evidence slides — always
- Structure: (1) Estate summary → (2) Readiness profile → (3) Cloud comparison (all three, equal treatment) → (4) Scoring matrix → (5) Recommendation with rationale → (6) Next steps
- When presenting the scoring matrix, explain the weighting methodology before showing the scores
- Use language that acknowledges alternatives: "AWS was close on overall cost but was disadvantaged on licensing" — never imply the other hyperscalers weren't seriously considered

**Template impact:** Epic 4D.4 (audit of executive summary template) must verify the slide flow follows evidence-before-recommendation structure.

---

## Summary Table

| # | Lesson | CRA Phase | Action Type | Template Impact |
| --- | --- | --- | --- | --- |
| 1 | Scope variance — assume CMDB is wrong | Phase 1 | SOW scoping + week 1 check | 4A.1 scope confidence field |
| 2 | CAB lead time — submit firewall request day 1 | Phase 1 | Kick-off checklist | Phase guide updated |
| 3 | Oracle — engage Oracle practice in Phase 1 | Phase 1 + 3 | Escalation trigger | 4A.1 Oracle flag; 4B.7 Oracle tab |
| 4 | Redis / OSS commercial licencing | Phase 2 | Readiness scoring flag | 4A.1 OSS licence risk field |
| 5 | AMM/MAP/PSO — register before Part 2 SOW | Phase 4 | Alliance Manager trigger | Phase guide updated |
| 6 | Utilisation data gate — non-negotiable | Phase 1 → Phase 3 | Hard gate communication | Phase guide updated |
| 7 | Phase 2 can start before Phase 1 ends | Phase 1/2 boundary | Resource planning | Phase guide updated |
| 8 | EoL OS — ESU cost in on-prem baseline | Phase 1 + 3 | TCO modelling | 4B.5 on-prem tab |
| 9 | Evidence before recommendation — always | Phase 3 + 4 | Presentation structure | 4D.4 template audit |

---

*Rackspace Cloud Solutions Architecture — CRA Framework v2.0*  
*Lessons derived from: DMG Media UK Cloud Readiness Assessment, February–May 2026*  
*For the full case study: `Examples/media-entertainment/dmg-media-uk-case-study.md`*
