# Cloud Readiness Accelerator - Discovery Phase Guide

## Phase Overview

The Discovery Phase is the foundation of the cloud readiness assessment. This phase focuses on understanding the current state of the organization's applications, infrastructure, and business context. The primary objectives are to establish a complete inventory of applications and infrastructure, identify key stakeholders, define assessment scope, and collect baseline data for subsequent analysis phases.

### Phase Objectives

1. Identify and engage all relevant stakeholders across business, technology, and operations
2. Define the scope of the assessment including applications, infrastructure, and business units in scope
3. Discover and inventory all applications and infrastructure components
4. Document application and infrastructure characteristics and dependencies
5. Establish baseline data for readiness evaluation
6. Validate data completeness and accuracy
7. Prepare for the Analysis Phase with complete and accurate data

### Phase Duration and Resources

- **Typical Duration**: 2-4 weeks (varies by organization size)
- **Small Organizations (10-50 apps)**: 1-2 weeks
- **Mid-Market Organizations (50-200 apps)**: 2-3 weeks
- **Enterprise Organizations (200+ apps)**: 3-4 weeks

### Resource Requirements

- **Assessment Lead**: 1 FTE (full-time equivalent)
- **Technical Leads**: 1-2 FTE (depending on organization size)
- **Business Analysts**: 1 FTE
- **Data Analysts**: 0.5 FTE
- **Stakeholder Representatives**: 0.5-1 FTE (part-time from business units)

---

## Phase Entry and Exit Criteria

### Entry Criteria

Before starting the Discovery Phase, ensure:

1. **Stakeholder Sponsorship**: Executive sponsor and steering committee identified and committed
2. **Scope Definition**: High-level scope approved including business units and application categories in scope
3. **Resource Allocation**: Assessment team resources allocated and available
4. **Tool Access**: Access to CMDB, monitoring systems, and other data sources confirmed
5. **Communication Plan**: Communication plan established and stakeholders notified of assessment initiation

### Exit Criteria

The Discovery Phase is complete when:

1. **Stakeholder Engagement**: All key stakeholders identified and engaged
2. **Application Inventory**: Complete inventory of applications in scope with metadata captured
3. **Infrastructure Inventory**: Complete inventory of infrastructure components with specifications
4. **Dependency Mapping**: Application and infrastructure dependencies documented
5. **Data Validation**: Data quality validation completed with discrepancies resolved
6. **Baseline Established**: Baseline data established for Analysis Phase
7. **Readiness Confirmed**: Assessment team confirms data completeness and readiness to proceed

---

## Step-by-Step Activity Instructions

### Activity 1: Stakeholder Identification and Engagement

**Objective**: Identify all relevant stakeholders and establish engagement model

**Duration**: 2-3 days

**Steps**:

1. **Identify Stakeholder Categories**
   - Executive sponsors and steering committee members
   - Business unit leaders and application owners
   - Technology leaders (CTO, infrastructure, database, security)
   - Operations and support teams
   - Finance and procurement stakeholders
   - Compliance and security officers

2. **Create Stakeholder Register**
   - Document stakeholder name, title, organization, and contact information
   - Identify stakeholder role in assessment (sponsor, contributor, reviewer, decision-maker)
   - Assess stakeholder interest and influence levels
   - Identify potential conflicts of interest or concerns

3. **Develop Engagement Strategy**
   - Define communication frequency and channels for each stakeholder group
   - Schedule kickoff meeting with executive sponsors and steering committee
   - Schedule working sessions with technical and business teams
   - Establish escalation procedures for issues and conflicts

4. **Conduct Kickoff Meeting**
   - Present assessment objectives, scope, and timeline
   - Explain stakeholder roles and responsibilities
   - Address questions and concerns
   - Confirm commitment and resource allocation

5. **Establish Governance Structure**
   - Define steering committee charter and meeting cadence
   - Define working group structure and responsibilities
   - Establish decision-making authority and escalation procedures
   - Document governance model in governance template

**Deliverables**:
- Stakeholder Register (spreadsheet with stakeholder information)
- Engagement Strategy Document
- Governance Model Documentation
- Meeting minutes from kickoff

**Best Practices**:
- Engage executive sponsors early to ensure organizational commitment
- Include representatives from all major business units and technology domains
- Establish clear communication channels and meeting cadence
- Document stakeholder concerns and address them proactively
- Ensure diversity of perspectives in stakeholder group

**Common Pitfalls**:
- Missing key stakeholders (especially from operations or compliance)
- Insufficient executive sponsorship leading to resource constraints
- Unclear roles and responsibilities causing confusion
- Inadequate communication leading to stakeholder disengagement
- Conflicts of interest not identified or managed

---

### Activity 2: Scope Definition

**Objective**: Define the scope of the assessment including applications, infrastructure, and business units

**Duration**: 3-5 days

**Steps**:

1. **Define Assessment Scope**
   - Identify business units in scope (all or specific units)
   - Identify application categories in scope (all or specific categories)
   - Identify infrastructure components in scope (all or specific types)
   - Document scope boundaries and exclusions

2. **Identify Scope Constraints**
   - Identify time constraints affecting assessment depth
   - Identify resource constraints affecting assessment breadth
   - Identify organizational constraints (e.g., restricted access to certain systems)
   - Identify technical constraints (e.g., legacy systems with limited data availability)

3. **Define Assessment Depth**
   - Determine assessment depth: light, standard, or comprehensive
   - Light assessment: High-level overview, 1-2 weeks, 50-100 apps
   - Standard assessment: Detailed analysis, 2-3 weeks, 50-200 apps
   - Comprehensive assessment: In-depth analysis, 3-4 weeks, 200+ apps

4. **Document Scope Statement**
   - Create formal scope statement including in-scope and out-of-scope items
   - Document scope constraints and assumptions
   - Identify scope change control procedures
   - Get stakeholder approval on scope statement

5. **Identify Data Sources**
   - Identify CMDB systems and access procedures
   - Identify monitoring systems and data availability
   - Identify financial systems for cost data
   - Identify other data sources (spreadsheets, documentation, etc.)

**Deliverables**:
- Scope Statement Document
- Scope Constraints and Assumptions Document
- Data Sources Inventory
- Scope Approval Sign-off

**Best Practices**:
- Define scope clearly to avoid scope creep
- Document constraints and assumptions explicitly
- Get stakeholder agreement on scope before proceeding
- Identify data sources early to plan data collection activities
- Consider assessment depth based on organization size and complexity

**Common Pitfalls**:
- Scope too broad leading to assessment delays
- Scope too narrow missing important applications or infrastructure
- Unclear scope boundaries causing confusion during data collection
- Inadequate data source identification leading to incomplete data
- Scope changes not managed through change control process

---

### Activity 3: Application Discovery and Inventory

**Objective**: Discover and inventory all applications in scope

**Duration**: 5-10 days (depending on organization size)

**Steps**:

1. **Extract CMDB Data**
   - Connect to CMDB system (ServiceNow, BMC, etc.)
   - Extract configuration items (CIs) for applications in scope
   - Extract CI relationships and dependencies
   - Validate extracted data for completeness and accuracy
   - Export data to assessment templates

2. **Conduct Application Interviews**
   - Schedule interviews with application owners and technical leads
   - Use application discovery template to guide interviews
   - Capture application metadata: name, owner, business criticality, platform, tech stack
   - Capture application characteristics: architecture pattern, performance, licensing
   - Capture application data: data classification, sensitivity, residency requirements
   - Document any data gaps or discrepancies

3. **Validate Application Inventory**
   - Cross-check CMDB data with interview data
   - Identify and resolve discrepancies
   - Verify completeness of application inventory
   - Confirm application owners and business criticality
   - Document any applications not in CMDB

4. **Consolidate Application Data**
   - Consolidate data from multiple sources into master application inventory
   - Standardize application names and identifiers
   - Normalize data formats and values
   - Create application inventory spreadsheet with all metadata

5. **Identify Data Gaps**
   - Identify applications with incomplete data
   - Prioritize data collection for critical applications
   - Schedule follow-up interviews or data collection activities
   - Document data gaps and remediation plan

**Deliverables**:
- Application Inventory Spreadsheet (with all metadata)
- CMDB Extract Report
- Application Interview Notes
- Data Gap Analysis and Remediation Plan

**Best Practices**:
- Start with CMDB data to establish baseline
- Conduct interviews with application owners for accuracy and completeness
- Validate data from multiple sources to ensure accuracy
- Prioritize critical applications for detailed data collection
- Document data sources and collection dates for audit trail

**Common Pitfalls**:
- Incomplete CMDB data leading to missing applications
- Application owners unavailable or unresponsive
- Inconsistent application naming across systems
- Data quality issues (missing fields, incorrect values)
- Difficulty accessing CMDB or other data sources

---

### Activity 4: Infrastructure Profiling

**Objective**: Profile all infrastructure components supporting applications in scope

**Duration**: 3-5 days

**Steps**:

1. **Extract Infrastructure Data from CMDB**
   - Extract server inventory (physical and virtual)
   - Extract database inventory and specifications
   - Extract storage and networking infrastructure
   - Extract operating system and middleware information
   - Validate extracted data for completeness

2. **Capture Server Specifications**
   - Document server name, type (physical/virtual), and location
   - Capture CPU, memory, and storage specifications
   - Document operating system and version
   - Capture server utilization metrics (CPU, memory, disk)
   - Document server support status and end-of-life dates

3. **Capture Database Specifications**
   - Document database name, type (Oracle, SQL Server, PostgreSQL, etc.)
   - Capture database version and support status
   - Document database size and growth rate
   - Capture database performance characteristics
   - Document database licensing model

4. **Capture Storage and Networking**
   - Document storage systems and capacity
   - Capture storage utilization and growth trends
   - Document network infrastructure and bandwidth
   - Capture network performance characteristics
   - Document any specialized networking requirements

5. **Consolidate Infrastructure Data**
   - Consolidate infrastructure data from multiple sources
   - Create infrastructure inventory spreadsheet
   - Link infrastructure to applications (application-to-infrastructure mapping)
   - Identify infrastructure components not linked to applications

**Deliverables**:
- Infrastructure Inventory Spreadsheet
- Server Specifications Report
- Database Inventory Report
- Storage and Networking Report
- Application-to-Infrastructure Mapping

**Best Practices**:
- Use CMDB as primary data source for infrastructure
- Validate infrastructure data with operations teams
- Capture performance metrics for capacity planning
- Document infrastructure support status and end-of-life dates
- Link infrastructure to applications for dependency analysis

**Common Pitfalls**:
- Incomplete infrastructure inventory (especially virtual machines)
- Outdated infrastructure data in CMDB
- Difficulty accessing infrastructure performance metrics
- Infrastructure components not linked to applications
- Specialized infrastructure (storage, networking) not captured

---

### Activity 5: Dependency Mapping

**Objective**: Document application and infrastructure dependencies

**Duration**: 5-7 days

**Steps**:

1. **Identify Application-to-Application Dependencies**
   - Interview application owners about dependencies
   - Review application architecture documentation
   - Analyze application logs and monitoring data for communication patterns
   - Document dependency type: synchronous, asynchronous, batch, real-time
   - Document dependency criticality: critical, high, medium, low

2. **Identify Application-to-Infrastructure Dependencies**
   - Document application dependencies on specific servers
   - Document application dependencies on specific databases
   - Document application dependencies on storage and networking
   - Document any specialized infrastructure requirements
   - Identify single points of failure

3. **Identify External Dependencies**
   - Document dependencies on third-party services and APIs
   - Document dependencies on external data sources
   - Document dependencies on partner systems
   - Identify any SaaS or cloud service dependencies
   - Document external dependency criticality and availability

4. **Analyze Dependency Chains**
   - Identify critical dependency chains
   - Identify circular dependencies or complex interdependencies
   - Identify applications with high dependency complexity
   - Identify applications with few dependencies (good migration candidates)
   - Document dependency analysis findings

5. **Create Dependency Visualization**
   - Create dependency diagrams showing application relationships
   - Create infrastructure dependency diagrams
   - Identify clusters of tightly coupled applications
   - Identify applications suitable for parallel migration
   - Document dependency visualization for stakeholder review

**Deliverables**:
- Application Dependency Matrix (spreadsheet)
- Infrastructure Dependency Documentation
- External Dependency Register
- Dependency Chain Analysis Report
- Dependency Diagrams and Visualizations

**Best Practices**:
- Interview application owners for accurate dependency information
- Use monitoring data to validate dependencies
- Document dependency criticality for migration planning
- Identify circular dependencies and complex interdependencies
- Create visualizations to help stakeholders understand dependencies

**Common Pitfalls**:
- Incomplete dependency information from application owners
- Difficulty accessing monitoring data for dependency analysis
- Undocumented or informal dependencies
- Circular dependencies not identified
- External dependencies not fully understood

---

### Activity 6: Data Collection and Validation

**Objective**: Collect and validate all assessment data

**Duration**: 3-5 days

**Steps**:

1. **Conduct Data Quality Validation**
   - Verify completeness: all required fields populated
   - Verify accuracy: data matches source systems
   - Verify consistency: data consistent across sources
   - Identify data quality issues and gaps
   - Create data quality report

2. **Resolve Data Discrepancies**
   - Identify discrepancies between CMDB and interview data
   - Investigate root causes of discrepancies
   - Determine authoritative data source
   - Update data to reflect correct information
   - Document discrepancy resolution

3. **Conduct Stakeholder Validation**
   - Present application inventory to business stakeholders
   - Confirm application names, owners, and criticality
   - Validate dependency information
   - Collect feedback and corrections
   - Update data based on stakeholder feedback

4. **Perform Completeness Check**
   - Verify all applications in scope have complete metadata
   - Verify all infrastructure components are documented
   - Verify all dependencies are captured
   - Identify any remaining data gaps
   - Create remediation plan for data gaps

5. **Prepare Data for Analysis Phase**
   - Export validated data to analysis templates
   - Create master data repository
   - Document data sources and collection dates
   - Create data dictionary for analysis team
   - Prepare data handoff to Analysis Phase

**Deliverables**:
- Data Quality Report
- Discrepancy Resolution Log
- Stakeholder Validation Sign-off
- Completeness Checklist
- Master Data Repository
- Data Dictionary

**Best Practices**:
- Validate data from multiple sources
- Involve stakeholders in data validation
- Document data sources and collection procedures
- Create audit trail of data changes
- Prepare data in formats suitable for analysis

**Common Pitfalls**:
- Insufficient data validation leading to poor analysis
- Data discrepancies not resolved
- Stakeholders not involved in validation
- Data gaps not identified until Analysis Phase
- Data not properly prepared for downstream analysis

---

## Best Practices and Lessons Learned

### Stakeholder Engagement Best Practices

1. **Executive Sponsorship**: Secure strong executive sponsorship to ensure organizational commitment and resource allocation
2. **Clear Communication**: Communicate assessment objectives, timeline, and expectations clearly to all stakeholders
3. **Regular Updates**: Provide regular status updates to steering committee and working groups
4. **Address Concerns**: Proactively address stakeholder concerns and questions
5. **Celebrate Milestones**: Recognize and celebrate completion of discovery activities

### Data Collection Best Practices

1. **Leverage Existing Systems**: Use CMDB and monitoring systems as primary data sources to reduce manual effort
2. **Standardize Data**: Establish data standards and naming conventions early
3. **Validate Early**: Validate data as it's collected rather than waiting until the end
4. **Document Sources**: Document data sources and collection procedures for audit trail
5. **Prioritize Critical Applications**: Focus detailed data collection on critical applications

### Dependency Mapping Best Practices

1. **Use Multiple Sources**: Combine interviews, documentation, and monitoring data for accurate dependencies
2. **Visualize Dependencies**: Create diagrams to help stakeholders understand complex dependencies
3. **Identify Tight Coupling**: Identify applications that must migrate together
4. **Document Criticality**: Document dependency criticality for migration planning
5. **Validate with Operations**: Validate dependencies with operations teams

### Common Lessons Learned

1. **CMDB Data Quality**: CMDB data is often incomplete or outdated; plan for data validation and correction
2. **Stakeholder Availability**: Key stakeholders are often busy; schedule interviews well in advance
3. **Undocumented Dependencies**: Many dependencies are undocumented; use monitoring data to identify them
4. **Data Standardization**: Data from different sources uses different naming conventions; plan for normalization
5. **Scope Creep**: Scope tends to expand; manage scope changes through formal change control

---

## Common Challenges and Solutions

### Challenge 1: Incomplete CMDB Data

**Problem**: CMDB is missing applications or has outdated information

**Solutions**:
- Conduct interviews with application owners to identify missing applications
- Use monitoring systems to identify active applications not in CMDB
- Implement CMDB data quality improvement process
- Prioritize CMDB updates for critical applications
- Plan for manual data collection for applications not in CMDB

### Challenge 2: Stakeholder Unavailability

**Problem**: Key stakeholders are too busy to participate in interviews

**Solutions**:
- Schedule interviews well in advance
- Offer flexible meeting times and formats (in-person, virtual, asynchronous)
- Prepare detailed questionnaires to minimize meeting time
- Use surveys for initial data collection, follow up with interviews
- Escalate to executive sponsor if stakeholders are unavailable

### Challenge 3: Undocumented Dependencies

**Problem**: Many dependencies are not documented in CMDB or application documentation

**Solutions**:
- Use monitoring systems (Splunk, Datadog, etc.) to identify communication patterns
- Analyze application logs for dependency information
- Conduct detailed interviews with application architects
- Use network monitoring to identify infrastructure dependencies
- Create dependency diagrams to validate with stakeholders

### Challenge 4: Data Quality Issues

**Problem**: Data from different sources is inconsistent or incomplete

**Solutions**:
- Establish data quality standards and validation procedures
- Create data normalization procedures
- Implement data validation checks
- Conduct stakeholder validation of data
- Create data quality improvement plan

### Challenge 5: Access to Data Sources

**Problem**: Difficulty accessing CMDB, monitoring systems, or other data sources

**Solutions**:
- Identify data source access requirements early
- Work with IT operations to establish access
- Use service accounts for automated data extraction
- Plan for manual data collection if automated access not available
- Document access procedures for future assessments

---

## Templates and Tools to Use

### Discovery Phase Templates

1. **Stakeholder Register Template**
   - Stakeholder name, title, organization, contact information
   - Stakeholder role in assessment
   - Interest and influence levels
   - Potential conflicts of interest

2. **Scope Statement Template**
   - Assessment objectives and scope
   - In-scope and out-of-scope items
   - Scope constraints and assumptions
   - Scope change control procedures

3. **Application Discovery Template**
   - Application name and identifier
   - Application owner and business unit
   - Business criticality (critical, high, medium, low)
   - Current platform and technology stack
   - Architecture pattern (monolithic, microservices, serverless)
   - Performance characteristics (CPU, memory, storage, network)
   - Licensing model and vendor support
   - Data classification and sensitivity

4. **Infrastructure Profiling Template**
   - Server name, type, and location
   - CPU, memory, and storage specifications
   - Operating system and version
   - Database name, type, and version
   - Storage and networking specifications
   - Infrastructure utilization metrics

5. **Dependency Mapping Template**
   - Source and target application/infrastructure
   - Dependency type (synchronous, asynchronous, batch, real-time)
   - Dependency criticality (critical, high, medium, low)
   - Dependency description and constraints

6. **Data Quality Validation Template**
   - Data element name and description
   - Data quality criteria (completeness, accuracy, consistency)
   - Validation results and issues
   - Remediation actions and status

### Discovery Phase Tools

1. **CMDB Systems**: ServiceNow, BMC Atrium, etc.
2. **Monitoring Systems**: Splunk, Datadog, New Relic, Prometheus
3. **Spreadsheet Tools**: Excel, Google Sheets
4. **Diagramming Tools**: Visio, Lucidchart, Draw.io
5. **Survey Tools**: SurveyMonkey, Qualtrics, Google Forms
6. **Collaboration Tools**: Confluence, SharePoint, Teams

---

## Success Criteria and Validation Procedures

### Success Criteria

The Discovery Phase is successful when:

1. **Stakeholder Engagement**: All key stakeholders identified and actively engaged
2. **Application Inventory**: Complete inventory of applications in scope with 95%+ data completeness
3. **Infrastructure Inventory**: Complete inventory of infrastructure components with 95%+ data completeness
4. **Dependency Mapping**: All critical dependencies documented and validated
5. **Data Quality**: Data quality validation completed with 90%+ accuracy
6. **Stakeholder Validation**: Stakeholders confirm accuracy of discovered data
7. **Readiness Confirmation**: Assessment team confirms readiness to proceed to Analysis Phase

### Validation Procedures

1. **Data Completeness Validation**
   - Verify all required fields populated for 95%+ of applications
   - Verify all required fields populated for 95%+ of infrastructure components
   - Identify and remediate data gaps

2. **Data Accuracy Validation**
   - Cross-check CMDB data with interview data
   - Validate application criticality with business stakeholders
   - Validate infrastructure specifications with operations teams
   - Resolve discrepancies through investigation and correction

3. **Dependency Validation**
   - Validate dependencies with application owners
   - Validate dependencies with monitoring data
   - Confirm critical dependencies with operations teams
   - Identify any missing or incorrect dependencies

4. **Stakeholder Validation**
   - Present application inventory to business stakeholders
   - Collect feedback and corrections
   - Confirm application owners and criticality
   - Document stakeholder sign-off

5. **Completeness Checklist**
   - Verify all applications in scope are discovered
   - Verify all infrastructure components are documented
   - Verify all dependencies are captured
   - Verify all required metadata is collected

---

## Stakeholder Engagement Guidance

### Stakeholder Communication Strategy

1. **Executive Sponsors**
   - Monthly steering committee meetings
   - Executive summary updates
   - Escalation of major issues or risks
   - Quarterly business reviews

2. **Business Unit Leaders**
   - Bi-weekly working group meetings
   - Application inventory reviews
   - Dependency validation sessions
   - Feedback collection on assessment progress

3. **Technical Teams**
   - Weekly technical working sessions
   - Infrastructure profiling reviews
   - Dependency mapping validation
   - Data quality discussions

4. **Operations Teams**
   - Infrastructure data collection sessions
   - Dependency validation with operations
   - Performance metrics collection
   - Infrastructure support status confirmation

### Engagement Activities

1. **Kickoff Meeting**: Present assessment objectives, scope, and timeline
2. **Working Sessions**: Conduct interviews and data collection activities
3. **Validation Sessions**: Present findings and collect feedback
4. **Status Updates**: Provide regular progress updates to steering committee
5. **Closeout Meeting**: Present Discovery Phase results and readiness for Analysis Phase

---

## Timeline and Resource Considerations

### Typical Discovery Phase Timeline

| Activity | Duration | Resources |
|----------|----------|-----------|
| Stakeholder Identification | 2-3 days | Assessment Lead, Business Analyst |
| Scope Definition | 3-5 days | Assessment Lead, Technical Lead |
| Application Discovery | 5-10 days | Technical Lead, Data Analyst |
| Infrastructure Profiling | 3-5 days | Technical Lead, Operations |
| Dependency Mapping | 5-7 days | Technical Lead, Application Owners |
| Data Validation | 3-5 days | Data Analyst, Assessment Lead |
| **Total** | **2-4 weeks** | **3-4 FTE** |

### Resource Allocation by Organization Size

**Small Organizations (10-50 apps)**:
- Assessment Lead: 1 FTE
- Technical Lead: 0.5 FTE
- Business Analyst: 0.5 FTE
- Total: 2 FTE

**Mid-Market Organizations (50-200 apps)**:
- Assessment Lead: 1 FTE
- Technical Leads: 1.5 FTE
- Business Analyst: 1 FTE
- Data Analyst: 0.5 FTE
- Total: 4 FTE

**Enterprise Organizations (200+ apps)**:
- Assessment Lead: 1 FTE
- Technical Leads: 2 FTE
- Business Analysts: 1.5 FTE
- Data Analysts: 1 FTE
- Total: 5.5 FTE

---

## Conclusion

The Discovery Phase establishes the foundation for the entire cloud readiness assessment. By systematically discovering and profiling applications and infrastructure, engaging stakeholders, and validating data quality, the assessment team ensures that subsequent analysis phases are based on accurate and complete information.

Success in the Discovery Phase requires strong stakeholder engagement, systematic data collection, rigorous data validation, and clear communication. By following the step-by-step instructions, best practices, and addressing common challenges, assessment teams can conduct effective discovery activities and prepare for the Analysis Phase.

The deliverables from the Discovery Phase—application inventory, infrastructure profiles, dependency maps, and validated data—form the foundation for readiness scoring, business case development, and migration planning in subsequent phases.
