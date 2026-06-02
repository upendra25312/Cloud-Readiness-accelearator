# Data Validation Checklists & QA Procedures

**Version**: 1.0 | **Tasks**: 12.1, 12.2 | **Requirements**: 14.1-14.6

---

## Section 1: Data Collection Completeness Checklist

### Application Inventory
- [ ] All in-scope applications identified and documented
- [ ] Application owner assigned for each application
- [ ] Business criticality rated for each application
- [ ] Technology stack documented for each application
- [ ] Architecture pattern documented (monolithic/microservices/etc.)
- [ ] Data classification assigned for each application
- [ ] Licensing model documented for each application
- [ ] Coverage: ≥95% of in-scope applications

### Infrastructure Inventory
- [ ] All servers (physical and virtual) documented
- [ ] Operating system and version captured for each server
- [ ] CPU, memory, storage specifications captured
- [ ] Database inventory complete with versions and sizes
- [ ] Storage systems documented with capacity and utilization
- [ ] Network topology documented
- [ ] Coverage: ≥95% of in-scope infrastructure

### Performance Data
- [ ] Minimum 30 days of performance data collected
- [ ] CPU utilization data (avg, peak, p95) for all servers
- [ ] Memory utilization data for all servers
- [ ] Disk I/O metrics for all servers
- [ ] Network throughput data for all servers
- [ ] No gaps >4 hours in collection data
- [ ] Data source documented for each metric

### Dependency Data
- [ ] Application-to-application dependencies documented
- [ ] Application-to-infrastructure dependencies documented
- [ ] External dependencies documented
- [ ] Dependency criticality rated
- [ ] Tight coupling groups identified
- [ ] Dependencies validated with application owners

### Financial Data
- [ ] Current infrastructure costs captured (annual)
- [ ] Software licensing costs captured (annual)
- [ ] Personnel costs captured (annual)
- [ ] Operational costs captured (annual)
- [ ] Cost data validated against financial records
- [ ] Cloud cost estimates obtained from ≥2 sources

---

## Section 2: Data Quality Validation

### Accuracy Checks
| Check | Method | Target | Status |
|-------|--------|--------|--------|
| Server specs match actual | Sample 10% against actual | 95% match | ☐ Pass ☐ Fail |
| Application owners are current | Validate with IT management | 100% current | ☐ Pass ☐ Fail |
| Cost data matches invoices | Cross-reference with finance | 95% match | ☐ Pass ☐ Fail |
| Performance data is representative | Check for anomalies/outages | No major anomalies | ☐ Pass ☐ Fail |
| Dependencies are complete | Validate with app owners | 90% confirmed | ☐ Pass ☐ Fail |

### Consistency Checks
| Check | Method | Target | Status |
|-------|--------|--------|--------|
| No duplicate records | Deduplicate by name/IP | 0 duplicates | ☐ Pass ☐ Fail |
| Consistent naming conventions | Review naming patterns | 95% consistent | ☐ Pass ☐ Fail |
| Cross-source consistency | Compare CMDB vs. monitoring | 90% match | ☐ Pass ☐ Fail |
| Units are normalized | Verify GB/TB, Mbps, etc. | 100% normalized | ☐ Pass ☐ Fail |

### Completeness Checks
| Check | Method | Target | Status |
|-------|--------|--------|--------|
| Required fields populated | Scan for null/empty | ≥95% populated | ☐ Pass ☐ Fail |
| All phases have data | Review per phase | 100% phases covered | ☐ Pass ☐ Fail |
| All dimensions scored | Review scoring templates | 100% scored | ☐ Pass ☐ Fail |

---

## Section 3: Peer Review Procedure

### Review Process
1. **Reviewer Assignment**: Assign independent reviewer (not the original assessor)
2. **Review Scope**: Findings, scores, recommendations, business case
3. **Review Checklist**:
   - [ ] Scoring rationale is documented and justified
   - [ ] Evidence supports the assigned scores
   - [ ] Recommendations are actionable and realistic
   - [ ] Business case assumptions are documented and reasonable
   - [ ] Risk assessment is comprehensive
   - [ ] Migration wave plan accounts for dependencies
   - [ ] Report is clear, consistent, and complete
4. **Feedback**: Document findings in peer review form
5. **Resolution**: Original assessor addresses feedback
6. **Sign-off**: Reviewer confirms issues resolved

### Peer Review Form

| Section Reviewed | Finding | Severity | Resolution | Status |
|-----------------|---------|----------|-----------|--------|
| | | ☐ Critical ☐ Major ☐ Minor | | ☐ Open ☐ Resolved |

---

## Section 4: Stakeholder Validation Procedure

### Validation Sessions
1. **Application Owners**: Validate application profiles, dependencies, readiness scores
2. **Infrastructure Team**: Validate infrastructure data, performance baselines
3. **Finance Team**: Validate cost data, business case assumptions
4. **Security/Compliance**: Validate risk assessment, compliance requirements
5. **Executive Stakeholders**: Validate recommendations, migration roadmap

### Validation Sign-off

| Stakeholder | Area Validated | Date | Status | Comments |
|------------|---------------|------|--------|----------|
| | Application profiles | | ☐ Approved ☐ Approved with changes ☐ Rejected | |
| | Infrastructure data | | ☐ Approved ☐ Approved with changes ☐ Rejected | |
| | Financial data | | ☐ Approved ☐ Approved with changes ☐ Rejected | |
| | Risk assessment | | ☐ Approved ☐ Approved with changes ☐ Rejected | |
| | Recommendations | | ☐ Approved ☐ Approved with changes ☐ Rejected | |

---

## Section 5: Discrepancy Resolution

| ID | Source 1 | Source 2 | Discrepancy | Resolution | Resolved By | Date |
|----|---------|---------|-------------|-----------|------------|------|
| | | | | ☐ Use Source 1 ☐ Use Source 2 ☐ New Value | | |

**Escalation**: If discrepancy cannot be resolved within 2 business days, escalate to Program Director.

---

*QA Framework Version 1.0 — Cloud Readiness Accelerator Framework*
