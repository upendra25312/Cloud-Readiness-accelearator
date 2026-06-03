#!/usr/bin/env python3
"""
CRA Presentation Generator v2 — uses the actual Rackspace PPTX template.
Template: Reports format example/DMG - CRA - Executive Summary v2 backup.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn, nsmap
from lxml import etree as LET
from lxml import etree
import copy, os

BASE     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(BASE, "Reports format example",
                        "DMG - CRA - Executive Summary v2 backup.pptx")

# ── Brand colours ──────────────────────────────────────────────────────────────
RED   = RGBColor(0xE3, 0x1C, 0x3D)
NAVY  = RGBColor(0x1A, 0x1F, 0x36)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LGRAY = RGBColor(0xF2, 0xF2, 0xF2)
DGRAY = RGBColor(0x33, 0x33, 0x33)
AZURE = RGBColor(0x00, 0x78, 0xD4)
AWSOR = RGBColor(0xFF, 0x99, 0x00)
GCPBL = RGBColor(0x42, 0x85, 0xF4)

# Layout indices in the Rackspace template
L_TITLE     = 42   # Single Column - Red  (full red left panel, content right)
L_CONTENT   = 1    # Single Column - Simple (title top, body below)
L_SUBHEAD   = 2    # Single column Simple - with subhead
L_TWO_COL   = 7    # Double Column
L_TABLE     = 9    # Table Slide
L_BREAKER   = 28   # Breaker / section divider
L_BLANK     = 5    # Blank
L_SINGLE_R  = 42   # Single Column - Red (title slides)


# ── Helper: clear all slides from a presentation ──────────────────────────────

def clear_slides(prs):
    """Remove all slides while preserving masters and layouts."""
    sldIdLst = prs.slides._sldIdLst
    slide_ids = list(sldIdLst)
    for sid in slide_ids:
        rId = sid.get(qn('r:id'))
        try:
            prs.part.drop_rel(rId)
        except Exception:
            pass
        sldIdLst.remove(sid)


# ── Helper: add slide from a layout ───────────────────────────────────────────

def add_slide(prs, layout_idx):
    layout = prs.slide_layouts[layout_idx]
    return prs.slides.add_slide(layout)


# ── Helper: set placeholder text ─────────────────────────────────────────────

def set_ph(slide, idx, text, size=None, bold=None, color=None, align=None):
    """Find placeholder by idx and set its text."""
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == idx:
            tf = ph.text_frame
            tf.clear()
            tf.word_wrap = True
            p = tf.paragraphs[0]
            run = p.add_run()
            run.text = text
            if size:
                run.font.size = Pt(size)
            if bold is not None:
                run.font.bold = bold
            if color:
                run.font.color.rgb = color
            if align:
                p.alignment = align
            return ph
    return None


def set_ph_bullets(slide, idx, bullets, size=None, bold_first=False):
    """Set placeholder with multiple bullet lines."""
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == idx:
            tf = ph.text_frame
            tf.clear()
            tf.word_wrap = True
            for i, line in enumerate(bullets):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                run = p.add_run()
                run.text = line
                if size:
                    run.font.size = Pt(size)
                if bold_first and i == 0:
                    run.font.bold = True
                p.space_after = Pt(3)
            return ph
    return None


def add_table_to_ph(slide, ph_idx, headers, rows, col_widths=None):
    """Replace a placeholder with a table."""
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == ph_idx:
            # Get position and size from placeholder
            x, y, cx, cy = ph.left, ph.top, ph.width, ph.height
            # Remove placeholder from slide
            sp = ph._element
            sp.getparent().remove(sp)
            # Add table shape
            ncols = len(headers)
            nrows = len(rows) + 1
            tbl_shape = slide.shapes.add_table(nrows, ncols, x, y, cx, cy)
            tbl = tbl_shape.table
            # Set col widths
            if col_widths:
                total = sum(col_widths)
                for ci, cw in enumerate(col_widths):
                    tbl.columns[ci].width = int(cx * cw / total)
            # Header row
            for ci, h in enumerate(headers):
                cell = tbl.cell(0, ci)
                cell.text = h
                _set_cell_color(cell, "E31C3D")
                p = cell.text_frame.paragraphs[0]
                for run in p.runs:
                    run.font.bold = True
                    run.font.size = Pt(12)
                    run.font.color.rgb = WHITE
            # Data rows
            for ri, row in enumerate(rows):
                bg = "F2F2F2" if ri % 2 == 0 else "FFFFFF"
                for ci, val in enumerate(row):
                    cell = tbl.cell(ri + 1, ci)
                    cell.text = str(val)
                    _set_cell_color(cell, bg)
                    p = cell.text_frame.paragraphs[0]
                    for run in p.runs:
                        run.font.size = Pt(11)
            return tbl_shape
    return None


def _set_cell_color(cell, hex_color):
    """Set table cell background color using OOXML."""
    tc = cell._tc
    tcPr = tc.find(qn('a:tcPr'))
    if tcPr is None:
        tcPr = LET.SubElement(tc, qn('a:tcPr'))
    # Remove existing solidFill if any
    for sf in tcPr.findall(qn('a:solidFill')):
        tcPr.remove(sf)
    # Insert new solidFill before other children
    solidFill = LET.SubElement(tcPr, qn('a:solidFill'))
    srgbClr = LET.SubElement(solidFill, qn('a:srgbClr'))
    srgbClr.set('val', hex_color)
    # Move solidFill to first position
    tcPr.remove(solidFill)
    tcPr.insert(0, solidFill)


# ── Slide builders ─────────────────────────────────────────────────────────────

def title_slide(prs, title, subtitle, meta=""):
    """Title slide using L_TITLE (red) layout."""
    slide = add_slide(prs, L_TITLE)
    # Layout 42 has: idx=0 (Title, left red panel), idx=12 (Body, right panel), idx=13 (subtext)
    set_ph(slide, 0, title, size=36, bold=True, color=WHITE)
    if subtitle:
        set_ph(slide, 12, subtitle, size=20, color=WHITE)
    if meta:
        set_ph(slide, 13, meta, size=14, color=RGBColor(0xFF, 0xCC, 0xCC))
    return slide


def content_slide(prs, title, bullets, subhead=None):
    """Content slide with title and bullet list."""
    if subhead:
        slide = add_slide(prs, L_SUBHEAD)
        set_ph(slide, 13, subhead, size=14, bold=True, color=RED)
    else:
        slide = add_slide(prs, L_CONTENT)
    # Layout 1/2: idx=0 (Title), idx=12 (Body)
    set_ph(slide, 0, title, size=24, bold=True)
    if bullets:
        set_ph_bullets(slide, 12, bullets, size=14)
    return slide


def two_col_slide(prs, title, left_head, left_items, right_head, right_items):
    """Two-column slide using Layout 7."""
    slide = add_slide(prs, L_TWO_COL)
    # Layout 7: idx=0 (Title), idx=12 (left body), idx=1 (right body), idx=13 (far-left icon area)
    set_ph(slide, 0, title, size=24, bold=True)
    left_content = ([left_head + ":"] if left_head else []) + left_items
    right_content = ([right_head + ":"] if right_head else []) + right_items
    set_ph_bullets(slide, 12, left_content, size=13, bold_first=bool(left_head))
    set_ph_bullets(slide, 1, right_content, size=13, bold_first=bool(right_head))
    return slide


def table_slide(prs, title, headers, rows, col_widths=None, intro=None):
    """Table slide using Layout 9."""
    slide = add_slide(prs, L_TABLE)
    # Layout 9: idx=0 (Title), idx=12 (right — where table goes), idx=13 (left callout)
    set_ph(slide, 0, title, size=22, bold=True)
    if intro:
        set_ph(slide, 13, intro, size=13, color=DGRAY)
    # Add table into the idx=12 placeholder area
    add_table_to_ph(slide, 12, headers, rows, col_widths)
    return slide


def breaker_slide(prs, title, subtitle=""):
    """Section break slide using Layout 28."""
    slide = add_slide(prs, L_BREAKER)
    # Layout 28: idx=16 (large title body), idx=18 (subtitle)
    set_ph(slide, 16, title, size=32, bold=True, color=WHITE)
    if subtitle:
        set_ph(slide, 18, subtitle, size=18, color=RGBColor(0xFF, 0xCC, 0xCC))
    return slide


# ── Deck definitions ───────────────────────────────────────────────────────────

def build_leadership(prs):
    title_slide(prs, "Cloud Readiness Accelerator",
        "A practitioner-grade framework for delivering cloud readiness assessments at scale",
        "Cloud Solutions Architecture  |  Internal Leadership Briefing  |  2026")

    content_slide(prs, "Every CRA engagement starts from scratch — and it costs us", [
        "Delivery teams spend 3–6 weeks scoping and building templates before an assessment even starts",
        "Inconsistent outputs across engagements create QA risk and weaken partner trust",
        "Customers get a free 15-minute Azure check from Microsoft — we must compete on depth, not speed",
        "",
        "\"Without a standardised framework, we win deals on relationships and lose renewals on quality.\"",
    ])

    table_slide(prs, "The window is open now",
        ["Signal", "What It Means for Rackspace"],
        [
            ["70% of enterprises accelerating cloud migration post-2024", "High inbound demand for formal readiness assessments"],
            ["Average CRA deal size: $250K–$1.5M", "Premium revenue per engagement"],
            ["Microsoft / AWS / GCP all have FREE 15-min tools", "We must differentiate on depth, deliverables, and alliance leverage"],
            ["Customers cite 'lack of internal capability' as #1 migration barrier", "CRA directly addresses the most cited blocker"],
            ["Alliance partners reward assessment-led deal creation", "Every CRA engagement is a co-sell opportunity"],
        ],
        intro="$10M+ revenue influence potential in Year 1 — 15 engagements x $650K average deal size"
    )

    two_col_slide(prs, "A complete, reusable toolkit — not a methodology document",
        "What it includes", [
            "Four-phase methodology (Discovery to Analysis to Evaluation to Planning)",
            "30+ reusable templates (Excel, Word, PPTX) for every deliverable",
            "TCO models validated against real customer data (AWS, Azure, GCP)",
            "Hyperscaler decision matrix — vendor-neutral, board-grade",
            "Reference case study: DMG Media UK (4,200+ VMs, Azure + AMM funding)",
            "Alliance alignment guides (Microsoft CAF, AWS MAP, GCP PSO)"
        ],
        "What it replaces", [
            "6–8 weeks of custom scoping and template-building",
            "Inconsistent outputs across delivery teams",
            "Architect-dependent tribal knowledge",
            "Missed AMM / MAP funding opportunities",
            "",
            "Result: 30%+ reduction in delivery time. Consistent, auditable outputs."
        ])

    content_slide(prs, "Structured, repeatable, end-to-end — four phases", [
        "DISCOVERY (7 weeks): Application inventory · Infrastructure profiling · Dependency mapping",
        "ANALYSIS (4 weeks): 5-dimension readiness scoring · Gap identification · Cloud maturity assessment",
        "EVALUATION (3 weeks): TCO modelling (AWS/Azure/GCP) · Hyperscaler decision matrix · Business case",
        "PLANNING (6 weeks): Migration waves · Risk register · Governance model · Part 2 entry point",
        "",
        "Total: 16–20 weeks parallelised (mid-market). Scales to 200+ applications.",
        "4,212 VMs discovered in Phase 1 (DMG Media UK)  |  57% scope variance identified  |  AMM funding unlocked"
    ])

    table_slide(prs, "Microsoft SMART and Rackspace CRA serve different moments",
        ["Microsoft SMART Assessment", "Rackspace CRA"],
        [
            ["Free, self-service", "Formal engagement, deliverable-based"],
            ["15 minutes", "16–20 weeks"],
            ["Azure only", "AWS + Azure + GCP"],
            ["No deliverable", "30–50 page assessment report"],
            ["Pre-sales screening", "Board / CIO sign-off document"],
            ["No AMM eligibility", "CRA outputs satisfy AMM requirements"],
        ],
        intro="SMART generates the lead. CRA converts it to revenue."
    )

    content_slide(prs, "One engagement. Every phase. Real numbers. — DMG Media UK", [
        "DMG Media UK (Daily Mail Group Trust) — UK's largest digital media group",
        "On-premises VMware estate, 2 UK data centres, 10 vCenter instances",
        "",
        "4,212 VMs discovered  |  +57% above SoW scope",
        "3-way evaluation: Azure vs AWS vs GCP across 9 regions",
        "Azure recommended: UK South primary  |  AMM funding identified",
        "",
        "Framework lessons embedded from this engagement:",
        "Scope validation worksheet · Legacy OS discovery · AMM pre-engagement checklist · Oracle RAC migration path"
    ])

    content_slide(prs, "The numbers that matter to leadership", [
        "30% FASTER — assessment delivery vs. custom-built engagement",
        "$10M+ INFLUENCED REVENUE — in Year 1  (15 engagements x $650K avg)",
        "3 ALLIANCE PROGRAMMES — Microsoft AMM + AWS MAP + Google PSO funding eligible",
        "",
        "NPS target: >70  |  30+ templates reused across engagements  |  8+ co-sell deals Year 1",
        "",
        "Investment to finish remaining 37%: ~$80K–$120K fully loaded",
        "(0.5 FTE x 12 weeks + writer + designer)",
        "Expected return: $10M+ influenced revenue — 80–100x ROI"
    ])

    table_slide(prs, "Built to fund, not just deliver — Alliance Partner Alignment",
        ["Partner", "CRA Alignment"],
        [
            ["Microsoft Azure (CAF/AMM)", "CRA phases map to CAF stages · TCO satisfies AMM deliverable requirements · AHB modelled · Pre-engagement AMM checklist"],
            ["AWS (MAP)", "CRA Assessment maps to MAP Assess · Inventory + readiness scoring satisfy MAP deal registration · TCO: On-Demand, 3yr RI, Savings Plans"],
            ["Google Cloud (PSO/RAMP)", "Discovery aligns to Migration Center inputs · GCP TCO across 3 regions (On-Demand + CUDs) · RAMP programme alignment"],
        ],
        intro="Every CRA engagement is a potential AMM, MAP, or PSO funding conversation. CRA makes this systematic."
    )

    content_slide(prs, "Roadmap — where we are, where we go next", [
        "PHASE 1: FOUNDATION — COMPLETE",
        "  Repo structured · 30+ templates · DMG Media UK case study · README rewritten · v1.0 published",
        "",
        "PHASE 2: ENHANCEMENT — IN PROGRESS",
        "  Template content audit (4A–4E) · Leadership and executive presentation decks",
        "  Microsoft CAF + AWS MAP + GCP PSO alignment docs · Branding applied",
        "",
        "PHASE 3: SCALE — PLANNED",
        "  Internal SA team training · SharePoint library · AMM programme submission · Alliance go-to-market",
        "",
        "Current status: 63% complete. On track for Release 1.1."
    ])

    content_slide(prs, "Three asks. Twelve weeks. $10M+ return.", [
        "1. RESOURCE COMMITMENT",
        "   0.5 FTE Cloud Solutions Architect for 12 weeks  +  0.1 FTE Technical Writer for 8 weeks",
        "   Estimated fully loaded cost: $80K–$120K",
        "",
        "2. EXECUTIVE SPONSORSHIP",
        "   VP or Director level sponsor for partner conversations with Microsoft, AWS, and Google",
        "   One internal leadership session to validate framework before external sharing",
        "",
        "3. GO-TO-MARKET ACTIVATION",
        "   Approval to share with Microsoft UK and AWS UK partner managers",
        "   (subject to legal review of DMG Media UK case study — in progress)",
        "",
        "Investment: ~$100K.  Return: $10M+ influenced revenue in Year 1.  100x ROI."
    ])

    table_slide(prs, "Next steps — decisions needed today",
        ["Action", "Owner", "When"],
        [
            ["Confirm 0.5 FTE architect commitment for Weeks 5–12", "[VP/Director Name]", "This meeting"],
            ["Identify executive sponsor for Microsoft/AWS co-sell conversations", "[VP Name]", "This week"],
            ["Initiate legal review of DMG Media UK case study", "Legal / [Name]", "This week"],
        ],
        intro="\"The framework exists. The methodology is proven. The case study is real. The only question is whether we resource it to scale.\""
    )


def build_executive(prs):
    title_slide(prs, "Cloud Readiness Assessment",
        "A structured path to a confident, evidence-based cloud migration decision",
        "Rackspace Cloud Solutions Architecture  |  [Customer Name]  |  [Date]")

    content_slide(prs, "Moving to cloud is not the hard part — deciding which cloud, when, and at what cost is", [
        "TOO MANY OPINIONS: Every hyperscaler says they are the best choice. Without independent analysis, the loudest voice wins.",
        "",
        "COMPLEXITY YOU CANNOT SEE: Oracle databases, end-of-life OS, licensing obligations, and infrastructure dependencies only visible once you look. Most cloud cost estimates start before the data is collected.",
        "",
        "THE COST OF GETTING IT WRONG: Organisations without a formal assessment overspend by 30–60% in Year 1.",
        "",
        "\"A cloud migration decision is a board-level financial commitment of £1M–£10M+. It deserves the same rigour as any capital investment.\"",
    ])

    table_slide(prs, "A CRA is a decision-making system, not a report",
        ["Deliverable", "Purpose"],
        [
            ["Infrastructure & Application Inventory", "Definitive record of your estate — scope, complexity, dependencies"],
            ["Cloud Readiness Scores", "Per-application traffic-light readiness rating"],
            ["Total Cost of Ownership (TCO) Analysis", "7-layer financial model covering all cost scenarios"],
            ["Hyperscaler Evaluation", "Scored comparison: AWS vs Azure vs GCP for your specific estate"],
            ["Hyperscaler Recommendation", "Evidence-based recommendation with financial justification"],
            ["Risk Register", "Technical, licensing, and delivery risks identified and scored"],
            ["Migration Wave Plan", "Sequenced application migration roadmap"],
            ["Part 2 Entry Point", "Commercial document that initiates the migration engagement"],
        ],
        intro="Four phases · 16–20 weeks · Uses proven tooling · Fully cloud-neutral recommendation"
    )

    two_col_slide(prs, "The difference is independence — and the ability to unlock partner funding",
        "Independence", [
            "Rackspace has no hyperscaler revenue target",
            "Our recommendation is based entirely on your data",
            "We have delivered assessments recommending all three hyperscalers",
            "If AWS is the right answer, we recommend AWS",
        ],
        "Partner Funding", [
            "Qualified partner for Microsoft AMM, AWS MAP, and Google PSO",
            "A correctly documented CRA can unlock £100K–£1M+ in partner funding",
            "We identify funding eligibility as part of the assessment — at no extra cost",
            "",
            "\"A Rackspace CRA pays for itself when partner funding is identified.\"",
        ])

    content_slide(prs, "Four phases. Structured gates. No guesswork.", [
        "PHASE 1: DISCOVERY (7 weeks): Deploy tooling · Collect VM, app, storage & network data · Map app dependencies",
        "PHASE 2: ANALYSIS (4 weeks, starts at Phase 1 Week 6): Score each app across 5 cloud readiness dimensions",
        "PHASE 3: EVALUATION (3 weeks): Model TCO for all 3 clouds · Evaluate all 3 hyperscalers · Produce recommendation",
        "  GATE 2: Alliance partner deal registration complete before Part 2 SOW",
        "PHASE 4: PLANNING (6 weeks): Build migration waves · Define risk register · Finalise Part 2 Entry Point",
        "",
        "GATE 1 (hard): >=14 days clean utilisation data required before Phase 3 can begin",
        "Total: 16–20 weeks for mid-market estates (200–500 applications)",
    ])

    table_slide(prs, "Phase 3 — A 7-layer cost model you can present to your board",
        ["Layer", "What It Models", "Why It Matters"],
        [
            ["(a) Like-for-Like Baseline", "Exact current specification, lifted to cloud", "Starting point — cost of doing nothing extra"],
            ["(b) Optimised / Right-Sized", "Cloud-right-sized instances (P95 utilisation data)", "Typically 20–35% lower than like-for-like"],
            ["(c) Delta (b minus a)", "Financial benefit of right-sizing alone", "Headline 'cloud saving' number"],
            ["(d) Licensing Overlay", "SQL Server AHB, Oracle BYOL, Windows AHB", "Often the single largest cost item in Microsoft-heavy estates"],
            ["(e) On-Premises Status Quo", "Current hardware + maintenance + facilities (3yr)", "Establishes true cost of staying on-premises"],
            ["(f) Year 1 Dual-Running", "Cloud costs + remaining on-prem during overlap", "Prevents 'it cost more in Year 1 than expected' problem"],
            ["(g) Partner Discounts & Credits", "AMM / MAP / PSO funding applied", "Net cost after partner funding — the board-level headline"],
        ],
        intro="Most cloud cost estimates only cover 2 of these 7 layers. Difference between layers (a) and (g) is typically 40–60% for a Microsoft-heavy estate with AMM funding."
    )

    content_slide(prs, "Phase 3 — How we choose the right cloud for your estate", [
        "\"The recommendation follows the evidence. We do not start with a preferred cloud and build a case for it.\"",
        "",
        "Evaluation criteria — agreed with you BEFORE scoring begins:",
        "  Technical compatibility with your estate",
        "  3-year Total Cost of Ownership",
        "  Regulatory and compliance fit",
        "  Azure Hybrid Benefit / licensing optimisation",
        "  Migration complexity and tooling",
        "  Hyperscaler roadmap and services",
        "",
        "All three hyperscalers are scored — we never eliminate options before the evidence is presented.",
        "The recommendation slide comes AFTER the evidence slides — never before.",
    ])

    table_slide(prs, "Eight formal deliverables — all board-grade",
        ["#", "Deliverable", "Format", "Phase"],
        [
            ["1", "Application & Infrastructure Inventory", "Excel workbooks (3 files)", "Phase 1"],
            ["2", "Phase 1 Discovery Report", "Word document, 20–30 pages", "Phase 1"],
            ["3", "Cloud Readiness Scores", "Excel workbook", "Phase 2"],
            ["4", "Governance Maturity Assessment", "Excel + workshop summary", "Phase 2"],
            ["5", "TCO Analysis — All 7 Layers", "Excel workbook (per hyperscaler)", "Phase 3"],
            ["6", "Cloud Readiness Assessment Report", "Word document, 40–60 pages", "Phase 3"],
            ["7", "Executive Summary Presentation", "PowerPoint deck, 18 slides", "Phase 3"],
            ["8", "Part 2 Entry Point (migration SOW)", "Word document, 8–12 pages", "Phase 4"],
        ]
    )

    content_slide(prs, "A reference engagement — four phases, every deliverable, a real outcome", [
        "A UK digital media group — one of the UK's largest digital publishing organisations",
        "On-premises VMware estate, 2 UK data centres",
        "",
        "Discovery:   4,200+ VMs · 280 applications · 18 Oracle RAC clusters · 57% more infrastructure than CMDB showed",
        "Analysis:    Cloud Readiness Scores for all 280 applications · Governance maturity across 6 domains",
        "Evaluation:  3-way TCO model (Azure vs AWS vs GCP) across 9 regions · Hyperscaler recommendation",
        "Planning:    Partner funding identified and pre-registered · Migration wave plan produced",
        "",
        "\"A board-ready business case, an evidence-backed hyperscaler recommendation, a migration wave plan for 280 applications, and identification of seven-figure partner funding eligibility — all within a 16-week structured engagement.\"",
    ])

    table_slide(prs, "You may be eligible for significant partner programme funding",
        ["Programme", "What It Covers", "CRA Requirement"],
        [
            ["Microsoft Azure — AMM", "Typically 10–30% of migration services cost", "Pre-registration before migration begins — CRA produces all required documentation"],
            ["AWS — MAP", "Financial assistance and technical support for migration to AWS", "ACE deal registration at engagement start — CRA Assessment maps to MAP Assess"],
            ["Google Cloud — PSO Credits / RAMP", "Migration credits against GCP consumption", "CRA outputs qualify for RAMP — opportunity registration at Phase 1"],
        ],
        intro="Partner programme eligibility confirmed by Rackspace before Part 2 SOW is signed. All applicable programmes pre-registered at Phase 1 kickoff."
    )

    table_slide(prs, "From this conversation to a signed Statement of Work",
        ["Step", "What Happens", "Timeline"],
        [
            ["Scoping Workshop", "Validate estate size · Screen for Oracle/SAP · Confirm funding eligibility · Agree timeline", "1–2 days after this meeting"],
            ["Statement of Work", "Fixed-fee SOW: agreed scope · deliverables · acceptance criteria · partner funding plan", "Within 1 week of scoping"],
            ["Phase 1 Kickoff", "Tooling deployment · CAB request submitted · Alliance Manager pre-registers · First status call", "Within 2 weeks of SOW signature"],
        ],
        intro="Ready to begin? Contact [your name] at [email] to schedule the scoping workshop."
    )

    content_slide(prs, "Next steps", [
        "Schedule a scoping workshop with Rackspace Cloud Solutions Architecture",
        "",
        "Contact: [Your Name] — [email] — Rackspace Cloud Solutions Architecture",
    ])


def build_technical(prs):
    title_slide(prs, "Cloud Readiness Accelerator — Technical Framework Overview",
        "Methodology, templates, tooling, and delivery guide for CRA practitioners",
        "Rackspace Cloud Solutions Architecture  |  CRA Framework v2.0")

    content_slide(prs, "Framework architecture — four phases, two gates, one parallelisation point", [
        "PHASE 1: DISCOVERY (Wks 1–7): Azure Migrate / GCP Migration Center / AWS ADS  ·  VM + app + network data  ·  App inventory",
        "PHASE 2: ANALYSIS (Wks 6–10): Cloud readiness scoring (5 dims) · Governance maturity · OSS licence flags",
        "PHASE 3: EVALUATION (Wks 11–14): 7-layer TCO per hyperscaler · Hyperscaler decision matrix · Recommendation",
        "PHASE 4: PLANNING (Wks 11–20): Migration wave plan · Risk register · Governance model · Part 2 Entry Point",
        "",
        "PARALLELISATION: Phase 2 starts at Phase 1 Week 6 — do NOT wait for Phase 1 to complete",
        "GATE 1 (hard): >=14 days clean utilisation data for >=90% of VMs before Phase 3",
        "GATE 2 (pre-commercial): Alliance partner deal registration COMPLETE before Part 2 SOW countersignature",
    ])

    content_slide(prs, "Phase 1 — three workstreams running simultaneously", [
        "Core objective: Complete, accurate, validated inventory with >=14 days clean CPU/RAM/storage/network utilisation data from >=90% of VMs.",
        "",
        "1. Infrastructure discovery tooling: VM specs, OS, hypervisor, utilisation data, storage I/O",
        "2. Application inventory: tech stack, DB, VM count, readiness flag, dependencies",
        "3. Dependency mapping (with app owners): dependency heat map, tightly-coupled clusters",
        "",
        "CRITICAL: Serialising these workstreams costs 4–6 weeks. Application workshops CAN start at Week 2 while tooling is collecting data.",
        "Run RVTools export on Day 1 regardless of target hyperscaler — provides instant VMware inventory for cross-validation.",
        "Submit firewall CAB request on Day 1 — can take 5–15 business days to approve in enterprise organisations.",
    ])

    table_slide(prs, "Phase 1 — discovery tooling selection",
        ["Tool", "Hyperscaler", "Deployment", "Key Output"],
        [
            ["Azure Migrate", "Azure primary", "Agent or agentless (vCenter connector)", "infrastructure-profiling.xlsx source data"],
            ["AWS ADS", "AWS primary", "Agent-based or Agentless Connector", "aws-evaluation.xlsx input"],
            ["GCP Migration Center", "GCP primary", "VM Manager agent or RVTools import", "gcp-evaluation.xlsx input"],
            ["RVTools", "All hyperscalers", "VMware utility — no agent needed", "Cross-validation of all discovery tools"],
        ]
    )

    content_slide(prs, "GATE 1 — Phase 3 cannot start without this", [
        "Utilisation data collection period: >=14 days continuous clean data",
        "VM coverage: >=90% of in-scope VMs reporting",
        "CPU data quality: P95 values available for >=90% of VMs",
        "RAM data quality: P95 values available for >=90% of VMs",
        "",
        "WHY THE GATE IS HARD:",
        "\"Using 6 days of data instead of 14 produces right-sizing recommendations with +-30-50% error. At 500 VMs, that is a £2M–£5M range in the business case — not acceptable at board level.\"",
        "",
        "When customer pushes to skip: quantify the risk in writing → offer interim (share Phase 1 report while data collection continues) → document customer's decision if they override",
    ])

    table_slide(prs, "Phase 2 — five-dimension scoring model",
        ["Dimension", "Scale", "Low Score Means"],
        [
            ["Technical Complexity", "1 (complex) – 5 (simple)", "Legacy OS, custom middleware, tightly-coupled architecture"],
            ["Business Criticality", "1 (critical) – 5 (non-critical)", "RTO < 4hrs, RPO < 1hr, zero-downtime required"],
            ["Data Sensitivity", "1 (highly sensitive) – 5 (non-sensitive)", "PII, FCA-regulated data, GDPR sovereignty constraints"],
            ["Dependency Risk", "1 (high) – 5 (low)", "Tightly-coupled dependencies, on-prem latency requirements"],
            ["Licence Risk", "1 (high risk) – 5 (low risk)", "Oracle RAC, Oracle EE, IBM ILMT, Windows without AHB, SAP"],
        ],
        intro="Composite: 4.0–5.0 = Cloud Ready  ·  3.0–3.9 = Cloud Friendly  ·  2.0–2.9 = Cloud Challenged  ·  1.0–1.9 = Blocked"
    )

    content_slide(prs, "Phase 2 — OSS licence risk: the commercial time bomb you must not miss", [
        "OSS LICENCE CHANGES (2023–2024) affecting cloud deployments:",
        "  Redis OSS (post v7.4): SSPL/RSALv2 — requires paid licence for commercial cloud use",
        "  Elasticsearch (post 7.10): SSPL — check if using elastic.co or AWS OpenSearch fork",
        "  HashiCorp Vault / Terraform: BSL — commercial use restrictions at scale",
        "  MongoDB: SSPL — validate version and applicable managed service",
        "",
        "Action trigger: ANY OSS Licence Risk Flag → immediate commercial review in Phase 2 BEFORE TCO is built",
        "A TCO model that does not include OSS re-licensing costs is incomplete and will create budget surprises.",
        "",
        "DMG Media UK: 140+ Redis instances identified. OSS flag column in the application inventory exists because of this engagement.",
    ])

    table_slide(prs, "Phase 3 — 7-layer TCO model: why each layer exists",
        ["Layer", "Tab Name", "Common Mistake"],
        [
            ["(a) Like-for-Like", "L4L-Baseline", "Using rounded estimates instead of actual P95 utilisation"],
            ["(b) Optimised", "Optimised-Rightsized", "Using P50 (median) instead of P95 — underestimates required size"],
            ["(c) Delta", "Calculated (b-a)", "Presenting this as 'the saving' without showing layers d–g"],
            ["(d) Licensing Overlay", "Licensing-Overlay", "Omitting Oracle BYOL licensing premium/saving"],
            ["(e) On-Prem Status Quo", "OnPrem-StatusQuo", "Using standard depreciation without including hardware refresh cycle"],
            ["(f) Year 1 Dual-Running", "Year1-DualRunning", "Omitting parallel environment costs (most common budget shock)"],
            ["(g) Partner Credits", "Partner-Credits", "Building the board case without this — largest headline number driver"],
        ],
        intro="Template: business-case-tco-roi.xlsx  ·  TCO-Summary tab produces board-level number: 3yr net cost (post-partner funding) vs 3yr on-prem"
    )

    content_slide(prs, "Phase 3 — Hyperscaler Decision Matrix: critical validation rules", [
        "9 required tabs: Criteria-Weights · Azure-Evaluation · AWS-Evaluation · GCP-Evaluation · Comparative-Matrix · 7Rs-Estate-View · Multi-Cloud-Exceptions · Worked-Example · Instructions",
        "",
        "CRITICAL RULES before presenting the recommendation:",
        "1. Criteria weights agreed in WRITING by customer BEFORE any scoring begins",
        "2. All three clouds scored with equal rigour — never eliminate one before matrix is complete",
        "3. Every score has a documented evidence reference — not 'expert judgment'",
        "4. Recommendation slide follows the evidence slides — NEVER precedes them",
        "5. The matrix score and the recommendation are consistent",
        "",
        "Evidence-before-recommendation is the most important quality rule in the entire framework.",
    ])

    table_slide(prs, "Phase 4 — wave sequencing principles",
        ["Wave", "Characteristics", "DO NOT include"],
        [
            ["Wave 0 (PoC, 8–12 wks)", "Non-production · 5–10% of estate · Dev/Test · simple Tier-3", "Tier-1 · SAP · Oracle RAC · business-critical"],
            ["Wave 1", "Cloud Ready · low dependency · Tier-3 · internal tools", "Tightly-coupled dependency clusters"],
            ["Wave 2", "Cloud Friendly · low-medium complexity · mid-tier", "Applications that need Wave 1 to complete first"],
            ["Wave 3", "Cloud Challenged or medium-high · custom middleware", "Tier-1 production before Wave 2 validated"],
            ["Wave 4", "Tier-1 business-critical · ERP, CRM, core business", "Only after waves 1–3 validated in production"],
            ["Wave 5+", "Retained · Oracle specialist · multi-cloud exceptions", "Force Oracle RAC to primary cloud without specialist review"],
        ]
    )

    table_slide(prs, "Nine lessons from a real engagement — embedded in the framework",
        ["#", "Lesson", "What Changed in Framework"],
        [
            ["1", "Scope variance: 57% more VMs than SoW", "Scope variance clause in SoW · confidence scoring in app inventory"],
            ["2", "CAB not submitted Day 1 → 2-week delay", "Phase 1 kickoff checklist — CAB on Day 1"],
            ["3", "Oracle RAC found Week 5 → Oracle analysis delayed Phase 3 by 6 weeks", "Oracle Practice Flag column in application inventory"],
            ["4", "Redis OSS licence change discovered in Phase 3 → TCO re-work", "OSS Licence Risk column in application inventory"],
            ["5", "AMM not pre-registered at Phase 1 → customer missed funding", "AMM registration at Phase 1 kickoff · Alliance Manager on Day 1 call"],
            ["6", "Utilisation data window shortened → TCO accuracy compromised", "Gate 1 hard requirement · written escalation process"],
            ["7", "Phase 2 not started until Phase 1 complete → 4-week delay", "Parallelisation: Phase 2 starts at Phase 1 Week 6"],
            ["8", "EoL OS not flagged until Phase 3 → ESU costs missed", "EoL OS column in infrastructure-profiling · flag in risk register"],
            ["9", "Recommendation before evidence → customer challenged credibility", "Evidence-before-recommendation rule · deck structure validation checklist"],
        ]
    )

    content_slide(prs, "Pre-playback QA checklist — 10 checks before presenting Phase 3", [
        "[ ] 1. >=14 days clean utilisation data confirmed for >=90% of VMs",
        "[ ] 2. All 7 TCO layers populated for each cloud — no blank rows",
        "[ ] 3. Pricing validated against calculator source this week",
        "[ ] 4. AHB eligibility confirmed (SA status verified with customer)",
        "[ ] 5. Oracle licensing reviewed by Oracle Practice Lead — email sign-off filed",
        "[ ] 6. OSS licence flags resolved — all modelled in TCO",
        "[ ] 7. Hyperscaler matrix weights agreed in writing by customer",
        "[ ] 8. All three clouds scored with evidence references — no blank evidence fields",
        "[ ] 9. Recommendation slide comes AFTER evidence slides (slide >=13)",
        "[ ] 10. AMM/MAP/PSO registration confirmed by Alliance Manager — email filed",
        "",
        "This checklist is not optional. A missing check is a quality failure. If you cannot complete all 10, delay the playback.",
    ])


def build_microsoft(prs):
    title_slide(prs, "Cloud Readiness Accelerator",
        "How Rackspace CRA drives Azure-first outcomes, AMM funding eligibility, and structured co-sell",
        "Rackspace x Microsoft — Cloud Partner Alliance  |  [Date]")

    content_slide(prs, "Every structured assessment is a co-sell opportunity waiting to be activated", [
        "THE GAP WE FILL: Microsoft SMART takes 15 minutes. For 50+ application estates with Oracle/SAP, it is top-of-funnel — not a decision-making tool. Rackspace CRA is what happens next.",
        "",
        "THE RACKSPACE ROLE: Independent trusted advisor. No hyperscaler quota. When data points to Azure — as it does for most Microsoft-heavy estates with AHB opportunity — customers receive a credible, evidence-based Azure recommendation.",
        "",
        "THE MICROSOFT VALUE: CRA-delivered assessments produce all documentation required for AMM programme funding eligibility. Every CRA engagement with an Azure recommendation is a pre-qualified AMM conversation.",
        "",
        "\"SMART generates the lead. CRA qualifies it. AMM funds the migration. Rackspace delivers it.\"",
    ])

    table_slide(prs, "CRA phases map directly to Microsoft Cloud Adoption Framework (CAF) stages",
        ["CAF Stage", "CRA Phase", "CRA Deliverables That Satisfy It"],
        [
            ["Strategy", "Pre-engagement scoping", "Business drivers workshop · scope statement · stakeholder alignment"],
            ["Plan", "Phase 1 Discovery + Phase 2 Analysis", "Application inventory · infrastructure profiling · 5-dimension readiness scores · dependency map"],
            ["Ready", "Phase 3 Evaluation", "Right-sizing recommendations · Azure architecture alignment · AHB model · AMM eligibility screen"],
            ["Migrate", "Phase 4 Planning", "Migration wave plan · Part 2 Entry Point · risk register · governance charter"],
            ["Govern", "Phase 4 Planning (governance output)", "Governance model · RACI · operating model design"],
            ["Manage", "Post-CRA (Part 2 operations)", "Baseline for ongoing managed services handoff"],
        ]
    )

    table_slide(prs, "CRA produces every artefact required for AMM programme eligibility",
        ["AMM Requirement", "CRA Output", "CRA Template"],
        [
            ["Documented assessment methodology", "CRA METHODOLOGY.md + phase guides", "docs/METHODOLOGY.md"],
            ["Application and infrastructure inventory", "Application inventory + Infrastructure profiling", "application-scoping-profiling.xlsx + infrastructure-profiling.xlsx"],
            ["Multi-dimensional readiness assessment", "5-dimension cloud readiness scores per application", "cloud-readiness-scoring-v2.xlsx"],
            ["TCO / ROI analysis", "7-layer TCO: Azure, AWS, GCP comparison", "business-case-tco-roi.xlsx"],
            ["Azure as primary recommendation", "Hyperscaler decision matrix + assessment report", "hyperscaler-decision-matrix.xlsx + report"],
            ["Migration wave plan", "Sequenced application migration plan", "migration-wave-planner.xlsx"],
        ],
        intro="A CRA-delivered assessment does not require additional documentation to support an AMM funding request. No post-assessment rework."
    )

    content_slide(prs, "Azure Hybrid Benefit — modelled explicitly, not forgotten", [
        "Windows Server Standard/Datacenter: 15–40% VM cost reduction (requires active Software Assurance)",
        "SQL Server Standard: ~70% cost reduction per core (requires active SA)",
        "SQL Server Enterprise: ~70% cost reduction per core (requires active SA)",
        "",
        "HOW CRA MODELS AHB:",
        "  Phase 1: Infrastructure profiling captures all Windows Server and SQL Server versions and licence types",
        "  Phase 3: AHB eligibility screened — requires active SA confirmation from customer",
        "  TCO Licensing Overlay tab: separate rows for PAYG vs AHB scenarios per VM type",
        "",
        "IMPORTANT: AHB saving only available in Azure. For Microsoft-heavy estates, this creates a structural cost advantage for Azure in the TCO.",
        "SA status confirmation: at Phase 1 scoping — not Phase 3.",
    ])

    table_slide(prs, "SMART to CRA handoff — step by step",
        ["Step", "Action", "Owner", "Timing"],
        [
            ["1", "Customer completes Microsoft SMART", "Customer (Microsoft SE facilitated)", "Pre-engagement"],
            ["2", "SMART score Amber or below → CRA trigger", "Microsoft SE + Rackspace Pre-Sales", "Within 1 week of SMART result"],
            ["3", "Rackspace scoping call (1 hr)", "Rackspace Pre-Sales Architect", "Within 1 week of SMART result"],
            ["4", "CRA scoping proposal produced", "Rackspace Pre-Sales", "Within 5 business days"],
            ["5", "Microsoft SE provides warm introduction to customer", "Microsoft SE", "With scoping proposal delivery"],
            ["6", "SOW signed → CRA begins", "Customer + Rackspace", "Week 0"],
            ["7", "Alliance Manager pre-registers AMM opportunity in MSPP", "Rackspace Alliance Manager", "Day 1"],
            ["8", "Microsoft PDM acknowledges co-sell in MSPP", "Microsoft PDM", "Week 1"],
        ]
    )

    content_slide(prs, "Extended Security Updates — the Azure cost advantage that gets missed", [
        "Microsoft provides ESU for Windows Server 2012/R2 and SQL Server 2012/2014 FREE in Azure.",
        "Running same EoL OS on AWS or GCP: customer must purchase ESU from Microsoft.",
        "",
        "TCO impact — 200 EoL servers over 3 years:",
        "  Azure ESU cost: £0 (included in Azure)",
        "  AWS or GCP ESU cost: £60K–£120K additional cost (paid to Microsoft)",
        "",
        "This is a legitimate Azure cost advantage that belongs in the TCO Licensing Overlay tab.",
        "",
        "Partner message: 'If your customer has Windows Server 2012 in their estate, Azure is structurally cheaper than AWS or GCP for those workloads — before you even include AHB.'",
    ])

    content_slide(prs, "How Rackspace ensures Azure recommendations are credible and defensible", [
        "1. Criteria weights agreed in WRITING by customer BEFORE scoring begins",
        "2. All three clouds scored with equal rigour — AWS and GCP at the same depth as Azure",
        "3. Every score has a documented evidence reference",
        "4. Recommendation slide follows the evidence slides — NEVER precedes them",
        "5. All three hyperscaler SEs are invited to the Phase 3 playback (standard practice)",
        "",
        "When all three hyperscalers are in the room and the recommendation still points to Azure — the Azure recommendation becomes unassailable.",
        "",
        "A CRA-delivered Azure recommendation is defensible to the customer's board, their procurement team, and any internal challenge from AWS or GCP advocates.",
    ])

    table_slide(prs, "Microsoft actions that maximise CRA co-sell success",
        ["Action", "When", "Why"],
        [
            ["Refer SMART Amber/Red customers to Rackspace", "Immediately after SMART result", "Top-of-funnel lead generation for CRA"],
            ["Provide warm introduction (not cold email)", "Before Rackspace scoping call", "Establishes Rackspace independence and credibility"],
            ["Confirm SA status for AHB eligibility", "At scoping workshop", "Enables accurate TCO modelling in Phase 3"],
            ["Acknowledge AMM deal registration in MSPP", "Phase 1 Week 1", "Required for AMM funding eligibility"],
            ["Provide AMM programme guidance for this account", "Phase 1 Week 1–2", "Confirms funding tier and programme requirements"],
            ["Attend Phase 3 playback (recommended)", "Phase 3 Week 14", "Shows co-sell alignment; strengthens Azure recommendation credibility"],
            ["Support AMM funding application", "Phase 3 Week 14–16", "Submits funding request once Azure recommendation is confirmed"],
        ]
    )

    content_slide(prs, "Phase 2 governance assessment prepares customer for Azure Landing Zone design", [
        "Azure-specific governance outputs from CRA Phase 2:",
        "  Identity & Access Management  →  Azure Active Directory (Entra ID) design · RBAC model for subscriptions",
        "  Security & Compliance  →  Defender for Cloud readiness · Microsoft Sentinel integration",
        "  Change & Release Management  →  Azure DevOps / GitHub Actions for cloud pipelines",
        "  Monitoring & Observability  →  Azure Monitor / Log Analytics workspace design",
        "  Cost Management (FinOps)  →  Azure Cost Management + Billing · tagging strategy for chargeback",
        "  Operations Readiness  →  Azure Update Manager · Azure Automation baseline",
        "",
        "KEY MESSAGE: The CRA governance baseline directly informs the Azure Landing Zone design.",
        "STU architects can take CRA governance output and directly begin landing zone design without running a separate assessment.",
    ])

    table_slide(prs, "Three ways to activate a Rackspace CRA opportunity with Microsoft",
        ["Path", "Trigger", "First Action"],
        [
            ["1. SMART Referral", "Microsoft SE completes SMART · score is Amber/Red", "SE refers to Rackspace Pre-Sales for CRA scoping call"],
            ["2. Joint Pipeline Review", "Monthly Rackspace + Microsoft PDM pipeline review", "Identify accounts where formal assessment accelerates Azure commitment"],
            ["3. Inbound from Customer", "Customer approaches Microsoft directly for cloud readiness help", "Microsoft SE recommends Rackspace CRA · warm introduction email"],
        ],
        intro="\"Schedule a 30-minute technical briefing between Rackspace Alliance Architecture and Microsoft STU to validate CRA against CAF and AMM requirements. This is the one session that unlocks co-sell activation.\""
    )


def build_aws(prs):
    title_slide(prs, "Cloud Readiness Accelerator",
        "How Rackspace CRA drives MAP-qualified assessments and structured AWS co-sell",
        "Rackspace x AWS — Migration Partner  |  [Date]")

    content_slide(prs, "CRA-qualified assessments feed directly into MAP migration pipeline", [
        "WHAT'S MISSING WITHOUT CRA: Most mid-market customers approaching AWS lack a formal application inventory, multi-cloud TCO model, and structured migration plan. Result: long discovery cycles and missed MAP registration windows.",
        "",
        "WHAT CRA PROVIDES: A 16-week structured assessment producing exactly the documentation MAP requires — application inventory, readiness assessment, AWS TCO with Savings Plans modelled, and a sequenced wave plan.",
        "",
        "THE MAP ACTIVATION: Every CRA engagement with an AWS recommendation is a MAP-eligible opportunity. Rackspace pre-registers in AWS ACE at Phase 1 kickoff.",
        "",
        "\"CRA Assessment phase outputs are the MAP Assess stage deliverables. The assessment work is done — MAP can begin immediately at Phase 4 close.\"",
    ])

    table_slide(prs, "CRA phases map directly to AWS MAP phases",
        ["MAP Phase", "CRA Phase", "CRA Deliverables"],
        [
            ["Assess (MRA, current-state baseline, business case)", "Phase 1 Discovery + Phase 2 Analysis", "Application inventory · infrastructure profiling · 5-dimension readiness scores · dependency map · AWS TCO baseline"],
            ["Mobilize (detailed migration plan, wave sequencing, landing zone)", "Phase 3 Evaluation + Phase 4 Planning", "AWS TCO model · hyperscaler recommendation · migration wave plan · Part 2 Entry Point · governance model"],
            ["Migrate & Modernize (full migration execution, WAR, optimization)", "Post-CRA (Part 2 engagement)", "CRA provides baseline and wave plan · migration execution is Part 2"],
        ]
    )

    table_slide(prs, "CRA produces every artefact required for MAP deal registration",
        ["MAP Requirement", "CRA Output", "CRA Template"],
        [
            ["Migration Readiness Assessment (MRA)", "CRA Phase 1+2: app inventory, readiness scores, governance assessment", "application-scoping-profiling.xlsx + cloud-readiness-scoring-v2.xlsx"],
            ["Current-state inventory", "Infrastructure profiling + Application inventory", "infrastructure-profiling.xlsx"],
            ["Business case with TCO analysis", "7-layer TCO with AWS On-Demand + RI + Savings Plans", "business-case-tco-roi.xlsx + aws-evaluation.xlsx"],
            ["Migration wave plan", "Wave planner with Tier-based sequencing", "migration-wave-planner.xlsx"],
            ["AWS as primary or co-primary recommendation", "Hyperscaler decision matrix — AWS scored and evidenced", "hyperscaler-decision-matrix.xlsx"],
            ["ACE deal registration", "Rackspace Alliance Manager registers at Phase 1 Day 1", "AWS Partner Central / ACE"],
        ]
    )

    content_slide(prs, "How CRA models AWS pricing — all three options, per region", [
        "On-Demand (tab: AWS-OnDemand): Like-for-Like baseline — worst case cost",
        "Reserved Instances 3yr All-Upfront (tab: AWS-RI-3yr): Standard commitment — typically 40–60% saving vs On-Demand",
        "Compute Savings Plans 3yr (tab: AWS-SavingsPlans): More flexible than RI; applies to EC2, Fargate, Lambda",
        "",
        "Key instance families:",
        "  m6i / m7i — General purpose: balanced CPU/RAM",
        "  r6i / r7i — Memory-optimised: databases, SAP",
        "  c6i / c7i — Compute-optimised: CPU-intensive workloads",
        "  i4i — Storage-optimised: high IOPS databases",
        "",
        "Cross-validate: use AWS Migration Evaluator from Phase 1 ADS data, then compare against manually-built aws-evaluation.xlsx.",
        "Always present all three pricing models — CFOs ask about flexibility vs. commitment.",
    ])

    content_slide(prs, "ACE deal registration — when and why it cannot wait", [
        "Phase 1 Day 1: Rackspace Alliance Manager registers opportunity in AWS Partner Central",
        "Phase 1 Week 2: AWS PSA confirms registration · confirms MAP programme applicability",
        "Phase 3 Week 11: TCO complete · Phase 3 Week 14: Recommendation presented",
        "",
        "HARD RULE: ACE registration must be active BEFORE Phase 3 begins.",
        "MAP assessment funding eligibility requires registration before assessment evidence is compiled — not after.",
        "",
        "AWS PDM ACTION REQUIRED:",
        "  Accept and acknowledge co-sell opportunity in ACE within 5 business days",
        "  Confirm MAP programme applicability for this customer tier",
        "  Introduce AWS PSA if technical depth needed in Phase 3",
    ])

    content_slide(prs, "CRA identifies open-source workload migration paths on AWS", [
        "OSS LICENCE RISK IDENTIFIED IN CRA PHASE 2 — AWS managed alternatives:",
        "  Redis OSS (post v7.4 — SSPL): Amazon ElastiCache (Valkey or Redis-compatible) — low complexity",
        "  Elasticsearch (post 7.10 — SSPL): Amazon OpenSearch Service (Apache 2.0 fork) — low-medium",
        "  HashiCorp Vault (BSL): AWS Secrets Manager + Parameter Store — medium",
        "  MongoDB (SSPL): Amazon DocumentDB (MongoDB-compatible) — medium",
        "",
        "CRA Phase 3: OSS-flagged workloads costed with managed service replacement in aws-evaluation.xlsx OSS-Migration tab.",
        "",
        "For AWS: ElastiCache and OpenSearch are more mature than equivalents on other hyperscalers — can be a legitimate AWS advantage for Redis/Elasticsearch-heavy estates.",
    ])

    content_slide(prs, "When CRA recommends AWS, the customer's board believes it", [
        "THE CREDIBILITY PROBLEM: Customers know hyperscaler-provided assessments are not independent. A free AWS assessment recommending AWS is not surprising.",
        "",
        "A formal, 16-week, three-way evaluation by an independent Rackspace-led team that recommends AWS is a different kind of evidence.",
        "",
        "What 'independent recommendation' means:",
        "  CRA evaluates all three clouds with equal rigour",
        "  Criteria weights are agreed by the customer before scoring — not by Rackspace or AWS",
        "  The TCO shows all three clouds — customer can see why AWS won",
        "  All three hyperscaler SEs are invited to the Phase 3 playback",
        "",
        "A CRA-delivered AWS recommendation is the strongest possible evidence for an investment committee, a Microsoft incumbent account team, or an Azure-preferring CTO.",
    ])

    table_slide(prs, "Three paths to a Rackspace CRA / AWS MAP co-sell activation",
        ["Path", "Trigger", "First Action"],
        [
            ["1. MAP Pipeline Identification", "AWS PDM identifies accounts approaching migration readiness", "Refer to Rackspace Pre-Sales for CRA scoping call"],
            ["2. CART / MRA Upgrade", "Customer has completed AWS CART · score suggests formal assessment needed", "Rackspace CRA provides MAP Assess deliverables to higher rigour standard"],
            ["3. Joint Pipeline Review", "Monthly joint review: Rackspace Alliance Manager + AWS PDM", "Identify accounts where CRA accelerates MAP registration"],
        ],
        intro="\"Schedule a 30-minute session between Rackspace Alliance Architecture and AWS PSA to confirm CRA methodology against MAP Assess requirements. One session. Unlocks the entire co-sell pipeline.\""
    )


def build_gcp(prs):
    title_slide(prs, "Cloud Readiness Accelerator",
        "How Rackspace CRA aligns to Google Cloud's migration methodology and PSO programme requirements",
        "Rackspace x Google Cloud — Migration Partner  |  [Date]")

    content_slide(prs, "CRA-qualified assessments are the front-end of GCP PSO migration engagements", [
        "THE GAP: Mid-market customers interested in GCP often complete Google Migration Center assessments but cannot translate output into a board-ready investment decision.",
        "",
        "WHAT CRA PROVIDES: A 16-week structured assessment producing the GCAF Assess and Plan stage deliverables at a rigour level supporting GCP PSO engagement qualification and migration credit eligibility.",
        "",
        "THE GCP ACTIVATION: Every CRA engagement with a GCP recommendation generates a PSO-qualified opportunity. Rackspace pre-registers in Google Partner Advantage at Phase 1 kickoff.",
        "",
        "\"CRA delivers the GCAF Assess and Plan stages. GCP PSO and RAMP can begin at Phase 4 close — no additional discovery required.\"",
    ])

    table_slide(prs, "CRA phases map directly to Google Cloud Adoption Framework stages",
        ["GCAF Stage", "CRA Phase", "CRA Deliverables"],
        [
            ["Assess (evaluate workloads, identify cloud fit, baseline TCO)", "Phase 1 Discovery + Phase 2 Analysis", "Application inventory · infrastructure profiling · 5-dimension readiness scores · dependency map · GCP cloud fit assessment"],
            ["Plan (design target architecture, build migration business case, define wave plan)", "Phase 3 Evaluation + Phase 4 Planning", "GCP TCO model · hyperscaler recommendation · migration wave plan · landing zone design guidance · governance model"],
            ["Deploy (landing zone build, foundation infrastructure, initial wave)", "Post-CRA (Part 2 engagement)", "CRA provides deployment specifications · landing zone build is separate Part 2 workstream"],
            ["Optimise (cost optimisation, SRE, FinOps)", "Post-CRA (ongoing)", "CRA TCO model provides cost optimisation baseline"],
        ]
    )

    content_slide(prs, "CRA Phase 1 uses Google Migration Center — natively", [
        "Migration Center accepts RVTools VMware export directly.",
        "If Azure Migrate is the primary discovery tool, the same RVTools export populates Migration Center — no additional agent deployment required.",
        "",
        "CRA INTEGRATION WORKFLOW:",
        "  Phase 1 Wk 1: Deploy GCP Migration Center collector or VM Manager agent",
        "  Phase 1 Wks 1–7: Collect 14+ days of utilisation data",
        "  Phase 3 Wk 11: Run Migration Center GCP right-sizing analysis",
        "  Phase 3 Wks 12–13: Cross-validate against gcp-evaluation.xlsx · resolve discrepancies",
        "",
        "Cross-validate because: Migration Center applies standard GCP pricing and default right-sizing assumptions. CRA manual model applies customer-specific Oracle workload costs, specific instance families, and customer-committed CUD levels.",
    ])

    table_slide(prs, "How CRA models GCP pricing — two options, per region",
        ["Pricing Model", "GCP Name", "CRA Tab", "Typical Saving"],
        [
            ["On-Demand", "Pay-as-you-go", "GCP-OnDemand", "Baseline — worst case cost"],
            ["Committed Use Discounts (3yr)", "3-year CUD", "GCP-CUD-3yr", "Typically 37–55% saving vs On-Demand"],
        ],
        intro="Key instance families: n2-standard (general) · n2-highmem (memory-optimised, Oracle) · c3-standard (latest gen) · m3-ultramem (SAP HANA, high-memory Oracle). GCP CUDs are resource-based (CPU/RAM) — more flexibility than AWS RI, less than AWS Savings Plans."
    )

    content_slide(prs, "GCP's open-source strength — and how CRA surfaces it", [
        "OSS LICENCE RISK IDENTIFIED IN CRA PHASE 2 — GCP managed alternatives:",
        "  Redis OSS (post v7.4 — SSPL): Memorystore for Redis / Valkey — fully managed, Redis-compatible",
        "  Elasticsearch (post 7.10 — SSPL): Elastic on GCP Marketplace or Vector Search — native Elastic partnership",
        "  HashiCorp Vault (BSL): Secret Manager / Berglas — GCP-native, no licence concerns",
        "  MongoDB (SSPL): Cloud Firestore / MongoDB Atlas on GCP Marketplace",
        "  Kafka: Pub/Sub + Dataflow — GCP's natural Kafka alternative, no licence risk",
        "",
        "CONTAINERS: For 'Cloud Friendly' (Replatform) workloads, CRA Phase 3 models containerisation on GKE.",
        "GKE is often the most capable managed Kubernetes service — a legitimate GCP advantage.",
    ])

    content_slide(prs, "GCP surfaces its advantage for data, analytics, and AI/ML workloads", [
        "CRA Phase 2 captures data platform and analytics workloads with extra criteria: data volume/frequency, current analytics stack (Spark/Hadoop/ETL), ML models in production, real-time vs batch requirements.",
        "",
        "WHERE GCP HAS A STRUCTURAL ADVANTAGE IN CRA TCO:",
        "  Apache Spark / Hadoop → Dataproc (fully managed, auto-scaling) vs EC2 Spark vs Azure HDInsight",
        "  Data warehouse (Teradata, Oracle DW) → BigQuery (serverless, no infrastructure cost) vs Azure Synapse vs Redshift",
        "  AI/ML training and inference → Vertex AI (integrated MLOps, TPU access)",
        "  Real-time event streaming → Pub/Sub + Dataflow (Kafka alternative)",
        "",
        "CRA action: Data platform workloads flagged in Phase 2 → modelled with GCP managed service alternatives in Phase 3.",
        "For customers with significant data workloads, this comparison often shows a strong GCP cost advantage.",
    ])

    content_slide(prs, "A CRA-delivered GCP recommendation is unassailable", [
        "THE CHALLENGE: Many mid-market enterprises default to Azure through inertia. A GCP recommendation from Google is dismissed as sales pressure.",
        "",
        "WHAT THE CRA PROCESS PROVIDES:",
        "  Customer agrees evaluation criteria and weights before any scoring begins",
        "  All three clouds scored with equal depth — Azure and AWS get the same rigour",
        "  GCP wins where GCP is genuinely the best fit: containerisation, data analytics, OSS workloads, AI/ML",
        "  The recommendation follows the evidence — it is not pre-determined",
        "  All three hyperscaler SEs are in the room at the Phase 3 playback",
        "",
        "'Rackspace ran a 16-week independent assessment. They evaluated Azure, AWS, and GCP. The data shows GCP is the right answer for our containerisation and analytics workloads.'",
        "This is a different conversation than any Google sales rep can have.",
    ])

    table_slide(prs, "Three paths to a Rackspace CRA / GCP co-sell activation",
        ["Path", "Trigger", "First Action"],
        [
            ["1. Migration Center Assessment Upgrade", "Customer has used GCP Migration Center · needs formal board-ready multi-cloud business case", "Rackspace CRA takes Migration Center data and builds complete GCAF Assess + Plan deliverables"],
            ["2. GCP Pipeline Identification", "GCP PDM identifies accounts with data, analytics, or containerisation workloads where GCP has advantage", "Refer to Rackspace Pre-Sales for CRA scoping call · CRA ensures TCO models BigQuery, Dataproc, GKE"],
            ["3. Joint Pipeline Review", "Monthly joint review: Rackspace Alliance Manager + GCP PDM", "Identify accounts where CRA accelerates partner programme registration"],
        ],
        intro="\"Schedule a 30-minute session between Rackspace Alliance Architecture and Google Cloud PSE to confirm CRA methodology against GCAF and PSO programme requirements.\""
    )


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    decks = [
        ("presentations/executive/CRA-Leadership-Overview.pptx",   build_leadership),
        ("presentations/executive/CRA-Executive-Overview.pptx",    build_executive),
        ("presentations/technical/CRA-Technical-Overview.pptx",    build_technical),
        ("presentations/alliance/CRA-Microsoft-Partner-Deck.pptx", build_microsoft),
        ("presentations/alliance/CRA-AWS-Partner-Deck.pptx",       build_aws),
        ("presentations/alliance/CRA-GCP-Partner-Deck.pptx",       build_gcp),
    ]
    for rel_path, builder in decks:
        out = os.path.join(BASE, rel_path)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        prs = Presentation(TEMPLATE)
        clear_slides(prs)
        builder(prs)
        prs.save(out)
        print(f"OK  {rel_path}  ({len(prs.slides)} slides)")

if __name__ == "__main__":
    main()
