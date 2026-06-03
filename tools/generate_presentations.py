#!/usr/bin/env python3
"""CRA Presentation Generator — creates all 6 PPTX files from content specs."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml
from lxml import etree
import os

# ── Colours ────────────────────────────────────────────────────────────────────
RED    = RGBColor(0xE3, 0x1C, 0x3D)
NAVY   = RGBColor(0x1A, 0x1F, 0x36)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
LGRAY  = RGBColor(0xF2, 0xF2, 0xF2)
DGRAY  = RGBColor(0x33, 0x33, 0x33)
MGRAY  = RGBColor(0x77, 0x77, 0x77)
AZURE  = RGBColor(0x00, 0x78, 0xD4)
AWSOR  = RGBColor(0xFF, 0x99, 0x00)
GCPBL  = RGBColor(0x42, 0x85, 0xF4)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Helpers ────────────────────────────────────────────────────────────────────

def new_prs():
    prs = Presentation()
    prs.slide_width  = Inches(13.33)
    prs.slide_height = Inches(7.5)
    return prs

def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])

def rgb_str(rgb: RGBColor) -> str:
    return f"{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"

def set_bg(slide, color: RGBColor):
    bg = slide.background; fill = bg.fill
    fill.solid(); fill.fore_color.rgb = color

def add_rect(slide, x, y, w, h, fill_color: RGBColor, line=False):
    shape = slide.shapes.add_shape(1, x, y, w, h)
    shape.fill.solid(); shape.fill.fore_color.rgb = fill_color
    if not line:
        shape.line.fill.background()
    return shape

def txt(slide, text, x, y, w, h, size=14, bold=False, color=DGRAY,
        align=PP_ALIGN.LEFT, wrap=True, italic=False):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame; tf.word_wrap = wrap
    p = tf.paragraphs[0]; p.alignment = align
    run = p.add_run(); run.text = text
    run.font.size = Pt(size); run.font.bold = bold
    run.font.color.rgb = color; run.font.name = "Calibri"
    run.font.italic = italic
    return tb

def add_footer(slide, text, color=MGRAY):
    txt(slide, text, Inches(0.3), Inches(7.1), Inches(12.5), Inches(0.35),
        size=8, color=color, align=PP_ALIGN.CENTER)

def set_notes(slide, notes_text):
    if not notes_text:
        return
    notes = slide.notes_slide
    tf = notes.notes_text_frame
    tf.text = notes_text

# ── Slide builders ─────────────────────────────────────────────────────────────

def title_slide(prs, title, subtitle, meta="", footer="", accent=RED, notes=""):
    slide = blank(prs)
    set_bg(slide, accent)
    # left white strip
    add_rect(slide, Inches(0), Inches(0), Inches(0.12), Inches(7.5), WHITE)
    txt(slide, title, Inches(0.5), Inches(2.2), Inches(12), Inches(1.6),
        size=38, bold=True, color=WHITE)
    if subtitle:
        txt(slide, subtitle, Inches(0.5), Inches(3.9), Inches(11), Inches(1.0),
            size=20, color=RGBColor(0xFF,0xCC,0xCC))
    if meta:
        txt(slide, meta, Inches(0.5), Inches(5.1), Inches(11), Inches(0.8),
            size=13, color=RGBColor(0xFF,0xDD,0xDD))
    if footer:
        txt(slide, footer, Inches(0.5), Inches(6.9), Inches(12), Inches(0.4),
            size=8, color=RGBColor(0xFF,0xCC,0xCC))
    set_notes(slide, notes)
    return slide

def content_slide(prs, heading, bullets, footer="", accent=RED, notes="", sub_bullets=None):
    """bullets = list of str; sub_bullets = dict {idx: [sub1, sub2]}"""
    slide = blank(prs)
    add_rect(slide, Inches(0), Inches(0), Inches(13.33), Inches(1.15), accent)
    txt(slide, heading, Inches(0.3), Inches(0.12), Inches(12.5), Inches(0.95),
        size=22, bold=True, color=WHITE)
    tb = slide.shapes.add_textbox(Inches(0.45), Inches(1.3), Inches(12.2), Inches(5.9))
    tf = tb.text_frame; tf.word_wrap = True
    for i, b in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = b
        p.level = 0
        for run in p.runs:
            run.font.size = Pt(13.5); run.font.color.rgb = DGRAY; run.font.name = "Calibri"
        p.space_after = Pt(3)
        if sub_bullets and i in sub_bullets:
            for sb in sub_bullets[i]:
                sp = tf.add_paragraph(); sp.text = "    " + sb; sp.level = 1
                for run in sp.runs:
                    run.font.size = Pt(12); run.font.color.rgb = MGRAY; run.font.name = "Calibri"
    if footer:
        add_footer(slide, footer)
    set_notes(slide, notes)
    return slide

def two_col_slide(prs, heading, left_title, left_items, right_title, right_items,
                  footer="", accent=RED, notes=""):
    slide = blank(prs)
    add_rect(slide, Inches(0), Inches(0), Inches(13.33), Inches(1.15), accent)
    txt(slide, heading, Inches(0.3), Inches(0.12), Inches(12.5), Inches(0.95),
        size=22, bold=True, color=WHITE)
    # divider line
    add_rect(slide, Inches(6.6), Inches(1.25), Inches(0.03), Inches(5.9), LGRAY)
    for col, (ctitle, citems, ox) in enumerate([
        (left_title, left_items, Inches(0.3)),
        (right_title, right_items, Inches(6.75))
    ]):
        if ctitle:
            txt(slide, ctitle, ox, Inches(1.3), Inches(6.0), Inches(0.45),
                size=14, bold=True, color=accent)
        tb = slide.shapes.add_textbox(ox, Inches(1.85), Inches(6.0), Inches(5.4))
        tf = tb.text_frame; tf.word_wrap = True
        for i, item in enumerate(citems):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = item
            for run in p.runs:
                run.font.size = Pt(13); run.font.color.rgb = DGRAY; run.font.name = "Calibri"
            p.space_after = Pt(4)
    if footer:
        add_footer(slide, footer)
    set_notes(slide, notes)
    return slide

def table_slide(prs, heading, headers, rows, footer="", accent=RED, notes="",
                col_widths=None, intro_text=""):
    slide = blank(prs)
    add_rect(slide, Inches(0), Inches(0), Inches(13.33), Inches(1.15), accent)
    txt(slide, heading, Inches(0.3), Inches(0.12), Inches(12.5), Inches(0.95),
        size=22, bold=True, color=WHITE)
    y_start = Inches(1.25)
    if intro_text:
        txt(slide, intro_text, Inches(0.4), y_start, Inches(12.5), Inches(0.55),
            size=13, color=DGRAY, italic=True)
        y_start += Inches(0.62)
    ncols = len(headers)
    if col_widths is None:
        col_widths = [Inches(13.0 / ncols)] * ncols
    table_h = Inches(0.42) * (len(rows) + 1)
    max_h = Inches(7.5) - y_start - Inches(0.5)
    if table_h > max_h:
        table_h = max_h
    tbl = slide.shapes.add_table(len(rows) + 1, ncols,
                                  Inches(0.15), y_start,
                                  sum(col_widths), table_h).table
    # set column widths
    for ci, cw in enumerate(col_widths):
        tbl.columns[ci].width = cw
    # header row
    for ci, h in enumerate(headers):
        cell = tbl.cell(0, ci)
        cell.text = h
        cell.fill.solid(); cell.fill.fore_color.rgb = accent
        p = cell.text_frame.paragraphs[0]
        for run in p.runs:
            run.font.bold = True; run.font.size = Pt(11)
            run.font.color.rgb = WHITE; run.font.name = "Calibri"
        p.alignment = PP_ALIGN.LEFT
    # data rows
    for ri, row in enumerate(rows):
        bg = LGRAY if ri % 2 == 0 else WHITE
        for ci, val in enumerate(row):
            cell = tbl.cell(ri + 1, ci)
            cell.text = str(val)
            cell.fill.solid(); cell.fill.fore_color.rgb = bg
            p = cell.text_frame.paragraphs[0]
            for run in p.runs:
                run.font.size = Pt(10.5); run.font.color.rgb = DGRAY; run.font.name = "Calibri"
    if footer:
        add_footer(slide, footer)
    set_notes(slide, notes)
    return slide

def callout_slide(prs, heading, callout_text, bullets=None, footer="", accent=RED, notes=""):
    slide = blank(prs)
    add_rect(slide, Inches(0), Inches(0), Inches(13.33), Inches(1.15), accent)
    txt(slide, heading, Inches(0.3), Inches(0.12), Inches(12.5), Inches(0.95),
        size=22, bold=True, color=WHITE)
    # callout box
    add_rect(slide, Inches(0.4), Inches(1.3), Inches(12.5), Inches(1.3), LGRAY)
    txt(slide, callout_text, Inches(0.6), Inches(1.42), Inches(12.1), Inches(1.1),
        size=15, bold=True, color=accent, italic=True)
    if bullets:
        tb = slide.shapes.add_textbox(Inches(0.45), Inches(2.8), Inches(12.2), Inches(4.3))
        tf = tb.text_frame; tf.word_wrap = True
        for i, b in enumerate(bullets):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = b
            for run in p.runs:
                run.font.size = Pt(13.5); run.font.color.rgb = DGRAY; run.font.name = "Calibri"
            p.space_after = Pt(4)
    if footer:
        add_footer(slide, footer)
    set_notes(slide, notes)
    return slide

# ── Deck: CRA Leadership Overview ──────────────────────────────────────────────

def build_leadership(prs):
    F = "© 2026 Rackspace Technology — INTERNAL ONLY"

    title_slide(prs, "Cloud Readiness Accelerator",
        "A practitioner-grade framework for delivering cloud readiness assessments at scale",
        "Cloud Solutions Architecture | Internal Leadership Briefing | 2026",
        F, notes="Welcome. This deck is for internal leadership. Goal: secure sponsorship and resource commitment to complete and activate the CRA framework.")

    content_slide(prs, "Every CRA engagement starts from scratch — and it costs us", [
        "Delivery teams spend 3–6 weeks scoping and building templates before an assessment even starts",
        "Inconsistent outputs across engagements create QA risk and weaken partner trust",
        "Customers can get a free 15-minute Azure check from Microsoft — we must compete on depth, not speed",
        "",
        "\"Without a standardised framework, we win deals on relationships and lose renewals on quality.\""
    ], F, notes="The status quo is custom-built per engagement. Templates recreated from scratch every time. Three consequences: slow time-to-value, inconsistent outputs, junior architects can't ramp up. CRA solves all three.")

    table_slide(prs, "The window is open now",
        ["Signal", "What It Means for Rackspace"],
        [
            ["70% of enterprises accelerating cloud migration post-2024", "High inbound demand for formal readiness assessments"],
            ["Average CRA deal size: $250K–$1.5M", "Premium revenue per engagement"],
            ["Microsoft / AWS / GCP all have FREE 15-min tools", "We must differentiate on depth, deliverables, and alliance leverage"],
            ["Customers cite 'lack of internal capability' as #1 migration barrier", "CRA directly addresses the most cited blocker"],
            ["Alliance partners reward assessment-led deal creation", "Every CRA engagement is a co-sell opportunity"],
        ],
        F, col_widths=[Inches(6.8), Inches(6.0)],
        intro_text="$10M+ revenue influence potential in Year 1 — 15 engagements × $650K average deal size",
        notes="Clear revenue number attached to this. Microsoft and AWS actively seek Rackspace-led assessments to feed their migration pipelines.")

    two_col_slide(prs, "A complete, reusable toolkit — not a methodology document",
        "What it includes:", [
            "Four-phase assessment methodology (Discovery → Analysis → Evaluation → Planning)",
            "30+ reusable templates (Excel, Word, PPTX) for every deliverable",
            "TCO models validated against real customer data (AWS, Azure, GCP)",
            "Hyperscaler decision matrix — vendor-neutral, board-grade",
            "Reference case study: DMG Media UK (4,200+ VMs, Azure recommendation with AMM funding)",
            "Executive and technical reporting templates",
            "Alliance alignment guides (Microsoft CAF, AWS MAP, GCP PSO)"
        ],
        "What it replaces:", [
            "6–8 weeks of custom scoping and template-building",
            "Inconsistent outputs across delivery teams",
            "Architect-dependent tribal knowledge",
            "Missed AMM / MAP funding opportunities",
            "",
            "Result: 30%+ reduction in delivery time. Consistent, auditable, partner-validated outputs."
        ], F, notes="The framework already exists and is 63% complete. This is not a future-state proposal — it was used in a live £1M+ engagement.")

    content_slide(prs, "Structured, repeatable, end-to-end", [
        "PHASE 1: DISCOVERY — 7 weeks",
        "    Application inventory · Infrastructure profiling · Dependency mapping",
        "PHASE 2: ANALYSIS — 4 weeks",
        "    5-dimension readiness scoring · Gap identification · Cloud maturity assessment",
        "PHASE 3: EVALUATION — 3 weeks",
        "    TCO modelling (AWS/Azure/GCP) · Hyperscaler decision matrix · Business case · ROI/NPV",
        "PHASE 4: PLANNING — 6 weeks",
        "    Migration waves · Risk register · Governance model · Part 2 entry point",
        "",
        "Total engagement: 16–20 weeks parallelised (mid-market). Scales to 200+ applications.",
        "4,212 VMs discovered in Phase 1 (DMG Media UK) · 57% scope variance identified · AMM funding unlocked"
    ], F, notes="Timeline based on a real engagement. Phase 1 takes 7 weeks because CAB approval (5–10 business days) and ≥14 day utilisation data window are non-negotiable quality gates.")

    table_slide(prs, "Microsoft SMART and Rackspace CRA serve different moments",
        ["Microsoft SMART Assessment", "Rackspace CRA"],
        [
            ["Free, self-service", "Formal engagement, deliverable-based"],
            ["15 minutes", "16–20 weeks"],
            ["Azure only", "AWS + Azure + GCP"],
            ["No deliverable", "30–50 page assessment report"],
            ["Pre-sales screening", "Board / CIO sign-off document"],
            ["< 50 applications", "50+ applications; complex infrastructure"],
            ["No AMM eligibility", "CRA outputs satisfy AMM requirements"],
        ], F,
        intro_text="SMART generates the lead. CRA converts it to revenue.",
        notes="SMART is top-of-funnel. When a customer's SMART score is amber/below, that triggers the CRA scoping call. Microsoft PDMs actively want partners who operationalise this handoff.")

    content_slide(prs, "One engagement. Every phase. Real numbers.", [
        "DMG Media UK (Daily Mail Group Trust) — UK's largest digital media group",
        "On-premises VMware estate, 2 UK data centres, 10 vCenter instances",
        "",
        "4,212 VMs discovered across all 10 vCenter instances",
        "+57% above SoW scope — estate was larger than expected",
        "3-way evaluation: Azure vs AWS vs GCP across 9 regions",
        "Azure recommended: UK South primary + AMM funding identified",
        "",
        "Framework lessons embedded: scope validation worksheet · legacy OS discovery · AMM pre-engagement checklist · Oracle RAC migration path"
    ], F, notes="Every number is real. The framework was built from this engagement. The next team to use CRA will not make the same mistakes.")

    content_slide(prs, "The numbers that matter to leadership", [
        "30% FASTER — assessment delivery vs. custom-built engagement (7-week template setup removed)",
        "",
        "$10M+ INFLUENCED REVENUE — in Year 1 (15 engagements × $650K avg deal size)",
        "",
        "3 ALLIANCE PROGRAMMES — Microsoft AMM + AWS MAP + Google PSO funding eligible",
        "",
        "NPS target: >70 · 30+ templates reused across engagements · 8+ co-sell deals Year 1",
        "",
        "Investment to finish remaining 37%: ~$80K–$120K fully loaded (0.5 FTE × 12 wks + writer + designer)",
        "Expected return: $10M+ influenced revenue — 80–100× ROI"
    ], F, notes="The $80–120K is the cost to FINISH it. It's already 63% complete. DMG comparison: 6–7 weeks building from scratch vs. zero with framework.")

    table_slide(prs, "Built to fund, not just deliver",
        ["Partner", "CRA Alignment", "Reference"],
        [
            ["Microsoft Azure (CAF/AMM)", "CRA phases map to CAF stages · TCO satisfies AMM deliverable requirements · AHB modelled · Pre-engagement AMM checklist built in", "docs/MICROSOFT-CAF-ALIGNMENT.md"],
            ["AWS (MAP)", "CRA Assessment phase maps to MAP Assess · Inventory + readiness scoring satisfy MAP deal registration · TCO: On-Demand, 3yr RI, Savings Plans", "docs/AWS-MAP-ALIGNMENT.md"],
            ["Google Cloud (PSO/RAMP)", "Discovery aligns to Migration Center inputs · GCP TCO across 3 regions (On-Demand + CUDs) · RAMP programme alignment", "docs/GOOGLE-PSO-ALIGNMENT.md"],
        ], F, col_widths=[Inches(2.2), Inches(7.8), Inches(2.8)],
        intro_text="Every CRA engagement is a potential AMM, MAP, or PSO funding conversation. CRA makes this systematic.",
        notes="CAF alignment is complete and in the repo now. AWS and GCP alignment docs complete. Invite partner PDMs to review METHODOLOGY.md.")

    content_slide(prs, "Where we are, where we go next", [
        "PHASE 1: FOUNDATION — COMPLETE ✓",
        "    Repo restructured · 30+ templates created · DMG Media UK case study published · README/docs rewritten · Release v1.0 published",
        "",
        "PHASE 2: ENHANCEMENT — IN PROGRESS",
        "    Template content audit (Epics 4A–4E) · Leadership and executive presentation decks",
        "    Microsoft CAF + AWS MAP + GCP PSO alignment docs complete · Branding applied",
        "",
        "PHASE 3: SCALE — PLANNED",
        "    Internal SA team training workshop · SharePoint library deployment",
        "    Microsoft AMM programme submission · AWS MAP pre-qualification · Alliance partner go-to-market",
        "",
        "Current status: 63% complete. On track for Release 1.1."
    ], F, notes="We are not asking for approval to START. We are asking for sponsorship to FINISH. Foundation is done. Asking for resources for the enhancement phase.")

    content_slide(prs, "Three asks. Twelve weeks. $10M+ return.", [
        "1. RESOURCE COMMITMENT",
        "   0.5 FTE Cloud Solutions Architect for 12 weeks to complete template library and alliance decks",
        "   0.1 FTE Technical Writer for 8 weeks | Estimated fully loaded cost: $80K–$120K",
        "",
        "2. EXECUTIVE SPONSORSHIP",
        "   VP or Director level sponsor to champion CRA in partner conversations with Microsoft, AWS, and Google",
        "   One internal leadership session to validate framework before external sharing",
        "",
        "3. GO-TO-MARKET ACTIVATION",
        "   Approval to share with Microsoft UK and AWS UK partner managers",
        "   (subject to legal review of DMG Media UK case study — Legal gate identified, in progress)",
        "",
        "Investment: ~$100K. Return: $10M+ influenced revenue in Year 1. 100× ROI."
    ], F, notes="The legal gate on case study is real but does not block internal enablement or partner pre-qualification at framework level. We can share methodology, templates, and alliance docs now while legal review is in flight.")

    table_slide(prs, "Next steps — decisions needed today",
        ["Action", "Owner", "When"],
        [
            ["Confirm 0.5 FTE architect commitment for Weeks 5–12", "[VP/Director Name]", "This meeting"],
            ["Identify executive sponsor for Microsoft/AWS co-sell conversations", "[VP Name]", "This week"],
            ["Initiate legal review of DMG Media UK case study", "Legal / [Name]", "This week"],
        ], F, col_widths=[Inches(7.5), Inches(3.0), Inches(2.3)],
        intro_text="\"The framework exists. The methodology is proven. The case study is real. The only question is whether we resource it to scale.\"",
        notes="Close by confirming next actions with owners and dates.")


# ── Deck: CRA Executive Overview (customer-facing) ────────────────────────────

def build_executive(prs):
    F = "© 2026 Rackspace Technology — Confidential and Proprietary"

    title_slide(prs, "Cloud Readiness Assessment",
        "A structured path to a confident, evidence-based cloud migration decision",
        "Rackspace Cloud Solutions Architecture | [Customer Name] | [Date]",
        F, notes="Welcome. This is not a sales presentation for a specific cloud. It is a structured overview of how Rackspace guides organisations from 'we need to move to cloud' to a board-ready business case and migration plan.")

    content_slide(prs, "Moving to cloud is not the hard part — deciding which cloud, when, and at what cost is", [
        "TOO MANY OPINIONS: Every hyperscaler says they are the best choice. Microsoft, AWS, and Google all have free tools telling you different things. Without independent analysis, the loudest voice wins.",
        "",
        "COMPLEXITY YOU CANNOT SEE: You likely have Oracle databases, end-of-life OS, licensing obligations, and infrastructure dependencies that affect cost and timelines — only visible once you look. Most cloud cost estimates are wrong because they start before the data is collected.",
        "",
        "THE COST OF GETTING IT WRONG: Organisations that start cloud migrations without a formal assessment overspend by 30–60% in Year 1. Recovery cost is typically 3–5× the cost of a proper upfront assessment.",
        "",
        "\"A cloud migration decision is a board-level financial commitment of £1M–£10M+. It deserves the same rigour as any capital investment.\""
    ], F, notes="Validate with customer. The CRA exists because these problems are real and predictable. Question is whether they encounter them before or after committing to a hyperscaler.")

    table_slide(prs, "A Cloud Readiness Assessment (CRA) is a decision-making system, not a report",
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
        ], F, col_widths=[Inches(5.5), Inches(7.3)],
        intro_text="Four phases · 16–20 weeks · Uses proven tooling · Fully cloud-neutral recommendation",
        notes="Emphasise 'system' not 'report'. The inventory becomes the source of truth. The TCO becomes the CFO reference. The wave plan becomes the programme plan.")

    two_col_slide(prs, "The difference is independence — and the ability to unlock partner funding",
        "Independence:", [
            "Rackspace has no hyperscaler revenue target to meet",
            "Our recommendation is based entirely on your data",
            "If AWS is the right answer, we recommend AWS",
            "If Azure is right, we recommend Azure",
            "We have delivered assessments recommending all three",
        ],
        "Partner Funding:", [
            "Rackspace is a qualified partner for Microsoft AMM, AWS MAP, and Google PSO",
            "A correctly documented CRA can unlock £100K–£1M+ in partner funding toward migration costs",
            "We identify this eligibility as part of the assessment — at no extra cost",
            "",
            "\"A Rackspace CRA pays for itself when partner funding is identified.\"",
        ], F, notes="Do not sell against Microsoft or AWS. SMART and CRA serve different purposes. The partner funding point is a genuine differentiator — spend time on it.")

    content_slide(prs, "Four phases. Structured gates. No guesswork.", [
        "PHASE 1: DISCOVERY — 7 weeks",
        "   Deploy tooling · Collect VM, app, storage & network data · Map app dependencies",
        "",
        "PHASE 2: ANALYSIS — 4 weeks  [starts at Phase 1 Week 6 in parallel]",
        "   Score each app across 5 cloud readiness dimensions · Assess cloud governance maturity",
        "",
        "PHASE 3: EVALUATION — 3 weeks",
        "   Model TCO for all 3 clouds · Evaluate all 3 hyperscalers · Produce recommendation with evidence",
        "   ► GATE 2: Alliance partner deal registration complete before Part 2 SOW",
        "",
        "PHASE 4: PLANNING — 6 weeks",
        "   Build migration waves · Define risk register · Finalise Part 2 Entry Point",
        "",
        "► GATE 1: ≥14 days clean utilisation data required before Phase 3 can begin",
        "Total: 16–20 weeks for mid-market estates (200–500 applications)"
    ], F, notes="The two gates protect the customer. Gate 1 ensures TCO accuracy. Gate 2 protects access to partner funding. Both are non-negotiable.")

    two_col_slide(prs, "Phase 1 Discovery — Getting the complete picture of your estate",
        "What Rackspace does:", [
            "Deploy non-invasive discovery tooling (agent-based or agentless)",
            "Collect 14+ days of CPU, memory, storage, and network utilisation data",
            "Build complete application inventory: tech stack, VM count, DB type, licensing, dependencies",
            "Identify Oracle, SAP, and other workloads requiring specialist input",
            "Conduct dependency mapping workshops with your application owners",
            "Deliver: Infrastructure Discovery Report + Application Inventory Workbook",
        ],
        "What you need to provide:", [
            "Firewall change approval (outbound port 443) — submit CAB request on Day 1",
            "Access to vCenter / VMware / hypervisor environments",
            "Application owner availability (2 × 2-hour workshops)",
            "CMDB export or equivalent — even if incomplete (we cross-validate)",
            "IT Director's time for weekly 30-minute status call",
            "",
            "\"We will almost certainly find more infrastructure than your CMDB shows. In our reference engagement, we discovered 57% more VMs than the customer's records showed.\"",
        ], F, notes="The CMDB point is important — reassure them this is normal. The key ask is the firewall CAB approval on Day 1. Some enterprises have 10–15 business day CAB windows.")

    table_slide(prs, "Phase 2 Analysis — Cloud Readiness Scoring across 5 dimensions",
        ["Dimension", "What It Measures", "Output Category"],
        [
            ["Technical Complexity", "Containerisation readiness, OS compatibility, architecture patterns", "Cloud Ready / Friendly / Challenged / Blocked"],
            ["Business Criticality", "RTO/RPO requirements, tier classification, business impact", "Drives wave sequencing in Phase 4"],
            ["Data Sensitivity", "Regulatory, compliance, sovereignty constraints (GDPR, FCA, etc.)", "Flags sovereignty-constrained workloads"],
            ["Dependency Risk", "Tightly coupled dependencies that constrain cloud placement", "Identifies apps that must migrate together"],
            ["Licence Risk", "Oracle, Microsoft, IBM licences with cloud mobility restrictions", "Triggers Oracle Practice Lead escalation"],
        ], F, col_widths=[Inches(2.8), Inches(5.8), Inches(4.2)],
        intro_text="Governance Maturity Assessment: 6 domains assessed (IAM · Security · Change · Monitoring · FinOps · Operations) on 1–5 scale",
        notes="Readiness scoring surprises customers. In practice 15–25% are Cloud Challenged and 5–10% are Blocked. Value is knowing this before committing to a migration programme.")

    table_slide(prs, "Phase 3 Evaluation — A 7-layer cost model you can present to your board",
        ["Layer", "What It Models", "Why It Matters"],
        [
            ["(a) Like-for-Like Baseline", "Exact current specification, lifted to cloud", "The starting point — cost of doing nothing extra"],
            ["(b) Optimised / Right-Sized", "Cloud-right-sized instances based on P95 utilisation data", "Typically 20–35% lower than like-for-like"],
            ["(c) Delta (b minus a)", "The financial benefit of right-sizing alone", "Headline 'cloud saving' number"],
            ["(d) Licensing Overlay", "SQL Server AHB, Oracle BYOL, Windows AHB", "Often the single largest cost item in Microsoft-heavy estates"],
            ["(e) On-Premises Status Quo", "Current hardware + maintenance + facilities + software (3yr)", "Establishes the true cost of staying on-premises"],
            ["(f) Year 1 Dual-Running", "Cloud costs + remaining on-prem during migration overlap", "Prevents 'it cost more in Year 1 than expected' problem"],
            ["(g) Partner Discounts & Credits", "AMM / MAP / PSO funding applied", "Net cost after partner funding — the board-level headline number"],
        ], F, col_widths=[Inches(3.2), Inches(5.0), Inches(4.6)],
        intro_text="Most cloud cost estimates only cover 2 of these 7 layers. The difference between layers (a) and (g) is typically 40–60% for a Microsoft-heavy estate with AMM funding.",
        notes="Walk through each layer. Licensing overlay (d) is where largest surprises are. Layer (e) makes the stay-on-prem option visible. Layer (g) is what goes to the board.")

    content_slide(prs, "Phase 3 Evaluation — How we choose the right cloud for your estate", [
        "\"The recommendation follows the evidence. We do not start with a preferred cloud and build a case for it. We build the evidence and let it lead to the recommendation.\"",
        "",
        "Evaluation criteria (agreed with you BEFORE scoring begins):",
        "  · Technical compatibility with your estate",
        "  · 3-year Total Cost of Ownership",
        "  · Regulatory and compliance fit",
        "  · Azure Hybrid Benefit / licensing optimisation",
        "  · Migration complexity and tooling",
        "  · Hyperscaler roadmap and services",
        "",
        "All three hyperscalers are scored — we never eliminate options before the evidence is presented.",
        "The recommendation slide comes AFTER the evidence slides — not before."
    ], F, notes="The 'criteria agreed before scoring' point is critical. If customer asks 'how do I know the recommendation wasn't pre-determined?' — the answer is that weighting is agreed in writing before scoring starts.")

    content_slide(prs, "Phase 4 Planning — From Recommendation to Migration Roadmap", [
        "MIGRATION WAVE PLAN: Applications sequenced by readiness score · business criticality · dependency clusters · environment readiness",
        "   Wave 0 (PoC) → Wave 1 (Cloud Ready, Tier-3) → Wave 2–3 (Medium complexity) → Wave 4 (Tier-1 business-critical) → Wave 5+ (Oracle/specialist)",
        "",
        "RISK REGISTER: 11 risk categories documented, scored, and mitigated",
        "   Technical · Dependency · Licensing (Oracle) · Data Quality · End-of-Life OS · Regulatory · Schedule · Resource · Commercial · Stakeholder · Third-Party",
        "",
        "PART 2 ENTRY POINT: The commercial document that defines the migration engagement",
        "   Scope and wave sequence · Timeline and resource model · Investment summary (net of partner funding) · Hyperscaler partner registration status · Next steps and signatures"
    ], F, notes="Phase 4 is where the assessment becomes a programme. Wave plan is what the customer's IT Programme Manager will use. Wave 0 is deliberate — do not put critical applications in Wave 0.")

    table_slide(prs, "Eight formal deliverables. All board-grade.",
        ["#", "Deliverable", "Format", "Phase"],
        [
            ["1", "Application & Infrastructure Inventory", "Excel workbooks (3 files)", "Phase 1"],
            ["2", "Phase 1 Discovery Report", "Word document, 20–30 pages", "Phase 1"],
            ["3", "Cloud Readiness Scores", "Excel workbook", "Phase 2"],
            ["4", "Governance Maturity Assessment", "Excel workbook + workshop summary", "Phase 2"],
            ["5", "TCO Analysis — All 7 Layers", "Excel workbook (per hyperscaler)", "Phase 3"],
            ["6", "Cloud Readiness Assessment Report", "Word document, 40–60 pages", "Phase 3"],
            ["7", "Executive Summary Presentation", "PowerPoint deck, 18 slides", "Phase 3"],
            ["8", "Part 2 Entry Point (migration SOW)", "Word document, 8–12 pages", "Phase 4"],
        ], F, col_widths=[Inches(0.6), Inches(4.6), Inches(3.8), Inches(3.7)],
        notes="Walk through each deliverable and who in the customer's organisation will use it. Every deliverable has a named audience and specific use case.")

    content_slide(prs, "A reference engagement — four phases, every deliverable, a real outcome", [
        "A UK digital media group — one of the UK's largest digital publishing organisations",
        "On-premises VMware estate, 2 UK data centres",
        "",
        "Discovery:  4,200+ VMs · 280 applications · 18 Oracle RAC clusters · 57% more infrastructure than CMDB showed",
        "Analysis:   Cloud Readiness Scores for all 280 applications · Governance maturity across all 6 domains",
        "Evaluation: 3-way TCO model (Azure vs AWS vs GCP) across 9 regions · Hyperscaler recommendation with full evidence trail",
        "Planning:   Partner funding identified and pre-registered · Migration wave plan produced",
        "",
        "\"A board-ready business case, an evidence-backed hyperscaler recommendation, a migration wave plan for 280 applications, and identification of seven-figure partner funding eligibility — all within a 16-week structured engagement.\""
    ], F, notes="Do not name the customer unless approved for external sharing. Reference as 'a UK digital media group.' The 57% scope variance figure is particularly important for customers who think their CMDB is reliable.")

    content_slide(prs, "Indicative engagement timeline — [Customer Name]", [
        "MONTH 1:  Phase 1 begins · Discovery tooling deployed · CAB change approved",
        "WEEK 6:   Phase 2 begins (parallel to Phase 1)",
        "WEEK 7:   Utilisation data window complete (≥14 days clean data)",
        "WEEK 8:   Phase 1 Discovery Report delivered",
        "WEEK 11:  Phase 2 Analysis complete · Cloud Readiness Scores delivered",
        "WEEK 14:  Phase 3 TCO Analysis complete",
        "WEEK 14:  Executive playback: hyperscaler recommendation presented",
        "WEEK 20:  Part 2 Entry Point signed · Migration engagement begins",
        "",
        "Note: Timeline is customised per engagement. Oracle estates, large CMDB gaps, or complex regulatory requirements may adjust specific phases.",
        "Phases 1 and 2 run in parallel from Week 6 — standard for mid-market estates."
    ], F, notes="Customise week numbers to customer's specific situation. If large Oracle estate, Phase 2 takes longer. Agree any timeline changes in the Statement of Work.")

    table_slide(prs, "You may be eligible for significant partner programme funding",
        ["Programme", "What It Covers", "CRA Requirement"],
        [
            ["Microsoft Azure — AMM", "Typically covers 10–30% of migration services cost", "Pre-registration before migration engagement begins — CRA produces all required documentation"],
            ["AWS — MAP (Migration Acceleration Programme)", "Financial assistance and technical support for migration to AWS", "Deal registration in AWS ACE portal at engagement start — CRA Assessment maps to MAP Assess"],
            ["Google Cloud — PSO Credits / RAMP", "Migration credits and PSO support against GCP consumption", "CRA outputs qualify for RAMP consideration — opportunity registration at Phase 1"],
        ], F, col_widths=[Inches(3.0), Inches(4.8), Inches(5.0)],
        intro_text="Partner programme eligibility is confirmed by Rackspace before the Part 2 SOW is signed. All applicable programmes are pre-registered at Phase 1 kickoff.",
        notes="Every customer should be screened. Most common reason organisations miss AMM or MAP: nobody pre-registered. Rackspace includes this as standard in the CRA scoping process.")

    table_slide(prs, "From this conversation to a signed Statement of Work",
        ["Step", "What Happens", "Timeline"],
        [
            ["Scoping Workshop", "Validate estate size · Screen for Oracle/SAP · Confirm partner funding eligibility · Agree engagement timeline", "1–2 days after this meeting"],
            ["Statement of Work", "Fixed-fee SOW: agreed scope · phase deliverables · acceptance criteria · timeline · partner funding plan · scope variance clause", "Within 1 week of scoping"],
            ["Phase 1 Kickoff", "Tooling deployment plan agreed · CAB change request submitted by customer IT on Day 1 · Alliance Manager pre-registers with hyperscaler(s) · First status call", "Within 2 weeks of SOW signature"],
        ], F, col_widths=[Inches(2.8), Inches(7.0), Inches(3.2)],
        intro_text="Ready to begin? Contact [your name] at [email] to schedule the scoping workshop.",
        notes="Close by confirming the scoping workshop. Goal: signed SOW within 2 weeks of this meeting. Do not leave without a next action owner and a date.")


# ── Deck: CRA Technical Overview ──────────────────────────────────────────────

def build_technical(prs):
    F = "© 2026 Rackspace Technology — CRA Framework v2.0"

    title_slide(prs, "Cloud Readiness Accelerator — Technical Framework Overview",
        "Methodology, templates, tooling, and delivery guide for CRA practitioners",
        "Rackspace Cloud Solutions Architecture | CRA Framework v2.0",
        F, notes="Practitioner deck. Audience: SAs, delivery architects, or technical alliance partners. Goal: full framework literacy. Someone completing this session should be able to lead a Phase 1 kickoff the following Monday without further briefing.")

    content_slide(prs, "Agenda — What we will cover today (60 minutes)", [
        "1. Framework architecture — phases, gates, and parallelisation model (5 min)",
        "2. Phase 1 Deep Dive — Discovery tooling, data collection, quality gates (10 min)",
        "3. Phase 2 Deep Dive — Readiness scoring, governance workshop, OSS flag (10 min)",
        "4. Phase 3 Deep Dive — TCO 7-layer model, hyperscaler matrix, recommendation protocol (15 min)",
        "5. Phase 4 Deep Dive — Wave planning, risk register, Part 2 Entry Point (10 min)",
        "6. Templates — the 15 critical files and what each produces (5 min)",
        "7. Failure modes — DMG Media UK lessons learned (5 min)",
    ], F, notes="Set expectations: 60 minutes, 25 slides. Phase 3 section is densest and most important — do not rush it. Failure modes at the end is the most practically valuable.")

    content_slide(prs, "Four phases, two gates, one parallelisation point", [
        "PHASE 1: DISCOVERY (Wks 1–7): Azure Migrate / GCP Migration Center / AWS ADS · VM + app + network utilisation data · App inventory",
        "PHASE 2: ANALYSIS (Wks 6–10): Cloud readiness scoring (5 dims) · Governance maturity assessment · Dependency analysis · OSS licence flags",
        "PHASE 3: EVALUATION (Wks 11–14): 7-layer TCO model per hyperscaler · Hyperscaler decision matrix + scoring · Recommendation with evidence",
        "PHASE 4: PLANNING (Wks 11–20): Migration wave plan · Risk register · Governance model · Part 2 Entry Point",
        "",
        "PARALLELISATION: Phase 2 starts at Phase 1 Week 6 — do not wait for Phase 1 to complete",
        "GATE 1 (hard): ≥14 days clean utilisation data for ≥90% of VMs before Phase 3",
        "GATE 2 (pre-commercial): Alliance partner deal registration COMPLETE before Part 2 SOW countersignature",
    ], F, notes="Parallelisation at Week 6 is most commonly missed. Waiting for Phase 1 to fully complete before starting Phase 2 wastes 4–6 weeks. By Week 6 you have enough inventory to begin readiness scoring on first cohort.")

    content_slide(prs, "Phase 1 is a data quality project, not a documentation project", [
        "Core objective: Produce a complete, accurate, validated inventory of every server, application, dependency, and licensing obligation — with ≥14 days clean CPU/RAM/storage/network utilisation data from ≥90% of in-scope VMs.",
        "",
        "THREE WORKSTREAMS RUNNING SIMULTANEOUSLY:",
        "  · Infrastructure discovery tooling → VM specs, OS, hypervisor, utilisation data, storage I/O",
        "  · Application inventory → tech stack, DB, VM count, readiness flag, dependencies",
        "  · Dependency mapping (with app owners) → dependency heat map, tightly-coupled clusters",
        "",
        "Critical: Serialising these workstreams costs 4–6 weeks. Application workshops CAN start at Week 2 while tooling is still collecting data.",
    ], F, notes="The three workstreams must run simultaneously. Common failure: finish infrastructure discovery, then application inventory, then dependencies. This serialisation costs 4–6 weeks.")

    table_slide(prs, "Phase 1 — Choose the right discovery tool for the target hyperscaler",
        ["Tool", "Hyperscaler", "Deployment", "Key Output"],
        [
            ["Azure Migrate", "Azure primary", "Agent or agentless (vCenter connector)", "infrastructure-profiling.xlsx source data"],
            ["AWS ADS (App Discovery Service)", "AWS primary", "Agent-based or Agentless Connector", "aws-evaluation.xlsx input"],
            ["GCP Migration Center", "GCP primary", "VM Manager agent or RVTools import", "gcp-evaluation.xlsx input"],
            ["RVTools", "All hyperscalers", "VMware utility — no agent needed", "Cross-validation of all discovery tools"],
        ], F, col_widths=[Inches(2.8), Inches(2.2), Inches(3.8), Inches(4.0)],
        intro_text="Run RVTools export on Day 1 regardless of target hyperscaler. Discrepancies between RVTools and discovery tool output indicate incomplete agent deployment or shadow VMs. Submit firewall CAB request on Day 1 — can take 5–15 business days to approve.",
        notes="CAB request is the single biggest schedule risk in Phase 1. Submit on Day 1 based on target URLs, even before appliance is live.")

    table_slide(prs, "Phase 1 — Application inventory: 10 critical columns of 25",
        ["Column", "Description", "Why Critical"],
        [
            ["Application Name", "Official application name", "Primary key — all other templates reference this"],
            ["Business Owner", "Named owner — not a team", "Drives governance workshop invitations in Phase 2"],
            ["Application Tier", "Tier 1 (mission-critical) / 2 / 3", "Drives wave sequencing in Phase 4"],
            ["Primary VM Count", "Number of VMs supporting this application", "Feeds TCO model and scope validation"],
            ["Database Type", "Oracle / SQL Server / PostgreSQL / MySQL / NoSQL", "Oracle flag — escalate immediately if Oracle RAC/EE"],
            ["Oracle Practice Flag", "Yes / No", "If Yes: engage Oracle Practice Lead in Phase 1 Week 2"],
            ["OSS Licence Risk Flag", "Yes / No / Review", "Redis OSS, Elasticsearch, HashiCorp Vault — licence change risk"],
            ["Scope Confidence", "High / Medium / Low", "Data from CMDB = Low; data from tooling = High"],
            ["Cloud Readiness (P1 estimate)", "Preliminary score from Phase 1 data", "Used to prioritise Phase 2 readiness scoring"],
            ["Dependency Cluster", "Cluster ID (groups tightly-coupled apps)", "Cannot separate these in wave planning"],
        ], F, col_widths=[Inches(2.8), Inches(4.5), Inches(5.5)],
        notes="Oracle Practice Flag is the most important column. Any Oracle RAC or Oracle EE finding → escalate same day. Oracle licensing analysis takes 4–6 weeks.")

    content_slide(prs, "GATE 1 — Phase 3 cannot start without this", [
        "Utilisation data collection period: ≥14 days continuous clean data",
        "VM coverage: ≥90% of in-scope VMs reporting",
        "CPU data quality: P95 values available for ≥90% of VMs",
        "RAM data quality: P95 values available for ≥90% of VMs",
        "Storage I/O data: available for VMs flagged as I/O-sensitive",
        "",
        "WHY THE GATE IS HARD:",
        "\"Using 6 days of data instead of 14 produces right-sizing recommendations with ±30–50% error. At 500 VMs, that is a £2M–£5M range in the business case — not acceptable at board level.\"",
        "",
        "When customer pushes to skip: quantify the risk in writing → offer an interim (share Phase 1 report while data collection continues) → document customer's decision if they override",
    ], F, notes="This is a real conversation you will have on most engagements. The data window is the line you do not move. The DMG engagement had this exact conversation — window was held, TCO was accurate.")

    table_slide(prs, "Phase 2 — Five-dimension scoring model",
        ["Dimension", "Scale", "Low Score Means"],
        [
            ["Technical Complexity", "1 (complex) – 5 (simple)", "Legacy OS, custom middleware, tightly-coupled architecture, bare-metal requirements"],
            ["Business Criticality", "1 (critical) – 5 (non-critical)", "RTO < 4hrs, RPO < 1hr, zero-downtime migration required"],
            ["Data Sensitivity", "1 (highly sensitive) – 5 (non-sensitive)", "PII, financial data, FCA-regulated data, GDPR sovereignty constraints"],
            ["Dependency Risk", "1 (high dependency) – 5 (low dependency)", "Many tightly-coupled dependencies, on-prem latency requirements"],
            ["Licence Risk", "1 (high risk) – 5 (low risk)", "Oracle RAC, Oracle EE, IBM ILMT, Windows Server (without AHB), SAP"],
        ], F, col_widths=[Inches(2.8), Inches(2.8), Inches(7.2)],
        intro_text="Composite score: 4.0–5.0 = Cloud Ready · 3.0–3.9 = Cloud Friendly · 2.0–2.9 = Cloud Challenged · 1.0–1.9 = Blocked",
        notes="Individual dimension scores are as important as composite. Any Licence Risk score of 1 or 2 requires Oracle or Commercial Practice Lead before Phase 3 TCO is built.")

    content_slide(prs, "Phase 2 — The commercial licence time bomb you must not miss", [
        "OSS LICENCE CHANGES (2023–2024) that affect cloud deployments:",
        "",
        "  Redis OSS (post v7.4): SSPL/RSALv2 — requires paid licence for commercial use",
        "  Elasticsearch (post 7.10): SSPL — check if using elastic.co or AWS OpenSearch fork",
        "  HashiCorp Vault / Terraform: BSL — commercial use restrictions at scale",
        "  MongoDB: SSPL — validate which version and applicable managed service",
        "",
        "Action trigger: ANY OSS Licence Risk Flag → immediate commercial review in Phase 2 before TCO is built",
        "",
        "DMG Media UK: 140+ Redis instances identified. Had licence risk been missed and deployed at scale, commercial exposure would have been significant.",
        "The OSS flag column in the application inventory exists specifically because of this engagement.",
    ], F, notes="Real DMG finding. The OSS flag column in application inventory exists because of this engagement. Flag in Phase 1, resolve in Phase 2, model correct cost in Phase 3.")

    table_slide(prs, "Phase 3 — The 7-layer TCO model: why each layer exists",
        ["Layer", "Tab Name", "Common Mistake"],
        [
            ["(a) Like-for-Like", "L4L-Baseline", "Using rounded estimates instead of actual P95 utilisation"],
            ["(b) Optimised", "Optimised-Rightsized", "Using P50 (median) instead of P95 — underestimates required size"],
            ["(c) Delta", "Calculated (b-a)", "Presenting this as 'the saving' without showing layers d–g"],
            ["(d) Licensing Overlay", "Licensing-Overlay", "Omitting Oracle BYOL licensing premium/saving"],
            ["(e) On-Prem Status Quo", "OnPrem-StatusQuo", "Using standard depreciation without including hardware refresh cycle"],
            ["(f) Year 1 Dual-Running", "Year1-DualRunning", "Omitting parallel environment costs (most common budget shock)"],
            ["(g) Partner Credits", "Partner-Credits", "Building the board case without this — largest headline number driver"],
        ], F, col_widths=[Inches(2.4), Inches(3.2), Inches(7.2)],
        intro_text="TCO-Summary tab produces the board-level number: 3yr net cost cloud (post-partner funding) vs 3yr on-prem status quo. Template: business-case-tco-roi.xlsx",
        notes="Walk through why each layer is included. Layer (e) is often most surprising — customers rarely have full view of current infrastructure costs including hardware refresh and VMware licence renewal.")

    content_slide(prs, "Phase 3 — Hyperscaler Decision Matrix: 9 required tabs", [
        "Criteria-Weights — customer-agreed weighting, agreed BEFORE scoring",
        "Azure-Evaluation — Azure-specific scores with evidence references",
        "AWS-Evaluation — AWS-specific scores with evidence references",
        "GCP-Evaluation — GCP-specific scores with evidence references",
        "Comparative-Matrix — side-by-side weighted scores across all three",
        "7Rs-Estate-View — each app classified: Rehost/Replatform/Rearchitect/Repurchase/Retire/Retain/Relocate",
        "Multi-Cloud-Exceptions — apps that cannot go to primary cloud with rationale",
        "Worked-Example — anonymised DMG Media UK scoring (reference and calibration)",
        "Instructions — read before scoring",
        "",
        "CRITICAL: Criteria weights agreed in writing BEFORE scoring · All 3 clouds scored · Every score has evidence reference · Recommendation slide AFTER evidence slides · Matrix score and recommendation are consistent"
    ], F, notes="Evidence-before-recommendation is the most important quality rule in the framework. DMG engagement had an early draft with recommendation early — restructured before customer saw it.")

    content_slide(prs, "Phase 4 — Wave sequencing principles", [
        "Wave 0 (PoC, 8–12 wks): Non-production · 5–10% of estate · Dev/Test · simple Tier-3 apps · NOT Tier-1",
        "Wave 1: Cloud Ready · low dependency · Tier-3 · internal tools, simple web apps",
        "Wave 2: Cloud Friendly · low-medium complexity · mid-tier apps · some dependencies",
        "Wave 3: Cloud Challenged or medium-high complexity · custom middleware · tighter RTO",
        "Wave 4: Tier-1 business-critical · ERP, CRM, core business systems",
        "Wave 5+: Retained · Oracle specialist · multi-cloud exceptions",
        "",
        "HARD RULES:",
        "  · Do NOT put Tier-1 applications in Wave 0 — this is a PoC, not a migration",
        "  · Do NOT put Oracle RAC clusters in Wave 1 — Oracle specialist migration path required",
        "  · Dependency clusters must move TOGETHER — never split across waves",
    ], F, notes="Hardest conversation in Phase 4: moving customer's favourite application out of Wave 0. 'Let's start with SAP to prove the value' — SAP in Wave 0 is a recipe for expensive failed PoC.")

    table_slide(prs, "Phase 4 — Eleven risk categories you must cover",
        ["Category", "Example Risk", "Default Likelihood", "Default Impact"],
        [
            ["Scope", "Estate larger than scoped in SoW", "High (4)", "High (4)"],
            ["Data Quality", "Utilisation data < 14 days clean", "Medium (3)", "Critical (5)"],
            ["Dependency", "Undocumented dependencies block wave sequencing", "Medium (3)", "High (4)"],
            ["Licensing", "Oracle EE licence not cloud-portable", "Medium (3)", "Critical (5)"],
            ["End-of-Life OS", "Windows Server 2012 / RHEL 6 ESU required", "High (4)", "High (4)"],
            ["Regulatory", "Data sovereignty blocks primary cloud region", "Low (2)", "Critical (5)"],
            ["Schedule", "CAB approval delays Phase 1 by ≥2 weeks", "Medium (3)", "Medium (3)"],
            ["Commercial", "Partner deal registration missed before Part 2 SOW", "Low (2)", "High (4)"],
        ], F, col_widths=[Inches(2.2), Inches(5.8), Inches(2.5), Inches(2.3)],
        intro_text="Risk scoring: Likelihood × Impact = Risk Score. Score ≥9 = Red · 6–8 = Amber · ≤5 = Green. Pre-populate all 11 risk categories on every engagement.",
        notes="Pre-populate register with these 11 default risks in every engagement. Oracle licensing and scope risk are most commonly underestimated in mid-market assessments.")

    table_slide(prs, "The 15 critical templates — every CRA deliverable traces to these",
        ["#", "Template", "Phase", "What It Produces"],
        [
            ["1", "application-scoping-profiling.xlsx", "Phase 1", "Application inventory, Oracle flags, readiness estimate"],
            ["2", "infrastructure-profiling.xlsx", "Phase 1", "VM specs, OS, utilisation data, Data Quality Summary"],
            ["3", "dependency-mapping.xlsx", "Phase 1", "App-to-app and app-to-infra dependency heat map"],
            ["4", "cloud-readiness-scoring-v2.xlsx", "Phase 2", "5-dimension readiness scores per application"],
            ["5", "governance-foundations-alignment.xlsx", "Phase 2", "Governance maturity scores, 6 domains, 1–5 scale"],
            ["6", "risk-assessment.xlsx", "Phase 2+4", "Risk register, 11 categories, likelihood × impact"],
            ["7", "azure-evaluation.xlsx", "Phase 3", "Azure TCO: PAYG + RI + AHB overlay"],
            ["8", "aws-evaluation.xlsx", "Phase 3", "AWS TCO: On-Demand + RI + Savings Plans"],
            ["9", "gcp-evaluation.xlsx", "Phase 3", "GCP TCO: On-Demand + 3yr CUDs"],
            ["10", "business-case-tco-roi.xlsx", "Phase 3", "7-layer TCO: all 3 clouds, all layers, 3yr summary"],
            ["11", "hyperscaler-decision-matrix.xlsx", "Phase 3", "Weighted scores, 7Rs classification, recommendation"],
            ["12", "migration-wave-planner.xlsx", "Phase 4", "Wave sequence, timeline, resource model, rollback plan"],
        ], F, col_widths=[Inches(0.5), Inches(4.5), Inches(1.8), Inches(6.0)],
        notes="Know these 15 templates well. Every CRA deliverable traces back to one or more of them. Most important for board: #1, 2, 10, 11, and the report/exec summary.")

    table_slide(prs, "Nine lessons from a real engagement — embedded in your framework now",
        ["#", "Lesson", "Template/Process Updated"],
        [
            ["1", "Scope variance: 57% more VMs than SoW (budget overrun risk)", "Scope variance clause in SoW · confidence scoring in app inventory"],
            ["2", "CAB request not submitted Day 1 → 2-week delay", "Phase 1 kickoff checklist — CAB on Day 1"],
            ["3", "Oracle RAC found in Phase 1 Week 5 → Oracle analysis delayed Phase 3 by 6 weeks", "Oracle Practice Flag column in application inventory"],
            ["4", "Redis OSS licence change discovered in Phase 3 → TCO re-work", "OSS Licence Risk column in application inventory"],
            ["5", "AMM not pre-registered at Phase 1 → customer missed AMM funding", "AMM registration at Phase 1 kickoff · Alliance Manager on Day 1 call"],
            ["6", "Utilisation data window shortened under pressure → TCO accuracy compromised", "Gate 1 hard requirement · written escalation process"],
            ["7", "Phase 2 not started until Phase 1 complete → 4-week delay", "Parallelisation model: Phase 2 starts at Phase 1 Week 6"],
            ["8", "EoL OS not flagged until Phase 3 → ESU costs missed in TCO", "EoL OS column in infrastructure-profiling · EoL flag in risk register"],
            ["9", "Recommendation before evidence → customer challenged credibility", "Evidence-before-recommendation rule · deck structure validation checklist"],
        ], F, col_widths=[Inches(0.4), Inches(7.2), Inches(5.2)],
        notes="This is the most important slide for practitioners. Every lesson resulted in a concrete change to the framework. After your next CRA engagement, identify one new lesson and embed it.")

    content_slide(prs, "The Alliance Manager is a Phase 1 team member — not a Phase 3 afterthought", [
        "COMMON MISTAKE: Alliance Manager briefed at Phase 3 when recommendation is known. By then, deal registration windows for AMM/MAP/PSO may have closed.",
        "",
        "Pre-engagement (SoW scoping): Screen for AMM/MAP/PSO eligibility · advise on deal registration requirements",
        "Phase 1 Day 1: Pre-register opportunity in Microsoft MSPP / AWS ACE / Google Partner Advantage",
        "Phase 1 Week 2: Confirm registration is active and acknowledged by hyperscaler partner team",
        "Phase 3 (recommendation complete): Update deal registration with actual recommended cloud and scope",
        "Phase 4 (Part 2 Entry Point): Confirm deal registration status for Section 5 of Part 2 Entry Point",
        "",
        "GATE 2 REMINDER: AMM/MAP/PSO registration MUST be complete before Rackspace countersigns the Part 2 SOW.",
        "Missing AMM registration cost a real engagement access to potential seven-figure funding."
    ], F, notes="The Alliance Manager must be ON the Phase 1 kickoff call. Not briefed before. On the call. This is the one practice change with highest commercial impact.")

    content_slide(prs, "EoL OS — the Azure cost advantage that gets missed in TCO", [
        "Windows Server 2012/R2 EoL (Oct 2023): ESU FREE in Azure until 2026 · On AWS/GCP: customer pays Microsoft",
        "SQL Server 2012/2014 EoL (Jul 2022/2024): ESU FREE in Azure · On AWS/GCP: paid to Microsoft",
        "RHEL 6 (Nov 2020 EoL): RHEL ELS subscription required on any cloud",
        "Ubuntu 18.04 LTS (Apr 2023 EoL): Ubuntu Pro subscription required for ESU",
        "",
        "TCO impact for a 200-EoL-server estate: Azure ESU = £0 · AWS or GCP = £60K–£120K additional cost (3yr)",
        "",
        "CRA Action: Flag all EoL OS in Phase 1 → include in risk register → model ESU cost (or Azure ESU saving) in Phase 3 TCO Licensing Overlay",
        "",
        "This is a legitimate Azure cost advantage that belongs in the TCO model. Do not omit it because it appears to favour Azure — present the evidence and let the data drive the recommendation."
    ], F, notes="For Microsoft-heavy estate, ESU difference between Azure (free) and AWS/GCP (paid) can be £300K–£500K over 3 years. Must appear in TCO model.")

    content_slide(prs, "Pre-playback QA checklist — 10 checks before presenting Phase 3", [
        "☐ 1. ≥14 days clean utilisation data confirmed for ≥90% of VMs",
        "☐ 2. All 7 TCO layers populated for each cloud — no blank rows",
        "☐ 3. Pricing validated against calculator source this week",
        "☐ 4. AHB eligibility confirmed (SA status verified with customer)",
        "☐ 5. Oracle licensing reviewed by Oracle Practice Lead — email sign-off filed",
        "☐ 6. OSS licence flags resolved — all modelled in TCO",
        "☐ 7. Hyperscaler matrix weights agreed in writing by customer — sign-off email filed",
        "☐ 8. All three clouds scored with evidence references — no blank evidence fields",
        "☐ 9. Recommendation slide comes AFTER evidence slides (slide ≥13)",
        "☐ 10. AMM/MAP/PSO registration confirmed by Alliance Manager — email filed",
        "",
        "This checklist is not optional before presenting to a customer CTO. A missing check is a quality failure. If you cannot complete all 10, delay the playback."
    ], F, notes="Two most commonly missed: check 9 (recommendation slide order) and check 10 (Alliance Manager confirmation).")

    content_slide(prs, "What you should be able to do now", [
        "1. LEAD A PHASE 1 KICKOFF — knowing to submit the CAB request Day 1, escalate Oracle in Week 1–2, and start Phase 2 at Week 6",
        "   Reference: docs/guides/01-discovery-phase-guide.md",
        "",
        "2. EXPLAIN THE 7-LAYER TCO MODEL to a CFO without internal jargon — and explain why layers d–g matter more than a–c",
        "   Reference: Templates/03-evaluation/TCO-TEMPLATES-AUDIT-SPEC.md",
        "",
        "3. RUN A CREDIBLE HYPERSCALER EVALUATION with customer-agreed criteria weights and evidence-referenced scores — recommendation after evidence",
        "   Reference: Templates/03-evaluation/HYPERSCALER-TEMPLATES-AUDIT-SPEC.md",
        "",
        "4. HOLD GATE 1 when a customer pushes to skip the utilisation data window — using the quantified accuracy argument",
        "   Reference: docs/guides/03-evaluation-phase-guide.md",
        "",
        "5. ESCALATE ORACLE, OSS, AND EoL OS FINDINGS at the right moment — not when they become critical path blockers",
        "   Reference: docs/DMG-MEDIA-UK-LESSONS-LEARNED.md",
        "",
        "\"The framework is only as good as the architects who use it with rigour. Every gate exists because someone pushed through it and paid the price on a real engagement.\""
    ], F)


# ── Deck: Microsoft Partner ────────────────────────────────────────────────────

def build_microsoft(prs):
    F = "Rackspace × Microsoft — Cloud Partner Alliance"

    title_slide(prs, "Cloud Readiness Accelerator",
        "How Rackspace CRA drives Azure-first outcomes, AMM funding eligibility, and structured co-sell with Microsoft",
        "Rackspace Cloud Solutions Architecture + Alliance | [Date]",
        F, accent=AZURE, notes="This deck is for Microsoft PDMs and STU architects. Goal: Microsoft team confident that CRA-delivered assessments produce the right artefacts for AMM deal registration and credible Azure recommendations.")

    content_slide(prs, "Every structured assessment is a co-sell opportunity waiting to be activated", [
        "THE GAP WE FILL: Microsoft SMART takes 15 minutes and identifies Azure fit at a surface level. For 50+ application estates with Oracle/SAP, SMART is top-of-funnel — not a decision-making tool. Rackspace CRA is what happens next.",
        "",
        "THE RACKSPACE ROLE: Independent trusted advisor. No hyperscaler quota. When data points to Azure (most Microsoft-heavy estates with AHB opportunity), customers receive a credible, evidence-based Azure recommendation that Microsoft can confidently co-sell with.",
        "",
        "THE MICROSOFT VALUE: CRA-delivered assessments produce all documentation required for AMM programme funding eligibility. Every CRA engagement with an Azure recommendation is a pre-qualified AMM conversation.",
        "",
        "\"SMART generates the lead. CRA qualifies it. AMM funds the migration. Rackspace delivers it.\""
    ], F, accent=AZURE, notes="This is the co-sell value chain in one sentence. The Microsoft PDM's role: ensure AMM registration is active from Phase 1 kickoff.")

    table_slide(prs, "CRA phases map directly to Microsoft Cloud Adoption Framework stages",
        ["CAF Stage", "CRA Phase", "CRA Deliverables That Satisfy It"],
        [
            ["Strategy", "Pre-engagement scoping", "Business drivers workshop · scope statement · stakeholder alignment"],
            ["Plan", "Phase 1 Discovery + Phase 2 Analysis", "Application inventory · infrastructure profiling · 5-dimension readiness scores · dependency map"],
            ["Ready", "Phase 3 Evaluation", "Right-sizing recommendations · Azure architecture alignment · AHB model · AMM eligibility screen"],
            ["Migrate", "Phase 4 Planning", "Migration wave plan · Part 2 Entry Point · risk register · governance charter"],
            ["Govern", "Phase 4 Planning (governance output)", "Governance model · RACI · operating model design"],
            ["Manage", "Post-CRA (Part 2 operations)", "Baseline for ongoing managed services handoff"],
        ], F, accent=AZURE, col_widths=[Inches(2.0), Inches(3.2), Inches(7.6)],
        notes="This is the key conversation for Microsoft PDMs. CRA deliverables map to every CAF stage. Phase 1+2 outputs match CAF Plan stage requirements for AMM deal registration.")

    table_slide(prs, "CRA produces every artefact required for AMM programme eligibility",
        ["AMM Requirement", "CRA Output", "CRA Template"],
        [
            ["Documented assessment methodology", "CRA METHODOLOGY.md + phase guides", "docs/METHODOLOGY.md"],
            ["Application and infrastructure inventory", "Application inventory + Infrastructure profiling", "application-scoping-profiling.xlsx + infrastructure-profiling.xlsx"],
            ["Multi-dimensional readiness assessment", "5-dimension cloud readiness scores per application", "cloud-readiness-scoring-v2.xlsx"],
            ["TCO / ROI analysis", "7-layer TCO: Azure, AWS, GCP comparison", "business-case-tco-roi.xlsx"],
            ["Azure as primary recommendation", "Hyperscaler decision matrix + assessment report", "hyperscaler-decision-matrix.xlsx + report"],
            ["Migration wave plan", "Sequenced application migration plan", "migration-wave-planner.xlsx"],
            ["Partner co-sell designation", "Rackspace Microsoft partner status ✓", "Rackspace partner tier documentation"],
        ], F, accent=AZURE, col_widths=[Inches(3.5), Inches(5.0), Inches(4.3)],
        intro_text="A CRA-delivered assessment does not require additional documentation to support an AMM funding request. No post-assessment rework.",
        notes="CRA was designed with AMM outputs in mind. Every required piece of evidence has a named template. Bring MICROSOFT-CAF-ALIGNMENT.md to any PDM technical review.")

    content_slide(prs, "Azure Hybrid Benefit — modelled explicitly, not forgotten", [
        "WHAT IS AHB? Microsoft licensing benefit allowing organisations with active Software Assurance to use Windows Server or SQL Server licences in Azure — eliminating licence cost from Azure VM or SQL managed service price.",
        "",
        "  Windows Server Standard/Datacenter: 15–40% VM cost reduction (requires active SA)",
        "  SQL Server Standard: ~70% cost reduction per core (requires active SA)",
        "  SQL Server Enterprise: ~70% cost reduction per core (requires active SA)",
        "",
        "HOW CRA MODELS AHB:",
        "  Phase 1: Captures all Windows Server and SQL Server versions and licence types",
        "  Phase 3: AHB eligibility screened (requires active SA confirmation from customer)",
        "  TCO Licensing Overlay tab: separate rows for PAYG vs. AHB scenarios per VM type",
        "",
        "IMPORTANT: AHB saving is only available in Azure. For Microsoft-heavy estates, this creates a legitimate structural cost advantage for Azure in the TCO model.",
        "SA status confirmation: ideally done at Phase 1 scoping — not in Phase 3."
    ], F, accent=AZURE, notes="For Microsoft-heavy estates, AHB can represent 15–25% of total 3-year TCO. Often the difference between cloud being cheaper or more expensive than on-prem.")

    table_slide(prs, "How to convert a SMART assessment into a Rackspace CRA engagement",
        ["Step", "Action", "Owner", "Timing"],
        [
            ["1", "Customer completes Microsoft SMART Assessment", "Customer (facilitated by Microsoft SE)", "Pre-engagement"],
            ["2", "SMART score Amber or below → CRA trigger", "Microsoft SE + Rackspace Pre-Sales", "Within 1 week of SMART result"],
            ["3", "Rackspace Pre-Sales conducts scoping call (1 hr)", "Rackspace Pre-Sales Architect", "Within 1 week of SMART result"],
            ["4", "Rackspace produces CRA scoping proposal", "Rackspace Pre-Sales", "Within 5 business days"],
            ["5", "Microsoft SE provides warm handoff introduction", "Microsoft SE", "With scoping proposal delivery"],
            ["6", "Customer SOW signed → CRA begins", "Customer + Rackspace", "Week 0"],
            ["7", "Alliance Manager pre-registers AMM opportunity in MSPP", "Rackspace Alliance Manager", "Day 1"],
            ["8", "Microsoft PDM acknowledges co-sell opportunity", "Microsoft PDM", "Week 1"],
            ["9", "Phase 3 playback: recommendation presented", "Rackspace Lead Architect", "Week 14"],
            ["10", "AMM funding application submitted (if Azure recommended)", "Rackspace Alliance + Microsoft PDM", "Week 14–16"],
        ], F, accent=AZURE, col_widths=[Inches(0.5), Inches(4.5), Inches(3.8), Inches(4.0)],
        notes="Warm handoff is the most important part. Customer trusts Rackspace independence because Microsoft contact introduced them. The framing: 'Rackspace evaluates all three clouds independently — we just happen to find Azure is the best fit for many Microsoft-heavy estates.'")

    content_slide(prs, "When to register in Microsoft MSPP — and why timing is critical", [
        "Phase 1 Day 1: Alliance Manager registers opportunity in MSPP Partner Center",
        "Phase 1 Week 2: Microsoft PDM confirms registration and confirms customer relationship status",
        "Phase 2 Week 10: Readiness scoring complete",
        "Phase 3 Week 11: TCO analysis complete",
        "Phase 3 Week 14: Recommendation presented to customer",
        "Phase 4 Week 18: Part 2 SOW ready",
        "",
        "WHY DAY 1 REGISTRATION IS CRITICAL: Some Microsoft AMM programmes require opportunity registration before the assessment is complete. Registering in Week 14 (after recommendation) may reduce or eliminate funding eligibility.",
        "",
        "MICROSOFT PDM ACTION REQUIRED: Acknowledge and accept co-sell opportunity in MSPP · Confirm alignment with CAM · Provide AMM programme guidance for this account tier",
    ], F, accent=AZURE, notes="Every Microsoft PDM should have the Rackspace Alliance Manager's contact before Phase 1 begins. Alliance Manager is single point of contact for AMM registration.")

    content_slide(prs, "A real engagement. A real Azure recommendation. AMM-eligible.", [
        "A UK digital media group — one of the UK's largest publishing organisations",
        "VMware on-premises estate, 2 UK data centres, 10 vCenter instances",
        "",
        "  4,200+ VMs assessed · 280 applications scoped",
        "  18 Oracle RAC clusters identified · 224 EoL OS instances (Windows Server 2012/R2)",
        "  140+ Redis OSS instances identified (licence review required)",
        "  6 governance maturity domains assessed",
        "",
        "Phase 3 Outcome:",
        "  3-way TCO model: Azure UK South vs AWS eu-west-2 vs GCP europe-west2",
        "  Azure AHB modelled — significant SQL Server and Windows Server licence saving",
        "  EoL OS ESU: Azure ESU (free) vs AWS/GCP ESU (paid) — material cost difference",
        "  Oracle workloads: AVS (Azure VMware Solution) path identified for Oracle RAC",
        "  PRIMARY RECOMMENDATION: Microsoft Azure UK South · AMM eligibility confirmed and pre-registered"
    ], F, accent=AZURE, notes="Do not name the customer unless cleared by legal. Reference as 'a UK digital media group.' Key message: credible evidence-backed Azure recommendation after genuine 3-way evaluation, pre-registered for AMM.")

    content_slide(prs, "Extended Security Updates for EoL Windows and SQL in Azure — FREE", [
        "Microsoft provides Extended Security Updates (ESU) for Windows Server 2012/R2 and SQL Server 2012/2014 FREE when running in Azure. Running same EoL OS on AWS or GCP: customer must purchase ESU from Microsoft.",
        "",
        "TCO impact — 200 EoL servers over 3 years:",
        "  Azure ESU cost: £0 (included in Azure)",
        "  AWS or GCP ESU cost: £60K–£120K (paid to Microsoft)",
        "",
        "Where it appears in CRA TCO: Licensing Overlay tab — Azure ESU saving row (as important as AHB row)",
        "",
        "PARTNER MESSAGING: 'If your customer has Windows Server 2012 or SQL Server 2012 in their estate, Azure is structurally cheaper than AWS or GCP for those specific workloads — before you even include AHB.'",
        "",
        "Microsoft PDMs: proactively flag this to customers with EoL OS in estate. Customers may not realise ESU costs disappear in Azure."
    ], F, accent=AZURE, notes="Microsoft PDMs should proactively flag this. Customers often considering ESU purchases from Microsoft anyway — they may not realise those costs disappear in Azure.")

    content_slide(prs, "How Rackspace ensures Azure recommendations are credible and defensible", [
        "\"How do I know the recommendation wasn't pre-determined?\"",
        "",
        "1. Criteria weights are agreed in WRITING by the customer BEFORE any scoring begins — not after",
        "2. All three clouds are scored with equal rigour — AWS and GCP evaluation at the same depth as Azure",
        "3. Every score has a documented evidence reference — not 'expert judgment'",
        "4. The recommendation slide follows the evidence slides — never precedes them",
        "5. All three hyperscaler SEs are invited to the Phase 3 playback — this is standard practice",
        "",
        "When Azure is the recommendation, it is because: Azure scored highest on customer-agreed weighted criteria · Azure TCO (including AHB and ESU savings) was the most compelling financial case · Azure was evidenced — not pre-selected",
        "",
        "When all three hyperscalers are in the room at Phase 3 playback and the recommendation still points to Azure, the customer is significantly more confident. The Azure recommendation becomes unassailable."
    ], F, accent=AZURE, notes="Some Microsoft PDMs initially concerned that inviting AWS and GCP SEs undermines Azure recommendation. The opposite is true — it strengthens it.")

    table_slide(prs, "Why Microsoft should prioritise CRA-qualified opportunities",
        ["Microsoft Metric", "CRA Contribution"],
        [
            ["Azure consumption commitments", "CRA TCO provides the consumption baseline for Azure Reserved Instance discussions"],
            ["AMM deal registrations", "Every Azure-recommended CRA = one AMM registration"],
            ["Co-sell pipeline", "CRA engagements are logged co-sell opportunities from Day 1 (Phase 1 kickoff)"],
            ["Partner engagement", "CRA is a structured partner-led engagement — trackable in MSPP"],
            ["Accelerated migration timeline", "Phase 4 wave plan ready; Part 2 can begin within 2 weeks of assessment"],
            ["Reduced STU involvement", "CRA absorbs assessment workload; STU can focus on architecture validation"],
            ["Azure landing zone acceleration", "CRA Phase 2 governance baseline maps directly to CAF landing zone design decisions"],
        ], F, accent=AZURE, col_widths=[Inches(4.5), Inches(8.3)],
        notes="Position this for the PDM's own metrics. Every Microsoft PDM has AMM registration target and co-sell pipeline target. A CRA engagement with Azure recommendation = direct contribution to both.")

    table_slide(prs, "Microsoft actions that maximise CRA co-sell success",
        ["Action", "When", "Why"],
        [
            ["☐ Refer SMART Amber/Red customers to Rackspace", "Immediately after SMART result", "Top-of-funnel lead generation for CRA"],
            ["☐ Provide warm introduction to customer (not cold email)", "Before Rackspace scoping call", "Establishes Rackspace independence and credibility"],
            ["☐ Confirm SA status for AHB eligibility", "At scoping workshop", "Enables accurate TCO modelling in Phase 3"],
            ["☐ Acknowledge AMM deal registration in MSPP", "Phase 1 Week 1", "Required for AMM funding eligibility"],
            ["☐ Provide AMM programme guidance for this account", "Phase 1 Week 1–2", "Confirms funding tier and programme requirements"],
            ["☐ Attend Phase 3 playback (optional but recommended)", "Phase 3 Week 14", "Shows co-sell alignment; strengthens Azure recommendation credibility"],
            ["☐ Support AMM funding application", "Phase 3 Week 14–16", "Submits funding request once Azure recommendation is confirmed"],
        ], F, accent=AZURE, col_widths=[Inches(5.2), Inches(2.8), Inches(4.8)],
        notes="Two critical actions: AMM registration acknowledgement (Phase 1 Week 1) and SA status confirmation for AHB (at scoping). Both are quick actions with major financial impact.")

    content_slide(prs, "Oracle workloads in Azure — the AVS path", [
        "THE ORACLE CHALLENGE: Oracle RAC and Oracle Database Enterprise Edition have specific licensing requirements in Azure. Azure VMware Solution (AVS) provides an Oracle-supported migration path that preserves existing Oracle licence terms without requiring Oracle BYOL renegotiation.",
        "",
        "  Oracle RAC (standard): AVS migration + Oracle Practice specialist engagement → Phase 4 Wave 5+ specialist path",
        "  Oracle E-Business Suite: Evaluate AVS or Azure-native (Oracle DB on Azure IaaS) → Oracle Practice Lead input required at Phase 2",
        "  Oracle Database on standard VMs: Azure IaaS BYOL or Oracle DB on Azure → Licence Overlay tab — Oracle rows",
        "  Oracle SE2 on Linux: Standard Azure IaaS migration → no AVS required",
        "",
        "CRA action: Oracle RAC identified in Phase 1 → Rackspace Oracle Practice Lead engaged Phase 1 → AVS is standard recommendation for Oracle RAC workloads targeting Azure",
        "This keeps Oracle workloads in the Azure estate rather than being retained on-premises or routed to OCI."
    ], F, accent=AZURE, notes="Rackspace CRA includes Oracle escalation path in Phase 1. AVS is modelled in Phase 3 where applicable. Oracle analysis takes 4–6 weeks — start early.")

    content_slide(prs, "Phase 2 governance assessment prepares customer for Azure landing zone design", [
        "Azure-specific governance outputs from CRA Phase 2:",
        "",
        "  Identity & Access Management → Azure Active Directory (Entra ID) design · RBAC model for Azure subscriptions",
        "  Security & Compliance → Defender for Cloud readiness · Microsoft Sentinel integration",
        "  Change & Release Management → Azure DevOps / GitHub Actions for cloud deployment pipelines",
        "  Monitoring & Observability → Azure Monitor / Log Analytics workspace design",
        "  Cost Management (FinOps) → Azure Cost Management + Billing · tagging strategy for chargeback",
        "  Operations Readiness → Azure Update Manager · Azure Automation baseline",
        "",
        "KEY MESSAGE: The CRA governance maturity assessment produces a baseline that directly informs the Azure Landing Zone design. This eliminates the 'design the landing zone from scratch' step that typically delays migration starts.",
        "STU architects can take CRA governance output and directly begin landing zone design without running a separate assessment."
    ], F, accent=AZURE, notes="Significant co-sell message for Microsoft STU architects. Landing zone design is often a bottleneck. CRA Phase 2 produces the baseline that answers those questions.")

    table_slide(prs, "Three ways to activate a Rackspace CRA opportunity with Microsoft",
        ["Path", "Trigger", "First Action"],
        [
            ["1. SMART Referral", "Microsoft SE completes SMART with customer · score is Amber/Red", "SE refers to Rackspace Pre-Sales Architect for CRA scoping call · Contact: [Rackspace Pre-Sales]"],
            ["2. Joint Pipeline Review", "Monthly Rackspace + Microsoft PDM pipeline review", "Identify accounts where formal assessment accelerates Azure commitment · Rackspace Pre-Sales attends joint account planning · Contact: [Alliance Manager]"],
            ["3. Inbound from Customer", "Customer approaches Microsoft directly for cloud readiness help", "Microsoft SE recommends Rackspace CRA · warm introduction email · Contact: [Rackspace Pre-Sales]"],
        ], F, accent=AZURE, col_widths=[Inches(2.2), Inches(5.3), Inches(5.3)],
        intro_text="\"Schedule a 30-minute technical briefing between Rackspace Alliance Architecture and Microsoft STU to validate CRA against CAF and AMM requirements. This is the one session that unlocks co-sell activation.\"",
        notes="Invite the Microsoft STU architect to review MICROSOFT-CAF-ALIGNMENT.md and METHODOLOGY.md. Microsoft PDM technical sign-off on CRA as an AMM-qualifying methodology would be a significant co-sell enabler.")


# ── Deck: AWS Partner ──────────────────────────────────────────────────────────

def build_aws(prs):
    F = "Rackspace × AWS — Migration Partner"

    title_slide(prs, "Cloud Readiness Accelerator",
        "How Rackspace CRA drives MAP-qualified assessments and structured AWS co-sell",
        "Rackspace Cloud Solutions Architecture + Alliance | [Date]",
        F, accent=NAVY, notes="For AWS PDMs, PSAs, and account managers. Goal: AWS partner team understands that a Rackspace CRA engagement is a pre-qualified MAP opportunity — and that Rackspace Alliance Manager process ensures ACE deal registration is active from Phase 1 Day 1.")

    content_slide(prs, "CRA-qualified assessments feed directly into MAP migration pipeline", [
        "WHAT'S MISSING WITHOUT CRA: Most mid-market customers approaching AWS lack a formal application inventory, a multi-cloud TCO model, and a structured migration plan. Result: long discovery cycles, missed MAP registration windows, delayed Azure/GCP alternatives getting in first.",
        "",
        "WHAT CRA PROVIDES: A 16-week structured assessment that produces exactly the documentation MAP requires — application inventory, readiness assessment, AWS TCO with Savings Plans modelled, and a sequenced migration wave plan. Produced by an independent assessor.",
        "",
        "THE MAP ACTIVATION: Every CRA engagement with an AWS recommendation is a MAP-eligible opportunity. Rackspace pre-registers in AWS ACE at Phase 1 kickoff. By Phase 4, the customer has a board-ready business case, migration plan, and signed Part 2 Entry Point.",
        "",
        "\"CRA Assessment phase outputs are the MAP Assess stage deliverables. The assessment work is done — MAP can begin immediately at Phase 4 close.\""
    ], F, accent=AWSOR, notes="Position CRA as the front-end of MAP, not an alternative to it. MAP has three stages: Assess, Mobilize, Migrate & Modernize. CRA delivers the Assess stage at depth far exceeding what most customers produce internally.")

    table_slide(prs, "CRA phases map directly to AWS MAP phases",
        ["MAP Phase", "CRA Phase", "CRA Deliverables"],
        [
            ["Assess (MRA, current-state baseline, business case, migration strategy)", "Phase 1 Discovery + Phase 2 Analysis", "Application inventory · infrastructure profiling · 5-dimension readiness scores · dependency map · AWS TCO baseline"],
            ["Mobilize (detailed migration plan, wave sequencing, landing zone design, pilot)", "Phase 3 Evaluation + Phase 4 Planning", "AWS TCO model · hyperscaler recommendation · migration wave plan · Part 2 Entry Point · governance model · risk register"],
            ["Migrate & Modernize (full migration execution, WAR, optimization)", "Post-CRA (Part 2 engagement)", "CRA provides baseline and wave plan · migration execution is Part 2"],
        ], F, accent=AWSOR, col_widths=[Inches(3.8), Inches(3.2), Inches(5.8)],
        notes="CRA Phases 1 and 2 are equivalent to MAP Assess. CRA Phases 3 and 4 cover MAP Mobilize. By the time a customer completes CRA, they have satisfied both MAP Assess and Mobilize requirements.")

    table_slide(prs, "CRA produces every artefact required for MAP deal registration",
        ["MAP Requirement", "CRA Output", "CRA Template"],
        [
            ["Migration Readiness Assessment (MRA)", "CRA Phase 1+2: app inventory, readiness scores, governance assessment", "application-scoping-profiling.xlsx + cloud-readiness-scoring-v2.xlsx"],
            ["Current-state inventory", "Infrastructure profiling + Application inventory", "infrastructure-profiling.xlsx"],
            ["Business case with TCO analysis", "7-layer TCO with AWS On-Demand + RI + Savings Plans", "business-case-tco-roi.xlsx + aws-evaluation.xlsx"],
            ["Migration wave plan", "Wave planner with Tier-based sequencing", "migration-wave-planner.xlsx"],
            ["AWS as primary or co-primary recommendation", "Hyperscaler decision matrix — AWS scored and evidenced", "hyperscaler-decision-matrix.xlsx"],
            ["APN Partner with Migration Competency", "Rackspace AWS Partner status ✓", "—"],
            ["ACE deal registration", "Rackspace Alliance Manager registers at Phase 1 Day 1", "AWS Partner Central / ACE"],
        ], F, accent=AWSOR, col_widths=[Inches(3.5), Inches(5.2), Inches(4.1)],
        notes="CRA was not designed specifically for MAP but the overlap is near-complete. Both are based on the same underlying principle: formal, evidence-based, people/process/technology assessment before credible migration recommendation.")

    table_slide(prs, "How CRA models AWS pricing — all three options, per region",
        ["Pricing Model", "AWS Name", "CRA Tab", "Notes"],
        [
            ["On-Demand", "EC2 On-Demand", "AWS-OnDemand", "Like-for-Like baseline — worst case cost"],
            ["Reserved Instances (3yr)", "EC2 RI (3yr, All Upfront)", "AWS-RI-3yr", "Standard commitment model; typically 40–60% saving vs On-Demand"],
            ["Savings Plans (3yr)", "Compute Savings Plans (3yr)", "AWS-SavingsPlans", "More flexible than RI; applies to EC2, Fargate, Lambda"],
        ], F, accent=AWSOR, col_widths=[Inches(2.5), Inches(3.0), Inches(2.8), Inches(4.5)],
        intro_text="Key instance families: m6i/m7i (general) · r6i/r7i (memory, databases) · c6i/c7i (compute-optimised) · i4i (storage-optimised). Always present all three pricing models — CFOs ask about flexibility vs. commitment.",
        notes="Always model all three AWS pricing options. Present all three in TCO comparison. Board-level number should be 3yr Savings Plans or RI — that is the committed cost the customer is actually deciding on.")

    content_slide(prs, "Integrating AWS Migration Evaluator with CRA Phase 1 data", [
        "WHAT MIGRATION EVALUATOR DOES: Free AWS tool that ingests current-state inventory data and produces an initial business case for AWS migration — direct from discovered VM data.",
        "",
        "CRA INTEGRATION WORKFLOW:",
        "  Phase 1 Wk 1: Deploy AWS ADS agentless collector or agent",
        "  Phase 1 Wks 1–7: Collect 14+ days utilisation data (same window as other tools)",
        "  Phase 1 Wk 7: Export collected data from AWS ADS",
        "  Phase 3 Wk 11: Upload to Migration Evaluator → generate initial business case",
        "  Phase 3 Wk 12: Cross-validate Migration Evaluator output against manually-built aws-evaluation.xlsx",
        "  Phase 3 Wk 13: Resolve discrepancies · use manually-built model as source of truth",
        "",
        "WHY CROSS-VALIDATE: Evaluator applies standard AWS pricing and default right-sizing assumptions. CRA manual model applies customer-specific assumptions: Oracle workloads, Savings Plan commitment level, specific instance families. Manual model is more accurate for complex estates.",
    ], F, accent=AWSOR, notes="AWS PSAs can offer to run Migration Evaluator on customer data during Phase 1 — accept the help, but always cross-validate. Evaluator tends to underestimate cost for Oracle workloads.")

    content_slide(prs, "When to register in AWS ACE — and why it cannot wait", [
        "Phase 1 Day 1: Rackspace Alliance Manager registers opportunity in AWS Partner Central → tags as Migration type, selects Assess phase, links to AWS account manager, enters estimated annual AWS run rate",
        "Phase 1 Week 2: AWS PSA confirms registration · confirms MAP programme applicability",
        "Phase 2 Week 10: Readiness scoring complete",
        "Phase 3 Week 11: TCO analysis complete",
        "Phase 3 Week 14: Recommendation presented",
        "Phase 4 Week 18: Part 2 SOW ready",
        "",
        "HARD RULE: ACE registration must be active BEFORE Phase 3 begins. MAP assessment funding eligibility requires registration before the assessment evidence is compiled — not after.",
        "",
        "AWS PDM ACTION REQUIRED: Accept and acknowledge co-sell opportunity in ACE within 5 business days · Confirm MAP programme applicability for this customer tier · Introduce AWS PSA if technical depth needed in Phase 3."
    ], F, accent=AWSOR, notes="MAP has time-sensitive registration requirements. Registering after TCO model is complete may only qualify for migration funding — not assessment funding. Day 1 registration maximises the opportunity.")

    table_slide(prs, "CRA readiness scoring and governance model align to AWS WAF pillars",
        ["WAF Pillar", "CRA Phase 2/4 Output", "Impact on AWS Deployment"],
        [
            ["Operational Excellence", "Governance maturity — Change Management, Monitoring & Observability domains", "Gap register for AWS CloudWatch / CloudTrail / CloudOps readiness"],
            ["Security", "Governance maturity — Security & Compliance domain; IAM domain", "Gap register for AWS Security Hub and IAM design"],
            ["Reliability", "Cloud Readiness Scores — Business Criticality dimension; RTO/RPO", "Applications requiring multi-AZ or multi-region AWS architecture"],
            ["Performance Efficiency", "Phase 1 P95 utilisation data + right-sizing recommendations", "EC2 instance family selection based on actual utilisation"],
            ["Cost Optimisation", "Phase 3 7-layer TCO; Savings Plans modelling", "Layer (g) MAP credits applied to net cost — the headline board number"],
            ["Sustainability", "Phase 3 right-sizing (fewer optimised instances = lower energy)", "Optional: add to Phase 4 governance model for ESG-conscious customers"],
        ], F, accent=AWSOR, col_widths=[Inches(2.8), Inches(5.2), Inches(4.8)],
        notes="AWS PSAs who conduct WAF reviews post-migration can use CRA governance outputs as baseline. Reduces WAF review time by 30–40%.")

    content_slide(prs, "CRA identifies open-source workload migration paths on AWS", [
        "OSS LICENCE RISK IDENTIFIED IN CRA PHASE 2 — AWS managed alternatives:",
        "",
        "  Redis OSS (post v7.4 — SSPL): Amazon ElastiCache (Valkey or Redis-compatible) → low complexity, configuration changes only",
        "  Elasticsearch (post 7.10 — SSPL): Amazon OpenSearch Service (Apache 2.0 fork) → low-medium, API compatible",
        "  HashiCorp Vault / Terraform (BSL): AWS Secrets Manager + Parameter Store → medium, workflow changes",
        "  MongoDB (SSPL): Amazon DocumentDB (MongoDB-compatible) → medium, driver changes",
        "",
        "CRA Phase 3 action: OSS-flagged workloads costed with managed service replacement in aws-evaluation.xlsx OSS-Migration tab.",
        "",
        "For AWS: ElastiCache and OpenSearch are more mature than equivalents on other hyperscalers — can be a legitimate AWS advantage for Redis/Elasticsearch-heavy estates.",
    ], F, accent=AWSOR, notes="For AWS, managed OSS alternatives are often cheaper and simpler. Make sure CRA architect models the managed service cost — not just the EC2 instance that would replace the on-prem server.")

    content_slide(prs, "When CRA recommends AWS, the customer's board believes it", [
        "THE CREDIBILITY PROBLEM AWS FACES: Customers know that hyperscaler-provided assessments are not independent. A free AWS assessment recommending AWS is not surprising.",
        "",
        "A formal, 16-week, three-way evaluation conducted by an independent Rackspace-led team that recommends AWS is a different kind of evidence.",
        "",
        "WHAT 'INDEPENDENT RECOMMENDATION' MEANS:",
        "  · CRA evaluates all three clouds with equal rigour — Azure and GCP get the same depth",
        "  · Criteria weights are agreed by the customer before scoring — not by Rackspace or AWS",
        "  · The TCO model shows all three clouds — the customer can see why AWS won",
        "  · All three hyperscaler SEs are invited to the Phase 3 playback",
        "  · The AWS recommendation is evidenced, auditable, and defensible",
        "",
        "A CRA-delivered AWS recommendation is the strongest possible evidence for a customer's investment committee, their Microsoft incumbent account team, or their Azure-preferring CTO."
    ], F, accent=AWSOR, notes="This is the 'why CRA and not just AWS free assessment' message. AWS CART and Migration Evaluator are useful but not independent. When board chooses between Azure and AWS, Rackspace independent recommendation carries far more weight.")

    table_slide(prs, "Three paths to a Rackspace CRA / AWS MAP co-sell activation",
        ["Path", "Trigger", "First Action"],
        [
            ["1. MAP Pipeline Identification", "AWS PDM identifies accounts approaching migration readiness", "Refers to Rackspace Pre-Sales for CRA scoping call · Contact: [Rackspace Pre-Sales]"],
            ["2. CART / MRA Upgrade", "Customer has completed AWS CART or internal MRA · score suggests formal assessment needed", "Rackspace CRA provides MAP Assess deliverables to higher rigour standard · Contact: [Rackspace Pre-Sales]"],
            ["3. Joint Pipeline Review", "Monthly joint pipeline review: Rackspace Alliance Manager + AWS PDM", "Identify accounts where CRA accelerates MAP registration · Contact: [Rackspace Alliance Manager]"],
        ], F, accent=AWSOR, col_widths=[Inches(2.5), Inches(5.5), Inches(4.8)],
        intro_text="\"Schedule a 30-minute session between Rackspace Alliance Architecture and AWS PSA to confirm CRA methodology against MAP Assess requirements. One session. Unlocks the entire co-sell pipeline.\"",
        notes="")


# ── Deck: GCP Partner ──────────────────────────────────────────────────────────

def build_gcp(prs):
    F = "Rackspace × Google Cloud — Migration Partner"

    title_slide(prs, "Cloud Readiness Accelerator",
        "How Rackspace CRA aligns to Google Cloud's migration methodology and PSO programme requirements",
        "Rackspace Cloud Solutions Architecture + Alliance | [Date]",
        F, accent=GCPBL, notes="For Google Cloud PDMs, PSEs, and CEs. Goal: Google partner team understands that Rackspace CRA produces the assessment deliverables that GCP PSO and RAMP require.")

    content_slide(prs, "CRA-qualified assessments are the front-end of GCP PSO migration engagements", [
        "THE GAP: Mid-market customers interested in GCP often lack the structured assessment capability to produce a board-ready business case, a multi-cloud comparison, and a migration plan. They complete Google Migration Center assessments but cannot translate output into an investment decision.",
        "",
        "WHAT CRA PROVIDES: A 16-week structured assessment that produces the GCAF Assess and Plan stage deliverables at a rigour level supporting GCP PSO engagement qualification and migration credit eligibility.",
        "",
        "THE GCP ACTIVATION: Every CRA engagement with a GCP recommendation generates a PSO-qualified opportunity. Rackspace pre-registers in Google Partner Advantage at Phase 1 kickoff. By Phase 4, the customer has a board-ready GCP business case, migration wave plan, and signed Part 2 Entry Point.",
        "",
        "\"CRA delivers the GCAF Assess and Plan stages. GCP PSO and RAMP can begin at Phase 4 close — no additional discovery required.\""
    ], F, accent=GCPBL, notes="Position CRA as the GCAF Assess + Plan stage executor. GCP's migration framework has four stages: Assess, Plan, Deploy, Optimise. CRA covers the first two.")

    table_slide(prs, "CRA phases map directly to Google Cloud Adoption Framework stages",
        ["GCAF Stage", "CRA Phase", "CRA Deliverables"],
        [
            ["Assess (evaluate current workloads, identify cloud fit, establish baseline TCO)", "Phase 1 Discovery + Phase 2 Analysis", "Application inventory · infrastructure profiling · 5-dimension readiness scores · dependency map · GCP cloud fit assessment"],
            ["Plan (design target architecture, build migration business case, define wave plan)", "Phase 3 Evaluation + Phase 4 Planning", "GCP TCO model · hyperscaler recommendation · migration wave plan · landing zone design guidance · governance model"],
            ["Deploy (landing zone build, foundation infrastructure, initial wave migration)", "Post-CRA (Part 2 engagement)", "CRA provides deployment specifications · landing zone build is separate Part 2 workstream"],
            ["Optimise (cost optimisation, SRE practices, FinOps, Architecture Framework review)", "Post-CRA (ongoing)", "CRA TCO model provides cost optimisation baseline · ongoing is managed services"],
        ], F, accent=GCPBL, col_widths=[Inches(3.5), Inches(3.2), Inches(6.1)],
        notes="CRA Phases 1+2 are GCAF Assess. Phases 3+4 are GCAF Plan. PDMs/PSEs can confidently position CRA as front-end of a GCP engagement entering Deploy immediately at Phase 4 close.")

    content_slide(prs, "CRA Phase 1 uses Google Migration Center — natively", [
        "WHAT MIGRATION CENTER DOES: Free Google Cloud discovery and assessment tool. Ingests inventory data from agent-based collection, RVTools export, or direct API integration. Produces GCP-specific right-sizing recommendations, TCO estimates, and fit analysis.",
        "",
        "CRA INTEGRATION WORKFLOW:",
        "  Phase 1 Wk 1: Deploy GCP Migration Center collector or VM Manager agent",
        "  Phase 1 Wks 1–7: Collect 14+ days of utilisation data",
        "  Phase 1 Wk 7: Export data · import to Migration Center dashboard",
        "  Phase 3 Wk 11: Run Migration Center GCP right-sizing analysis",
        "  Phase 3 Wks 12–13: Cross-validate against manually-built gcp-evaluation.xlsx · resolve discrepancies",
        "",
        "ALTERNATIVE — RVTools IMPORT: Migration Center accepts direct RVTools VMware export. If Azure Migrate is the primary discovery tool, the same RVTools export can populate Migration Center in parallel — no additional agent deployment required.",
    ], F, accent=GCPBL, notes="GCP Migration Center is most straightforward tool to integrate with CRA because it accepts RVTools imports directly. If primary tool is Azure Migrate, same RVTools export populates Migration Center without running separate collector.")

    table_slide(prs, "How CRA models GCP pricing — two options, per region",
        ["Pricing Model", "GCP Name", "CRA Tab", "Notes"],
        [
            ["On-Demand", "Pay-as-you-go", "GCP-OnDemand", "Like-for-Like baseline"],
            ["Committed Use Discounts (3yr)", "3-year CUD", "GCP-CUD-3yr", "Typically 37–55% saving vs On-Demand; resource-based (CPU/RAM) for more flexibility than AWS RI"],
        ], F, accent=GCPBL, col_widths=[Inches(2.8), Inches(2.5), Inches(2.5), Inches(5.0)],
        intro_text="Key instance families: n2-standard (general purpose) · n2-highmem (memory-optimised, Oracle) · c3-standard (latest gen) · m3-ultramem (SAP HANA, high-memory Oracle). GCP CUDs are resource-based — more flexibility than AWS RI but less than AWS Savings Plans.",
        notes="GCP CUDs apply to specific regions and resource types. Must know which region (typically europe-west2 for UK) and CPU/RAM mix. Cross-validate Migration Center CUD estimate against manual model.")

    content_slide(prs, "Registering in Google Partner Advantage — when and how", [
        "Phase 1 Day 1: Rackspace Alliance Manager logs into Google Partner Advantage · creates Deal Registration for customer account · tags as Migration type · links to Google Cloud account team · enters estimated annual GCP consumption · selects applicable programme (PSO credits, RAMP)",
        "Phase 1 Week 2: GCP PDM acknowledges and accepts partner opportunity registration",
        "Phase 2 Week 10: Readiness scoring complete",
        "Phase 3 Week 11: TCO analysis complete",
        "Phase 3 Week 14: Recommendation presented",
        "Phase 4 Week 18: Part 2 SOW ready",
        "",
        "GCP PDM ACTION REQUIRED: Acknowledge partner opportunity · Connect with Rackspace Alliance Manager · Confirm PSO credit or RAMP programme eligibility · Introduce Google Cloud PSE if architecture depth needed in Phase 3",
        "",
        "IMPORTANT: GCP programme terms change more frequently than AWS MAP or Azure AMM. Rackspace Alliance Manager should always confirm current programme terms with GCP PDM at Phase 1 kickoff — not assume from prior engagements."
    ], F, accent=GCPBL, notes="GCP programme structures are also more geography-specific than AWS or Azure programmes. Always confirm current terms at kickoff.")

    table_slide(prs, "CRA governance assessment baseline aligns to GCAF Architecture Framework pillars",
        ["GCAF Pillar", "CRA Phase 2/4 Output", "Impact on GCP Deployment"],
        [
            ["System Design", "Cloud Readiness Scores — Technical Complexity; dependency mapping", "Identifies apps requiring rearchitecting for GCP · dependency clusters that must colocate"],
            ["Operational Excellence", "Governance maturity — Change Management domain", "Gap register for GCP Cloud Operations Suite readiness · SRE practice maturity"],
            ["Security, Privacy, Compliance", "Governance maturity — Security & Compliance · data sensitivity scoring", "GCP Security Command Center baseline · BeyondCorp / Zero Trust readiness"],
            ["Reliability", "Cloud Readiness Scores — Business Criticality; RTO/RPO", "Applications requiring multi-region or zonal redundancy in GCP"],
            ["Cost Optimisation", "Phase 3 7-layer TCO; CUD modelling", "Layer (g) GCP migration credits applied to net cost"],
            ["Performance", "Phase 1 P95 utilisation data; right-sizing", "GCP instance family selection based on actual utilisation"],
        ], F, accent=GCPBL, col_widths=[Inches(2.8), Inches(5.2), Inches(4.8)],
        notes="Google Cloud PSEs who conduct Architecture Framework reviews post-migration can use CRA governance outputs as baseline. Reduces PSO pre-engagement discovery time.")

    content_slide(prs, "GCP's open-source strength — and how CRA surfaces it", [
        "CRA Phase 2 flags OSS Licence Risk for Redis, Elasticsearch, HashiCorp Vault, MongoDB. GCP managed alternatives — strong in several cases:",
        "",
        "  Redis OSS (post v7.4 — SSPL): Memorystore for Redis / Valkey → fully managed, Redis-compatible",
        "  Elasticsearch (post 7.10 — SSPL): Elastic on GCP Marketplace or Vector Search → native Elastic partnership",
        "  HashiCorp Vault (BSL): Secret Manager / Berglas → GCP-native, no licence concerns",
        "  MongoDB (SSPL): Cloud Firestore / MongoDB Atlas on GCP Marketplace",
        "  Kafka: Pub/Sub + Dataflow → GCP's natural Kafka alternative, no licence risk",
        "",
        "CRA Phase 3: OSS-flagged workloads costed using GCP managed service pricing in gcp-evaluation.xlsx OSS-Migration tab.",
        "",
        "CONTAINERS / KUBERNETES: For 'Cloud Friendly' (Replatform) workloads, CRA Phase 3 models containerisation cost on GKE. GKE is often the most capable managed Kubernetes service — a legitimate GCP advantage for containerisation-ready workloads.",
    ], F, accent=GCPBL, notes="GCP's open-source ecosystem relationships (Elastic, MongoDB Atlas on GCP, HashiCorp on GCP Marketplace) are genuine differentiator. Ensure CRA architect models managed service cost — not just the GCE instance.")

    content_slide(prs, "GCP surfaces its advantage for data, analytics, and AI/ML workloads", [
        "CRA Phase 2: Application inventory captures data platform and analytics workloads with extra criteria — data processing volume/frequency, current analytics stack (Spark/Hadoop/ETL), ML models in production, real-time vs batch requirements.",
        "",
        "WHERE GCP HAS A STRUCTURAL ADVANTAGE IN CRA TCO:",
        "  Apache Spark / Hadoop → Dataproc (fully managed, auto-scaling) vs EC2 Spark vs Azure HDInsight",
        "  Data warehouse (Teradata, Oracle DW) → BigQuery (serverless, no infrastructure cost) vs Azure Synapse vs Redshift",
        "  AI/ML training and inference → Vertex AI (integrated MLOps, TPU access) — Phase 4 planning modernisation workstream",
        "  Real-time event streaming → Pub/Sub + Dataflow (Kafka alternative) vs managed Kafka on Azure/AWS",
        "",
        "CRA Action: Data platform or analytics workloads flagged in Phase 2 → modelled with GCP managed service alternatives in Phase 3. BigQuery and Dataproc pricing compared against Azure and AWS equivalents.",
        "For customers with significant data workloads, this comparison often shows a strong GCP cost advantage."
    ], F, accent=GCPBL, notes="GCP's clearest area of competitive advantage in CRA. BigQuery is genuinely cheaper than Synapse Analytics or Redshift for large analytics workloads. Ensure architect models BigQuery/Dataproc in GCP TCO for any customer with data/analytics workloads.")

    content_slide(prs, "A CRA-delivered GCP recommendation is unassailable", [
        "THE CHALLENGE GCP FACES: Many mid-market enterprises default to Azure because they have an existing Microsoft EA and their CTO has strong Microsoft relationships. A GCP recommendation from Google is dismissed as sales pressure.",
        "",
        "WHAT THE CRA PROCESS PROVIDES:",
        "  · Customer agrees evaluation criteria and weights before any scoring begins",
        "  · All three clouds scored with equal depth — Azure and AWS get the same rigour",
        "  · GCP wins where GCP is genuinely the best fit: containerisation, data analytics, OSS workloads, AI/ML",
        "  · The recommendation follows the evidence — it is not pre-determined",
        "  · All three hyperscaler SEs are in the room at the Phase 3 playback",
        "",
        "For a customer's Microsoft-aligned CTO: 'Rackspace ran a 16-week independent assessment. They evaluated Azure, AWS, and GCP. The data shows GCP is the right answer for our containerisation and analytics workloads.'",
        "This is a different conversation than any Google sales rep can have."
    ], F, accent=GCPBL, notes="For GCP, credibility problem is more acute than for Azure or AWS because many organisations default to Azure through inertia. CRA-delivered GCP recommendation bypasses 'you're just saying that because you're Google' objection.")

    table_slide(prs, "Three paths to a Rackspace CRA / GCP co-sell activation",
        ["Path", "Trigger", "First Action"],
        [
            ["1. Migration Center Assessment Upgrade", "Customer has used GCP Migration Center · needs formal board-ready multi-cloud business case", "Rackspace CRA takes Migration Center data and builds complete GCAF Assess + Plan deliverables · Contact: [Rackspace Pre-Sales]"],
            ["2. GCP Pipeline Identification", "GCP PDM identifies accounts with data, analytics, or containerisation workloads where GCP has advantage", "Refer to Rackspace Pre-Sales for CRA scoping call · CRA ensures TCO explicitly models BigQuery, Dataproc, GKE vs alternatives · Contact: [Alliance Manager]"],
            ["3. Joint Pipeline Review", "Monthly joint pipeline review: Rackspace Alliance Manager + GCP PDM", "Identify accounts where CRA accelerates partner programme registration · Contact: [Rackspace Alliance Manager]"],
        ], F, accent=GCPBL, col_widths=[Inches(2.5), Inches(5.5), Inches(4.8)],
        intro_text="\"Schedule a 30-minute session between Rackspace Alliance Architecture and Google Cloud PSE to confirm CRA methodology against GCAF and PSO programme requirements.\"",
        notes="")


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
        prs = new_prs()
        builder(prs)
        prs.save(out)
        print(f"OK  {rel_path}  ({len(prs.slides)} slides)")

if __name__ == "__main__":
    main()
