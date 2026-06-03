# Case Study: DMG Media UK — Cloud Readiness Assessment

**Client:** DMG Media UK (part of DMGT — Daily Mail Group Trust)  
**Industry:** Media & Entertainment / Digital Publishing  
**Engagement:** Cloud Readiness Assessment Phase 1 — February–June 2026  
**Delivered by:** Rackspace Technology — Cloud Solutions Architecture  
**Framework version:** CRA v1.0  
**Outcome:** Azure primary hyperscaler recommendation

---

## Executive Summary

DMG Media UK is one of the UK's largest digital media groups, operating major consumer brands across news, lifestyle, and entertainment. Facing an aging on-premises VMware estate across two UK data centres, DMG Media engaged Rackspace to conduct a structured cloud readiness assessment to determine migration feasibility, select a primary hyperscaler, and produce a board-ready business case.

Rackspace applied the Cloud Readiness Accelerator (CRA) framework across all four phases. The engagement surfaced a VMware estate **57% larger than initially scoped**, identified 224 active VMs running end-of-life operating systems, and produced a full three-way hyperscaler evaluation (AWS, Azure, GCP). Azure was selected as the primary recommendation, with UK South as the primary region.

---

## Client Profile

| Attribute | Detail |
|---|---|
| Organisation | DMG Media UK (Daily Mail Group Trust) |
| Industry | Digital Media & Entertainment |
| Primary locations | Slough (UK), Reading (UK), with satellite sites in Sydney and New York |
| Infrastructure model | On-premises VMware across two data centres |
| Virtualisation platform | VMware vSphere — 10 vCenter instances |
| Discovery tool | GCP Migration Center (europe-west4) |

---

## Business Challenge

DMG Media's on-premises VMware estate had grown organically over many years. The key business drivers for cloud assessment were:

- **VMware estate cost shock**: The Broadcom acquisition of VMware eliminated perpetual licensing for vSphere and vSAN; DMG faced a 3–5× increase in licensing costs at the next renewal cycle under subscription-only pricing. This was the primary commercial trigger for the engagement — not a discretionary cloud strategy review.
- **Licence and hardware refresh risk**: End-of-life VMware licensing and ageing physical infrastructure in both Slough and Reading data centres
- **Operating system debt**: A significant portion of the estate running past end-of-support operating systems, creating compliance and security exposure
- **Scalability constraints**: Media workloads with spiky traffic patterns (breaking news, major events) poorly suited to fixed on-premises capacity
- **Cost visibility**: Limited ability to attribute infrastructure costs to individual products and brands
- **Cloud capability gap**: Leadership required a structured, vendor-neutral assessment before committing to a hyperscaler — internal capability to do this was not available at the required pace

The organisation needed a hyperscaler recommendation backed by real TCO modelling and a formal readiness assessment — not a vendor-supplied quick assessment — to achieve board and group-level sign-off.

---

## Discovery Phase Findings

Discovery was executed using GCP Migration Center, providing a full VMware inventory across all 10 vCenter instances.

### Estate Scale

| Metric | Value |
|---|---|
| Total VMware VMs discovered | 4,212 |
| Active non-VDI VMs | 3,617 |
| SoW scope | 2,300 VMs |
| **Scope variance** | **+57% above SoW** |
| vCPU cores | 18,319 |
| Total memory | ~57 TB |
| Total storage (allocated) | 764 TB |
| Storage utilisation | 46% |
| Primary locations | Slough 65%, Reading 33% |

The scope variance — 1,317 VMs above the Statement of Work — was a significant discovery finding. A scope refinement workshop was required with DMG stakeholders to establish the actual migration candidate list, separate from decommission and retain-on-premises workloads.

### Infrastructure Complexity

| Complexity Factor | Detail |
|---|---|
| Network environments | 2 isolated network zones, each requiring separate discovery execution |
| OS diversity | 40+ distinct operating systems identified |
| End-of-life OS risk | 224 active VMs on unsupported OS (RHEL 5/6/7, Solaris 10, Windows Server 2008) |
| Legacy OS requiring special handling | 23 production Solaris 10 VMs — no native cloud equivalent |
| Database footprint | ~343 VMs with database workloads identified from naming patterns |

### Data Tier Profile

| Technology | VMs | Notes |
|---|---|---|
| Redis (caching) | 263 | Distributed caching across ~47 application prefixes |
| MS SQL Server | 35 | Windows Server 2019/2022; up to 17 TB per instance |
| MySQL | 13 | 4 high-memory instances (128–258 GB RAM) |
| Oracle RAC | 12 | Clustered — significant lift complexity |
| Kafka / RabbitMQ / ActiveMQ | 10 | Event streaming and messaging infrastructure |
| PostgreSQL | 5 | |
| MongoDB | 3 | Video platform workloads |

The Redis footprint (263 VMs across 47 application stacks) indicated a heavily distributed, microservices-oriented architecture. The Oracle RAC cluster and high-memory MySQL instances were identified as the heaviest migration challenges requiring specialist planning.

### Cloud Compatibility (GCP Migration Center Output)

| Platform | Compatible VMs | % |
|---|---|---|
| Google Compute Engine (GCE) | 3,947 | 93.7% |
| Google Cloud VMware Engine (GCVE) | 4,212 | 100% |
| Google Kubernetes Engine (GKE) — eligible | 3,366 | 79.9% |

265 VMs could not run natively on any cloud's standard compute and required either lift-and-shift via VMware-on-cloud (GCVE/AVS) or OS/app refactoring. The 23 production Solaris VMs were the highest-risk items, with no cloud-native equivalent.

---

## Hyperscaler Evaluation

All three major hyperscalers were formally evaluated. Each submitted pricing responses covering multiple European regions. Rackspace produced independent cost models and scored each against the CRA hyperscaler decision matrix.

### Regions Assessed per Hyperscaler

| Hyperscaler | Regions Evaluated |
|---|---|
| **Azure** | UK South, North Europe (Ireland), Germany West Central |
| **AWS** | London (eu-west-2), Ireland (eu-west-1), Frankfurt (eu-central-1) |
| **GCP** | europe-west2, europe-west1, europe-west3 (all groups) |

### Evaluation Dimensions

Each hyperscaler was scored across five dimensions using the CRA evaluation framework:

| Dimension | Weighting |
|---|---|
| Technical fit (workload compatibility, service mapping) | 30% |
| Commercial (TCO, RI/CUD savings, bring-your-own-licence) | 25% |
| Alliance & funding eligibility (AMM, MAP, PSO) | 15% |
| Data residency & compliance (UK/EU requirements) | 20% |
| Strategic alignment (roadmap, support model, partner ecosystem) | 10% |

### Pricing Model Variants

For each hyperscaler, the following pricing models were modelled independently:

| Model | Description |
|---|---|
| PAYG / On-Demand | Baseline, no commitment |
| 3-Year Reserved Instances / Committed Use Discounts | Committed capacity pricing |
| Azure Hybrid Benefit (Azure only) | Bring-your-own Windows Server and SQL Server licences |
| Like-for-like (LKL) vs right-sized | Current spec vs. cloud-optimised spec |

---

## Outcome: Azure Primary Recommendation

**Primary recommendation: Microsoft Azure — UK South (primary), North Europe (DR/secondary)**

### Key Rationale

1. **UK South data residency**: DMG Media's regulatory and editorial sensitivity requirements favour UK-domiciled data. Azure UK South is the strongest UK-native region with the broadest PaaS service availability.

2. **Windows and SQL Server licence portability and Extended Security Updates**: A significant portion of DMG's Windows Server and SQL Server estate qualifies for Azure Hybrid Benefit, producing material TCO reduction. Additionally, the 224 EoL VMs running Windows Server 2008 and SQL Server legacy versions qualify for **3 years of free Extended Security Updates (ESU) on Azure** — a saving not available on AWS or GCP, where ESU must be purchased separately from Microsoft. The combined AHB + ESU saving was a decisive factor in the Azure financial case at the board level.

3. **Media industry PaaS alignment**: Azure Media Services, Azure CDN (Akamai-backed), and Azure Front Door align directly with DMG's content delivery and video streaming requirements.

4. **Oracle and Solaris migration path**: For the 12-node Oracle RAC cluster, **Oracle Database@Azure** (Oracle Exadata Database Service deployed natively inside Azure datacenters, operated by Oracle and billed through Azure — a distinct product from the OCI/Azure network interconnect; GA in UK South and North Europe) is the primary migration path. It preserves Oracle licensing and eliminates the need for AVS for the Oracle workload specifically. **Azure VMware Solution (AVS)** is the correct path for the 23 Solaris 10 VMs and remaining VMware lift workloads (265 VMs total). These are distinct products and must be planned separately with different lead times and team involvement (Oracle Database@Azure requires 4–6 weeks to engage the Oracle and Microsoft Oracle practice teams).

5. **Microsoft AMM funding eligibility**: The engagement scope and TCO output qualified DMG for Microsoft Azure Migration and Modernisation (AMM) programme funding, directly reducing Rackspace engagement cost and strengthening the business case for board sign-off.

6. **Rackspace–Microsoft alliance**: Rackspace's Microsoft co-sell status enabled a co-branded delivery model with aligned support from Microsoft's UK field team, strengthening the client's confidence in the recommendation.

---

## CRA Framework Artifacts Used

| Framework Component | Artifact | Output |
|---|---|---|
| Discovery | GCP Migration Center + CRA infrastructure profiling template | 4,212-VM inventory with cloud fit analysis |
| Analysis | CRA readiness scoring (5 dimensions) | Per-zone and per-workload readiness scores |
| Evaluation | CRA hyperscaler decision matrix | Weighted 3-way score — Azure recommended |
| Evaluation | Azure PAYG/RI/AHB cost models (UK South, North Europe, Germany West Central) | 3-year TCO comparison across regions and models |
| Evaluation | AWS MPA pricing models (London, Ireland, Frankfurt) | AWS 3-year TCO comparison |
| Evaluation | GCP detailed pricing and TCO report | GCP 3-year TCO with consumption modelling |
| Evaluation | Business case TCO/ROI model | Board-ready NPV and payback period |
| Planning | Migration wave planner | Wave sequencing by complexity and risk |
| Planning | Risk register | Oracle RAC, Solaris, EoL OS, scope variance risks |
| Reporting | CRA executive summary template | CIO/board-ready 15-slide recommendation deck |
| Reporting | CRA phase 1 assessment report | Full 30-page written assessment |

---

## Key Lessons Learned — Framework Improvements

This engagement directly informed several CRA framework improvements now included in v1.0:

| Finding | Framework Update |
|---|---|
| SoW scope significantly underestimated actual VM count | Added scope validation worksheet to Discovery phase guide; recommend automated inventory before SoW is signed |
| Two isolated network zones required separate discovery runs | Discovery guide now explicitly covers multi-zone / network-segmented environments |
| Solaris and legacy OS VMs require GCVE/AVS — much more expensive than standard compute | Evaluation phase now includes explicit legacy OS remediation cost modelling |
| Redis at scale (263 VMs) indicates microservices architecture — containerisation opportunity | Analysis scoring now includes containerisation readiness dimension |
| Oracle RAC is the highest-complexity single workload type | Planning templates now include dedicated Oracle RAC migration playbook |
| AMM funding eligibility was not assessed at scoping — almost missed | Pre-engagement checklist now includes alliance funding eligibility screening |

---

## Reference Files in This Repository

The following anonymised output files from this engagement are included as reference examples:

| File | Location | Description |
|---|---|---|
| Azure PAYG like-for-like assessments | `Examples/azure/` | UK South, North Europe, Germany West Central — PAYG pricing |
| Azure 3-year RI + AHB assessments | `Examples/azure/` | UK South, North Europe, Germany West Central — reserved + hybrid benefit |
| Azure cost models summary | `Examples/azure/azure-assessment-cost-models-summary.xlsx` | Cross-region, cross-model comparison |
| AWS MPA pricing — 3 regions | `Examples/aws/` | London, Ireland, Frankfurt — full scope and no-DB variants |
| AWS business case decks | `Examples/aws/` | Lift & Shift, DB Refactoring, Storage Assessment |
| Hyperscaler decision matrix (completed) | `Examples/Azure Example -2/Hyperscaler_Decision_Matrix_Microsoft_Completed.xlsx` | Final weighted scoring across all three hyperscalers |

---

## Engagement Metrics

| Metric | Value |
|---|---|
| Discovery phase duration | 7 weeks total (3 weeks tooling setup + 4 weeks active data collection). The 4-week data collection window is the period cited in project status reports; the full Phase 1 duration including tooling stand-up and CAB-gated firewall changes was 7 weeks, consistent with the CRA v2.0 methodology. |
| VMs inventoried | 4,212 |
| Applications in scope (SoW) | 39 |
| Hyperscalers formally evaluated | 3 (AWS, Azure, GCP) |
| Pricing regions modelled | 9 (3 per hyperscaler) |
| Pricing model variants | 4 per hyperscaler (PAYG, 3yr RI, AHB, right-sized) |
| Framework templates used | 11 |
| Alliance funding identified | Microsoft AMM |

---

*Rackspace Technology — Cloud Solutions Architecture*  
*© 2026 Rackspace Technology. All rights reserved.*  
*Client information used with permission. Infrastructure data anonymised where appropriate.*
