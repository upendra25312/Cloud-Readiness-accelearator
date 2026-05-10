# Migration RACI Matrix Template

**Project:** ___________________________  
**Cloud:** ☐ Azure  ☐ AWS  ☐ GCP  
**Version:** 1.0  
**Date:** ___________________________

---

## Legend

| Code | Role |
|---|---|
| **R** | Responsible — Does the work |
| **A** | Accountable — Owns the outcome (only one per row) |
| **C** | Consulted — Provides input before/during |
| **I** | Informed — Notified of outcome |

---

## RACI Matrix

| Activity | Cloud Architect | Project Manager | Application Team | Security Team | Network Team | FinOps/Finance | Executive Sponsor |
|---|---|---|---|---|---|---|---|
| **Strategy & Planning** | | | | | | | |
| Define cloud strategy | C | C | I | C | I | C | A |
| Build business case | C | R | C | I | I | R | A |
| Portfolio rationalization | R | C | C | I | I | I | I |
| Migration wave planning | R | A | C | C | C | I | I |
| **Landing Zone** | | | | | | | |
| Landing zone design | R/A | I | C | C | C | I | I |
| Landing zone deployment | R | C | I | C | R | I | I |
| Network architecture design | C | I | I | C | R/A | I | I |
| IAM/RBAC design | C | I | I | R/A | I | I | I |
| Policy & governance setup | R | I | I | C | I | C | I |
| **Migration Execution** | | | | | | | |
| Pre-migration assessment | R | C | C | C | C | I | I |
| Migration wave execution | C | R/A | R | C | C | I | I |
| Application testing (post-migration) | C | C | R/A | C | I | I | I |
| Go/No-Go decision | A | C | C | C | C | I | C |
| Cutover execution | C | A | R | C | R | I | I |
| **Security & Compliance** | | | | | | | |
| Security baseline implementation | C | I | I | R/A | C | I | I |
| Compliance assessment | C | C | I | R/A | I | I | I |
| Penetration testing | I | C | I | R/A | I | I | I |
| **Governance & FinOps** | | | | | | | |
| Tagging standards definition | C | C | C | I | I | R/A | I |
| Budget setup & alerts | I | C | I | I | I | R/A | C |
| Cost reporting | I | I | I | I | I | R/A | I |
| **Operations** | | | | | | | |
| Monitoring setup | C | C | R | C | C | I | I |
| Runbook documentation | C | C | R/A | C | C | I | I |
| DR/BCDR validation | R | A | C | C | C | I | I |
| Post-migration optimization | R | C | C | C | C | C | I |

---

## Project Contacts

| Role | Name | Email | Organization |
|---|---|---|---|
| Cloud Architect | | | |
| Project Manager | | | |
| Application Lead | | | |
| Security Lead | | | |
| Network Lead | | | |
| FinOps Lead | | | |
| Executive Sponsor | | | |
| CSP TAM / Partner | | | |

---

*Reference: [Cloud Governance Framework](../governance/cloud-governance-framework.md) | [Azure Migration Guide](../frameworks/azure/azure-migration-guide.md)*
