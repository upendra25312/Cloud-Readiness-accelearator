# Cloud Governance Framework

**Version:** 2.0  
**Authors:** Senior Cloud Architecture Teams — Microsoft, AWS, Google Cloud  
**Aligned To:** Azure CAF Governance · AWS Control Tower · Google Cloud Adoption Framework

---

## Overview

Cloud governance ensures that cloud environments are managed securely, cost-effectively, and in compliance with organizational policies and regulatory requirements. This framework provides standardized governance controls applicable across **Azure**, **AWS**, and **GCP**.

---

## Governance Foundation: The 6 Disciplines

Based on the **Microsoft Cloud Adoption Framework**, governance is structured across six disciplines — adapted here for multi-cloud applicability:

| Discipline | Description |
|---|---|
| **Cost Management** | Visibility, accountability, and optimization of cloud spend |
| **Security Baseline** | Minimum security controls for all cloud environments |
| **Identity Baseline** | IAM standards and access control governance |
| **Resource Consistency** | Standards for resource naming, tagging, and configuration |
| **Deployment Acceleration** | IaC standards, CI/CD pipelines, and change management |
| **Resource Management** | Lifecycle management, retirement, and operational standards |

---

## Landing Zone Design

A **landing zone** is a pre-configured, governed cloud environment ready to host workloads. It encodes organizational policy into infrastructure.

### Azure Landing Zone (Enterprise Scale)

```
Management Group Hierarchy
│
├── Root MG (Tenant)
│   ├── Platform MG
│   │   ├── Identity Subscription (Entra ID, AD DS)
│   │   ├── Management Subscription (Log Analytics, Automation)
│   │   └── Connectivity Subscription (Hub VNet, ExpressRoute, Firewall)
│   │
│   ├── Landing Zones MG
│   │   ├── Corp MG (connected to on-premises)
│   │   │   ├── Production Subscription(s)
│   │   │   └── Non-Production Subscription(s)
│   │   └── Online MG (internet-facing)
│   │       ├── Production Subscription(s)
│   │       └── Non-Production Subscription(s)
│   │
│   ├── Sandboxes MG (developer experimentation — budget-capped)
│   └── Decommissioned MG (workloads being retired)
```

**Deployment:** Use [Azure Landing Zone Accelerator (Bicep/Terraform)](https://aka.ms/alz)

### AWS Landing Zone (Control Tower)

```
AWS Organizations
│
├── Root
│   ├── Security OU
│   │   ├── Log Archive Account
│   │   └── Security Tooling Account (Security Hub, GuardDuty, Inspector)
│   │
│   ├── Infrastructure OU
│   │   ├── Network Account (Transit Gateway, Direct Connect, Route 53)
│   │   └── Shared Services Account (AD, patch, monitoring)
│   │
│   ├── Workloads OU
│   │   ├── Production OU → Production Account(s)
│   │   └── Non-Production OU → Dev/Test Account(s)
│   │
│   └── Sandbox OU → Developer Accounts (budget-limited)
```

**Deployment:** Use [AWS Control Tower](https://aws.amazon.com/controltower/) + [Landing Zone Accelerator on AWS](https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/)

### GCP Landing Zone (Fabric FAST)

```
GCP Organization
│
├── Platform Folder
│   ├── Network Hub Project (Shared VPC, Interconnect)
│   ├── Security Project (SCC, Chronicle, Forseti)
│   └── Shared Services Project (Artifact Registry, CI/CD, DNS)
│
├── Workloads Folder
│   ├── Production Folder → Production Projects
│   └── Non-Production Folder → Dev/Test Projects
│
└── Sandbox Folder → Developer Projects (org policy restricted)
```

**Deployment:** Use [Fabric FAST](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/blob/master/fast/README.md) or [Google Cloud Foundation Toolkit](https://github.com/terraform-google-modules)

---

## Resource Naming Conventions

### Standard Naming Pattern

```
{cloud}-{environment}-{region}-{resource-type}-{workload}-{instance}
```

**Examples:**

| Resource | Azure | AWS | GCP |
|---|---|---|---|
| Virtual Machine | `az-prod-eus2-vm-webapp-001` | `aws-prod-use1-ec2-webapp-001` | `gcp-prod-use1-vm-webapp-001` |
| Virtual Network | `az-prod-eus2-vnet-hub-001` | `aws-prod-use1-vpc-hub-001` | `gcp-prod-use1-vpc-hub-001` |
| Storage Account | `azproddeus2stwebapp001` | `aws-prod-use1-s3-webapp-001` | `gcp-prod-use1-gcs-webapp-001` |
| Key Vault / Secrets | `az-prod-eus2-kv-webapp-001` | `aws-prod-use1-sm-webapp-001` | `gcp-prod-use1-sm-webapp-001` |

**Environment Abbreviations:** `prod` · `nonprod` · `dev` · `test` · `staging` · `sandbox`

**Region Abbreviations:** `eus2` (East US 2) · `weu` (West Europe) · `use1` (us-east-1) · `usw2` (us-west-2) · `use4` (us-east4 GCP) · `euw1` (europe-west1 GCP)

---

## Mandatory Tagging Standards

All cloud resources **must** have the following tags applied at provisioning time. Enforcement is via Azure Policy / AWS SCPs + Config Rules / GCP Org Policies.

| Tag | Required? | Description | Example |
|---|---|---|---|
| `Environment` | ✅ Required | Deployment environment | `Production` |
| `Owner` | ✅ Required | Team email or alias | `platform-eng@company.com` |
| `CostCenter` | ✅ Required | Finance cost center code | `CC-4521` |
| `Project` | ✅ Required | Project or application name | `erp-migration` |
| `DataClassification` | ✅ Required | Data sensitivity level | `Confidential` |
| `Compliance` | ✅ Required | Applicable regulation | `GDPR`, `HIPAA`, `PCI` |
| `CreatedBy` | ✅ Required | IaC pipeline or user identity | `terraform-pipeline` |
| `ExpiryDate` | For sandboxes | Auto-deletion date | `2025-12-31` |

---

## Policy Guardrails

### Azure Policy Initiatives (Apply to all subscriptions)

| Initiative | Purpose |
|---|---|
| Azure Security Benchmark | Security baseline controls |
| CIS Microsoft Azure Foundations Benchmark | CIS Level 1 & 2 controls |
| NIST SP 800-53 Rev. 5 | Federal compliance controls |
| Require tags on resource groups | Tagging enforcement |
| Allowed locations | Data residency enforcement |
| Deny public IP on non-approved resources | Network security |
| Require HTTPS on storage accounts | Encryption in transit |

### AWS Service Control Policies (SCPs)

| SCP | Purpose |
|---|---|
| Deny root account API use | Root account protection |
| Require MFA for console access | Authentication control |
| Deny regions not approved | Data residency enforcement |
| Deny deletion of GuardDuty / CloudTrail | Security control protection |
| Require S3 bucket encryption | Data protection |
| Deny creation of untagged resources | Tagging enforcement |

### GCP Organization Policies

| Policy | Purpose |
|---|---|
| `constraints/gcp.resourceLocations` | Data residency — restrict regions |
| `constraints/iam.allowedPolicyMemberDomains` | Allow only internal identities |
| `constraints/compute.requireShieldedVm` | Enforce Shielded VM |
| `constraints/sql.restrictPublicIp` | Deny public Cloud SQL IPs |
| `constraints/storage.uniformBucketLevelAccess` | Enforce bucket-level IAM |
| `constraints/compute.disableSerialPortAccess` | Harden VM access |

---

## Cloud Governance RACI Matrix

| Activity | Cloud Platform Team | Application Team | Security Team | Finance/FinOps | Audit/Compliance |
|---|---|---|---|---|---|
| Define landing zone standards | **R/A** | C | C | I | I |
| Deploy landing zone | **R** | I | C | I | I |
| Define tagging standards | **R/A** | C | C | **R** | C |
| Enforce tagging via policy | **R** | I | A | I | I |
| Cloud cost reporting | I | I | I | **R/A** | I |
| Security baseline enforcement | C | I | **R/A** | I | C |
| Compliance audit | I | I | C | I | **R/A** |
| IAM access reviews | C | C | **R/A** | I | C |
| Well-Architected Reviews | **R** | **R** | C | C | I |

*R = Responsible · A = Accountable · C = Consulted · I = Informed*

---

## Governance Review Cadence

| Review | Frequency | Participants |
|---|---|---|
| Cloud Cost Review | Monthly | FinOps, Engineering Leads, Finance |
| Security Posture Review | Monthly | CISO, Security Team, Cloud Platform |
| Policy Compliance Review | Quarterly | Audit, Cloud Platform, Security |
| Landing Zone Review | Quarterly | Cloud Architecture, Platform Team |
| Well-Architected Review | Per workload / Annually | Cloud Architect, App Teams |
| Governance Board Meeting | Quarterly | CTO, CISO, CIO, Cloud Directors |

---

*See also: [Security & Compliance Framework](../security/security-compliance-framework.md) | [FinOps Framework](../cost-optimization/finops-framework.md) | [Multi-Cloud Strategy](../frameworks/multi-cloud/multi-cloud-strategy.md)*
