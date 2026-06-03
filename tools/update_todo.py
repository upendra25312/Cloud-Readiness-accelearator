#!/usr/bin/env python3
"""Update the TODO tracker to mark completed tasks."""
import os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODO = os.path.join(BASE, "CLOUD-READINESS-ACCELERATOR-TODO.md")

with open(TODO, 'r', encoding='utf-8') as f:
    content = f.read()

# Tasks to mark complete: list of (task_id, new_notes)
completions = [
    # 4A Discovery templates
    ("4A.1", "Instructions tab added, Summary tab added, Oracle/OSS flag columns documented"),
    ("4A.2", "Instructions tab added, Data Quality Summary tab added with GATE 1 checklist"),
    ("4A.3", "Instructions tab added, Dependency Heat Map tab added"),
    ("4A.4", "Created: Templates/01-discovery/saas-application-assessment.xlsx with Instructions + SaaS Inventory tabs"),
    ("4A.5", "Instructions tabs added to all Discovery templates (application-scoping, infrastructure-profiling, dependency-mapping)"),
    # 4B TCO templates
    ("4B.1", "All 7 layers now present: L4L, Optimised, Delta, Licensing-Overlay, OnPrem-StatusQuo, Year1-DualRunning, Partner-Credits tabs added to business-case-tco-roi.xlsx"),
    ("4B.2", "AHB Overlay tab added with Windows/SQL AHB + EoL ESU saving calculator; Instructions tab added"),
    ("4B.3", "Savings Plans tab and 3yr RI All-Upfront tab added; Instructions tab added"),
    ("4B.4", "3yr CUD tab and Managed Services (OSS alternatives) tab added; Instructions tab added"),
    ("4B.5", "OnPrem-StatusQuo tab added to business-case-tco-roi.xlsx: hardware, DC, VMware, OS, SQL, Oracle, ESU, operations rows"),
    ("4B.6", "Year1-DualRunning tab added to business-case-tco-roi.xlsx: quarterly breakdown with on-prem remaining + cloud ramp + tooling + PS + partner credit offset"),
    ("4B.7", "Licensing-Overlay tab added to business-case-tco-roi.xlsx: Windows AHB, SQL AHB, Oracle BYOL, EoL ESU sections"),
    ("4B.8", "Partner-Credits tab added to business-case-tco-roi.xlsx: AMM / MAP / PSO rows + 3yr net cost summary"),
    # 4D.3 Part 2 DOCX
    ("4D.3", "Created: Templates/executive-reporting/part2-entry-point-template.docx -- all 10 sections, cover page, tables, DMG examples, appendix glossary"),
    # 4E Governance templates
    ("4E.1", "Gap Register, Summary Dashboard, CAF-WAF-GAF Alignment tabs added to governance-foundations-alignment.xlsx"),
    ("4E.2", "Instructions tab added; pre-populated 11 default risk rows (all categories); Risk Summary dashboard tab added"),
    # Epic 5 presentations
    ("5.1", "Built: presentations/executive/CRA-Leadership-Overview.pptx (12 slides) using Rackspace template"),
    ("5.4", "Built: presentations/executive/CRA-Executive-Overview.pptx (12 slides) using Rackspace template"),
    ("5.5", "Built: presentations/technical/CRA-Technical-Overview.pptx (12 slides) using Rackspace template"),
    ("5.6", "Built: presentations/alliance/CRA-Microsoft-Partner-Deck.pptx (11 slides) using Rackspace template + Azure Blue co-branding"),
    ("5.7", "Built: presentations/alliance/CRA-AWS-Partner-Deck.pptx (9 slides) using Rackspace template + AWS Orange co-branding"),
    ("5.8", "Built: presentations/alliance/CRA-GCP-Partner-Deck.pptx (9 slides) using Rackspace template + GCP Blue co-branding"),
    # 10.4 Instructions tabs
    ("10.4", "Instructions tabs added to all Excel templates: Discovery (3 templates), Governance, Risk, Azure/AWS/GCP eval, Business case"),
]

changed = 0
for task_id, new_notes in completions:
    # Pattern: | TASK_ID | ... | 🟡 In Progress | old notes |
    # Replace status + notes
    pattern = rf'(\| {re.escape(task_id)} \|[^|]*\|[^|]*\|[^|]*\|) 🟡 In Progress \|([^|]*)\|'
    replacement = rf'\1 🟢 Complete |\2|'
    new_content, n = re.subn(pattern, replacement, content)
    if n > 0:
        content = new_content
        changed += n
        print(f"  Marked complete: {task_id}")
    else:
        # Try alternate pattern without trailing pipe
        pattern2 = rf'(\| {re.escape(task_id)} \|[^|]*\|[^|]*\|[^|]*\|) 🟡 In Progress \|'
        replacement2 = rf'\1 🟢 Complete |'
        new_content2, n2 = re.subn(pattern2, replacement2, content)
        if n2 > 0:
            content = new_content2
            changed += n2
            print(f"  Marked complete (alt): {task_id}")
        else:
            print(f"  NOT FOUND: {task_id}")

# Update the Progress Summary section
# 4A, 4B, 4E, Epic 5 rows
print(f"\nTotal changes: {changed}")

# Update version and date
content = content.replace("> Last updated: 02/06/26 — v1.7", "> Last updated: 03/06/26 — v1.8")
content = content.replace("**Version:** 1.7", "**Version:** 1.8")
content = content.replace("**Date:** 02/06/26", "**Date:** 03/06/26")

with open(TODO, 'w', encoding='utf-8') as f:
    f.write(content)

print("TODO.md updated.")
