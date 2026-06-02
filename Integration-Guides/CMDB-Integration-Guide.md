# CMDB Integration Guide

**Version**: 1.0 | **Task**: 10.1 | **Requirements**: 10.1, 15.1

---

## Overview

This guide provides procedures for extracting application and infrastructure data from CMDB systems (ServiceNow, BMC Helix, etc.) to populate Cloud Readiness Accelerator templates.

---

## ServiceNow Integration

### Data Extraction Queries

**Application Inventory**:
```
Table: cmdb_ci_appl
Fields: name, short_description, owned_by, operational_status, business_criticality, 
        environment, platform, version, vendor, support_group
Filter: operational_status = 1 (Operational)
```

**Server Inventory**:
```
Table: cmdb_ci_server
Fields: name, os, os_version, cpu_count, ram, disk_space, ip_address, 
        dns_domain, location, environment, operational_status
Filter: operational_status = 1 (Operational)
```

**Database Inventory**:
```
Table: cmdb_ci_database
Fields: name, type, version, instance_name, port, size_bytes, 
        host, operational_status
Filter: operational_status = 1 (Operational)
```

**Relationships/Dependencies**:
```
Table: cmdb_rel_ci
Fields: parent, child, type
Join: cmdb_rel_type for relationship type names
```

### Export Formats
- CSV export via ServiceNow Reports module
- Excel export via ServiceNow Export functionality
- JSON via ServiceNow REST API: `GET /api/now/table/{table_name}`

---

## BMC Helix / Remedy Integration

### Data Extraction
- Use BMC Atrium CMDB REST API
- Export via BMC Reporting module
- Use ITSM integration for relationship data

### Key Tables
- `BMC_COMPUTERSYSTEM` — Servers
- `BMC_APPLICATION` — Applications
- `BMC_DATABASE` — Databases
- `BMC_BASERELATIONSHIP` — Dependencies

---

## Data Mapping to Accelerator Templates

| CMDB Field | Accelerator Template Field | Transformation |
|-----------|--------------------------|---------------|
| name | Application Name | Direct |
| owned_by | Application Owner | Lookup display name |
| business_criticality | Business Criticality | Map: 1=Critical, 2=High, 3=Medium, 4=Low |
| os + os_version | Operating System | Concatenate |
| cpu_count | CPU Cores | Direct |
| ram | RAM (GB) | Convert MB to GB if needed |
| disk_space | Storage (GB) | Convert MB to GB if needed |
| environment | Environment | Map: Production/Staging/Dev/DR |

---

## Data Validation Procedures

1. **Completeness Check**: Verify all required fields are populated (>95% target)
2. **Accuracy Check**: Sample 10% of records and validate against actual infrastructure
3. **Currency Check**: Verify last_discovered date is within 90 days
4. **Relationship Check**: Validate dependency relationships with application owners
5. **Duplicate Check**: Identify and merge duplicate CIs

### Common Data Quality Issues

| Issue | Detection | Resolution |
|-------|----------|-----------|
| Missing owner | owned_by is null | Contact IT management for assignment |
| Stale data | last_discovered > 90 days | Re-run discovery or manual validation |
| Duplicate CIs | Same name/IP across records | Merge records, keep most recent |
| Missing relationships | Application with no dependencies | Interview application owners |
| Incorrect criticality | Default values not updated | Business owner validation |

---

## Error Handling

| Error | Cause | Resolution |
|-------|-------|-----------|
| Connection timeout | Network/firewall issue | Check connectivity, VPN, firewall rules |
| Authentication failure | Credentials expired | Refresh API credentials |
| Rate limiting | Too many API calls | Implement pagination, add delays |
| Data format mismatch | Schema changes | Update field mappings |
| Missing tables | Insufficient permissions | Request CMDB read access |

---

*Guide Version 1.0 — Cloud Readiness Accelerator Framework*
