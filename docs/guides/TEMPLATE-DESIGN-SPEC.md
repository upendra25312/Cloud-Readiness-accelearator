# Template Design Specification — Cover Slides, Header Blocks & Usability Standards

**Covers Epics:** 10.5 (PPTX cover slides), 10.6 (DOCX header blocks)  
**Applies to:** All CRA framework templates in `Templates/` and all guide documents in `docs/`  
**How to use this spec:** Follow these standards when creating new templates or updating existing ones. The goal is that any architect picking up a template for the first time knows immediately: what it is, who fills it in, when, and what to do with it.

---

## Why Templates Must Be Self-Contained

> "A framework that requires tribal knowledge defeats its own purpose."

A template that has no instructions, no context, and no guidance becomes usable only by people who already know how to use it. That is the opposite of an accelerator.

**The two-minute test:** If a cloud architect who has never seen the CRA framework opens a template, can they:
1. Understand what the template is for? ✅ / ❌
2. Know what phase of the engagement it belongs to? ✅ / ❌
3. Understand who fills in which parts? ✅ / ❌
4. Find the instructions without asking anyone? ✅ / ❌

If any answer is ❌ — the template needs a cover slide, header block, or Instructions tab.

---

## Epic 10.5 — Cover Slide Spec for PPTX Templates

Add a cover slide as **Slide 1** (before any content slides) to every CRA PowerPoint template.

### Standard Cover Slide Layout

```
┌─────────────────────────────────────────────────────────┐
│  [RACKSPACE LOGO — top right]                           │
│                                                         │
│                                                         │
│  ████████████████████████████████████████████████████   │
│  ██                                                 ██   │
│  ██  [TEMPLATE NAME — 28pt bold white]              ██   │
│  ██  [Subtitle: Phase X — Phase Name]               ██   │
│  ██                                                 ██   │
│  ████████████████████████████████████████████████████   │  ← Rackspace Red #E31C3D
│                                                         │
│  PURPOSE                                                │
│  [2–3 sentence description of what this template is     │
│   for and what deliverable it produces]                 │
│                                                         │
│  AUDIENCE          WHEN TO USE           VERSION        │
│  [Target reader]   [Phase + timing]      v[X.X]         │
│                                                         │
│  WHAT TO CUSTOMISE                                      │
│  ■ [Placeholder 1 — e.g., "Replace [Customer Name]"]   │
│  ■ [Placeholder 2 — e.g., "Update pricing to current"] │
│  ■ [Placeholder 3]                                      │
│                                                         │
│  ─────────────────────────────────────────────────────  │
│  CRA Framework v2.0 — Rackspace Cloud Solutions Arch.  │
│  © 2026 Rackspace Technology. All rights reserved.     │
└─────────────────────────────────────────────────────────┘
```

### Required Fields — Cover Slide

| Field | Where | Content Standard |
| --- | --- | --- |
| Template Name | Red band, 28pt bold white | Official template name matching the filename (e.g., "CRA Executive Summary Template") |
| Phase Label | Below template name, 18pt | "Phase 3: Hyperscaler Evaluation" or "Executive Reporting" |
| Rackspace Logo | Top right | White version on dark background; coloured version on white |
| Purpose Statement | Body, 12pt | 2–3 sentences. What the template produces. Who uses the output. |
| Audience | Footer row left | "Customer CTO + Rackspace Lead Architect" |
| When to Use | Footer row centre | "Phase 3 playback — after TCO and scoring complete" |
| Version | Footer row right | "v2.0" — update when structure changes |
| What to Customise | Bulleted list | 3–5 specific placeholders the architect must replace |
| Footer | Bottom line | "CRA Framework v2.0 — Rackspace Cloud Solutions Architecture" |

### Per-Template Cover Slide Content

#### `cra-executive-summary-v3.pptx`

```
Template Name:  CRA Executive Summary Presentation
Phase:          Phase 3: Hyperscaler Evaluation → Customer Playback

PURPOSE
This is the Phase 3 playback deck presented to the customer CTO and senior leadership team.
It presents the assessment findings, three-cloud comparison, TCO analysis, and hyperscaler
recommendation. This template is the most customer-visible CRA deliverable.

AUDIENCE: Customer CTO / IT Director + Rackspace Lead Architect
WHEN TO USE: After Phase 3 TCO and hyperscaler scoring are complete; before Part 2 SOW
VERSION: v3.0

WHAT TO CUSTOMISE
■ Replace [Customer Name] on every slide (20+ instances)
■ Update all financial figures from your TCO model
■ Populate the scoring matrix with your engagement's weighted scores
■ Confirm recommendation slide (Slide 13) comes AFTER evidence slides 8–12
■ Update the partner funding slide with actual AMM/MAP/PSO eligibility
```

#### `cra-phase1-report-template.docx` (cover slide equivalent for PPTX)
→ Use the DOCX header block spec below (10.6)

#### `cloud-strategy-generic.pptx`

```
Template Name:  Cloud Strategy Overview
Phase:          Pre-Sales / Executive Briefing (before Phase 1)

PURPOSE
A pre-sales executive overview of cloud migration strategy for customers who are evaluating
whether to start a cloud readiness assessment. Use this to set context before presenting
the CRA framework to a new customer or stakeholder.

AUDIENCE: Customer VP/CIO (pre-sales) + Rackspace Pre-Sales Architect
WHEN TO USE: Pre-sales discovery call or executive briefing; before CRA SOW is signed
VERSION: v1.0

WHAT TO CUSTOMISE
■ Add customer logo to title slide
■ Adjust industry vertical examples to match customer sector
■ Update market benchmark statistics to current year
```

#### `azure-calculator-walkthrough.pptx`

```
Template Name:  Azure Pricing Calculator Walkthrough
Phase:          Phase 3: TCO Validation

PURPOSE
Step-by-step guide for validating Azure pricing using the Azure Pricing Calculator and
Azure Migrate pricing tool. Use this to verify that TCO model prices match current
Azure published rates and to explain the pricing methodology to the customer.

AUDIENCE: Rackspace Platform Architect (Azure)
WHEN TO USE: Phase 3, during TCO model validation (see TCO-TEMPLATES-AUDIT-SPEC.md 4B.9)
VERSION: v1.0

WHAT TO CUSTOMISE
■ Update pricing screenshots to current Azure pricing (valid for 90 days from last update)
■ Confirm region selected matches customer requirements
■ Update AHB eligibility count from your engagement's infrastructure-profiling.xlsx
```

---

## Epic 10.6 — Header Block Spec for DOCX Templates

Add a standard header block at the top of every CRA Word template, immediately after the cover page and before the Table of Contents.

### Standard Header Block Layout

The header block is a grey-shaded table (no borders, light grey fill #F2F2F2) with the following structure:

```
┌─────────────────────────────────────────────────────────────────────────┐
│  DOCUMENT INFORMATION                                                    │
├──────────────────────┬──────────────────────────────────────────────────┤
│  Document Purpose:   │  [What this document is for and who reads it]    │
│  CRA Phase:          │  Phase [X]: [Phase Name]                         │
│  Target Audience:    │  [Customer CTO + Rackspace Lead Architect, etc.] │
│  When to Complete:   │  [Phase X weeks Y–Z; dependency on prior phase]  │
│  Est. Time to Fill:  │  [X–Y hours to complete; X–Y pages when complete]│
│  Template Version:   │  v[X.X] — last updated [DATE]                    │
├──────────────────────┴──────────────────────────────────────────────────┤
│  WHAT TO CUSTOMISE                                                       │
│  ■ Placeholder 1: [Specific instruction]                                │
│  ■ Placeholder 2: [Specific instruction]                                │
│  ■ Placeholder 3: [Specific instruction]                                │
├──────────────────────────────────────────────────────────────────────────│
│  ⚠️ IMPORTANT: [Key requirement or warning, e.g., "The Recommendation    │
│  section must come AFTER the TCO and scoring sections — never before."] │
└─────────────────────────────────────────────────────────────────────────┘
```

The Important row (yellow highlight, ⚠️ prefix) should only be included if there is a genuine risk of misuse. Do not add a warning for every template.

### Per-Template Header Block Content

#### `cra-assessment-report-template-v3.docx`

```
Document Purpose:   The primary written deliverable of the CRA engagement. Delivered to
                    the customer CTO/CIO at Phase 3 completion. Must be board-quality.
CRA Phase:          Phase 3: Hyperscaler Evaluation → Customer Deliverable
Target Audience:    Customer CTO, CIO, IT Director + Rackspace Delivery Team
When to Complete:   Phase 3 weeks 2–3; final review in Phase 4 before Part 2 SOW
Est. Time to Fill:  16–24 hours (spread across Phases 2–3); 40–60 pages when complete
Template Version:   v3.0

WHAT TO CUSTOMISE
■ Replace all [Customer Name] placeholders (30+ instances throughout document)
■ Replace all financial figures with your engagement's TCO model outputs
■ Section 15 (Recommendation): confirm it comes AFTER sections 10–14
■ Update the partner funding table (Section 13) with your AMM/MAP/PSO actuals
■ Remove any sections marked [IF APPLICABLE] that don't apply (e.g., Oracle section if no Oracle)

⚠️ IMPORTANT: The Recommendation section must appear AFTER the TCO Analysis,
Licensing Overlay, Partner Funding, and Hyperscaler Scoring sections. A recommendation
that precedes the evidence will be perceived as pre-determined. See docs/DMG-MEDIA-UK-LESSONS-LEARNED.md Lesson 9.
```

#### `cra-phase1-report-template.docx`

```
Document Purpose:   Phase 1 delivery report documenting the infrastructure discovery
                    findings, application inventory, and data quality summary.
CRA Phase:          Phase 1: Discovery → End-of-Phase Deliverable
Target Audience:    Customer IT Director + Rackspace Lead Architect
When to Complete:   Phase 1 Week 6–7 (final week); presented at Phase 1 exit gate meeting
Est. Time to Fill:  8–12 hours; 20–30 pages when complete
Template Version:   v2.0

WHAT TO CUSTOMISE
■ Replace [Customer Name] and [Date] on cover page
■ Update infrastructure summary table from infrastructure-profiling.xlsx Data Quality tab
■ Update application inventory summary from application-scoping-profiling.xlsx Summary tab
■ Fill in the Utilisation Data Quality section with actual collection period and coverage %
■ Flag any Oracle or EoL OS findings in the Key Findings section
```

#### `part2-entry-point-template.docx` (when built from CONTENT.md)

```
Document Purpose:   The commercial handoff document that initiates the Part 2 migration
                    engagement. Contains: Part 2 scope, timeline, investment, and next steps.
                    The customer signs this at the Phase 4 playback meeting.
CRA Phase:          Phase 4: Planning → Part 2 Handoff
Target Audience:    Customer CTO/CFO (for signature) + Rackspace Pre-Sales (for pricing)
When to Complete:   Phase 4 weeks 3–5; present at Phase 4 playback and leave for signature
Est. Time to Fill:  6–8 hours (much of content comes from Phase 3 outputs); 8–12 pages
Template Version:   v1.0

WHAT TO CUSTOMISE
■ Section 3 (Hyperscaler Recommendation): copy from Phase 3 report; do not re-derive
■ Section 4 (TCO Summary): reference Phase 3 TCO model; use 3-year net figure
■ Section 5 (Partner Funding): confirm AMM/MAP/PSO registration status with Alliance Manager
■ Section 10 (Investment): obtain pricing from Pre-Sales; do not estimate without approval

⚠️ IMPORTANT: AMM/MAP/PSO deal registration must be COMPLETE before Rackspace
countersigns this document. Check with the Alliance Manager before preparing Section 5.
See docs/DMG-MEDIA-UK-LESSONS-LEARNED.md Lesson 5.
```

#### `sow-template.docx`

```
Document Purpose:   Statement of Work for CRA Part 1 engagement. Signed by customer and
                    Rackspace before Phase 1 begins. Defines scope, deliverables, fees, timeline.
CRA Phase:          Pre-Engagement → Phase 1 Gate
Target Audience:    Customer commercial/legal team + Rackspace Pre-Sales and Legal
When to Complete:   Before Phase 1 kickoff; minimum 5 business days before start date
Est. Time to Fill:  3–5 hours (customisation); must be reviewed by Pre-Sales Director
Template Version:   v1.0

WHAT TO CUSTOMISE
■ Section 2–3 (Scope): replace estimated VM/application count with customer-provided figures
■ Section 5 (Scope Variance Clause): confirm the 15% threshold is in the final document
■ Section 8 (Utilisation Gate): confirm minimum data collection period is specified
■ Section 10 (Fees): Pre-Sales Director must approve all fee figures before circulation
■ Section 12 (Alliance Partner): confirm AMM/MAP/PSO registration clause is present

⚠️ IMPORTANT: Three critical clauses must be present before this SOW is sent for signature:
(1) Scope Variance clause — protects Rackspace if CMDB data is wrong
(2) Utilisation Data Gate clause — protects Phase 3 data quality
(3) Alliance Partner Registration clause — ensures AMM/MAP/PSO is registered on time
See Templates/executive-reporting/REPORTING-TEMPLATES-AUDIT-SPEC.md Section 4D.5.
```

#### `governance-workshop-schedule.docx`

```
Document Purpose:   Workshop schedule for the cloud governance foundations alignment
                    session with the customer's IT Director (Phase 2).
CRA Phase:          Phase 2: Analysis
Target Audience:    Customer IT Director + Rackspace Lead Architect
When to Complete:   Phase 2 Week 1; book the session in Phase 1 Week 6
Est. Time to Fill:  1–2 hours to customise agenda; workshop itself is 2–3 hours
Template Version:   v1.0

WHAT TO CUSTOMISE
■ Add customer name and contact names
■ Adjust domain weighting based on customer sector (e.g., heavier Compliance for FCA/healthcare)
■ Add any sector-specific governance domains (e.g., PCI for payments; HIPAA for healthcare)
```

---

## PPTX Slide Notes Standards (applies to all PPTX templates)

Every slide in every CRA PowerPoint template must have speaker notes. The notes make the template usable by any architect, not just the one who built it.

### Speaker Notes Standard Format

```
[What this slide shows]
1-2 sentences describing what the data/charts on this slide communicate.

[What to say]
2–4 bullet points: key messages to land with the audience.

[Customise before presenting]
■ [Specific change 1 — e.g., "Update the TCO saving % from your model"]
■ [Specific change 2]

[Common questions]
Q: [Likely audience question]
A: [Suggested answer]
```

### Minimum Notes Length by Slide Type

| Slide Type | Minimum Notes |
| --- | --- |
| Data/chart slide | 3–5 sentences + what to say + what to customise |
| Recommendation slide | 6–8 sentences + talking points + common objections |
| Cover/agenda/divider | 1–2 sentences (context setter) |
| Appendix | "Appendix — show only if the audience asks for detail on [topic]" |

---

## Filename Standards for Templates

All templates must follow this naming convention:

```
[phase-prefix]-[descriptive-name]-[type].[ext]
```

Examples:
- `01-discovery-application-scoping.xlsx` ✅
- `03-evaluation-tco-business-case.xlsx` ✅
- `exec-cra-executive-summary-v3.pptx` ✅
- `Application Scoping Template FINAL v2 USE THIS ONE.xlsx` ❌
- `TCO NEW.xlsx` ❌

**Phase prefixes:**
- `01-discovery-` → Phase 1 Discovery templates
- `02-analysis-` → Phase 2 Analysis templates
- `03-evaluation-` → Phase 3 Evaluation/TCO templates
- `04-planning-` → Phase 4 Planning templates
- `exec-` → Executive Reporting templates (not phase-specific)

---

*CRA Framework v2.0 — Template Design Standards — Rackspace Cloud Solutions Architecture*
