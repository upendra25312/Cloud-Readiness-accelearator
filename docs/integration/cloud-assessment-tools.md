# Cloud Assessment Tool Integration Guide

**Version**: 1.0 | **Task**: 10.3 | **Requirements**: 10.3, 15.3

---

## Overview

This guide covers integrating data from cloud provider assessment tools into the Cloud Readiness Accelerator framework.

---

## AWS Migration Evaluator

### Data Collection
1. Install Migration Evaluator collector agent on target servers
2. Collect 2-4 weeks of utilization data
3. Export assessment report from Migration Evaluator console

### Key Outputs to Extract
| Output | Maps To | Template |
|--------|---------|---------|
| Server inventory | Infrastructure Profiling Template | Section 1 |
| Right-sizing recommendations | AWS Evaluation Template | Section 1 |
| Cost projections (On-Demand, RI, SP) | AWS Evaluation Template | Section 3 |
| License optimization | Business Case Template | Section 2 |

### Export Format: Excel/CSV from Migration Evaluator dashboard

---

## Azure Migrate

### Data Collection
1. Deploy Azure Migrate appliance in on-premises environment
2. Run discovery (agentless or agent-based)
3. Run assessment for target Azure region

### Key Outputs to Extract
| Output | Maps To | Template |
|--------|---------|---------|
| Discovered servers | Infrastructure Profiling Template | Section 1 |
| Azure readiness | Azure Evaluation Template | Section 1 |
| Cost estimates (PAYG, AHB, RI) | Azure Evaluation Template | Section 3 |
| Dependency visualization | Dependency Mapping Template | Section 1 |
| SQL assessment | Azure Evaluation Template | Database Mapping |

### Export Format: Excel from Azure Migrate portal, JSON via REST API

---

## Google Cloud Migrate for Compute Engine

### Data Collection
1. Deploy Migrate for Compute Engine in source environment
2. Run discovery and assessment
3. Export fit assessment report

### Key Outputs to Extract
| Output | Maps To | Template |
|--------|---------|---------|
| Server inventory | Infrastructure Profiling Template | Section 1 |
| GCP fit assessment | GCP Evaluation Template | Section 1 |
| Cost estimates | GCP Evaluation Template | Section 3 |
| Migration complexity | GCP Evaluation Template | Section 5 |

### Export Format: CSV/Excel from Google Cloud Console

---

## RVTools (VMware Environments)

### Data Collection
1. Run RVTools against vCenter
2. Export all tabs to Excel

### Key Tabs to Extract
| Tab | Maps To | Template |
|-----|---------|---------|
| vInfo | Server inventory (VM details) | Infrastructure Profiling |
| vCPU | CPU configuration | Infrastructure Profiling Section 5 |
| vMemory | Memory configuration | Infrastructure Profiling Section 5 |
| vDisk | Storage configuration | Infrastructure Profiling Section 3 |
| vNetwork | Network configuration | Infrastructure Profiling Section 4 |

---

## Data Normalization Procedures

### Server Sizing Normalization
| Source Tool | CPU Field | Memory Field | Storage Field | Normalization |
|-----------|----------|-------------|--------------|--------------|
| AWS Migration Evaluator | vCPUs | Memory (GiB) | Storage (GiB) | Direct |
| Azure Migrate | Cores | Memory (MB) | Disk (GB) | Memory: MB→GB |
| RVTools | Num CPUs | Memory (MB) | Provisioned (MB) | Memory/Storage: MB→GB |
| CMDB | cpu_count | ram (varies) | disk_space (varies) | Check units |

### Cost Normalization
- Normalize all costs to same currency (£/$/€)
- Normalize to monthly or annual periods
- Include/exclude support costs consistently
- Document exchange rates and date used

---

## Validation Checklist

- [ ] Tool data covers >95% of in-scope servers
- [ ] Collection period meets minimum (2-4 weeks)
- [ ] Data cross-referenced with CMDB inventory
- [ ] Discrepancies documented and resolved
- [ ] Cost estimates validated against current invoices
- [ ] Right-sizing recommendations reviewed by app owners

---

*Guide Version 1.0 — Cloud Readiness Accelerator Framework*
