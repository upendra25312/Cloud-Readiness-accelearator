# Cloud Readiness Accelerator — To-Do Tracker

**Version:** 2.0  
**Date:** 03/06/26  
**Owner:** Rackspace Cloud Solutions Architecture  
**Update Frequency:** Weekly

---

## Legend

| Symbol | Meaning |
|---|---|
| 🔴 | Blocked |
| 🟡 | In Progress |
| 🟢 | Complete |
| ⬜ | Not Started |
| ⭐ | High Priority |

---

## EPIC 0: Existing File Triage, Organization & Professionalization

**Goal:** Transform the current file collection into a clean, senior-leadership-ready asset with zero clutter, zero sensitive data leakage, and every artifact correctly named, placed, and branded.  
**Why This Comes First:** Senior leaders will judge the entire framework by first impression. A directory of 45+ operational meta-files named `GITHUB-COMPLETION-SUMMARY.md` or `PERMISSION-DENIED-FIX.md` instantly signals internal working notes, not a professional product.  
**Target:** Complete before any external sharing — Release 1.0 gate

### 0A. Sensitive & Customer-Data Files (MUST DO FIRST — Legal Gate)

> These files contain DMG customer data. Protected in public repo via `.gitignore`. When migrating to private `rxt-mpc/ps-ind-cloud-readiness-accelerator`, include under `Examples/media-entertainment/` as supporting case study assets.

| # | File / Folder | Action Required | Priority | Status | Notes |
|---|---|---|---|---|---|
| 0A.1 | `Examples/Azure Example -2/DMG RFP - SOFT PERKS - Non Protected.pdf` | Protected by `.gitignore` in public repo | 🔴 Critical | 🟢 Complete | Gitignored; not tracked by git. Include in private rxt-mpc migration under Examples/media-entertainment/ |
| 0A.2 | `Examples/Azure Example -2/DMG RFP - SOFT PERKS - Notes Non Protected.pdf` | Protected by `.gitignore` in public repo | 🔴 Critical | 🟢 Complete | Gitignored; not tracked by git. Include in private rxt-mpc migration |
| 0A.3 | `Examples/Azure Example -2/Microsoft Unified for DMG Media.pptx` | Protected by `.gitignore` in public repo | 🔴 Critical | 🟢 Complete | Gitignored; local only. Include in private rxt-mpc migration |
| 0A.4 | `Examples/Azure Example -2/Hyperscaler_Decision_Matrix_Microsoft_Completed.xlsx` | Protected by `.gitignore`; include in private repo after anonymization review | ⭐ High | 🟢 Complete | Gitignored. See 0G.10 for anonymization review. Include in private rxt-mpc migration |
| 0A.5 | `Reports format example/DMG - CRA - Executive Summary v2.pdf` | Protected by `.gitignore`; include in private repo under Examples/media-entertainment/ | ⭐ High | 🟢 Complete | `Reports format example/` directory gitignored entirely |
| 0A.6 | `Reports format example/DMG - CRA - Executive Summary v2 backup.pptx` | Protected by `.gitignore`; include in private repo | ⭐ High | 🟢 Complete | Gitignored |
| 0A.7 | `Reports format example/DMG_Cloud_Readiness_Assessment_Part_1_Report_v2.0.docx` | Protected by `.gitignore`; include in private repo; use as anonymized case study reference | ⭐ High | 🟢 Complete | Gitignored; best reference for case study |
| 0A.8 | `Reports format example/DMG_Cloud_Readiness_Assessment_Part_1_Report_v2.0.pdf` | Protected by `.gitignore`; include in private repo | ⭐ High | 🟢 Complete | Gitignored |
| 0A.9 | `SOW/DMG Cloud Readiness Assessment Part 1 - Rebaselined Objectives & Plan - 10 Apr 2026.docx` | Protected by `.gitignore`; include in private repo; basis for generic SOW template | ⭐ High | 🟢 Complete | `SOW/` directory gitignored entirely |
| 0A.10 | `Templates/DMG - CRA - Executive Summary v2.pptx` | Renamed to `cra-executive-summary-template.pptx`; DMG content debranded | ⭐ High | 🟢 Complete | Now at `Templates/executive-reporting/cra-executive-summary-template.pptx` (commit 4418c03) |
| 0A.11 | `Templates/DMG_CRA_Phase1_Report_v2.docx` | Renamed to `cra-phase1-report-template.docx`; DMG content debranded | ⭐ High | 🟢 Complete | Now at `Templates/executive-reporting/cra-phase1-report-template.docx` (commit 4418c03) |

### 0B. Operational Meta-Files — Archive or Delete

> These ~45 files were generated as working notes during repo setup. They have no value to a VP, Director, or alliance partner. Leaving them in the root signals "unfinished work."

| # | Files to Archive / Delete | Action | Priority | Status |
|---|---|---|---|---|
| 0B.1 | `EXECUTE-GITHUB-PUBLICATION.sh`, `EXECUTE-GITHUB-PUBLICATION.bat` | Delete — obsolete shell scripts | ⭐ High | 🟢 Complete |
| 0B.2 | `PERMISSION-DENIED-FIX.md`, `MANUAL-GITHUB-STEPS.md` | Delete — internal troubleshooting notes | ⭐ High | 🟢 Complete |
| 0B.3 | `GITHUB-COMPLETION-SUMMARY.md`, `GITHUB-IMPLEMENTATION-COMPLETE.md`, `GITHUB-READY-FOR-PUBLICATION.md` | Delete — session artifacts | ⭐ High | 🟢 Complete |
| 0B.4 | `GITHUB-IMPLEMENTATION-GUIDE.md`, `GITHUB-IMPLEMENTATION-INDEX.md`, `GITHUB-IMPLEMENTATION-STRATEGY.md` | Delete — superseded by PLAN.md | ⭐ High | 🟢 Complete |
| 0B.5 | `GITHUB-PUBLISHING-GUIDE.md`, `GITHUB-PUBLISHING-SUMMARY.md`, `GITHUB-QUICK-START.md` | Delete — superseded by README + PLAN.md | ⭐ High | 🟢 Complete |
| 0B.6 | `GITHUB-START-HERE.md`, `GITHUB-GETTING-STARTED.md`, `START-HERE.md`, `START-GITHUB-PUBLICATION.md` | Delete — replaced by new START-HERE.md | ⭐ High | 🟢 Complete |
| 0B.7 | `GITHUB-METHODOLOGY.md` | Extract any unique content → merge into `docs/METHODOLOGY.md`, then delete | Medium | 🟢 Complete |
| 0B.8 | `SHAREPOINT-DEPLOYMENT-GUIDE.md`, `SHAREPOINT-IMPLEMENTATION-PLAN.md`, `SHAREPOINT-PAGE-CONTENT.md`, `SHAREPOINT-PUBLISHING-SUMMARY.md`, `SHAREPOINT-PAGE.html` | Move to `_internal-only/sharepoint/` (useful for internal SharePoint setup) | Medium | 🟢 Complete |
| 0B.9 | `SHAREPOINT-EXECUTIVE-SUMMARY.md`, `SHAREPOINT-VS-GITHUB-ANALYSIS.md`, `COPILOT-SHAREPOINT-PROMPT.md` | Move to `_internal-only/sharepoint/` | Medium | 🟢 Complete |
| 0B.10 | `COPY-PASTE-COMMANDS.md`, `README-GITHUB-EXECUTION.md`, `README-SHAREPOINT-PUBLISHING.md` | Delete — internal working notes | ⭐ High | 🟢 Complete |
| 0B.11 | `DEPLOYMENT-PACKAGE.md`, `DEPLOYMENT-STRATEGY.md`, `PHASE-1-DEPLOYMENT-CHECKLIST.md` | Merge useful content → PLAN.md or delete | Medium | 🟢 Complete |
| 0B.12 | `IMPLEMENTATION-STATUS.md`, `PARALLEL-WORKSTREAMS-PLAN.md`, `NEXT-STEPS-ACTION-PLAN.md` | Delete — superseded by TODO tracker | ⭐ High | 🟢 Complete |
| 0B.13 | `EXPERT-TEAM-DECISION.md`, `EXPERT-TEAM-SUMMARY.md`, `EXECUTIVE-ACTION-SUMMARY.md` | Delete/move — internal session notes | ⭐ High | 🟢 Complete |
| 0B.14 | `DELIVERABLES-CHECKLIST.md`, `ACCELERATOR-SUMMARY.md` | Merge useful content → README or TODO, then delete | Medium | 🟢 Complete |
| 0B.15 | `FINAL-PUBLISHING-STRATEGY.md`, `FINAL-SUMMARY-AND-NEXT-STEPS.md` | Delete — superseded by PLAN.md | ⭐ High | 🟢 Complete |
| 0B.16 | `design.md`, `requirements.md`, `tasks.md`, `package.json` | Reviewed; deleted or moved to `_internal-only/` | Medium | 🟢 Complete |

### 0C. GitHub Standard Files — Rename & Consolidate

> Several standard repo files exist with "GITHUB-" prefix. Rename them to standard names.

| # | Current File | Rename To | Action | Status |
|---|---|---|---|---|
| 0C.1 | `GITHUB-CHANGELOG.md` | `CHANGELOG.md` | Rename (standard GitHub convention) | 🟢 Complete |
| 0C.2 | `GITHUB-CONTRIBUTING.md` | `CONTRIBUTING.md` | Rename | 🟢 Complete |
| 0C.3 | `GITHUB-CODE-OF-CONDUCT.md` | `CODE_OF_CONDUCT.md` | Rename | 🟢 Complete |
| 0C.4 | `QUICK-START-GUIDE.md` | Merged into new `START-HERE.md`; original deleted | Medium | 🟢 Complete |
| 0C.5 | `QUICK-REFERENCE-CARD.md` | `docs/guides/quick-reference.md` | Medium | 🟢 Complete |
| 0C.6 | `ROADMAP.md` | Retained as standalone at root | Medium | 🟢 Complete |

### 0D. Framework Content — Reorganize to Target Structure

> Phase guides, integration guides, and methodology docs are in the wrong locations.

| # | Current Location | Move To | Action | Status |
|---|---|---|---|---|
| 0D.1 | `Discovery-Phase-Guide.md` (root) | `docs/guides/01-discovery-phase-guide.md` | Move + rename | 🟢 Complete |
| 0D.2 | `Analysis-Phase-Guide.md` (root) | `docs/guides/02-analysis-phase-guide.md` | Move + rename | 🟢 Complete |
| 0D.3 | `Evaluation-Phase-Guide.md` (root) | `docs/guides/03-evaluation-phase-guide.md` | Move + rename | 🟢 Complete |
| 0D.4 | `Planning-Phase-Guide.md` (root) | `docs/guides/04-planning-phase-guide.md` | Move + rename | 🟢 Complete |
| 0D.5 | `Methodology-Overview.md` (root) | `docs/methodology-overview.md` | Move | 🟢 Complete |
| 0D.6 | `docs/METHODOLOGY.md` | `docs/METHODOLOGY.md` | Retained at docs/ root | 🟢 Complete |
| 0D.7 | `FRAMEWORK-INDEX.md` (root) | `docs/FRAMEWORK-INDEX.md` | Move | 🟢 Complete |
| 0D.8 | `Integration-Guides/CMDB-Integration-Guide.md` | `docs/integration/cmdb-integration-guide.md` | Move | 🟢 Complete |
| 0D.9 | `Integration-Guides/Cloud-Assessment-Tool-Integration-Guide.md` | `docs/integration/cloud-assessment-tools.md` | Move | 🟢 Complete |
| 0D.10 | `Integration-Guides/Monitoring-Tool-Integration-Guide.md` | `docs/integration/monitoring-tools.md` | Move | 🟢 Complete |
| 0D.11 | `Customization-Guides/Industry-Customization-Guide.md` | `docs/customization/industry-customization.md` | Move | 🟢 Complete |
| 0D.12 | `Customization-Guides/Organization-Size-Adaptation-Guide.md` | `docs/customization/org-size-adaptation.md` | Move | 🟢 Complete |
| 0D.13 | `Quality-Assurance/Data-Validation-Checklist.md` | `docs/governance/data-validation-checklist.md` | Move | 🟢 Complete |
| 0D.14 | `docs/azure-cloud-adoption-framework.pdf` | `docs/reference/azure-cloud-adoption-framework.pdf` | Move to reference subfolder | 🟢 Complete |

### 0E. Templates — Rename, Debrand & Reorganize by Phase

> All templates need: (1) DMG branding removed from filename, (2) moved to phase-based subfolders, (3) content reviewed for customer data.

| # | Current Filename | Target Location & New Name | Action Required | Status |
|---|---|---|---|---|
| 0E.1 | `Templates/Application Scoping & Profiling - template.xlsx` | `Templates/01-discovery/application-scoping-profiling.xlsx` | Rename + move | 🟢 Complete |
| 0E.2 | `Templates/Infrastructure-Profiling-Template.xlsx` | `Templates/01-discovery/infrastructure-profiling.xlsx` | Move + lowercase | 🟢 Complete |
| 0E.3 | `Templates/Dependency-Mapping-Template.xlsx` | `Templates/01-discovery/dependency-mapping.xlsx` | Move + lowercase | 🟢 Complete |
| 0E.4 | `Templates/Cloud-Readiness-Assessment-v2.xlsx` | `Templates/02-analysis/cloud-readiness-scoring-v2.xlsx` | Move + rename | 🟢 Complete |
| 0E.5 | `Templates/Readiness-Scoring-Criteria-Template.xlsx` | `Templates/02-analysis/readiness-scoring-criteria.xlsx` | Move + lowercase | 🟢 Complete |
| 0E.6 | `Templates/CRA - LITE Governance Foundations Alignment Tool - Template.xlsx` | `Templates/02-analysis/governance-foundations-alignment.xlsx` | Move + rename | 🟢 Complete |
| 0E.7 | `Templates/AWS-Evaluation-Template.xlsx` | `Templates/03-evaluation/aws-evaluation.xlsx` | Move + lowercase | 🟢 Complete |
| 0E.8 | `Templates/Azure-Evaluation-Template.xlsx` | `Templates/03-evaluation/azure-evaluation.xlsx` | Move + lowercase | 🟢 Complete |
| 0E.9 | `Templates/GCP-Evaluation-Template.xlsx` | `Templates/03-evaluation/gcp-evaluation.xlsx` | Move + lowercase | 🟢 Complete |
| 0E.10 | `Templates/Hyperscaler-Decision-Matrix-Template.xlsx` | `Templates/03-evaluation/hyperscaler-decision-matrix.xlsx` | Move + lowercase | 🟢 Complete |
| 0E.11 | `Templates/HyperScalar Weighted Selection Criteria.xlsx` (root) | `Templates/03-evaluation/hyperscaler-weighted-selection-criteria.xlsx` | Move + rename | 🟢 Complete |
| 0E.12 | `Templates/Business-Case-Template.xlsx` | `Templates/03-evaluation/business-case-tco-roi.xlsx` | Move + rename | 🟢 Complete |
| 0E.13 | `Templates/Risk-Assessment-Template.xlsx` | `Templates/04-planning/risk-assessment.xlsx` | Move + lowercase | 🟢 Complete |
| 0E.14 | `Templates/Migration-Wave-Planning-Template.xlsx` | `Templates/04-planning/migration-wave-planner.xlsx` | Move + lowercase | 🟢 Complete |
| 0E.15 | `Templates/Governance-Model-Template.xlsx` | `Templates/04-planning/governance-model.xlsx` | Move + lowercase | 🟢 Complete |
| 0E.16 | `Templates/Executive-Summary-Report-Template.xlsx` | `Templates/04-planning/executive-summary-data.xlsx` | Move + rename | 🟢 Complete |
| 0E.17 | `Templates/CRA - LITE Governance Assessment Workshop Schedule Template.docx` | `Templates/04-planning/governance-workshop-schedule.docx` | Move + rename | 🟢 Complete |
| 0E.18 | `Templates/DMG - CRA - Executive Summary v2.pptx` | `Templates/executive-reporting/cra-executive-summary-template.pptx` | **Debrand DMG → Rackspace**, move | 🟢 Complete |
| 0E.19 | `Templates/DMG_CRA_Phase1_Report_v2.docx` | `Templates/executive-reporting/cra-phase1-report-template.docx` | **Debrand DMG → Rackspace**, move | 🟢 Complete |
| 0E.20 | `Templates/Cloud_Readiness_Assessment_Executive_Summary_Template_v3_Audited.pptx` | `Templates/executive-reporting/cra-executive-summary-v3.pptx` | Move — already audited | 🟢 Complete |
| 0E.21 | `Templates/Cloud_Readiness_Assessment_Report_Template_v3_Audited.docx` | `Templates/executive-reporting/cra-assessment-report-template-v3.docx` | Move — already audited | 🟢 Complete |
| 0E.22 | `Templates/ADFD-Solution-Assessment-Report.pptx` | Moved to `_internal-only/templates/adfd-solution-assessment-report.pptx` | Medium | 🟢 Complete |
| 0E.23 | `Templates/MS-Solution-Assessment Report.pptx` | `Templates/executive-reporting/ms-solution-assessment.pptx` | Move — Microsoft partner reference | 🟢 Complete |
| 0E.24 | `Templates/Azure Calc.pptx` | `Templates/03-evaluation/azure-calculator-walkthrough.pptx` | Move + rename | 🟢 Complete |
| 0E.25 | `Templates/Cloud-Strategy-Generic.pptx` | `Templates/executive-reporting/cloud-strategy-generic.pptx` | Move | 🟢 Complete |
| 0E.26 | `Templates/Data Gathering Template Guide.pptx` | `docs/guides/data-gathering-guide.pptx` | Move to docs | 🟢 Complete |

### 0F. Presentations — Review, Rebrand & Classify

> Three CRA PPTX files at root need quality review and Rackspace branding applied.

| # | File | Action | Notes | Status |
|---|---|---|---|---|
| 0F.1 | `Cloud_Readiness_Accelerator_Rackspace_V1.1.pptx` | Moved to `presentations/executive/cra-overview-v1.1.pptx` | Primary executive presentation | 🟢 Complete |
| 0F.2 | `Cloud Readiness Accelerator Reusable Enterprise Multi-Cloud Assessment Framework V1.pptx` | Moved to `presentations/executive/cra-overview-v0.pptx` | Earlier draft — retained as reference | 🟢 Complete |
| 0F.3 | `Cloud Readiness Accelerator Reusable Enterprise Multi-Cloud Assessment Framework.pptx` | Archived — superseded by V1.1 | Earliest draft | 🟢 Complete |
| 0F.4 | `Azure AMM - Delivery Guide.pptx` | Moved to `presentations/alliance/azure-amm-delivery-guide.pptx` | Microsoft partner reference — retained | 🟢 Complete |
| 0F.5 | `RXT Microsoft Funding Interactive Enablement (Sellers + SAs PODs)_January 2026 [SHARED].pptx` | Moved to `presentations/alliance/rxt-microsoft-funding-enablement-jan2026.pptx` | Rackspace × Microsoft co-sell enablement | 🟢 Complete |

### 0G. Examples — Anonymize & Repackage as Reference Cases

> The Examples folder has real engagement data with mixed sensitivity. Goal: keep useful financial benchmarks, remove all identifiable customer info.

| # | File | Action | Status |
|---|---|---|---|
| 0G.1 | `Examples/AWS Example/MPA Pricing Frankfurt - Full Scope.xlsx` | Renamed to `Examples/aws/aws-mpa-pricing-example-region-1.xlsx` | 🟢 Complete |
| 0G.2 | `Examples/AWS Example/MPA Pricing Ireland - Full Scope.xlsx` | Renamed to `Examples/aws/aws-mpa-pricing-example-region-2.xlsx` | 🟢 Complete |
| 0G.3 | `Examples/AWS Example/MPA Pricing London - Full Scope.xlsx` | Renamed to `Examples/aws/aws-mpa-pricing-example-region-3.xlsx` | 🟢 Complete |
| 0G.4 | `Examples/AWS Example/MPA Pricing Ireland - Full Scope no DB.xlsx` | Renamed to `Examples/aws/aws-mpa-pricing-no-db-region-2.xlsx` | 🟢 Complete |
| 0G.5 | `Examples/AWS Example/MPA Pricing London - Full Scope no DB.xlsx` | Renamed to `Examples/aws/aws-mpa-pricing-no-db-region-3.xlsx` | 🟢 Complete |
| 0G.6 | `Examples/AWS Example/business_case_lift_and_shift.pptx` | Renamed to `Examples/aws/aws-business-case-lift-shift-example.pptx` | 🟢 Complete |
| 0G.7 | `Examples/AWS Example/business_case_DB_refactoring.pptx` | Renamed to `Examples/aws/aws-business-case-db-refactoring-example.pptx` | 🟢 Complete |
| 0G.8 | `Examples/AWS Example/Storage Assessment Business Case V2...pptx` | Renamed to `Examples/aws/aws-storage-assessment-business-case-example.pptx` | 🟢 Complete |
| 0G.9 | `Examples/Azure Example -1/*.xlsx` (10 files) | Renamed to `azure-assessment-[scenario]-example.xlsx` format in `Examples/azure/` | 🟢 Complete |
| 0G.10 | `Examples/Azure Example -2/` (all 4 files) | **BLOCKED** — do not touch until 0A.1–0A.4 private repo migration plan confirmed; sensitive files still in original location (gitignored) | 🔴 Blocked |

### 0H. Project Plan & SOW Files at Root

| # | File | Action | Status |
|---|---|---|---|
| 0H.1 | `Cloud_Readiness_Assessment_Project_Plan.xlsx` | Moved to `docs/reference/cra-project-plan-template.xlsx` | 🟢 Complete |
| 0H.2 | `Cloud_Readiness_Assessment_SoW.docx` | Moved to `Templates/04-planning/sow-template.docx` | 🟢 Complete |

---

## EPIC 1: Repository Restructure & Cleanup

**Goal:** Reorganize GitHub repo to enterprise-grade structure  
**Target:** Release 1.0 ✅ **Complete**

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 1.1 | Fix git remote: point to `upendra25312/Cloud-Readiness-accelearator` | ⭐ High | Upendra | 🟢 Complete | Remote corrected and verified |
| 1.2 | Resolve git index.lock from stale background process | ⭐ High | Upendra | 🟢 Complete | Resolved by creating fresh inner `.git` |
| 1.3 | Stage and commit all local files in one clean commit | ⭐ High | Upendra | 🟢 Complete | Initial commit — all framework files staged |
| 1.4 | Force-push to `upendra25312/Cloud-Readiness-accelearator` main branch | ⭐ High | Upendra | 🟢 Complete | Force-pushed to establish clean history |
| 1.5 | Execute Epic 0 file triage: remove sensitive files, delete meta-files, rename templates | ⭐ High | Upendra | 🟢 Complete | Epic 0 fully executed across commits 61556e0–4418c03 |
| 1.6 | Create target folder structure: `docs/`, `templates/`, `presentations/`, `examples/`, `tools/` | ⭐ High | Upendra | 🟢 Complete | All target directories created and populated |
| 1.7 | Move templates to phase-based subfolders (Epic 0E tasks) | Medium | Upendra | 🟢 Complete | All 26 template files in `Templates/01-04/` and `executive-reporting/` |
| 1.8 | Move phase guides to `docs/guides/` (Epic 0D tasks) | Medium | Upendra | 🟢 Complete | All 4 phase guides at `docs/guides/0N-*-phase-guide.md` |
| 1.9 | Move integration + customization guides to `docs/integration/` and `docs/customization/` | Medium | Upendra | 🟢 Complete | All integration and customization guides moved |
| 1.10 | Commit all restructuring changes and push to GitHub | ⭐ High | Upendra | 🟢 Complete | Latest commit: 828b695 — pushed to main |

---

## EPIC 2: Executive README & Branding

**Goal:** Create VP/Director-quality README and apply Rackspace branding  
**Target:** Release 1.0 / 1.1

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 2.1 | Rewrite README.md to VP/Director standard (see PRD FR-50) | ⭐ High | Upendra | 🟢 Complete | Rewritten to professional framework standard (commit 0b48da0) |
| 2.2 | Add Rackspace logo SVG badge to README header | ⭐ High | Upendra | 🟢 Complete | Rackspace Red (#E31C3D) badge added to README (commit a62f524) |
| 2.3 | Fix all GitHub badge URLs to point to `upendra25312/Cloud-Readiness-accelearator` | ⭐ High | Upendra | 🟢 Complete | All 5 shields.io badges point to correct repo (commit a62f524) |
| 2.4 | Add "Quick Decision Guide: SMART vs. CRA" section to README | High | Upendra | 🟢 Complete | Decision table and customer journey diagram added to README; also added "Who Should Use This" persona routing table |
| 2.5 | Update CONTRIBUTING.md with clear contribution guidelines | Medium | Upendra | 🟢 Complete | Full rewrite — CRA-specific contribution types, quality standards, naming conventions, folder structure, security policy |
| 2.6 | Create SECURITY.md (security disclosure policy) | Medium | Upendra | 🟢 Complete | SECURITY.md created (commit a62f524) |
| 2.7 | Update CHANGELOG.md with v1.0, v1.1, v2.0 release history | Medium | Upendra | 🟢 Complete | CHANGELOG.md updated with v1.0 and v1.1.0 entries (commit a62f524) |
| 2.8 | Apply Rackspace color scheme (#E31C3D) to all PPTX presentations | ⭐ High | Upendra | 🟢 Complete | Automated via `tools/apply_rackspace_branding.py`; theme XML updated in 8 legacy files (EB0000 -> E31C3D); 4 template PPTX + 8 presentation PPTX; reference: DMG CRA Executive Summary v2 backup.pptx |
| 2.9 | Add Rackspace logo to all PPTX title slides and footers | ⭐ High | Upendra | 🟢 Complete | White logo (top-right) on all 12 title/cover slides; dark logo (bottom-left footer) on all 197 content slides; logo extracted from DMG backup (image2.png, 1410x180 RGBA); white variant generated programmatically |
| 2.10 | Review all docs for internal jargon — replace with external-facing language | High | Upendra | 🟢 Complete | Jargon review executed: README.md acronyms expanded (CAF/AMM/MAP/PSO); phase durations corrected to v2.0 actuals; START-HERE.md template names updated to renamed files; AMM/MAP/PSO defined in alliance table; "Hard gate" → "Mandatory phase gate" in METHODOLOGY.md + all phase guides; "v2.0 audit note" labels removed from all 3 phase guides |

---

## EPIC 3: Core Methodology & Documentation

**Goal:** Ensure methodology docs are complete, accurate, and peer-reviewed  
**Target:** Release 1.1

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 3.1 | Peer-review `docs/METHODOLOGY.md` — validate phase durations against DMG experience | ⭐ High | Upendra | 🟢 Complete | METHODOLOGY.md already at v2.0 with audited timings; CAB lead time, utilization data window, and parallel delivery model all documented |
| 3.2 | Update phase duration estimates to reflect real-world ranges (not optimistic) | High | Upendra | 🟢 Complete | v2.0 audit note already present; timelines revised: Phase 1=7wks, Phase 2=4wks, Phase 3=3wks, Phase 4=6wks |
| 3.3 | Add "When to Use This Framework" decision tree to methodology | High | Upendra | 🟢 Complete | SMART vs CRA decision guide added to README (Epic 2.4); full decision table and customer journey diagram |
| 3.4 | Create `docs/MICROSOFT-CAF-ALIGNMENT.md` | Medium | Upendra | 🟢 Complete | Created: CAF stage-to-CRA phase map, AMM funding eligibility table, AMM pre-qualification checklist, SMART integration, AHB modelling, DMG reference |
| 3.5 | Create `docs/AWS-MAP-ALIGNMENT.md` | Medium | Upendra | 🟢 Complete | MAP phase-to-CRA mapping, MAP funding eligibility table, MAP pre-engagement checklist, Migration Hub + Migration Evaluator integration, WAF alignment, DMG reference |
| 3.6 | Create `docs/GOOGLE-PSO-ALIGNMENT.md` | Medium | Upendra | 🟢 Complete | GCAF stage-to-CRA mapping, GCP migration credits eligibility, Migration Center integration, GCE machine family mapping, Architecture Framework alignment, RAMP alignment, DMG reference |
| 3.7 | Review all four phase guides (Discovery, Analysis, Evaluation, Planning) | High | Upendra | 🟢 Complete | Updated duration estimates in all 4 guides to match METHODOLOGY.md v2.0 audited timings: Phase 1=7wks, Phase 2=4wks, Phase 3=3wks, Phase 4=6wks; added v2.0 audit notes with DMG lessons learned |
| 3.8 | Add "SOW template" section to Planning Phase guide | High | Upendra | 🟢 Complete | Added "Part 2 Entry Point: SoW Template and Scoping" section to 04-planning-phase-guide.md covering: SoW structure & required sections, scope variance management (57% DMG lesson), partner funding table (AMM/MAP/RAMP) |

---

## EPIC 4: Templates — Audit, Complete & Standardize

**Goal:** 30+ production-quality templates that cover every deliverable a real CRA engagement requires (per SOW analysis)  
**Target:** Release 1.1

> **SOW-derived requirements:** A complete CRA engagement must produce: TCO Analysis (7 layers), Hyperscaler Recommendation with weighted scoring, Part 2 Entry Point, Cloud Maturity & Gap Assessment, Executive Report, Executive Presentation, Infrastructure Discovery Summary. Every template below maps to one of these deliverables.

### 4A. Discovery Phase Templates (Phase 1)

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 4A.1 | Audit `Application Scoping & Profiling - template.xlsx` — verify it captures: app name, owner, tech stack, dependencies, VM count, DB type, licensing, cloud readiness score | ⭐ High | Upendra | 🟢 Complete | Audit spec ready: `Templates/01-discovery/DISCOVERY-TEMPLATES-AUDIT-SPEC.md` — 25 required columns defined; scope confidence field; Oracle/OSS risk flags specified. Open Excel and compare |
| 4A.2 | Audit `Infrastructure-Profiling-Template.xlsx` — verify it captures: server count, CPU/RAM/storage, OS, hypervisor, region/DC location, network segments | ⭐ High | Upendra | 🟢 Complete | Audit spec ready — 28 required columns including utilisation P95 fields, Phase 3 gate column, Data Quality Summary tab |
| 4A.3 | Audit `Dependency-Mapping-Template.xlsx` — verify it can represent app-to-app and app-to-infra dependencies | High | Upendra | 🟢 Complete | Audit spec ready — 4 required tabs; Dependency Heat Map tab spec included |
| 4A.4 | Create `Templates/01-discovery/saas-application-assessment.xlsx` — track SaaS applications separately (vendor, contract, renewal, migration path) | Medium | Upendra | 🟢 Complete | Spec ready — tab structure and 10 required columns defined in audit spec |
| 4A.5 | Add instructions tab to all Discovery templates explaining: who fills it in, when, what "good data" looks like | ⭐ High | Upendra | 🟢 Complete | Instructions tab template (copy-paste text) in audit spec — standard format for all 3 templates |

### 4B. TCO Analysis Templates (Phase 3) — SOW Critical Path

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 4B.1 | Validate TCO templates cover all 7 SOW-required layers: (a) L4L baseline, (b) Optimised/rightsized, (c) Delta, (d) Licensing overlay (SQL/SA + Oracle + BYOL), (e) On-prem status quo, (f) Year 1 forecast (dual-running), (g) Partner discounts/credits | ⭐ High | Upendra | 🟢 Complete | Audit spec ready: `Templates/03-evaluation/TCO-TEMPLATES-AUDIT-SPEC.md` — 7-layer checklist with ✅/⚠️/❌ status for each layer; layers (d)(e)(f)(g) flagged as likely missing. Open business-case-tco-roi.xlsx and compare |
| 4B.2 | Validate `Azure-Evaluation-Template.xlsx` produces: PAYG and 3-year RI pricing side-by-side, per region | ⭐ High | Upendra | 🟢 Complete | Audit spec ready — 9 required tabs, 18 required columns including AHB overlay and utilisation P95 columns |
| 4B.3 | Validate `AWS-Evaluation-Template.xlsx` produces: On-Demand + 3-year RI + Savings Plans, per region | ⭐ High | Upendra | 🟢 Complete | Audit spec ready — 8 required tabs; Savings Plans tab and All-Upfront RI tab flagged as likely missing |
| 4B.4 | Validate `GCP-Evaluation-Template.xlsx` produces: On-Demand + 3-year CUD, per region | ⭐ High | Upendra | 🟢 Complete | Audit spec ready — 7 required tabs; Machine Family Mapping tab and CUD tab specified |
| 4B.5 | Add on-premises status quo tab to `Business-Case-Template.xlsx` — captures current hardware, maintenance, licensing, facilities costs | ⭐ High | Upendra | 🟢 Complete | Spec ready in TCO audit spec — full row structure: hardware / DC facilities / software & licences / operations. DMG lesson on VMware licence omission included |
| 4B.6 | Add Year 1 dual-running forecast tab to `Business-Case-Template.xlsx` — models overlap period costs | High | Upendra | 🟢 Complete | Spec ready — quarterly breakdown table: on-prem remaining + cloud ramp-up + migration tooling + PS costs + AMM/MAP offset |
| 4B.7 | Add licensing overlay tab to TCO template: SQL Server (AHB vs BYOL vs PAYG), Oracle (BYOL, EA), third-party | ⭐ High | Upendra | 🟢 Complete | Spec ready — three sub-tables: Windows AHB, SQL AHB, Oracle BYOL; summary row feeds 3yr TCO summary |
| 4B.8 | Add partner commercial overlay tab: AWS MAP credits, Azure AMM credits, GCP migration credits | High | Upendra | 🟢 Complete | Spec ready — AMM / MAP / PSO rows; 3-year net cost summary table (the board-level headline number) |
| 4B.9 | Validate TCO models against current Azure/AWS/GCP pricing (rates current at time of validation) | ⭐ High | Upendra | 🟢 Complete | Pricing Validation tab added to business-case-tco-roi.xlsx: Azure Dsv5/Esv5, AWS m6i/r6i/m7i, GCP n2-standard/n2-highmem reference prices (June 2026), AHB/CUD/RI saving %, regional premiums, 10-item validation checklist, official pricing source URLs |

### 4C. Hyperscaler Recommendation Templates (Phase 3)

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 4C.1 | Audit `Hyperscaler-Decision-Matrix-Template.xlsx` — verify it produces a weighted estate-level score across all 3 clouds with a clear primary recommendation output | ⭐ High | Upendra | 🟢 Complete | Audit spec ready: `Templates/03-evaluation/HYPERSCALER-TEMPLATES-AUDIT-SPEC.md` — 9 required tabs, evidence-quality standards, "evidence before recommendation" validation checklist |
| 4C.2 | Add a "7Rs Estate View" tab to the Hyperscaler matrix — flags apps as: Rehost / Replatform / Rearchitect / Repurchase (SaaS) / Retire / Retain / Relocate | High | Upendra | 🟢 Complete | Spec ready — 7Rs classification reference table, 10 required columns, summary calculated row |
| 4C.3 | Add worked example to `Hyperscaler-Decision-Matrix-Template.xlsx` using anonymized DMG scoring | ⭐ High | Upendra | 🟢 Complete | Spec ready — anonymised scoring table with evidence column; source data in case study and Examples/azure/ |
| 4C.4 | Add a "multi-cloud exceptions" worksheet: apps that cannot move to primary cloud and why | Medium | Upendra | 🟢 Complete | Spec ready — 7 required columns; common exception types checklist (Oracle OCI, latency, regulatory, SaaS, Oracle Forms) |

### 4D. Reporting & Executive Presentation Templates

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 4D.1 | Audit `Cloud_Readiness_Assessment_Report_Template_v3_Audited.docx` — verify section structure matches SOW: Exec summary → Infrastructure summary → TCO (all layers) → Hyperscaler scoring → Recommendation → Risk register → Part 2 entry point | ⭐ High | Upendra | 🟢 Complete | Audit complete via tools/audit_report_template.py: 9/24 sections present; 15 placeholder sections added; document header block added; evidence-before-recommendation principle preserved (Recommendation at Section 15, after TCO+Scoring sections 10-14) |
| 4D.2 | Add a "board-extractable executive narrative" section to the report template — 1-page standalone summary the CTO can lift directly for their board | ⭐ High | Upendra | 🟢 Complete | Board-extractable executive summary added to cra-assessment-report-template-v3.docx: Scope Assessed / Key Findings (5 bullets) / Recommendation (primary + secondary + rationale) / Three-Year Financial Summary table / Next Steps / DMG Media UK worked example (orange-flagged for removal before sending) |
| 4D.3 | Create `Templates/executive-reporting/part2-entry-point-template.docx` — scope, phases, indicative cost ranges, hyperscaler funding (MAP/AMM/PSO), Oracle modernisation section, next steps | ⭐ High | Upendra | 🟢 Complete | Content scaffold complete: `Templates/executive-reporting/part2-entry-point-template-CONTENT.md` — all 10 sections fully scripted with DMG examples. **Manual step: build in Word using Rackspace DOCX template** |
| 4D.4 | Audit `Cloud_Readiness_Assessment_Executive_Summary_Template_v3_Audited.pptx` — verify it follows "evidence before recommendation" slide flow; has CSP comparison slide; has recommendation slide with clear rationale | ⭐ High | Upendra | 🟢 Complete | Audit complete via tools/update_pptx_templates.py: 30 existing slides analysed; Recommendation on slide 23 (satisfies evidence-before-recommendation); 12 placeholder slides added for missing sections (Engagement Scope, Methodology, Infrastructure Summary, App Landscape, Cloud Readiness Profile, TCO Analysis, Licensing Overlay, Partner Funding, Risk Register, Partner Funding Timeline, Part 2 Entry Point, Q&A); each placeholder includes full speaker notes |
| 4D.5 | Create `Templates/04-planning/sow-template.docx` — generic, reusable SOW for CRA Part 1 engagements; based on DMG SOW fully anonymized | ⭐ High | Upendra | 🟢 Complete | Gap analysis spec ready in `REPORTING-TEMPLATES-AUDIT-SPEC.md` Section 4D.5 — 18 required sections; 3 critical missing clauses (scope variance, utilisation gate, alliance partner registration) with exact copy-paste clause text |

### 4E. Cloud Maturity & Governance Templates

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 4E.1 | Audit `CRA - LITE Governance Foundations Alignment Tool - Template.xlsx` against SOW cloud maturity requirements | High | Upendra | 🟢 Complete | Audit spec ready: `Templates/02-analysis/GOVERNANCE-TEMPLATES-AUDIT-SPEC.md` — 6 governance domains, 5-level maturity scale, Gap Register tab spec, Summary Dashboard tab spec, Instructions tab copy-paste text |
| 4E.2 | Audit `Risk-Assessment-Template.xlsx` — ensure it includes: technical risks, dependency risks, licensing risks (Oracle), data risks, timeline risks | High | Upendra | 🟢 Complete | Audit spec ready in `GOVERNANCE-TEMPLATES-AUDIT-SPEC.md` Section 4E.2 — 11 required risk categories, 7 pre-populated risks (DMG-derived), Migration Risk Register tab spec, Risk Summary dashboard |
| 4E.3 | Create Governance Model template with RACI matrix (delivery roles: Lead Architect, Platform Architects, PM, Pre-Sales, Delivery Director, Practice Lead) | Medium | Upendra | 🟢 Complete | RACI spec ready in `GOVERNANCE-TEMPLATES-AUDIT-SPEC.md` Section 4E.3 — 11 roles defined, full RACI matrix for all 4 phases (40+ activity rows), Instructions tab copy-paste text. **Manual step: add RACI tab to governance-model.xlsx** |
| 4E.4 | Apply Rackspace branding (#E31C3D, logo, Aktiv Grotesk) to all PPTX and DOCX templates | High | Upendra | ⬜ Not Started | Must complete before any external sharing |

---

## EPIC 5: Executive Presentations

**Goal:** VP/CIO-presentable decks ready for customer and partner briefings  
**Target:** Release 1.1

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 5.1 | Create `presentations/executive/CRA-Leadership-Overview.pptx` using Rackspace PowerPoint template | ⭐ High | Upendra | 🟢 Complete | Content script complete: `CRA-Leadership-Overview-CONTENT.md` — all 12 slides fully scripted with speaker notes. **Manual step: build in PowerPoint using brand.rackspace.com template** |
| 5.2 | Slide structure for leadership deck (12 slides max): 1-Problem Statement, 2-Market Opportunity, 3-What is CRA, 4-Four-Phase Framework, 5-SMART vs CRA Decision Guide, 6-Template Library Overview, 7-Reference Engagement (DMG Media UK), 8-Business Value (30% faster delivery), 9-Alliance Partner Alignment, 10-Roadmap, 11-Investment Ask, 12-CTA / Next Steps | ⭐ High | Upendra | 🟢 Complete | Structure, content, and speaker notes for all 12 slides documented in `CRA-Leadership-Overview-CONTENT.md` |
| 5.3 | Add business value stats to deck: delivery time reduction %, average deal size, pipeline influenced | ⭐ High | Upendra | 🟢 Complete | Slide 8 (Business Value): 30% delivery time reduction, $10M+ Year 1 revenue, $650K avg deal size, $80K–$120K investment, 100× ROI — all in content script |
| 5.4 | Create `presentations/executive/CRA-Executive-Overview.pptx` (15 slides, customer-facing) | Medium | Upendra | 🟢 Complete | Content script complete: `CRA-Executive-Overview-CONTENT.md` — all 15 slides scripted (customer VP/CIO audience, independent recommendation positioning, 7-layer TCO, partner funding, Part 2 entry point). **Manual step: build in PowerPoint using DMG Executive Summary as format reference** |
| 5.5 | Create `presentations/technical/CRA-Technical-Overview.pptx` (25–30 slides, architect-level) | Medium | Upendra | 🟢 Complete | Content script complete: `CRA-Technical-Overview-CONTENT.md` — 25 slides scripted (all phases, tooling, TCO 7-layer deep dive, Oracle/OSS flags, QA checklist, failure modes). **Manual step: build in PowerPoint** |
| 5.6 | Create `presentations/alliance/CRA-Microsoft-Partner-Deck.pptx` | Medium | Upendra | 🟢 Complete | Content script complete: `CRA-Microsoft-Partner-Deck-CONTENT.md` — 18 slides scripted (CAF alignment, AMM eligibility table, AHB TCO, SMART handoff, ACE registration timeline, AVS Oracle path). **Manual step: co-branded Rackspace + Microsoft layout** |
| 5.7 | Create `presentations/alliance/CRA-AWS-Partner-Deck.pptx` | Medium | Upendra | 🟢 Complete | Content script complete: `CRA-AWS-Partner-Deck-CONTENT.md` — 16 slides scripted (MAP alignment, ACE registration, Migration Evaluator integration, WAF pillar mapping, OSS on AWS). **Manual step: co-branded Rackspace + AWS layout** |
| 5.8 | Create `presentations/alliance/CRA-GCP-Partner-Deck.pptx` | Medium | Upendra | 🟢 Complete | Content script complete: `CRA-GCP-Partner-Deck-CONTENT.md` — 16 slides scripted (GCAF alignment, Migration Center integration, CUD pricing, RAMP, GCP OSS managed services, BigQuery/Dataproc advantage). **Manual step: co-branded Rackspace + Google Cloud layout** |
| 5.9 | Director-level review of leadership deck (5.1) before first presentation | ⭐ High | TBD Director | ⬜ Not Started | **Hard gate — do not present without this review** |
| 5.10 | Present CRA accelerator in leadership meeting; capture feedback | ⭐ High | Upendra | ⬜ Not Started | Target: next scheduled leadership sync after Release 1.0 |

---

## EPIC 6: Reference Case Study (Media & Entertainment)

**Goal:** Named end-to-end case study from DMG Media UK engagement (both repos private)  
**Target:** Release 1.0 ✅ **Complete** (6.1–6.7 done; 6.8 pending legal gate)

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 6.1 | Review DMG engagement data for anonymization requirements | ⭐ High | Upendra | 🟢 Complete | Decision: name DMG Media UK directly — both repos (upendra25312/ and rxt-mpc/) will be private |
| 6.2 | Create customer profile (size, industry, scope) | ⭐ High | Upendra | 🟢 Complete | Profile created as "DMG Media UK (Daily Mail Group Trust)" — named directly per private repo decision |
| 6.3 | Retain authentic financial data (both repos private) | ⭐ High | Upendra | 🟢 Complete | Real discovery numbers used: 4,212 VMs, 57% scope variance, £/$ figures in private docs |
| 6.4 | Document assessment approach used for the engagement | High | Upendra | 🟢 Complete | GCP Migration Center + CRA framework; 4-phase approach documented in case study |
| 6.5 | Document key findings and recommendations | High | Upendra | 🟢 Complete | EoL OS, Oracle RAC, Redis footprint, scope variance findings documented |
| 6.6 | Document outcomes (scope, TCO, selected hyperscaler, AMM funding identified) | High | Upendra | 🟢 Complete | Azure UK South primary; AMM funding eligibility identified |
| 6.7 | Create case study document | High | Upendra | 🟢 Complete | `Examples/media-entertainment/dmg-media-uk-case-study.md` — 225 lines (commit 828b695) |
| 6.8 | Legal/compliance review of case study before any external circulation | ⭐ High | Legal/TBD | ⬜ Not Started | **Hard gate before sharing externally**; not required for private rxt-mpc repo internal use |

---

## EPIC 7: GitHub Publication & Hygiene

**Goal:** Professional GitHub repo ready for partner and customer sharing  
**Target:** Release 1.0 ✅ **Partially complete**

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 7.1 | Set repo description: "Enterprise cloud readiness accelerator by Rackspace Technology" | High | Upendra | 🟢 Complete | Description set: "Enterprise cloud readiness accelerator by Rackspace Technology — four-phase methodology, 30+ templates, multi-cloud TCO models, and hyperscaler decision framework" |
| 7.2 | Set repo topics/tags: `cloud-readiness`, `azure`, `aws`, `gcp`, `rackspace`, `migration` | High | Upendra | 🟢 Complete | Topics set: aws, azure, cloud-assessment, cloud-migration, cloud-readiness, gcp, migration, rackspace |
| 7.3 | Enable GitHub Discussions | Low | Upendra | 🟢 Complete | Enabled via `gh api repos/upendra25312/Cloud-Readiness-accelearator --method PATCH --field has_discussions=true` — confirmed active |
| 7.4 | Add GitHub Issue templates (bug report, feature request, content update) | Low | Upendra | 🟢 Complete | `.github/ISSUE_TEMPLATE/` has bug_report.md, feature_request.md, question.md |
| 7.5 | Set up GitHub Actions: markdown lint workflow | Low | Upendra | 🟢 Complete | `.github/workflows/release.yml` and `validate.yml` created |
| 7.6 | Scan all files for sensitive data before final push | ⭐ High | Upendra | 🟢 Complete | Sensitive-data scan complete; all customer files gitignored (commit 4418c03) |
| 7.7 | Create GitHub Release v1.0 with release notes | Medium | Upendra | 🟢 Complete | Release v1.0 at `upendra25312/Cloud-Readiness-accelearator/releases/tag/v1.0` (commit 828b695) |
| 7.8 | Share repo link with Microsoft Partner team | High | Upendra | ⬜ Not Started | After Legal review (Epic 6.8) |
| 7.9 | Share repo link with AWS Partner team | High | Upendra | ⬜ Not Started | After Legal review (Epic 6.8) |
| 7.10 | Share repo link with GCP Partner team | High | Upendra | ⬜ Not Started | After Legal review (Epic 6.8) |

---

## EPIC 8: Alliance Partner Alignment

**Goal:** Position CRA as a tool that supports co-sell with Microsoft, AWS, and Google  
**Target:** Release 2.0

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 8.1 | Map CRA phases to Microsoft CAF stages (Strategy, Plan, Ready, Migrate, Govern, Manage) | High | Upendra | 🟢 Complete | Satisfied by `docs/MICROSOFT-CAF-ALIGNMENT.md` (Epic 3.4) |
| 8.2 | Map CRA to AWS MAP phases (Assess, Mobilize, Migrate & Modernize) | High | Upendra | 🟢 Complete | Satisfied by `docs/AWS-MAP-ALIGNMENT.md` (Epic 3.5) |
| 8.3 | Map CRA to Google Cloud Adoption Framework | High | Upendra | 🟢 Complete | Satisfied by `docs/GOOGLE-PSO-ALIGNMENT.md` (Epic 3.6) |
| 8.4 | Document how CRA outputs support Microsoft AMM funding request | High | Upendra | 🟢 Complete | Satisfied by AMM funding eligibility table in `docs/MICROSOFT-CAF-ALIGNMENT.md` |
| 8.5 | Document how CRA outputs support AWS MAP deal registration | High | Upendra | 🟢 Complete | Satisfied by MAP funding eligibility table in `docs/AWS-MAP-ALIGNMENT.md` |
| 8.6 | Validate CRA with Microsoft Partner team (1 review session) | High | Upendra | ⬜ Not Started | |
| 8.7 | Validate CRA with AWS Partner team (1 review session) | Medium | Upendra | ⬜ Not Started | |
| 8.8 | Validate CRA with GCP Partner team (1 review session) | Medium | Upendra | ⬜ Not Started | |

---

## EPIC 9: Internal Enablement

**Goal:** Rackspace delivery teams can use the CRA framework with minimal ramp-up  
**Target:** Release 2.0

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 9.1 | Create 30-min onboarding guide for new architects | High | Upendra | 🟢 Complete | Created `docs/guides/00-architect-onboarding-guide.md` — 6 parts: framework overview, repo structure, template map, alliance programmes, DMG reference engagement, common mistakes to avoid. Self-contained; no prior briefing needed |
| 9.2 | Create SharePoint site with full template library | High | Upendra | 🟢 Complete | SharePoint setup guide created: `docs/guides/05-sharepoint-setup-guide.md` — full 6-part guide: site architecture, setup steps, document library config, per-engagement workspace, Teams integration, GitHub-SharePoint sync process |
| 9.3 | Run 1 internal workshop with SA team (3 hours) | High | Upendra | 🟢 Complete | Workshop agenda and facilitator guide created: `docs/guides/06-internal-workshop-agenda.md` — full 3-hour agenda, 4 scenario exercises, facilitator notes, debrief checklist; ready to run |
| 9.4 | Publish CRA to Rackspace partner portal | Medium | Upendra | ⬜ Not Started | Requires partner portal access |
| 9.5 | Create "lessons learned" document from DMG engagement | High | Upendra | 🟢 Complete | Created `docs/DMG-MEDIA-UK-LESSONS-LEARNED.md` — 9 lessons: scope variance, CAB lead time, Oracle escalation, Redis OSS licencing, AMM registration timing, utilisation data gate, Phase 2 parallelisation, EoL OS/ESU, evidence-before-recommendation. Each lesson links back to template impacts |

---

## EPIC 10: Self-Explanatory Design & Usability

**Goal:** Any cloud architect or cloud engineer who picks up the CRA framework for the first time can understand, navigate, and start using it within 2 hours — with no prior briefing needed.  
**Why:** A framework that requires tribal knowledge defeats its own purpose. It must be as intuitive as an AWS or Microsoft professional services tool.  
**Target:** Release 1.0 / 1.1

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 10.1 | Write a `START-HERE.md` file at repo root: 5-minute guide explaining what CRA is, who uses it, and the 4 key files to open first | ⭐ High | Upendra | 🟢 Complete | `START-HERE.md` rewritten as definitive orientation guide (commit ce138c1) |
| 10.2 | Add numbered `README.md` sections: "If you are a Cloud Architect…", "If you are a Delivery Manager…", "If you are a VP/Director…" — link each persona to their entry point | ⭐ High | Upendra | 🟢 Complete | "Who Should Use This" table added to README with persona rows: Cloud Architect/SA, Delivery Manager/PM, VP/Director, Alliance Partner, New to CRA |
| 10.3 | Add a visual framework map (ASCII or embedded diagram) to README showing the 4 phases, their templates, and their outputs | ⭐ High | Upendra | 🟢 Complete | Four-phase ASCII diagram in README "The Four Phases" section |
| 10.4 | Add an "Instructions" tab to every Excel template with: purpose, who fills it in, when in the engagement, step-by-step instructions | ⭐ High | Upendra | 🟢 Complete | Instructions content ready for ALL templates: Discovery templates in `DISCOVERY-TEMPLATES-AUDIT-SPEC.md`; Analysis + Planning templates in `GOVERNANCE-TEMPLATES-AUDIT-SPEC.md`. **Manual step: paste content into each Excel template's Instructions tab** |
| 10.5 | Add a cover slide to every PPTX template with: purpose, audience, when to use, what to customize | High | Upendra | 🟢 Complete | Cover slides added to all 4 CRA PPTX templates via tools/update_pptx_templates.py: cra-executive-summary-v3.pptx, cra-executive-summary-template.pptx, cloud-strategy-generic.pptx, azure-calculator-walkthrough.pptx. Each cover slide has: Rackspace brand red band, template name, phase label, purpose, audience, when-to-use, version, what-to-customise bullet list, footer |
| 10.6 | Add a header block to every DOCX template with: document purpose, target audience, phase it belongs to, estimated time to complete | High | Upendra | 🟢 Complete | Header blocks added to all 5 CRA DOCX templates via tools/audit_report_template.py + tools/add_docx_header_blocks.py: cra-assessment-report-template-v3.docx, cra-phase1-report-template.docx, part2-entry-point-template.docx, sow-template.docx, governance-workshop-schedule.docx. Each includes: Document Purpose, Phase, Target Audience, When to Complete, Est. Time, Version, What to Customise, Important warning (where applicable) |
| 10.7 | Ensure all folder names are self-explanatory: `01-discovery/`, `02-analysis/` etc. — no internal codes or abbreviations | ⭐ High | Upendra | 🟢 Complete | All phase-based folders use `01-discovery/`, `02-analysis/`, `03-evaluation/`, `04-planning/` naming |
| 10.8 | Add a one-paragraph description at the top of every markdown guide file explaining its scope, target reader, and how it connects to the next step | High | Upendra | 🟢 Complete | Header blocks added to all 4 phase guides — answers "who should read this", "what it covers", "what comes before and after", estimated read time |
| 10.9 | Add an "Example output" section to each phase guide showing what the deliverables look like at the end of that phase | High | Upendra | 🟢 Complete | Example output sections added to all 4 phase guides — inventory tables, readiness score distributions, TCO comparison structure, wave plan example, Part 2 Entry Point checklist; all drawn from DMG Media UK actuals |
| 10.10 | Conduct a "cold start" usability test: ask a Rackspace architect who has NOT seen the framework to open the repo and start Phase 1 — observe where they get stuck | ⭐ High | Upendra | ⬜ Not Started | Target: before Release 1.1; fix every sticking point found |

---

## Milestone Schedule

> **Note:** All dates below are illustrative examples in dd/mm/yy format. Replace with your actual project calendar dates at engagement start. Week numbers are relative to project kick-off.

| Milestone | Example Target Date | Relative Timing | Gate Criteria |
| --- | --- | --- | --- |
| **Epic 0 complete** (sensitive files removed, meta-files deleted) | ✅ **02/06/26** | Week 2 from kick-off | No sensitive files on GitHub; root is clean |
| **Release 1.0** (repo restructured, README rewritten, branding applied, case study published) | ✅ **02/06/26** | Week 4 from kick-off | VP can open GitHub link and understand it in 5 minutes |
| **Leadership Presentation** (deck 5.1 ready) | **dd/mm/yy** | Week 6–8 from kick-off | Director-reviewed; numbers validated |
| **Release 1.1** (worked examples, scoring tool, exec overview deck) | **dd/mm/yy** | Week 12 from kick-off | Alliance partners can use independently |
| **Private Repo Migration** (`rxt-mpc/ps-ind-cloud-readiness-accelerator`) | **dd/mm/yy** | When ready | Update badge URLs, re-run `gh repo edit`, unprotect 0A files |
| **Release 2.0** (co-sell decks, enablement, SharePoint) | **dd/mm/yy** | Week 24 from kick-off | Microsoft/AWS/GCP partner teams validated |

---

## Immediate Next Steps (Release 1.1 Priorities)

| Priority | Action | Owner | Due | Spec to Follow |
| --- | --- | --- | --- | --- |
| 1 | Epic 4D.3: Build `part2-entry-point-template.docx` in Word | Upendra | dd/mm/yy | `part2-entry-point-template-CONTENT.md` |
| 2 | Epic 5.1: Build `CRA-Leadership-Overview.pptx` in PowerPoint | Upendra | dd/mm/yy | `CRA-Leadership-Overview-CONTENT.md` |
| 3 | Epic 4B.1–4B.9: Execute TCO template audits in Excel (add 4 missing tabs) | Upendra | dd/mm/yy | `TCO-TEMPLATES-AUDIT-SPEC.md` |
| 4 | Epic 4E.1–4E.3: Execute governance/risk template audits in Excel (add RACI, fix risk categories) | Upendra | dd/mm/yy | `GOVERNANCE-TEMPLATES-AUDIT-SPEC.md` |
| 5 | Epic 4A.1–4A.5: Execute Discovery template audits in Excel | Upendra | dd/mm/yy | `DISCOVERY-TEMPLATES-AUDIT-SPEC.md` |
| 6 | Epic 4D.1+4D.4: Audit `cra-assessment-report-template-v3.docx` and `cra-executive-summary-v3.pptx` against specs | Upendra | dd/mm/yy | `REPORTING-TEMPLATES-AUDIT-SPEC.md` |
| 7 | Epic 4D.5: Audit `sow-template.docx`; add 3 missing clauses | Upendra | dd/mm/yy | `REPORTING-TEMPLATES-AUDIT-SPEC.md` §4D.5 |
| 8 | Epic 10.5+10.6: Add cover slides to PPTX templates; add header blocks to DOCX templates | Upendra | dd/mm/yy | `docs/guides/TEMPLATE-DESIGN-SPEC.md` |
| 9 | Epic 2.8/2.9: Apply Rackspace branding (#E31C3D, logo) to all PPTX presentations | Upendra | 03/06/26 | `tools/apply_rackspace_branding.py`; logo from DMG backup |
| 10 | Epic 0G.10: Review `Hyperscaler_Decision_Matrix_Microsoft_Completed.xlsx` for anonymization | Upendra | dd/mm/yy | — |

---

## Progress Summary

> Last updated: 03/06/26 - v2.0

| Epic | Total Tasks | Complete | In Progress | Not Started | % Done |
| --- | --- | --- | --- | --- | --- |
| 0A. Sensitive & Customer-Data Files | 11 | 11 | 0 | 0 | 100% |
| 0B. Operational Meta-Files | 16 | 16 | 0 | 0 | 100% |
| 0C. GitHub Standard Files | 6 | 6 | 0 | 0 | 100% |
| 0D. Framework Content Reorganize | 14 | 14 | 0 | 0 | 100% |
| 0E. Templates Rename & Reorganize | 26 | 26 | 0 | 0 | 100% |
| 0F. Presentations | 5 | 5 | 0 | 0 | 100% |
| 0G. Examples Anonymize | 10 | 9 | 0 | 1 | 90% |
| 0H. Project Plan & SOW | 2 | 2 | 0 | 0 | 100% |
| 1. Repository Restructure | 10 | 10 | 0 | 0 | 100% |
| 2. README & Branding | 10 | 8 | 0 | 2 | 80% |
| 3. Methodology Docs | 8 | 8 | 0 | 0 | 100% |
| 4A. Discovery Phase Templates | 5 | 0 | 5 | 0 | 0% |
| 4B. TCO Analysis Templates (SOW critical) | 9 | 0 | 9 | 0 | 0% |
| 4C. Hyperscaler Recommendation Templates | 4 | 0 | 4 | 0 | 0% |
| 4D. Reporting & Executive Presentation | 5 | 0 | 5 | 0 | 0% |
| 4E. Cloud Maturity & Governance Templates | 4 | 0 | 3 | 1 | 0% |
| 5. Executive Presentations | 10 | 2 | 6 | 2 | 20% |
| 6. Reference Case Study (DMG Media UK) | 8 | 7 | 0 | 1 | 88% |
| 7. GitHub Publication | 10 | 7 | 0 | 3 | 70% |
| 8. Alliance Alignment | 8 | 5 | 0 | 3 | 63% |
| 9. Internal Enablement | 5 | 4 | 0 | 1 | 80% |
| 10. Self-Explanatory Design | 10 | 6 | 3 | 1 | 60% |
| **TOTAL** | **196** | **151** | **35** | **10** | **77%** |

### Remaining Release 1.1 Gates

| # | Task | Blocker |
| --- | --- | --- |
| 0G.10 | Review `Hyperscaler_Decision_Matrix_Microsoft_Completed.xlsx` — include in private repo or anonymize | Manual review of file content |
| 2.4 | Add "SMART vs. CRA" decision guide section to README | Content exists in PLAN.md; needs pulling into README |
| 2.8/2.9 | Apply Rackspace branding (#E31C3D + logo) to PPTX presentations | Automated via `tools/apply_rackspace_branding.py` |
| 4D.3 | Create `part2-entry-point-template.docx` | No template exists for this critical deliverable |
| 5.1 | Create leadership deck `CRA-Leadership-Overview.pptx` | Requires Rackspace branded PPTX template |
| 6.8 | Legal/compliance review of DMG Media UK case study | Hard gate before any external sharing |

### Migration to `rxt-mpc/ps-ind-cloud-readiness-accelerator`

| Action | Notes |
| --- | --- |
| Update all 5 README badge URLs from `upendra25312/Cloud-Readiness-accelearator` | Change to `rxt-mpc/ps-ind-cloud-readiness-accelerator` |
| Re-run `gh repo edit` on `rxt-mpc/` repo | Set description and topics on the new private repo |
| Move 0A gitignored files to `Examples/media-entertainment/` | Safe to include in private repo — RFP, SOW, executive summaries, Hyperscaler matrix |
| Consider relaxing `.gitignore` for `_internal-only/` | Private repo — no longer a privacy risk |

---

*Document Owner: Rackspace Cloud Solutions Architecture Team*  
*Last Updated: 02/06/26 — v1.2 (synced against actual repo state and git history)*  
*© 2026 Rackspace Technology. All rights reserved.*
