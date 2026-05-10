# Pre-Sales & Alliance Partner Playbook

**Version:** 2.0  
**Authors:** Pre-Sales Architects & Alliance Partner Teams — Microsoft, AWS, Google Cloud  
**Audience:** Sales Engineers, Solution Architects, Alliance Managers, Partner Success Managers

---

## Overview

This playbook equips pre-sales architects and alliance partners with the tools, conversation frameworks, discovery guides, and competitive positioning needed to effectively qualify, assess, and win cloud readiness and migration opportunities across **Microsoft Azure**, **AWS**, and **Google Cloud Platform**.

---

## Opportunity Qualification Framework

### The MEDDPICC Qualification Model for Cloud Deals

| Letter | Element | Cloud Context |
|---|---|---|
| **M** | Metrics | Quantified business outcomes: 30% cost reduction, 50% faster deployments |
| **E** | Economic Buyer | CISO, CTO, CIO, CFO — who controls the cloud budget? |
| **D** | Decision Criteria | Security, compliance, TCO, partner ecosystem, support SLA |
| **D** | Decision Process | RFP? POC? Single-vendor? Board approval required? |
| **P** | Paper Process | Procurement, legal review, MSA, volume discount agreements |
| **I** | Identify Pain | Legacy tech debt, datacenter exit, digital transformation pressure |
| **C** | Champion | Internal advocate — who wins internally if this succeeds? |
| **C** | Competition | Competing cloud providers, SI partners, internal "do it ourselves" |

---

## Discovery Conversation Guide

### Phase 1: Business Discovery (C-Suite/Executive)

**Key Questions:**
1. What are your top 3 strategic priorities for the next 18 months?
2. What is driving your cloud initiative — cost, agility, innovation, compliance, or datacenter exit?
3. What does success look like 12–24 months from now? How will it be measured?
4. What is your timeline and what is the burning platform (if any)?
5. What concerns do you have about cloud adoption (security, cost, skills, vendor lock-in)?
6. Who are the key stakeholders that need to be aligned for this initiative?

**Executive Pain Points → Cloud Narrative:**

| Pain Point | Cloud Value Proposition |
|---|---|
| "Our IT costs are too high" | TCO analysis: 30–60% reduction with right-sizing + reserved capacity + Azure Hybrid Benefit |
| "We can't deploy fast enough" | DevOps + IaC + cloud-native: from months to hours for new environments |
| "We had a security breach / audit failure" | Zero Trust, SIEM, CSPM, compliance-as-code |
| "Our datacenter lease is expiring" | Datacenter exit program: fixed timeline, proven migration factory |
| "Our competitors are moving faster" | Cloud innovation: AI/ML, microservices, global scale in days |
| "We're struggling to hire and retain engineers" | Cloud-first attracts talent; developers want modern platforms |

---

### Phase 2: Technical Discovery (IT / Architecture)

**Key Questions:**
1. How many applications are in your portfolio? What is the breakdown (web, DB, mainframe, packaged)?
2. What is your current infrastructure (VMware, Hyper-V, bare metal, colocation, AWS/Azure/GCP)?
3. What are your top 5 most critical / highest-revenue applications?
4. What are your compliance and regulatory requirements (GDPR, HIPAA, PCI, FedRAMP, SOC 2)?
5. What identity platform do you use (Active Directory, Okta, Ping Identity)?
6. What DevOps tools are in place (CI/CD, source control, ticketing)?
7. What is your current monitoring and observability stack?
8. What is your network architecture (MPLS, SD-WAN, internet edge)?

**Technical Pain Points → Cloud Architecture Response:**

| Technical Pain | Solution |
|---|---|
| VMware license cost spike | Azure VMware Solution / AWS VMware Cloud / GCP VMware Engine — migrate without refactor |
| SQL Server license costs | Azure SQL MI + Hybrid Benefit, RDS with BYOL, Cloud SQL |
| Disaster recovery complexity | Azure Site Recovery, AWS DRS, GCP Backup and DR |
| Manual infrastructure provisioning | IaC with Terraform/Bicep/CDK; self-service landing zones |
| Security compliance reporting | Defender for Cloud / Security Hub / SCC — automated compliance dashboards |

---

## ROI & Business Case Framework

### TCO Components to Model

**On-Premises Costs (3-Year View):**
- Hardware refresh (servers, storage, networking): purchase + maintenance
- Datacenter costs: power, cooling, colocation fees
- Software licenses: OS, middleware, databases, virtualization (VMware)
- IT staffing: infrastructure operations, security, database admin
- Disaster recovery infrastructure (secondary datacenter)

**Cloud Costs (3-Year View):**
- Compute (reserved instances / committed use discounts)
- Storage (object, block, archive)
- Networking (ingress free, egress costs, ExpressRoute/Direct Connect/Interconnect)
- Managed services (PaaS databases, Kubernetes, serverless)
- Cloud management tooling

**Value Benefits (Hard):**
- Infrastructure cost reduction: typically 30–50%
- License savings: Azure Hybrid Benefit up to 40% additional
- Datacenter exit savings: colocation + power + cooling eliminated
- Staff redeployment from "run the infrastructure" to "run the business"

**Value Benefits (Soft):**
- Faster time-to-market for new products/features
- Improved application availability (99.99% SLA vs. typical on-prem 99.5%)
- Business agility (scale up/down in minutes vs. months for hardware)
- Innovation acceleration (AI/ML, IoT, big data — cloud-native)

**Business Case Template:** `../templates/business-case-template.md`

---

## Competitive Positioning

### Azure vs. AWS vs. GCP: When to Lead With Each

#### Lead with Azure when:
- Customer is Microsoft-heavy (M365, Teams, Active Directory, Dynamics 365, SQL Server)
- SAP on Azure is a strong pull (Microsoft + SAP preferred partnership)
- Regulated industries in Europe (data residency, GDPR-specific Azure commitments)
- Strong existing Microsoft enterprise agreements (EA) — consolidate under MACC
- AI/GenAI opportunities (Azure OpenAI is the enterprise GenAI leader)

#### Lead with AWS when:
- Customer has no dominant cloud vendor (greenfield)
- Startup / ISV / SaaS-native workloads
- Deepest breadth of cloud services (over 200+ services)
- Strongest global partner ecosystem for migrations (MAP program)
- High-performance computing (HPC) / semiconductor / genomics workloads

#### Lead with GCP when:
- Data, analytics, and AI are the primary drivers (BigQuery, Vertex AI)
- Kubernetes-native shops (GKE is the market reference)
- Cost competitiveness matters (GCP pricing often lower, CUDs auto-applied)
- Google Workspace customer (natural extension to GCP)
- Open-source community alignment (Google created Kubernetes, TensorFlow)

---

## Alliance Partner Programs

### Microsoft Partner Network (MPN) / Cloud Partner Program

| Program | Benefits |
|---|---|
| **Solutions Partner for Azure** | Lead referrals, GTM co-funding, marketplace listing |
| **Azure Expert MSP** | Premier managed service recognition, top-of-funnel referrals |
| **ISV Co-Sell** | Microsoft sellers co-sell your solution with Azure |
| **MACC (Microsoft Azure Consumption Commitment)** | Customer commitments count toward your marketplace sales |
| **FastTrack for Azure** | Free Microsoft engineering support for qualified deployments |

### AWS Partner Network (APN)

| Program | Benefits |
|---|---|
| **AWS Select / Advanced / Premier Tier** | Tiered benefits based on certifications + revenue |
| **AWS Migration Acceleration Program (MAP)** | Funding for migration assessments and delivery |
| **AWS Marketplace** | Sell solutions on AWS Marketplace; co-sell with AWS sellers |
| **AWS ISV Accelerate** | Co-sell program for ISVs with AWS-compatible solutions |
| **AWS Competencies** | Differentiation in specific domains (Security, Migration, Analytics) |

### Google Cloud Partner Advantage

| Program | Benefits |
|---|---|
| **Services Partner** | Tiered (Member, Partner, Premier) based on certifications + CCAI |
| **Google Cloud Marketplace** | List and transact solutions; co-sell with Google Cloud sellers |
| **ISV Specialization** | Recognized expertise in Google Cloud solution areas |
| **PSO Referrals** | Google Professional Services referrals to certified partners |
| **Customer Engagements (CE)** | Funded engagements for qualified migrations and modernizations |

---

## Pre-Sales Engagement Checklist

### Discovery Phase
- [ ] Completed executive discovery conversation (business drivers, outcomes, timeline)
- [ ] Completed technical discovery (portfolio, compliance, architecture, tooling)
- [ ] Identified champion and economic buyer
- [ ] Qualified against MEDDPICC criteria

### Assessment Phase
- [ ] Delivered Cloud Readiness Assessment ([assessments/cloud-readiness-assessment.md](../assessments/cloud-readiness-assessment.md))
- [ ] Proposed landing zone architecture aligned to customer requirements
- [ ] Built directional TCO/ROI business case

### Proposal Phase
- [ ] Proposed phased migration roadmap (3-year horizon)
- [ ] Included relevant reference architectures and customer case studies
- [ ] Identified partner funding programs (MAP, MACC, GCP CE)
- [ ] Included managed services / support options

### Close Phase
- [ ] Executive business case presentation completed
- [ ] Proof-of-concept (POC) or pilot scope agreed
- [ ] Contract/MSA aligned; procurement process mapped
- [ ] Kickoff meeting scheduled

---

*See also: [Cloud Readiness Assessment](../assessments/cloud-readiness-assessment.md) | [Multi-Cloud Strategy](../frameworks/multi-cloud/multi-cloud-strategy.md) | [FinOps Framework](../cost-optimization/finops-framework.md)*
