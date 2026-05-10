# Cloud Readiness Assessment

**Version:** 2.0  
**Authors:** Microsoft Azure Cloud Architecture Team, AWS Solutions Architecture, Google Cloud Pre-Sales  
**Applies To:** Azure · AWS · Google Cloud Platform

---

## Purpose

This assessment provides a structured scoring model to evaluate an organization's readiness to adopt, migrate to, or expand on cloud platforms. It covers six domains drawn from the **Microsoft Cloud Adoption Framework (CAF)**, **AWS Cloud Adoption Framework**, and **Google Cloud Adoption Framework**.

Each domain is scored 1–5 (1 = Initial/Ad-hoc, 5 = Optimized). Use the [scorecard template](../templates/readiness-scorecard.md) to record results.

---

## Assessment Domains

### Domain 1: Strategy & Business Alignment

| # | Question | Score (1–5) | Notes |
|---|---|---|---|
| 1.1 | Has a formal cloud strategy been defined and approved by executive leadership? | | |
| 1.2 | Are cloud business outcomes documented (e.g., cost reduction, agility, innovation)? | | |
| 1.3 | Is there a defined cloud business case with ROI projections? | | |
| 1.4 | Are cloud objectives aligned to overall digital transformation goals? | | |
| 1.5 | Is there a documented cloud-first or cloud-smart policy? | | |
| 1.6 | Have cloud risk appetite and tolerance levels been defined? | | |

**Domain Score: ___ / 30**

---

### Domain 2: Organization & Skills Readiness

| # | Question | Score (1–5) | Notes |
|---|---|---|---|
| 2.1 | Is there a Cloud Center of Excellence (CCoE) or equivalent team? | | |
| 2.2 | Have cloud skill gaps been assessed and training plans developed? | | |
| 2.3 | Are cloud-specific roles defined (Cloud Architect, FinOps, SecOps)? | | |
| 2.4 | Do teams follow agile/DevOps practices compatible with cloud delivery? | | |
| 2.5 | Is there a defined RACI matrix for cloud decisions and operations? | | |
| 2.6 | Are vendor partner ecosystems (SI, ISV, CSP) engaged and mapped? | | |

**Domain Score: ___ / 30**

---

### Domain 3: Platform & Technical Readiness

| # | Question | Score (1–5) | Notes |
|---|---|---|---|
| 3.1 | Has a full application portfolio inventory been completed? | | |
| 3.2 | Have application dependencies been mapped (network, data, integrations)? | | |
| 3.3 | Is there a defined cloud landing zone or account/subscription architecture? | | |
| 3.4 | Is infrastructure-as-code (IaC) tooling in place (Terraform, Bicep, CDK)? | | |
| 3.5 | Are CI/CD pipelines established for cloud deployments? | | |
| 3.6 | Is there a defined cloud operating model (shared responsibility mapped)? | | |
| 3.7 | Have cloud-native design patterns been evaluated (containers, serverless, PaaS)? | | |
| 3.8 | Is a hybrid/multi-cloud connectivity strategy defined (ExpressRoute, Direct Connect, Interconnect)? | | |

**Domain Score: ___ / 40**

---

### Domain 4: Security & Compliance Readiness

| # | Question | Score (1–5) | Notes |
|---|---|---|---|
| 4.1 | Is there a cloud security policy aligned to regulatory requirements (ISO 27001, SOC 2, GDPR, HIPAA)? | | |
| 4.2 | Has a Zero Trust security architecture been defined for cloud environments? | | |
| 4.3 | Is identity and access management (IAM/RBAC/ABAC) strategy documented? | | |
| 4.4 | Is data classification and data sovereignty policy in place? | | |
| 4.5 | Are cloud security benchmarks applied (CIS, NIST, CSA CCM)? | | |
| 4.6 | Is there a defined incident response and SIEM integration plan for cloud? | | |
| 4.7 | Are encryption-at-rest and in-transit requirements documented? | | |

**Domain Score: ___ / 35**

---

### Domain 5: Governance & Financial Management

| # | Question | Score (1–5) | Notes |
|---|---|---|---|
| 5.1 | Are cloud tagging standards and resource naming conventions defined? | | |
| 5.2 | Is there a cloud cost management process (budgets, alerts, showback/chargeback)? | | |
| 5.3 | Are cloud policies enforced through guardrails (Azure Policy, AWS SCPs, GCP Org Policies)? | | |
| 5.4 | Is there a FinOps practice or function established? | | |
| 5.5 | Are reserved instance/savings plan strategies defined? | | |
| 5.6 | Is there a cloud audit and compliance monitoring process? | | |

**Domain Score: ___ / 30**

---

### Domain 6: Operations & Resilience

| # | Question | Score (1–5) | Notes |
|---|---|---|---|
| 6.1 | Is there a cloud monitoring and observability strategy (logs, metrics, traces)? | | |
| 6.2 | Are SLAs and SLOs defined for cloud-hosted workloads? | | |
| 6.3 | Are business continuity and disaster recovery (BCDR) plans validated for cloud? | | |
| 6.4 | Is there a defined cloud incident management and escalation process? | | |
| 6.5 | Are auto-scaling and resilience patterns applied? | | |
| 6.6 | Is chaos engineering / failure injection testing practiced? | | |
| 6.7 | Are cloud Well-Architected Reviews conducted regularly? | | |

**Domain Score: ___ / 35**

---

## Scoring Summary

| Domain | Max Score | Your Score | Maturity Level |
|---|---|---|---|
| 1. Strategy & Business Alignment | 30 | | |
| 2. Organization & Skills | 30 | | |
| 3. Platform & Technical Readiness | 40 | | |
| 4. Security & Compliance | 35 | | |
| 5. Governance & Financial Management | 30 | | |
| 6. Operations & Resilience | 35 | | |
| **Total** | **200** | | |

---

## Maturity Levels

| Score Range | Maturity Level | Description |
|---|---|---|
| 0–59 | **1 – Initial** | Ad-hoc, no formal cloud practices. High risk. Immediate action required. |
| 60–99 | **2 – Developing** | Some practices defined, inconsistently applied. Foundational gaps. |
| 100–139 | **3 – Defined** | Documented standards, applied to most workloads. Moderate maturity. |
| 140–169 | **4 – Managed** | Measured, managed, and continuously improved. Low risk. |
| 170–200 | **5 – Optimized** | Industry-leading practices. Cloud-native, data-driven, automated. |

---

## Recommended Next Steps

Based on your maturity score:

- **Score 1–2:** Focus on [Strategy Framework](../frameworks/multi-cloud/multi-cloud-strategy.md) and [Governance](../governance/cloud-governance-framework.md) first. Engage a Cloud Adoption readiness workshop.
- **Score 3:** Prioritize [Security](../security/security-compliance-framework.md) and [FinOps](../cost-optimization/finops-framework.md) hardening.
- **Score 4:** Drive towards optimization via [AI/ML Readiness](../ai-ml-readiness/ai-ml-readiness-framework.md) and platform engineering maturity.
- **Score 5:** Share learnings with the community and contribute back to this accelerator.

---

*For assessment facilitation guidance, see [docs/assessment-facilitation-guide.md](../docs/assessment-facilitation-guide.md).*
