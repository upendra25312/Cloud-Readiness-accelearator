#!/usr/bin/env python3
"""Generates Templates/executive-reporting/part2-entry-point-template.docx from content spec."""

from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT  = os.path.join(BASE, "Templates", "executive-reporting", "part2-entry-point-template.docx")

RED   = RGBColor(0xE3, 0x1C, 0x3D)
NAVY  = RGBColor(0x1A, 0x1F, 0x36)
LGRAY = RGBColor(0xF2, 0xF2, 0xF2)
DGRAY = RGBColor(0x44, 0x44, 0x44)

# ── Helpers ────────────────────────────────────────────────────────────────────

def set_cell_bg(cell, hex_color: str):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

def cell_text(cell, text, bold=False, size=10, color=None, italic=False):
    cell.text = ""
    p = cell.paragraphs[0]
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    run.font.italic = italic
    if color:
        run.font.color.rgb = color

def heading(doc, text, level=1):
    p = doc.add_heading(text, level=level)
    p.style.font.color.rgb = RED
    for run in p.runs:
        run.font.color.rgb = RED
    return p

def body(doc, text, size=10.5, bold=False, italic=False, color=None):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.bold = bold
    run.font.italic = italic
    if color:
        run.font.color.rgb = color
    p.paragraph_format.space_after = Pt(4)
    return p

def bullet(doc, items, level=0):
    for item in items:
        p = doc.add_paragraph(item, style='List Bullet')
        p.paragraph_format.left_indent = Inches(0.25 * (level + 1))
        p.paragraph_format.space_after = Pt(2)
        for run in p.runs:
            run.font.size = Pt(10.5)

def spacer(doc, n=1):
    for _ in range(n):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.space_before = Pt(0)

def make_table(doc, headers, rows, col_widths=None, header_bg="E31C3D", alt_row=True):
    tbl = doc.add_table(rows=len(rows)+1, cols=len(headers))
    tbl.style = 'Table Grid'
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    # Header
    hrow = tbl.rows[0]
    for ci, h in enumerate(headers):
        cell = hrow.cells[ci]
        set_cell_bg(cell, header_bg)
        cell_text(cell, h, bold=True, size=9.5, color=RGBColor(0xFF,0xFF,0xFF))
    # Data rows
    for ri, row in enumerate(rows):
        trow = tbl.rows[ri+1]
        bg = "F2F2F2" if (ri % 2 == 0 and alt_row) else "FFFFFF"
        for ci, val in enumerate(row):
            cell = trow.cells[ci]
            set_cell_bg(cell, bg)
            cell_text(cell, str(val), size=9.5)
    # Col widths
    if col_widths:
        for ri in range(len(rows)+1):
            for ci, w in enumerate(col_widths):
                tbl.rows[ri].cells[ci].width = Inches(w)
    return tbl

def warning_box(doc, text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.style = 'Table Grid'
    cell = tbl.rows[0].cells[0]
    set_cell_bg(cell, "FFF3CD")
    p = cell.paragraphs[0]
    run = p.add_run(text)
    run.font.size = Pt(10)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x85, 0x64, 0x04)

def note_box(doc, text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.style = 'Table Grid'
    cell = tbl.rows[0].cells[0]
    set_cell_bg(cell, "E8F4FD")
    p = cell.paragraphs[0]
    run = p.add_run(text)
    run.font.size = Pt(10)
    run.font.italic = True
    run.font.color.rgb = NAVY

def section_banner(doc, text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.style = 'Table Grid'
    cell = tbl.rows[0].cells[0]
    set_cell_bg(cell, "E31C3D")
    p = cell.paragraphs[0]
    run = p.add_run(text)
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)

# ── Document ───────────────────────────────────────────────────────────────────

def build(doc):
    # ── Cover Page ──────────────────────────────────────────────────────────────
    doc.add_section()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("\n\n\n")

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("CLOUD READINESS ASSESSMENT")
    run.font.size = Pt(28); run.font.bold = True; run.font.color.rgb = RED

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Part 2 Entry Point")
    run.font.size = Pt(22); run.font.bold = True; run.font.color.rgb = NAVY

    spacer(doc, 2)

    cover_data = [
        ("Customer:", "[CUSTOMER LEGAL ENTITY NAME]"),
        ("Prepared By:", "[LEAD ARCHITECT NAME], Rackspace Technology"),
        ("Engagement Reference:", "[ENGAGEMENT ID / SOW REFERENCE]"),
        ("Date:", "[DD Month YYYY]"),
        ("Document Version:", "1.0"),
        ("Classification:", "Client Confidential"),
    ]
    tbl = doc.add_table(rows=len(cover_data), cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ri, (label, val) in enumerate(cover_data):
        cell_text(tbl.rows[ri].cells[0], label, bold=True, size=11)
        cell_text(tbl.rows[ri].cells[1], val, size=11)
        tbl.rows[ri].cells[0].width = Inches(2.5)
        tbl.rows[ri].cells[1].width = Inches(4.0)

    spacer(doc, 2)
    note_box(doc, "Footer on all pages: [Customer Name] — Cloud Readiness Assessment Part 2 Entry Point — Rackspace Confidential")
    doc.add_page_break()

    # ── How to Use ──────────────────────────────────────────────────────────────
    heading(doc, "How to Use This Template", level=1)
    body(doc, "This document is the authoring blueprint for the Part 2 Entry Point. Work through each section in order. Every section includes: Purpose, Required Content, Format, and a populated DMG Media UK example.")
    bullet(doc, [
        "Replace all [PLACEHOLDER] text with engagement-specific content",
        "Tables with 'TEMPLATE ROW' labels: duplicate the row for each item in your engagement",
        "Sections marked with [MANDATORY] must not be omitted — write 'TBD — [reason]' if data is incomplete",
        "Sections marked [OPTIONAL] are strongly recommended for enterprise customers",
    ])
    spacer(doc)

    # ── Section 1 ───────────────────────────────────────────────────────────────
    section_banner(doc, "SECTION 1 — EXECUTIVE SUMMARY  [MANDATORY]")
    spacer(doc)
    heading(doc, "1. Executive Summary", level=2)
    body(doc, "Purpose: Give the CTO/CFO a one-page standalone summary they can extract for their board. If they read nothing else, they read this.", italic=True)
    body(doc, "Required content (in order):", bold=True)
    bullet(doc, [
        "One-sentence engagement statement — what was assessed, by whom, over what period",
        "Estate summary — total VMs/servers, application count, DC locations assessed",
        "Recommended hyperscaler — primary + rationale in two sentences",
        "Three-year TCO summary — on-prem baseline vs. recommended cloud (net saving / net increase + %)",
        "Partner funding identified — AMM / MAP / PSO credits available (£/$ headline figure)",
        "Recommended next step — one sentence describing what Part 2 is and the proposed start date",
    ])
    body(doc, "Format: Boxed 'At a Glance' summary table + 2–3 paragraph narrative. Maximum 1 page.", italic=True, color=DGRAY)
    spacer(doc)
    make_table(doc,
        ["At a Glance", ""],
        [
            ["Organisation", "[CUSTOMER NAME]"],
            ["Assessment Period", "[Start Date] – [End Date]  ([N] weeks)"],
            ["Estate Assessed", "[N] VMs · [N] applications · [N] data centres"],
            ["Recommended Hyperscaler", "[PRIMARY CLOUD] — [REGION]"],
            ["3-Year TCO: On-Premises", "£/$ [X]"],
            ["3-Year TCO: Recommended Cloud (Optimised + Partner Funding)", "£/$ [X]  ([Y]% saving)"],
            ["Partner Funding Identified", "[AMM / MAP / PSO] — estimated £/$ [X]–[Y]"],
            ["Recommended Next Step", "[Part 2 description] — proposed start [Quarter Year]"],
        ],
        col_widths=[2.8, 4.0]
    )
    spacer(doc)
    body(doc, "Narrative (2–3 paragraphs):", bold=True)
    body(doc, "Rackspace Technology completed a Cloud Readiness Assessment of [CUSTOMER NAME]'s on-premises estate across [N] data centres from [Start Month] to [End Month] [Year]. The assessment covered [N] virtual machines, [N] Oracle RAC clusters, and approximately [N] in-scope applications.")
    spacer(doc)
    note_box(doc, "DMG Media UK example: Rackspace Technology completed a Cloud Readiness Assessment of DMG Media UK's on-premises estate across two London data centres from February to May 2026. The assessment covered 4,212 virtual machines, 18 Oracle RAC clusters, and approximately 280 in-scope applications. Primary recommendation: Microsoft Azure (UK South primary, UK West DR). Three-year TCO: On-premises status quo £18.4M. Azure (3-year RI, AHB applied) £11.2M. Net saving: £7.2M (39%) before AMM funding. Partner funding: Microsoft AMM eligibility identified — estimated £800K–£1.2M.")
    doc.add_page_break()

    # ── Section 2 ───────────────────────────────────────────────────────────────
    section_banner(doc, "SECTION 2 — SCOPE OF PART 1 ASSESSMENT  [MANDATORY]")
    spacer(doc)
    heading(doc, "2. Scope of Part 1 Assessment", level=2)

    heading(doc, "2.1 Estate Summary Table", level=3)
    make_table(doc,
        ["Category", "Count", "Notes"],
        [
            ["Virtual Machines (in scope)", "[N]", "[TEMPLATE ROW — add rows as needed]"],
            ["Physical Servers", "[N]", ""],
            ["Oracle RAC clusters", "[N]", ""],
            ["SQL Server instances", "[N]", ""],
            ["Applications profiled", "[N]", ""],
            ["Data centres / locations", "[N]", "[Location names]"],
            ["Assessment period", "[Start] – [End]", "[N] weeks"],
        ],
        col_widths=[2.8, 1.2, 2.8]
    )
    note_box(doc, "DMG Media UK example: 4,212 VMs · 18 Oracle RAC · 340+ SQL Server · 280 applications · 2 DCs (London Docklands + Sovereign House) · 16 weeks.")
    spacer(doc)

    heading(doc, "2.2 What Was Out of Scope", level=3)
    body(doc, "List any assets explicitly excluded. This prevents scope creep in Part 2 or disputes about what was and was not assessed.")
    make_table(doc,
        ["Asset / Area", "Reason Out of Scope"],
        [["[TEMPLATE ROW]", "[TEMPLATE ROW]"]],
        col_widths=[3.5, 3.3]
    )
    note_box(doc, "DMG Media UK example: Network infrastructure redesign (flagged as Part 2 workstream) · SaaS applications (separate SaaS rationalisation workstream) · DR/BC detailed design (preliminary flags only in Part 1).")
    spacer(doc)

    heading(doc, "2.3 Scope Variance Note  [MANDATORY if applicable]", level=3)
    warning_box(doc, "MANDATORY — If scope grew during the engagement, document it here to protect Part 2 commercial baseline.")
    spacer(doc)
    body(doc, '"The original SOW estimated [N] in-scope VMs. Final assessed estate was [N] VMs — a [X]% variance. This variance was managed through [agreed mechanism: change control / extended timeline / additional resource]. The Part 2 SOW should be scoped against the final assessed figure of [N] VMs."')
    note_box(doc, "DMG Media UK example: Original SOW: 2,700 VMs. Final estate: 4,212 VMs. 57% variance. Managed through phased scope expansion with customer approval. Part 2 SOW must be scoped at 4,212 VMs.")
    doc.add_page_break()

    # ── Section 3 ───────────────────────────────────────────────────────────────
    section_banner(doc, "SECTION 3 — HYPERSCALER RECOMMENDATION  [MANDATORY]")
    spacer(doc)
    heading(doc, "3. Hyperscaler Recommendation", level=2)
    warning_box(doc, "Evidence before recommendation — always show the data first. Section 3.1 (scoring table) must come before Section 3.2 (recommendation rationale).")
    spacer(doc)

    heading(doc, "3.1 Hyperscaler Scoring Summary", level=3)
    make_table(doc,
        ["Evaluation Criterion", "Weighting", "Azure", "AWS", "GCP", "Notes"],
        [
            ["TCO (3-year, primary workloads)", "[X]%", "[Score/10]", "[Score/10]", "[Score/10]", "[TEMPLATE ROW]"],
            ["Licensing advantage (AHB / BYOL)", "[X]%", "", "", "", ""],
            ["Regulatory compliance posture", "[X]%", "", "", "", ""],
            ["Partner commercial (AMM / MAP / PSO)", "[X]%", "", "", "", ""],
            ["Technical fit (workload types)", "[X]%", "", "", "", ""],
            ["Strategic alignment (enterprise agreements)", "[X]%", "", "", "", ""],
            ["WEIGHTED TOTAL", "100%", "[Score]", "[Score]", "[Score]", ""],
            ["RECOMMENDATION", "", "[PRIMARY]", "Secondary", "Tertiary", ""],
        ],
        col_widths=[3.0, 1.2, 0.9, 0.9, 0.9, 1.8]
    )
    spacer(doc)

    heading(doc, "3.2 Recommendation Rationale", level=3)
    body(doc, "Write 3–5 bullet points, each citing a specific data point from the assessment. Use the structure below:")
    bullet(doc, [
        "Cost: \"[Primary cloud] TCO over 3 years is [£/$X] vs. on-prem [£/$Y] — a [Z]% saving, driven by [AHB / RI pricing / licensing overlay].\"",
        "Licensing: \"[N] SQL Server licences eligible for AHB — saving [£/$X] vs. PAYG. [N] Oracle workloads [recommended migration path].\"",
        "Compliance: \"[Primary cloud] holds [specific certifications relevant to sector] required for [specific regulatory obligation].\"",
        "Partner funding: \"[AMM / MAP / PSO] funding eligibility identified — estimated [£/$X] available.\"",
        "Strategic: \"[Primary cloud] aligns to existing [enterprise agreement / support contract / roadmap commitment].\"",
    ])
    spacer(doc)

    heading(doc, "3.3 Multi-Cloud Exceptions", level=3)
    body(doc, "Document any workloads that cannot move to the primary cloud:")
    make_table(doc,
        ["Application / Workload", "Reason for Exception", "Recommended Cloud", "Notes"],
        [["[TEMPLATE ROW]", "[TEMPLATE ROW]", "[TEMPLATE ROW]", ""]],
        col_widths=[2.5, 2.8, 1.8, 1.7]
    )
    doc.add_page_break()

    # ── Section 4 ───────────────────────────────────────────────────────────────
    section_banner(doc, "SECTION 4 — TCO SUMMARY  [MANDATORY]")
    spacer(doc)
    heading(doc, "4. TCO Summary", level=2)
    body(doc, "Every figure must trace back to a tab in the TCO Excel model (business-case-tco-roi.xlsx).", italic=True, color=DGRAY)

    heading(doc, "4.1 Three-Year Cost Comparison", level=3)
    make_table(doc,
        ["Scenario", "Year 1", "Year 2", "Year 3", "3-Year Total", "vs. On-Prem"],
        [
            ["On-premises (status quo)", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "Baseline"],
            ["[Primary cloud] — Like-for-Like", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "[+/-X%]"],
            ["[Primary cloud] — Optimised (RI / AHB / CUD)", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "[+/-X%]"],
            ["[Primary cloud] — Optimised + Partner Credits", "£/$ [X]", "£/$ [X]", "£/$ [X]", "£/$ [X]", "[+/-X%]"],
        ],
        col_widths=[2.8, 1.2, 1.2, 1.2, 1.5, 1.0]
    )
    note_box(doc, "Note on Year 1: Year 1 includes dual-running costs (on-prem + cloud overlap during migration). See Section 4.2.")
    spacer(doc)

    heading(doc, "4.2 Year 1 Dual-Running Forecast", level=3)
    body(doc, "Year 1 is typically the most expensive year because workloads run in both environments during migration. Document this explicitly to avoid budget shock.")
    make_table(doc,
        ["Cost Component", "Amount", "Notes"],
        [
            ["On-premises costs (full year — decommission not yet complete)", "£/$ [X]", ""],
            ["Cloud costs (partial year — wave 1 + 2 migrated)", "£/$ [X]", ""],
            ["Migration tooling and licences", "£/$ [X]", ""],
            ["Professional services (Part 2)", "£/$ [X]", ""],
            ["YEAR 1 TOTAL (dual-running)", "£/$ [X]", ""],
            ["Year 1 Net (offset by AMM/MAP/PSO credits)", "£/$ [X]", ""],
        ],
        col_widths=[3.8, 1.5, 3.5]
    )
    spacer(doc)

    heading(doc, "4.3 Licensing Overlay", level=3)
    make_table(doc,
        ["Licence Type", "Volume", "Current Annual Cost", "Cloud Path", "Optimised Annual Cost", "Saving"],
        [
            ["Windows Server (AHB eligible)", "[N]", "£/$ [X]", "AHB + 3yr RI", "£/$ [X]", "£/$ [X]"],
            ["SQL Server (AHB eligible)", "[N]", "£/$ [X]", "AHB + 3yr RI", "£/$ [X]", "£/$ [X]"],
            ["Oracle (BYOL)", "[N]", "£/$ [X]", "BYOL on [VM/RDS/Exadata]", "£/$ [X]", "£/$ [X]"],
            ["[Other — TEMPLATE ROW]", "", "", "", "", ""],
            ["LICENSING TOTAL SAVING", "", "", "", "", "£/$ [X]"],
        ],
        col_widths=[2.2, 0.8, 1.5, 1.8, 1.5, 1.0]
    )
    doc.add_page_break()

    # ── Section 5 ───────────────────────────────────────────────────────────────
    section_banner(doc, "SECTION 5 — PARTNER FUNDING  [MANDATORY]")
    spacer(doc)
    heading(doc, "5. Partner Funding", level=2)
    warning_box(doc, "MANDATORY: Programme deal registration must be completed BEFORE Part 2 SOW signature. Registration after Part 2 start risks funding eligibility. Confirm with Alliance Manager before completing this section.")
    spacer(doc)

    heading(doc, "5.1 Partner Funding Summary Table", level=3)
    make_table(doc,
        ["Programme", "Provider", "Eligibility", "Estimated Value", "CRA Deliverables Required", "Status"],
        [
            ["Azure Migration and Modernisation (AMM)", "Microsoft", "[Yes/No/TBC]", "£/$ [X]–[Y]", "MRA, inventory, business case, wave plan", "[Not yet registered / Registered / Approved]"],
            ["AWS Migration Acceleration Programme (MAP)", "AWS", "[Yes/No/TBC]", "£/$ [X]–[Y]", "MRA, inventory, business case, wave plan", "[Not yet registered / Registered / Approved]"],
            ["Google Cloud RAMP / PSO", "Google", "[Yes/No/TBC]", "£/$ [X]–[Y]", "GCAF assessment, discovery export, opportunity registration", "[Not yet registered / Registered / Approved]"],
        ],
        col_widths=[2.0, 1.0, 1.0, 1.2, 2.5, 1.1]
    )
    spacer(doc)

    heading(doc, "5.2 AMM Pre-Qualification Checklist  [if Azure primary]", level=3)
    make_table(doc,
        ["Requirement", "Status", "Evidence"],
        [
            ["Migration Readiness Assessment (MRA) complete", "[ ] / [x]", "CRA Phase 2 output"],
            ["Validated infrastructure inventory", "[ ] / [x]", "Templates/01-discovery/"],
            ["Business case with 3-year TCO", "[ ] / [x]", "Templates/03-evaluation/business-case-tco-roi.xlsx"],
            ["Migration wave plan (high level)", "[ ] / [x]", "Templates/04-planning/migration-wave-planner.xlsx"],
            ["Azure as primary or co-primary cloud", "[ ] / [x]", "Hyperscaler recommendation"],
            ["Rackspace registered in MSPP as Delivery Partner", "[ ] / [x]", "Rackspace Alliance Manager to confirm"],
        ],
        col_widths=[4.0, 1.2, 3.6]
    )
    doc.add_page_break()

    # ── Section 6 ───────────────────────────────────────────────────────────────
    section_banner(doc, "SECTION 6 — MIGRATION APPROACH (HIGH LEVEL)  [MANDATORY]")
    spacer(doc)
    heading(doc, "6. Migration Approach — High Level", level=2)

    heading(doc, "6.1 Recommended Migration Approach", level=3)
    make_table(doc,
        ["Phase", "Workloads", "Approach", "Target Completion"],
        [
            ["Wave 0 — Proof of Concept", "[N] VMs — [lowest risk workloads]", "Rehost — IaaS lift-and-shift", "[Month Year]"],
            ["Wave 1 — Core Infrastructure", "[N] VMs — [dev/test, non-critical]", "Rehost — IaaS", "[Month Year]"],
            ["Wave 2 — Business Applications", "[N] VMs — [business apps, mid-tier]", "Rehost / Replatform", "[Month Year]"],
            ["Wave 3 — Tier-1 / Production", "[N] VMs — [prod, customer-facing]", "Rehost with optimisation", "[Month Year]"],
            ["Wave 4 — Oracle / Complex", "[N] nodes — [Oracle RAC, legacy]", "Replatform / Rearchitect", "[Month Year]"],
            ["Wave 5 — Decommission On-Prem", "All", "DC exit", "[Month Year]"],
        ],
        col_widths=[2.0, 2.5, 2.5, 1.8]
    )
    note_box(doc, "Wave plan above is indicative. Part 2 will produce a detailed wave plan with application-level sequencing, dependency management, and cutover windows.")
    spacer(doc)

    heading(doc, "6.2 7Rs Estate View — High Level", level=3)
    make_table(doc,
        ["Migration Pattern", "Est. VM / App Count", "Notes"],
        [
            ["Rehost (lift-and-shift)", "[N]  ([X]%)", "Majority of estate — low complexity"],
            ["Replatform", "[N]  ([X]%)", "PaaS-eligible (SQL to managed service, etc.)"],
            ["Rearchitect / Refactor", "[N]  ([X]%)", "Greenfield rebuild or containerisation candidates"],
            ["Repurchase (SaaS)", "[N]", "Replace with SaaS equivalent"],
            ["Retire", "[N]", "Confirmed decommission — do not migrate"],
            ["Retain", "[N]", "Cannot migrate — regulatory / latency / dependency"],
            ["Relocate", "[N]", "Move to different DC without cloud migration"],
        ],
        col_widths=[2.5, 2.0, 4.3]
    )
    doc.add_page_break()

    # ── Section 7 ───────────────────────────────────────────────────────────────
    section_banner(doc, "SECTION 7 — RISK REGISTER (SUMMARY)  [MANDATORY]")
    spacer(doc)
    heading(doc, "7. Risk Register — Summary", level=2)
    body(doc, "Document the top risks identified in Part 1 so Part 2 has a risk baseline. Do not defer to Part 2 — risks identified now reduce surprises later.")
    make_table(doc,
        ["#", "Risk", "Category", "Likelihood", "Impact", "Mitigation"],
        [
            ["1", "Oracle licensing cost overrun — BYOL complexity", "Licensing", "[H/M/L]", "[H/M/L]", "[Action]"],
            ["2", "Network redesign delays wave 1", "Technical", "", "", ""],
            ["3", "Scope variance from additional discovery", "Commercial", "", "", ""],
            ["4", "CAB approval lead time for firewall changes", "Operational", "", "", ""],
            ["5", "[TEMPLATE ROW]", "", "", "", ""],
        ],
        col_widths=[0.3, 2.8, 1.5, 1.1, 1.0, 2.1]
    )
    note_box(doc, "DMG Media UK top risks: (1) Oracle RAC decommission — 18 clusters — BYOL path modelled, Oracle account team engaged. (2) Scope variance risk — estate grew 57% in Part 1 — scope gate added at Part 2 SOW. (3) Redis OSS licence change — 140+ instances — Redis Enterprise Ltd commercial negotiation parallel-tracked. (4) EoL OS (Windows 2012, RHEL 6) — 340+ servers — ESU cost modelled, upgrade wave prioritised. (5) CAB approval lead time 5–10 business days per firewall change — CAB pre-engagement initiated in week 1 of Part 2.")
    doc.add_page_break()

    # ── Section 8 ───────────────────────────────────────────────────────────────
    section_banner(doc, "SECTION 8 — ORACLE MODERNISATION  [OPTIONAL — include if Oracle in estate]")
    spacer(doc)
    heading(doc, "8. Oracle Modernisation", level=2)
    body(doc, "Oracle is frequently the highest-risk and highest-cost element of any migration. A named section prevents it from being buried in the wave plan.", italic=True)

    heading(doc, "8.1 Oracle Estate Summary", level=3)
    make_table(doc,
        ["Workload", "Version", "Licence Model", "VM / Node Count", "Recommended Path", "Est. Annual Saving"],
        [
            ["Oracle RAC", "[version]", "BYOL (Processor)", "[N nodes]", "Oracle DB on dedicated VM hosts (BYOL) — evaluate OCI in 24 months", "£/$ [X]"],
            ["Oracle SE / EE standalone", "[version]", "BYOL", "[N]", "Rehost BYOL on [Azure / AWS / GCP]", "£/$ [X]"],
            ["Oracle Forms / E-Business Suite", "[version]", "BYOL", "[N]", "Rehost IaaS — no PaaS alternative at scale", "N/A"],
            ["[TEMPLATE ROW]", "", "", "", "", ""],
        ],
        col_widths=[1.5, 0.9, 1.3, 1.1, 2.5, 1.5]
    )
    spacer(doc)

    heading(doc, "8.2 Oracle Licensing Flags", level=3)
    bullet(doc, [
        "[ ] Is Oracle licensing currently processor-based or NUP? (affects cloud core count)",
        "[ ] Does the customer have an Oracle Unlimited Licence Agreement (ULA)?",
        "[ ] Are any workloads eligible for Oracle database service inclusion in OCI? (changes hyperscaler recommendation)",
        "[ ] Has the customer engaged Oracle account management on cloud migration intent?",
    ])
    warning_box(doc, "Rackspace Oracle practice note: Engage the Rackspace Oracle DBA practice before committing Oracle licensing recommendations to the Part 2 SOW. Oracle licensing in the cloud has non-obvious traps (VMware soft-partitioning, cloud vCPU multipliers) that require specialist review.")
    doc.add_page_break()

    # ── Section 9 ───────────────────────────────────────────────────────────────
    section_banner(doc, "SECTION 9 — PART 2 ENGAGEMENT MODEL  [MANDATORY]")
    spacer(doc)
    heading(doc, "9. Part 2 Engagement Model", level=2)

    heading(doc, "9.1 What Part 2 Delivers", level=3)
    make_table(doc,
        ["Deliverable", "Description", "Format"],
        [
            ["Detailed migration wave plan", "Application-level sequencing with dependencies, cutover windows, rollback plans", "Excel + PPTX"],
            ["Architecture blueprints", "Landing zone design, network topology, IAM model for [primary cloud]", "Visio / draw.io + DOCX"],
            ["Migration runbooks", "Wave-level runbooks for Rehost migrations; application-specific for complex workloads", "DOCX"],
            ["Oracle migration plan", "Detailed Oracle estate migration path with licensing confirmation", "DOCX"],
            ["Governance framework", "Operating model for cloud-first operations post-migration", "DOCX"],
            ["Programme governance", "Programme board, weekly reporting, RAID log, change control", "Ongoing"],
            ["[Additional — TEMPLATE ROW]", "", ""],
        ],
        col_widths=[2.5, 4.0, 1.3]
    )
    spacer(doc)

    heading(doc, "9.2 Indicative Timeline", level=3)
    make_table(doc,
        ["Phase", "Duration", "Activities"],
        [
            ["Foundation", "Weeks 1–4", "Landing zone build, tooling deployment, Wave 0 PoC"],
            ["Wave 1", "Weeks 5–12", "Dev/test + non-critical workloads"],
            ["Wave 2", "Weeks 13–20", "Business applications"],
            ["Wave 3", "Weeks 21–32", "Tier-1 / production"],
            ["Wave 4", "Weeks 33–44", "Oracle / complex workloads"],
            ["DC Exit", "Weeks 45–52", "Decommission on-prem, final validation"],
        ],
        col_widths=[1.8, 1.5, 5.5]
    )
    note_box(doc, "Timeline is indicative and based on [N] VMs and [N] waves. Actual timeline confirmed at Part 2 kick-off after detailed wave planning.")
    spacer(doc)

    heading(doc, "9.3 Investment Summary", level=3)
    make_table(doc,
        ["Component", "Indicative Range", "Basis"],
        [
            ["Professional services (Rackspace Part 2 delivery)", "£/$ [X]–[Y]", "Per SOW"],
            ["Cloud consumption (Year 1 — post-migration)", "£/$ [X]–[Y]", "Per TCO model"],
            ["Migration tooling (licences)", "£/$ [X]–[Y]", ""],
            ["AMM / MAP / PSO funding offset", "(£/$ [X]–[Y])", "Subject to programme approval"],
            ["NET YEAR 1 INVESTMENT", "£/$ [X]–[Y]", "After partner funding"],
        ],
        col_widths=[3.5, 2.0, 3.3]
    )
    doc.add_page_break()

    # ── Section 10 ──────────────────────────────────────────────────────────────
    section_banner(doc, "SECTION 10 — NEXT STEPS  [MANDATORY]")
    spacer(doc)
    heading(doc, "10. Next Steps", level=2)
    body(doc, "The customer must leave this document knowing exactly what happens next and who does what.")
    make_table(doc,
        ["#", "Action", "Owner", "Target Date"],
        [
            ["1", "Customer sign-off on Part 2 Entry Point", "[Customer sponsor name]", "[DD Month YYYY]"],
            ["2", "Rackspace issues Part 2 SOW for review", "Rackspace Delivery Manager", "[DD Month YYYY]"],
            ["3", "AMM / MAP / PSO deal registration", "Rackspace Alliance Manager", "Before SOW signature"],
            ["4", "Part 2 kick-off meeting (SAs + customer architects)", "[Lead Architect]", "[DD Month YYYY]"],
            ["5", "Landing zone decision confirmed (greenfield vs. existing)", "[Customer CTO / Lead Architect]", "[DD Month YYYY]"],
            ["6", "Oracle account management engagement", "[Customer Oracle owner]", "[DD Month YYYY]"],
            ["[TEMPLATE ROW]", "", "", ""],
        ],
        col_widths=[0.4, 3.8, 2.8, 1.8]
    )
    doc.add_page_break()

    # ── Document Control ─────────────────────────────────────────────────────────
    section_banner(doc, "DOCUMENT CONTROL")
    spacer(doc)
    make_table(doc,
        ["Version", "Date", "Author", "Changes"],
        [
            ["0.1", "[DD Month YYYY]", "[Lead Architect]", "Initial draft"],
            ["0.2", "[DD Month YYYY]", "[Lead Architect]", "Customer review feedback incorporated"],
            ["1.0", "[DD Month YYYY]", "[Delivery Director]", "Approved for customer presentation"],
        ],
        col_widths=[1.0, 1.8, 2.0, 4.0]
    )
    spacer(doc)

    # ── Appendix A ───────────────────────────────────────────────────────────────
    heading(doc, "Appendix A — Glossary", level=1)
    make_table(doc,
        ["Term", "Definition"],
        [
            ["AMM", "Azure Migration and Modernisation — Microsoft funded migration programme"],
            ["AHB", "Azure Hybrid Benefit — licence portability for Windows Server and SQL Server on Azure"],
            ["CRA", "Cloud Readiness Assessment — Rackspace four-phase assessment framework"],
            ["CUD", "Committed Use Discount — GCP equivalent of Reserved Instances"],
            ["L4L", "Like-for-Like — cloud sizing based on current on-prem specs without rightsizing"],
            ["MAP", "Migration Acceleration Programme — AWS funded migration programme"],
            ["MRA", "Migration Readiness Assessment — structured questionnaire required for AMM and MAP"],
            ["Part 2", "CRA Phase 2 — migration execution; follows this Entry Point document"],
            ["PSO", "Professional Services Organisation — Google Cloud delivery partner programme"],
            ["RAMP", "Rapid Assessment & Migration Program — Google structured migration programme"],
            ["RI", "Reserved Instance — pre-committed compute pricing on AWS and Azure (1yr or 3yr)"],
            ["7Rs", "Seven migration patterns: Rehost, Replatform, Rearchitect, Repurchase, Retire, Retain, Relocate"],
        ],
        col_widths=[1.2, 7.6]
    )
    spacer(doc)
    body(doc, "Content Specification: Rackspace Cloud Solutions Architecture — CRA Framework v2.0", italic=True, color=DGRAY)
    body(doc, "© 2026 Rackspace Technology. All rights reserved.", italic=True, color=DGRAY)


def main():
    doc = Document()
    # Page margins
    for section in doc.sections:
        section.top_margin    = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin   = Cm(2.5)
        section.right_margin  = Cm(2.5)
    build(doc)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    doc.save(OUT)
    print("OK  Templates/executive-reporting/part2-entry-point-template.docx")

if __name__ == "__main__":
    main()
