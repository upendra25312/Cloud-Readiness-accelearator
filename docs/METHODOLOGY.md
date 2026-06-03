# Cloud Readiness Accelerator - Assessment Methodology Overview

## Executive Summary

The Cloud Readiness Accelerator provides a comprehensive, four-phase assessment methodology designed to enable organizations to systematically evaluate their cloud migration readiness. This methodology combines structured discovery, multi-dimensional analysis, rigorous evaluation, and strategic planning to produce actionable insights for cloud migration decision-making.

The four-phase approach—Discovery, Analysis, Evaluation, and Planning—guides organizations through a complete assessment lifecycle, from initial application inventory through detailed migration roadmap development. Each phase builds on the previous one, with clear entry/exit criteria, defined activities, and measurable success criteria.

> **Timeline note (v2 — audited).** Phase durations in this document have been updated to reflect a Sr Director–level audit of real-world delivery patterns. They explicitly account for: discovery tooling stand-up time (CAB lead time for firewall changes, service-account provisioning, appliance certification); a troubleshooting reserve for on-prem firewall and OS-level access constraints; and a **minimum two-week utilization-data window** (target four weeks) before right-sizing recommendations are considered confident. Aggressive compression of these windows is the leading cause of unreliable assessment outputs.

---

## Assessment Methodology Overview

### Four-Phase Assessment Model

The Cloud Readiness Accelerator implements a structured four-phase assessment workflow:

```
Phase 1: Discovery
    ↓
Phase 2: Analysis
    ↓
Phase 3: Evaluation
    ↓
Phase 4: Planning
```

Each phase has distinct objectives, activities, and deliverables that progressively build a comprehensive understanding of the organization's cloud readiness.

### Sequential vs. Parallelized Delivery

Phase 2 (Analysis) can be parallelized with the back half of Phase 1 (Discovery) because application-owner interviews, criticality classification, and compliance review do not require completed utilization data — only the validated inventory. This compression reduces elapsed duration by approximately 25–30% without compromising data quality. Phase 3 (Evaluation) cannot start until at least two weeks of clean utilization data has been collected, regardless of parallelization choices.

---

## Phase 1: Discovery

### Phase Objectives

The Discovery phase establishes the foundation for the entire assessment by identifying all applications and infrastructure in scope, understanding organizational context, and collecting baseline data.

**Primary Objectives:**
- Identify and engage all relevant stakeholders
- Define assessment scope and boundaries
- Stand up discovery tooling and resolve on-prem access constraints
- Create comprehensive application and infrastructure inventory
- Map application and infrastructure dependencies
- Collect a minimum of two weeks (target four weeks) of utilization data
- Establish governance structure and decision-making framework

### Phase Activities

#### 1.1 Stakeholder Identification and Engagement
- Identify all stakeholders across business, technology, and operations
- Conduct stakeholder interviews to understand priorities and constraints
- Establish governance structure (steering committee, working groups)
- Define roles and responsibilities
- Create communication and engagement plan
- **Duration:** 1–2 weeks (runs in parallel with 1.2 and 1.3)
- **Resources:** Assessment lead, business analyst, stakeholder management specialist

#### 1.2 Scope Definition and Validation
- Define assessment scope (applications, infrastructure, business units, geographies)
- Identify scope boundaries and exclusions
- Document scope assumptions and constraints
- Validate scope with stakeholders
- Create scope statement and change control procedures
- **Duration:** 1 week
- **Resources:** Assessment lead, business analyst

#### 1.3 Discovery Tooling Setup
- Design discovery architecture (Azure Migrate appliance, RVTools, native exports)
- Submit firewall and network change requests through CAB (allow 5–10 business days)
- Provision service accounts and credential vault
- Deploy and certify the discovery appliance per site
- Run an initial connectivity and data-flow test on a 10-host pilot
- **Reserve a 1-week troubleshooting buffer** for known data-capture issues: on-prem firewall egress blocks, WMI / SSH / SNMP failures, OS-level GPO and PowerShell ExecutionPolicy restrictions, and sudoers misconfiguration
- **Duration:** 3 weeks
- **Resources:** Discovery architect, network SME, security SME

**Discovery tooling selection and alliance programme implications:**

| Tool | Primary Use Case | Alliance Programme Note |
|---|---|---|
| Azure Migrate appliance | Azure-primary engagements; VMware vCenter ≥ 6.5; outputs feed Azure Migrate assessment and AHB modelling | Required for AMM deliverable completeness; CAB lead time 5–10 days |
| AWS Application Discovery Service (ADS) | AWS-primary engagements; required if pursuing MAP funding | **MAP requires ADS or an AWS-approved partner tool** — GCP Migration Center outputs alone do not satisfy MAP discovery evidence requirements |
| GCP Migration Center | GCP-primary engagements; strong agentless VMware coverage; good for multi-cloud baseline | Can be used as the primary discovery tool for non-AWS engagements; does not satisfy MAP evidence |
| RVTools | Supplementary VM inventory from vCenter; fast; no network change required | Good pilot tool and cross-check; not sufficient as sole discovery source for AMM/MAP |

> If the engagement is likely to lead to an AWS recommendation and MAP funding, deploy ADS alongside the primary tool from Day 1 of tooling setup. Retrofitting ADS after Phase 1 is complete is time-consuming and may jeopardise MAP eligibility.

#### 1.4 Application Inventory Collection
- Extract application list from CMDB or via discovery tooling
- Collect application metadata (name, owner, criticality, platform, tech stack)
- Document application architecture patterns
- Identify application owners and technical contacts
- Validate application inventory with stakeholders
- **Duration:** 2 weeks (runs in parallel with 1.5 and 1.6 utilization collection)
- **Resources:** Assessment team, application owners, CMDB administrators

#### 1.5 Infrastructure Profiling and Utilization Data Collection
- Continuously collect infrastructure inventory and utilization metrics (CPU, memory, storage, network)
- Document server specifications, OS versions, database configurations
- **Collect a minimum of 2 weeks of clean utilization data; target 4 weeks** to capture weekly seasonality (month-end batch jobs, weekend reporting cycles, payroll runs)
- Run daily appliance health checks and re-sync for any disconnects
- Re-discover the expected 10–15% of hosts that fail initial collection due to credential, network, or agent issues
- Validate inventory completeness against stakeholder-approved scope
- **Duration:** 4 weeks (target window for capturing weekly seasonality)
- **Resources:** Assessment team, infrastructure teams, discovery architect

#### 1.6 Dependency Mapping
- Document application-to-application dependencies (synchronous, asynchronous)
- Document application-to-infrastructure dependencies
- Identify external dependencies (third-party services, APIs)
- Create dependency diagrams and relationship maps
- Validate dependencies with technical teams
- **Duration:** 2–3 weeks (runs in parallel with the back half of 1.5)
- **Resources:** Assessment team, application architects, technical leads

### Phase Entry Criteria

- Executive sponsorship and commitment secured
- Assessment budget and resources allocated
- Stakeholder list identified and initial engagement completed
- Scope definition initiated with business stakeholders
- Access to CMDB, monitoring systems, and other data sources confirmed
- CAB process and lead times understood and reflected in the schedule

### Phase Exit Criteria

- Inventory completeness ≥ 95% of in-scope servers
- Utilization data ≥ 2 weeks (target 4 weeks) for ≥ 95% of in-scope servers
- Dependency map coverage ≥ 90% of in-scope servers
- All stakeholders confirm scope and inventory accuracy
- Discovery tooling is operational and re-discovery cycles are complete
- Governance structure established with first steering committee meeting held

### Phase Success Criteria

- **Completeness:** ≥ 95% of applications and infrastructure in scope documented
- **Accuracy:** Inventory data validated against source systems with < 5% discrepancies
- **Data Quality:** Utilization data window meets the 2-week minimum (4-week target)
- **Stakeholder Alignment:** All stakeholders confirm scope and inventory accuracy
- **Timeline:** Phase completed within planned timeline (typically 6–10 weeks for mid-market)
- **Governance:** Governance structure established and first steering committee meeting held

### Phase Deliverables

- Application Inventory (spreadsheet with all applications and metadata)
- Infrastructure Inventory and Utilization Dataset (≥ 2 weeks continuous data)
- Dependency Map (visual and tabular representation of dependencies)
- Discovery Architecture Design (tooling, ports, accounts, troubleshooting log)
- Stakeholder Engagement Plan (communication strategy and cadence)
- Governance Charter (roles, responsibilities, decision authorities)
- Assessment Scope Statement (scope, boundaries, assumptions)
- Data Quality Report (completeness, accuracy, and confidence-level assessment)

### Estimated Timeline and Resources

| Aspect | Details |
|--------|---------|
| **Phase Duration (mid-market default)** | **7 weeks** (3 weeks tooling setup + 4 weeks data collection / inventory in parallel) |
| **Small Org (10–50 apps, < 200 servers)** | 5–6 weeks |
| **Mid-Market (50–200 apps, 200–1,500 servers)** | 7 weeks |
| **Enterprise (200+ apps, 1,500+ servers)** | 9–10 weeks |
| **Core Team Size** | 3–5 people |
| **Effort (Small Org)** | 400–600 hours |
| **Effort (Mid-Market)** | 800–1,200 hours |
| **Effort (Enterprise)** | 1,600–2,400 hours |

> **Audit note.** The previous version of this methodology cited 4–8 weeks for Discovery. That estimate compressed both tooling stand-up and the utilization-data window into the same period. The revised range separates them: a 3-week tooling-setup floor (driven by CAB lead time and OS-level troubleshooting) plus a 4-week data window (driven by weekly seasonality) yields a realistic 7 weeks for the mid-market default.

### Stakeholder Engagement Guidance

**Executive Stakeholders:**
- Frequency: Monthly steering committee meetings
- Focus: Budget, timeline, scope changes, escalations
- Engagement: Executive summary updates, decision requests

**Business Stakeholders:**
- Frequency: Bi-weekly working group meetings
- Focus: Application criticality, business priorities, scope validation
- Engagement: Detailed findings, business impact analysis

**Technical Stakeholders:**
- Frequency: Weekly technical working group meetings
- Focus: Application details, dependencies, technical constraints
- Engagement: Detailed technical assessments, remediation planning

**Operations Stakeholders:**
- Frequency: Weekly operational working group meetings
- Focus: Performance data, operational procedures, support requirements
- Engagement: Operational assessment, support model evaluation

---

## Phase 2: Analysis

### Phase Objectives

The Analysis phase evaluates applications and infrastructure across multiple dimensions to understand technical, operational, security, compliance, and business characteristics.

**Primary Objectives:**
- Conduct detailed technical assessment of applications
- Evaluate operational maturity and readiness
- Assess security posture and controls
- Identify compliance requirements and constraints
- Analyze performance characteristics and sizing requirements
- Develop detailed application profiles for readiness scoring

> **Parallelization note.** Phase 2 begins approximately one week before Phase 1 ends. Application-owner interviews, criticality classification, and compliance review only require a validated inventory (available by mid-Phase 1), not a completed utilization dataset.

### Phase Activities

#### 2.1 Application Technical Assessment
- Evaluate application architecture (monolithic, microservices, serverless)
- Assess technology stack compatibility with cloud platforms
- Identify technical dependencies and constraints
- Evaluate application modernization opportunities
- Document technical remediation requirements
- **Duration:** 2–3 weeks
- **Resources:** Solution architects, technical leads, application experts

#### 2.2 Operational Assessment
- Evaluate automation maturity (deployment, configuration, scaling)
- Assess monitoring and observability capabilities
- Evaluate incident response and support procedures
- Assess operational complexity and staffing requirements
- Identify operational improvements needed for cloud
- **Duration:** 1–2 weeks
- **Resources:** Operations managers, DevOps engineers, support teams

#### 2.3 Security Assessment
- Evaluate identity and access management controls
- Assess encryption and data protection measures
- Evaluate vulnerability management procedures
- Assess security controls and compliance with standards
- Identify security gaps and remediation needs
- **Duration:** 1–2 weeks
- **Resources:** Security architects, security engineers, compliance specialists

#### 2.4 Compliance Assessment
- Identify applicable compliance frameworks (HIPAA, PCI-DSS, GDPR, SOC2, etc.)
- Document regulatory requirements for each application
- Assess current compliance status
- Identify compliance gaps and remediation needs
- Evaluate hyperscaler compliance certifications
- **Duration:** 1–2 weeks
- **Resources:** Compliance officers, legal counsel, compliance specialists

#### 2.5 Performance Analysis
- Analyze CPU, memory, storage, and network utilization (uses Phase 1.5 dataset)
- Identify performance bottlenecks and constraints
- Assess scalability requirements and patterns
- Evaluate database performance and sizing
- Document performance optimization opportunities
- **Duration:** 1–2 weeks
- **Resources:** Performance engineers, database administrators, infrastructure teams

#### 2.6 Dependency Analysis
- Analyze application-to-application dependency chains
- Identify critical paths and bottlenecks
- Assess tight coupling and integration patterns
- Evaluate external service dependencies
- Document dependency constraints for migration planning
- **Duration:** 1–2 weeks
- **Resources:** Solution architects, application architects, technical leads

### Phase Entry Criteria

- Phase 1 (Discovery) inventory validated (utilization collection may still be in progress)
- Assessment team trained on analysis methodology
- Analysis templates and tools prepared
- Access to application owners and technical experts confirmed
- Stakeholder engagement plan active

### Phase Exit Criteria

- Technical assessment completed for all applications in scope
- Operational assessment completed for all applications
- Security assessment completed for all applications
- Compliance requirements documented for all applications
- Performance analysis completed for all applications (using ≥ 2 weeks of utilization data)
- Dependency analysis completed and validated
- All assessment data entered into analysis tools
- Data quality validation completed

### Phase Success Criteria

- **Completeness:** Technical, operational, security, compliance, and performance assessments completed for ≥ 95% of applications
- **Data Quality:** All required assessment fields populated for ≥ 95% of applications
- **Accuracy:** Assessment findings validated with application owners and technical experts
- **Stakeholder Alignment:** Business stakeholders confirm assessment accuracy
- **Timeline:** Phase completed within planned timeline (typically 4 weeks for mid-market)
- **Documentation:** All assessment rationale and supporting evidence documented

### Phase Deliverables

- Technical Assessment Report (architecture, technology stack, modernization opportunities)
- Operational Assessment Report (automation, monitoring, incident response maturity)
- Security Assessment Report (controls, vulnerabilities, remediation needs)
- Compliance Assessment Report (regulatory requirements, compliance gaps)
- Performance Analysis Report (utilization, bottlenecks, sizing requirements)
- Dependency Analysis Report (dependency chains, critical paths, constraints)
- Application Profile Database (detailed profiles for all applications)
- Assessment Data Quality Report (completeness and accuracy metrics)

### Estimated Timeline and Resources

| Aspect | Details |
|--------|---------|
| **Phase Duration (mid-market default)** | **4 weeks** (parallelized with the back half of Phase 1) |
| **Small Org (10–50 apps)** | 3 weeks |
| **Mid-Market (50–200 apps)** | 4 weeks |
| **Enterprise (200+ apps)** | 5–6 weeks |
| **Core Team Size** | 4–8 people |
| **Effort (Small Org)** | 600–900 hours |
| **Effort (Mid-Market)** | 1,200–1,800 hours |
| **Effort (Enterprise)** | 2,400–3,600 hours |

### Stakeholder Engagement Guidance

**Technical Stakeholders:**
- Frequency: Weekly technical working group meetings
- Focus: Assessment findings, technical details, remediation planning
- Engagement: Detailed technical assessments, expert interviews

**Application Owners:**
- Frequency: Individual interviews and follow-ups; budget 2–3 hours per week per application
- Focus: Application characteristics, business requirements, constraints
- Engagement: Detailed application assessments, validation

**Operations Teams:**
- Frequency: Weekly operational working group meetings
- Focus: Operational procedures, support models, performance data
- Engagement: Operational assessments, support model evaluation

**Security and Compliance Teams:**
- Frequency: Weekly security/compliance working group meetings
- Focus: Security controls, compliance requirements, risk assessment
- Engagement: Security and compliance assessments, control evaluation

---

## Phase 3: Evaluation

### Phase Objectives

The Evaluation phase synthesizes analysis findings into readiness scores, evaluates multi-cloud options, develops business cases, and produces strategic recommendations.

**Primary Objectives:**
- Calculate cloud readiness scores across five dimensions
- Evaluate applications against AWS, Azure, and Google Cloud
- Develop comprehensive business cases with TCO and ROI analysis
- Assess risks and compliance implications
- Develop migration wave plans
- Produce strategic recommendations and prioritization

> **Mandatory phase gate.** Phase 3 cannot start until at least two weeks of clean utilisation data has been captured in Phase 1. Right-sizing recommendations issued without this minimum are flagged as low-confidence and require remediation in a follow-up cycle.

### Phase Activities

#### 3.1 Cloud Readiness Scoring
- Calculate Technical readiness scores (architecture, dependencies, tech stack, platform support)
- Calculate Operational readiness scores (automation, monitoring, incident response, complexity)
- Calculate Security readiness scores (identity, encryption, vulnerability management, controls)
- Calculate Compliance readiness scores (regulatory requirements, audit trails, data residency, certifications)
- Calculate Business readiness scores (stakeholder alignment, budget, business case, strategic fit)
- Calculate **Data & AI Readiness scores** (see dimension 6 below)
- Calculate overall Cloud_Readiness_Score as weighted average across all six dimensions
- Document scoring rationale and supporting evidence
- **Duration:** 1 week
- **Resources:** Solution architects, assessment leads, scoring specialists

##### Dimension 6: Data & AI Readiness (added v2.1)

All three major hyperscalers differentiate significantly on AI and data platform capability. This dimension ensures the assessment captures signals that inform both the hyperscaler scoring and the Part 2 opportunity scope.

| Sub-dimension | What to Assess | Azure Signal | AWS Signal | GCP Signal |
|---|---|---|---|---|
| Data platform maturity | Data warehouse, data lake, real-time streaming infrastructure | Azure Synapse / Fabric readiness | Redshift / Kinesis readiness | BigQuery / Dataflow readiness |
| ML/AI workload identification | Existing ML models, inference workloads, AI-adjacent services (recommendation engines, content scoring, fraud detection) | Azure Machine Learning, Azure OpenAI Service | Amazon SageMaker, Amazon Bedrock | Vertex AI, Vertex AI Search |
| Data gravity | Where does training data, inference data, and analytical data reside? Which hyperscaler region is closest? | Proximity to Azure data services | Proximity to AWS data lake | GCP data affinity |
| GenAI readiness | LLM API consumption candidates, RAG architecture signals (large Redis/vector cache footprints), vector database requirements, existing data pipeline infrastructure (Kafka, Spark, Databricks) as signal for data platform migration path | **Azure AI Foundry** (unified hub including Azure OpenAI Service, phi models, fine-tuning); Azure AI Search | Amazon Bedrock, Amazon Kendra; **AWS Trainium/Inferentia** for existing ML training pipelines | **Vertex AI Gemini** (Gemini 1.5 Pro/Flash via Vertex API); AlloyDB AI |
| Microsoft 365 Copilot readiness (Azure-specific) | Teams/Exchange Online adoption, SharePoint Online migration status, Microsoft 365 E3/E5 licensing | M365 Copilot requires Teams + SharePoint + OneDrive on cloud — assess migration status | N/A | N/A |

> **Discovery signal:** A large Redis estate (e.g., 200+ VMs across many application stacks) is a strong indicator of microservices architecture and a potential RAG / vector caching use case. Flag these estates for AI readiness follow-up in Phase 2 application interviews.

#### 3.2 Multi-Cloud Evaluation and Right-Sizing
- Evaluate AWS, Azure, and Google Cloud service compatibility for each application
- Produce right-sizing recommendations per server (target SKU + confidence level)
- Apply Reserved Instance / Savings Plan strategy and Azure Hybrid Benefit modeling
- Assess hyperscaler-specific factors (service availability, pricing, regional presence)
- Assess organizational factors (existing investments, team expertise, vendor relationships)
- Develop hyperscaler recommendations for each application
- Document service mapping and migration paths
- **Duration:** 1–2 weeks
- **Resources:** Cloud architects, AWS/Azure/GCP specialists, FinOps analyst

#### 3.3 Business Case Development
- Capture current-state costs (infrastructure, licensing, personnel, operations)
- Estimate cloud-state costs (compute, storage, networking, managed services)
- Calculate Total Cost of Ownership (TCO) for 3–5 year period
- Calculate Return on Investment (ROI) including cost savings and benefits
- Estimate migration costs (assessment, planning, execution, validation)
- Calculate payback period, net present value (NPV), and internal rate of return (IRR) — enterprise finance committees require all three; payback period for operational readers, NPV for absolute value, IRR for comparison against alternative capital investments
- Conduct sensitivity analysis for different scenarios
- Document financial assumptions and risk factors
- **Duration:** 1–2 weeks
- **Resources:** Financial analysts, FinOps analyst, business analysts

#### 3.4 Risk and Compliance Evaluation
- Identify security, operational, and compliance risks
- Assess risk likelihood and impact using risk matrix
- Develop risk mitigation strategies and controls
- Evaluate hyperscaler compliance certifications
- Assess data residency and sovereignty requirements
- Document risk register and mitigation plans
- **Duration:** 1 week
- **Resources:** Risk managers, security architects, compliance specialists

#### 3.5 Strategic Recommendations and Prioritization
- Prioritize applications for migration based on readiness, business value, and risk
- Develop migration strategy (lift-and-shift, replatform, refactor, retire, retain)
- Identify quick wins and early value opportunities
- Develop executive recommendations and business case summary
- Create presentation materials for stakeholder decision-making
- **Duration:** 1 week
- **Resources:** Solution architects, assessment leads, business analysts

> **Vendor Neutrality Commitment.** Rackspace holds co-sell and funding relationships with all three major hyperscalers (Microsoft AMM, AWS MAP, Google Cloud PSO). To preserve the integrity of the CRA recommendation, the hyperscaler scoring in Phase 3 must follow the "evidence before recommendation" principle: the weighted decision matrix score is calculated and reviewed by the delivery team *before* commercial or alliance considerations are applied. The final recommendation is the highest-scoring hyperscaler on evidence. Where scores are within 5 points of each other, a tie-break workshop with the customer is mandatory. Alliance funding eligibility is presented as a *consequence* of the recommendation, never as a driver of it. This principle is enforced by the Phase 3 QA peer review gate.

### Phase Entry Criteria

- Phase 2 (Analysis) completed with all assessment data collected
- Minimum two weeks of clean utilization data captured in Phase 1
- Readiness scoring model and criteria defined
- Multi-cloud evaluation framework prepared
- Business case templates and financial models prepared
- Risk assessment framework prepared
- Stakeholder engagement plan active

### Phase Exit Criteria

- Cloud readiness scores calculated for all applications
- Multi-cloud evaluation completed for all applications
- Right-sizing recommendations produced per server with confidence level
- Business case developed with TCO, ROI, and payback period
- Risk assessment completed with mitigation strategies
- Strategic recommendations developed
- Executive summary and presentation materials prepared
- Stakeholder review and feedback incorporated

### Phase Success Criteria

- **Completeness:** Readiness scores, multi-cloud evaluation, right-sizing, and business cases completed for ≥ 95% of applications
- **Accuracy:** Scoring rationale validated with technical and business stakeholders
- **Confidence:** Right-sizing recommendations carry high or medium confidence (low-confidence items explicitly flagged with remediation plan)
- **Business Alignment:** Business case assumptions validated with finance and business stakeholders
- **Risk Assessment:** Risk register reviewed and approved by risk and compliance teams
- **Timeline:** Phase completed within planned timeline (typically 3 weeks for mid-market)

### Phase Deliverables

- Cloud Readiness Scorecard (scores by dimension and application)
- Readiness Assessment Report (scoring methodology, findings, recommendations)
- Multi-Cloud Evaluation Report (AWS, Azure, GCP comparison and recommendations)
- Right-Sizing Recommendations (per-server target SKU with confidence level)
- Business Case Summary (TCO, ROI, financial projections, sensitivity analysis)
- Risk Assessment Report (identified risks, likelihood/impact, mitigation strategies)
- Executive Summary (key findings, recommendations, business case summary)
- Hyperscaler Recommendation Report (platform comparison and recommendations)
- Compliance and Security Assessment Report (requirements, controls, gaps)
- Strategic Recommendations Presentation (for executive decision-making)

### Estimated Timeline and Resources

| Aspect | Details |
|--------|---------|
| **Phase Duration (mid-market default)** | **3 weeks** |
| **Small Org (10–50 apps)** | 2 weeks |
| **Mid-Market (50–200 apps)** | 3 weeks |
| **Enterprise (200+ apps)** | 4 weeks |
| **Core Team Size** | 5–10 people |
| **Effort (Small Org)** | 600–900 hours |
| **Effort (Mid-Market)** | 1,200–1,800 hours |
| **Effort (Enterprise)** | 2,000–3,000 hours |

### Stakeholder Engagement Guidance

**Executive Stakeholders:**
- Frequency: Monthly steering committee meetings
- Focus: Strategic recommendations, business case, decision-making
- Engagement: Executive summary, presentation materials, decision requests

**Business Stakeholders:**
- Frequency: Bi-weekly working group meetings
- Focus: Business case, prioritization, wave planning
- Engagement: Business case review, prioritization workshops

**Technical Stakeholders:**
- Frequency: Weekly technical working group meetings
- Focus: Readiness scores, multi-cloud evaluation, technical recommendations
- Engagement: Scoring review, technical validation, remediation planning

**Finance Stakeholders:**
- Frequency: Bi-weekly finance working group meetings
- Focus: Business case, financial assumptions, ROI analysis
- Engagement: Business case development, financial validation

**Risk and Compliance Stakeholders:**
- Frequency: Weekly risk/compliance working group meetings
- Focus: Risk assessment, compliance requirements, mitigation strategies
- Engagement: Risk assessment review, compliance validation

---

## Phase 4: Planning

### Phase Objectives

The Planning phase develops detailed migration wave plans, finalizes the readiness report, and secures stakeholder sign-off to prepare for cloud migration execution.

**Primary Objectives:**
- Develop migration wave plan and roadmap with timelines and milestones
- Plan resource requirements and staffing model
- Develop risk mitigation and contingency plans
- Finalize the readiness report and executive deliverable package
- Secure formal stakeholder sign-off
- Prepare for migration execution phase

### Phase Activities

#### 4.1 Migration Wave Planning
- Group applications by dependencies and readiness scores
- Sequence waves to minimize operational risk
- Identify applications requiring synchronized migration
- Define migration approach per wave (lift-and-shift, replatform, refactor, retire, retain)
- Develop wave-level effort estimates
- Plan cutover and rollback procedures
- **Duration:** 2 weeks
- **Resources:** Migration program managers, solution architects, technical leads

#### 4.2 Detailed Roadmap and Resource Planning
- Develop detailed migration roadmap with phases, waves, timelines, and milestones
- Identify resource requirements by role and skill
- Develop staffing plan and recruitment strategy
- Plan training and knowledge transfer activities
- Identify internal vs. external resource needs
- Plan vendor and partner engagement
- **Duration:** 1 week (runs in parallel with 4.1)
- **Resources:** Program managers, HR specialists, resource managers

#### 4.3 Risk Mitigation and Governance Framework
- Develop detailed mitigation strategies for identified risks
- Plan contingency procedures for high-risk scenarios
- Establish execution governance structure (steering committee, working groups)
- Define decision-making authorities and escalation procedures
- Develop status reporting and metrics framework
- Establish change management procedures
- **Duration:** 1 week
- **Resources:** Risk managers, program managers, governance specialists

##### Scope Variance Change Request Protocol

Scope variance — where the discovered estate differs materially from the SoW estimate — is the most common cause of commercial disputes in CRA engagements. The DMG Media UK engagement surfaced a 57% variance (+1,912 VMs above the SoW estimate). The following protocol is mandatory when variance is discovered:

| Trigger | Action | Owner | Timeline |
|---|---|---|---|
| Discovered count exceeds SoW estimate by **>15%** | Raise scope variance flag to Delivery Director and Account Manager immediately; do not continue Phase 1 without acknowledgement | Lead Architect | Within 24 hours of discovery |
| Variance confirmed and stakeholder-validated | Convene scope refinement workshop with customer IT Director and Rackspace PM to agree the actual migration candidate list | PM + Lead Architect | Within 5 business days of flag |
| Migration candidate list agreed | Issue formal **Change Request (CR)** document to customer covering: revised scope, revised timeline, revised commercial terms | PM + Account Manager | Within 3 business days of workshop |
| Customer signs CR | Update SoW; update Phase 2–4 resource plan; update billing forecast | PM | Before Phase 2 begins |
| Customer disputes CR | Escalate to Delivery Director and Customer Executive Sponsor; do not absorb scope without commercial rebaseline | Delivery Director | Within 5 business days |

> **SoW protection clause (required):** Every CRA SoW must include the following or equivalent: *"This engagement assumes approximately [N] in-scope applications and [M] physical/virtual servers based on information provided by [Client] on [date]. If the actual discovered count differs by more than 15% from the agreed scope, Rackspace reserves the right to issue a Change Request adjusting scope, timeline, and commercial terms."* See `Templates/04-planning/sow-template.docx` Section 5 (Scope Variance Clause).

#### 4.4 Readiness Report Authoring and QA
- Author executive summary and business case
- Author technical findings and recommendations document
- Author migration roadmap (PPTX / XLSX)
- Conduct internal peer review and QA cycle
- Produce customer-ready deliverable package
- **Duration:** 2 weeks
- **Resources:** PM, lead architect, technical writers

#### 4.5 Stakeholder Review and Sign-Off
- Conduct technical workshop walkthrough with customer technical stakeholders
- Incorporate revisions based on technical feedback
- Deliver executive readout and Q&A
- Obtain formal sign-off and engagement closeout
- Communicate strategy to broader organization
- **Duration:** 2 weeks (split across two cycles: technical, then executive)
- **Resources:** Program managers, communication specialists, executive sponsors

### Phase Entry Criteria

- Phase 3 (Evaluation) completed with strategic recommendations
- Right-sizing recommendations finalized at acceptable confidence levels
- Executive stakeholders aware of preliminary recommendations
- Migration strategy and approach defined
- Resource budget approved
- Governance structure defined

### Phase Exit Criteria

- Migration wave plan approved
- Detailed migration roadmap developed with timelines and milestones
- Resource plan developed with staffing requirements
- Risk mitigation and contingency plans documented
- Execution governance framework established
- Customer-ready deliverable package produced and QA'd
- Executive stakeholders have signed off on strategy and roadmap
- Engagement formally closed

### Phase Success Criteria

- **Completeness:** Wave plan, detailed roadmap, resource plan, and risk mitigation completed
- **Stakeholder Alignment:** Executive stakeholders have signed off on strategy and roadmap
- **Quality:** Deliverable package has passed internal QA peer review
- **Timeline:** Phase completed within planned timeline (typically 6 weeks for mid-market)
- **Communication:** Strategy and roadmap communicated to broader organization
- **Execution Readiness:** Detailed activity plans and procedures prepared for first wave

### Phase Deliverables

- Migration Wave Plan (waves grouped by dependency, with effort estimates)
- Detailed Migration Roadmap (phases, waves, timelines, milestones, dependencies)
- Resource Plan (staffing requirements, recruitment strategy, training plan)
- Risk Mitigation Plan (mitigation strategies, contingency procedures, rollback plans)
- Execution Governance Charter (governance structure, decision authorities, escalation procedures)
- Communication and Engagement Plan (stakeholder communication strategy and cadence)
- Executive Summary and Business Case (sponsor-ready)
- Technical Findings and Recommendations Document
- Executive Roadmap Presentation (strategy, roadmap, business case, next steps)
- Stakeholder Sign-Off Documentation (executive approvals, stakeholder alignment)
- Final Deliverable Package (formal acceptance signed)

### Estimated Timeline and Resources

| Aspect | Details |
|--------|---------|
| **Phase Duration (mid-market default)** | **6 weeks** (2 wks wave planning + 2 wks report authoring & QA + 2 wks review & sign-off) |
| **Small Org (10–50 apps)** | 4 weeks |
| **Mid-Market (50–200 apps)** | 6 weeks |
| **Enterprise (200+ apps)** | 7–8 weeks |
| **Core Team Size** | 4–8 people |
| **Effort (Small Org)** | 300–500 hours |
| **Effort (Mid-Market)** | 600–1,000 hours |
| **Effort (Enterprise)** | 1,200–1,800 hours |

> **Audit note.** The previous version of this methodology cited 2–4 weeks for Planning. That estimate covered roadmap development only and excluded the report authoring, QA, and stakeholder sign-off cycles that customers expect from a Cloud Readiness Assessment. The revised range builds those activities in explicitly so the deliverable package is exec-grade rather than rushed.

### Stakeholder Engagement Guidance

**Executive Stakeholders:**
- Frequency: Monthly steering committee meetings, plus dedicated executive readout
- Focus: Roadmap approval, resource allocation, strategic alignment, formal sign-off
- Engagement: Roadmap presentation, sign-off, ongoing governance

**Business Stakeholders:**
- Frequency: Bi-weekly working group meetings
- Focus: Wave planning, business impact, communication strategy
- Engagement: Roadmap review, prioritization confirmation, communication planning

**Technical Stakeholders:**
- Frequency: Weekly technical working group meetings, plus dedicated technical workshop
- Focus: Technical roadmap, resource requirements, execution procedures
- Engagement: Detailed roadmap review, procedure development, training

**Operations Stakeholders:**
- Frequency: Weekly operational working group meetings
- Focus: Operational procedures, support model, monitoring and support
- Engagement: Operational procedure development, support planning

**Finance Stakeholders:**
- Frequency: Bi-weekly finance working group meetings
- Focus: Resource costs, budget tracking, financial reporting
- Engagement: Resource plan review, budget confirmation

---

## Cross-Phase Considerations

### Project Initiation (Pre-Phase 1) — 2 Weeks

Every CRA engagement begins with a 2-week Project Initiation phase before Phase 1 tooling setup starts. This phase is not optional — skipping it pushes its activities into Phase 1, compressing the tooling window and causing the most common Phase 1 delays.

| Activity | Owner | Output |
|---|---|---|
| Engagement charter and RACI sign-off | PM + Delivery Director | Signed charter with named owners for each CRA phase |
| Tooling licensing procurement | Lead Architect | Azure Migrate / ADS / GCP Migration Center licences confirmed; service accounts requested |
| CAB ticket submission (firewall rules) | Discovery Architect | Change requests submitted; 5–10 business day lead time starts here, not in Phase 1 |
| NDA and data-sharing agreement execution | Account Manager | Signed NDA; customer IT contacts confirmed |
| Alliance partner deal registration | Alliance Manager | ACE / Partner Center / Google Partner Advantage registration completed before SoW countersign |
| Kick-off meeting and stakeholder map | PM | Steering committee identified; working group leads named |

> Submitting CAB tickets and firewall change requests during Project Initiation (rather than Phase 1 Day 1) eliminates the most common single cause of Phase 1 slippage.

### Assessment Timeline Summary

The table below reflects the audited (v2) durations. Numbers in the **Sequential** column assume each phase finishes before the next begins. The **Parallelized** column reflects the recommended delivery model in which Phase 2 begins approximately one week before Phase 1 ends.

| Phase | Duration (Mid-Market) | Cumulative (Sequential) | Cumulative (Parallelized) |
|-------|-----------------------|-------------------------|---------------------------|
| **Project Initiation** | **2 weeks** | 2 weeks | 2 weeks |
| Phase 1: Discovery | 7 weeks | 9 weeks | 9 weeks |
| Phase 2: Analysis | 4 weeks | 13 weeks | 11 weeks |
| Phase 3: Evaluation | 3 weeks | 16 weeks | 13 weeks |
| Phase 4: Planning | 6 weeks | 22 weeks | 18 weeks |
| **Total End-to-End (Mid-Market)** | — | **22 weeks** | **18 weeks (~4½ months)** |

> **Note.** The 18-week parallelized total runs from contract signature to final customer sign-off. For planning purposes, use 18 weeks as the standard mid-market engagement duration.

### Phase Duration by Organization Size

| Phase | Small Org | Mid-Market | Enterprise |
|-------|-----------|------------|-----------|
| Phase 1: Discovery | 5–6 wks | 7 wks | 9–10 wks |
| Phase 2: Analysis | 3 wks | 4 wks | 5–6 wks |
| Phase 3: Evaluation | 2 wks | 3 wks | 4 wks |
| Phase 4: Planning | 4 wks | 6 wks | 7–8 wks |
| **Sequential Total** | **14–15 wks** | **20 wks** | **25–28 wks** |
| **Parallelized Total** | **12 wks** | **16 wks** | **20–22 wks** |

### Resource Requirements Summary

| Organization Size | Total Effort | Core Team | Duration (Parallelized) |
|-------------------|-------------|-----------|--------------------------|
| **Small (10–50 apps)** | 1,900–2,900 hours | 3–5 people | 12 weeks |
| **Mid-Market (50–200 apps)** | 3,800–5,800 hours | 5–8 people | 16 weeks |
| **Enterprise (200+ apps)** | 7,200–11,400 hours | 8–12 people | 20–22 weeks |

### What Drives the Critical Path

The critical path through the assessment is rarely a single phase. Three constraints dominate elapsed duration in real engagements:

1. **CAB / firewall change lead times.** A 5–10 business-day lead time for network change requests is normal; aggressive plans that ignore this slip Phase 1 by 1–2 weeks.
2. **Utilization data window.** Two weeks is the floor for confident right-sizing; four weeks is the target to capture month-end and weekly seasonality. Compressing this is the leading cause of low-confidence recommendations.
3. **Application owner availability.** Phase 2 interviews assume 2–3 hours per week per application owner. When availability drops below 80% of plan, Phase 2 slips and Phase 3 readiness scoring becomes guesswork.

### Quality Assurance Throughout Assessment

- **Data Quality Validation:** Ongoing validation of data completeness and accuracy
- **Peer Review:** Independent review of findings and recommendations at each phase
- **Stakeholder Validation:** Regular validation of findings with business and technical stakeholders
- **Discrepancy Resolution:** Systematic identification and resolution of data conflicts
- **Confidence Flagging:** Right-sizing and TCO outputs explicitly carry confidence levels (high / medium / low)
- **Assessment Accuracy:** Comparison of assessment predictions with actual outcomes

### Governance and Decision-Making

- **Steering Committee:** Monthly meetings for executive oversight and decision-making
- **Working Groups:** Weekly meetings for technical, operational, business, and compliance teams
- **Escalation Procedures:** Clear procedures for resolving conflicts and data discrepancies
- **Change Management:** Formal procedures for scope changes and assessment modifications
- **Status Reporting:** Regular status reports on assessment progress, issues, and risks

### Stakeholder Communication

- **Executive Stakeholders:** Monthly updates on progress, findings, and recommendations
- **Business Stakeholders:** Bi-weekly updates on business impact and prioritization
- **Technical Stakeholders:** Weekly updates on technical findings and recommendations
- **Broader Organization:** Regular communication on assessment progress and outcomes

### Risk Management

- **Assessment Risks:** Risks related to data quality, stakeholder engagement, timeline delays
- **Technical Risks:** Risks related to application complexity, dependency constraints, technical feasibility
- **Business Risks:** Risks related to business case assumptions, financial projections, ROI realization
- **Organizational Risks:** Risks related to resource availability, organizational change, stakeholder alignment

---

## Conclusion

The Cloud Readiness Accelerator assessment methodology provides a comprehensive, structured approach to evaluating cloud migration readiness. By following the four-phase model—Discovery, Analysis, Evaluation, and Planning—organizations can systematically assess their applications and infrastructure, develop informed migration strategies, and prepare for successful cloud migration execution.

The methodology is designed to be flexible and scalable, adapting to different organization sizes, technology landscapes, and industry contexts. Clear entry/exit criteria, defined activities, and measurable success criteria ensure consistent, high-quality assessments across different engagements.

This methodology overview serves as the foundation for all assessment activities and should be used in conjunction with phase-specific guidance documents, activity-specific instructions, and detailed templates for each assessment artifact.

---

## Revision History

| Version | Date | Change | Rationale |
|---------|------|--------|-----------|
| v1.0 | Initial | Original four-phase model with 12–23 week range | Baseline methodology |
| **v2.0** | **2026-04-25** | **Phase durations audited and revised; explicit utilization-data minimum (2 wks) and target (4 wks); discovery tooling stand-up and OS-troubleshooting buffer called out; sequential vs. parallelized totals separated** | **Sr Director audit — original durations compressed tooling stand-up and data window into the same period, leading to low-confidence right-sizing in real engagements.** |
