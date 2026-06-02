# Industry-Specific Customization Guide

**Version**: 1.0 | **Task**: 11.1 | **Requirements**: 11.1, 11.2

---

## Overview

This guide provides customization recommendations for adapting the Cloud Readiness Accelerator to specific industry contexts. Each industry section covers regulatory considerations, scoring weight adjustments, and additional assessment criteria.

---

## Financial Services

### Regulatory Considerations
- FCA (UK), SEC/FINRA (US), MiFID II (EU) requirements
- PCI-DSS for payment card data
- SOX compliance for financial reporting systems
- Basel III/IV for risk management systems
- DORA (Digital Operational Resilience Act) for EU operations

### Scoring Weight Adjustments
| Dimension | Default Weight | Financial Services Weight | Rationale |
|-----------|---------------|--------------------------|-----------|
| Technical | 25% | 20% | Reduce — mature tech stacks |
| Operational | 20% | 20% | Maintain — operational resilience critical |
| Security | 20% | 25% | **Increase** — heightened security requirements |
| Compliance | 20% | 25% | **Increase** — heavy regulatory burden |
| Business | 15% | 10% | Reduce — business case usually clear |

### Additional Assessment Criteria
- Data sovereignty requirements per jurisdiction
- Real-time transaction processing latency requirements
- Disaster recovery RTO/RPO for Tier 1 systems (<15 min RTO)
- Third-party risk management (cloud as outsourcing)
- Regulatory reporting system migration constraints

---

## Healthcare

### Regulatory Considerations
- HIPAA (US) / NHS DSPT (UK) compliance
- HL7/FHIR interoperability standards
- FDA 21 CFR Part 11 for clinical systems
- GDPR for patient data (EU/UK)
- Medical device regulations (if applicable)

### Scoring Weight Adjustments
| Dimension | Default Weight | Healthcare Weight | Rationale |
|-----------|---------------|-------------------|-----------|
| Technical | 25% | 20% | Reduce — focus on compliance over tech |
| Operational | 20% | 15% | Reduce slightly |
| Security | 20% | 25% | **Increase** — PHI protection critical |
| Compliance | 20% | 30% | **Increase** — HIPAA/regulatory dominant |
| Business | 15% | 10% | Reduce |

### Additional Assessment Criteria
- PHI data identification and classification
- BAA (Business Associate Agreement) requirements with cloud providers
- Clinical system uptime requirements (99.99%+)
- Interoperability with EHR/EMR systems
- Audit trail requirements for clinical data access

---

## Retail & E-Commerce

### Regulatory Considerations
- PCI-DSS for payment processing
- GDPR/CCPA for customer data
- Consumer protection regulations
- Accessibility requirements (WCAG)

### Scoring Weight Adjustments
| Dimension | Default Weight | Retail Weight | Rationale |
|-----------|---------------|---------------|-----------|
| Technical | 25% | 30% | **Increase** — scalability critical |
| Operational | 20% | 25% | **Increase** — peak season resilience |
| Security | 20% | 20% | Maintain |
| Compliance | 20% | 15% | Reduce — fewer regulations vs. FS/HC |
| Business | 15% | 10% | Reduce |

### Additional Assessment Criteria
- Peak season scaling requirements (Black Friday, holiday)
- CDN and edge computing requirements
- Real-time inventory and pricing system latency
- Multi-region deployment for global operations
- PCI-DSS scope and segmentation in cloud

---

## Manufacturing

### Regulatory Considerations
- IEC 62443 for industrial control systems
- NIST SP 800-82 for OT security
- Industry-specific safety regulations
- Supply chain data protection

### Scoring Weight Adjustments
| Dimension | Default Weight | Manufacturing Weight | Rationale |
|-----------|---------------|---------------------|-----------|
| Technical | 25% | 30% | **Increase** — legacy/OT integration complex |
| Operational | 20% | 25% | **Increase** — operational continuity critical |
| Security | 20% | 20% | Maintain |
| Compliance | 20% | 15% | Reduce — fewer data regulations |
| Business | 15% | 10% | Reduce |

### Additional Assessment Criteria
- OT/IT convergence assessment
- Legacy system (SCADA, PLC) cloud connectivity
- Real-time data processing requirements
- Edge computing requirements for factory floor
- Supply chain integration dependencies

---

## How to Apply Customizations

1. Select the industry profile that best matches the organization
2. Adjust scoring dimension weights in the Readiness Scoring Calculator
3. Add industry-specific criteria to the scoring templates
4. Include industry-specific compliance requirements in the Risk Assessment
5. Document all customizations in the assessment report
6. Validate customizations with industry-experienced stakeholders

---

*Guide Version 1.0 — Cloud Readiness Accelerator Framework*
