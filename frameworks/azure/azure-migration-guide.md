# Azure Migration Guide

**Version:** 2.0  
**Authors:** Microsoft Expert Azure Cloud Architecture Team  
**Aligned To:** Microsoft Cloud Adoption Framework (CAF) for Azure

---

## Overview

This guide provides a structured, phased approach to migrating workloads to Microsoft Azure. It is aligned with the **Microsoft Cloud Adoption Framework (CAF)** and the **Azure Well-Architected Framework (WAF)**, and is designed for use by enterprise architecture teams, project managers, and delivery partners.

---

## Azure Migration Phases

### Phase 1: Strategy

**Objective:** Define the motivations, outcomes, and business justification for migrating to Azure.

**Key Activities:**
- Document cloud adoption motivations (cost savings, agility, innovation, BCDR, datacenter exit)
- Define measurable business outcomes (e.g., 30% infrastructure cost reduction, 50% faster deployment)
- Build a cloud business case with TCO analysis using the [Azure TCO Calculator](https://azure.microsoft.com/pricing/tco/calculator/)
- Identify executive sponsor and Cloud Adoption Team members
- Align to relevant compliance requirements (GDPR, ISO 27001, HIPAA, FedRAMP)
- ✅ **Run Microsoft SMART Assessment** — complete the [Strategic Migration Assessment and Readiness Tool](https://learn.microsoft.com/en-us/assessments/Strategic-Migration-Assessment/) to establish a baseline readiness score across all 10 SMART categories. Use the accelerator's [SMART Assessment Guide](../../assessments/smart-migration-assessment.md) for facilitated deep-dive discovery.

**Deliverables:**
- Cloud Strategy Document
- Business Case & ROI Model
- Executive Stakeholder Alignment Sign-off
- **SMART Readiness Index (SRI) — baseline scores for all 10 categories**

---

### Phase 2: Plan

**Objective:** Build the cloud adoption plan covering portfolio rationalization and resource planning.

**Key Activities:**
- Complete full application portfolio inventory (use [Azure Migrate](https://azure.microsoft.com/products/azure-migrate/) for discovery)
- ✅ **Address SMART Category 3 (Discovery & Assessment):** Deploy Azure Migrate appliances; run dependency analysis; produce rationalization register. See [SMART Category 3 guidance](../../assessments/smart-migration-assessment.md#category-3-discovery--assessment).
- Apply the **5 Rs of Rationalization**:
  - **Rehost** (Lift & Shift) — Move as-is to Azure IaaS
  - **Refactor** — Minor code changes to use PaaS (e.g., Azure App Service, Azure SQL)
  - **Rearchitect** — Restructure for cloud-native (containers, microservices)
  - **Rebuild** — Redevelop cloud-native from scratch
  - **Replace** — Move to SaaS alternatives (Microsoft 365, Dynamics 365)
- Prioritize migration waves based on business value and complexity
- Define Azure subscription and management group hierarchy
- Identify Azure regions (primary + DR) based on data sovereignty requirements
- Develop skills readiness plan and identify training (Microsoft Learn, certifications)

**Deliverables:**
- Application Portfolio Rationalization Report
- Migration Wave Plan
- Azure Subscription Design
- Skills Readiness Plan
- **SMART Categories 3, 4, 5, 6 scores updated (post-Plan phase)**

---

### Phase 3: Ready (Landing Zone)

**Objective:** Build the Azure landing zone — a scalable, secure, governed foundation.

**Landing Zone Architecture (Azure CAF Enterprise Scale):**

```
Management Group Hierarchy
├── Root Management Group
│   ├── Platform
│   │   ├── Identity (AAD, AD DS)
│   │   ├── Management (Log Analytics, Security Center)
│   │   └── Connectivity (Hub VNet, ExpressRoute/VPN, Firewall)
│   └── Landing Zones
│       ├── Corp (Connectivity to On-Premises)
│       └── Online (Internet-facing)
│           ├── Production
│           ├── Non-Production
│           └── Sandbox
```

**Key Activities:**
- Deploy Azure landing zone using [Azure Landing Zone Accelerator](https://aka.ms/alz)
- Configure Azure Active Directory (Entra ID) tenant settings
- Establish hub-spoke network topology with Azure Virtual WAN or Hub VNet
- Configure Azure Firewall, DDoS Protection, Private DNS
- Set up Azure Monitor, Log Analytics Workspace, Microsoft Defender for Cloud
- Apply Azure Policy initiatives (CIS, NIST, ISO 27001 compliance)
- Establish naming conventions and tagging standards

**Reference Architecture:** [Azure Hub-Spoke Network Topology](https://learn.microsoft.com/azure/architecture/reference-architectures/hybrid-networking/hub-spoke)

**Deliverables:**
- Azure Landing Zone (deployed via Terraform/Bicep)
- Network Architecture Diagram
- Azure Policy Baseline
- RBAC Role Assignments Matrix
- **SMART Category 7 (Landing Zone) score ≥ 80 before Wave 1 migration begins**

---

### Phase 4: Migrate

**Objective:** Execute migration waves, validate, and optimize.

**Migration Tools:**

| Workload Type | Recommended Tool |
|---|---|
| VMs (VMware/Hyper-V/Physical) | Azure Migrate (Server Migration) |
| SQL Server Databases | Azure Database Migration Service (DMS) |
| Web Applications | Azure App Service Migration Assistant |
| Data / File Shares | Azure Data Box, AzCopy, Storage Mover |
| SAP | SAP on Azure Migration Guide |
| Mainframe | Azure Mainframe Migration Program |

**Migration Wave Execution:**
1. **Pre-migration:** Replicate & validate in Azure (test failover)
2. **Migration window:** Execute cutover (minimize downtime)
3. **Post-migration:** Validate functionality, performance, and connectivity
4. **Decommission:** Remove on-premises workload after validation period

**Key Considerations:**
- Use [Azure Site Recovery](https://azure.microsoft.com/products/site-recovery/) for lift-and-shift VM migration
- Leverage [Azure Database Migration Service](https://azure.microsoft.com/products/database-migration/) for SQL workloads
- Apply network security groups (NSGs) and application security groups (ASGs) from day one
- Validate backup policies using [Azure Backup](https://azure.microsoft.com/products/backup/)

**Deliverables:**
- Migration Wave Runbook
- Go/No-Go Checklist (per wave)
- Post-Migration Validation Report
- **SMART Category 8 (Migration Execution) score updated post-Wave 1**

---

### Phase 5: Govern & Manage

**Objective:** Establish ongoing governance, operations, and continuous optimization.

**Azure Governance Tools:**

| Tool | Purpose |
|---|---|
| Azure Policy | Enforce compliance standards automatically |
| Azure Blueprints (now Policy) | Deploy governance packages |
| Microsoft Defender for Cloud | Security posture management & threat protection |
| Azure Cost Management + Billing | FinOps, budgets, cost allocation |
| Azure Monitor | Unified monitoring (metrics, logs, alerts) |
| Azure Advisor | Right-sizing and optimization recommendations |

**Azure Well-Architected Framework Pillars:**
1. **Reliability** — Design for failure; use availability zones, geo-redundant storage, Traffic Manager
2. **Security** — Zero Trust; Microsoft Entra ID, Defender for Cloud, Key Vault, Private Endpoints
3. **Cost Optimization** — Reserved Instances, Spot VMs, Azure Hybrid Benefit, auto-scaling
4. **Operational Excellence** — IaC (Bicep/Terraform), Azure DevOps/GitHub Actions, Azure Monitor
5. **Performance Efficiency** — Auto-scale, CDN, Azure Front Door, caching (Redis)

**Deliverables:**
- Cloud Operations Runbook
- Monthly Cost Optimization Report
- Well-Architected Review Report
- **SMART Categories 9 (Governance) and 10 (Management) scores ≥ 80 — target for full program completion**

---

## SMART Gate Criteria per Migration Phase

The following table defines the minimum SMART category scores required before advancing to each phase:

| Migration Phase | SMART Categories | Minimum Score | Gate Check |
|---|---|---|---|
| Advance to **Plan** | Business Strategy (1), Business Case (4) | ≥ 60 | Phase 1 gate |
| Advance to **Ready** | Discovery & Assessment (3), Migration Plan (5), Technical Skilling (6), Partner Support (2) | ≥ 60 | Phase 2 gate |
| Advance to **Migrate** (Wave 1) | Landing Zone (7) | ≥ 80 | Phase 3 gate |
| Advance to **Migrate** (at-scale) | Migration Execution (8) | ≥ 60 | Post-Wave 1 gate |
| **Program Complete** | Governance (9), Management (10) | ≥ 80 | Final gate |

---

## Azure Reference Architectures

| Scenario | Reference Architecture |
|---|---|
| Highly available web application | [Multi-region web app](https://learn.microsoft.com/azure/architecture/reference-architectures/app-service-web-app/multi-region) |
| Microservices on AKS | [AKS microservices](https://learn.microsoft.com/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices) |
| Event-driven serverless | [Serverless event processing](https://learn.microsoft.com/azure/architecture/reference-architectures/serverless/event-processing) |
| Analytics data platform | [Azure Analytics end-to-end](https://learn.microsoft.com/azure/architecture/example-scenario/dataplate2e/data-platform-end-to-end) |
| Hybrid network | [Hub-spoke with ExpressRoute](https://learn.microsoft.com/azure/architecture/reference-architectures/hybrid-networking/expressroute) |

---

## Azure Certifications Roadmap

| Role | Recommended Certifications |
|---|---|
| Cloud Administrator | AZ-900 → AZ-104 |
| Cloud Architect | AZ-900 → AZ-104 → AZ-305 |
| Data Engineer | DP-900 → DP-203 |
| AI Engineer | AI-900 → AI-102 |
| Security Engineer | SC-900 → AZ-500 → SC-100 |
| DevOps Engineer | AZ-400 |

---

*See also: [SMART Migration Assessment](../../assessments/smart-migration-assessment.md) | [Multi-Cloud Strategy](../multi-cloud/multi-cloud-strategy.md) | [Security Framework](../../security/security-compliance-framework.md) | [Governance Framework](../../governance/cloud-governance-framework.md)*
