# FinOps & Cloud Cost Optimization Framework

**Version:** 2.0  
**Authors:** Senior Cloud Architecture & FinOps Teams — Microsoft, AWS, Google Cloud  
**Aligned To:** FinOps Foundation Framework · Cloud Cost Optimization Best Practices

---

## Overview

**FinOps** (Financial Operations) is the practice of bringing financial accountability to the variable spend model of cloud computing. This framework provides a structured approach to cloud cost management across **Azure**, **AWS**, and **Google Cloud Platform**, enabling organizations to maximize business value from cloud investment.

---

## FinOps Maturity Model

| Phase | Description | Indicators |
|---|---|---|
| **1 – Crawl** | Basic visibility; limited optimization | Tags inconsistent, no chargeback, reactive cost reviews |
| **2 – Walk** | Consistent tagging, budgets set, showback in place | Monthly cost reviews, reserved capacity started |
| **3 – Run** | Full chargeback, automated optimization, FinOps team | Real-time dashboards, committed use >50%, continuous optimization |

---

## The FinOps Lifecycle

```
┌────────────────────────────────────────────┐
│                                            │
│   Inform → Optimize → Operate → [Repeat]   │
│                                            │
└────────────────────────────────────────────┘
```

### Phase 1: Inform (Visibility & Allocation)

**Goal:** Establish complete cost visibility and allocate spend to teams/products.

**Key Actions:**
- Enforce tagging standards (CostCenter, Owner, Project, Environment)
- Enable cloud cost exports to central data store
  - Azure: Cost Management export to Storage Account / Log Analytics
  - AWS: CUR (Cost and Usage Report) to S3 + Athena
  - GCP: Billing export to BigQuery
- Build cost dashboards (Power BI, Looker, Grafana)
- Implement showback reports by team, project, and environment

**Tools:**

| Tool | Cloud | Purpose |
|---|---|---|
| Azure Cost Management + Billing | Azure | Native cost visibility |
| AWS Cost Explorer + CUR | AWS | Native cost visibility |
| GCP Billing Reports + BigQuery | GCP | Native cost visibility |
| [Apptio Cloudability](https://www.apptio.com/) | Multi-cloud | Enterprise FinOps platform |
| [CloudHealth by VMware](https://cloudhealth.vmware.com/) | Multi-cloud | Multi-cloud cost management |
| [Spot.io](https://spot.io/) | Multi-cloud | Automated cost optimization |

---

### Phase 2: Optimize (Cost Reduction)

#### Right-Sizing

- Identify over-provisioned VMs using:
  - Azure Advisor compute recommendations
  - AWS Compute Optimizer
  - GCP Active Assist Recommender
- Target: >80% CPU/Memory utilization on production; resize or terminate underutilized resources
- Implement auto-scaling for variable workloads

**Right-Sizing Targets:**

| Resource | Action | Typical Savings |
|---|---|---|
| Over-provisioned VMs | Downsize to right-size SKU | 20–40% |
| Idle/stopped VMs | Terminate or schedule on/off | 100% (idle) |
| Unattached disks | Delete orphaned disks | 100% (orphaned) |
| Unattached public IPs | Release unused IPs | 100% (orphaned) |
| Unused load balancers | Decommission | 100% (unused) |
| Over-provisioned databases | Scale to appropriate tier | 20–50% |

#### Reserved Capacity / Committed Use

| Provider | Product | Discount vs. On-Demand |
|---|---|---|
| Azure | Reserved VM Instances (1yr) | ~40% |
| Azure | Reserved VM Instances (3yr) | ~60% |
| Azure | Azure Hybrid Benefit (Windows/SQL) | Additional 20–40% |
| Azure | Azure Savings Plan | ~15–40% |
| AWS | Reserved Instances — Standard 1yr No Upfront | ~40% |
| AWS | Reserved Instances — Standard 3yr No Upfront | ~60% |
| AWS | Savings Plans (Compute) | Up to 66% |
| GCP | Committed Use Discounts — 1yr | ~37% |
| GCP | Committed Use Discounts — 3yr | ~55% |
| GCP | Sustained Use Discounts | Automatic ~30% |

**Recommended Strategy:**
- Cover **60–70%** of stable baseline with Reserved/Committed capacity (1–3 year)
- Cover **15–20%** with Spot/Preemptible/Savings Plans for flexible workloads
- Keep **10–15%** on-demand for burst / unpredictable workloads

#### Spot / Preemptible / Spot VMs

| Cloud | Product | Use Cases |
|---|---|---|
| Azure | Azure Spot VMs | Batch, CI/CD, test workloads |
| AWS | EC2 Spot Instances | Big data, containerized apps, ML training |
| GCP | Spot VMs (Preemptible) | Dataflow, ML training, batch jobs |

**Typical Savings:** 60–90% vs. on-demand pricing

#### Storage Optimization

| Action | Azure | AWS | GCP |
|---|---|---|---|
| Lifecycle tiering | Blob tiering (Hot→Cool→Archive) | S3 Intelligent-Tiering / Lifecycle | GCS Autoclass / Lifecycle |
| Delete orphaned snapshots | Azure Snapshot cleanup | EBS Snapshot cleanup | GCE Snapshot cleanup |
| Compress/deduplicate | Azure Backup compression | AWS Backup deduplication | GCP Snapshot compression |
| Object storage vs. block | Use Blob/S3/GCS where possible | — | — |

#### Network Cost Optimization

- Minimize cross-region data transfer (design workloads co-located with consumers)
- Use Content Delivery Networks (CDN) for static content (Azure CDN, CloudFront, Cloud CDN)
- Use VPC Endpoints / Private Link / Private Service Connect (avoid NAT Gateway charges for S3/services)
- Compress data before transit
- Analyze egress costs monthly and optimize top data transfer paths

---

### Phase 3: Operate (Governance & Continuous Optimization)

**Budget Management:**

| Control | Description |
|---|---|
| Cloud budgets | Set monthly budgets per subscription/account/project |
| Alerts | Alert at 50%, 75%, 90%, 100% of budget |
| Anomaly detection | Enable native anomaly detection (Azure Cost Alerts, AWS Cost Anomaly Detection, GCP Budget Alerts) |
| Chargeback/showback | Allocate costs to teams via tags; integrate with ITSM (ServiceNow) |

**FinOps Review Cadence:**

| Review | Frequency | Participants |
|---|---|---|
| Cost anomaly review | Daily (automated alerts) | FinOps, Engineering |
| Cost optimization review | Monthly | FinOps, Engineering Leads, Finance |
| Reserved capacity review | Quarterly | FinOps, Cloud Architects, Finance |
| Annual cloud spend planning | Annually | CIO, CTO, CFO, FinOps |

---

## Cost Optimization Quick-Win Checklist

### Immediate Actions (Week 1–2)
- [ ] Enable cost exports and build a spend dashboard
- [ ] Identify top 10 cost drivers (compute, storage, network, data transfer)
- [ ] Identify and decommission idle/unused resources (VMs, disks, IPs, LBs)
- [ ] Enforce mandatory tagging via policy; alert on untagged resources

### Short-Term (Month 1–3)
- [ ] Purchase reserved instances/committed use discounts for stable workloads
- [ ] Implement auto-scaling for all compute workloads
- [ ] Move archive/cold data to low-cost storage tiers
- [ ] Implement auto-shutdown for dev/test environments (nights and weekends)

### Medium-Term (Month 3–6)
- [ ] Implement full showback/chargeback reporting
- [ ] Migrate eligible workloads to Spot/Preemptible instances
- [ ] Optimize data transfer costs (CDN, private endpoints, compression)
- [ ] Complete right-sizing for all production workloads (Advisor/Compute Optimizer recommendations)

### Ongoing
- [ ] Monthly FinOps review meetings
- [ ] Quarterly reserved capacity optimization
- [ ] Annual cloud spend forecasting and planning
- [ ] FinOps KPI dashboard reviewed by leadership

---

## Key FinOps KPIs

| KPI | Target |
|---|---|
| Reserved/Committed coverage | >60% of stable compute |
| Tagging compliance | >95% of resources tagged |
| Idle/unused resource ratio | <2% of total spend |
| Cost per business unit accuracy | 100% allocated |
| Month-over-month cost variance | <10% without planned change |
| Savings vs. on-demand baseline | >30% average discount |

---

*See also: [Governance Framework](../governance/cloud-governance-framework.md) | [Multi-Cloud Strategy](../frameworks/multi-cloud/multi-cloud-strategy.md) | [Azure Migration Guide](../frameworks/azure/azure-migration-guide.md)*
