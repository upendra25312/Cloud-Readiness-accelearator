# Cloud Readiness Accelerator - Analysis Phase Guide

**Who should read this:** Cloud Architects and Solutions Engineers running Phase 2 of a CRA engagement. Also relevant for Security Analysts and Compliance leads who will contribute to the readiness scoring workshops.

**What this guide covers:** How to transform Phase 1 discovery data into application-level cloud readiness scores across five dimensions: Technical, Operational, Security, Compliance, and Business. The output of this phase is the evidence base for the hyperscaler recommendation in Phase 3.

**What comes before and after:** Phase 2 starts approximately 1 week before Phase 1 ends (as soon as the validated infrastructure inventory is available — utilisation data does not need to be complete). Phase 3 (Evaluation) follows; it requires the readiness scores from this phase plus ≥2 weeks of clean utilisation data from Phase 1.

**Time to read this guide:** 15–20 minutes

---

## Phase Overview

The Analysis Phase transforms the discovery data into actionable insights through systematic evaluation of applications across multiple dimensions. This phase focuses on assessing technical, operational, security, compliance, and business readiness for each application. The primary objectives are to evaluate applications against readiness criteria, identify remediation needs, and prepare comprehensive analysis for the Evaluation Phase.

### Phase Objectives

1. Evaluate applications across five readiness dimensions: Technical, Operational, Security, Compliance, and Business
2. Assess technical architecture, dependencies, and technology stack compatibility
3. Evaluate operational maturity, automation, and monitoring capabilities
4. Assess security posture and identity management
5. Evaluate compliance requirements and regulatory alignment
6. Assess business alignment and stakeholder readiness
7. Identify remediation needs and improvement opportunities
8. Prepare analysis for Evaluation Phase

### Phase Duration and Resources

- **Mid-Market Default (50–200 apps)**: **4 weeks** (parallelized with the back half of Phase 1)
- **Small Organizations (10–50 apps)**: 3 weeks
- **Enterprise Organizations (200+ apps)**: 5–6 weeks

> **Timing note:** Phase 2 begins approximately one week before Phase 1 ends. Application-owner interviews, criticality classification, and compliance review only require a validated inventory — not a completed utilisation dataset. Starting Phase 2 early compresses overall elapsed time by 25–30% without compromising data quality. Phase 3 cannot start until at least 2 weeks of clean utilisation data has been collected regardless of parallelisation choices.

### Resource Requirements

- **Assessment Lead**: 1 FTE
- **Technical Analysts**: 2-3 FTE
- **Security Analyst**: 1 FTE
- **Compliance Analyst**: 0.5 FTE
- **Business Analyst**: 1 FTE

---

## Phase Entry and Exit Criteria

### Entry Criteria

Before starting the Analysis Phase, ensure:

1. **Discovery Complete**: Discovery Phase completed with validated application and infrastructure inventory
2. **Data Quality**: Data quality validation completed with 90%+ accuracy
3. **Stakeholder Validation**: Stakeholders confirmed accuracy of discovered data
4. **Assessment Team Ready**: Analysis team trained on assessment methodology and tools
5. **Analysis Tools Prepared**: Readiness scoring tools and templates prepared

### Exit Criteria

The Analysis Phase is complete when:

1. **Technical Assessment**: All applications evaluated for technical readiness
2. **Operational Assessment**: All applications evaluated for operational readiness
3. **Security Assessment**: All applications evaluated for security readiness
4. **Compliance Assessment**: All applications evaluated for compliance readiness
5. **Business Assessment**: All applications evaluated for business readiness
6. **Readiness Scores**: Overall Cloud_Readiness_Score calculated for all applications
7. **Analysis Validation**: Analysis results validated with stakeholders
8. **Readiness Confirmed**: Assessment team confirms readiness to proceed to Evaluation Phase

---

## Step-by-Step Activity Instructions

### Activity 1: Technical Assessment

**Objective**: Evaluate applications for technical readiness including architecture, dependencies, and technology stack

**Duration**: 4-6 days

**Steps**:

1. **Assess Architecture Modernization**
   - Evaluate current architecture pattern (monolithic, microservices, serverless)
   - Assess architecture alignment with cloud-native patterns
   - Identify architectural constraints or limitations
   - Document architecture modernization recommendations
   - Score architecture dimension (0-100)

2. **Assess Dependency Complexity**
   - Analyze application dependency chains
   - Evaluate tight coupling and interdependencies
   - Assess impact of dependencies on cloud migration
   - Identify applications with high dependency complexity
   - Score dependency complexity dimension (0-100)

3. **Assess Technology Stack Compatibility**
   - Evaluate compatibility of programming languages with cloud platforms
   - Assess compatibility of frameworks and libraries
   - Evaluate database compatibility with cloud services
   - Assess middleware and integration technology compatibility
   - Score technology stack compatibility dimension (0-100)

4. **Assess Platform Support and Licensing**
   - Evaluate vendor support status for current platform
   - Assess licensing model compatibility with cloud
   - Identify licensing constraints or restrictions
   - Evaluate open-source vs. commercial technology considerations
   - Score platform support dimension (0-100)

5. **Assess Performance and Scalability**
   - Evaluate current performance characteristics
   - Assess scalability requirements and constraints
   - Evaluate cloud platform capability to meet performance needs
   - Identify performance optimization opportunities
   - Score performance dimension (0-100)

6. **Calculate Technical Readiness Score**
   - Aggregate dimension scores into overall Technical_Readiness_Score
   - Document scoring rationale and evidence
   - Identify remediation recommendations
   - Prepare technical assessment summary

**Deliverables**:
- Technical Assessment Report (by application)
- Technical Readiness Scores (by dimension and application)
- Architecture Modernization Recommendations
- Technology Stack Compatibility Analysis
- Technical Assessment Summary

**Best Practices**:
- Use objective criteria for scoring to ensure consistency
- Document scoring rationale for audit trail
- Involve technical experts in assessment
- Validate assessments with application architects
- Identify quick wins for technical improvements

**Common Pitfalls**:
- Subjective scoring without clear criteria
- Insufficient technical expertise in assessment team
- Failure to validate assessments with application teams
- Underestimating complexity of legacy systems
- Not considering cloud-native architecture patterns

---

### Activity 2: Operational Assessment

**Objective**: Evaluate applications for operational readiness including automation, monitoring, and incident response

**Duration**: 3-5 days

**Steps**:

1. **Assess Automation Maturity**
   - Evaluate deployment automation capabilities
   - Assess infrastructure automation maturity
   - Evaluate configuration management practices
   - Assess testing automation and CI/CD maturity
   - Score automation dimension (0-100)

2. **Assess Monitoring and Observability**
   - Evaluate monitoring tool coverage and capabilities
   - Assess log aggregation and analysis capabilities
   - Evaluate alerting and notification procedures
   - Assess performance monitoring and trending
   - Score monitoring dimension (0-100)

3. **Assess Incident Response Procedures**
   - Evaluate incident response procedures and documentation
   - Assess incident response team structure and training
   - Evaluate incident communication and escalation procedures
   - Assess incident tracking and post-mortem procedures
   - Score incident response dimension (0-100)

4. **Assess Operational Complexity**
   - Evaluate operational complexity and manual procedures
   - Assess operational staffing requirements
   - Evaluate operational documentation quality
   - Assess operational runbook completeness
   - Score operational complexity dimension (0-100)

5. **Assess Change Management**
   - Evaluate change management procedures
   - Assess change approval and communication procedures
   - Evaluate change testing and validation procedures
   - Assess rollback procedures and disaster recovery
   - Score change management dimension (0-100)

6. **Calculate Operational Readiness Score**
   - Aggregate dimension scores into overall Operational_Readiness_Score
   - Document scoring rationale and evidence
   - Identify operational improvement recommendations
   - Prepare operational assessment summary

**Deliverables**:
- Operational Assessment Report (by application)
- Operational Readiness Scores (by dimension and application)
- Automation Maturity Assessment
- Monitoring and Observability Analysis
- Operational Improvement Recommendations
- Operational Assessment Summary

**Best Practices**:
- Involve operations teams in assessment
- Use monitoring data to validate operational capabilities
- Identify automation opportunities for cloud migration
- Document operational procedures and runbooks
- Assess readiness for cloud operational model

**Common Pitfalls**:
- Insufficient involvement of operations teams
- Underestimating operational complexity
- Not considering cloud operational model differences
- Failure to identify automation opportunities
- Inadequate monitoring and observability

---

### Activity 3: Security Assessment

**Objective**: Evaluate applications for security readiness including identity management, encryption, and vulnerability management

**Duration**: 4-6 days

**Steps**:

1. **Assess Identity and Access Management**
   - Evaluate identity management capabilities
   - Assess access control procedures and enforcement
   - Evaluate multi-factor authentication implementation
   - Assess privileged access management
   - Score identity management dimension (0-100)

2. **Assess Encryption and Data Protection**
   - Evaluate encryption at rest implementation
   - Assess encryption in transit implementation
   - Evaluate key management procedures
   - Assess data protection and privacy controls
   - Score encryption dimension (0-100)

3. **Assess Vulnerability Management**
   - Evaluate vulnerability scanning and assessment procedures
   - Assess patch management procedures
   - Evaluate vulnerability remediation procedures
   - Assess security testing and code review procedures
   - Score vulnerability management dimension (0-100)

4. **Assess Security Controls**
   - Evaluate firewall and network security controls
   - Assess intrusion detection and prevention
   - Evaluate security information and event management (SIEM)
   - Assess endpoint protection and antivirus
   - Score security controls dimension (0-100)

5. **Assess Security Compliance**
   - Evaluate security policy compliance
   - Assess security training and awareness
   - Evaluate security incident response procedures
   - Assess security audit and assessment procedures
   - Score security compliance dimension (0-100)

6. **Calculate Security Readiness Score**
   - Aggregate dimension scores into overall Security_Readiness_Score
   - Document scoring rationale and evidence
   - Identify security improvement recommendations
   - Prepare security assessment summary

**Deliverables**:
- Security Assessment Report (by application)
- Security Readiness Scores (by dimension and application)
- Identity and Access Management Analysis
- Encryption and Data Protection Assessment
- Vulnerability Management Assessment
- Security Improvement Recommendations
- Security Assessment Summary

**Best Practices**:
- Involve security teams in assessment
- Use security scanning tools to validate security posture
- Assess cloud security model alignment
- Identify security improvement opportunities
- Document security assumptions and dependencies

**Common Pitfalls**:
- Insufficient security expertise in assessment team
- Failure to involve security teams
- Underestimating security complexity
- Not considering cloud security model differences
- Inadequate vulnerability management

---

### Activity 4: Compliance Assessment

**Objective**: Evaluate applications for compliance readiness including regulatory requirements and audit controls

**Duration**: 3-5 days

**Steps**:

1. **Identify Compliance Requirements**
   - Identify applicable compliance frameworks (HIPAA, PCI-DSS, GDPR, SOC2, etc.)
   - Document specific compliance requirements for each application
   - Assess compliance requirement complexity
   - Identify compliance gaps and remediation needs
   - Score compliance requirements dimension (0-100)

2. **Assess Audit and Logging**
   - Evaluate audit logging capabilities
   - Assess audit log retention and archival procedures
   - Evaluate audit trail completeness and accuracy
   - Assess audit log security and integrity
   - Score audit and logging dimension (0-100)

3. **Assess Data Residency and Sovereignty**
   - Evaluate data residency requirements
   - Assess data sovereignty constraints
   - Evaluate geographic data storage requirements
   - Assess data transfer and cross-border restrictions
   - Score data residency dimension (0-100)

4. **Assess Compliance Certifications**
   - Evaluate current compliance certifications
   - Assess certification maintenance requirements
   - Evaluate cloud provider compliance certifications
   - Assess certification alignment with requirements
   - Score compliance certifications dimension (0-100)

5. **Assess Compliance Controls**
   - Evaluate compliance control implementation
   - Assess control effectiveness and testing
   - Evaluate control documentation and evidence
   - Assess control remediation procedures
   - Score compliance controls dimension (0-100)

6. **Calculate Compliance Readiness Score**
   - Aggregate dimension scores into overall Compliance_Readiness_Score
   - Document scoring rationale and evidence
   - Identify compliance improvement recommendations
   - Prepare compliance assessment summary

**Deliverables**:
- Compliance Assessment Report (by application)
- Compliance Readiness Scores (by dimension and application)
- Compliance Requirements Analysis
- Data Residency and Sovereignty Assessment
- Compliance Controls Assessment
- Compliance Improvement Recommendations
- Compliance Assessment Summary

**Best Practices**:
- Involve compliance and legal teams in assessment
- Document compliance requirements clearly
- Assess cloud provider compliance certifications
- Identify compliance gaps and remediation needs
- Plan for compliance validation in cloud environment

**Common Pitfalls**:
- Insufficient compliance expertise in assessment team
- Failure to involve compliance teams
- Underestimating compliance complexity
- Not considering cloud compliance model differences
- Inadequate data residency and sovereignty assessment

---

### Activity 5: Business Assessment

**Objective**: Evaluate applications for business readiness including stakeholder alignment and business case justification

**Duration**: 2-4 days

**Steps**:

1. **Assess Stakeholder Alignment**
   - Evaluate business stakeholder support for cloud migration
   - Assess business unit readiness for cloud transition
   - Evaluate business process alignment with cloud model
   - Assess organizational change readiness
   - Score stakeholder alignment dimension (0-100)

2. **Assess Budget and Financial Readiness**
   - Evaluate budget availability for cloud migration
   - Assess financial justification for cloud migration
   - Evaluate cost-benefit analysis and business case
   - Assess financial risk tolerance
   - Score financial readiness dimension (0-100)

3. **Assess Business Case Justification**
   - Evaluate business case for cloud migration
   - Assess cost savings and ROI potential
   - Evaluate strategic fit with business objectives
   - Assess business value and benefits realization
   - Score business case dimension (0-100)

4. **Assess Strategic Fit**
   - Evaluate alignment with organizational strategy
   - Assess alignment with digital transformation initiatives
   - Evaluate competitive advantage potential
   - Assess innovation enablement potential
   - Score strategic fit dimension (0-100)

5. **Assess Risk Tolerance**
   - Evaluate organizational risk tolerance for cloud migration
   - Assess risk appetite for new technologies
   - Evaluate risk management capabilities
   - Assess contingency planning and mitigation
   - Score risk tolerance dimension (0-100)

6. **Calculate Business Readiness Score**
   - Aggregate dimension scores into overall Business_Readiness_Score
   - Document scoring rationale and evidence
   - Identify business improvement recommendations
   - Prepare business assessment summary

**Deliverables**:
- Business Assessment Report (by application)
- Business Readiness Scores (by dimension and application)
- Stakeholder Alignment Analysis
- Financial Readiness Assessment
- Business Case Justification Analysis
- Strategic Fit Assessment
- Business Assessment Summary

**Best Practices**:
- Involve business stakeholders in assessment
- Assess business case and ROI potential
- Evaluate strategic alignment
- Identify business value and benefits
- Plan for business change management

**Common Pitfalls**:
- Insufficient business stakeholder involvement
- Failure to assess business case and ROI
- Underestimating organizational change requirements
- Not considering business process changes
- Inadequate stakeholder alignment assessment

---

### Activity 6: Overall Readiness Scoring and Analysis

**Objective**: Calculate overall Cloud_Readiness_Score and prepare comprehensive analysis

**Duration**: 2-3 days

**Steps**:

1. **Calculate Overall Readiness Scores**
   - Calculate weighted average of dimension scores
   - Use standard weights: Technical (25%), Operational (20%), Security (20%), Compliance (20%), Business (15%)
   - Allow customization of weights for organizational priorities
   - Validate score calculations
   - Document scoring methodology

2. **Categorize Applications by Readiness**
   - Categorize applications into readiness tiers:
     - Tier 1 (Ready): Score 76-100 (immediate migration candidates)
     - Tier 2 (Moderate): Score 51-75 (migration with remediation)
     - Tier 3 (Limited): Score 26-50 (significant remediation needed)
     - Tier 4 (Not Ready): Score 0-25 (major remediation or stay on-premises)
   - Identify applications in each tier
   - Analyze tier distribution

3. **Identify Remediation Opportunities**
   - Identify quick wins for readiness improvement
   - Identify major remediation efforts
   - Prioritize remediation by impact and effort
   - Estimate remediation timeline and cost
   - Prepare remediation roadmap

4. **Prepare Readiness Analysis Summary**
   - Summarize readiness assessment findings
   - Highlight key insights and patterns
   - Identify applications suitable for immediate migration
   - Identify applications requiring remediation
   - Prepare recommendations for next steps

5. **Validate Analysis with Stakeholders**
   - Present readiness scores to business stakeholders
   - Collect feedback and validation
   - Address questions and concerns
   - Confirm accuracy of assessments
   - Document stakeholder sign-off

6. **Prepare for Evaluation Phase**
   - Consolidate analysis results
   - Prepare data for multi-cloud evaluation
   - Prepare data for business case development
   - Prepare data for risk assessment
   - Prepare handoff to Evaluation Phase

**Deliverables**:
- Cloud Readiness Scorecard (all applications with scores)
- Readiness Analysis Summary Report
- Application Categorization by Readiness Tier
- Remediation Opportunity Analysis
- Remediation Roadmap
- Stakeholder Validation Sign-off
- Analysis Data Package for Evaluation Phase

**Best Practices**:
- Use consistent scoring methodology across all applications
- Document scoring rationale for audit trail
- Validate scores with stakeholders
- Identify remediation opportunities
- Prepare clear recommendations for next steps

**Common Pitfalls**:
- Inconsistent scoring across applications
- Failure to validate scores with stakeholders
- Not identifying remediation opportunities
- Inadequate documentation of scoring rationale
- Unclear recommendations for next steps

---

## Best Practices and Lessons Learned

### Assessment Best Practices

1. **Consistent Methodology**: Use consistent scoring criteria and methodology across all applications
2. **Expert Involvement**: Involve subject matter experts (technical, security, compliance, business) in assessments
3. **Data-Driven Assessment**: Use objective data and evidence to support assessments
4. **Stakeholder Validation**: Validate assessments with application owners and stakeholders
5. **Documentation**: Document scoring rationale and evidence for audit trail

### Scoring Best Practices

1. **Clear Criteria**: Define clear scoring criteria for each dimension and score level
2. **Calibration**: Calibrate scoring across assessment team to ensure consistency
3. **Evidence-Based**: Base scores on objective evidence and data
4. **Rationale Documentation**: Document scoring rationale for each application
5. **Peer Review**: Have peer review of scores for consistency and accuracy

### Analysis Best Practices

1. **Pattern Identification**: Identify patterns and trends in readiness scores
2. **Root Cause Analysis**: Analyze root causes of low readiness scores
3. **Remediation Planning**: Identify and prioritize remediation opportunities
4. **Stakeholder Communication**: Communicate findings clearly to stakeholders
5. **Actionable Recommendations**: Provide specific, actionable recommendations

### Common Lessons Learned

1. **Scoring Consistency**: Scoring consistency is critical; invest in calibration and peer review
2. **Stakeholder Involvement**: Stakeholder involvement improves assessment accuracy and acceptance
3. **Data Quality**: Assessment quality depends on discovery data quality
4. **Remediation Complexity**: Remediation often more complex than initially estimated
5. **Organizational Factors**: Business and organizational factors often more important than technical factors

---

## Common Challenges and Solutions

### Challenge 1: Inconsistent Scoring

**Problem**: Different assessors score applications differently

**Solutions**:
- Establish clear scoring criteria and definitions
- Conduct scoring calibration sessions
- Implement peer review of scores
- Use scoring rubrics and examples
- Document scoring rationale for consistency

### Challenge 2: Insufficient Data for Assessment

**Problem**: Discovery data insufficient for accurate assessment

**Solutions**:
- Conduct additional interviews with application teams
- Use monitoring data to supplement discovery data
- Perform technical assessments and reviews
- Engage subject matter experts
- Document data gaps and assumptions

### Challenge 3: Stakeholder Disagreement

**Problem**: Stakeholders disagree with assessment results

**Solutions**:
- Present assessment methodology and criteria clearly
- Provide evidence and rationale for scores
- Conduct stakeholder validation sessions
- Address concerns and questions
- Adjust scores if new information provided

### Challenge 4: Complexity of Assessment

**Problem**: Assessment is complex and time-consuming

**Solutions**:
- Prioritize applications for detailed assessment
- Use automated tools for data collection and analysis
- Streamline assessment procedures
- Leverage existing assessments and data
- Focus on critical applications first

### Challenge 5: Organizational Resistance

**Problem**: Stakeholders resistant to assessment or findings

**Solutions**:
- Communicate assessment objectives and benefits clearly
- Involve stakeholders in assessment process
- Address concerns and resistance proactively
- Provide training on assessment methodology
- Celebrate quick wins and improvements

---

## Templates and Tools to Use

### Analysis Phase Templates

1. **Technical Assessment Template**
   - Architecture modernization assessment
   - Dependency complexity assessment
   - Technology stack compatibility assessment
   - Platform support and licensing assessment
   - Performance and scalability assessment

2. **Operational Assessment Template**
   - Automation maturity assessment
   - Monitoring and observability assessment
   - Incident response assessment
   - Operational complexity assessment
   - Change management assessment

3. **Security Assessment Template**
   - Identity and access management assessment
   - Encryption and data protection assessment
   - Vulnerability management assessment
   - Security controls assessment
   - Security compliance assessment

4. **Compliance Assessment Template**
   - Compliance requirements assessment
   - Audit and logging assessment
   - Data residency and sovereignty assessment
   - Compliance certifications assessment
   - Compliance controls assessment

5. **Business Assessment Template**
   - Stakeholder alignment assessment
   - Budget and financial readiness assessment
   - Business case justification assessment
   - Strategic fit assessment
   - Risk tolerance assessment

6. **Readiness Scoring Template**
   - Dimension score calculation
   - Overall readiness score calculation
   - Score interpretation and categorization
   - Remediation opportunity identification

### Analysis Phase Tools

1. **Readiness Scoring Calculator**: Excel-based calculator for readiness score calculation
2. **Assessment Templates**: Word/Excel templates for each assessment dimension
3. **Scoring Rubrics**: Detailed scoring criteria and examples
4. **Data Analysis Tools**: Excel, Tableau, Power BI for analysis and visualization
5. **Collaboration Tools**: Confluence, SharePoint for documentation and collaboration

---

## Success Criteria and Validation Procedures

### Success Criteria

The Analysis Phase is successful when:

1. **Technical Assessment**: All applications evaluated for technical readiness with documented rationale
2. **Operational Assessment**: All applications evaluated for operational readiness with documented rationale
3. **Security Assessment**: All applications evaluated for security readiness with documented rationale
4. **Compliance Assessment**: All applications evaluated for compliance readiness with documented rationale
5. **Business Assessment**: All applications evaluated for business readiness with documented rationale
6. **Readiness Scores**: Overall Cloud_Readiness_Score calculated for all applications
7. **Stakeholder Validation**: Stakeholders confirm accuracy of assessments
8. **Remediation Identified**: Remediation opportunities identified and prioritized

### Validation Procedures

1. **Scoring Consistency Validation**
   - Verify consistent scoring methodology across applications
   - Validate scoring criteria application
   - Confirm peer review of scores
   - Identify and resolve scoring inconsistencies

2. **Assessment Accuracy Validation**
   - Validate assessments with application owners
   - Confirm assessment evidence and rationale
   - Verify assessment completeness
   - Resolve assessment discrepancies

3. **Stakeholder Validation**
   - Present assessments to business stakeholders
   - Collect feedback and validation
   - Address questions and concerns
   - Document stakeholder sign-off

4. **Data Quality Validation**
   - Verify assessment data completeness
   - Validate assessment data accuracy
   - Confirm data consistency
   - Identify and resolve data issues

---

## Stakeholder Engagement Guidance

### Stakeholder Communication Strategy

1. **Executive Sponsors**
   - Weekly status updates on assessment progress
   - Readiness findings and recommendations
   - Key insights and patterns
   - Escalation of major issues

2. **Business Unit Leaders**
   - Application-specific assessment results
   - Readiness scores and interpretation
   - Remediation recommendations
   - Next steps and timeline

3. **Technical Teams**
   - Technical assessment findings
   - Remediation opportunities
   - Cloud architecture recommendations
   - Technical validation sessions

4. **Security and Compliance Teams**
   - Security and compliance assessment findings
   - Risk and compliance recommendations
   - Compliance gap analysis
   - Remediation planning

### Engagement Activities

1. **Assessment Kickoff**: Present assessment methodology and criteria
2. **Working Sessions**: Conduct assessments with application teams
3. **Validation Sessions**: Present findings and collect feedback
4. **Remediation Planning**: Plan remediation activities
5. **Closeout Meeting**: Present Analysis Phase results and readiness for Evaluation Phase

---

## Timeline and Resource Considerations

### Typical Analysis Phase Timeline

| Activity | Duration | Resources |
|----------|----------|-----------|
| Technical Assessment | 4-6 days | Technical Analysts |
| Operational Assessment | 3-5 days | Technical Analysts, Operations |
| Security Assessment | 4-6 days | Security Analyst |
| Compliance Assessment | 3-5 days | Compliance Analyst |
| Business Assessment | 2-4 days | Business Analyst |
| Readiness Scoring | 2-3 days | Assessment Lead, Analysts |
| **Total** | **3–4 weeks** | **5-6 FTE** |

### Resource Allocation by Organization Size

**Small Organizations (10-50 apps)**:
- Assessment Lead: 1 FTE
- Technical Analysts: 1 FTE
- Security Analyst: 0.5 FTE
- Business Analyst: 0.5 FTE
- Total: 3.5 FTE

**Mid-Market Organizations (50-200 apps)**:
- Assessment Lead: 1 FTE
- Technical Analysts: 2 FTE
- Security Analyst: 1 FTE
- Compliance Analyst: 0.5 FTE
- Business Analyst: 1 FTE
- Total: 5.5 FTE

**Enterprise Organizations (200+ apps)**:
- Assessment Lead: 1 FTE
- Technical Analysts: 3 FTE
- Security Analyst: 1.5 FTE
- Compliance Analyst: 1 FTE
- Business Analyst: 1.5 FTE
- Total: 8 FTE

---

## Conclusion

The Analysis Phase transforms discovery data into actionable insights through systematic evaluation of applications across multiple readiness dimensions. By assessing technical, operational, security, compliance, and business readiness, the assessment team provides a comprehensive view of each application's cloud migration readiness.

Success in the Analysis Phase requires expert involvement, consistent methodology, data-driven assessment, and stakeholder validation. By following the step-by-step instructions, best practices, and addressing common challenges, assessment teams can conduct effective analysis and prepare for the Evaluation Phase.

The deliverables from the Analysis Phase—readiness scores, assessment reports, and remediation recommendations—form the foundation for multi-cloud evaluation, business case development, and migration planning in the Evaluation and Planning phases.

---

## Example Output — What Phase 2 Looks Like When Done

The following is drawn from the DMG Media UK engagement. Use this as a quality reference.

### Application Readiness Score Distribution (excerpt)

At the end of Phase 2, you should have a scored readiness profile for every in-scope application. The distribution tells you the migration complexity profile of the estate.

| Readiness Band | Score Range | % of Estate | Migration Approach |
| --- | --- | --- | --- |
| Cloud Ready | 8–10 | ~35% | Rehost — minimal preparation |
| Cloud Friendly | 5–7 | ~40% | Replatform / minor remediation |
| Cloud Challenged | 2–4 | ~20% | Rearchitect or significant prep required |
| Cloud Blocked | 0–1 | ~5% | Retain on-prem or retire |

> In the DMG Media UK engagement, Oracle RAC clusters and Redis OSS instances drove the "Cloud Challenged" category. These workloads require specialist planning and are good candidates for Wave 4 (late migration) rather than early waves.

### Key Flags Surfaced in Phase 2 (DMG Media UK)

These were identified in Analysis and fed directly into the Phase 3 TCO and hyperscaler scoring:

| Finding | Detail | Impact |
| --- | --- | --- |
| End-of-Life OS | 340+ servers on Windows 2012 or RHEL 6 | ESU cost modelled in TCO; upgrade wave prioritised |
| Oracle RAC | 18 clusters — requires BYOL or OCI | Major licensing cost driver; Oracle practice engaged |
| Redis OSS | 140+ instances — OSS licence → Redis Enterprise commercial | Commercial licensing negotiation required |
| SQL Server AHB eligibility | 347 SQL Server instances | £Xm saving via AHB; flagged for Azure preference in Phase 3 |
| Compliance — FCA / GDPR | Customer is a regulated media company | UK-region cloud placement required; data residency constraints |

### Phase 2 Exit Checklist

- [ ] All in-scope applications scored across all five readiness dimensions
- [ ] Cloud Challenged and Cloud Blocked applications documented with specific blockers
- [ ] EoL OS, Oracle, and third-party licence flags surfaced and quantified (even if rough)
- [ ] Compliance and data residency requirements captured per application
- [ ] Governance maturity baseline completed
- [ ] Readiness report issued to customer for validation — no surprises at Phase 3 presentation
- [ ] Phase 3 team briefed — readiness scores handed off; TCO modelling can begin
