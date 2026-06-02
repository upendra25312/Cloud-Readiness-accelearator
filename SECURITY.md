# Security Policy

## Supported Versions

This repository contains framework documentation, templates, and reference materials — not executable software. There are no versioned software releases with security patch cycles.

If you identify a security concern related to sensitive data exposure in this repository, follow the reporting process below.

## Reporting a Security Concern

**Do not open a public GitHub issue for security concerns.**

If you discover:
- Personally identifiable information (PII) that should not be in this repository
- Customer-confidential data that has been inadvertently published
- Any other sensitive content requiring immediate removal

Please report it directly to:

**Email:** [security@rackspace.com](mailto:security@rackspace.com)  
**Subject line:** `[CRA Framework] Security concern — <brief description>`

Include:
- The file path or URL where the sensitive content is located
- A brief description of what the content is and why it is sensitive
- Your contact details so we can follow up

We aim to acknowledge reports within 2 business days and resolve confirmed issues within 5 business days.

## Data Classification — What This Repository Contains

| Content Type | Classification | Notes |
|---|---|---|
| Framework templates (`.xlsx`, `.docx`, `.pptx`) | Public | Generic, customer-agnostic |
| Phase guides and methodology docs (`.md`) | Public | No customer references |
| Reference examples (`Examples/aws/`, `Examples/azure/`) | Public | Anonymized — no customer-identifying data |
| Executive presentations (`presentations/`) | Public | Rackspace-branded, no customer data |
| Alliance partner materials | Public | Publicly available partner programme content |

## What Is Explicitly Excluded

The following categories of files are excluded from this repository via `.gitignore` and must never be committed:

- Customer SOW documents
- Customer RFP or tender documents
- Customer-branded executive reports or presentations
- Any file containing real customer names, pricing, or infrastructure data
- Internal Rackspace pricing models or partner discount structures
- Local IDE and tool configuration files (`.claude/`, `.vscode/`, `.kiro/`)

## Responsible Use

This framework is provided for professional services use by Rackspace Technology and its partners. When using these templates in a real engagement:

- Do not store completed customer workbooks in this repository
- Do not commit customer data to any branch, including private forks
- Follow your organisation's data classification and handling policies

---

*Rackspace Cloud Solutions Architecture*  
*© Rackspace Technology. All rights reserved.*
