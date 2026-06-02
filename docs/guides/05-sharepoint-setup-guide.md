# CRA SharePoint Site — Setup & Content Guide

**Who should read this:** Rackspace delivery managers or practice leads setting up the internal CRA SharePoint site for the first time.  
**What this guide covers:** SharePoint site architecture, page structure, document library setup, permissions model, and content to populate on each page.  
**What comes before and after:** Set up SharePoint after the GitHub repo is stable (Release 1.0). SharePoint is the internal delivery tool; GitHub is the external/partner-facing tool. They serve different audiences.  
**Time to read this guide:** 20–25 minutes

> **Epic 9.2 — Internal SharePoint Site**  
> This guide enables Rackspace delivery teams to set up the CRA SharePoint site. The SharePoint site hosts the complete internal template library (including versions with real customer data), internal enablement materials, and the delivery team workspace.

---

## Why SharePoint (Not Just GitHub)

| Capability | GitHub Repo | SharePoint Site |
| --- | --- | --- |
| External sharing with customers / partners | ✅ Yes (public repo) | ❌ No |
| Internal Rackspace access | ✅ Yes (with link) | ✅ Yes (via SSO) |
| Store customer-confidential files | ❌ No (even private GitHub has risk) | ✅ Yes (M365 DLP protection) |
| Co-authoring in Office (Word/Excel/PPT) | ❌ No | ✅ Yes — real-time co-edit |
| SharePoint Copilot integration | ❌ No | ✅ Yes — M365 Copilot can summarise |
| Teams channel integration | ❌ No | ✅ Yes |
| Customer delivery workspace | ❌ No | ✅ Yes — per-engagement folders |

**Use GitHub for:** Framework methodology, generic templates, case studies, partner decks — things that benefit from public visibility.  
**Use SharePoint for:** Active engagement files, customer-specific data, internal pricing, delivery team workspaces.

---

## Part 1 — SharePoint Site Architecture

### Recommended Site Structure

```
CRA Framework — Rackspace Cloud Solutions Architecture
│
├── 🏠 Home Page
│   ├── What is CRA? (3-sentence intro)
│   ├── Quick Links: Start Here → Phase Guides → Templates → Case Studies
│   └── Recent Updates (news web part)
│
├── 📋 Framework Overview
│   ├── Four-Phase Methodology (embedded diagram)
│   ├── SMART vs CRA Decision Guide
│   └── Phase Duration Reference
│
├── 📁 Template Library (Document Library)
│   ├── 01-Discovery/
│   ├── 02-Analysis/
│   ├── 03-Evaluation/
│   ├── 04-Planning/
│   └── Executive-Reporting/
│
├── 📚 Phase Guides
│   ├── 00 - Architect Onboarding (30 min)
│   ├── 01 - Discovery Phase Guide
│   ├── 02 - Analysis Phase Guide
│   ├── 03 - Evaluation Phase Guide
│   └── 04 - Planning Phase Guide
│
├── 📊 Case Studies
│   ├── DMG Media UK (internal version — full data)
│   └── [Future engagements]
│
├── 🤝 Alliance Partners
│   ├── Microsoft: CAF Alignment + AMM Guide
│   ├── AWS: MAP Alignment + MAP Guide
│   └── GCP: PSO Alignment + RAMP Guide
│
├── 🏗️ Active Engagements (Document Library)
│   ├── [Customer Name — Year]/
│   │   ├── Phase 1 - Discovery/
│   │   ├── Phase 2 - Analysis/
│   │   ├── Phase 3 - Evaluation/
│   │   ├── Phase 4 - Planning/
│   │   └── Deliverables - Final/
│   └── [Next Customer]/
│
└── ⚙️ Internal Resources
    ├── Lessons Learned
    ├── Pricing Reference (internal — not on GitHub)
    └── Architect Directory
```

---

## Part 2 — Setting Up the SharePoint Site

### Step 1 — Create the SharePoint Site

1. Go to [M365 Admin Center](https://admin.microsoft.com) or request via IT
2. Create a **Team Site** (not Communication Site) — Team Site allows document co-authoring and Teams integration
3. Site name: `CRA Framework — Cloud Solutions Architecture`
4. Site URL: `/sites/cra-framework` (or as allocated by your tenant admin)
5. Privacy: **Private** — invitation only
6. Owner: Practice Lead (you) + backup owner (Delivery Manager)

### Step 2 — Set Up Permissions Groups

| Group | Members | Permissions |
| --- | --- | --- |
| CRA Owners | Practice Lead, Senior Architects | Full control |
| CRA Members | All CRA delivery architects | Edit |
| CRA Visitors | Pre-Sales, Leadership, Alliance Managers | Read |
| Per-Engagement Group | Engagement team only | Edit (for that engagement folder only) |

> **Important:** Customer-specific folders in Active Engagements must use item-level permissions — only the engagement team should have access. Do not give all CRA Members access to every customer folder.

### Step 3 — Create the Document Libraries

Create two document libraries:

**Library 1: Template Library**
- Name: `CRA Template Library`
- Enable versioning: Yes (major versions, keep last 10)
- Require checkout: No
- Metadata columns to add:
  - `CRA Phase` (Choice: Phase 1 Discovery / Phase 2 Analysis / Phase 3 Evaluation / Phase 4 Planning / Executive Reporting)
  - `File Type` (Choice: Excel / Word / PowerPoint / PDF / Markdown)
  - `Template Version` (Text)
  - `Last Validated` (Date — when pricing/content was last verified)

**Library 2: Active Engagements**
- Name: `CRA Engagements`
- Create a folder per engagement: `[Customer Name] — [Year]`
- Metadata columns:
  - `Customer Name` (Text)
  - `Primary Hyperscaler` (Choice: Azure / AWS / GCP / TBD)
  - `Engagement Stage` (Choice: Phase 1 / Phase 2 / Phase 3 / Phase 4 / Complete)
  - `Lead Architect` (Person)
  - `Start Date` (Date)

### Step 4 — Populate the Template Library

Upload all files from the GitHub repo `Templates/` folder. Map to SharePoint folders:

| GitHub Path | SharePoint Folder | Tag: CRA Phase |
| --- | --- | --- |
| `Templates/01-discovery/` | `Template Library/01-Discovery/` | Phase 1 Discovery |
| `Templates/02-analysis/` | `Template Library/02-Analysis/` | Phase 2 Analysis |
| `Templates/03-evaluation/` | `Template Library/03-Evaluation/` | Phase 3 Evaluation |
| `Templates/04-planning/` | `Template Library/04-Planning/` | Phase 4 Planning |
| `Templates/executive-reporting/` | `Template Library/Executive-Reporting/` | Executive Reporting |

**After upload:** Set the `Last Validated` date on each file. Any template not validated in the last 6 months should be flagged for review (pricing changes quarterly for cloud SKUs).

### Step 5 — Add the Confidential Files (Not on GitHub)

Files that are gitignored on GitHub should be stored here:
- `Reports format example/DMG_Cloud_Readiness_Assessment_Part_1_Report_v2.0.docx` → `Case Studies/DMG Media UK/`
- `SOW/DMG Cloud Readiness Assessment Part 1 - Rebaselined.docx` → `Case Studies/DMG Media UK/`
- `Examples/Azure Example -2/` (all 4 files) → `Case Studies/DMG Media UK/`
- Any internal pricing reference files → `Internal Resources/Pricing Reference/`

### Step 6 — Create the Home Page

Add the following web parts to the SharePoint Home Page:

1. **Hero web part** — Feature image: CRA four-phase diagram; CTA button: "Start Here →"
2. **Quick Links** — 6 tiles:
   - "New to CRA? Start Here" → 00-architect-onboarding-guide
   - "Phase 1: Discovery" → 01-discovery-phase-guide
   - "Phase 3: TCO Templates" → 03-Evaluation folder
   - "DMG Media UK Case Study" → Case Studies folder
   - "Microsoft AMM Guide" → Alliance Partners/Microsoft
   - "GitHub Repo" → external link to `upendra25312/Cloud-Readiness-accelearator`
3. **News web part** — pull from a "CRA Updates" SharePoint list (post updates when templates are changed)
4. **Recent Documents** — from Template Library (filtered to files modified in last 30 days)
5. **People web part** — the CRA practice team: Lead Architect, Platform Architects

---

## Part 3 — Per-Engagement Workspace Setup

When a new CRA engagement starts, create a workspace in the Active Engagements library:

### Step-by-Step for New Engagement

1. Create folder: `[Customer Name] — [YYYY]` (e.g., `Acme Corp — 2026`)
2. Create subfolders: `Phase 1 - Discovery`, `Phase 2 - Analysis`, `Phase 3 - Evaluation`, `Phase 4 - Planning`, `Deliverables - Final`
3. Copy templates from Template Library into the engagement folder:
   - Phase 1: `application-scoping-profiling.xlsx`, `infrastructure-profiling.xlsx`, `dependency-mapping.xlsx`
   - Phase 2: `cloud-readiness-scoring-v2.xlsx`, `governance-foundations-alignment.xlsx`
   - Phase 3: `azure-evaluation.xlsx`, `aws-evaluation.xlsx`, `gcp-evaluation.xlsx`, `hyperscaler-decision-matrix.xlsx`, `business-case-tco-roi.xlsx`
   - Phase 4: `risk-assessment.xlsx`, `migration-wave-planner.xlsx`
4. Set item-level permissions: Add the engagement team members to this folder only
5. Create a Teams channel (optional): `CRA — [Customer Name]` and link to the SharePoint folder
6. In the `Deliverables - Final` folder, create blank files for each named deliverable:
   - `Phase-1-Infrastructure-Discovery-Summary.docx`
   - `Phase-3-Executive-Playback.pptx`
   - `Phase-3-TCO-Analysis.xlsx`
   - `Phase-4-Part2-Entry-Point.docx`

### Permissions for Engagement Workspace

```
Only add people who work on this engagement.
Do not share customer data folders with:
- Other engagement teams
- Pre-Sales (unless actively supporting this deal)
- Alliance managers (unless needed for AMM registration)
```

---

## Part 4 — Teams Integration

### Recommended Teams Channel Structure

Create a Teams team: `CRA Framework — Cloud Solutions Architecture`

Channels:
| Channel | Purpose |
| --- | --- |
| General | Announcements; template updates; practice news |
| Framework Development | Discussion about improving CRA methodology and templates |
| [Customer Name] | Per-engagement channel (create as private channel) |
| Alliance Partners | AMM/MAP/PSO deal status; partner team contacts |
| Lessons Learned | Post one lesson after each engagement completes |

Add a tab in each engagement channel:
- `Templates` → link to the engagement SharePoint folder
- `Phase Guide` → link to the relevant phase guide

---

## Part 5 — Keeping SharePoint and GitHub in Sync

| Event | GitHub Action | SharePoint Action |
| --- | --- | --- |
| Template updated (new columns, new tabs) | Commit to main branch; update CHANGELOG.md | Upload new version to Template Library; update `Last Validated` date |
| New phase guide written | Push to `docs/guides/` on GitHub | Link from SharePoint Phase Guides page |
| New case study added | Add to `Examples/media-entertainment/` on GitHub | Add full version (with real data) to SharePoint Case Studies |
| Pricing validated (quarterly) | Update TCO audit spec on GitHub | Update `Last Validated` column in Template Library |

---

## Part 6 — SharePoint Copilot Integration

Once the SharePoint site is populated, M365 Copilot (if licensed) can be used to:

- **Summarise a case study:** "Summarise the DMG Media UK CRA outcomes for a 2-minute verbal briefing"
- **Draft a status update:** "Draft a weekly status email based on the Phase 2 deliverables in this folder"
- **Find a template:** "Which template should I use for licensing analysis?" → points to `business-case-tco-roi.xlsx`
- **Populate a template:** "Using the data in the infrastructure-profiling worksheet, populate the TCO Summary tab"

For Copilot to work effectively:
- Files must have meaningful names (not `Template v2 FINAL FINAL.xlsx`)
- Metadata must be populated (CRA Phase, Last Validated)
- Folders must be logically organised (done — see structure above)

---

*CRA Framework v2.0 — Rackspace Cloud Solutions Architecture*  
*For GitHub public version: see [docs/guides/ on GitHub](https://github.com/upendra25312/Cloud-Readiness-accelearator/tree/main/docs/guides)*
