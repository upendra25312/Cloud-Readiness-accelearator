#!/usr/bin/env python3
"""
4E.4: Apply Aktiv Grotesk font to all PPTX and DOCX templates.

Replaces common system fonts (Calibri, Calibri Light, Arial, Helvetica,
Trebuchet MS, Segoe UI) with Aktiv Grotesk across:
  - PPTX: theme XML, slide masters, slide layouts, individual slides
  - DOCX: theme XML, styles, document body, headers, footers

NOTE: Aktiv Grotesk must be installed on the rendering machine for the font
to display correctly. Without the font installed, Office substitutes a fallback
automatically — the file remains valid and openable either way.
"""

import os
import zipfile

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TARGET_FONT = "Aktiv Grotesk"

# Ordered: multi-word names first to avoid partial substring matches
REPLACE_FONTS = [
    "Calibri Light",
    "Trebuchet MS",
    "Segoe UI",
    "Calibri",
    "Arial",
    "Helvetica",
]

PPTX_FILES = [
    # Templates
    os.path.join(BASE, "Templates", "executive-reporting", "cra-executive-summary-v3.pptx"),
    os.path.join(BASE, "Templates", "executive-reporting", "cra-executive-summary-template.pptx"),
    os.path.join(BASE, "Templates", "executive-reporting", "cloud-strategy-generic.pptx"),
    os.path.join(BASE, "Templates", "executive-reporting", "ms-solution-assessment.pptx"),
    os.path.join(BASE, "Templates", "03-evaluation", "azure-calculator-walkthrough.pptx"),
    # Presentations
    os.path.join(BASE, "presentations", "executive", "CRA-Executive-Overview.pptx"),
    os.path.join(BASE, "presentations", "executive", "CRA-Leadership-Overview.pptx"),
    os.path.join(BASE, "presentations", "executive", "cra-overview-v1.1.pptx"),
    os.path.join(BASE, "presentations", "alliance", "CRA-Microsoft-Partner-Deck.pptx"),
    os.path.join(BASE, "presentations", "alliance", "CRA-AWS-Partner-Deck.pptx"),
    os.path.join(BASE, "presentations", "alliance", "CRA-GCP-Partner-Deck.pptx"),
    os.path.join(BASE, "presentations", "technical", "CRA-Technical-Overview.pptx"),
    os.path.join(BASE, "docs", "guides", "data-gathering-guide.pptx"),
]

DOCX_FILES = [
    os.path.join(BASE, "Templates", "executive-reporting", "cra-assessment-report-template-v3.docx"),
    os.path.join(BASE, "Templates", "executive-reporting", "cra-phase1-report-template.docx"),
    os.path.join(BASE, "Templates", "executive-reporting", "part2-entry-point-template.docx"),
    os.path.join(BASE, "Templates", "04-planning", "sow-template.docx"),
    os.path.join(BASE, "Templates", "04-planning", "governance-workshop-schedule.docx"),
]

# XML path prefixes to process inside each archive
PPTX_XML_PREFIXES = ("ppt/",)
DOCX_XML_PREFIXES = ("word/",)


def replace_fonts_in_xml(data: bytes) -> tuple:
    """Replace known system fonts with Aktiv Grotesk. Returns (patched_data, replacement_count)."""
    total = 0
    for font in REPLACE_FONTS:
        # Covers: typeface="Font" (PPTX/theme), w:ascii="Font" w:hAnsi="Font" w:cs="Font" (DOCX)
        patterns = [
            (f'typeface="{font}"',  f'typeface="{TARGET_FONT}"'),
            (f"typeface='{font}'",  f"typeface='{TARGET_FONT}'"),
            (f'w:ascii="{font}"',   f'w:ascii="{TARGET_FONT}"'),
            (f"w:ascii='{font}'",   f"w:ascii='{TARGET_FONT}'"),
            (f'w:hAnsi="{font}"',   f'w:hAnsi="{TARGET_FONT}"'),
            (f"w:hAnsi='{font}'",   f"w:hAnsi='{TARGET_FONT}'"),
            (f'w:cs="{font}"',      f'w:cs="{TARGET_FONT}"'),
            (f"w:cs='{font}'",      f"w:cs='{TARGET_FONT}'"),
            (f'w:eastAsia="{font}"', f'w:eastAsia="{TARGET_FONT}"'),
        ]
        for old_str, new_str in patterns:
            old_b, new_b = old_str.encode(), new_str.encode()
            n = data.count(old_b)
            if n:
                data = data.replace(old_b, new_b)
                total += n
    return data, total


def patch_office_file(path: str, xml_prefixes: tuple) -> int:
    """
    Open an Office file as a ZIP archive, replace fonts in all XML parts whose
    path starts with one of xml_prefixes, then write the patched file in-place.
    Returns the total number of attribute replacements made.
    """
    total = 0
    tmp = path + "._font_tmp"
    try:
        with zipfile.ZipFile(path, "r") as zin:
            with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
                for item in zin.infolist():
                    data = zin.read(item.filename)
                    if item.filename.endswith(".xml") and item.filename.startswith(xml_prefixes):
                        patched, count = replace_fonts_in_xml(data)
                        data = patched
                        total += count
                    zout.writestr(item, data)
        os.replace(tmp, path)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise
    return total


def process_file(path: str, xml_prefixes: tuple):
    label = os.path.relpath(path, BASE)
    if not os.path.exists(path):
        print(f"  SKIP (not found): {label}")
        return
    count = patch_office_file(path, xml_prefixes)
    if count:
        print(f"  {label}: {count} font attribute(s) replaced")
    else:
        print(f"  {label}: no target fonts found (already Aktiv Grotesk or no explicit font set)")


def main():
    print("4E.4: Apply Aktiv Grotesk font to all CRA PPTX and DOCX files")
    print("=" * 70)
    print(f"  Target font : {TARGET_FONT}")
    print(f"  Replacing   : {', '.join(REPLACE_FONTS)}")
    print()

    print("[PPTX — Templates and Presentations]")
    print("-" * 70)
    for path in PPTX_FILES:
        process_file(path, PPTX_XML_PREFIXES)

    print()
    print("[DOCX — Templates]")
    print("-" * 70)
    for path in DOCX_FILES:
        process_file(path, DOCX_XML_PREFIXES)

    print()
    print("=" * 70)
    print("Complete.")
    print()
    print("IMPORTANT: Aktiv Grotesk must be installed on each machine that opens")
    print("these files. If not installed, Office will auto-substitute a fallback")
    print("font. Download from: https://brand.rackspace.com (internal font portal)")


if __name__ == "__main__":
    main()
