# TCO Templates Audit Specification

**Covers Epics:** 4B.1 – 4B.9  
**Templates in scope:**
- `Templates/03-evaluation/azure-evaluation.xlsx`
- `Templates/03-evaluation/aws-evaluation.xlsx`
- `Templates/03-evaluation/gcp-evaluation.xlsx`
- `Templates/03-evaluation/business-case-tco-roi.xlsx`

**How to use this spec:** Open each template in Excel. Compare the current tab list against the "Required Tab Structure" below. Add any missing tabs. Validate column coverage against the field lists. Prioritise 4B.1 (7-layer coverage) — this is the SOW-critical task.

---

## 4B.1 — 7-Layer TCO Coverage Check (All Templates)

The CRA SOW requires the TCO output to cover all seven cost layers. Check each template against this list. If a layer is missing, it must be added before the template is used on a live engagement.

| Layer | Description | Where It Must Appear | Likely in Template? |
| --- | --- | --- | --- |
| (a) Like-for-Like (L4L) baseline | Current on-prem specs, no rightsizing | Tab in each cloud eval template | ✅ Likely present |
| (b) Optimised / rightsized | Cloud-right-sized based on utilisation data | Tab or formula column in each cloud eval | ✅ Likely present |
| (c) Delta | L4L vs Optimised saving | Calculated column / summary tab | ⚠️ May be missing |
| (d) Licensing overlay | SQL Server (AHB/BYOL/PAYG), Oracle (BYOL), third-party | Separate overlay tab or columns in business case | ❌ Likely missing |
| (e) On-premises status quo | Current hardware, maintenance, facilities, OS support costs | Dedicated tab in `business-case-tco-roi.xlsx` | ❌ Likely missing |
| (f) Year 1 dual-running forecast | Migration overlap — cloud + on-prem running simultaneously | Dedicated tab in `business-case-tco-roi.xlsx` | ❌ Likely missing |
| (g) Partner discounts / credits | AMM / MAP / PSO funded value; RI/CUD savings | Overlay tab or row in business case summary | ❌ Likely missing |

> **Action:** For each ❌ row above, add the missing tab to the appropriate template. Specs for each missing tab are in sections 4B.5–4B.8 below.

---

## 4B.2 — Azure Evaluation Template (`azure-evaluation.xlsx`)

### Required Tab Structure

| Tab Name | Purpose | Status to Verify |
| --- | --- | --- |
| Instructions | Who fills this in, when, how | Add if missing — see Epic 10.4 |
| VM Inventory Input | Paste VM list from discovery tool; columns: VM Name, vCPU, RAM (GB), OS, Region | Verify column coverage |
| L4L Pricing — PAYG | Azure VM SKU matching at PAYG rates; UK South + UK West columns | Verify both regions present |
| L4L Pricing — 3yr RI | Same SKUs at 3-year Reserved Instance rates | Verify 3yr (not just 1yr) |
| Optimised Pricing — PAYG | Right-sized based on utilisation P95 data; PAYG | Verify utilisation column feeds this |
| Optimised Pricing — 3yr RI | Right-sized at 3-year RI rates | **This is the headline recommendation number** |
| AHB Overlay | Windows Server AHB saving (row-level); SQL Server AHB saving | Verify AHB columns exist |
| Summary | Side-by-side: L4L PAYG vs L4L 3yr RI vs Optimised 3yr RI vs Optimised 3yr RI + AHB | The output that feeds the business case |
| Storage | Managed disk / Blob / Files cost by tier | Verify storage is not rolled into VM cost |

### Key Column Requirements (VM rows)

Each VM row must have:

| Column | Purpose |
| --- | --- |
| VM Name / ID | From discovery inventory |
| vCPU (current) | Input from discovery |
| RAM GB (current) | Input from discovery |
| Peak CPU % (P95) | From utilisation data — drives right-sizing |
| Average CPU % | Context for right-sizing |
| Peak RAM % (P95) | From utilisation data |
| OS | Windows / Linux — determines AHB eligibility |
| SQL Server licence | Yes/No — determines SQL AHB eligibility |
| Azure VM SKU (L4L) | Auto-selected or manually mapped |
| Azure VM SKU (Optimised) | Right-sized SKU |
| PAYG Rate (monthly) | From Azure pricing API or Calculator |
| 3yr RI Rate (monthly) | Pre-paid or monthly equivalent |
| AHB saving (if applicable) | Windows AHB saving per VM per month |
| Region | UK South / UK West / specify |
| Monthly cost (L4L PAYG) | Calculated |
| Monthly cost (Optimised 3yr RI + AHB) | **The headline output column** |

### Validation Against Current Rates

Azure pricing changes quarterly. Before using this template on a live engagement:

1. Open [azure.microsoft.com/pricing/calculator](https://azure.microsoft.com/pricing/calculator)
2. Check the Dsv5 and Esv5 series pricing for UK South — these are the most common CRA VM families
3. Verify the template rates match within ±5%
4. Update the rate source date cell (should be visible in the Summary tab header)

**Reference files:** `Examples/azure/` — 10 assessment examples from prior engagements. Compare formula structures.

---

## 4B.3 — AWS Evaluation Template (`aws-evaluation.xlsx`)

### Required Tab Structure

| Tab Name | Purpose | Status to Verify |
| --- | --- | --- |
| Instructions | Who fills this in, when, how | Add if missing |
| VM Inventory Input | Same as Azure template — paste from discovery | Verify shared input format |
| L4L Pricing — On-Demand | EC2 On-Demand rates; eu-west-2 (London) primary | Verify London region |
| L4L Pricing — 3yr RI (No Upfront) | 3-year Reserved Instance, no upfront payment option | Verify 3yr present |
| L4L Pricing — 3yr RI (All Upfront) | All-upfront RI (lowest effective rate) | Add if missing — often the most competitive number |
| L4L Pricing — Savings Plans | Compute Savings Plans (more flexible than RI) | Add if missing |
| Optimised — 3yr RI | Right-sized + 3yr RI | Verify |
| Migration Evaluator Comparison | Side-by-side vs. AWS Migration Evaluator output | Add column if AWS ME was run |
| Summary | On-Demand vs 3yr RI vs Savings Plans vs Optimised | Verify all 4 columns |

### AWS-Specific Fields

| Column | Purpose | Notes |
| --- | --- | --- |
| EC2 Instance Type (L4L) | e.g., m6i.xlarge | Mapped from vCPU/RAM |
| EC2 Instance Type (Optimised) | Right-sized | |
| Pricing Model | On-Demand / RI / Savings Plan | |
| Region | eu-west-2 primary; eu-central-1 DR | |
| SQL Server on RDS? | If SQL Server, is RDS a viable path? | Flags replatform opportunity |
| BYOL eligible? | Oracle / SQL Server BYOL | |

**Reference files:** `Examples/aws/aws-mpa-pricing-example-region-*.xlsx` — three MPA pricing examples from the DMG engagement (Frankfurt, Ireland, London). These are the closest to real completed templates in the repo. Cross-reference formula structure.

---

## 4B.4 — GCP Evaluation Template (`gcp-evaluation.xlsx`)

### Required Tab Structure

| Tab Name | Purpose | Status to Verify |
| --- | --- | --- |
| Instructions | Who fills this in, when, how | Add if missing |
| VM Inventory Input | Shared input from discovery | Verify consistent with Azure/AWS tabs |
| L4L Pricing — On-Demand | GCE On-Demand; europe-west2 (London) | Verify London region |
| L4L Pricing — 3yr CUD | 3-year Committed Use Discount | Verify CUD (not just 1yr) |
| Optimised — 3yr CUD | Right-sized + 3yr CUD | |
| Machine Family Mapping | N-series / M-series / C-series / E2 / Z3 mapping logic | Verify all 5 families present |
| Summary | On-Demand vs 3yr CUD vs Optimised | |

### GCP Machine Family Mapping (reference)

| Family | Use Case | CRA Mapping Rule |
| --- | --- | --- |
| N2 / N2D | General purpose (default) | Most VMs map here |
| M2 / M3 | High-memory (>8 GB RAM per vCPU) | Oracle, SAP, large DB |
| C2 / C3 | Compute-optimised (high vCPU, low RAM) | Batch processing, HPC |
| E2 | Economy / dev-test | Non-production workloads |
| Z3 | Storage-optimised (high local SSD) | Data warehousing |

> Verify the GCP template has a column that maps each VM to the correct machine family before pricing. Wrong family mapping inflates or deflates the GCP cost.

**Reference files:** `docs/GOOGLE-PSO-ALIGNMENT.md` Section 6 — GCE machine family mapping table.

---

## 4B.5 — On-Premises Status Quo Tab (add to `business-case-tco-roi.xlsx`)

**This tab is currently missing from most TCO templates. It is a named SOW deliverable.**

The on-premises status quo cost must be modelled before the cloud comparison is meaningful. Without it, the "39% saving" headline has no denominator.

### Tab Name: `On-Prem Status Quo`

### Required Columns / Rows

| Cost Category | Annual Cost (£/$) | Notes |
| --- | --- | --- |
| **Hardware** | | |
| Server lease / refresh cycle | [X] | Amortised over refresh cycle (typically 5yr) |
| Storage (SAN, NAS) | [X] | |
| Network (DC switching, cabling) | [X] | |
| **Data Centre Facilities** | | |
| Co-location fees (rack/cage) | [X] | |
| Power and cooling | [X] | Typically 30–50% on top of power draw |
| Physical security | [X] | |
| **Software & Licences** | | |
| Hypervisor (VMware vSphere EA) | [X] | Often the largest single licence cost |
| Operating system (Windows Server) | [X] | Note EoL servers requiring ESU |
| SQL Server on-prem licence | [X] | SA cost if under Software Assurance |
| Oracle on-prem licence | [X] | Annual support (22% of licence value) |
| Third-party software (anti-virus, backup, monitoring) | [X] | |
| **Operations** | | |
| DC operations staff | [X] | FTE cost attributed to DC ops |
| Hardware maintenance contracts | [X] | Typically 8–12% of hardware value/yr |
| Backup media and off-site storage | [X] | |
| **Subtotals** | | |
| Total Annual On-Prem Cost | **[X]** | This is the denominator for all savings % |
| 3-Year On-Prem Cost (status quo) | **[X]** | Assume flat — adjust for refresh cycles |

### Source for Data

- Hardware: customer asset register / CMDB / co-location invoices
- Licences: customer software licence inventory (ask during Phase 1 stakeholder interviews)
- VMware: VMware portal or EA summary
- Co-location: data centre invoices
- Staff: estimate from customer IT org chart and FTE costs (ask finance)

> **Lesson from DMG Media UK:** The on-premises baseline was initially underestimated because the VMware licence cost (£XX/yr) was not included. Always ask specifically about hypervisor licence costs — customers often treat this as "infrastructure" not "software" and miss it in the initial cost estimate.

---

## 4B.6 — Year 1 Dual-Running Forecast Tab (add to `business-case-tco-roi.xlsx`)

**Year 1 is always the most expensive year of a cloud migration. Failing to model it creates budget shock.**

### Tab Name: `Year 1 Dual-Running`

### Required Structure

| Cost Component | Q1 | Q2 | Q3 | Q4 | Year 1 Total |
| --- | --- | --- | --- | --- | --- |
| **On-Premises (remaining — not yet decommissioned)** | | | | | |
| Data centre co-location | [X] | [X] | [X] | [X] | [X] |
| VMware licences (still running on-prem) | [X] | [X] | [X] | [X] | [X] |
| Hardware maintenance | [X] | [X] | [X] | [X] | [X] |
| Staff (DC operations) | [X] | [X] | [X] | [X] | [X] |
| **Cloud Costs (workloads migrated)** | | | | | |
| Wave 1 cloud spend (from Q2 onward) | — | [X] | [X] | [X] | [X] |
| Wave 2 cloud spend (from Q3 onward) | — | — | [X] | [X] | [X] |
| Wave 3 cloud spend (from Q4 onward) | — | — | — | [X] | [X] |
| **Migration Costs (one-off)** | | | | | |
| Migration tooling licences | [X] | [X] | — | — | [X] |
| Professional services (Rackspace Part 2) | [X] | [X] | [X] | [X] | [X] |
| Customer internal resource (project team) | [X] | [X] | [X] | [X] | [X] |
| **Partner Funding Offset** | | | | | |
| AMM / MAP / PSO funded services credit | ([X]) | ([X]) | — | — | ([X]) |
| **Year 1 Net Total** | | | | | **[X]** |

### Linking to Wave Plan

The Year 1 dual-running tab must link to the migration wave plan (`Templates/04-planning/migration-wave-planner.xlsx`). The key input is: which waves complete in which quarter. Until the wave plan is finalised in Phase 4, use the indicative wave schedule from the Phase 3 playback.

---

## 4B.7 — Licensing Overlay Tab (add to `business-case-tco-roi.xlsx`)

**Oracle was flagged as "significant cost, core to the estate" in the SOW. This tab is mandatory when Oracle, SQL Server, or third-party licences are in scope.**

### Tab Name: `Licensing Overlay`

### Required Structure

**Windows Server — Azure Hybrid Benefit**

| Column | Content |
| --- | --- |
| VM Name | From inventory |
| Windows Server Version | 2012 / 2016 / 2019 / 2022 |
| Licence Status | SA (AHB eligible) / PAYG / OEM |
| AHB Eligible? | Yes / No |
| PAYG Monthly Cost | From Azure eval template |
| AHB Monthly Cost | 0 (Windows is free with AHB) |
| AHB Monthly Saving | = PAYG − AHB |

**SQL Server — Azure Hybrid Benefit**

| Column | Content |
| --- | --- |
| Instance Name | From inventory |
| SQL Server Edition | Standard / Enterprise / Developer |
| Licence Status | SA (AHB eligible) / PAYG |
| AHB Eligible? | Yes / No |
| Azure SQL service | SQL VM / Managed Instance / Azure SQL DB |
| PAYG Monthly Cost | From Azure pricing |
| AHB Monthly Cost | |
| AHB Monthly Saving | |

**Oracle**

| Column | Content |
| --- | --- |
| Cluster / Instance Name | From inventory |
| Oracle Edition | SE2 / EE / RAC |
| Processor licences in use | Count (2 vCPUs = 1 processor for most workloads) |
| Current annual support cost | 22% of licence value |
| Cloud deployment model | BYOL on VM / RDS / Exadata / OCI |
| Cloud annual licence cost | BYOL = same as on-prem; varies by deployment |
| Delta vs. on-prem | Saving or premium |

**Summary Row (all licence types)**

| Category | On-Prem Annual | Cloud Annual (PAYG) | Cloud Annual (AHB/BYOL) | Net Saving |
| --- | --- | --- | --- | --- |
| Windows Server | [X] | [X] | [X] | [X] |
| SQL Server | [X] | [X] | [X] | [X] |
| Oracle | [X] | [X] | [X] | [X] |
| Other (VMware, Redis, etc.) | [X] | [X] | [X] | [X] |
| **Total** | **[X]** | **[X]** | **[X]** | **[X]** |

---

## 4B.8 — Partner Commercial Overlay Tab (add to `business-case-tco-roi.xlsx`)

### Tab Name: `Partner Credits`

| Programme | Provider | Eligibility Status | Estimated Funded Value | Delivery Terms | Net Impact on Year 1 |
| --- | --- | --- | --- | --- | --- |
| Azure Migration and Modernisation (AMM) | Microsoft | [Eligible / TBC / Not eligible] | £/$ [X]–[Y] | Funded professional services; not cash | Reduces Part 2 PS cost by [£X] |
| AWS Migration Acceleration Programme (MAP) | AWS | [Eligible / TBC] | £/$ [X]–[Y] | Mobilize phase funding + migration credits | |
| GCP RAMP / PSO co-delivery | Google | [Eligible / TBC] | £/$ [X]–[Y] | PSO co-delivery hours | |
| Azure Hybrid Benefit (already in Licensing tab) | Microsoft | Per-VM eligibility in Licensing tab | Calculated | Licence portability | |
| 3-year RI / CUD (already in eval templates) | Cloud provider | Committed spend | Calculated in eval templates | Compute commitment | |

### Three-Year Net Cost Summary (the final board number)

| Scenario | Year 1 | Year 2 | Year 3 | 3-Year Total | vs. On-Prem |
| --- | --- | --- | --- | --- | --- |
| On-premises (status quo) | [X] | [X] | [X] | [X] | Baseline |
| Cloud — L4L PAYG | [X] | [X] | [X] | [X] | [+/-X%] |
| Cloud — Optimised 3yr RI/CUD | [X] | [X] | [X] | [X] | [+/-X%] |
| Cloud — Optimised + AHB/BYOL | [X] | [X] | [X] | [X] | [+/-X%] |
| Cloud — Optimised + AHB + Partner Credits | **[X]** | **[X]** | **[X]** | **[X]** | **[+/-X%]** |

> The bottom row is the headline customer-facing number. It should appear on the executive summary slide and in the Part 2 Entry Point.

---

## 4B.9 — Pricing Validation (all templates)

Before using these templates on a live engagement, validate the pricing against current published rates:

| Cloud | Pricing Source | Frequency to Validate |
| --- | --- | --- |
| Azure | [azure.microsoft.com/pricing/calculator](https://azure.microsoft.com/pricing/calculator) | Before each engagement |
| AWS | [aws.amazon.com/pricing](https://aws.amazon.com/pricing) | Before each engagement |
| GCP | [cloud.google.com/products/calculator](https://cloud.google.com/products/calculator) | Before each engagement |

**Key SKUs to validate (most common in CRA engagements):**

| SKU | Cloud | Region | Check |
| --- | --- | --- | --- |
| D4s v5 (4 vCPU, 16 GB) | Azure | UK South | General purpose — most common mapping |
| E4s v5 (4 vCPU, 32 GB) | Azure | UK South | Memory-optimised — SQL Server |
| m6i.xlarge (4 vCPU, 16 GB) | AWS | eu-west-2 | General purpose |
| r6i.xlarge (4 vCPU, 32 GB) | AWS | eu-west-2 | Memory-optimised |
| n2-standard-4 (4 vCPU, 16 GB) | GCP | europe-west2 | General purpose |
| n2-highmem-4 (4 vCPU, 32 GB) | GCP | europe-west2 | Memory-optimised |

---

*Template audit spec for CRA Framework v2.0 — Rackspace Cloud Solutions Architecture*  
*Reference: SOW analysis from DMG Media UK CRA Part 1, February–May 2026*
