# Google Cloud Migration Guide

**Version:** 2.0  
**Authors:** Google Cloud Pre-Sales Architecture Team  
**Aligned To:** Google Cloud Adoption Framework · CAMP (Cloud Architecture Migration Program)

---

## Overview

This guide provides a structured, phased approach to migrating workloads to **Google Cloud Platform (GCP)**. It aligns with the **Google Cloud Adoption Framework**, **Google Cloud Architecture Framework**, and **CAMP (Cloud Architecture Migration Program)**, and is designed for enterprise architects, project managers, and Google Cloud Partners.

---

## Google Cloud Migration Phases

### Phase 1: Assess

**Objective:** Understand the current environment, quantify business value, and define a migration strategy.

**Key Activities:**
- Complete current state assessment using [Stratozone](https://cloud.google.com/migrate/stratozone) or [Google Cloud Rapid Assessment & Migration Program (RAMP)](https://cloud.google.com/solutions/migration)
- Run Google Cloud Adoption Framework (GCAF) assessment across four themes:
  1. **Learn** — Cloud literacy and skills
  2. **Lead** — Sponsorship and organizational design
  3. **Scale** — Operating model, processes
  4. **Secure** — Security and compliance posture
- Build TCO analysis using [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator)
- Identify workload candidates and prioritize using GCAF **Migration Factory** approach
- Define Google Cloud region strategy (data residency, latency, compliance)

**Deliverables:**
- Google Cloud Readiness Assessment Report
- Application Portfolio Discovery (Stratozone export)
- Directional Business Case

---

### Phase 2: Plan (Foundation)

**Objective:** Build the Google Cloud landing zone (resource hierarchy) and establish the migration plan.

**Google Cloud Resource Hierarchy:**

```
Organization (Cloud Identity / Workspace)
├── Folders
│   ├── Platform
│   │   ├── Network Hub Project (VPC, Cloud Interconnect, VPN)
│   │   ├── Security Project (SIEM, Chronicle, SCC)
│   │   └── Shared Services Project (Artifact Registry, CI/CD)
│   └── Workloads
│       ├── Production
│       │   ├── App Project(s)
│       │   └── Data Project(s)
│       ├── Non-Production
│       └── Sandbox
```

**Key Activities:**
- Deploy Google Cloud landing zone using [Google Cloud Terraform modules](https://github.com/terraform-google-modules) or [Fabric FAST](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/blob/master/fast/README.md)
- Configure Cloud Identity / Google Workspace federation
- Establish Shared VPC hub-and-spoke or VPC peering topology
- Configure Cloud Interconnect (Dedicated or Partner) or Cloud VPN
- Enable Organization-level policies (Org Policies)
- Set up Security Command Center (SCC), Cloud Audit Logs, Chronicle SIEM
- Apply **Migration Strategies (5 Rs)**:
  - **Retire** — Decommission unused workloads
  - **Retain** — Keep on-premises temporarily
  - **Rehost** — Lift-and-shift to Compute Engine
  - **Replatform** — Move to GKE, Cloud SQL, App Engine
  - **Refactor** — Cloud-native redesign (Cloud Run, Anthos, Spanner)

**Deliverables:**
- Google Cloud Landing Zone (deployed)
- Network Architecture Design
- Org Policy Baseline
- IAM & RBAC Design (with Google Groups)
- Migration Wave Plan

---

### Phase 3: Migrate

**Objective:** Execute migration waves with minimal disruption.

**Google Cloud Migration Tools:**

| Workload Type | Recommended Tool |
|---|---|
| VMs (VMware/Hyper-V/AWS/Azure) | [Google Cloud Migrate to Virtual Machines](https://cloud.google.com/migrate/virtual-machines) |
| Databases | [Database Migration Service (DMS)](https://cloud.google.com/database-migration) |
| VMware Workloads | [Google Cloud VMware Engine (GCVE)](https://cloud.google.com/vmware-engine) |
| Data (large-scale) | [Transfer Appliance](https://cloud.google.com/transfer-appliance) or [Storage Transfer Service](https://cloud.google.com/storage-transfer) |
| Containers | [Anthos](https://cloud.google.com/anthos) / [Migrate to Containers](https://cloud.google.com/migrate/containers) |
| SAP | [SAP on Google Cloud](https://cloud.google.com/solutions/sap) |

**Migration Wave Execution:**
1. **Replication:** Install Migrate to VMs replication appliance; start continuous data replication
2. **Test clone:** Create test clones in GCP; validate application behavior
3. **Cutover:** Execute production cutover in maintenance window
4. **Post-migration:** Monitor with Cloud Monitoring, validate backups (Cloud Backup and DR)
5. **Decommission:** Remove source after stabilization period

**Key Considerations:**
- Use Migrate to Containers to modernize to GKE during migration (not just lift-and-shift)
- Use Google Cloud DMS for MySQL, PostgreSQL, Oracle, SQL Server migrations
- Apply VPC firewall rules and firewall policies from day one
- Configure Cloud Armor for web application protection
- Validate backup/DR using [Google Cloud Backup and DR](https://cloud.google.com/backup-disaster-recovery)

**Deliverables:**
- Migration Wave Runbooks
- Go/No-Go Checklist
- Post-Migration Validation Report

---

### Phase 4: Optimize & Innovate

**Objective:** Continuously optimize costs, performance, and leverage Google Cloud-native innovation.

**Google Cloud Operations & Governance Tooling:**

| Tool | Purpose |
|---|---|
| Resource Manager (Org Policies) | Policy enforcement |
| Security Command Center (SCC) | Security posture management |
| Chronicle SIEM | Threat detection and response |
| Cloud Audit Logs | API and activity audit trail |
| Cloud Monitoring + Cloud Logging | Unified observability |
| Error Reporting + Cloud Trace | APM and distributed tracing |
| Active Assist (Recommender) | Right-sizing and optimization |
| Cloud Billing Budgets & Alerts | Cost management |
| FinOps Hub | Cost attribution and showback |

**Google Cloud Architecture Framework Pillars:**
1. **Operational Excellence** — IaC (Terraform), Cloud Build CI/CD, SRE practices
2. **Security, Privacy & Compliance** — BeyondCorp Zero Trust, IAM, VPC SC, CMEK
3. **Reliability** — Multi-region active-active, Cloud Spanner, GKE autopilot, Cloud Armor
4. **Cost Optimization** — Committed Use Discounts (CUDs), Spot VMs, Cloud Storage lifecycle
5. **Performance** — Cloud CDN, Cloud Load Balancing, Memorystore, AlloyDB, Bigtable
6. **Sustainability** — Carbon-free energy regions, efficient instance families (T2D ARM)

**Google's Unique Differentiators:**
- **BigQuery** — Serverless, petabyte-scale analytics (no infrastructure to manage)
- **Vertex AI** — Unified AI/ML platform with Gemini integration
- **Cloud Spanner** — Globally distributed, strongly consistent relational database
- **Google Kubernetes Engine (GKE) Autopilot** — Fully managed Kubernetes
- **Anthos** — Hybrid and multi-cloud platform
- **Chronicle** — Cloud-native SIEM at Google scale

**Deliverables:**
- Cloud Operations Runbook
- Monthly Optimization Report
- Google Cloud Architecture Framework Review

---

## Google Cloud Reference Architectures

| Scenario | Reference |
|---|---|
| Enterprise web application | [GCP Reference Architectures](https://cloud.google.com/architecture) |
| Microservices on GKE | [GKE Architecture Best Practices](https://cloud.google.com/kubernetes-engine/docs/best-practices) |
| Serverless data processing | [Dataflow pipelines](https://cloud.google.com/dataflow/docs/guides/templates/provided-streaming) |
| Analytics & ML platform | [Google Cloud Analytics Platform](https://cloud.google.com/solutions/smart-analytics) |
| Hybrid connectivity | [Cloud Interconnect Reference Architecture](https://cloud.google.com/network-connectivity/docs/interconnect) |

---

## Google Cloud Certifications Roadmap

| Role | Recommended Certifications |
|---|---|
| Cloud Digital Leader | Cloud Digital Leader |
| Cloud Engineer | Associate Cloud Engineer → Professional Cloud Architect |
| Data Engineer | Professional Data Engineer |
| ML Engineer | Professional Machine Learning Engineer |
| Security Engineer | Professional Cloud Security Engineer |
| Network Engineer | Professional Cloud Network Engineer |
| DevOps Engineer | Professional Cloud DevOps Engineer |

---

*See also: [Multi-Cloud Strategy](../multi-cloud/multi-cloud-strategy.md) | [Security Framework](../../security/security-compliance-framework.md) | [AI/ML Readiness](../../ai-ml-readiness/ai-ml-readiness-framework.md)*
