#!/usr/bin/env python3
"""
4D.1: Audit cra-assessment-report-template-v3.docx -- verify 25-section structure
4D.2: Add board-extractable executive summary section
10.6(a): Add document header block to report template
"""
import os
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.oxml.ns import qn
from lxml import etree

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(BASE, "Templates", "executive-reporting", "cra-assessment-report-template-v3.docx")

RAX_RED = RGBColor(0xE3, 0x1C, 0x3D)
ORANGE  = RGBColor(0xC0, 0x50, 0x00)

REQUIRED_SECTIONS = [
    ("Cover Page",                          "cover"),
    ("Document Control",                    "document control"),
    ("Executive Summary",                   "executive summary"),
    ("Table of Contents",                   "table of contents"),
    ("1. Engagement Scope",                 "engagement scope"),
    ("2. Methodology",                      "methodology"),
    ("3. Infrastructure Discovery Summary", "infrastructure discovery"),
    ("4. Utilisation Data Summary",         "utilisation data"),
    ("5. Application Inventory Summary",    "application inventory"),
    ("6. Dependency Analysis",              "dependency"),
    ("7. Cloud Readiness Assessment",       "cloud readiness assessment"),
    ("8. EoL / End-of-Support Analysis",    "end-of-support"),
    ("9. Licensing Analysis",               "licensing analysis"),
    ("10. Cloud Comparison",                "cloud comparison"),
    ("11. TCO Analysis",                    "tco analysis"),
    ("12. Licensing Overlay",               "licensing overlay"),
    ("13. Partner Funding",                 "partner funding"),
    ("14. Hyperscaler Scoring Matrix",      "scoring matrix"),
    ("15. Recommendation",                  "recommendation"),
    ("16. Migration Approach",              "migration approach"),
    ("17. Indicative Wave Plan",            "wave plan"),
    ("18. Risk Register",                   "risk register"),
    ("20. Part 2 Entry Point",              "part 2 entry"),
    ("Appendix A",                          "appendix"),
]

def all_texts(doc):
    return [(p.style.name, p.text.lower()) for p in doc.paragraphs if p.text.strip()]

def section_present(texts, keyword):
    return any(keyword in t[1] for t in texts)

# ── element builders ─────────────────────────────────────────────────────────

def _heading(doc, text, level=1, color=None):
    h = doc.add_paragraph(text, style=f"Heading {level}")
    c = color or RAX_RED
    for run in h.runs:
        try:
            run.font.color.rgb = c
        except Exception:
            pass
    return h._element

def _para(doc, text, bold=False, italic=False):
    p = doc.add_paragraph(style="Normal")
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    return p._element

def _bullet(doc, text, size=None):
    p = doc.add_paragraph(style="List Bullet")
    run = p.add_run(text)
    if size:
        run.font.size = Pt(size)
    return p._element

def _spacer(doc):
    return doc.add_paragraph("")._element

def _bold_para(doc, label, body_text):
    p = doc.add_paragraph(style="Normal")
    r1 = p.add_run(label)
    r1.bold = True
    p.add_run(body_text)
    return p._element

# ── 10.6(a): Header block ────────────────────────────────────────────────────

def build_header_block(doc):
    table = doc.add_table(rows=9, cols=2)
    try:
        table.style = "Light Shading"
    except Exception:
        pass

    def set_width(cell, inches):
        from docx.oxml import OxmlElement
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        tcW = OxmlElement("w:tcW")
        tcW.set(qn("w:w"), str(int(inches * 1440)))
        tcW.set(qn("w:type"), "dxa")
        tcPr.append(tcW)

    # Header row
    hrow = table.rows[0]
    hcell = hrow.cells[0].merge(hrow.cells[1])
    hcell.text = "DOCUMENT INFORMATION"
    hcell.paragraphs[0].runs[0].bold = True
    try:
        hcell.paragraphs[0].runs[0].font.color.rgb = RAX_RED
    except Exception:
        pass

    data = [
        ("Document Purpose:",
         "The primary written deliverable of the CRA engagement. Delivered to the customer "
         "CTO/CIO at Phase 3 completion. Must be board-quality."),
        ("CRA Phase:",   "Phase 3: Hyperscaler Evaluation -- Customer Deliverable"),
        ("Target Audience:",
         "Customer CTO, CIO, IT Director + Rackspace Delivery Team"),
        ("When to Complete:",
         "Phase 3 weeks 2-3; final review in Phase 4 before Part 2 SOW"),
        ("Est. Time to Fill:",
         "16-24 hours (spread across Phases 2-3); 40-60 pages when complete"),
        ("Template Version:", "v3.0"),
    ]
    for i, (label, value) in enumerate(data):
        r = table.rows[i + 1]
        r.cells[0].text = label
        try:
            r.cells[0].paragraphs[0].runs[0].bold = True
        except Exception:
            pass
        r.cells[1].text = value

    # Customise row
    crow = table.rows[7]
    ccell = crow.cells[0].merge(crow.cells[1])
    ccell.text = (
        "WHAT TO CUSTOMISE\n"
        "- Replace all [Customer Name] placeholders (30+ instances throughout document)\n"
        "- Replace all financial figures with your TCO model outputs\n"
        "- Section 15 (Recommendation): confirm it comes AFTER sections 10-14\n"
        "- Update partner funding table (Section 13) with your AMM/MAP/PSO actuals\n"
        "- Remove sections marked [IF APPLICABLE] that do not apply"
    )
    try:
        ccell.paragraphs[0].runs[0].bold = True
    except Exception:
        pass

    # Important row
    irow = table.rows[8]
    icell = irow.cells[0].merge(irow.cells[1])
    icell.text = (
        "IMPORTANT: The Recommendation section (Section 15) must appear AFTER the TCO Analysis, "
        "Licensing Overlay, Partner Funding, and Hyperscaler Scoring sections (Sections 10-14). "
        "A recommendation that precedes the evidence will be perceived as pre-determined. "
        "See docs/DMG-MEDIA-UK-LESSONS-LEARNED.md Lesson 9."
    )
    try:
        icell.paragraphs[0].runs[0].bold = True
        icell.paragraphs[0].runs[0].font.color.rgb = RAX_RED
    except Exception:
        pass

    return table._element

# ── 4D.2: Board-extractable executive summary ────────────────────────────────

def build_board_exec_summary(doc):
    elems = []

    elems.append(_spacer(doc))
    elems.append(_heading(doc,
        "[CUSTOMER NAME] Cloud Readiness Assessment -- Executive Summary", 1))
    elems.append(_para(doc,
        "Prepared by Rackspace Technology  |  [DATE]  |  CONFIDENTIAL", bold=True))
    elems.append(_para(doc, "=" * 68))
    elems.append(_spacer(doc))

    # SCOPE
    elems.append(_heading(doc, "SCOPE ASSESSED", 2))
    elems.append(_para(doc,
        "[NUMBER] applications | [NUMBER] VMs | [NUMBER] data centre(s) | [DURATION]-week assessment"))
    elems.append(_spacer(doc))

    # KEY FINDINGS
    elems.append(_heading(doc, "KEY FINDINGS", 2))
    for f in [
        "[Finding 1: e.g., 39% on-premises cost reduction achievable]",
        "[Finding 2: e.g., 340+ servers running EoL OS; ESU cost avoided in cloud]",
        "[Finding 3: e.g., [X] SQL Server + [X] Windows Server AHB-eligible -- saving Xm/yr]",
        "[Finding 4: e.g., [X] Oracle RAC clusters identified; Oracle practice engaged]",
        "[Finding 5: e.g., [X]% of estate assessed as Cloud Ready or Cloud Friendly]",
    ]:
        elems.append(_bullet(doc, f))
    elems.append(_spacer(doc))

    # RECOMMENDATION
    elems.append(_heading(doc, "RECOMMENDATION", 2))
    elems.append(_bold_para(doc, "Primary cloud: ", "[HYPERSCALER] ([REGION])"))
    elems.append(_bold_para(doc, "Rationale: ",
        "[3 sentences. Must reference TCO saving %, licensing advantage, and compliance alignment. "
        "Do NOT name the hyperscaler above without citing these three evidence sources.]"))
    elems.append(_bold_para(doc, "Secondary (DR / specific workloads): ", "[HYPERSCALER]"))
    elems.append(_spacer(doc))

    # THREE-YEAR FINANCIAL SUMMARY (as a table)
    elems.append(_heading(doc, "THREE-YEAR FINANCIAL SUMMARY", 2))
    fin_table = doc.add_table(rows=4, cols=2)
    try:
        fin_table.style = "Table Grid"
    except Exception:
        pass
    fin_data = [
        ("On-premises status quo:",           "£ [X]M  (incl. ESU, hardware refresh, maintenance)"),
        ("[Primary cloud] (3yr RI + AHB/BYOL):", "£ [X]M"),
        ("Saving:",                            "£ [X]M  ( [X]% )"),
        ("Partner funding identified:",        "£ [X]M - £ [X]M  (AMM/MAP/PSO)"),
    ]
    for i, (label, val) in enumerate(fin_data):
        fin_table.rows[i].cells[0].text = label
        try:
            fin_table.rows[i].cells[0].paragraphs[0].runs[0].bold = True
        except Exception:
            pass
        fin_table.rows[i].cells[1].text = val
    elems.append(fin_table._element)
    elems.append(_spacer(doc))

    # NEXT STEPS
    elems.append(_heading(doc, "NEXT STEPS -- PART 2 ENGAGEMENT", 2))
    elems.append(_para(doc,
        "[Part 2 scope: 2-3 sentences describing the migration and modernisation engagement. "
        "Reference the primary cloud, wave plan structure, and any specialist workstreams "
        "(Oracle RAC, landing zone design, DC exit roadmap).]"))
    elems.append(_bold_para(doc, "Indicative investment: ", "[RANGE]"))
    elems.append(_bold_para(doc, "Target start: ", "[DATE]"))
    elems.append(_para(doc, "=" * 68))
    elems.append(_bold_para(doc, "Engagement Lead: ", "[NAME]  |  [EMAIL]  |  [PHONE]"))
    elems.append(_spacer(doc))

    # DMG Worked Example (orange warning header so it's easy to remove)
    elems.append(_heading(doc,
        "[WORKED EXAMPLE -- DMG Media UK -- Remove this section before sending to customer]",
        2, color=ORANGE))
    for item in [
        "Scope: 280 applications | 4,212 VMs | 2 data centres (Docklands + Sovereign House) | 16-week assessment",
        "Finding 1: 39% total cost reduction achievable on Azure (3yr RI + AHB applied)",
        "Finding 2: 340+ servers running Windows Server 2012 EoL OS; Azure Extended Security Updates included free",
        "Finding 3: 1,200+ Windows Server + 347 SQL Server licences AHB-eligible; estimated saving Xm/yr",
        "Finding 4: 18 Oracle RAC clusters identified; Oracle practice engagement underway",
        "Finding 5: 75% of estate assessed as Cloud Ready or Cloud Friendly",
        "Recommendation: Microsoft Azure (UK South primary / UK West DR)",
        "Rationale: Azure delivers 39% 3yr TCO saving vs 30% AWS / 34% GCP, driven by AHB on the Windows/SQL estate. Azure UK South holds FCA, ISO 27001, SOC 2 Type II, UK data residency compliance. Microsoft EA and Unified Support provide commercial continuity.",
        "Partner funding: £800K - £1.2M (Microsoft AMM confirmed eligible; deal registration initiated Phase 1 Week 3)",
        "Part 2 scope: Landing Zone design, migration factory engagement, Wave 0 PoC (50 VMs), Oracle RAC modernisation planning, DC exit roadmap",
    ]:
        elems.append(_bullet(doc, item, size=9))

    elems.append(_spacer(doc))
    return elems

# ── Missing section placeholders (4D.1) ─────────────────────────────────────

def add_placeholder_sections(doc, body, missing):
    if not missing:
        return
    body.append(_para(doc,
        "--- SECTIONS BELOW ADDED BY AUDIT SCRIPT (complete with engagement data) ---",
        italic=True, bold=True))
    for section_name in missing:
        body.append(_spacer(doc))
        body.append(_heading(doc, section_name, 1))
        body.append(_para(doc,
            f"[PLACEHOLDER: Complete this section with actual engagement data. "
            f"See Templates/executive-reporting/REPORTING-TEMPLATES-AUDIT-SPEC.md "
            f"for content guidance on '{section_name}'.]",
            italic=True))

# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    doc = Document(FILE)
    body = doc.element.body

    print(f"Auditing: {FILE}")
    print(f"Total paragraphs: {len(doc.paragraphs)}")

    texts = all_texts(doc)

    # ── 4D.1: Audit ─────────────────────────────────────────────────────────
    print("\n4D.1 Audit Results:")
    print("=" * 60)
    present_count = 0
    missing_sections = []
    for section_name, keyword in REQUIRED_SECTIONS:
        found = section_present(texts, keyword)
        print(f"  [{'OK  ' if found else 'MISS'}] {section_name}")
        if found:
            present_count += 1
        else:
            missing_sections.append(section_name)
    print(f"\n  Present: {present_count}/{len(REQUIRED_SECTIONS)}")
    print(f"  Missing: {len(missing_sections)}")

    # ── 10.6(a): Header block ────────────────────────────────────────────────
    if section_present(texts, "document information"):
        print("\n10.6: Header block already present -- skipping")
    else:
        print("\n10.6: Adding header block at document start...")
        header_elem = build_header_block(doc)
        spacer_elem = _spacer(doc)
        body.insert(0, spacer_elem)
        body.insert(0, header_elem)
        print("  Header block inserted at position 0")

    # ── 4D.2: Board-extractable executive summary ────────────────────────────
    if section_present(all_texts(doc), "scope assessed"):
        print("\n4D.2: Board-extractable executive summary already present -- skipping")
    else:
        print("\n4D.2: Adding board-extractable executive summary...")
        # Insert after header block (position 3) to keep it near the top
        exec_elems = build_board_exec_summary(doc)
        insert_pos = min(3, len(list(body)))
        for offset, elem in enumerate(exec_elems):
            body.insert(insert_pos + offset, elem)
        print(f"  Board-extractable executive summary added ({len(exec_elems)} elements)")

    # ── 4D.1: Add missing sections as placeholders ───────────────────────────
    if missing_sections:
        print(f"\n4D.1: Appending {len(missing_sections)} placeholder sections...")
        add_placeholder_sections(doc, body, missing_sections)

    doc.save(FILE)
    print(f"\nSaved: {FILE}")

    # Verification
    doc2 = Document(FILE)
    texts2 = all_texts(doc2)
    checks = [
        ("Header block",                 "document information"),
        ("Board exec summary",           "scope assessed"),
        ("Recommendation section",       "recommendation"),
        ("TCO Analysis",                 "tco analysis"),
        ("Partner Funding",              "partner funding"),
        ("Evidence-before-rec note",     "evidence"),
    ]
    print("\nVerification:")
    for label, keyword in checks:
        found = section_present(texts2, keyword)
        print(f"  {'OK' if found else 'MISSING'}: {label}")
    print(f"  Total paragraphs after: {len(doc2.paragraphs)}")


if __name__ == "__main__":
    main()
