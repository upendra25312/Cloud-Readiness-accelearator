# Hyperscaler Recommendation Templates Audit Specification

**Covers Epics:** 4C.1 – 4C.4  
**Templates in scope:**
- `Templates/03-evaluation/hyperscaler-decision-matrix.xlsx` (4C.1)
- `Templates/03-evaluation/hyperscaler-weighted-selection-criteria.xlsx` (4C.1 supplement)

**How to use this spec:** Open each template. Compare against the required structure below. The Decision Matrix is the single most customer-visible deliverable in Phase 3 — it must produce a defensible, documented recommendation. Any scoring that looks arbitrary or pre-determined will undermine the entire engagement.

---

## 4C.1 — Hyperscaler Decision Matrix (`hyperscaler-decision-matrix.xlsx`)

### Purpose

The primary deliverable of Phase 3. Produces a weighted score for each hyperscaler and a documented primary recommendation with rationale. Must be completed before the Phase 3 playback meeting.

### Required Tab Structure

| Tab | Purpose |
| --- | --- |
| Instructions | Who fills this in, when, how |
| Criteria & Weights | Define evaluation criteria and weighting (customer-agreed) |
| Azure Scoring | Score Azure against each criterion with evidence |
| AWS Scoring | Score AWS against each criterion with evidence |
| GCP Scoring | Score GCP against each criterion with evidence |
| Weighted Summary | Auto-calculated: weighted scores + recommendation output |
| 7Rs Estate View | One row per application: Rehost / Replatform / Rearchitect / Repurchase / Retire / Retain / Relocate |
| Multi-Cloud Exceptions | Apps that cannot go to the primary cloud — documented reason |
| Worked Example | Anonymised DMG Media UK scoring (reference) |

### Required Structure — Criteria & Weights Tab

The weighting must be agreed with the customer before scoring begins. Use this standard starting point — adjust per engagement.

| Criterion | Description | Default Weight | Notes |
| --- | --- | --- | --- |
| Total Cost of Ownership (3yr) | L4L and optimised scenarios across all tiers | 30% | Highest weight — customers care most about cost |
| Licensing advantage | AHB / BYOL / SA portability; SQL / Windows / Oracle | 20% | High impact for Microsoft-heavy estates |
| Technical fit | Workload type compatibility; managed services availability; GPU / HPC / storage options | 15% | |
| Regulatory & compliance | Certifications (ISO, SOC, FCA, GDPR); data residency; UK region footprint | 15% | Critical for regulated sectors (media, finance, health) |
| Partner commercial (AMM/MAP/PSO) | Funded programme eligibility; estimated value; registration status | 10% | Rackspace differentiator |
| Strategic alignment | Existing enterprise agreements; roadmap; executive relationships; support contracts | 10% | |
| **Total** | | **100%** | |

> **Important:** Present the weighting to the customer and get written agreement (email confirmation is sufficient) before running the scores. This prevents "you weighted it in Azure's favour" challenges after the recommendation is made.

### Required Structure — Scoring Tabs (one per hyperscaler)

Each cloud must have its own scoring tab with identical structure.

| Column | Content |
| --- | --- |
| Criterion | From Criteria & Weights tab |
| Weight | From Criteria & Weights tab |
| Score (1–10) | Lead Architect assessment |
| Evidence | Specific data point justifying the score |
| Source | Where the evidence comes from (TCO tab / customer interview / public documentation) |
| Weighted Score | = Score × Weight |

**Evidence must be specific.** Examples of acceptable evidence:

| Score | Acceptable Evidence | Unacceptable Evidence |
| --- | --- | --- |
| TCO / Cost | "Azure 3yr RI + AHB: £11.2M vs. AWS 3yr RI: £12.8M — see TCO Summary tab" | "Azure is cheaper" |
| Licensing | "1,200 Windows Server + 347 SQL Server AHB-eligible — saving £Xm/yr vs PAYG" | "Good licensing options" |
| Compliance | "Azure UK South holds FCA, ISO 27001, SOC 2, GDPR. Customer requires UK data residency." | "Good compliance" |
| AMM/MAP/PSO | "AMM eligibility confirmed: estimated £800K–£1.2M funded services" | "Funding available" |

### Required Structure — Weighted Summary Tab

This tab is the output that appears in the Phase 3 playback deck.

| Row | Content |
| --- | --- |
| Header | Criterion, Weight, Azure, AWS, GCP |
| Data rows | One row per criterion; weighted score calculated |
| Weighted Total | SUM of weighted scores per hyperscaler |
| Rank | 1st / 2nd / 3rd |
| **Recommendation** | **[HYPERSCALER] is recommended as the primary cloud platform** |
| Rationale | 3–5 bullet points, each citing a specific data point |
| Secondary | [HYPERSCALER] for [specific use case or DR] |
| Multi-cloud note | [N] workload exceptions — see Multi-Cloud Exceptions tab |

### Validation — "Evidence Before Recommendation"

Before the Phase 3 playback, validate that the slide deck follows this order:

1. Estate summary (what was assessed)
2. Readiness profile (Phase 2 output)
3. Cloud comparison (cost, licensing, compliance — all three clouds treated equally)
4. Scoring matrix (show weights agreed with customer)
5. **Recommendation** (primary + rationale)
6. Next steps

The recommendation must not appear before step 4 in the deck. If it does — restructure.

---

## 4C.2 — 7Rs Estate View Tab (add to `hyperscaler-decision-matrix.xlsx`)

**This is a named SOW deliverable.** The 7Rs view is required even if it is not detailed — it must flag each application with a migration pattern.

### Tab Name: `7Rs Estate View`

### Required Columns

| Column | Content |
| --- | --- |
| App ID | From application-scoping-profiling.xlsx |
| Application Name | |
| Business Criticality | Critical / High / Medium / Low |
| Current Platform | VMware / Hyper-V / Physical / Already cloud |
| 7R Classification | See table below |
| Justification | One sentence |
| Complexity | High / Medium / Low |
| Target Service | e.g., Azure VM / Azure SQL MI / Azure App Service / SaaS product |
| Wave (indicative) | 1–5 |
| Notes | |

### 7Rs Classification Reference

| Pattern | Definition | When to use |
| --- | --- | --- |
| **Rehost** | Lift-and-shift to IaaS VM | No code changes needed; fastest migration path; most of the estate |
| **Replatform** | Migrate with minor changes to use managed services | e.g., SQL Server → Azure SQL Managed Instance; saves patching overhead |
| **Rearchitect** | Significant redesign to use cloud-native services | e.g., monolith → containers; high complexity / high long-term benefit |
| **Repurchase** | Replace with a SaaS product | e.g., on-prem CRM → Salesforce; vendor SaaS now covers the need |
| **Retire** | Decommission — do not migrate | Application confirmed redundant or replaced; stop paying for it |
| **Retain** | Keep on-premises — cannot migrate | Regulatory / latency / dependency constraint prevents migration |
| **Relocate** | Move to different DC without cloud | Consolidate DCs without migrating to cloud |

### 7Rs Summary (calculated)

Add a summary row at the top of the tab:

| Pattern | Count | % of Estate | Notes |
| --- | --- | --- | --- |
| Rehost | COUNTIF | % | Target: 50–70% for typical enterprise estate |
| Replatform | COUNTIF | % | Target: 15–25% |
| Rearchitect | COUNTIF | % | Target: 5–10% (high cost/complexity) |
| Repurchase | COUNTIF | % | |
| Retire | COUNTIF | % | Cost saving opportunity — quantify |
| Retain | COUNTIF | % | Multi-cloud exceptions |
| Relocate | COUNTIF | % | |

---

## 4C.3 — Worked Example (add to `hyperscaler-decision-matrix.xlsx`)

### Tab Name: `Worked Example — Reference`

Populate this tab with anonymised DMG Media UK scoring to show architects what a completed matrix looks like.

**Source:** `Examples/azure/` and `Examples/media-entertainment/dmg-media-uk-case-study.md`

The key data points to use (anonymised — do not include customer name in cell values, use "Reference Engagement — Media Sector UK"):

| Criterion | Azure Score | AWS Score | GCP Score | Evidence (anonymised) |
| --- | --- | --- | --- | --- |
| TCO (3yr) | 8.5 | 7.2 | 7.8 | "Azure optimised: ~39% vs on-prem; AWS: ~30%; GCP: ~34%" |
| Licensing | 9.0 | 6.5 | 5.0 | "1,200+ Windows + 340+ SQL Server AHB-eligible; no AWS/GCP equivalent" |
| Technical fit | 8.0 | 7.5 | 7.5 | "All three clouds support workload types; Azure strongest for .NET/Windows stack" |
| Compliance | 8.5 | 8.0 | 7.5 | "All three hold UK data residency; Azure FCA alignment strongest for regulated media" |
| Partner commercial | 8.5 | 7.0 | 6.0 | "AMM eligibility confirmed; MAP partial; GCP PSO eligible" |
| Strategic | 8.0 | 6.5 | 6.0 | "Existing Microsoft EA and Unified Support" |
| **Weighted Total** | **8.6** | **7.1** | **6.9** | |
| **Recommendation** | **Primary** | Secondary | Tertiary | |

> Add a yellow header row to this tab: "WORKED EXAMPLE — Reference only. Do not edit. Replace with your own engagement scoring in the Azure Scoring / AWS Scoring / GCP Scoring tabs."

---

## 4C.4 — Multi-Cloud Exceptions Tab (add to `hyperscaler-decision-matrix.xlsx`)

**Every enterprise engagement has some workloads that cannot go to the primary cloud.**  
Documenting them explicitly prevents them from becoming a dispute point after the recommendation is presented.

### Tab Name: `Multi-Cloud Exceptions`

### Required Columns

| Column | Content |
| --- | --- |
| App ID | From application-scoping-profiling.xlsx |
| Application Name | |
| Why It Cannot Go to Primary Cloud | Specific technical / regulatory / contractual reason |
| Recommended Alternative | Second cloud / on-prem retain / SaaS |
| Complexity | High / Medium / Low |
| Commercial Impact | Estimated cost delta vs. primary cloud path |
| Action Required | Who decides / what is the resolution path |

### Common Exceptions (use as a starting checklist)

| Exception Type | Example | Action |
| --- | --- | --- |
| Oracle on OCI | Customer has Oracle workloads; OCI is cheaper but primary is Azure | Model OCI cost; present as cost optimisation option in Part 2 |
| Latency-sensitive to on-prem partner | App must stay <5ms from a specific on-prem system | Retain on-prem; include in Part 2 network design |
| Regulatory — data residency | Specific data must remain in-country; primary cloud lacks the required region | Check all three clouds for compliant regions |
| SaaS vendor lock-in | Vendor data in their own cloud; cannot extract | Retain; integrate via API from primary cloud landing zone |
| Oracle Forms / legacy apps | No cloud-native equivalent; requires IaaS rehost minimum | Rehost on primary cloud if technically possible; else Retain |

---

*Template audit spec for CRA Framework v2.0 — Rackspace Cloud Solutions Architecture*
