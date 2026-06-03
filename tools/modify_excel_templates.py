#!/usr/bin/env python3
"""
CRA Excel Template Modifier
Adds missing tabs and structure to all Excel templates per audit specs.
"""

import openpyxl
from openpyxl import load_workbook, Workbook
from openpyxl.styles import (PatternFill, Font, Alignment, Border, Side,
                              GradientFill)
from openpyxl.utils import get_column_letter
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Styles ────────────────────────────────────────────────────────────────────

RED_FILL    = PatternFill("solid", fgColor="E31C3D")
NAVY_FILL   = PatternFill("solid", fgColor="1A1F36")
LGRAY_FILL  = PatternFill("solid", fgColor="F2F2F2")
MGRAY_FILL  = PatternFill("solid", fgColor="DDDDDD")
YELLOW_FILL = PatternFill("solid", fgColor="FFF3CD")
BLUE_FILL   = PatternFill("solid", fgColor="E8F4FD")
GREEN_FILL  = PatternFill("solid", fgColor="D4EDDA")
ORANGE_FILL = PatternFill("solid", fgColor="FFF0E0")

WHITE_BOLD  = Font(name="Calibri", bold=True, color="FFFFFF", size=11)
HEADER_FONT = Font(name="Calibri", bold=True, color="FFFFFF", size=10)
BODY_FONT   = Font(name="Calibri", size=10)
BOLD_FONT   = Font(name="Calibri", bold=True, size=10)
RED_FONT    = Font(name="Calibri", bold=True, color="E31C3D", size=11)
TITLE_FONT  = Font(name="Calibri", bold=True, size=14, color="1A1F36")
SMALL_FONT  = Font(name="Calibri", size=9)

WRAP   = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT   = Alignment(horizontal="left", vertical="top", wrap_text=True)

THIN_BORDER = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

def h_row(ws, row, col, text, fill=RED_FILL, font=HEADER_FONT):
    """Write a header cell."""
    c = ws.cell(row=row, column=col, value=text)
    c.fill = fill; c.font = font
    c.alignment = CENTER; c.border = THIN_BORDER
    return c

def b_row(ws, row, col, text, fill=None, font=BODY_FONT, bold=False):
    """Write a body cell."""
    c = ws.cell(row=row, column=col, value=text)
    if fill: c.fill = fill
    c.font = Font(name="Calibri", bold=bold, size=10)
    c.alignment = LEFT; c.border = THIN_BORDER
    return c

def title_row(ws, row, text, colspan, fill=NAVY_FILL):
    """Write a full-width title row."""
    c = ws.cell(row=row, column=1, value=text)
    c.fill = fill; c.font = WHITE_BOLD
    c.alignment = LEFT
    ws.merge_cells(start_row=row, start_column=1,
                   end_row=row, end_column=colspan)

def auto_col_width(ws, min_w=10, max_w=50):
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            if cell.value:
                max_len = max(max_len, len(str(cell.value)))
        ws.column_dimensions[col_letter].width = min(max(max_len + 2, min_w), max_w)

def freeze_header(ws, row=2):
    ws.freeze_panes = ws.cell(row=row, column=1)

# ── Instructions tab builder ──────────────────────────────────────────────────

def add_instructions_tab(wb, purpose, who, when, good_data, mistakes,
                          template_name, tab_name="Instructions",
                          insert_at=0):
    """Add a professional Instructions tab to a workbook."""
    if tab_name in wb.sheetnames:
        return  # already exists

    ws = wb.create_sheet(tab_name, insert_at)
    ws.sheet_view.showGridLines = False
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 70

    r = 1
    # Title
    ws.merge_cells(f'A{r}:B{r}')
    c = ws.cell(r, 1, f"Instructions — {template_name}")
    c.font = Font(name="Calibri", bold=True, size=16, color="E31C3D")
    c.alignment = LEFT
    ws.row_dimensions[r].height = 28
    r += 1

    ws.merge_cells(f'A{r}:B{r}')
    ws.cell(r, 1, "Read this before opening any other tab")
    ws.cell(r, 1).font = Font(name="Calibri", italic=True, size=11, color="666666")
    r += 2

    sections = [
        ("PURPOSE", purpose),
        ("WHO FILLS THIS IN", who),
        ("WHEN TO USE", when),
        ("WHAT 'GOOD DATA' LOOKS LIKE", good_data),
        ("COMMON MISTAKES TO AVOID", mistakes),
    ]
    for label, content in sections:
        c = ws.cell(r, 1, label)
        c.font = BOLD_FONT; c.fill = NAVY_FILL
        ws.cell(r, 1).font = Font(name="Calibri", bold=True, size=10, color="FFFFFF")
        ws.cell(r, 1).fill = NAVY_FILL
        ws.cell(r, 1).alignment = LEFT
        ws.merge_cells(f'A{r}:B{r}')
        ws.row_dimensions[r].height = 18
        r += 1

        if isinstance(content, list):
            for item in content:
                ws.merge_cells(f'A{r}:B{r}')
                c2 = ws.cell(r, 1, f"  • {item}")
                c2.font = BODY_FONT; c2.alignment = LEFT
                ws.row_dimensions[r].height = 15
                r += 1
        else:
            ws.merge_cells(f'A{r}:B{r}')
            c2 = ws.cell(r, 1, f"  {content}")
            c2.font = BODY_FONT; c2.alignment = WRAP
            ws.row_dimensions[r].height = max(15, len(content) // 6 * 4)
            r += 1
        r += 1

    ws.merge_cells(f'A{r}:B{r}')
    ws.cell(r, 1, f"CRA Framework v2.0  |  Rackspace Cloud Solutions Architecture  |  {template_name}")
    ws.cell(r, 1).font = SMALL_FONT
    ws.cell(r, 1).font = Font(name="Calibri", size=8, color="999999", italic=True)


# ── 1. application-scoping-profiling.xlsx ─────────────────────────────────────

def update_app_scoping(path):
    wb = load_workbook(path)

    # Add Instructions tab at position 0
    add_instructions_tab(wb,
        purpose="Capture one row per in-scope application. This data feeds directly into Phase 2 readiness scoring, Phase 3 TCO modelling (VM counts, licensing), and Phase 4 wave planning (criticality, dependencies).",
        who="Lead Architect (initial pass) + Application Owners (validation). Every row must be confirmed by a named application owner before Phase 2 starts.",
        when="Phase 1 Weeks 1–4. App owners must confirm their rows before Phase 2 starts. Do not begin readiness scoring until Business Owner column is confirmed for all Tier-1 applications.",
        good_data=[
            "Every row has a confirmed Business Owner (name + team, not just 'IT')",
            "VM count matches the infrastructure profiling template",
            "Oracle and SQL Server licences are captured (version + licence type)",
            "No TBC in Business Criticality for Tier-1 applications",
            "Scope Confidence = High for all apps before Phase 3 begins",
            "Oracle Practice Flag set for any Oracle RAC or Oracle EE application",
        ],
        mistakes=[
            "Forgetting non-production VMs (dev/test/staging can be 2-3x the prod count)",
            "Not capturing Oracle version — affects licensing path significantly",
            "Missing external integrations — breaks dependency mapping in Phase 2",
            "Treating 'Planned Retirement' apps as out-of-scope before confirming decommission date",
            "Using team names instead of individual names for Business Owner",
            "Leaving OSS Licence Risk Flag blank — Redis/Elasticsearch changes affect TCO",
        ],
        template_name="application-scoping-profiling.xlsx",
        insert_at=0
    )

    # Add Summary tab if missing
    if "Summary" not in wb.sheetnames:
        ws = wb.create_sheet("Summary")
        ws.sheet_view.showGridLines = False
        ws.column_dimensions['A'].width = 35
        ws.column_dimensions['B'].width = 20

        title_row(ws, 1, "Application Inventory — Summary Dashboard", 2)
        ws.row_dimensions[1].height = 22

        rows = [
            ("Total Applications in Scope", '=COUNTA(\'Customer Template\'!A:A)-1'),
            ("Applications with Confirmed Business Owner", ""),
            ("Applications flagged as Tier 1 (Critical)", ""),
            ("Applications with Oracle Practice Flag = Yes", ""),
            ("Applications with OSS Licence Risk Flag", ""),
            ("Applications with Scope Confidence = High", ""),
            ("Applications with Scope Confidence = Low", ""),
            ("Applications flagged for Planned Retirement", ""),
        ]
        for i, (label, val) in enumerate(rows, start=3):
            ws.cell(i, 1, label).font = BODY_FONT
            ws.cell(i, 1).fill = LGRAY_FILL if i % 2 == 0 else PatternFill()
            ws.cell(i, 2, val).font = BOLD_FONT
            ws.cell(i, 2).alignment = CENTER

        ws.cell(12, 1, "Update this summary manually or add COUNTIF formulas referencing the 'Customer Template' tab once column positions are confirmed.").font = Font(name="Calibri", italic=True, size=9, color="888888")
        ws.merge_cells('A12:B12')

    wb.save(path)
    print(f"  Updated: {os.path.relpath(path, BASE)}")


# ── 2. infrastructure-profiling.xlsx ──────────────────────────────────────────

def update_infra_profiling(path):
    wb = load_workbook(path)

    add_instructions_tab(wb,
        purpose="One row per server/VM. This is the authoritative inventory used to populate the TCO evaluation templates. It is the primary output of the discovery tooling (Azure Migrate, GCP Migration Center, AWS ADS).",
        who="Platform Architect (lead). Data is imported from discovery tooling exports (Azure Migrate portal, Migration Center dashboard, or RVTools VMware export). Application owners validate the application-to-VM mapping.",
        when="Phase 1 Weeks 1–7. The Data Quality Summary tab must show >=90% VM coverage and >=14 days of clean P95 utilisation data before GATE 1 is cleared and Phase 3 can begin.",
        good_data=[
            ">=90% of in-scope VMs have P95 CPU and RAM utilisation data",
            "Utilisation data collection period is >=14 days continuous",
            "Every VM has an assigned Application ID cross-referencing the app inventory",
            "OS Version captured for all VMs (critical for EoL OS flag)",
            "Storage (GB) captured per VM — not just VM count",
            "EoL OS Flag set for any Windows Server 2012 or RHEL 6 instances",
        ],
        mistakes=[
            "Using P50 (average) utilisation instead of P95 — underestimates right-sized instance size",
            "Not capturing non-production VMs — they must appear even if excluded from primary TCO",
            "Missing storage data — storage is often 15-20% of total cloud cost",
            "Incomplete OS Version — blocks EoL OS detection and ESU cost modelling",
            "Not validating RVTools export against discovery tool output — shadow VMs are common",
        ],
        template_name="infrastructure-profiling.xlsx",
        insert_at=0
    )

    # Add Data Quality Summary tab if missing
    if "Data Quality Summary" not in wb.sheetnames:
        ws = wb.create_sheet("Data Quality Summary")
        ws.sheet_view.showGridLines = False
        ws.column_dimensions['A'].width = 40
        ws.column_dimensions['B'].width = 18
        ws.column_dimensions['C'].width = 25

        title_row(ws, 1, "GATE 1 Data Quality Checklist — Phase 3 cannot begin until all rows are GREEN", 3, RED_FILL)
        ws.row_dimensions[1].height = 22

        h_row(ws, 2, 1, "Quality Check", NAVY_FILL, HEADER_FONT)
        h_row(ws, 2, 2, "Current Status", NAVY_FILL, HEADER_FONT)
        h_row(ws, 2, 3, "Required Threshold", NAVY_FILL, HEADER_FONT)

        checks = [
            ("VM coverage: % of in-scope VMs reporting", "[Enter %]", ">=90%"),
            ("Utilisation data collection period", "[Enter days]", ">=14 days continuous clean data"),
            ("CPU P95 data: % of VMs with P95 values", "[Enter %]", ">=90% of VMs"),
            ("RAM P95 data: % of VMs with P95 values", "[Enter %]", ">=90% of VMs"),
            ("Storage I/O: VMs flagged as I/O-sensitive", "[Enter count]", "100% of DB/high-IOPS VMs"),
            ("OS Version captured: % of VMs", "[Enter %]", "100%"),
            ("Application ID assigned: % of VMs", "[Enter %]", ">=95%"),
            ("EoL OS Flag reviewed", "[ ] Complete", "All Windows 2012, RHEL 6 flagged"),
            ("RVTools cross-validation complete", "[ ] Complete", "Discrepancies resolved"),
        ]
        fills = [LGRAY_FILL, PatternFill()]
        for i, (check, status, threshold) in enumerate(checks, start=3):
            f = fills[i % 2]
            ws.cell(i, 1, check).font = BODY_FONT; ws.cell(i, 1).fill = f; ws.cell(i, 1).border = THIN_BORDER; ws.cell(i, 1).alignment = LEFT
            ws.cell(i, 2, status).font = BODY_FONT; ws.cell(i, 2).fill = YELLOW_FILL; ws.cell(i, 2).border = THIN_BORDER; ws.cell(i, 2).alignment = CENTER
            ws.cell(i, 3, threshold).font = BODY_FONT; ws.cell(i, 3).fill = f; ws.cell(i, 3).border = THIN_BORDER; ws.cell(i, 3).alignment = LEFT

        ws.row_dimensions[12].height = 25
        ws.cell(12, 1, "GATE 1 STATUS:").font = Font(name="Calibri", bold=True, size=12, color="E31C3D")
        ws.cell(12, 2, "[ ] OPEN — update all rows above before clearing").font = Font(name="Calibri", bold=True, size=10)
        ws.merge_cells('B12:C12')

    wb.save(path)
    print(f"  Updated: {os.path.relpath(path, BASE)}")


# ── 3. dependency-mapping.xlsx ────────────────────────────────────────────────

def update_dependency_mapping(path):
    wb = load_workbook(path)

    add_instructions_tab(wb,
        purpose="Map application-to-application and application-to-infrastructure dependencies. This is used to identify dependency clusters in Phase 2 and sequence migration waves in Phase 4. Applications with tightly-coupled dependencies cannot be separated across different migration waves.",
        who="Lead Architect (facilitation) + Application Owners (workshop participants). The dependency data comes from two sources: (1) automated discovery tooling (Azure Migrate network dependencies, AWS ADS, GCP Migration Center), and (2) workshops with application owners.",
        when="Phase 1 Weeks 2–6. Workshops with application owners should be scheduled in Phase 1 Week 2 while discovery tooling is still collecting data in the background. Do not wait for Phase 1 to complete.",
        good_data=[
            "Every Tier-1 application has its dependencies validated by its application owner",
            "Dependency Cluster IDs assigned to all tightly-coupled groups",
            "External dependencies (SaaS, APIs, third-party services) are documented",
            "Bi-directional dependencies captured (upstream AND downstream)",
            "Latency-sensitive dependencies flagged (cannot tolerate WAN latency post-migration)",
        ],
        mistakes=[
            "Relying on automated tools only — they miss application-level logical dependencies",
            "Not capturing database-level dependencies (shared SQL instances across apps)",
            "Ignoring SaaS dependencies — a migrated app that calls an on-prem SaaS proxy breaks",
            "Not clustering tightly-coupled apps — splitting them across waves causes migration failures",
        ],
        template_name="dependency-mapping.xlsx",
        insert_at=0
    )

    # Add Dependency Heat Map tab if missing
    if "Dependency Heat Map" not in wb.sheetnames:
        ws = wb.create_sheet("Dependency Heat Map")
        ws.sheet_view.showGridLines = False

        title_row(ws, 1, "Dependency Heat Map — Applications by Cluster and Coupling Level", 5, NAVY_FILL)

        headers = ["Cluster ID", "Application Name", "App Tier", "Coupling Level", "Notes"]
        fills_map = {"Tightly Coupled": RED_FILL, "Loosely Coupled": ORANGE_FILL, "Independent": GREEN_FILL}
        for ci, h in enumerate(headers, 1):
            h_row(ws, 2, ci, h)

        sample_rows = [
            ("C001", "[App Name - from inventory]", "Tier 1", "Tightly Coupled", "Cannot migrate independently - shares DB with C001-B"),
            ("C001", "[App Name - from inventory]", "Tier 2", "Tightly Coupled", "C001 cluster must move together in same wave"),
            ("C002", "[App Name - from inventory]", "Tier 3", "Loosely Coupled", "Soft dependency - can migrate in adjacent wave"),
            ("NONE", "[App Name - from inventory]", "Tier 3", "Independent", "No dependencies - Wave 0 PoC candidate"),
        ]
        col_widths = [12, 35, 12, 22, 50]
        for ci, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(ci)].width = w

        for ri, row in enumerate(sample_rows, start=3):
            f = fills_map.get(row[3], LGRAY_FILL)
            for ci, val in enumerate(row, 1):
                c = ws.cell(ri, ci, val)
                c.font = BODY_FONT; c.fill = LGRAY_FILL if ri % 2 == 0 else PatternFill()
                c.border = THIN_BORDER; c.alignment = LEFT
            ws.cell(ri, 4).fill = f

        ws.row_dimensions[7].height = 20
        ws.cell(7, 1, "Legend:").font = BOLD_FONT
        ws.cell(7, 2, "Tightly Coupled = must migrate in same wave").fill = RED_FILL
        ws.cell(7, 2).font = Font(name="Calibri", bold=True, size=10, color="FFFFFF")
        ws.cell(7, 3, "Loosely Coupled = adjacent wave").fill = ORANGE_FILL
        ws.cell(7, 3).font = Font(name="Calibri", size=10)
        ws.cell(7, 4, "Independent = any wave").fill = GREEN_FILL
        ws.cell(7, 4).font = Font(name="Calibri", size=10)

    wb.save(path)
    print(f"  Updated: {os.path.relpath(path, BASE)}")


# ── 4. governance-foundations-alignment.xlsx ──────────────────────────────────

def update_governance_foundations(path):
    wb = load_workbook(path)

    # Add Gap Register tab if missing
    if "Gap Register" not in wb.sheetnames:
        ws = wb.create_sheet("Gap Register")
        ws.sheet_view.showGridLines = False

        title_row(ws, 1, "Cloud Governance Gap Register — Gaps to Close Before or During Part 2", 7, NAVY_FILL)

        headers = ["Gap ID", "Domain", "Gap Description", "Business Risk if Not Closed",
                   "Recommended Action", "Priority", "Part 2 Dependency?"]
        for ci, h in enumerate(headers, 1):
            h_row(ws, 2, ci, h)

        sample_gaps = [
            ("G001", "Identity & Access Management", "No RBAC model defined for cloud subscriptions", "Uncontrolled access to cloud resources; audit failure", "Design Azure RBAC / AWS IAM policy framework in Part 2 landing zone", "Critical", "Yes"),
            ("G002", "Cost Management", "No FinOps process — cloud costs will not be allocated by BU", "Cloud cost overrun with no accountability; finance unable to attribute spend", "Implement tagging strategy and cost allocation model in landing zone", "High", "Yes"),
            ("G003", "Change Management", "CAB lead time 10+ business days — blocks Phase 1 discovery", "Phase 1 delayed if firewall change not submitted on Day 1", "Submit CAB pre-engagement; target dedicated cloud change category", "Critical", "No (Phase 1 action)"),
            ("G004", "Monitoring & Observability", "No cloud-native monitoring capability — Dynatrace on-prem only", "Cloud workloads will not be monitored post-migration", "Deploy Azure Monitor / AWS CloudWatch / GCP Cloud Operations in Part 2", "High", "Yes"),
        ]
        col_widths = [8, 20, 40, 45, 45, 12, 18]
        for ci, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(ci)].width = w

        for ri, row in enumerate(sample_gaps, start=3):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                c = ws.cell(ri, ci, val)
                c.font = BODY_FONT; c.fill = f
                c.border = THIN_BORDER; c.alignment = WRAP
            # Colour-code Priority
            priority_fills = {"Critical": RED_FILL, "High": ORANGE_FILL, "Medium": YELLOW_FILL, "Low": GREEN_FILL}
            ws.cell(ri, 6).fill = priority_fills.get(row[5], f)
            if row[5] == "Critical":
                ws.cell(ri, 6).font = Font(name="Calibri", bold=True, size=10, color="FFFFFF")

        freeze_header(ws)

    # Add Summary Dashboard tab if missing
    if "Summary Dashboard" not in wb.sheetnames:
        ws = wb.create_sheet("Summary Dashboard")
        ws.sheet_view.showGridLines = False
        ws.column_dimensions['A'].width = 30
        ws.column_dimensions['B'].width = 20
        ws.column_dimensions['C'].width = 20
        ws.column_dimensions['D'].width = 30

        title_row(ws, 1, "Cloud Governance Maturity — Executive Summary Dashboard", 4, NAVY_FILL)

        h_row(ws, 2, 1, "Governance Domain")
        h_row(ws, 2, 2, "Current Maturity (1-5)")
        h_row(ws, 2, 3, "Target Maturity (1-5)")
        h_row(ws, 2, 4, "Status")

        domains = [
            "Identity & Access Management",
            "Security & Compliance",
            "Change Management",
            "Monitoring & Observability",
            "Cost Management (FinOps)",
            "Operational Readiness",
        ]
        status_map = {
            "1": ("Initial", RED_FILL, "FFFFFF"),
            "2": ("Developing", ORANGE_FILL, "000000"),
            "3": ("Defined", YELLOW_FILL, "000000"),
            "4": ("Managed", GREEN_FILL, "000000"),
            "5": ("Optimising", PatternFill("solid", fgColor="0070C0"), "FFFFFF"),
        }
        for i, domain in enumerate(domains, start=3):
            f = LGRAY_FILL if i % 2 == 0 else PatternFill()
            ws.cell(i, 1, domain).font = BODY_FONT; ws.cell(i, 1).fill = f; ws.cell(i, 1).border = THIN_BORDER
            ws.cell(i, 2, "[Score from assessment tab]").font = Font(name="Calibri", size=10, color="888888")
            ws.cell(i, 2).fill = YELLOW_FILL; ws.cell(i, 2).border = THIN_BORDER; ws.cell(i, 2).alignment = CENTER
            ws.cell(i, 3, "[Target score]").font = Font(name="Calibri", size=10, color="888888")
            ws.cell(i, 3).fill = f; ws.cell(i, 3).border = THIN_BORDER; ws.cell(i, 3).alignment = CENTER
            ws.cell(i, 4, "[ ] Review maturity tabs and enter scores").font = Font(name="Calibri", italic=True, size=9, color="888888")
            ws.cell(i, 4).fill = f; ws.cell(i, 4).border = THIN_BORDER

        ws.cell(10, 1, "Overall Assessment Note:").font = BOLD_FONT
        ws.cell(11, 1, "[Enter overall governance readiness narrative for this customer. Reference the Gap Register for remediation roadmap.]")
        ws.cell(11, 1).font = Font(name="Calibri", italic=True, size=10)
        ws.merge_cells('A11:D11')
        ws.row_dimensions[11].height = 40
        ws.cell(11, 1).alignment = WRAP

    # Add CAF / WAF / GAF Alignment tab if missing
    if "CAF-WAF-GAF Alignment" not in wb.sheetnames:
        ws = wb.create_sheet("CAF-WAF-GAF Alignment")
        ws.sheet_view.showGridLines = False

        title_row(ws, 1, "Framework Alignment — CAF / AWS WAF / Google Cloud Architecture Framework", 5, NAVY_FILL)

        headers = ["Governance Domain", "CAF Stage / Pillar", "AWS WAF Pillar", "GCAF Pillar", "CRA Output"]
        for ci, h in enumerate(headers, 1):
            h_row(ws, 2, ci, h)

        data = [
            ("Identity & Access Management", "CAF: Ready — Identity Management", "Security (IAM)", "Security, Privacy, Compliance", "Governance Maturity score + Gap Register → informs landing zone IAM design"),
            ("Security & Compliance", "CAF: Ready — Security Baseline", "Security", "Security, Privacy, Compliance", "Compliance requirements captured → cloud region constraints in TCO"),
            ("Change Management", "CAF: Plan — Platform Automation", "Operational Excellence", "Operational Excellence", "CAB lead time documented → Phase 1 risk register item"),
            ("Monitoring & Observability", "CAF: Manage — Management Baseline", "Operational Excellence", "Operational Excellence", "Monitoring gap → Part 2 landing zone tooling requirement"),
            ("Cost Management (FinOps)", "CAF: Govern — Cost Management", "Cost Optimisation", "Cost Optimisation", "FinOps maturity → TCO Layer (g) partner credits visibility"),
            ("Operational Readiness", "CAF: Manage", "Reliability", "Reliability", "RTO/RPO requirements → Business Criticality scores in readiness template"),
        ]
        col_widths = [25, 30, 25, 30, 50]
        for ci, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(ci)].width = w

        for ri, row in enumerate(data, start=3):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                c = ws.cell(ri, ci, val)
                c.font = BODY_FONT; c.fill = f
                c.border = THIN_BORDER; c.alignment = WRAP
            ws.row_dimensions[ri].height = 30

        freeze_header(ws)

    wb.save(path)
    print(f"  Updated: {os.path.relpath(path, BASE)}")


# ── 5. risk-assessment.xlsx ───────────────────────────────────────────────────

def update_risk_assessment(path):
    wb = load_workbook(path)

    add_instructions_tab(wb,
        purpose="Document and score all identified risks for the CRA engagement. This register is maintained throughout the engagement and is a key deliverable in the Phase 3 Assessment Report and Part 2 Entry Point. All 11 risk categories must be reviewed for every engagement.",
        who="Lead Architect (maintains). Delivery Manager (reviews weekly). Customer IT Director (reviews at Phase 3 playback). Alliance Manager reviews Commercial category risks.",
        when="Phase 2 onwards. Pre-populate all 11 default risk categories at Phase 1 kickoff. Update likelihood and impact scores as more information becomes available. Review and refresh before each phase gate review.",
        good_data=[
            "All 11 risk categories have at least one row (even if Low likelihood)",
            "Every risk has a named mitigation owner",
            "Oracle licensing and scope variance risks are scored accurately",
            "Risk scores (Likelihood x Impact) are current — not from initial assessment",
            "All Critical and High risks have a documented mitigation plan",
        ],
        mistakes=[
            "Leaving risk register empty until Phase 3 — risks identified early can be mitigated early",
            "Under-scoring scope variance risk — it is High Likelihood on most engagements",
            "Not including Commercial category risks (missed partner registration = loss of AMM/MAP funding)",
            "Marking risks as 'Closed' without verifying the mitigation was actually implemented",
        ],
        template_name="risk-assessment.xlsx",
        insert_at=0
    )

    # Check if the existing Risk Assessment tab needs enhancement
    ws = wb["Risk Assessment"]

    # Add a Risk Summary tab
    if "Risk Summary" not in wb.sheetnames:
        ws2 = wb.create_sheet("Risk Summary")
        ws2.sheet_view.showGridLines = False
        ws2.column_dimensions['A'].width = 22
        ws2.column_dimensions['B'].width = 15
        ws2.column_dimensions['C'].width = 15
        ws2.column_dimensions['D'].width = 15

        title_row(ws2, 1, "Risk Summary Dashboard — CRA Engagement Risk Status", 4, NAVY_FILL)

        h_row(ws2, 2, 1, "Risk Category")
        h_row(ws2, 2, 2, "Red Risks (>=9)")
        h_row(ws2, 2, 3, "Amber Risks (6-8)")
        h_row(ws2, 2, 4, "Green Risks (<=5)")

        categories = ["Scope", "Data Quality", "Dependency", "Licensing", "End-of-Life OS",
                      "Regulatory", "Schedule", "Resource", "Commercial", "Stakeholder", "Third-Party"]
        for i, cat in enumerate(categories, start=3):
            f = LGRAY_FILL if i % 2 == 0 else PatternFill()
            ws2.cell(i, 1, cat).font = BODY_FONT; ws2.cell(i, 1).fill = f; ws2.cell(i, 1).border = THIN_BORDER
            for ci in [2, 3, 4]:
                ws2.cell(i, ci, 0).font = BODY_FONT; ws2.cell(i, ci).fill = f; ws2.cell(i, ci).border = THIN_BORDER; ws2.cell(i, ci).alignment = CENTER

        ws2.cell(15, 1, "Note: Update counts manually from the Risk Assessment tab, or add COUNTIFS formulas once row structure is confirmed.").font = Font(name="Calibri", italic=True, size=9, color="888888")
        ws2.merge_cells('A15:D15')

    # Add pre-populated default risks to the Risk Assessment tab
    # Check if it looks mostly empty (fewer than 5 data rows)
    data_rows = sum(1 for row in ws.iter_rows(min_row=2, values_only=True) if any(row))
    if data_rows < 5:
        # Find the last row with data or start from row 2
        next_row = ws.max_row + 1
        if next_row < 3:
            next_row = 3

        # Add headers if row 1 is empty
        if not ws.cell(1, 1).value:
            headers = ["Risk ID", "Category", "Risk Description", "Likelihood (1-5)",
                       "Impact (1-5)", "Risk Score", "Status", "Mitigation", "Owner", "Due Date"]
            for ci, h in enumerate(headers, 1):
                h_row(ws, 1, ci, h)
            ws.column_dimensions['A'].width = 8
            ws.column_dimensions['B'].width = 18
            ws.column_dimensions['C'].width = 45
            ws.column_dimensions['D'].width = 16
            ws.column_dimensions['E'].width = 16
            ws.column_dimensions['F'].width = 12
            ws.column_dimensions['G'].width = 12
            ws.column_dimensions['H'].width = 45
            ws.column_dimensions['I'].width = 18
            ws.column_dimensions['J'].width = 14
            next_row = 2

        default_risks = [
            ("R001", "Scope", "Estate larger than scoped in SoW — VM count underestimated", 4, 4, "=D{r}*E{r}", "Open", "Add scope confidence column to app inventory; validate against RVTools export", "Lead Architect", "Phase 1 Wk 4"),
            ("R002", "Data Quality", "Utilisation data window < 14 days clean — TCO accuracy compromised", 3, 5, "=D{r}*E{r}", "Open", "Gate 1: enforce >=14 day clean data window before Phase 3; document in writing if customer overrides", "Platform Architect", "Phase 1 Wk 7"),
            ("R003", "Dependency", "Undocumented application dependencies — block wave sequencing", 3, 4, "=D{r}*E{r}", "Open", "Schedule dependency workshops with app owners in Phase 1 Week 2", "Lead Architect", "Phase 2"),
            ("R004", "Licensing", "Oracle EE licence not cloud-portable — requires specialist review", 3, 5, "=D{r}*E{r}", "Open", "Engage Oracle Practice Lead at Phase 1 Week 2 if Oracle RAC or EE found", "Oracle Practice Lead", "Phase 1 Wk 2"),
            ("R005", "End-of-Life OS", "Windows Server 2012 / RHEL 6 — ESU commitment required", 4, 4, "=D{r}*E{r}", "Open", "Flag all EoL OS in infrastructure-profiling.xlsx; model ESU cost in Phase 3 TCO Licensing Overlay", "Platform Architect", "Phase 3"),
            ("R006", "Regulatory", "Data sovereignty constraint blocks primary cloud region", 2, 5, "=D{r}*E{r}", "Open", "Confirm regulatory requirements at scoping workshop; validate cloud region eligibility in Phase 2", "Lead Architect", "Phase 2"),
            ("R007", "Schedule", "CAB approval lead time delays Phase 1 discovery by >=2 weeks", 3, 3, "=D{r}*E{r}", "Open", "Submit firewall CAB request on Phase 1 Day 1 — do not wait for appliance deployment", "Delivery Manager", "Phase 1 Day 1"),
            ("R008", "Resource", "Customer IT resource unavailable for Phase 2 workshops", 3, 3, "=D{r}*E{r}", "Open", "Confirm workshop dates and IT Director availability at Phase 1 kickoff", "Delivery Manager", "Phase 1 Wk 1"),
            ("R009", "Commercial", "Partner deal registration missed before Part 2 SOW — AMM/MAP funding lost", 2, 4, "=D{r}*E{r}", "Open", "Alliance Manager pre-registers opportunity on Phase 1 Day 1; confirm before Part 2 SOW", "Alliance Manager", "Phase 1 Day 1"),
            ("R010", "Stakeholder", "CTO changes during assessment — recommendation re-presented", 2, 3, "=D{r}*E{r}", "Open", "Document stakeholder map at Phase 1; confirm presentation audience at Phase 3 playback scheduling", "Lead Architect", "Phase 3"),
            ("R011", "Third-Party", "Oracle Practice Lead availability delays Phase 2 Oracle analysis", 3, 3, "=D{r}*E{r}", "Open", "Engage Oracle Practice Lead at Phase 1 Week 1 if Oracle detected — not at Phase 3", "Delivery Manager", "Phase 1 Wk 1"),
        ]

        score_fills = {}  # will be applied post-write

        for i, risk in enumerate(default_risks):
            r = next_row + i
            f = LGRAY_FILL if r % 2 == 0 else PatternFill()
            ws.cell(r, 1, risk[0]).font = BODY_FONT; ws.cell(r, 1).fill = f; ws.cell(r, 1).border = THIN_BORDER
            ws.cell(r, 2, risk[1]).font = BODY_FONT; ws.cell(r, 2).fill = f; ws.cell(r, 2).border = THIN_BORDER
            ws.cell(r, 3, risk[2]).font = BODY_FONT; ws.cell(r, 3).fill = f; ws.cell(r, 3).border = THIN_BORDER; ws.cell(r, 3).alignment = WRAP
            ws.cell(r, 4, risk[3]).font = BOLD_FONT; ws.cell(r, 4).fill = f; ws.cell(r, 4).border = THIN_BORDER; ws.cell(r, 4).alignment = CENTER
            ws.cell(r, 5, risk[4]).font = BOLD_FONT; ws.cell(r, 5).fill = f; ws.cell(r, 5).border = THIN_BORDER; ws.cell(r, 5).alignment = CENTER
            score = risk[3] * risk[4]
            score_fill = RED_FILL if score >= 9 else (ORANGE_FILL if score >= 6 else GREEN_FILL)
            ws.cell(r, 6, score).font = Font(name="Calibri", bold=True, size=10); ws.cell(r, 6).fill = score_fill; ws.cell(r, 6).border = THIN_BORDER; ws.cell(r, 6).alignment = CENTER
            ws.cell(r, 7, risk[6]).font = BODY_FONT; ws.cell(r, 7).fill = f; ws.cell(r, 7).border = THIN_BORDER; ws.cell(r, 7).alignment = CENTER
            ws.cell(r, 8, risk[7]).font = BODY_FONT; ws.cell(r, 8).fill = f; ws.cell(r, 8).border = THIN_BORDER; ws.cell(r, 8).alignment = WRAP
            ws.cell(r, 9, risk[8]).font = BODY_FONT; ws.cell(r, 9).fill = f; ws.cell(r, 9).border = THIN_BORDER
            ws.cell(r, 10, risk[9]).font = BODY_FONT; ws.cell(r, 10).fill = f; ws.cell(r, 10).border = THIN_BORDER
            ws.row_dimensions[r].height = 30

        freeze_header(ws)

    wb.save(path)
    print(f"  Updated: {os.path.relpath(path, BASE)}")


# ── 6. azure-evaluation.xlsx ──────────────────────────────────────────────────

def update_azure_eval(path):
    wb = load_workbook(path)

    add_instructions_tab(wb,
        purpose="Model Azure TCO across multiple pricing scenarios: Like-for-Like PAYG, Like-for-Like 3yr RI, Optimised 3yr RI, and Optimised 3yr RI + AHB. The AHB (Azure Hybrid Benefit) overlay is mandatory for any estate with Windows Server or SQL Server licences with active Software Assurance.",
        who="Platform Architect (Azure). Input data comes from the infrastructure-profiling.xlsx template (VM specs + P95 utilisation). AHB eligibility must be confirmed with the customer's Microsoft licensing contact before the AHB scenario is presented as a committed saving.",
        when="Phase 3 Weeks 11–13. Pricing must be validated against azure.microsoft.com/pricing/calculator at the start of Phase 3 — not using pricing captured more than 90 days ago. Document the pricing source date in the Summary tab header.",
        good_data=[
            "VM SKUs mapped from actual P95 utilisation data — not rounded estimates",
            "AHB eligibility confirmed by customer (active Software Assurance on Windows/SQL Server)",
            "Pricing validated against Azure Calculator this week (source date in Summary tab)",
            "Both PAYG and 3yr RI scenarios present — CFO will ask about both",
            "UK South primary + DR region both modelled",
            "Storage costs in dedicated Storage tab — not rolled into VM cost",
        ],
        mistakes=[
            "Using P50 (average) instead of P95 for right-sizing — underestimates instance size",
            "Presenting AHB scenario without confirming SA status — can be materially wrong",
            "Using pricing from a prior engagement — Azure prices change quarterly",
            "Not modelling ESU saving for Windows Server 2012 / SQL Server 2012 (free in Azure)",
            "Forgetting to include storage costs — often 15-20% of total cloud spend",
        ],
        template_name="azure-evaluation.xlsx",
        insert_at=0
    )

    # Add AHB Overlay tab if missing
    if "AHB Overlay" not in wb.sheetnames:
        ws = wb.create_sheet("AHB Overlay")
        ws.sheet_view.showGridLines = False

        title_row(ws, 1, "Azure Hybrid Benefit (AHB) Overlay — Requires Active Software Assurance Confirmation", 6, NAVY_FILL)
        ws.row_dimensions[1].height = 22

        # AHB explanation
        ws.merge_cells('A2:F2')
        ws.cell(2, 1, "AHB allows organisations with active SA on Windows Server or SQL Server licences to use those licences in Azure at no additional licence cost. SA status must be confirmed by the customer before including this saving in the TCO.")
        ws.cell(2, 1).font = Font(name="Calibri", italic=True, size=10)
        ws.cell(2, 1).fill = BLUE_FILL
        ws.cell(2, 1).alignment = WRAP
        ws.row_dimensions[2].height = 35

        headers = ["VM Name", "OS", "vCPUs", "SQL Server Licence?", "AHB Applicable?",
                   "Monthly Saving (AHB vs PAYG)", "Notes"]
        for ci, h in enumerate(headers, 1):
            h_row(ws, 3, ci, h)

        col_widths = [30, 18, 10, 20, 18, 28, 40]
        for ci, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(ci)].width = w

        # EoL OS ESU section
        ws.merge_cells('A12:G12')
        title_row(ws, 12, "Extended Security Updates (ESU) — Windows Server 2012 / SQL Server 2012 (FREE in Azure)", 7, RED_FILL)

        ws.merge_cells('A13:G13')
        ws.cell(13, 1, "Windows Server 2012/R2 and SQL Server 2012/2014 ESU is FREE when running in Azure. On AWS or GCP, the customer must purchase ESU from Microsoft (typically £100–£200 per server per year). This is a LEGITIMATE Azure cost advantage that must appear in the TCO.")
        ws.cell(13, 1).font = Font(name="Calibri", bold=True, size=10)
        ws.cell(13, 1).fill = YELLOW_FILL
        ws.cell(13, 1).alignment = WRAP
        ws.row_dimensions[13].height = 45

        esu_headers = ["EoL OS / Product", "Count in Estate", "Azure ESU Cost (3yr)", "AWS/GCP ESU Cost (3yr)", "Azure Saving vs AWS/GCP"]
        for ci, h in enumerate(esu_headers, 1):
            h_row(ws, 14, ci, h)

        esu_data = [
            ("Windows Server 2012/R2", "[Count from infrastructure-profiling]", "£0 (free in Azure)", "~£300–£600 per server (3yr)", "=C15-D15 per server"),
            ("SQL Server 2012", "[Count from infrastructure-profiling]", "£0 (free in Azure)", "~£400–£800 per server (3yr)", "=C16-D16 per server"),
            ("SQL Server 2014", "[Count]", "£0 (free in Azure)", "~£400–£800 per server (3yr)", "=C17-D17 per server"),
        ]
        for ri, row in enumerate(esu_data, start=15):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                c = ws.cell(ri, ci, val)
                c.font = BODY_FONT; c.fill = f; c.border = THIN_BORDER; c.alignment = WRAP

        ws.cell(19, 1, "TOTAL ESU SAVING (Azure vs AWS/GCP):").font = BOLD_FONT
        ws.cell(19, 1).fill = NAVY_FILL
        ws.cell(19, 1).font = Font(name="Calibri", bold=True, size=10, color="FFFFFF")
        ws.cell(19, 2, "[Calculate: sum of ESU savings across all EoL OS instances x 3 years]").font = BODY_FONT
        ws.cell(19, 2).fill = YELLOW_FILL

        freeze_header(ws, 4)

    wb.save(path)
    print(f"  Updated: {os.path.relpath(path, BASE)}")


# ── 7. aws-evaluation.xlsx ────────────────────────────────────────────────────

def update_aws_eval(path):
    wb = load_workbook(path)

    add_instructions_tab(wb,
        purpose="Model AWS TCO across three pricing scenarios: On-Demand, 3yr Reserved Instance (All Upfront), and Compute Savings Plans (3yr). All three must be present so the customer's CFO can make an informed commitment decision. Cross-validate against AWS Migration Evaluator output.",
        who="Platform Architect (AWS). Input from infrastructure-profiling.xlsx. Cross-validate the Optimised pricing against AWS Migration Evaluator output (if ADS was deployed during Phase 1). For Oracle workloads, engage the Oracle Practice Lead before finalising AWS TCO.",
        when="Phase 3 Weeks 11–13. Validate all pricing against aws.amazon.com/ec2/pricing at the start of Phase 3. Document the pricing source date in the Summary tab header.",
        good_data=[
            "All three pricing models present (On-Demand, 3yr RI, 3yr Savings Plans)",
            "Instance families use current generation (m6i/m7i, not m5)",
            "eu-west-2 (London) primary + eu-central-1 (Frankfurt) DR region both modelled",
            "Oracle workloads reviewed by Oracle Practice Lead (dedicated host cost modelled)",
            "Savings Plans cross-validated against AWS Migration Evaluator output",
        ],
        mistakes=[
            "Using previous-generation instance types (m5 instead of m6i) — inflates cost",
            "Not including All-Upfront RI pricing — this is often the most competitive number",
            "Forgetting dedicated host cost for Oracle RAC — can be 3-5x standard EC2 cost",
            "Using a single region estimate — customers always ask about DR region cost",
        ],
        template_name="aws-evaluation.xlsx",
        insert_at=0
    )

    # Add Savings Plans tab if missing
    if "Savings Plans" not in wb.sheetnames:
        ws = wb.create_sheet("Savings Plans")
        ws.sheet_view.showGridLines = False

        title_row(ws, 1, "AWS Compute Savings Plans (3-Year) — More Flexible Than Reserved Instances", 5, NAVY_FILL)
        ws.row_dimensions[1].height = 22

        ws.merge_cells('A2:E2')
        ws.cell(2, 1, "Compute Savings Plans provide the same ~40-60% saving as 3yr RI but are not tied to a specific instance type or region. They apply to EC2, Fargate, and Lambda. This makes them more appropriate for customers who want to reserve compute spend without locking to specific instance families.")
        ws.cell(2, 1).font = Font(name="Calibri", italic=True, size=10)
        ws.cell(2, 1).fill = BLUE_FILL
        ws.cell(2, 1).alignment = WRAP
        ws.row_dimensions[2].height = 45

        headers = ["VM / Workload Name", "Instance Type (Optimised)", "Region",
                   "On-Demand Monthly", "3yr Savings Plan Monthly", "Saving vs On-Demand"]
        for ci, h in enumerate(headers, 1):
            h_row(ws, 3, ci, h)

        col_widths = [30, 22, 18, 22, 25, 22]
        for ci, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(ci)].width = w

        # Key comparison table
        ws.merge_cells('A8:F8')
        title_row(ws, 8, "Commitment Model Comparison — Present All Three to the Customer", 6, NAVY_FILL)
        h_row(ws, 9, 1, "Pricing Model")
        h_row(ws, 9, 2, "Discount vs On-Demand")
        h_row(ws, 9, 3, "Flexibility")
        h_row(ws, 9, 4, "Applies To")
        h_row(ws, 9, 5, "Best For")
        h_row(ws, 9, 6, "3yr Total Cost")

        comparison = [
            ("On-Demand", "None (baseline)", "Maximum — no commitment", "EC2 instances", "Proof of Concept / variable workloads", "[=sum of On-Demand tab]"),
            ("3yr Reserved Instance (All Upfront)", "~55-62%", "Low — specific instance type/region/OS", "EC2 specific instances", "Stable, predictable workloads with known specs", "[=sum of RI tab]"),
            ("3yr Compute Savings Plans", "~52-58%", "Medium — flexible across EC2/Fargate/Lambda", "EC2 + Fargate + Lambda", "Flexible cloud-first estates; container workloads", "[=sum of this tab]"),
        ]
        for ri, row in enumerate(comparison, start=10):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                c = ws.cell(ri, ci, val)
                c.font = BODY_FONT; c.fill = f; c.border = THIN_BORDER; c.alignment = WRAP
            ws.row_dimensions[ri].height = 35

        freeze_header(ws, 4)

    # Add RI All-Upfront tab if missing
    if "3yr RI All-Upfront" not in wb.sheetnames:
        ws = wb.create_sheet("3yr RI All-Upfront")
        ws.sheet_view.showGridLines = False

        title_row(ws, 1, "AWS 3-Year Reserved Instance — All Upfront (Lowest Effective Rate)", 6, NAVY_FILL)

        ws.merge_cells('A2:F2')
        ws.cell(2, 1, "All-Upfront 3yr RI provides the highest discount (55-62% vs On-Demand) but requires the full 3yr cost paid upfront. This is the board-level commitment scenario — the number that demonstrates maximum cloud cost savings when the customer is confident in their workload stability.")
        ws.cell(2, 1).font = Font(name="Calibri", italic=True, size=10)
        ws.cell(2, 1).fill = BLUE_FILL
        ws.cell(2, 1).alignment = WRAP
        ws.row_dimensions[2].height = 40

        headers = ["VM Name", "EC2 Instance Type", "Region", "vCPU", "RAM GB",
                   "3yr All-Upfront Total Cost", "Effective Monthly Cost", "On-Demand Monthly", "Saving %"]
        for ci, h in enumerate(headers, 1):
            h_row(ws, 3, ci, h)
        col_widths = [30, 20, 15, 8, 10, 25, 22, 22, 12]
        for ci, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(ci)].width = w

        ws.cell(8, 1, "Source: aws.amazon.com/ec2/pricing/reserved-instances — verify current rates at start of Phase 3").font = Font(name="Calibri", italic=True, size=9, color="888888")
        ws.merge_cells('A8:I8')

        freeze_header(ws, 4)

    wb.save(path)
    print(f"  Updated: {os.path.relpath(path, BASE)}")


# ── 8. gcp-evaluation.xlsx ────────────────────────────────────────────────────

def update_gcp_eval(path):
    wb = load_workbook(path)

    add_instructions_tab(wb,
        purpose="Model GCP TCO across two pricing scenarios: On-Demand and 3-year Committed Use Discounts (CUDs). CUDs are resource-based (commit to CPU/RAM in a region, not a specific instance type) — this gives more flexibility than AWS RI but requires knowing the target region and estimated CPU/RAM mix.",
        who="Platform Architect (GCP). Input from infrastructure-profiling.xlsx. Cross-validate with GCP Migration Center output (use RVTools export as input). For data/analytics workloads, model BigQuery and Dataproc alternatives alongside standard GCE pricing.",
        when="Phase 3 Weeks 11–13. Validate pricing against cloud.google.com/products/calculator at start of Phase 3. Document pricing source date in header.",
        good_data=[
            "Both On-Demand and 3yr CUD scenarios present",
            "Instance families use current generation (n2-standard, c3-standard — not n1)",
            "europe-west2 (London) primary region modelled — not US regions",
            "GCP Migration Center output cross-validated (if collector was deployed)",
            "Data/analytics workloads modelled with BigQuery/Dataproc pricing where applicable",
        ],
        mistakes=[
            "Using n1-standard (previous generation) — n2-standard is 30% more cost-effective",
            "Not specifying the target region — GCP pricing varies by region",
            "Omitting Memorystore (managed Redis) cost for Redis-heavy estates",
            "Forgetting sustained use discounts on On-Demand (GCP auto-applies these — include in baseline)",
        ],
        template_name="gcp-evaluation.xlsx",
        insert_at=0
    )

    # Add CUD tab if missing
    if "3yr CUD" not in wb.sheetnames:
        ws = wb.create_sheet("3yr CUD")
        ws.sheet_view.showGridLines = False

        title_row(ws, 1, "GCP 3-Year Committed Use Discounts (CUDs) — Resource-Based Commitment", 7, NAVY_FILL)
        ws.row_dimensions[1].height = 22

        ws.merge_cells('A2:G2')
        ws.cell(2, 1, "GCP CUDs commit to a specific amount of vCPU and memory in a region for 1 or 3 years — NOT to a specific instance type. This gives more flexibility than AWS Reserved Instances. Typical 3yr CUD saving: 37-55% vs On-Demand. CUDs apply to GCE instances; Preemptible/Spot VMs are not eligible.")
        ws.cell(2, 1).font = Font(name="Calibri", italic=True, size=10)
        ws.cell(2, 1).fill = BLUE_FILL
        ws.cell(2, 1).alignment = WRAP
        ws.row_dimensions[2].height = 50

        headers = ["VM / Workload Name", "GCE Machine Type (Optimised)", "Region",
                   "Committed vCPU", "Committed RAM (GB)", "On-Demand Monthly", "3yr CUD Monthly", "Saving %"]
        for ci, h in enumerate(headers, 1):
            h_row(ws, 3, ci, h)

        col_widths = [30, 25, 18, 16, 18, 22, 22, 12]
        for ci, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(ci)].width = w

        # CUD vs On-Demand comparison
        ws.merge_cells('A8:H8')
        title_row(ws, 8, "CUD Commitment Planning — Aggregate Regional CPU/RAM Required", 8, NAVY_FILL)
        h_row(ws, 9, 1, "Resource Type"); h_row(ws, 9, 2, "Region"); h_row(ws, 9, 3, "Total Committed Units")
        h_row(ws, 9, 4, "CUD Commitment (3yr)"); h_row(ws, 9, 5, "On-Demand Equivalent")
        h_row(ws, 9, 6, "3yr CUD Total Cost"); h_row(ws, 9, 7, "On-Demand 3yr Total"); h_row(ws, 9, 8, "CUD Saving")

        cud_rows = [
            ("vCPU (General Purpose — n2)", "europe-west2", "[Total vCPU]", "[£/hr]", "[£/hr]", "", "", ""),
            ("Memory GB (General Purpose — n2)", "europe-west2", "[Total RAM GB]", "[£/GB-hr]", "[£/GB-hr]", "", "", ""),
            ("vCPU (Memory-Optimised — n2-highmem)", "europe-west2", "[Total vCPU]", "[£/hr]", "[£/hr]", "", "", ""),
        ]
        for ri, row in enumerate(cud_rows, start=10):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                c = ws.cell(ri, ci, val); c.font = BODY_FONT; c.fill = f; c.border = THIN_BORDER; c.alignment = WRAP

        ws.cell(14, 1, "Source: cloud.google.com/compute/docs/instances/committed-use-discounts-overview — verify current rates at start of Phase 3").font = Font(name="Calibri", italic=True, size=9, color="888888")
        ws.merge_cells('A14:H14')

        freeze_header(ws, 4)

    # Add Managed Services tab if missing (for OSS alternatives)
    if "Managed Services" not in wb.sheetnames:
        ws2 = wb.create_sheet("Managed Services")
        ws2.sheet_view.showGridLines = False

        title_row(ws2, 1, "GCP Managed Service Alternatives — OSS Licence Risk Resolution", 5, NAVY_FILL)

        ws2.merge_cells('A2:E2')
        ws2.cell(2, 1, "For workloads flagged with OSS Licence Risk (Redis, Elasticsearch, MongoDB, Kafka, HashiCorp Vault), model the GCP managed service alternative cost here. Include this in the Layer (d) Licensing Overlay of the business-case-tco-roi.xlsx.")
        ws2.cell(2, 1).font = Font(name="Calibri", italic=True, size=10)
        ws2.cell(2, 1).fill = BLUE_FILL
        ws2.cell(2, 1).alignment = WRAP
        ws2.row_dimensions[2].height = 40

        headers = ["On-Prem Workload", "OSS Product", "Licence Risk", "GCP Managed Alternative", "Monthly Cost Estimate", "Notes"]
        for ci, h in enumerate(headers, 1):
            h_row(ws2, 3, ci, h)

        defaults = [
            ("[e.g., Caching layer]", "Redis OSS (post v7.4)", "SSPL — commercial restrictions", "Memorystore for Redis / Valkey", "[Enter from GCP Calculator]", "Resolves OSS licence risk"),
            ("[e.g., Search service]", "Elasticsearch (post 7.10)", "SSPL — commercial restrictions", "Elastic on GCP Marketplace / Vector Search", "[Enter from GCP Calculator]", "Native Elastic partnership"),
            ("[e.g., Secret vault]", "HashiCorp Vault (BSL)", "BSL — commercial use restrictions", "Secret Manager / Berglas", "[Enter from GCP Calculator]", "GCP-native, no licence concern"),
            ("[e.g., Message queue]", "Apache Kafka", "No licence risk", "Pub/Sub + Dataflow", "[Enter from GCP Calculator]", "Natural Kafka replacement on GCP"),
        ]
        col_widths = [25, 22, 25, 30, 25, 30]
        for ci, w in enumerate(col_widths, 1):
            ws2.column_dimensions[get_column_letter(ci)].width = w

        for ri, row in enumerate(defaults, start=4):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                c = ws2.cell(ri, ci, val); c.font = BODY_FONT; c.fill = f; c.border = THIN_BORDER; c.alignment = WRAP
            ws2.row_dimensions[ri].height = 25

    wb.save(path)
    print(f"  Updated: {os.path.relpath(path, BASE)}")


# ── 9. business-case-tco-roi.xlsx ─────────────────────────────────────────────

def update_business_case(path):
    wb = load_workbook(path)
    existing = wb.sheetnames

    # Add Instructions tab
    add_instructions_tab(wb,
        purpose="The master TCO business case workbook. Consolidates all 7 cost layers from the individual cloud evaluation templates into a single board-ready financial comparison. This is the document that goes to the customer's CFO and board. Every figure must trace back to a named tab.",
        who="Lead Architect (owns the model). Platform Architect (AWS/Azure/GCP) populates the cloud-specific inputs. Alliance Manager confirms Partner Credits (Layer g) before finalising. Delivery Manager reviews before Phase 3 playback.",
        when="Phase 3 Weeks 13–14. All individual cloud evaluation templates (azure-evaluation.xlsx, aws-evaluation.xlsx, gcp-evaluation.xlsx) must be complete before populating this workbook. Do NOT build this workbook in parallel with individual templates — validate each cloud model first.",
        good_data=[
            "All 7 cost layers present — no missing tabs",
            "Every figure traces to a source (cloud evaluation template tab and row)",
            "Pricing source date visible in header — not more than 90 days old",
            "AHB eligibility confirmed before including AHB scenario in board presentation",
            "Partner Credits (Layer g) confirmed by Alliance Manager before presenting",
            "Year 1 dual-running model shows the peak cost year honestly — no smoothing",
        ],
        mistakes=[
            "Presenting only layers (a) and (b) — these are not the full picture",
            "Including AHB saving without confirming Software Assurance status with customer",
            "Showing 'cloud is cheaper' before modelling on-prem status quo (layer e) properly",
            "Not including Year 1 dual-running — customers are always surprised by Year 1 cost",
            "Presenting partner credits (layer g) as confirmed before Alliance Manager signs off",
        ],
        template_name="business-case-tco-roi.xlsx",
        insert_at=0
    )

    # Add Licensing-Overlay tab if missing
    if "Licensing-Overlay" not in wb.sheetnames:
        ws = wb.create_sheet("Licensing-Overlay")
        ws.sheet_view.showGridLines = False

        title_row(ws, 1, "TCO Layer (d) — Licensing Overlay: AHB, BYOL, Oracle, EoL ESU", 7, NAVY_FILL)

        # Section: Windows AHB
        ws.merge_cells('A2:G2')
        title_row(ws, 2, "Section 1: Windows Server — Azure Hybrid Benefit", 7, PatternFill("solid", fgColor="0078D4"))

        headers = ["Licence Type", "Volume", "Current Annual Cost", "Cloud Scenario", "Optimised Annual Cost", "Annual Saving", "3yr Saving"]
        for ci, h in enumerate(headers, 1):
            h_row(ws, 3, ci, h)

        ahb_rows = [
            ("Windows Server Standard (AHB — Azure)", "[N from infrastructure-profiling]", "£/$ [X]", "AHB + 3yr RI", "£/$ [X]", "£/$ [X]", "£/$ [X]"),
            ("Windows Server Datacenter (AHB — Azure)", "[N]", "£/$ [X]", "AHB + 3yr RI", "£/$ [X]", "£/$ [X]", "£/$ [X]"),
        ]
        for ri, row in enumerate(ahb_rows, start=4):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                ws.cell(ri, ci, val).font = BODY_FONT; ws.cell(ri, ci).fill = f; ws.cell(ri, ci).border = THIN_BORDER; ws.cell(ri, ci).alignment = WRAP

        # Section: SQL AHB
        title_row(ws, 7, "Section 2: SQL Server — Azure Hybrid Benefit", 7, PatternFill("solid", fgColor="0078D4"))
        for ci, h in enumerate(headers, 1):
            h_row(ws, 8, ci, h)
        sql_rows = [
            ("SQL Server Standard (AHB — Azure)", "[N from infrastructure-profiling]", "£/$ [X]", "AHB + 3yr RI", "£/$ [X]", "£/$ [X]", "£/$ [X]"),
            ("SQL Server Enterprise (AHB — Azure)", "[N]", "£/$ [X]", "AHB + 3yr RI", "£/$ [X]", "£/$ [X]", "£/$ [X]"),
        ]
        for ri, row in enumerate(sql_rows, start=9):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                ws.cell(ri, ci, val).font = BODY_FONT; ws.cell(ri, ci).fill = f; ws.cell(ri, ci).border = THIN_BORDER

        # Section: Oracle BYOL
        title_row(ws, 12, "Section 3: Oracle — BYOL (Bring Your Own Licence)", 7, ORANGE_FILL)
        ws.cell(12, 1).font = Font(name="Calibri", bold=True, size=10, color="000000")
        for ci, h in enumerate(headers, 1):
            h_row(ws, 13, ci, h)
        oracle_rows = [
            ("Oracle SE2 (BYOL)", "[N instances]", "£/$ [X]", "BYOL on [Azure VM / AWS EC2 / GCP GCE]", "£/$ [X]", "£/$ [X]", "£/$ [X]"),
            ("Oracle EE (BYOL — Processor)", "[N cores]", "£/$ [X]", "BYOL on dedicated hosts (verify cloud rules)", "£/$ [X]", "£/$ [X]", "£/$ [X]"),
            ("Oracle RAC", "[N nodes]", "£/$ [X]", "AVS (Azure) / Dedicated host (AWS) / Bare Metal (GCP)", "£/$ [X]", "£/$ [X]", "Engage Oracle Practice Lead"),
        ]
        for ri, row in enumerate(oracle_rows, start=14):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                ws.cell(ri, ci, val).font = BODY_FONT; ws.cell(ri, ci).fill = f; ws.cell(ri, ci).border = THIN_BORDER; ws.cell(ri, ci).alignment = WRAP

        # EoL ESU section
        title_row(ws, 18, "Section 4: EoL OS Extended Security Updates (ESU) — Azure ESU is FREE, AWS/GCP ESU is PAID", 7, RED_FILL)
        for ci, h in enumerate(headers, 1):
            h_row(ws, 19, ci, h)
        esu_rows = [
            ("Windows Server 2012/R2 ESU", "[N from infrastructure-profiling]", "N/A (not yet in cloud)", "Azure: FREE  |  AWS/GCP: ~£100-200/server/yr", "£0 (Azure) OR £[X] (AWS/GCP)", "£[X] per server", "[N] x £[X] x 3yr"),
            ("SQL Server 2012/2014 ESU", "[N]", "N/A", "Azure: FREE  |  AWS/GCP: ~£100-200/server/yr", "£0 (Azure) OR £[X]", "£[X] per server", "[N] x £[X] x 3yr"),
        ]
        for ri, row in enumerate(esu_rows, start=20):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                ws.cell(ri, ci, val).font = BODY_FONT; ws.cell(ri, ci).fill = f; ws.cell(ri, ci).border = THIN_BORDER; ws.cell(ri, ci).alignment = WRAP
            ws.row_dimensions[ri].height = 30

        # Summary row
        ws.cell(23, 1, "TOTAL LICENSING OVERLAY SAVING").font = Font(name="Calibri", bold=True, size=11, color="FFFFFF")
        ws.cell(23, 1).fill = NAVY_FILL
        ws.cell(23, 7, "=SUM([Saving rows])").font = BOLD_FONT
        ws.cell(23, 7).fill = YELLOW_FILL
        ws.merge_cells('A23:F23')

        col_widths = [30, 25, 22, 40, 22, 18, 18]
        for ci, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(ci)].width = w

        freeze_header(ws, 4)

    # Add OnPrem-StatusQuo tab if missing
    if "OnPrem-StatusQuo" not in wb.sheetnames:
        ws = wb.create_sheet("OnPrem-StatusQuo")
        ws.sheet_view.showGridLines = False

        title_row(ws, 1, "TCO Layer (e) — On-Premises Status Quo: True Cost of Staying On-Premises (3-Year)", 6, NAVY_FILL)

        ws.merge_cells('A2:F2')
        ws.cell(2, 1, "IMPORTANT: This is the most frequently underestimated element of the TCO comparison. Include hardware refresh, data centre costs, VMware licence renewal, and OS support costs. When customers see their actual 3yr on-prem cost including hardware refresh, the cloud comparison changes significantly.")
        ws.cell(2, 1).font = Font(name="Calibri", bold=True, italic=True, size=10)
        ws.cell(2, 1).fill = YELLOW_FILL; ws.cell(2, 1).alignment = WRAP; ws.row_dimensions[2].height = 45

        headers = ["Cost Category", "Current Annual Cost", "Year 1", "Year 2", "Year 3", "3-Year Total", "Notes"]
        for ci, h in enumerate(headers, 1):
            h_row(ws, 3, ci, h)

        rows = [
            ("Hardware — Server refresh / maintenance", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(C4:E4)", "Include end of HW support contracts"),
            ("Data Centre — Colocation / facilities", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(C5:E5)", "Power, cooling, rack space, connectivity"),
            ("VMware / Hypervisor licences", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(C6:E6)", "Include vSphere, vCenter, NSX, vSAN"),
            ("OS Licences (Windows Server, RHEL)", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(C7:E7)", "Include SA renewals"),
            ("SQL Server licences (on-prem)", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(C8:E8)", "EA or per-core perpetual + SA"),
            ("Oracle licences (on-prem)", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(C9:E9)", "Processor or NUP — per Oracle BYOL path"),
            ("EoL OS Extended Security Updates", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(C10:E10)", "Win 2012, RHEL 6, SQL 2012 — confirm scope"),
            ("Operations (staff, monitoring, helpdesk)", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(C11:E11)", "On-prem operations overhead"),
            ("Backup / DR infrastructure", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(C12:E12)", ""),
            ("Network (WAN, interconnects)", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(C13:E13)", ""),
        ]
        for ri, row in enumerate(rows, start=4):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                ws.cell(ri, ci, val).font = BODY_FONT; ws.cell(ri, ci).fill = f
                ws.cell(ri, ci).border = THIN_BORDER; ws.cell(ri, ci).alignment = WRAP
            ws.row_dimensions[ri].height = 22

        total_row = 14
        ws.cell(total_row, 1, "TOTAL ON-PREMISES STATUS QUO COST").font = Font(name="Calibri", bold=True, size=11, color="FFFFFF")
        ws.cell(total_row, 1).fill = RED_FILL
        ws.merge_cells(f'A{total_row}:E{total_row}')
        ws.cell(total_row, 6, "=SUM(F4:F13)").font = Font(name="Calibri", bold=True, size=12)
        ws.cell(total_row, 6).fill = YELLOW_FILL; ws.cell(total_row, 6).border = THIN_BORDER; ws.cell(total_row, 6).alignment = CENTER

        col_widths = [35, 22, 18, 18, 18, 18, 40]
        for ci, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(ci)].width = w
        freeze_header(ws, 4)

    # Add Year1-DualRunning tab if missing
    if "Year1-DualRunning" not in wb.sheetnames:
        ws = wb.create_sheet("Year1-DualRunning")
        ws.sheet_view.showGridLines = False

        title_row(ws, 1, "TCO Layer (f) — Year 1 Dual-Running: Migration Overlap Cost Forecast", 5, NAVY_FILL)

        ws.merge_cells('A2:E2')
        ws.cell(2, 1, "Year 1 is typically the most expensive year of a migration because workloads run in both environments during the transition. This is the most common source of 'it cost more than expected in Year 1' complaints. Model it explicitly — do not hide it in a smoothed 3yr average.")
        ws.cell(2, 1).font = Font(name="Calibri", bold=True, italic=True, size=10)
        ws.cell(2, 1).fill = YELLOW_FILL; ws.cell(2, 1).alignment = WRAP; ws.row_dimensions[2].height = 40

        headers = ["Cost Component", "Q1", "Q2", "Q3", "Q4", "Year 1 Total", "Notes"]
        for ci, h in enumerate(headers, 1):
            h_row(ws, 3, ci, h)

        rows = [
            ("On-premises costs (remaining estate — decommission not complete)", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(B4:E4)", "Reduces quarterly as waves decommission on-prem"),
            ("Cloud costs (ramp-up — Waves 0 + 1 migrated)", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(B5:E5)", "Increases as more waves complete"),
            ("Migration tooling and licences", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(B6:E6)", "Azure Migrate / Velero / etc."),
            ("Professional services — Part 2 delivery (Rackspace)", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "=SUM(B7:E7)", "From Part 2 SOW"),
            ("Partner credits offset (AMM / MAP / PSO)", "(£/$ [X])", "(£/$ [X])", "(£/$ [X])", "(£/$ [X])", "=SUM(B8:E8)", "Negative row — reduces Year 1 cost"),
        ]
        for ri, row in enumerate(rows, start=4):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                ws.cell(ri, ci, val).font = BODY_FONT; ws.cell(ri, ci).fill = f
                ws.cell(ri, ci).border = THIN_BORDER; ws.cell(ri, ci).alignment = WRAP
            ws.row_dimensions[ri].height = 30

        total_row = 10
        ws.cell(total_row, 1, "YEAR 1 TOTAL (DUAL-RUNNING NET)").font = Font(name="Calibri", bold=True, size=11, color="FFFFFF")
        ws.cell(total_row, 1).fill = RED_FILL
        ws.merge_cells(f'A{total_row}:E{total_row}')
        ws.cell(total_row, 6, "=SUM(F4:F9)").font = Font(name="Calibri", bold=True, size=12)
        ws.cell(total_row, 6).fill = YELLOW_FILL; ws.cell(total_row, 6).border = THIN_BORDER; ws.cell(total_row, 6).alignment = CENTER

        col_widths = [42, 15, 15, 15, 15, 18, 40]
        for ci, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(ci)].width = w
        freeze_header(ws, 4)

    # Add Partner-Credits tab if missing
    if "Partner-Credits" not in wb.sheetnames:
        ws = wb.create_sheet("Partner-Credits")
        ws.sheet_view.showGridLines = False

        title_row(ws, 1, "TCO Layer (g) — Partner Discounts and Credits: AMM / MAP / PSO Funded Value", 6, NAVY_FILL)

        ws.merge_cells('A2:F2')
        ws.cell(2, 1, "THIS IS THE BOARD-LEVEL HEADLINE NUMBER. Layer (g) is what makes the cloud financial case compelling. Partner credits from AMM, MAP, or PSO can represent 10-30% of Part 2 professional services cost. MANDATORY: Confirm programme eligibility and registration status with the Rackspace Alliance Manager before including any figures here.")
        ws.cell(2, 1).font = Font(name="Calibri", bold=True, size=10)
        ws.cell(2, 1).fill = YELLOW_FILL; ws.cell(2, 1).alignment = WRAP; ws.row_dimensions[2].height = 50

        headers = ["Programme", "Hyperscaler", "Eligibility Status", "Estimated Funded Value",
                   "Registration Status", "Notes"]
        for ci, h in enumerate(headers, 1):
            h_row(ws, 3, ci, h)

        prog_rows = [
            ("Azure Migration and Modernisation (AMM)", "Microsoft", "[Eligible / Not Eligible / TBC]", "£/$ [X] – [Y]", "[Not Registered / Registered / Approved]", "Must be registered in MSPP before Part 2 SOW. Requires Azure as primary or co-primary recommendation."),
            ("AWS Migration Acceleration Programme (MAP)", "AWS", "[Eligible / Not Eligible / TBC]", "£/$ [X] – [Y]", "[Not Registered / Registered / Approved]", "Must be registered in AWS ACE before assessment evidence compiled. Requires AWS as primary or co-primary."),
            ("Google Cloud RAMP / PSO Credits", "Google", "[Eligible / Not Eligible / TBC]", "£/$ [X] – [Y]", "[Not Registered / Registered / Approved]", "Programme terms vary by geography. Confirm with Rackspace Alliance Manager."),
        ]
        col_widths = [32, 14, 22, 25, 28, 50]
        for ci, w in enumerate(col_widths, 1):
            ws.column_dimensions[get_column_letter(ci)].width = w

        for ri, row in enumerate(prog_rows, start=4):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            for ci, val in enumerate(row, 1):
                ws.cell(ri, ci, val).font = BODY_FONT; ws.cell(ri, ci).fill = f
                ws.cell(ri, ci).border = THIN_BORDER; ws.cell(ri, ci).alignment = WRAP
            ws.row_dimensions[ri].height = 40

        ws.cell(8, 1, "TOTAL PARTNER CREDITS (Confirmed):").font = Font(name="Calibri", bold=True, size=11, color="FFFFFF")
        ws.cell(8, 1).fill = NAVY_FILL
        ws.cell(8, 4, "[Enter confirmed total from Alliance Manager]").font = Font(name="Calibri", bold=True, size=11)
        ws.cell(8, 4).fill = GREEN_FILL; ws.cell(8, 4).border = THIN_BORDER; ws.cell(8, 4).alignment = CENTER
        ws.merge_cells('A8:C8')

        # 3yr Net Cost Summary
        title_row(ws, 10, "3-Year Net Cost Summary — Board-Level Headline", 6, PatternFill("solid", fgColor="E31C3D"))
        summary_rows = [
            ("On-Premises Status Quo (3yr)", "=[OnPrem-StatusQuo tab total]", "Baseline"),
            ("[Primary Cloud] Like-for-Like (3yr)", "=[Cloud eval tab total]", "+/- vs on-prem"),
            ("[Primary Cloud] Optimised + AHB/BYOL (3yr)", "=[Licensing-Overlay adjusted]", "+/- vs on-prem"),
            ("[Primary Cloud] Optimised + Partner Credits (3yr)", "=[Optimised] - [Partner Credits]", "NET COST — THIS IS THE HEADLINE"),
        ]
        for ci, h in enumerate(["Scenario", "3yr Total Cost", "vs On-Prem"], 1):
            h_row(ws, 11, ci, h)
        for ri, row in enumerate(summary_rows, start=12):
            f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
            if "HEADLINE" in row[2]:
                f = GREEN_FILL
            for ci, val in enumerate(row, 1):
                ws.cell(ri, ci, val).font = BOLD_FONT if "HEADLINE" in row[2] else BODY_FONT
                ws.cell(ri, ci).fill = f; ws.cell(ri, ci).border = THIN_BORDER; ws.cell(ri, ci).alignment = WRAP
            ws.row_dimensions[ri].height = 25

        freeze_header(ws, 4)

    wb.save(path)
    print(f"  Updated: {os.path.relpath(path, BASE)}")


# ── 10. Create saas-application-assessment.xlsx ───────────────────────────────

def create_saas_template(path):
    if os.path.exists(path):
        print(f"  Exists (skip): {os.path.relpath(path, BASE)}")
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "SaaS Inventory"

    # Title
    ws.merge_cells('A1:J1')
    ws.cell(1, 1, "SaaS Application Assessment").font = Font(name="Calibri", bold=True, size=16, color="E31C3D")
    ws.cell(1, 1).alignment = LEFT

    headers = [
        "App ID", "SaaS Application Name", "Vendor", "Business Function",
        "Contract Renewal Date", "Annual Cost £/$", "Users (Internal)",
        "Migration Path", "On-Prem Integration?", "Notes"
    ]
    for ci, h in enumerate(headers, 1):
        h_row(ws, 2, ci, h)

    col_widths = [8, 30, 20, 25, 22, 18, 18, 30, 22, 30]
    for ci, w in enumerate(col_widths, 1):
        ws.column_dimensions[get_column_letter(ci)].width = w

    migration_paths = ["Retain (SaaS stays)", "Replace with cloud-native equivalent", "Integrate with migrated on-prem apps", "Retire", "TBC"]
    sample_rows = [
        ("S001", "[e.g., Salesforce CRM]", "[Vendor]", "CRM / Customer management", "[MM/YYYY]", "£[X]", "[N]", "Retain (SaaS stays)", "Yes — integrates with on-prem ERP", "Check API compatibility with migrated ERP"),
        ("S002", "[e.g., ServiceNow ITSM]", "[Vendor]", "ITSM / Change management", "[MM/YYYY]", "£[X]", "[N]", "Retain (SaaS stays)", "Yes — CAB process managed here", "CAB lead times from ServiceNow affect Phase 1 timeline"),
    ]
    for ri, row in enumerate(sample_rows, start=3):
        f = LGRAY_FILL if ri % 2 == 0 else PatternFill()
        for ci, val in enumerate(row, 1):
            ws.cell(ri, ci, val).font = BODY_FONT; ws.cell(ri, ci).fill = f
            ws.cell(ri, ci).border = THIN_BORDER; ws.cell(ri, ci).alignment = WRAP

    ws.freeze_panes = "A3"

    # Instructions tab
    add_instructions_tab(wb,
        purpose="Track all SaaS applications in the customer estate. SaaS applications do not migrate in the same way as on-prem VMs, but they must be catalogued because: (1) they may have on-prem integrations that break when the integrated app migrates, and (2) they represent ongoing contracts that affect the total cost comparison.",
        who="Lead Architect (initial pass from customer IT spend records) + Business stakeholders (validate renewal dates and integration dependencies).",
        when="Phase 1 alongside the main application inventory. SaaS applications with on-prem integrations must be included in the dependency mapping. SaaS contracts due for renewal during the migration window should be flagged to the Alliance Manager.",
        good_data=[
            "All SaaS applications with on-prem integrations are identified",
            "Contract renewal dates captured — flag any renewing during the migration window",
            "Annual costs captured — they feed into the on-prem status quo cost comparison",
            "Migration Path confirmed: Retain / Replace / Integrate / Retire",
        ],
        mistakes=[
            "Treating SaaS applications as entirely out of scope — their integrations affect migration",
            "Not capturing renewal dates — a SaaS contract renewing during migration adds lock-in risk",
            "Ignoring SaaS-to-on-prem API dependencies — these break when the on-prem app migrates",
        ],
        template_name="saas-application-assessment.xlsx"
    )

    wb.save(path)
    print(f"  Created: {os.path.relpath(path, BASE)}")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("Modifying Excel templates...")
    print()

    print("Discovery templates (4A):")
    update_app_scoping(      os.path.join(BASE, "Templates/01-discovery/application-scoping-profiling.xlsx"))
    update_infra_profiling(  os.path.join(BASE, "Templates/01-discovery/infrastructure-profiling.xlsx"))
    update_dependency_mapping(os.path.join(BASE,"Templates/01-discovery/dependency-mapping.xlsx"))
    create_saas_template(    os.path.join(BASE, "Templates/01-discovery/saas-application-assessment.xlsx"))

    print()
    print("Governance/Risk templates (4E):")
    update_governance_foundations(os.path.join(BASE, "Templates/02-analysis/governance-foundations-alignment.xlsx"))
    update_risk_assessment(  os.path.join(BASE, "Templates/04-planning/risk-assessment.xlsx"))

    print()
    print("TCO/Evaluation templates (4B):")
    update_azure_eval(       os.path.join(BASE, "Templates/03-evaluation/azure-evaluation.xlsx"))
    update_aws_eval(         os.path.join(BASE, "Templates/03-evaluation/aws-evaluation.xlsx"))
    update_gcp_eval(         os.path.join(BASE, "Templates/03-evaluation/gcp-evaluation.xlsx"))
    update_business_case(    os.path.join(BASE, "Templates/03-evaluation/business-case-tco-roi.xlsx"))

    print()
    print("All Excel templates updated.")

if __name__ == "__main__":
    main()
