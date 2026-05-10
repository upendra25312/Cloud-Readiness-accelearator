# AWS Migration Guide

**Version:** 2.0  
**Authors:** AWS Solutions Architecture Team  
**Aligned To:** AWS Cloud Adoption Framework (AWS CAF) · AWS Migration Acceleration Program (MAP)

---

## Overview

This guide provides a structured, phased approach to migrating workloads to Amazon Web Services (AWS). It is aligned with the **AWS Cloud Adoption Framework (AWS CAF)** and the **AWS Well-Architected Framework**, and is designed for enterprise teams, system integrators, and AWS partners.

---

## AWS Migration Phases (MAP)

### Phase 1: Assess

**Objective:** Evaluate current state, build a directional business case, and identify migration readiness gaps.

**Key Activities:**
- Run the [AWS Migration Readiness Assessment (MRA)](https://aws.amazon.com/migration-acceleration-program/)
- Complete application portfolio discovery using [AWS Application Discovery Service](https://aws.amazon.com/application-discovery/)
- Build a directional TCO business case using the [AWS Pricing Calculator](https://calculator.aws/)
- Identify migration readiness gaps across six AWS CAF perspectives:
  1. **Business** — Strategy, finance, portfolio management
  2. **People** — Change management, organizational readiness
  3. **Governance** — Program management, risk, compliance
  4. **Platform** — Architecture, CI/CD, solution engineering
  5. **Security** — IAM, infrastructure, data protection, incident response
  6. **Operations** — Monitoring, service management, performance

**Deliverables:**
- AWS MRA Report
- Application Portfolio Discovery Report
- Directional Business Case (TCO)

---

### Phase 2: Mobilize

**Objective:** Address readiness gaps, build the migration factory foundation, and develop a detailed migration plan.

**Key Activities:**
- Establish AWS Landing Zone using [AWS Control Tower](https://aws.amazon.com/controltower/)
- Define multi-account strategy:

```
AWS Organizations
├── Root
│   ├── Security OU
│   │   ├── Log Archive Account
│   │   └── Security Tooling Account
│   ├── Infrastructure OU
│   │   ├── Network Account (Transit Gateway, VPN, Direct Connect)
│   │   └── Shared Services Account
│   └── Workloads OU
│       ├── Production OU
│       ├── Non-Production OU
│       └── Sandbox OU
```

- Deploy network foundation (VPC, Transit Gateway, AWS Direct Connect / Site-to-Site VPN)
- Configure AWS Security Hub, AWS Config, CloudTrail, GuardDuty
- Apply Service Control Policies (SCPs) for guardrails
- Apply **7 Rs of Migration**:
  - **Retire** — Decommission legacy applications
  - **Retain** — Keep on-premises (temporarily)
  - **Rehost** — Lift and shift to EC2/ECS
  - **Relocate** — Move VMware to VMware Cloud on AWS
  - **Repurchase** — Move to SaaS
  - **Replatform** — Minimal changes to use AWS PaaS (RDS, Elastic Beanstalk)
  - **Refactor/Re-architect** — Cloud-native rebuild (Lambda, EKS, Aurora)
- Develop migration runbooks and wave plans

**Deliverables:**
- AWS Landing Zone (deployed)
- Detailed Migration Plan (wave by wave)
- Migration Runbooks
- Skills Training Plan

---

### Phase 3: Migrate & Modernize

**Objective:** Execute migration waves and modernize applications incrementally.

**AWS Migration Tools:**

| Workload Type | Recommended Tool |
|---|---|
| Servers (VM/Physical) | [AWS Application Migration Service (MGN)](https://aws.amazon.com/application-migration-service/) |
| Databases | [AWS Database Migration Service (DMS)](https://aws.amazon.com/dms/) |
| VMware Workloads | [VMware Cloud on AWS](https://aws.amazon.com/vmware/) |
| Data / Storage | [AWS DataSync](https://aws.amazon.com/datasync/), [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/) |
| Large-Scale Data | [AWS Snow Family](https://aws.amazon.com/snow/) (Snowcone, Snowball, Snowmobile) |
| SAP | [SAP on AWS Migration Guide](https://aws.amazon.com/sap/) |
| Mainframe | [AWS Mainframe Modernization](https://aws.amazon.com/mainframe-modernization/) |

**Migration Wave Execution:**
1. **Pre-migration:** Install MGN replication agent; start continuous replication
2. **Test cutover:** Validate in AWS (non-production test)
3. **Cutover window:** Execute production cutover; validate
4. **Post-migration:** Monitor, optimize, decommission source

**Key Considerations:**
- Use AWS MGN for all VM replication (preferred over CloudEndure)
- Use AWS DMS with Schema Conversion Tool (SCT) for heterogeneous DB migrations
- Apply Security Groups, NACLs, and VPC Flow Logs from day one
- Validate backup using [AWS Backup](https://aws.amazon.com/backup/)
- Tag all resources at creation (cost allocation, ownership, environment)

**Deliverables:**
- Migration Wave Runbooks
- Go/No-Go Decision Checklist
- Post-Migration Validation Report

---

### Phase 4: Operate & Optimize

**Objective:** Run optimized cloud operations and continuously improve.

**AWS Operations Tooling:**

| Tool | Purpose |
|---|---|
| AWS Organizations + SCPs | Account governance and guardrails |
| AWS Control Tower | Multi-account governance |
| AWS Config + AWS Config Rules | Compliance monitoring and remediation |
| AWS Security Hub | Centralized security posture management |
| Amazon GuardDuty | Threat detection |
| AWS CloudTrail | API audit logging |
| Amazon CloudWatch | Monitoring, metrics, logs, alarms |
| AWS Systems Manager | Operations management (Patch Manager, Run Command) |
| AWS Cost Explorer + Budgets | FinOps and cost management |
| AWS Trusted Advisor | Best practice recommendations |
| AWS Compute Optimizer | Right-sizing recommendations |

**AWS Well-Architected Framework Pillars:**
1. **Operational Excellence** — IaC (CloudFormation/Terraform/CDK), CI/CD, runbooks
2. **Security** — IAM Least Privilege, GuardDuty, Security Hub, KMS, Macie
3. **Reliability** — Multi-AZ, Auto Scaling, Route 53, Backup, Chaos Engineering (FIS)
4. **Performance Efficiency** — Auto-scaling, CloudFront, ElastiCache, RDS Aurora
5. **Cost Optimization** — Reserved Instances, Savings Plans, Spot Instances, S3 lifecycle
6. **Sustainability** — Efficient instance selection, auto-scaling, serverless

**Deliverables:**
- Cloud Operations Runbook
- Monthly Well-Architected Review
- Monthly Cost Optimization Report

---

## AWS Reference Architectures

| Scenario | Reference |
|---|---|
| Highly available web application | [AWS HA Web Application](https://aws.amazon.com/architecture/reference-architecture-diagrams/) |
| Microservices on EKS | [Amazon EKS Best Practices](https://aws.github.io/aws-eks-best-practices/) |
| Serverless API backend | [Serverless on AWS](https://aws.amazon.com/serverless/) |
| Data analytics platform | [AWS Analytics Reference Architecture](https://aws-samples.github.io/aws-analytics-reference-architecture/) |
| Hybrid network | [AWS Direct Connect + VPN](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html) |

---

## AWS Certifications Roadmap

| Role | Recommended Certifications |
|---|---|
| Cloud Practitioner | AWS Certified Cloud Practitioner (CLF-C02) |
| Solutions Architect | SAA-C03 → SAP-C02 |
| SysOps Administrator | SOA-C02 |
| Developer | DVA-C02 |
| Data Engineer | DEA-C01 |
| ML Engineer | MLA-C01 |
| Security Specialty | SCS-C02 |
| Networking Specialty | ANS-C01 |

---

*See also: [Multi-Cloud Strategy](../multi-cloud/multi-cloud-strategy.md) | [Security Framework](../../security/security-compliance-framework.md) | [FinOps Framework](../../cost-optimization/finops-framework.md)*
