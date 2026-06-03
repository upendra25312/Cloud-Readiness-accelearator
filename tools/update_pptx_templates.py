#!/usr/bin/env python3
"""
10.5: Add cover slide to all CRA PPTX templates
4D.4: Audit cra-executive-summary-v3.pptx -- verify 18-slide structure and
      evidence-before-recommendation ordering; add missing slides
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAX_RED  = RGBColor(0xE3, 0x1C, 0x3D)
WHITE    = RGBColor(0xFF, 0xFF, 0xFF)
DARK     = RGBColor(0x1A, 0x1A, 0x1A)
GREY     = RGBColor(0x64, 0x64, 0x64)
LT_GREY  = RGBColor(0xF2, 0xF2, 0xF2)

# ── Slide move helper ─────────────────────────────────────────────────────────

def move_slide_to_front(prs):
    """Move the last slide (just added) to position 0."""
    xml_slides = prs.slides._sldIdLst
    last = xml_slides[-1]
    xml_slides.remove(last)
    xml_slides.insert(0, last)


# ── Text-box helpers ──────────────────────────────────────────────────────────

def _tb(slide, left, top, width, height):
    return slide.shapes.add_textbox(left, top, width, height)


def _label_value_box(slide, left, top, width, height, label, value,
                     label_size=9, value_size=9):
    tb = _tb(slide, left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    r1 = p1.add_run()
    r1.text = label
    r1.font.bold = True
    r1.font.size = Pt(label_size)
    r1.font.color.rgb = RAX_RED
    p2 = tf.add_paragraph()
    r2 = p2.add_run()
    r2.text = value
    r2.font.size = Pt(value_size)
    return tb


def _rect(slide, left, top, width, height, fill_color, line_color=None):
    shape = slide.shapes.add_shape(1, left, top, width, height)  # MSO_SHAPE_TYPE.RECTANGLE = 1
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.color.rgb = line_color
    else:
        shape.line.fill.background()
    return shape


# ── Cover slide builder (10.5) ────────────────────────────────────────────────

def add_cover_slide(prs, template_name, phase_label, purpose,
                    audience, when_to_use, version, customise_items):
    """
    Add a Rackspace-branded cover slide and move it to position 0.
    Layout: dark top strip, red band with template name, white body with
    purpose / audience / when-to-use / what-to-customise sections.
    """
    # Use blank layout (usually index 6; fall back to 0)
    blank_layout = prs.slide_layouts[6] if len(prs.slide_layouts) > 6 else prs.slide_layouts[0]
    slide = prs.slides.add_slide(blank_layout)

    W = prs.slide_width
    H = prs.slide_height

    # Dark top strip
    _rect(slide, 0, 0, W, int(H * 0.22), DARK)

    # Red band (covers the lower part of the dark strip into the white area)
    band_top = int(H * 0.18)
    band_h   = int(H * 0.20)
    _rect(slide, 0, band_top, W, band_h, RAX_RED)

    # "RACKSPACE" label in dark strip (top left)
    tb_brand = _tb(slide, Inches(0.4), Inches(0.12), Inches(3), Inches(0.35))
    p_brand = tb_brand.text_frame.paragraphs[0]
    r_brand = p_brand.add_run()
    r_brand.text = "RACKSPACE TECHNOLOGY"
    r_brand.font.bold = True
    r_brand.font.size = Pt(10)
    r_brand.font.color.rgb = WHITE

    # Template name in red band
    tb_title = _tb(slide, Inches(0.4), int(H * 0.20), W - Inches(0.8), int(H * 0.16))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    r_title = p_title.add_run()
    r_title.text = template_name
    r_title.font.bold = True
    r_title.font.size = Pt(26)
    r_title.font.color.rgb = WHITE

    # Phase label (just below red band)
    tb_phase = _tb(slide, Inches(0.4), int(H * 0.40), W - Inches(0.8), Inches(0.4))
    p_phase = tb_phase.text_frame.paragraphs[0]
    r_phase = p_phase.add_run()
    r_phase.text = phase_label
    r_phase.font.size = Pt(12)
    r_phase.font.color.rgb = GREY

    # PURPOSE section
    tb_purpose = _tb(slide, Inches(0.4), int(H * 0.48), W - Inches(0.8), int(H * 0.14))
    tf_purpose = tb_purpose.text_frame
    tf_purpose.word_wrap = True
    p_pur_h = tf_purpose.paragraphs[0]
    r_pur_h = p_pur_h.add_run()
    r_pur_h.text = "PURPOSE"
    r_pur_h.font.bold = True
    r_pur_h.font.size = Pt(9)
    r_pur_h.font.color.rgb = RAX_RED
    p_pur_b = tf_purpose.add_paragraph()
    r_pur_b = p_pur_b.add_run()
    r_pur_b.text = purpose
    r_pur_b.font.size = Pt(9)

    # AUDIENCE | WHEN TO USE | VERSION row
    footer_y = int(H * 0.65)
    footer_h = Inches(0.55)
    col1_w = int(W * 0.30)
    col2_w = int(W * 0.38)
    col3_w = int(W * 0.20)

    _label_value_box(slide, Inches(0.4),          footer_y, col1_w, footer_h,
                     "AUDIENCE",    audience)
    _label_value_box(slide, Inches(0.4) + col1_w, footer_y, col2_w, footer_h,
                     "WHEN TO USE", when_to_use)
    _label_value_box(slide, W - Inches(0.4) - col3_w, footer_y, col3_w, footer_h,
                     "VERSION",     version)

    # WHAT TO CUSTOMISE
    cust_y = int(H * 0.75)
    tb_cust = _tb(slide, Inches(0.4), cust_y, W - Inches(0.8), int(H * 0.16))
    tf_cust = tb_cust.text_frame
    tf_cust.word_wrap = True
    p_ch = tf_cust.paragraphs[0]
    r_ch = p_ch.add_run()
    r_ch.text = "WHAT TO CUSTOMISE"
    r_ch.font.bold = True
    r_ch.font.size = Pt(9)
    r_ch.font.color.rgb = RAX_RED
    for item in customise_items:
        p_ci = tf_cust.add_paragraph()
        r_ci = p_ci.add_run()
        r_ci.text = "- " + item
        r_ci.font.size = Pt(9)

    # Footer line
    tb_footer = _tb(slide, Inches(0.4), int(H * 0.93), W - Inches(0.8), Inches(0.25))
    p_f = tb_footer.text_frame.paragraphs[0]
    r_f = p_f.add_run()
    r_f.text = (
        "CRA Framework v2.0 -- Rackspace Cloud Solutions Architecture  |  "
        "Confidential  |  (c) 2026 Rackspace Technology"
    )
    r_f.font.size = Pt(7)
    r_f.font.color.rgb = GREY

    move_slide_to_front(prs)
    return slide


# ── 4D.4: PPTX structure audit + missing slide insertion ─────────────────────

# Required 18-slide structure for cra-executive-summary-v3.pptx
REQUIRED_SLIDES = [
    "Cover",
    "Agenda",
    "Engagement Scope",
    "Assessment Methodology",
    "Infrastructure Summary",
    "Application Landscape",
    "Cloud Readiness Profile",
    "Three-Cloud Comparison",
    "TCO Analysis",
    "Licensing Overlay",
    "Partner Funding",
    "Hyperscaler Scoring Matrix",
    "Recommendation",
    "Migration Approach",
    "Risk Register",
    "Partner Funding & Timeline",
    "Part 2 Entry Point",
    "Questions & Next Steps",
]


def get_slide_titles(prs):
    titles = []
    for slide in prs.slides:
        title = ""
        for shape in slide.shapes:
            if shape.has_text_frame and shape.shape_type in (13, 1, 17):
                text = shape.text_frame.text.strip()
                if text:
                    title = text
                    break
        if not title:
            # grab any first text
            for shape in slide.shapes:
                if shape.has_text_frame:
                    title = shape.text_frame.text.strip()[:60]
                    break
        titles.append(title)
    return titles


def slide_keyword_present(titles, keyword):
    return any(keyword.lower() in t.lower() for t in titles)


def add_placeholder_slide(prs, slide_title, notes_text=""):
    """Add a simple placeholder slide at the end with a title."""
    blank_layout = prs.slide_layouts[6] if len(prs.slide_layouts) > 6 else prs.slide_layouts[0]
    slide = prs.slides.add_slide(blank_layout)

    W = prs.slide_width
    H = prs.slide_height

    # Red header band
    _rect(slide, 0, 0, W, Inches(1.3), RAX_RED)

    # Title in red band
    tb = _tb(slide, Inches(0.4), Inches(0.3), W - Inches(0.8), Inches(0.9))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = slide_title
    r.font.bold = True
    r.font.size = Pt(28)
    r.font.color.rgb = WHITE

    # Body placeholder
    tb2 = _tb(slide, Inches(0.6), Inches(1.6), W - Inches(1.2), H - Inches(2.0))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    r2 = p2.add_run()
    r2.text = f"[PLACEHOLDER: Complete '{slide_title}' with engagement data.]"
    r2.font.size = Pt(14)
    r2.font.color.rgb = GREY

    # Speaker notes
    if notes_text:
        slide.notes_slide.notes_text_frame.text = notes_text
    else:
        slide.notes_slide.notes_text_frame.text = (
            f"[What this slide shows]\n"
            f"This is the '{slide_title}' slide.\n\n"
            f"[What to say]\n"
            f"- Complete with engagement-specific data before presenting.\n\n"
            f"[Customise before presenting]\n"
            f"- Replace placeholder text with actual findings."
        )

    return slide


SLIDE_NOTES = {
    "Cover":
        "Cover slide. State the customer name, engagement name, and date. "
        "Classify as CONFIDENTIAL in footer.",
    "Agenda":
        "Briefly walk through the agenda. Time-box each section for a live presentation. "
        "Typical session: 90 minutes including Q&A.",
    "Engagement Scope":
        "State what was in scope: application count, VM count, DC count, duration. "
        "Also state the scope confidence level (High/Medium/Low) and any late-breaking "
        "scope changes (e.g., a 57% variance like the DMG Media UK engagement).",
    "Assessment Methodology":
        "Show the CRA four-phase diagram. State the discovery tooling used "
        "(GCP Migration Center, RVTools, Azure Migrate, etc.) and the data quality grade.",
    "Infrastructure Summary":
        "VM count by OS / hypervisor / size tier. Highlight EoL OS flags. "
        "Link to Appendix for full detail.",
    "Application Landscape":
        "App count by criticality (P1/P2/P3). Tech stack distribution. "
        "Highlight Oracle RAC and OSS licensing risks if present.",
    "Cloud Readiness Profile":
        "Show the readiness distribution: Cloud Ready / Cloud Friendly / Cloud Challenged / Blocked. "
        "Bar chart is clearest. Call out the % that requires re-architecture.",
    "Three-Cloud Comparison":
        "CRITICAL: All three clouds must be shown in equal columns. "
        "Do NOT use language that pre-judges the outcome. "
        "Compare on: cost (headline TCO), technical fit, compliance, commercial.",
    "TCO Analysis":
        "Three-year comparison chart. Show on-prem status quo vs Azure vs AWS vs GCP. "
        "Ensure on-prem baseline INCLUDES ESU costs and hardware refresh. "
        "Show Year 1 dual-running cost. Year 1 dual-running is often 15-25% higher than steady state.",
    "Licensing Overlay":
        "Show AHB impact (Windows + SQL Server count and £/$ saving). "
        "Show Oracle BYOL options. Show net TCO AFTER licensing overlay. "
        "This is often the slide that changes the recommendation relative to pure compute cost.",
    "Partner Funding":
        "MANDATORY: Show AMM / MAP / PSO eligibility and estimated credit value. "
        "This is a Rackspace commercial differentiator. Do NOT put this in the appendix. "
        "State whether deal registration has been initiated.",
    "Hyperscaler Scoring Matrix":
        "Show the weighted criteria table: TCO 30%, Licensing 20%, Technical Fit 15%, "
        "Compliance 15%, Partner Commercial 10%, Strategic 10%. "
        "Show scores for all three clouds with evidence column. "
        "Customer must have agreed the weights BEFORE scoring begins.",
    "Recommendation":
        "CRITICAL: This slide must come AFTER the scoring matrix (slide 12). "
        "Each bullet MUST cite a specific data point (e.g., 'Azure 39% saving -- see slide 9'). "
        "Do NOT say 'Azure offers the best value' without citing the evidence slides.",
    "Migration Approach":
        "7Rs estate view: Rehost / Replatform / Rearchitect / Repurchase / Retire / Retain counts. "
        "5-wave plan overview. Define Wave 0 PoC (target: 50 VMs, 8-12 weeks).",
    "Risk Register":
        "Top 10 risks in table format: RAG status, mitigation. "
        "Ensure Oracle risks (if present), data residency, and EoL OS are in the register.",
    "Partner Funding & Timeline":
        "AMM/MAP/PSO registration timeline. Show that deal registration was (or will be) "
        "completed before Part 2 SOW countersignature. This protects partner funding.",
    "Part 2 Entry Point":
        "Part 2 scope, indicative investment range (pre-approved by Pre-Sales Director), "
        "timeline, and next steps. The customer should be able to decide at this meeting "
        "whether to proceed.",
    "Questions & Next Steps":
        "CTA: who needs to sign what by when. Immediate actions (alliance registration, "
        "Part 2 kickoff date, AMM submission). Leave 15-20 min for Q&A.",
}


def audit_pptx(file_path):
    """4D.4: Audit cra-executive-summary-v3.pptx structure."""
    prs = Presentation(file_path)
    titles = get_slide_titles(prs)

    print(f"\n4D.4 Audit: {os.path.basename(file_path)}")
    print(f"  Current slide count: {len(prs.slides)}")
    print("  Current slide titles:")
    for i, t in enumerate(titles, 1):
        print(f"    Slide {i:2d}: {t[:70]}")

    # Check recommendation placement
    rec_slide = None
    for i, t in enumerate(titles):
        if "recommendation" in t.lower():
            rec_slide = i + 1
            break

    if rec_slide:
        if rec_slide >= 13:
            print(f"  OK: Recommendation on slide {rec_slide} (>= 13) -- evidence-before-recommendation satisfied")
        else:
            print(f"  WARNING: Recommendation on slide {rec_slide} (<13) -- restructure required!")
    else:
        print("  INFO: No 'Recommendation' slide found in current titles")

    # Check which required slides are present
    print("\n  Required slide check:")
    missing_slides = []
    for req in REQUIRED_SLIDES:
        keywords = {
            "Three-Cloud Comparison": ["three-cloud", "cloud comparison", "comparison"],
            "Hyperscaler Scoring Matrix": ["scoring", "matrix", "weighted"],
            "Partner Funding & Timeline": ["partner funding", "timeline", "funding"],
        }.get(req, [req.lower()])

        found = any(any(kw in t.lower() for kw in keywords) for t in titles)
        print(f"    [{'OK  ' if found else 'MISS'}] {req}")
        if not found:
            missing_slides.append(req)

    print(f"\n  Present: {len(REQUIRED_SLIDES) - len(missing_slides)}/{len(REQUIRED_SLIDES)}")
    if missing_slides:
        print(f"  Missing: {missing_slides}")

    return prs, missing_slides


# ── Per-template cover slide specs (10.5) ────────────────────────────────────

PPTX_TEMPLATES = [
    {
        "file": os.path.join(BASE, "Templates", "executive-reporting",
                             "cra-executive-summary-v3.pptx"),
        "label": "cra-executive-summary-v3.pptx",
        "audit_4d4": True,
        "template_name": "CRA Executive Summary Presentation",
        "phase_label": "Phase 3: Hyperscaler Evaluation --> Customer Playback",
        "purpose": (
            "This is the Phase 3 playback deck presented to the customer CTO and senior "
            "leadership team. It presents assessment findings, three-cloud comparison, "
            "TCO analysis, and hyperscaler recommendation. This is the most customer-visible "
            "CRA deliverable."
        ),
        "audience": "Customer CTO / IT Director + Rackspace Lead Architect",
        "when_to_use": "After Phase 3 TCO and scoring complete; before Part 2 SOW",
        "version": "v3.0",
        "customise": [
            "Replace [Customer Name] on every slide (20+ instances)",
            "Update all financial figures from your TCO model",
            "Populate the scoring matrix with your engagement's weighted scores",
            "Confirm Recommendation slide comes AFTER evidence slides 8-12",
            "Update partner funding slide with actual AMM/MAP/PSO eligibility",
        ],
    },
    {
        "file": os.path.join(BASE, "Templates", "executive-reporting",
                             "cra-executive-summary-template.pptx"),
        "label": "cra-executive-summary-template.pptx",
        "audit_4d4": False,
        "template_name": "CRA Executive Summary Template (v2)",
        "phase_label": "Phase 3: Hyperscaler Evaluation --> Customer Playback",
        "purpose": (
            "Earlier version of the Phase 3 playback deck (based on DMG Media UK format). "
            "Use cra-executive-summary-v3.pptx for new engagements. "
            "This version is retained as a format reference."
        ),
        "audience": "Customer CTO / IT Director + Rackspace Lead Architect",
        "when_to_use": "Reference only -- prefer v3 for new engagements",
        "version": "v2.0",
        "customise": [
            "Replace [Customer Name] and DMG-specific content throughout",
            "Update all financial figures from your TCO model",
            "Consider migrating to v3 structure for new engagements",
        ],
    },
    {
        "file": os.path.join(BASE, "Templates", "executive-reporting",
                             "cloud-strategy-generic.pptx"),
        "label": "cloud-strategy-generic.pptx",
        "audit_4d4": False,
        "template_name": "Cloud Strategy Overview",
        "phase_label": "Pre-Sales / Executive Briefing (before Phase 1)",
        "purpose": (
            "A pre-sales executive overview of cloud migration strategy for customers "
            "evaluating whether to start a cloud readiness assessment. Use this to set "
            "context before presenting the CRA framework to a new customer."
        ),
        "audience": "Customer VP/CIO (pre-sales) + Rackspace Pre-Sales Architect",
        "when_to_use": "Pre-sales discovery call or executive briefing; before CRA SOW is signed",
        "version": "v1.0",
        "customise": [
            "Add customer logo to title slide",
            "Adjust industry vertical examples to match customer sector",
            "Update market benchmark statistics to current year",
        ],
    },
    {
        "file": os.path.join(BASE, "Templates", "03-evaluation",
                             "azure-calculator-walkthrough.pptx"),
        "label": "azure-calculator-walkthrough.pptx",
        "audit_4d4": False,
        "template_name": "Azure Pricing Calculator Walkthrough",
        "phase_label": "Phase 3: TCO Validation",
        "purpose": (
            "Step-by-step guide for validating Azure pricing using the Azure Pricing "
            "Calculator and Azure Migrate pricing tool. Use this to verify TCO model "
            "prices match current Azure published rates."
        ),
        "audience": "Rackspace Platform Architect (Azure)",
        "when_to_use": "Phase 3, during TCO model validation (see TCO-TEMPLATES-AUDIT-SPEC.md 4B.9)",
        "version": "v1.0",
        "customise": [
            "Update pricing screenshots to current Azure pricing (valid for 90 days from last update)",
            "Confirm region selected matches customer requirements",
            "Update AHB eligibility count from your infrastructure-profiling.xlsx",
        ],
    },
]


# ── Cover-slide already-present check ────────────────────────────────────────

def cover_slide_present(prs):
    """Return True if slide 0 already has 'CRA Framework v2.0' footer text."""
    if not prs.slides:
        return False
    slide0 = prs.slides[0]
    for shape in slide0.shapes:
        if shape.has_text_frame:
            if "cra framework v2.0" in shape.text_frame.text.lower():
                return True
    return False


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("10.5 + 4D.4: Updating PPTX templates")
    print("=" * 60)

    for tpl in PPTX_TEMPLATES:
        if not os.path.exists(tpl["file"]):
            print(f"\nSKIP (not found): {tpl['label']}")
            continue

        print(f"\nProcessing: {tpl['label']}")

        # 4D.4 audit (exec summary v3 only)
        if tpl.get("audit_4d4"):
            prs, missing = audit_pptx(tpl["file"])
            if missing:
                print(f"\n  Adding {len(missing)} missing placeholder slides...")
                for slide_title in missing:
                    add_placeholder_slide(prs, slide_title,
                                          notes_text=SLIDE_NOTES.get(slide_title, ""))
                    print(f"    Added: {slide_title}")
        else:
            prs = Presentation(tpl["file"])

        # 10.5: Add cover slide
        if cover_slide_present(prs):
            print(f"  SKIP cover slide (already present)")
        else:
            print(f"  Adding cover slide...")
            add_cover_slide(
                prs,
                tpl["template_name"],
                tpl["phase_label"],
                tpl["purpose"],
                tpl["audience"],
                tpl["when_to_use"],
                tpl["version"],
                tpl["customise"],
            )
            print(f"  Cover slide added (now slide 1 of {len(prs.slides)})")

        prs.save(tpl["file"])
        print(f"  Saved: {tpl['label']}")

    print("\n\nVerification:")
    for tpl in PPTX_TEMPLATES:
        if not os.path.exists(tpl["file"]):
            continue
        prs2 = Presentation(tpl["file"])
        has_cover = cover_slide_present(prs2)
        count = len(prs2.slides)
        print(f"  {tpl['label']}: {count} slides, cover={'OK' if has_cover else 'MISSING'}")


if __name__ == "__main__":
    main()
