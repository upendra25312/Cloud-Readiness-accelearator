# Security & Compliance Framework

**Version:** 2.0  
**Authors:** Cloud Security Architecture Teams — Microsoft, AWS, Google Cloud  
**Standards Aligned To:** CIS Benchmarks · NIST CSF · ISO/IEC 27001 · CSA CCM · Zero Trust

---

## Overview

This framework defines the security and compliance controls required for enterprise cloud deployments across **Azure**, **AWS**, and **Google Cloud Platform**. It is structured around the **NIST Cybersecurity Framework (CSF)** functions and maps to major compliance standards.

---

## Zero Trust Architecture Principles

Cloud security is built on **Zero Trust** — "Never Trust, Always Verify."

| Principle | Implementation |
|---|---|
| **Verify Explicitly** | Authenticate and authorize every request (identity, device, location, service) |
| **Use Least Privilege** | RBAC/ABAC — grant minimum required permissions; time-bound access |
| **Assume Breach** | Segment networks, encrypt all data, assume adversary presence |

**Zero Trust Pillars:**

```
Identity → Devices → Applications → Data → Infrastructure → Networks
    ↕           ↕           ↕         ↕          ↕              ↕
 Entra ID /  Intune /    App        Data       Azure         NSG /
 AWS IAM /   MDM         Proxy /    Class.     Defender /    GuardDuty /
 GCP IAM                 CASB       DLP        AWS Shield    Cloud Armor
```

---

## NIST CSF Framework Controls

### Function 1: Identify (ID)

| Control | Azure | AWS | GCP |
|---|---|---|---|
| Asset inventory | Azure Resource Graph | AWS Config | Cloud Asset Inventory |
| Risk assessment | Microsoft Defender for Cloud | AWS Security Hub | Security Command Center |
| Data classification | Microsoft Purview | AWS Macie | Cloud DLP |
| Supply chain risk | Defender for DevOps | Amazon Inspector | Binary Authorization |

### Function 2: Protect (PR)

**Identity & Access Management:**

| Control | Azure | AWS | GCP |
|---|---|---|---|
| Identity provider | Microsoft Entra ID (AAD) | AWS IAM Identity Center | Cloud Identity / Workspace |
| MFA enforcement | Conditional Access + MFA | IAM MFA policy | MFA on Cloud Identity |
| Privileged access | Entra ID PIM | AWS IAM + Just-in-Time | Privileged Access Manager |
| Service accounts | Managed Identities | IAM Roles for EC2/Lambda | Service Accounts (workload identity) |
| Secrets management | Azure Key Vault | AWS Secrets Manager | Secret Manager |

**Data Protection:**

| Control | Requirement |
|---|---|
| Encryption at rest | AES-256 minimum; customer-managed keys (CMK) for sensitive data |
| Encryption in transit | TLS 1.2+ enforced; no plaintext protocols (HTTP, Telnet, FTP) |
| Key management | Azure Key Vault HSM / AWS CloudHSM / GCP Cloud HSM |
| Data residency | Enforce region-locked storage for regulated data (GDPR, data sovereignty) |
| Backup encryption | All backup copies encrypted with CMK |

**Network Security:**

| Control | Azure | AWS | GCP |
|---|---|---|---|
| Network segmentation | VNet + NSG + ASG | VPC + Security Groups + NACLs | VPC + Firewall Rules |
| DDoS protection | Azure DDoS Protection Standard | AWS Shield Advanced | Cloud Armor |
| WAF | Azure Application Gateway WAF | AWS WAF | Cloud Armor WAF |
| Private connectivity | Private Endpoints | VPC Endpoints / PrivateLink | Private Service Connect |
| Firewall | Azure Firewall Premium | AWS Network Firewall | Cloud NGFW |
| DNS security | Azure Private DNS + Resolver | Route 53 Resolver DNS Firewall | Cloud DNS |

### Function 3: Detect (DE)

| Control | Azure | AWS | GCP |
|---|---|---|---|
| Threat detection | Microsoft Sentinel + Defender XDR | AWS GuardDuty | Security Command Center + Chronicle |
| Log aggregation | Log Analytics Workspace | CloudWatch Logs + S3 | Cloud Logging (Cloud Storage sink) |
| Audit logging | Azure Monitor Activity Log | CloudTrail | Cloud Audit Logs |
| Vulnerability scanning | Defender for Cloud (CSPM) | Amazon Inspector | SCC Vulnerability Reports |
| Container scanning | Defender for Containers | Amazon ECR scanning | Artifact Registry scanning |

**Logging Retention Standards:**

| Log Type | Minimum Retention |
|---|---|
| Authentication / IAM events | 12 months (hot), 7 years (cold archive) |
| API call logs (CloudTrail/Activity Log) | 12 months |
| Network flow logs | 90 days |
| Application logs | 90 days (or per regulatory requirement) |
| Security alerts | 2 years |

### Function 4: Respond (RS)

**Incident Response Plan (Cloud-Specific):**

1. **Detection:** Alert triggered by SIEM/CSPM
2. **Triage:** SOC analyst reviews severity (P1–P4 classification)
3. **Containment:**
   - Azure: Revoke Entra ID tokens, disable user, apply NSG deny-all
   - AWS: Attach Deny-all IAM policy, isolate EC2 with SG update, revoke credentials
   - GCP: Disable service account, apply Org Policy deny, quarantine VPC
4. **Eradication:** Remove malicious access, patch vulnerability, rotate credentials
5. **Recovery:** Restore from known-good backup; validate before go-live
6. **Post-Incident:** Root cause analysis, lessons learned, control improvements

**Escalation Matrix:**

| Severity | Response SLA | Escalation |
|---|---|---|
| P1 – Critical (active breach) | 15 minutes | CISO + Cloud Architects + Vendor TAM |
| P2 – High (confirmed threat) | 1 hour | Security Lead + Cloud Operations |
| P3 – Medium (suspicious activity) | 4 hours | SOC Analyst + Security Lead |
| P4 – Low (anomaly/informational) | 24 hours | SOC Analyst |

### Function 5: Recover (RC)

| Control | Requirement |
|---|---|
| RTO (Recovery Time Objective) | Defined per workload tier (Tier 1: <1h, Tier 2: <4h, Tier 3: <24h) |
| RPO (Recovery Point Objective) | Defined per workload tier (Tier 1: <15min, Tier 2: <1h, Tier 3: <24h) |
| Backup testing | Monthly restore tests; quarterly DR failover test |
| Runbook documentation | DR runbook for each Tier 1 and Tier 2 workload |

---

## Compliance Standards Mapping

| Standard | Azure | AWS | GCP |
|---|---|---|---|
| **ISO/IEC 27001** | Azure Compliance Manager | AWS Audit Manager | SCC Compliance Dashboard |
| **SOC 2 Type II** | Built-in CSP compliance | Built-in CSP compliance | Built-in CSP compliance |
| **GDPR** | Microsoft Privacy Shield + Purview | AWS GDPR Center | Google Cloud GDPR |
| **HIPAA** | Azure HIPAA BAA | AWS HIPAA BAA | GCP HIPAA BAA |
| **PCI DSS v4** | Azure PCI DSS Blueprint | AWS PCI DSS Quick Start | GCP PCI DSS Reference Architecture |
| **FedRAMP** | Azure Government (FedRAMP High) | AWS GovCloud (FedRAMP High) | Google FedRAMP Moderate |
| **NIST 800-53** | Azure NIST Policy Initiative | AWS NIST Config Rules | GCP NIST Constraints |
| **CIS Benchmarks** | Azure CIS Policy Initiative | AWS CIS Config Rules | GCP CIS Org Policies |

---

## Security Hardening Checklist

### Identity & Access
- [ ] MFA enforced for all user accounts (no exceptions)
- [ ] Privileged accounts use PIM/JIT access (no standing admin)
- [ ] Service accounts use managed identities (no stored credentials)
- [ ] External access reviewed quarterly; guest/vendor accounts time-bounded
- [ ] IAM policies follow least privilege; no wildcard permissions in production

### Network
- [ ] All production traffic uses private endpoints / PrivateLink / PSC
- [ ] No resources exposed directly to internet without WAF protection
- [ ] VPC/VNet flow logs enabled and forwarded to SIEM
- [ ] Firewall rules documented; unused rules reviewed quarterly

### Data
- [ ] All data classified; sensitive data tagged appropriately
- [ ] Encryption at rest enabled for all storage (CMK for sensitive workloads)
- [ ] TLS 1.2+ enforced; SSL inspection enabled on egress proxy
- [ ] DLP policies active on sensitive data stores and egress channels

### Operations
- [ ] Cloud security posture score monitored weekly (Defender for Cloud / Security Hub / SCC)
- [ ] Vulnerability management SLA: Critical <24h, High <72h, Medium <30d
- [ ] Penetration testing conducted annually
- [ ] Security awareness training completed by all cloud users

---

*See also: [Governance Framework](../governance/cloud-governance-framework.md) | [Azure Migration Guide](../frameworks/azure/azure-migration-guide.md) | [AWS Migration Guide](../frameworks/aws/aws-migration-guide.md)*
