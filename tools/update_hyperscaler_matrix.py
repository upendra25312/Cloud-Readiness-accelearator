#!/usr/bin/env python3
"""
4C.1-4C.4: Audit and enhance hyperscaler-decision-matrix.xlsx
Adds: Instructions, Criteria & Weights, Azure/AWS/GCP Scoring, Weighted Summary,
      7Rs Estate View, Multi-Cloud Exceptions, Worked Example tabs
"""
import os
import openpyxl
from openpyxl.styles import (
    PatternFill, Font, Alignment, Border, Side
)
from openpyxl.utils import get_column_letter

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(BASE, "Templates", "03-evaluation", "hyperscaler-decision-matrix.xlsx")

# ── colour palette ────────────────────────────────────────────────────────────
RED    = "E31C3D"   # Rackspace red
NAVY   = "1F3864"
WHITE  = "FFFFFF"
LGRAY  = "F2F2F2"
DGRAY  = "D9D9D9"
AZURE  = "0078D4"
AWSOR  = "FF9900"
GCPBL  = "4285F4"
AMBER  = "FFC000"
GREEN  = "70AD47"
YELLOW = "FFFF99"

def _fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def _font(bold=False, color=WHITE, size=10, italic=False):
    return Font(bold=bold, color=color, size=size, italic=italic, name="Calibri")

def _align(h="left", v="center", wrap=True):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)

def _border():
    s = Side(style="thin", color="AAAAAA")
    return Border(left=s, right=s, top=s, bottom=s)

def _hdr(ws, row, col, text, bg=RED, fg=WHITE, bold=True, size=10):
    c = ws.cell(row=row, column=col, value=text)
    c.fill = _fill(bg)
    c.font = _font(bold=bold, color=fg, size=size)
    c.alignment = _align()
    c.border = _border()
    return c

def _cell(ws, row, col, text, bg=WHITE, fg="000000", bold=False, wrap=True, align="left"):
    c = ws.cell(row=row, column=col, value=text)
    c.fill = _fill(bg)
    c.font = _font(bold=bold, color=fg)
    c.alignment = _align(h=align, wrap=wrap)
    c.border = _border()
    return c

def _title(ws, row, text, cols, bg=NAVY):
    ws.cell(row=row, column=1, value=text).fill = _fill(bg)
    ws.cell(row=row, column=1).font = _font(bold=True, size=12)
    ws.cell(row=row, column=1).alignment = _align(h="center")
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=cols)

def set_col_widths(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


# ── INSTRUCTIONS ─────────────────────────────────────────────────────────────
def add_instructions(wb):
    ws = wb.create_sheet("Instructions", 0)
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["B"].width = 80

    _title(ws, 1, "HYPERSCALER DECISION MATRIX", 2)
    _title(ws, 2, "CRA Framework -- Phase 3: Hyperscaler Evaluation", 2, bg="404040")

    rows = [
        ("PURPOSE", ""),
        ("", "Produce a weighted, evidence-backed score for each hyperscaler and generate a"),
        ("", "documented primary recommendation. This is the single most customer-visible"),
        ("", "deliverable in Phase 3. Scores that look arbitrary or pre-determined will undermine"),
        ("", "the entire engagement. Every score MUST cite a specific evidence data point."),
        ("", ""),
        ("WHO FILLS THIS IN", ""),
        ("", "Lead Architect (scoring framework) + Platform Architects (per-cloud scoring)"),
        ("", "Criteria & Weights tab: agreed with customer before scoring begins."),
        ("", ""),
        ("WHEN", ""),
        ("", "Phase 3, Weeks 1-3. Must be complete before Phase 3 playback meeting."),
        ("", "GATE: Do not present a recommendation before slides 8-12 of the playback deck."),
        ("", ""),
        ("TAB GUIDE", ""),
        ("Instructions",        "This sheet"),
        ("Criteria & Weights",  "Define evaluation criteria and weighting -- agree with customer first"),
        ("Azure Scoring",       "Score Azure against each criterion with specific evidence"),
        ("AWS Scoring",         "Score AWS against each criterion with specific evidence"),
        ("GCP Scoring",         "Score GCP against each criterion with specific evidence"),
        ("Weighted Summary",    "Auto-calculated weighted totals + recommendation output"),
        ("7Rs Estate View",     "One row per application: Rehost/Replatform/Rearchitect/Repurchase/Retire/Retain/Relocate"),
        ("Multi-Cloud Exceptions", "Apps that cannot go to the primary cloud -- documented reason"),
        ("Worked Example",      "Anonymised reference scoring -- do NOT present to customer"),
        ("", ""),
        ("EVIDENCE STANDARD", ""),
        ("", "ACCEPTABLE: 'Azure 3yr RI + AHB: 39% saving vs on-prem -- see TCO Summary tab'"),
        ("", "NOT ACCEPTABLE: 'Azure is cheaper'"),
        ("", "ACCEPTABLE: '1,200 Windows + 347 SQL Server AHB-eligible -- saving estimated Xm/yr'"),
        ("", "NOT ACCEPTABLE: 'Good licensing options'"),
        ("", ""),
        ("PROCESS", ""),
        ("", "1. Present Criteria & Weights to customer and get written agreement (email OK)"),
        ("", "2. Complete Azure Scoring, AWS Scoring, GCP Scoring tabs with evidence"),
        ("", "3. Weighted Summary calculates automatically"),
        ("", "4. Complete 7Rs Estate View for all in-scope applications"),
        ("", "5. Document any multi-cloud exceptions in Multi-Cloud Exceptions tab"),
        ("", "6. Present Weighted Summary in Phase 3 playback (slide 12, BEFORE recommendation)"),
        ("", ""),
        ("QUESTIONS?", "Refer to docs/guides/03-evaluation-phase-guide.md"),
    ]

    for i, (label, val) in enumerate(rows, 3):
        if label and label != "":
            c = ws.cell(row=i, column=1, value=label)
            c.font = _font(bold=True, color="000000", size=10)
            c.fill = _fill(LGRAY)
            c.alignment = _align()
            c.border = _border()
        else:
            ws.cell(row=i, column=1).border = _border()

        c2 = ws.cell(row=i, column=2, value=val)
        c2.font = Font(name="Calibri", size=10, color="000000")
        c2.alignment = _align()
        c2.border = _border()

    ws.row_dimensions[1].height = 28
    ws.row_dimensions[2].height = 20


# ── CRITERIA & WEIGHTS ────────────────────────────────────────────────────────
def add_criteria_weights(wb):
    ws = wb.create_sheet("Criteria & Weights")
    ws.sheet_view.showGridLines = False
    set_col_widths(ws, [5, 32, 58, 14, 40])

    _title(ws, 1, "CRITERIA & WEIGHTS -- Agree with customer BEFORE scoring begins", 5)
    _title(ws, 2, "Edit the Weight % column to reflect customer-agreed weightings. Total must equal 100%.", 5, bg="404040")

    hdrs = ["#", "Criterion", "Description", "Weight %", "Notes"]
    for c, h in enumerate(hdrs, 1):
        _hdr(ws, 3, c, h)

    criteria = [
        (1, "Total Cost of Ownership (3yr)",
         "L4L and optimised scenarios across all tiers. Include Year 1 dual-running and partner credits.",
         "30%", "Highest weight -- customers care most about cost"),
        (2, "Licensing Advantage",
         "AHB / BYOL / SA portability; SQL Server, Windows Server, Oracle BYOL options.",
         "20%", "High impact for Microsoft-heavy estates (Windows/SQL)"),
        (3, "Technical Fit",
         "Workload type compatibility; managed services availability; GPU / HPC / storage options.",
         "15%", "Consider .NET, Oracle, Linux, container workloads"),
        (4, "Regulatory & Compliance",
         "Certifications (ISO 27001, SOC 2, FCA, GDPR); data residency; UK region footprint.",
         "15%", "Critical for regulated sectors (media, finance, health)"),
        (5, "Partner Commercial (AMM/MAP/PSO)",
         "Funded programme eligibility; estimated credit value; deal registration status.",
         "10%", "Rackspace differentiator -- must be quantified"),
        (6, "Strategic Alignment",
         "Existing enterprise agreements; roadmap alignment; executive relationships; support contracts.",
         "10%", "EA and Unified Support carry weight for enterprise customers"),
    ]
    bg_cycle = [WHITE, LGRAY]
    for i, (num, name, desc, wt, notes) in enumerate(criteria):
        r = 4 + i
        bg = bg_cycle[i % 2]
        _cell(ws, r, 1, num, bg=bg, align="center")
        _cell(ws, r, 2, name, bg=bg, bold=True, fg="000000")
        _cell(ws, r, 3, desc, bg=bg, fg="000000")
        _cell(ws, r, 4, wt, bg=bg, align="center", fg="000000")
        _cell(ws, r, 5, notes, bg=bg, fg="444444")

    r = 10
    _cell(ws, r, 1, "", bg=NAVY)
    _cell(ws, r, 2, "TOTAL", bg=NAVY, bold=True)
    _cell(ws, r, 3, "", bg=NAVY)
    _cell(ws, r, 4, "100%", bg=NAVY, bold=True, align="center")
    _cell(ws, r, 5, "Must equal 100% before scoring begins", bg=NAVY)

    ws.row_dimensions[1].height = 24
    ws.row_dimensions[2].height = 20


# ── SCORING TAB (shared structure) ───────────────────────────────────────────
def add_scoring_tab(wb, name, cloud_color):
    ws = wb.create_sheet(name)
    ws.sheet_view.showGridLines = False
    set_col_widths(ws, [32, 10, 10, 58, 38, 16])

    _title(ws, 1, f"{name.upper()} -- Evidence-backed scoring", 6, bg=cloud_color)
    _title(ws, 2, "Score = Lead Architect assessment (1-10). Evidence MUST be specific -- cite tab, date, or source.", 6, bg="404040")

    hdrs = ["Criterion", "Weight %", "Score (1-10)", "Evidence (specific data point)", "Source", "Weighted Score"]
    for c, h in enumerate(hdrs, 1):
        _hdr(ws, 3, c, h, bg=cloud_color)

    criteria = [
        "Total Cost of Ownership (3yr)",
        "Licensing Advantage",
        "Technical Fit",
        "Regulatory & Compliance",
        "Partner Commercial (AMM/MAP/PSO)",
        "Strategic Alignment",
    ]
    weights = [0.30, 0.20, 0.15, 0.15, 0.10, 0.10]
    bg_cycle = [WHITE, LGRAY]
    for i, (crit, wt) in enumerate(zip(criteria, weights)):
        r = 4 + i
        bg = bg_cycle[i % 2]
        _cell(ws, r, 1, crit, bg=bg, fg="000000", bold=True)
        _cell(ws, r, 2, f"{int(wt*100)}%", bg=bg, align="center", fg="000000")
        _cell(ws, r, 3, "[0-10]", bg=YELLOW, align="center", fg="000000")
        _cell(ws, r, 4, "[Enter specific evidence -- e.g. 'Azure 3yr RI: 39% saving vs on-prem -- TCO tab']", bg=YELLOW, fg="444444")
        _cell(ws, r, 5, "[TCO tab / interview / public doc]", bg=YELLOW, fg="444444")
        col_letter_score = get_column_letter(3)
        col_letter_weight = get_column_letter(2)
        ws.cell(row=r, column=6).value = f"=VALUE(LEFT({col_letter_weight}{r},LEN({col_letter_weight}{r})-1))/100*{col_letter_score}{r}"
        ws.cell(row=r, column=6).fill = _fill(LGRAY)
        ws.cell(row=r, column=6).font = _font(color="000000")
        ws.cell(row=r, column=6).alignment = _align(h="center")
        ws.cell(row=r, column=6).border = _border()

    r = 10
    for c in range(1, 6):
        _cell(ws, r, c, "", bg=NAVY)
    ws.cell(row=r, column=1).value = "WEIGHTED TOTAL"
    ws.cell(row=r, column=1).font = _font(bold=True)
    ws.cell(row=r, column=6).value = "=SUM(F4:F9)"
    ws.cell(row=r, column=6).fill = _fill(NAVY)
    ws.cell(row=r, column=6).font = _font(bold=True)
    ws.cell(row=r, column=6).alignment = _align(h="center")
    ws.cell(row=r, column=6).border = _border()

    r = 12
    _title(ws, r, "EVIDENCE QUALITY REMINDER", 6, bg="C00000")
    r = 13
    for c in range(1, 7):
        ws.cell(row=r, column=c).fill = _fill(LGRAY)
        ws.cell(row=r, column=c).border = _border()
    ws.cell(row=r, column=1).value = "ACCEPTABLE evidence:"
    ws.cell(row=r, column=1).font = _font(bold=True, color="000000")
    ws.cell(row=r, column=2).value = "'Azure 3yr RI + AHB: 39% saving -- see TCO tab' | '1,200 Windows AHB-eligible -- saving XM/yr'"
    ws.cell(row=r, column=2).font = Font(name="Calibri", size=9, color="006400", italic=True)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)

    r = 14
    for c in range(1, 7):
        ws.cell(row=r, column=c).fill = _fill("FFE6E6")
        ws.cell(row=r, column=c).border = _border()
    ws.cell(row=r, column=1).value = "NOT ACCEPTABLE:"
    ws.cell(row=r, column=1).font = _font(bold=True, color="C00000")
    ws.cell(row=r, column=2).value = "'Azure is cheaper' | 'Good licensing options' | 'Strong compliance'"
    ws.cell(row=r, column=2).font = Font(name="Calibri", size=9, color="C00000", italic=True)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)

    ws.row_dimensions[1].height = 24


# ── WEIGHTED SUMMARY ──────────────────────────────────────────────────────────
def add_weighted_summary(wb):
    ws = wb.create_sheet("Weighted Summary")
    ws.sheet_view.showGridLines = False
    set_col_widths(ws, [32, 10, 14, 14, 14])

    _title(ws, 1, "WEIGHTED SUMMARY -- Phase 3 Playback Output", 5)
    _title(ws, 2, "This tab is the output presented in the Phase 3 playback deck (slide 12). Scores auto-calculate from scoring tabs.", 5, bg="404040")

    hdrs = ["Criterion", "Weight", "Azure", "AWS", "GCP"]
    for c, h in enumerate(hdrs, 1):
        _hdr(ws, 3, c, h)

    criteria = ["Total Cost of Ownership (3yr)", "Licensing Advantage", "Technical Fit",
                "Regulatory & Compliance", "Partner Commercial (AMM/MAP/PSO)", "Strategic Alignment"]
    weight_refs = ["30%", "20%", "15%", "15%", "10%", "10%"]
    bg_cycle = [WHITE, LGRAY]

    for i, (crit, wt) in enumerate(zip(criteria, weight_refs)):
        r = 4 + i
        bg = bg_cycle[i % 2]
        _cell(ws, r, 1, crit, bg=bg, fg="000000", bold=True)
        _cell(ws, r, 2, wt, bg=bg, align="center", fg="000000")
        for col, sheet in [(3, "'Azure Scoring'"), (4, "'AWS Scoring'"), (5, "'GCP Scoring'")]:
            ref_row = 4 + i
            ws.cell(row=r, column=col).value = f"={sheet}!F{ref_row}"
            ws.cell(row=r, column=col).fill = _fill(bg)
            ws.cell(row=r, column=col).font = Font(name="Calibri", size=10, color="000000")
            ws.cell(row=r, column=col).alignment = _align(h="center")
            ws.cell(row=r, column=col).border = _border()

    r = 10
    _cell(ws, r, 1, "WEIGHTED TOTAL", bg=NAVY, bold=True)
    _cell(ws, r, 2, "", bg=NAVY)
    for col, rng in [(3, "C4:C9"), (4, "D4:D9"), (5, "E4:E9")]:
        ws.cell(row=r, column=col).value = f"=SUM({rng})"
        ws.cell(row=r, column=col).fill = _fill(NAVY)
        ws.cell(row=r, column=col).font = _font(bold=True)
        ws.cell(row=r, column=col).alignment = _align(h="center")
        ws.cell(row=r, column=col).border = _border()

    r = 11
    _cell(ws, r, 1, "RANK", bg=DGRAY, bold=True, fg="000000")
    _cell(ws, r, 2, "", bg=DGRAY)
    for col in [3, 4, 5]:
        _cell(ws, r, col, "[Rank auto or manual: 1st / 2nd / 3rd]", bg=AMBER, fg="000000", align="center")

    r = 13
    _title(ws, r, "RECOMMENDATION OUTPUT", 5, bg="C00000")
    rows_rec = [
        ("Primary Recommendation", "[HYPERSCALER] is recommended as the primary cloud platform"),
        ("Region", "[PRIMARY REGION] primary / [DR REGION] DR"),
        ("Rationale 1", "[Specific data point -- e.g. 'Highest 3yr TCO saving: 39% -- see slide 9']"),
        ("Rationale 2", "[Specific data point -- e.g. '1,200+ Windows + 347 SQL AHB-eligible -- saving XM/yr']"),
        ("Rationale 3", "[Specific data point -- e.g. 'UK South holds FCA, ISO 27001, SOC 2 -- data residency confirmed']"),
        ("Rationale 4", "[Specific data point -- e.g. 'AMM eligibility confirmed: estimated 800K-1.2M funded services']"),
        ("Rationale 5", "[Specific data point -- optional 5th bullet]"),
        ("Secondary Cloud", "[HYPERSCALER] for [specific use case or DR]"),
        ("Multi-Cloud Note", "[N] workload exceptions -- see Multi-Cloud Exceptions tab"),
    ]
    for i, (label, val) in enumerate(rows_rec):
        r2 = 14 + i
        _cell(ws, r2, 1, label, bg=LGRAY, bold=True, fg="000000")
        ws.merge_cells(start_row=r2, start_column=2, end_row=r2, end_column=5)
        _cell(ws, r2, 2, val, bg=YELLOW if "Rationale" in label else WHITE, fg="000000")

    r3 = 24
    _title(ws, r3, "EVIDENCE-BEFORE-RECOMMENDATION CHECKLIST", 5, bg=NAVY)
    checks = [
        "1. Estate summary (what was assessed) -- presented before scoring",
        "2. Readiness profile (Phase 2 output) -- presented before scoring",
        "3. Cloud comparison: cost, licensing, compliance -- all 3 clouds treated equally",
        "4. Scoring matrix (weights agreed with customer) -- presented before recommendation",
        "5. Recommendation -- appears AFTER all of the above. If not: restructure the deck.",
    ]
    for i, chk in enumerate(checks):
        r4 = 25 + i
        bg = bg_cycle[i % 2]
        _cell(ws, r4, 1, "[  ]", bg=bg, align="center", fg="000000")
        ws.merge_cells(start_row=r4, start_column=2, end_row=r4, end_column=5)
        _cell(ws, r4, 2, chk, bg=bg, fg="000000")


# ── 7Rs ESTATE VIEW ───────────────────────────────────────────────────────────
def add_7rs_estate_view(wb):
    ws = wb.create_sheet("7Rs Estate View")
    ws.sheet_view.showGridLines = False
    set_col_widths(ws, [10, 26, 16, 20, 18, 36, 14, 30, 14, 28])

    # Summary section first
    _title(ws, 1, "7Rs ESTATE VIEW -- Named SOW Deliverable", 10)
    _title(ws, 2, "Flag every application with a migration pattern. Complete before Phase 3 playback.", 10, bg="404040")

    summary_hdrs = ["Pattern", "Count", "% of Estate", "Notes"]
    patterns_summary = [
        ("Rehost",     "=COUNTIF(E:E,\"Rehost\")",     "Target: 50-70% of typical estate"),
        ("Replatform", "=COUNTIF(E:E,\"Replatform\")", "Target: 15-25%"),
        ("Rearchitect","=COUNTIF(E:E,\"Rearchitect\")","Target: 5-10% (high cost/complexity)"),
        ("Repurchase",  "=COUNTIF(E:E,\"Repurchase\")", "Replace with SaaS"),
        ("Retire",     "=COUNTIF(E:E,\"Retire\")",     "Cost saving -- quantify decommission saving"),
        ("Retain",     "=COUNTIF(E:E,\"Retain\")",     "Multi-cloud exceptions -- see that tab"),
        ("Relocate",   "=COUNTIF(E:E,\"Relocate\")",   "DC consolidation without cloud"),
        ("TOTAL",      "=COUNTA(E18:E500)-COUNTBLANK(E18:E500)", ""),
    ]

    _title(ws, 3, "SUMMARY (auto-calculated from data below)", 10, bg=NAVY)
    for c, h in enumerate(summary_hdrs, 1):
        _hdr(ws, 4, c, h)
    for c in range(5, 11):
        _cell(ws, 4, c, "", bg=RED)

    PAT_COLORS = {
        "Rehost": "C6EFCE",     # green
        "Replatform": "FFEB9C", # yellow
        "Rearchitect": "FFC7CE",# red
        "Repurchase": "BDD7EE", # blue
        "Retire": "D9D9D9",     # grey
        "Retain": "FCE4D6",     # orange
        "Relocate": "E2EFDA",   # light green
        "TOTAL": DGRAY,
    }
    for i, (pat, cnt_formula, notes) in enumerate(patterns_summary):
        r = 5 + i
        bg = PAT_COLORS.get(pat, WHITE)
        _cell(ws, r, 1, pat, bg=bg, bold=(pat == "TOTAL"), fg="000000")
        ws.cell(row=r, column=2).value = cnt_formula
        ws.cell(row=r, column=2).fill = _fill(bg)
        ws.cell(row=r, column=2).font = Font(name="Calibri", size=10, color="000000")
        ws.cell(row=r, column=2).alignment = _align(h="center")
        ws.cell(row=r, column=2).border = _border()
        pct_cell = ws.cell(row=r, column=3)
        pct_cell.value = f"=IF(B{r}>0,B{r}/B13,\"\")" if pat != "TOTAL" else ""
        pct_cell.number_format = "0%"
        pct_cell.fill = _fill(bg)
        pct_cell.font = Font(name="Calibri", size=10, color="000000")
        pct_cell.alignment = _align(h="center")
        pct_cell.border = _border()
        _cell(ws, r, 4, notes, bg=bg, fg="444444")
        for c in range(5, 11):
            _cell(ws, r, c, "", bg=bg)

    # Reference table
    _title(ws, 14, "7Rs CLASSIFICATION REFERENCE", 10, bg=NAVY)
    ref_hdrs = ["Pattern", "Definition", "When to Use"]
    for c, h in enumerate(ref_hdrs, 1):
        _hdr(ws, 15, c, h)
    for c in range(4, 11):
        _cell(ws, 15, c, "", bg=RED)

    ref_rows = [
        ("Rehost",     "Lift-and-shift to IaaS VM. No code changes.",
         "No code changes needed; fastest migration path; most of the estate (50-70%)"),
        ("Replatform", "Migrate with minor changes to use managed services.",
         "e.g., SQL Server -> Azure SQL Managed Instance; saves patching overhead"),
        ("Rearchitect","Significant redesign to use cloud-native services.",
         "e.g., monolith -> containers; high complexity / high long-term benefit"),
        ("Repurchase",  "Replace with a SaaS product.",
         "e.g., on-prem CRM -> Salesforce; vendor SaaS now covers the need"),
        ("Retire",     "Decommission -- do not migrate.",
         "Application confirmed redundant or replaced; stop paying for it"),
        ("Retain",     "Keep on-premises -- cannot migrate.",
         "Regulatory / latency / dependency constraint prevents migration"),
        ("Relocate",   "Move to different DC without cloud.",
         "Consolidate DCs without migrating to cloud"),
    ]
    bg_cycle = [WHITE, LGRAY]
    for i, (pat, defn, when) in enumerate(ref_rows):
        r = 16 + i
        bg = bg_cycle[i % 2]
        _cell(ws, r, 1, pat, bg=bg, bold=True, fg="000000")
        _cell(ws, r, 2, defn, bg=bg, fg="000000")
        _cell(ws, r, 3, when, bg=bg, fg="444444")
        for c in range(4, 11):
            _cell(ws, r, c, "", bg=bg)

    # Data table
    _title(ws, 24, "APPLICATION DATA -- One row per application", 10, bg="C00000")
    hdrs_data = ["App ID", "Application Name", "Business Criticality",
                 "Current Platform", "7R Classification", "Justification",
                 "Complexity", "Target Service", "Wave (Indicative)", "Notes"]
    for c, h in enumerate(hdrs_data, 1):
        _hdr(ws, 25, c, h)

    sample_rows = [
        ("APP-001", "[App Name]", "Critical", "VMware vSphere", "Rehost",
         "No code changes needed; fast migration path", "Low",
         "Azure VM D4sv5 / AWS m6i.xlarge / GCP n2-standard-4", "2", ""),
        ("APP-002", "[App Name]", "High", "VMware vSphere", "Replatform",
         "SQL Server -> Azure SQL Managed Instance; reduces patching overhead", "Medium",
         "Azure SQL Managed Instance", "3", "Validate compatibility"),
        ("APP-003", "[App Name]", "Medium", "Physical", "Retire",
         "Confirmed redundant -- replaced by SaaS product", "Low",
         "Decommission", "0", "Save decommission cost"),
        ("APP-004", "[App Name]", "High", "VMware vSphere", "Retain",
         "Latency requirement <5ms to on-prem payment system", "N/A",
         "On-premises (retain)", "N/A", "See Multi-Cloud Exceptions tab"),
    ]
    for i, row in enumerate(sample_rows):
        r = 26 + i
        bg = bg_cycle[i % 2]
        for c, val in enumerate(row, 1):
            _cell(ws, r, c, val, bg=bg, fg="000000")


# ── MULTI-CLOUD EXCEPTIONS ────────────────────────────────────────────────────
def add_multicloud_exceptions(wb):
    ws = wb.create_sheet("Multi-Cloud Exceptions")
    ws.sheet_view.showGridLines = False
    set_col_widths(ws, [10, 26, 48, 28, 14, 26, 40])

    _title(ws, 1, "MULTI-CLOUD EXCEPTIONS -- Every enterprise engagement has workloads that cannot go to the primary cloud", 7)
    _title(ws, 2, "Document ALL exceptions explicitly before the Phase 3 playback. Prevents post-recommendation disputes.", 7, bg="404040")

    hdrs = ["App ID", "Application Name", "Why It Cannot Go to Primary Cloud",
            "Recommended Alternative", "Complexity", "Commercial Impact", "Action Required"]
    for c, h in enumerate(hdrs, 1):
        _hdr(ws, 3, c, h)

    sample_rows = [
        ("APP-XXX", "[App Name]",
         "Oracle RAC workload -- OCI significantly cheaper for Oracle ULA customers",
         "Oracle OCI (for Oracle DB tier)", "Medium",
         "OCI vs Azure: model at Part 2 design phase",
         "Model OCI cost; present as optimisation option in Part 2"),
        ("APP-XXX", "[App Name]",
         "Latency-sensitive -- must be <5ms from on-prem payment gateway",
         "Retain on-premises", "N/A",
         "No cloud migration cost; on-prem running cost continues",
         "Include in Part 2 network design; review if DC exit changes topology"),
        ("APP-XXX", "[App Name]",
         "SaaS vendor data locked in AWS S3; extraction not commercially viable",
         "Retain in vendor SaaS; integrate via API from landing zone", "Low",
         "Integration cost at Part 2",
         "Scope API integration in Part 2 landing zone workstream"),
        ("APP-XXX", "[App Name]",
         "Oracle Forms -- no cloud-native equivalent; requires specialist IaaS rehost",
         "Rehost on primary cloud OR retain (assess Oracle practice)", "High",
         "Oracle practice engagement required -- cost TBD",
         "Escalate to Oracle Practice Lead; include in Phase 3 risk register"),
    ]
    bg_cycle = [WHITE, LGRAY]
    for i, row in enumerate(sample_rows):
        r = 4 + i
        bg = bg_cycle[i % 2]
        for c, val in enumerate(row, 1):
            _cell(ws, r, c, val, bg=bg, fg="000000")

    r = 9
    _title(ws, r, "COMMON EXCEPTION CHECKLIST -- Review at Phase 3 start", 7, bg=NAVY)
    checklist = [
        ("Oracle on OCI",            "Customer has Oracle workloads; OCI may be cheaper for Oracle ULA",
         "Model OCI cost; present as cost optimisation option in Part 2"),
        ("Latency-sensitive to on-prem", "App must stay <5ms from a specific on-prem system",
         "Retain on-prem; include in Part 2 network design"),
        ("Regulatory -- data residency", "Specific data must remain in-country; primary cloud lacks required region",
         "Check all three clouds for compliant regions"),
        ("SaaS vendor lock-in",      "Vendor data in their own cloud; cannot extract",
         "Retain; integrate via API from primary cloud landing zone"),
        ("Oracle Forms / legacy",    "No cloud-native equivalent; IaaS rehost minimum",
         "Rehost on primary cloud if technically possible; else Retain"),
    ]
    hdrs2 = ["Exception Type", "Example", "Action"]
    for c, h in enumerate(hdrs2, 1):
        _hdr(ws, 10, c, h)
    for c in range(4, 8):
        _cell(ws, 10, c, "", bg=RED)

    for i, (etype, example, action) in enumerate(checklist):
        r2 = 11 + i
        bg = bg_cycle[i % 2]
        _cell(ws, r2, 1, etype, bg=bg, bold=True, fg="000000")
        _cell(ws, r2, 2, example, bg=bg, fg="000000")
        _cell(ws, r2, 3, action, bg=bg, fg="444444")
        for c in range(4, 8):
            _cell(ws, r2, c, "", bg=bg)


# ── WORKED EXAMPLE ────────────────────────────────────────────────────────────
def add_worked_example(wb):
    ws = wb.create_sheet("Worked Example -- Reference")
    ws.sheet_view.showGridLines = False
    set_col_widths(ws, [32, 10, 12, 12, 12, 58])

    _title(ws, 1, "WORKED EXAMPLE -- Reference only. Do not edit. Replace with your own scoring in the Azure/AWS/GCP Scoring tabs.", 6, bg=AMBER)
    ws.cell(row=1, column=1).font = Font(name="Calibri", size=11, bold=True, color="000000")
    _title(ws, 2, "Source: Reference Engagement -- Media Sector UK (anonymised). Weights and evidence are illustrative.", 6, bg="404040")

    hdrs = ["Criterion", "Weight", "Azure Score", "AWS Score", "GCP Score", "Evidence (anonymised)"]
    for c, h in enumerate(hdrs, 1):
        _hdr(ws, 3, c, h)

    example_rows = [
        ("Total Cost of Ownership (3yr)", "30%", 8.5, 7.2, 7.8,
         "Azure optimised (3yr RI + AHB): ~39% saving vs on-prem | AWS: ~30% | GCP: ~34% -- see TCO tab"),
        ("Licensing Advantage", "20%", 9.0, 6.5, 5.0,
         "1,200+ Windows Server + 340+ SQL Server AHB-eligible; no AWS or GCP equivalent programme"),
        ("Technical Fit", "15%", 8.0, 7.5, 7.5,
         "All 3 clouds support workload types; Azure strongest for .NET/Windows stack (85% of estate)"),
        ("Regulatory & Compliance", "15%", 8.5, 8.0, 7.5,
         "All 3 hold UK data residency; Azure FCA alignment strongest for regulated media operations"),
        ("Partner Commercial (AMM/MAP/PSO)", "10%", 8.5, 7.0, 6.0,
         "AMM eligibility confirmed: estimated 800K-1.2M funded services | MAP partial | GCP PSO eligible"),
        ("Strategic Alignment", "10%", 8.0, 6.5, 6.0,
         "Existing Microsoft EA + Unified Support; no equivalent AWS/GCP enterprise agreement"),
    ]
    bg_cycle = [WHITE, LGRAY]
    for i, (crit, wt, az, aws, gcp, evid) in enumerate(example_rows):
        r = 4 + i
        bg = bg_cycle[i % 2]
        _cell(ws, r, 1, crit, bg=bg, bold=True, fg="000000")
        _cell(ws, r, 2, wt, bg=bg, align="center", fg="000000")
        _cell(ws, r, 3, az, bg=bg, align="center", fg="000000")
        _cell(ws, r, 4, aws, bg=bg, align="center", fg="000000")
        _cell(ws, r, 5, gcp, bg=bg, align="center", fg="000000")
        _cell(ws, r, 6, evid, bg=bg, fg="444444")

    r = 10
    _cell(ws, r, 1, "WEIGHTED TOTAL", bg=NAVY, bold=True)
    _cell(ws, r, 2, "", bg=NAVY)
    _cell(ws, r, 3, 8.6, bg="C6EFCE", bold=True, align="center", fg="000000")
    _cell(ws, r, 4, 7.1, bg="FFEB9C", align="center", fg="000000")
    _cell(ws, r, 5, 6.9, bg="FCE4D6", align="center", fg="000000")
    _cell(ws, r, 6, "Calculated: Score x Weight for each criterion", bg=NAVY, fg=WHITE)

    r = 11
    _cell(ws, r, 1, "RANK", bg=DGRAY, bold=True, fg="000000")
    _cell(ws, r, 2, "", bg=DGRAY)
    _cell(ws, r, 3, "1st (Primary)", bg="C6EFCE", bold=True, align="center", fg="006100")
    _cell(ws, r, 4, "2nd (Secondary)", bg="FFEB9C", align="center", fg="9C5700")
    _cell(ws, r, 5, "3rd", bg="FCE4D6", align="center", fg="9C0006")
    _cell(ws, r, 6, "", bg=DGRAY)

    r = 13
    _title(ws, r, "RECOMMENDATION (Reference)", 6, bg="C00000")
    rec_rows = [
        ("Primary Cloud", "Microsoft Azure (UK South primary / UK West DR)"),
        ("Rationale 1",   "Highest 3yr TCO saving: ~39% vs on-prem (Azure RI + AHB) vs 30% AWS, 34% GCP"),
        ("Rationale 2",   "AHB advantage: 1,200+ Windows + 340+ SQL licences eligible; estimated Xm/yr saving"),
        ("Rationale 3",   "Azure UK South holds FCA, ISO 27001, SOC 2 Type II -- required for regulated media"),
        ("Rationale 4",   "AMM eligibility confirmed: 800K-1.2M funded services available"),
        ("Rationale 5",   "Existing Microsoft EA + Unified Support -- commercial continuity for customer"),
        ("Secondary",     "AWS London (eu-west-2) for DR and batch processing workloads"),
        ("Multi-Cloud",   "4 workload exceptions -- see Multi-Cloud Exceptions tab"),
    ]
    for i, (label, val) in enumerate(rec_rows):
        r2 = 14 + i
        bg = LGRAY if i % 2 == 0 else WHITE
        _cell(ws, r2, 1, label, bg=bg, bold=True, fg="000000")
        ws.merge_cells(start_row=r2, start_column=2, end_row=r2, end_column=6)
        _cell(ws, r2, 2, val, bg=bg, fg="000000")


# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    wb = openpyxl.load_workbook(FILE)
    print(f"Loaded: {FILE}")
    print(f"Existing tabs: {wb.sheetnames}")

    # Remove existing tabs if re-running
    tabs_to_remove = [
        "Instructions", "Criteria & Weights",
        "Azure Scoring", "AWS Scoring", "GCP Scoring",
        "Weighted Summary", "7Rs Estate View",
        "Multi-Cloud Exceptions", "Worked Example -- Reference",
    ]
    for tab in tabs_to_remove:
        if tab in wb.sheetnames:
            del wb[tab]

    add_instructions(wb)
    add_criteria_weights(wb)
    add_scoring_tab(wb, "Azure Scoring", AZURE)
    add_scoring_tab(wb, "AWS Scoring", AWSOR)
    add_scoring_tab(wb, "GCP Scoring", GCPBL)
    add_weighted_summary(wb)
    add_7rs_estate_view(wb)
    add_multicloud_exceptions(wb)
    add_worked_example(wb)

    wb.save(FILE)
    print(f"Saved: {FILE}")
    print(f"Final tabs: {wb.sheetnames}")


if __name__ == "__main__":
    main()
