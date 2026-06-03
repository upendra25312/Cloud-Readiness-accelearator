#!/usr/bin/env python3
"""
4D.5: Add 3 missing clauses to sow-template.docx
- Clause 1: Scope Variance Management (after Section 2.5, before Section 3)
- Clause 2: Utilisation Data Gate (after Section 3.3 deliverables, before Section 3.4)
- Clause 3: Alliance Partner Funding (after Section 12 body, before Section 13 Signatures)
"""
import os, copy
from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from lxml import etree

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(BASE, "Templates", "04-planning", "sow-template.docx")

# Rackspace red
RAX_RED = RGBColor(0xE3, 0x1C, 0x3D)


def _insert_after(body, ref_element, new_element):
    """Insert new_element immediately after ref_element in body."""
    ref_idx = list(body).index(ref_element)
    body.insert(ref_idx + 1, new_element)


def make_heading2(doc, text):
    p = doc.add_paragraph(text, style="Heading 2")
    for run in p.runs:
        run.font.color.rgb = RAX_RED
    return p._element


def make_normal(doc, text):
    p = doc.add_paragraph(text, style="Normal")
    return p._element


def make_normal_bold_intro(doc, label, body_text):
    """Paragraph with a bold label followed by normal text."""
    p = doc.add_paragraph(style="Normal")
    run_label = p.add_run(label + "  ")
    run_label.bold = True
    p.add_run(body_text)
    return p._element


def make_notice_box(doc, text):
    """Important notice paragraph — bold red border style."""
    p = doc.add_paragraph(style="Normal")
    run = p.add_run(text)
    run.bold = True
    run.font.color.rgb = RAX_RED
    # Add subtle left-indent shading via paragraph XML border
    pPr = p._p.get_or_add_pPr()
    pBdr = etree.SubElement(pPr, qn("w:pBdr"))
    left = etree.SubElement(pBdr, qn("w:left"))
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), "12")
    left.set(qn("w:space"), "4")
    left.set(qn("w:color"), "E31C3D")
    return p._element


def make_blockquote(doc, text):
    """Body text styled as a block-quote / clause verbatim."""
    p = doc.add_paragraph(style="Normal")
    run = p.add_run(text)
    run.font.size = Pt(9)
    run.font.italic = True
    # Left indent
    pPr = p._p.get_or_add_pPr()
    ind = etree.SubElement(pPr, qn("w:ind"))
    ind.set(qn("w:left"), "720")   # ~0.5 inch
    ind.set(qn("w:right"), "360")
    # Light grey shading
    shd = etree.SubElement(pPr, qn("w:shd"))
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), "F2F2F2")
    return p._element


def make_spacer(doc):
    return doc.add_paragraph("")._element


def find_para_index(doc, partial_text):
    """Return index of first paragraph whose text contains partial_text."""
    for i, p in enumerate(doc.paragraphs):
        if partial_text in p.text:
            return i
    return None


def get_para_element(doc, index):
    return doc.paragraphs[index]._element


def main():
    doc = Document(FILE)
    body = doc.element.body

    # ── CLAUSE 1: Scope Variance Management ─────────────────────────────────
    # Insert after the last bullet of Section 2.5 (para 58), before Section 3 heading (para 59)

    # Find "3. Scope of Services" heading as anchor
    scope_idx = find_para_index(doc, "3. Scope of Services")
    if scope_idx is None:
        print("WARNING: Could not find '3. Scope of Services' -- skipping Clause 1")
    else:
        anchor = get_para_element(doc, scope_idx)

        elements_to_insert = []
        elements_to_insert.append(make_spacer(doc))
        elements_to_insert.append(make_heading2(doc, "2.6 Scope Variance Management"))
        elements_to_insert.append(make_notice_box(doc,
            "IMPORTANT: Scope variance is the single most common source of commercial dispute "
            "in CRA engagements. This clause is mandatory and must not be removed."))
        elements_to_insert.append(make_normal(doc,
            "The estate scope provided by [CUSTOMER NAME] is an estimate based on "
            "[CMDB / customer-provided data / vCenter export] as at [DATE]. Rackspace will "
            "conduct an independent VM count during Phase 1 (Weeks 1-2). If the independently "
            "assessed estate exceeds the estimated scope by more than 15%, Rackspace will issue "
            "a Change Control Notification within 5 business days."))
        elements_to_insert.append(make_blockquote(doc,
            "Scope Variance Clause: The engagement will continue at current scope until the "
            "Change Control is agreed. Rackspace will not perform work materially outside the "
            "agreed scope without a signed Change Control. If the estate is larger than estimated, "
            "Rackspace will present the additional effort and cost for customer approval before "
            "proceeding."))
        elements_to_insert.append(make_normal(doc,
            "Scope confidence is classified at engagement start (High / Medium / Low) based on "
            "the quality of the customer-provided estate data. A Low confidence rating triggers "
            "an early VM count validation in Phase 0."))

        # Insert all elements before the anchor
        anchor_idx = list(body).index(anchor)
        for offset, elem in enumerate(elements_to_insert):
            body.insert(anchor_idx + offset, elem)
        print("  Clause 1 (Scope Variance) inserted before '3. Scope of Services'")

    # ── CLAUSE 2: Utilisation Data Gate ─────────────────────────────────────
    # Insert after Section 3.3 deliverables, before Section 3.4 heading

    # Re-parse paragraphs after insertions
    phase4_idx = find_para_index(doc, "Phase 3")
    if phase4_idx is None:
        phase4_idx = find_para_index(doc, "3.4 Phase")
    if phase4_idx is None:
        print("WARNING: Could not find Phase 3/3.4 heading -- skipping Clause 2")
    else:
        anchor2 = get_para_element(doc, phase4_idx)

        elements2 = []
        elements2.append(make_spacer(doc))
        elements2.append(make_heading2(doc, "3.3A Utilisation Data Quality Gate"))
        elements2.append(make_notice_box(doc,
            "GATE: Phase 3 (Evaluation) cannot commence until this data quality gate is passed. "
            "A TCO model built on insufficient data has +/-30-50% accuracy. This clause protects "
            "both Rackspace and the customer from a defensible recommendation."))
        elements2.append(make_normal(doc,
            "Phase 3 (Hyperscaler Evaluation and TCO Analysis) cannot commence until a minimum "
            "of [14] calendar days of clean CPU, RAM, storage, and network utilisation data has "
            "been collected from 90% or more of the in-scope VM estate."))
        elements2.append(make_blockquote(doc,
            "Utilisation Data Gate Clause: Rackspace will provide a weekly data quality report "
            "to [CUSTOMER CONTACT NAME] showing collection coverage percentage and data quality "
            "grade. If schedule pressure arises, Rackspace will present the financial risk in "
            "writing: a TCO model built on fewer than 14 days of data has +/-30-50% accuracy, "
            "versus +/-10-15% accuracy with 28 or more days of data. The customer may approve "
            "proceeding with reduced data quality by signing a Data Quality Waiver, which "
            "Rackspace will attach to the final report."))
        elements2.append(make_normal(doc,
            "Recommended minimum: 14 days. Target: 28 days. Extended data collection beyond "
            "28 days is available if the customer timeline permits and improves TCO accuracy."))

        anchor2_idx = list(body).index(anchor2)
        for offset, elem in enumerate(elements2):
            body.insert(anchor2_idx + offset, elem)
        print("  Clause 2 (Utilisation Data Gate) inserted before Phase 3/3.4")

    # ── CLAUSE 3: Alliance Partner Funding ───────────────────────────────────
    # Insert after Section 12 body, before Section 13 Signatures

    sig_idx = find_para_index(doc, "13. Signatures")
    if sig_idx is None:
        print("WARNING: Could not find '13. Signatures' -- skipping Clause 3")
    else:
        anchor3 = get_para_element(doc, sig_idx)

        elements3 = []
        elements3.append(make_spacer(doc))
        elements3.append(make_heading2(doc, "12.1 Alliance Partner Funding"))
        elements3.append(make_notice_box(doc,
            "IMPORTANT: Deal registration must be completed before Part 2 SOW countersignature. "
            "Failure to register early is the most common reason partner funding is lost. "
            "This clause is mandatory and must not be removed."))
        elements3.append(make_normal(doc,
            "Rackspace will identify applicable hyperscaler partner funding programmes "
            "(Microsoft Azure Migration and Modernisation / AWS Migration Acceleration Programme "
            "/ Google Cloud PSO Credits) at engagement start. Where the customer is eligible, "
            "Rackspace will initiate deal registration with the relevant partner programme "
            "during Phase 1."))
        elements3.append(make_blockquote(doc,
            "Alliance Partner Registration Clause: Formal deal registration submission will be "
            "completed before the Part 2 Statement of Work is countersigned by Rackspace. "
            "This clause does not guarantee funding approval; it ensures registration is "
            "completed at the earliest eligible stage. Rackspace will provide written "
            "confirmation of registration status to the customer within 5 business days of "
            "registration submission."))
        elements3.append(make_normal(doc,
            "Applicable programmes at time of engagement:"))
        for prog in [
            "Microsoft Azure Migration and Modernisation (AMM) -- eligible for Windows/SQL estates migrating to Azure",
            "AWS Migration Acceleration Programme (MAP) -- eligible for workloads migrating to AWS",
            "Google Cloud PSO Credits / Cloud Ready Programmes -- eligible for workloads migrating to GCP",
        ]:
            p = doc.add_paragraph(style="List Paragraph")
            p.add_run(prog)
            elements3.append(p._element)
        elements3.append(make_normal(doc,
            "Estimated partner funding value will be documented in the Phase 3 executive report "
            "and presentation. Actual funding is subject to hyperscaler programme approval and "
            "is not a commercial commitment by Rackspace."))

        anchor3_idx = list(body).index(anchor3)
        for offset, elem in enumerate(elements3):
            body.insert(anchor3_idx + offset, elem)
        print("  Clause 3 (Alliance Partner Funding) inserted before '13. Signatures'")

    doc.save(FILE)
    print(f"\nSaved: {FILE}")

    # Verify
    doc2 = Document(FILE)
    clause_checks = [
        "2.6 Scope Variance Management",
        "3.3A Utilisation Data Quality Gate",
        "12.1 Alliance Partner Funding",
    ]
    for check in clause_checks:
        found = any(check in p.text for p in doc2.paragraphs)
        print(f"  {'OK' if found else 'MISSING'}: {check}")


if __name__ == "__main__":
    main()
