# Microsoft SMART — Strategic Migration Assessment and Readiness Tool

**Version:** 2.0  
**Authors:** Microsoft Expert Azure Cloud Architecture Team · Senior Project Managers · Pre-Sales Architects  
**Source:** [Microsoft Learn — Strategic Migration Assessment](https://learn.microsoft.com/en-us/assessments/Strategic-Migration-Assessment/)  
**Aligned To:** Microsoft Cloud Adoption Framework (CAF) for Azure · Azure Well-Architected Framework

---

## Overview

The **Strategic Migration Assessment and Readiness Tool (SMART)** is Microsoft's official assessment for evaluating an organization's readiness to plan and execute a successful cloud migration to Azure. It generates a personalized readiness report with prioritized recommendations, resource links, and a curated action plan.

This document embeds the SMART framework into the Cloud Readiness Accelerator workflow so that practitioners — cloud architects, pre-sales engineers, project managers, and alliance partners — can run SMART-aligned assessments during customer engagements.

**How to use this document:**
1. Run the official [SMART online assessment](https://learn.microsoft.com/en-us/assessments/Strategic-Migration-Assessment/) with the customer (≈15 minutes) — this generates a Microsoft-curated report.
2. Use **this document** during a deeper discovery workshop (1–2 hours) to go beyond the online tool's questions, capture evidence, identify owners, and map findings to the accelerator's remediation frameworks.
3. Record results in the [Combined Readiness Scorecard](../templates/readiness-scorecard.md).

---

## SMART Categories Overview

SMART evaluates migration readiness across **10 categories**, each mapped to a CAF phase:

| # | SMART Category | CAF Phase | Accelerator Reference |
|---|---|---|---|
| 1 | Business Strategy | Strategy | [Multi-Cloud Strategy](../frameworks/multi-cloud/multi-cloud-strategy.md) |
| 2 | Partner Support | Plan | [Pre-Sales Playbook](../presales/presales-playbook.md) |
| 3 | Discovery & Assessment | Plan | [Azure Migration Guide — Phase 2](../frameworks/azure/azure-migration-guide.md) |
| 4 | Business Case | Strategy | [Pre-Sales Playbook — ROI Framework](../presales/presales-playbook.md) |
| 5 | Migration Plan | Plan | [Azure Migration Guide — Phase 2](../frameworks/azure/azure-migration-guide.md) |
| 6 | Technical Skilling | Plan / Ready | [Azure Migration Guide — Certifications](../frameworks/azure/azure-migration-guide.md) |
| 7 | Landing Zone | Ready | [Governance Framework — Landing Zone](../governance/cloud-governance-framework.md) |
| 8 | Migration Execution | Migrate | [Azure Migration Guide — Phase 4](../frameworks/azure/azure-migration-guide.md) |
| 9 | Governance | Govern | [Cloud Governance Framework](../governance/cloud-governance-framework.md) |
| 10 | Management | Manage | [Azure Migration Guide — Phase 5](../frameworks/azure/azure-migration-guide.md) |

---

## SMART Scoring Model

Each category is scored on a **0–100** scale, producing a SMART Readiness Index (SRI):

| Score Range | Readiness Level | Recommended Action |
|---|---|---|
| **0–39** | 🔴 Not Ready | Address foundational gaps before migration begins |
| **40–59** | 🟠 Developing | Targeted remediation plan required; defer migration of complex workloads |
| **60–79** | 🟡 Approaching Ready | Minor gaps; migration can proceed with mitigations in place |
| **80–100** | 🟢 Ready | Migration can proceed; maintain monitoring for regression |

> **Target:** All 10 categories should reach **≥60** before migrating Tier 1 workloads. Aim for **≥80** organization-wide before at-scale migration factory execution.

---

## Category 1: Business Strategy

**SMART Definition:** Alignment of cloud migration goals with overall organizational business objectives, with executive sponsorship and measured outcomes.

**Why It Matters:** Migrations without executive alignment and measured business outcomes are 3× more likely to stall or be cancelled (Source: McKinsey Cloud Adoption Study, 2023).

### Assessment Questions

| # | Question | Evidence Required | Score (0–4) |
|---|---|---|---|
| 1.1 | Has executive leadership formally approved a cloud strategy document? | Strategy document with exec sign-off | |
| 1.2 | Are migration motivations clearly documented (cost, agility, innovation, BCDR, datacenter exit)? | Migration motivation statement | |
| 1.3 | Are specific, measurable cloud business outcomes defined (e.g., 30% cost reduction, 50% faster deployments)? | OKRs or KPIs with baseline and target | |
| 1.4 | Is there an active executive sponsor accountable for the migration program? | Named executive sponsor + escalation path | |
| 1.5 | Are cloud adoption goals tied to a broader digital transformation strategy? | Link between cloud plan and digital strategy | |

**Category Score: ___ / 20 → Convert to 0–100: ___ × 5 = ___**

### Common Gaps & Remediation

| Gap | Remediation |
|---|---|
| No executive sponsor | Facilitate executive alignment workshop; present TCO analysis to CFO/CIO |
| Strategy exists but not linked to business outcomes | Run outcome-mapping workshop; define OKRs per business unit |
| Migration viewed as IT initiative only | Reposition as business transformation; involve product/operations owners |

**Accelerator Resources:**
- [Multi-Cloud Strategy Framework](../frameworks/multi-cloud/multi-cloud-strategy.md) — Strategy drivers and motivation framework
- [Pre-Sales Playbook — Business Discovery](../presales/presales-playbook.md) — Executive discovery questions
- [Business Case Template](../templates/business-case-template.md) — ROI model with outcome metrics

---

## Category 2: Partner Support

**SMART Definition:** Engagement of Microsoft partners (SIs, CSPs, MSPs) to support migration planning, delivery, and ongoing management.

**Why It Matters:** Organizations with active partner engagement complete migrations 40% faster and achieve 25% better cost outcomes (Source: Microsoft Internal Partner Analytics, 2023).

### Assessment Questions

| # | Question | Evidence Required | Score (0–4) |
|---|---|---|---|
| 2.1 | Has a Microsoft partner (SI, CSP, MSP) been engaged for migration support? | Named partner with scope of engagement | |
| 2.2 | Is the partner's scope clearly defined (planning, delivery, managed services)? | Statement of Work or engagement letter | |
| 2.3 | Has a Microsoft account team (CSAM, CE) been engaged? | Microsoft CSAM/CE contact confirmed | |
| 2.4 | Is there a FastTrack for Azure or AMMP engagement in place? | FastTrack nomination or AMMP enrollment | |
| 2.5 | Are partner roles and responsibilities clear (RACI with partner)? | RACI matrix with partner columns | |

**Category Score: ___ / 20 → Convert to 0–100: ___ × 5 = ___**

### Common Gaps & Remediation

| Gap | Remediation |
|---|---|
| No partner engaged | Refer to Microsoft Partner Directory; engage CSP or SI with Azure migration competency |
| Partner engaged but scope unclear | Develop joint Statement of Work with milestone-based deliverables |
| No Microsoft account team relationship | Contact Microsoft CSAM via Microsoft account portal; nominate for FastTrack for Azure |

**Accelerator Resources:**
- [Pre-Sales Playbook — Alliance Partner Programs](../presales/presales-playbook.md) — MPN/APN/GCP partner program details
- [Migration RACI Template](../templates/migration-raci-template.md) — Includes partner/CSP rows

**FastTrack for Azure:** Eligible customers (>150 Azure seats or equivalent ACV) receive free Microsoft engineering assistance for landing zone deployment and migration execution. [Nominate at aka.ms/fasttrack](https://aka.ms/fasttrack)

---

## Category 3: Discovery & Assessment

**SMART Definition:** Effectiveness of infrastructure and application portfolio discovery, dependency mapping, and rationalization to inform migration planning.

**Why It Matters:** Organizations that skip structured discovery are 2× more likely to encounter critical blockers mid-migration. Missing dependencies are the #1 cause of post-migration outages.

### Assessment Questions

| # | Question | Evidence Required | Score (0–4) |
|---|---|---|---|
| 3.1 | Has a complete application portfolio inventory been completed (all apps, VMs, databases)? | Portfolio inventory spreadsheet or Azure Migrate report | |
| 3.2 | Have application dependencies been mapped (network, data, integrations, licensing)? | Dependency map or Azure Migrate dependency visualization | |
| 3.3 | Have workloads been rationalized using the 5 Rs (Rehost, Refactor, Rearchitect, Rebuild, Replace)? | Rationalization register with R-classification per app | |
| 3.4 | Have migration waves been defined based on complexity, value, and dependency order? | Wave plan with priority sequencing | |
| 3.5 | Have Azure Migrate or equivalent tools been deployed for discovery? | Azure Migrate project configured; appliances deployed | |

**Category Score: ___ / 20 → Convert to 0–100: ___ × 5 = ___**

### Common Gaps & Remediation

| Gap | Remediation |
|---|---|
| No portfolio inventory | Deploy Azure Migrate appliance; run 2–4 week discovery sprint |
| Dependencies not mapped | Enable Azure Migrate dependency analysis (agentless or agent-based) |
| No rationalization completed | Run app rationalization workshop using 5 Rs framework |
| No wave plan | Prioritize by: low complexity + high business value for early waves |

**Azure Discovery Tools:**

| Tool | Use Case |
|---|---|
| [Azure Migrate](https://azure.microsoft.com/products/azure-migrate/) | VM, server, and database discovery + dependency mapping |
| [Movere](https://www.microsoft.com/security/blog/movere/) | Agentless SaaS discovery (acquired by Microsoft) |
| [Service Map (Log Analytics)](https://learn.microsoft.com/azure/azure-monitor/vm/service-map) | Process and TCP dependency mapping |
| [MAP Toolkit](https://www.microsoft.com/download/details.aspx?id=7826) | Microsoft Assessment and Planning Toolkit (offline/air-gapped environments) |

**Accelerator Resources:**
- [Azure Migration Guide — Phase 2 (Plan)](../frameworks/azure/azure-migration-guide.md)
- [Cloud Readiness Assessment — Domain 3](cloud-readiness-assessment.md)

---

## Category 4: Business Case

**SMART Definition:** Clarity, completeness, and approval of the financial and business justification for migrating to Azure.

**Why It Matters:** A validated business case secures executive funding, reduces mid-program cancellation risk, and aligns stakeholders to a shared financial commitment.

### Assessment Questions

| # | Question | Evidence Required | Score (0–4) |
|---|---|---|---|
| 4.1 | Has a TCO analysis been completed comparing on-premises vs. Azure costs over 3 years? | TCO analysis document (Azure TCO Calculator output recommended) | |
| 4.2 | Does the business case quantify hard savings (infrastructure, licensing, operations)? | Itemized cost reduction with baseline | |
| 4.3 | Does the business case include soft/strategic benefits (agility, innovation, talent)? | Qualitative benefits section | |
| 4.4 | Has the business case been reviewed and approved by Finance/CFO? | Finance approval sign-off | |
| 4.5 | Is there an Azure consumption commitment (MACC) in place aligned to the business case? | MACC agreement or Azure EA amendment | |

**Category Score: ___ / 20 → Convert to 0–100: ___ × 5 = ___**

### Common Gaps & Remediation

| Gap | Remediation |
|---|---|
| No TCO analysis | Use [Azure TCO Calculator](https://azure.microsoft.com/pricing/tco/calculator/) + partner-assisted modeling |
| Business case not finance-approved | Schedule CFO/Finance review; include Azure Hybrid Benefit savings |
| No MACC | Engage Microsoft account team to discuss MACC options under EA |

**Accelerator Resources:**
- [Business Case Template](../templates/business-case-template.md) — 3-year TCO model with savings analysis
- [Pre-Sales Playbook — ROI & Business Case Framework](../presales/presales-playbook.md)
- [FinOps Framework — Reserved Capacity Discounts](../cost-optimization/finops-framework.md)

---

## Category 5: Migration Plan

**SMART Definition:** Realism, completeness, and approval of the migration plan including timelines, resource allocation, wave sequencing, and rollback procedures.

### Assessment Questions

| # | Question | Evidence Required | Score (0–4) |
|---|---|---|---|
| 5.1 | Is there a documented, phased migration plan with milestones and timeline? | Migration project plan (Gantt or milestone view) | |
| 5.2 | Are migration waves sequenced with clear rationale (dependencies, risk, business value)? | Wave sequencing document | |
| 5.3 | Is there a defined cutover approach with rollback procedures for each wave? | Cutover runbook with rollback steps | |
| 5.4 | Are resource requirements (people, tooling, budget) allocated to each phase? | Resource allocation plan | |
| 5.5 | Has the plan been reviewed and approved by all key stakeholders? | Stakeholder sign-off on plan | |

**Category Score: ___ / 20 → Convert to 0–100: ___ × 5 = ___**

### Common Gaps & Remediation

| Gap | Remediation |
|---|---|
| No formal migration plan | Use Azure Migration Guide phases as plan template |
| No rollback procedures | Define rollback criteria and steps in the migration runbook |
| Resources not allocated | Perform resourcing workshop; identify skills gaps and partner support needs |

**Accelerator Resources:**
- [Azure Migration Guide — Phase 4 (Migrate)](../frameworks/azure/azure-migration-guide.md)
- [Migration RACI Template](../templates/migration-raci-template.md)

---

## Category 6: Technical Skilling

**SMART Definition:** Workforce readiness in terms of Azure skills, training plans, and certifications to support migration and cloud operations.

**Why It Matters:** Skills gaps are the #2 reported barrier to cloud adoption (after security concerns). Organizations with structured skilling programs reduce operational incidents post-migration by 35%.

### Assessment Questions

| # | Question | Evidence Required | Score (0–4) |
|---|---|---|---|
| 6.1 | Has a cloud skills gap assessment been completed for all impacted teams? | Skills gap report or assessment results | |
| 6.2 | Is there a structured training plan aligned to migration roles (Admin, Architect, DevOps, Security)? | Training plan with named individuals and certifications | |
| 6.3 | Are cloud-specific training resources allocated (budget, time, Microsoft Learn access)? | Training budget line item | |
| 6.4 | Is there a target certification path defined for key cloud roles? | Certification roadmap per role | |
| 6.5 | Has a Cloud Center of Excellence (CCoE) or cloud champions network been established? | CCoE charter or champions program documentation | |

**Category Score: ___ / 20 → Convert to 0–100: ___ × 5 = ___**

### Common Gaps & Remediation

| Gap | Remediation |
|---|---|
| No skills gap assessment | Use Microsoft Organizational Readiness Assessment; map roles to learning paths |
| No training plan | Build role-based training plan using Microsoft Learn + partner-led training |
| No CCoE | Establish CCoE with 3–5 initial members; use [Azure CCoE guidance](https://learn.microsoft.com/azure/cloud-adoption-framework/organize/cloud-center-of-excellence) |

**Azure Certification Roadmap (Embedded from Azure Migration Guide):**

| Role | Path |
|---|---|
| Cloud Administrator | AZ-900 → AZ-104 |
| Cloud Architect | AZ-900 → AZ-104 → AZ-305 |
| Security Engineer | SC-900 → AZ-500 → SC-100 |
| DevOps Engineer | AZ-400 |
| AI / ML Engineer | AI-900 → AI-102 |

**Accelerator Resources:**
- [Azure Migration Guide — Certifications Roadmap](../frameworks/azure/azure-migration-guide.md)
- [Cloud Readiness Assessment — Domain 2 (Organization & Skills)](cloud-readiness-assessment.md)

---

## Category 7: Landing Zone

**SMART Definition:** Preparedness of the Azure target environment with foundational security, governance, networking, and identity controls in place before workload migration.

**Why It Matters:** Migrating without a landing zone is like moving into a house before the electricity and plumbing are connected. Landing zone gaps are the #1 technical cause of security incidents in cloud migrations.

### Assessment Questions

| # | Question | Evidence Required | Score (0–4) |
|---|---|---|---|
| 7.1 | Is an Azure landing zone (or equivalent) deployed and validated? | Deployed Azure subscription with management group hierarchy | |
| 7.2 | Is the Azure management group and subscription hierarchy defined and implemented? | Management group design document | |
| 7.3 | Is hub-spoke or Azure Virtual WAN network topology deployed? | Network architecture diagram | |
| 7.4 | Is Azure connectivity to on-premises established (ExpressRoute or Site-to-Site VPN)? | Connectivity test results | |
| 7.5 | Is Microsoft Entra ID (Azure AD) configured with MFA and Conditional Access? | Entra ID configuration review | |
| 7.6 | Are Azure Policies and RBAC role assignments deployed across the landing zone? | Policy compliance dashboard | |
| 7.7 | Is Microsoft Defender for Cloud enabled and security posture baseline established? | Defender for Cloud secure score (target: >60%) | |
| 7.8 | Are monitoring and logging configured (Log Analytics Workspace, Diagnostic Settings)? | Log Analytics workspace with data sources connected | |

**Category Score: ___ / 32 → Convert to 0–100: ___ × 3.125 = ___**

### Common Gaps & Remediation

| Gap | Remediation |
|---|---|
| No landing zone deployed | Use [Azure Landing Zone Accelerator (aka.ms/alz)](https://aka.ms/alz) — deploy via Bicep or Terraform in 1–2 days |
| No hybrid connectivity | Order ExpressRoute circuit or configure Site-to-Site VPN via Azure VPN Gateway |
| Low Defender for Cloud score | Run Defender for Cloud recommendations; prioritize high-severity findings |
| No Azure Policy baseline | Apply CIS or Azure Security Benchmark policy initiative |

**Accelerator Resources:**
- [Cloud Governance Framework — Landing Zone Design](../governance/cloud-governance-framework.md)
- [Security & Compliance Framework](../security/security-compliance-framework.md)
- [Azure Migration Guide — Phase 3 (Ready)](../frameworks/azure/azure-migration-guide.md)

---

## Category 8: Migration Execution

**SMART Definition:** Technical capabilities, tools, and processes for executing the actual migration, including replication, testing, cutover, and validation.

### Assessment Questions

| # | Question | Evidence Required | Score (0–4) |
|---|---|---|---|
| 8.1 | Have the appropriate migration tools been selected and tested (Azure Migrate, MGN, DMS)? | Tool selection document + test migration results | |
| 8.2 | Has a test migration been successfully completed for at least one workload? | Test migration report | |
| 8.3 | Are migration runbooks defined for each wave, including pre/post validation steps? | Migration runbook (per wave) | |
| 8.4 | Is there a defined cutover window and communication plan? | Cutover schedule + stakeholder communications template | |
| 8.5 | Are backup and restore procedures validated in Azure for migrated workloads? | Azure Backup policy + restore test results | |

**Category Score: ___ / 20 → Convert to 0–100: ___ × 5 = ___**

### Common Gaps & Remediation

| Gap | Remediation |
|---|---|
| Tools not tested | Deploy Azure Migrate appliance + run test migration on non-critical VM |
| No runbooks | Use the migration runbook template in this accelerator |
| No validated backup | Configure Azure Backup policies; perform restore test before cutover |

**Migration Tool Selection:**

| Scenario | Tool |
|---|---|
| VM lift-and-shift (VMware/Hyper-V) | [Azure Migrate — Server Migration](https://azure.microsoft.com/products/azure-migrate/) |
| SQL Server migration | [Azure Database Migration Service](https://azure.microsoft.com/products/database-migration/) |
| Large-scale data transfer | [Azure Data Box](https://azure.microsoft.com/products/databox/) |
| Web app migration | [Azure App Service Migration Assistant](https://azure.microsoft.com/products/app-service/migration-tools/) |
| SAP | [SAP on Azure Migration Guide](https://learn.microsoft.com/azure/sap/workloads/migration-guide) |

**Accelerator Resources:**
- [Azure Migration Guide — Phase 4 (Migrate)](../frameworks/azure/azure-migration-guide.md)

---

## Category 9: Governance

**SMART Definition:** Policies, guardrails, and controls for managing cloud resources, ensuring cost accountability, and maintaining compliance during and after migration.

### Assessment Questions

| # | Question | Evidence Required | Score (0–4) |
|---|---|---|---|
| 9.1 | Are resource naming conventions and tagging standards defined and enforced? | Naming/tagging policy + compliance report | |
| 9.2 | Are Azure Policy initiatives applied to enforce compliance standards? | Azure Policy compliance score | |
| 9.3 | Is there a cloud cost management process with budgets, alerts, and showback/chargeback? | Azure Cost Management budget configuration | |
| 9.4 | Are privileged access and IAM policies reviewed and enforced (PIM, RBAC)? | PIM configuration + RBAC review results | |
| 9.5 | Is there a cloud audit trail and compliance monitoring process? | Azure Activity Log + Defender for Cloud compliance dashboard | |

**Category Score: ___ / 20 → Convert to 0–100: ___ × 5 = ___**

### Common Gaps & Remediation

| Gap | Remediation |
|---|---|
| No tagging policy | Define mandatory tag schema; enforce with Azure Policy deny effect |
| No cost budgets | Configure budgets in Azure Cost Management at subscription level |
| No PIM | Enable Entra ID Privileged Identity Management for all admin roles |

**Accelerator Resources:**
- [Cloud Governance Framework](../governance/cloud-governance-framework.md) — Full governance framework
- [FinOps Framework](../cost-optimization/finops-framework.md) — Cost management and FinOps

---

## Category 10: Management

**SMART Definition:** Ongoing operational processes post-migration, covering monitoring, patching, cost optimization, and incident management in the Azure environment.

### Assessment Questions

| # | Question | Evidence Required | Score (0–4) |
|---|---|---|---|
| 10.1 | Is there a cloud monitoring and alerting strategy (Azure Monitor, Log Analytics, Alerts)? | Azure Monitor alert rules + dashboards | |
| 10.2 | Is patch management automated for migrated workloads (Azure Update Manager)? | Update Manager policy assigned | |
| 10.3 | Is there a defined incident response process for cloud-hosted workloads? | Incident response runbook | |
| 10.4 | Are cost optimization processes in place (right-sizing, reserved instances, Advisor)? | Azure Advisor recommendations review cadence | |
| 10.5 | Is an Azure Well-Architected Review planned for migrated workloads within 90 days? | WAR scheduled or completed | |

**Category Score: ___ / 20 → Convert to 0–100: ___ × 5 = ___**

### Common Gaps & Remediation

| Gap | Remediation |
|---|---|
| No monitoring strategy | Deploy Azure Monitor Baseline alerts; configure Log Analytics workspace |
| No patch management | Enable Azure Update Manager; schedule maintenance windows |
| No WAR planned | Book [Azure Well-Architected Review](https://learn.microsoft.com/assessments/azure-architecture-review/) — free with Microsoft account team |

**Accelerator Resources:**
- [Azure Migration Guide — Phase 5 (Govern & Manage)](../frameworks/azure/azure-migration-guide.md)
- [Security & Compliance Framework — Operations](../security/security-compliance-framework.md)
- [FinOps Framework — Ongoing Optimization](../cost-optimization/finops-framework.md)

---

## SMART Readiness Index (SRI) Summary

After completing all categories, calculate the SMART Readiness Index:

| # | SMART Category | Score (0–100) | Readiness Level |
|---|---|---|---|
| 1 | Business Strategy | | |
| 2 | Partner Support | | |
| 3 | Discovery & Assessment | | |
| 4 | Business Case | | |
| 5 | Migration Plan | | |
| 6 | Technical Skilling | | |
| 7 | Landing Zone | | |
| 8 | Migration Execution | | |
| 9 | Governance | | |
| 10 | Management | | |
| **SMART Readiness Index (SRI)** | **Average of above** | | |

---

## SMART Priority Action Plan

Based on the SRI, complete the following table. Focus first on categories scoring **below 60**.

| Priority | Category | Current Score | Target Score | Key Actions | Owner | Target Date |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

---

## Mapping SMART Categories to the Cloud Readiness Assessment (CRA)

This accelerator's [Cloud Readiness Assessment (CRA)](cloud-readiness-assessment.md) provides complementary multi-cloud coverage. The table below shows how CRA domains and SMART categories reinforce each other:

| CRA Domain | SMART Categories Covered |
|---|---|
| 1. Strategy & Business Alignment | Business Strategy (1) · Business Case (4) |
| 2. Organization & Skills Readiness | Technical Skilling (6) · Partner Support (2) |
| 3. Platform & Technical Readiness | Discovery & Assessment (3) · Migration Plan (5) · Migration Execution (8) |
| 4. Security & Compliance | Landing Zone (7) — security controls |
| 5. Governance & Financial Management | Governance (9) · Business Case (4) |
| 6. Operations & Resilience | Management (10) |

**Recommended approach:** Run both assessments. Use SMART for Azure-specific depth and the CRA for multi-cloud breadth and organizational maturity.

---

## Related Microsoft Assessments

After completing SMART, the following Microsoft assessments provide additional depth:

| Assessment | Purpose | Link |
|---|---|---|
| Azure Well-Architected Review (WAR) | Workload-level architecture assessment | [learn.microsoft.com/assessments/azure-architecture-review](https://learn.microsoft.com/assessments/azure-architecture-review/) |
| Cloud Adoption Strategy Evaluator | Business strategy depth | [learn.microsoft.com/assessments/cloud-journey-tracker](https://learn.microsoft.com/assessments/cloud-journey-tracker/) |
| Security Compass Assessment | Security posture assessment | [Microsoft Security Compass](https://aka.ms/securitycompass) |
| Microsoft Defender for Cloud Secure Score | Ongoing security posture | [Defender for Cloud](https://azure.microsoft.com/products/defender-for-cloud/) |

---

*See also: [Cloud Readiness Assessment](cloud-readiness-assessment.md) | [Assessment Facilitation Guide](../docs/assessment-facilitation-guide.md) | [Azure Migration Guide](../frameworks/azure/azure-migration-guide.md) | [Readiness Scorecard](../templates/readiness-scorecard.md)*
