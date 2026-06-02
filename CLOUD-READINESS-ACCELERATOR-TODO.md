# Cloud Readiness Accelerator — To-Do Tracker

**Version:** 1.1  
**Date:** dd/mm/yy  
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

> These files contain DMG customer data. They MUST NOT be shared externally or left unprotected in a public GitHub repo.

| # | File / Folder | Action Required | Priority | Status | Notes |
|---|---|---|---|---|---|
| 0A.1 | `Examples/Azure Example -2/DMG RFP - SOFT PERKS - Non Protected.pdf` | **REMOVE from GitHub immediately** | 🔴 Critical | ⬜ Not Started | Customer RFP document — never publish |
| 0A.2 | `Examples/Azure Example -2/DMG RFP - SOFT PERKS - Notes Non Protected.pdf` | **REMOVE from GitHub immediately** | 🔴 Critical | ⬜ Not Started | Customer notes — never publish |
| 0A.3 | `Examples/Azure Example -2/Microsoft Unified for DMG Media.pptx` | **REMOVE from GitHub; keep local only** | 🔴 Critical | ⬜ Not Started | Microsoft-DMG joint document — confidential |
| 0A.4 | `Examples/Azure Example -2/Hyperscaler_Decision_Matrix_Microsoft_Completed.xlsx` | Move to `_internal-only/examples/` after anonymization review | ⭐ High | ⬜ Not Started | Contains DMG-specific scoring — needs anonymization |
| 0A.5 | `Reports format example/DMG - CRA - Executive Summary v2.pdf` | Move to `_internal-only/reference/`; remove from GitHub | ⭐ High | ⬜ Not Started | Customer executive summary — legal review needed |
| 0A.6 | `Reports format example/DMG - CRA - Executive Summary v2 backup.pptx` | Move to `_internal-only/reference/`; remove from GitHub | ⭐ High | ⬜ Not Started | Customer PPTX backup — sensitive |
| 0A.7 | `Reports format example/DMG_Cloud_Readiness_Assessment_Part_1_Report_v2.0.docx` | Move to `_internal-only/reference/`; create anonymized version | ⭐ High | ⬜ Not Started | Full customer report — **best reference for anonymized case study** |
| 0A.8 | `Reports format example/DMG_Cloud_Readiness_Assessment_Part_1_Report_v2.0.pdf` | Same as 0A.7 | ⭐ High | ⬜ Not Started | PDF version of customer report |
| 0A.9 | `SOW/DMG Cloud Readiness Assessment Part 1 - Rebaselined Objectives & Plan - 10 Apr 2026.docx` | Move to `_internal-only/sow/`; create anonymized SOW template from it | ⭐ High | ⬜ Not Started | Customer SOW — DO NOT publish; use as basis for generic SOW template |
| 0A.10 | `Templates/DMG - CRA - Executive Summary v2.pptx` | Rename to `CRA-Executive-Summary-Template-v2.pptx`; strip DMG content | ⭐ High | ⬜ Not Started | Good template foundation — just needs debranding |
| 0A.11 | `Templates/DMG_CRA_Phase1_Report_v2.docx` | Rename to `CRA-Phase1-Report-Template-v2.docx`; strip DMG content | ⭐ High | ⬜ Not Started | Good template — needs debranding |

### 0B. Operational Meta-Files — Archive or Delete

> These ~45 files were generated as working notes during repo setup. They have no value to a VP, Director, or alliance partner. Leaving them in the root signals "unfinished work."

| # | Files to Archive / Delete | Action | Priority | Status |
|---|---|---|---|---|
| 0B.1 | `EXECUTE-GITHUB-PUBLICATION.sh`, `EXECUTE-GITHUB-PUBLICATION.bat` | Delete — obsolete shell scripts | ⭐ High | ⬜ Not Started |
| 0B.2 | `PERMISSION-DENIED-FIX.md`, `MANUAL-GITHUB-STEPS.md` | Delete — internal troubleshooting notes | ⭐ High | ⬜ Not Started |
| 0B.3 | `GITHUB-COMPLETION-SUMMARY.md`, `GITHUB-IMPLEMENTATION-COMPLETE.md`, `GITHUB-READY-FOR-PUBLICATION.md` | Delete — session artifacts | ⭐ High | ⬜ Not Started |
| 0B.4 | `GITHUB-IMPLEMENTATION-GUIDE.md`, `GITHUB-IMPLEMENTATION-INDEX.md`, `GITHUB-IMPLEMENTATION-STRATEGY.md` | Delete — superseded by PLAN.md | ⭐ High | ⬜ Not Started |
| 0B.5 | `GITHUB-PUBLISHING-GUIDE.md`, `GITHUB-PUBLISHING-SUMMARY.md`, `GITHUB-QUICK-START.md` | Delete — superseded by README + PLAN.md | ⭐ High | ⬜ Not Started |
| 0B.6 | `GITHUB-START-HERE.md`, `GITHUB-GETTING-STARTED.md`, `START-HERE.md`, `START-GITHUB-PUBLICATION.md` | Delete — replaced by README.md | ⭐ High | ⬜ Not Started |
| 0B.7 | `GITHUB-METHODOLOGY.md` | Extract any unique content → merge into `docs/METHODOLOGY.md`, then delete | Medium | ⬜ Not Started |
| 0B.8 | `SHAREPOINT-DEPLOYMENT-GUIDE.md`, `SHAREPOINT-IMPLEMENTATION-PLAN.md`, `SHAREPOINT-PAGE-CONTENT.md`, `SHAREPOINT-PUBLISHING-SUMMARY.md`, `SHAREPOINT-PAGE.html` | Move to `_internal-only/sharepoint/` (useful for internal SharePoint setup) | Medium | ⬜ Not Started |
| 0B.9 | `SHAREPOINT-EXECUTIVE-SUMMARY.md`, `SHAREPOINT-VS-GITHUB-ANALYSIS.md`, `COPILOT-SHAREPOINT-PROMPT.md` | Move to `_internal-only/sharepoint/` | Medium | ⬜ Not Started |
| 0B.10 | `COPY-PASTE-COMMANDS.md`, `README-GITHUB-EXECUTION.md`, `README-SHAREPOINT-PUBLISHING.md` | Delete — internal working notes | ⭐ High | ⬜ Not Started |
| 0B.11 | `DEPLOYMENT-PACKAGE.md`, `DEPLOYMENT-STRATEGY.md`, `PHASE-1-DEPLOYMENT-CHECKLIST.md` | Merge useful content → PLAN.md or delete | Medium | ⬜ Not Started |
| 0B.12 | `IMPLEMENTATION-STATUS.md`, `PARALLEL-WORKSTREAMS-PLAN.md`, `NEXT-STEPS-ACTION-PLAN.md` | Delete — superseded by TODO tracker | ⭐ High | ⬜ Not Started |
| 0B.13 | `EXPERT-TEAM-DECISION.md`, `EXPERT-TEAM-SUMMARY.md`, `EXECUTIVE-ACTION-SUMMARY.md` | Delete — internal session notes | ⭐ High | ⬜ Not Started |
| 0B.14 | `DELIVERABLES-CHECKLIST.md`, `ACCELERATOR-SUMMARY.md` | Merge useful content → README or TODO, then delete | Medium | ⬜ Not Started |
| 0B.15 | `FINAL-PUBLISHING-STRATEGY.md`, `FINAL-SUMMARY-AND-NEXT-STEPS.md` | Delete — superseded by PLAN.md | ⭐ High | ⬜ Not Started |
| 0B.16 | `design.md`, `requirements.md`, `tasks.md`, `package.json` | Review for useful content; delete or move to `_internal-only/` | Medium | ⬜ Not Started |

### 0C. GitHub Standard Files — Rename & Consolidate

> Several standard repo files exist with "GITHUB-" prefix. Rename them to standard names.

| # | Current File | Rename To | Action | Status |
|---|---|---|---|---|
| 0C.1 | `GITHUB-CHANGELOG.md` | `CHANGELOG.md` | Rename (standard GitHub convention) | ⬜ Not Started |
| 0C.2 | `GITHUB-CONTRIBUTING.md` | `CONTRIBUTING.md` | Rename | ⬜ Not Started |
| 0C.3 | `GITHUB-CODE-OF-CONDUCT.md` | `CODE_OF_CONDUCT.md` | Rename | ⬜ Not Started |
| 0C.4 | `QUICK-START-GUIDE.md` | Merge into README.md "Quick Start" section, then delete | Medium | ⬜ Not Started |
| 0C.5 | `QUICK-REFERENCE-CARD.md` | Move to `docs/guides/quick-reference.md` | Low | ⬜ Not Started |
| 0C.6 | `ROADMAP.md` | Review content; merge into PLAN.md Section 8 or keep as standalone | Medium | ⬜ Not Started |

### 0D. Framework Content — Reorganize to Target Structure

> Phase guides, integration guides, and methodology docs are in the wrong locations.

| # | Current Location | Move To | Action | Status |
|---|---|---|---|---|
| 0D.1 | `Discovery-Phase-Guide.md` (root) | `docs/guides/01-discovery-phase-guide.md` | Move + rename | ⬜ Not Started |
| 0D.2 | `Analysis-Phase-Guide.md` (root) | `docs/guides/02-analysis-phase-guide.md` | Move + rename | ⬜ Not Started |
| 0D.3 | `Evaluation-Phase-Guide.md` (root) | `docs/guides/03-evaluation-phase-guide.md` | Move + rename | ⬜ Not Started |
| 0D.4 | `Planning-Phase-Guide.md` (root) | `docs/guides/04-planning-phase-guide.md` | Move + rename | ⬜ Not Started |
| 0D.5 | `Methodology-Overview.md` (root) | `docs/methodology/methodology-overview.md` | Move | ⬜ Not Started |
| 0D.6 | `docs/METHODOLOGY.md` | `docs/methodology/METHODOLOGY.md` | Move into subdirectory | ⬜ Not Started |
| 0D.7 | `FRAMEWORK-INDEX.md` (root) | `docs/FRAMEWORK-INDEX.md` | Move | ⬜ Not Started |
| 0D.8 | `Integration-Guides/CMDB-Integration-Guide.md` | `docs/integration/cmdb-integration-guide.md` | Move | ⬜ Not Started |
| 0D.9 | `Integration-Guides/Cloud-Assessment-Tool-Integration-Guide.md` | `docs/integration/cloud-assessment-tools.md` | Move | ⬜ Not Started |
| 0D.10 | `Integration-Guides/Monitoring-Tool-Integration-Guide.md` | `docs/integration/monitoring-tools.md` | Move | ⬜ Not Started |
| 0D.11 | `Customization-Guides/Industry-Customization-Guide.md` | `docs/customization/industry-customization.md` | Move | ⬜ Not Started |
| 0D.12 | `Customization-Guides/Organization-Size-Adaptation-Guide.md` | `docs/customization/org-size-adaptation.md` | Move | ⬜ Not Started |
| 0D.13 | `Quality-Assurance/Data-Validation-Checklist.md` | `docs/governance/data-validation-checklist.md` | Move | ⬜ Not Started |
| 0D.14 | `docs/azure-cloud-adoption-framework.pdf` | `docs/reference/azure-cloud-adoption-framework.pdf` | Move to reference subfolder | ⬜ Not Started |

### 0E. Templates — Rename, Debrand & Reorganize by Phase

> All templates need: (1) DMG branding removed from filename, (2) moved to phase-based subfolders, (3) content reviewed for customer data.

| # | Current Filename | Target Location & New Name | Action Required | Status |
|---|---|---|---|---|
| 0E.1 | `Templates/Application Scoping & Profiling - template.xlsx` | `templates/01-discovery/application-scoping-profiling.xlsx` | Rename + move | ⬜ Not Started |
| 0E.2 | `Templates/Infrastructure-Profiling-Template.xlsx` | `templates/01-discovery/infrastructure-profiling.xlsx` | Move + lowercase | ⬜ Not Started |
| 0E.3 | `Templates/Dependency-Mapping-Template.xlsx` | `templates/01-discovery/dependency-mapping.xlsx` | Move + lowercase | ⬜ Not Started |
| 0E.4 | `Templates/Cloud-Readiness-Assessment-v2.xlsx` | `templates/02-analysis/cloud-readiness-scoring-v2.xlsx` | Move + rename | ⬜ Not Started |
| 0E.5 | `Templates/Readiness-Scoring-Criteria-Template.xlsx` | `templates/02-analysis/readiness-scoring-criteria.xlsx` | Move + lowercase | ⬜ Not Started |
| 0E.6 | `Templates/CRA - LITE Governance Foundations Alignment Tool - Template.xlsx` | `templates/02-analysis/governance-foundations-alignment.xlsx` | Move + rename | ⬜ Not Started |
| 0E.7 | `Templates/AWS-Evaluation-Template.xlsx` | `templates/03-evaluation/aws-evaluation.xlsx` | Move + lowercase | ⬜ Not Started |
| 0E.8 | `Templates/Azure-Evaluation-Template.xlsx` | `templates/03-evaluation/azure-evaluation.xlsx` | Move + lowercase | ⬜ Not Started |
| 0E.9 | `Templates/GCP-Evaluation-Template.xlsx` | `templates/03-evaluation/gcp-evaluation.xlsx` | Move + lowercase | ⬜ Not Started |
| 0E.10 | `Templates/Hyperscaler-Decision-Matrix-Template.xlsx` | `templates/03-evaluation/hyperscaler-decision-matrix.xlsx` | Move + lowercase | ⬜ Not Started |
| 0E.11 | `Templates/HyperScalar Weighted Selection Criteria.xlsx` (root) | `templates/03-evaluation/hyperscaler-weighted-selection-criteria.xlsx` | Move + rename | ⬜ Not Started |
| 0E.12 | `Templates/Business-Case-Template.xlsx` | `templates/03-evaluation/business-case-tco-roi.xlsx` | Move + rename | ⬜ Not Started |
| 0E.13 | `Templates/Risk-Assessment-Template.xlsx` | `templates/04-planning/risk-assessment.xlsx` | Move + lowercase | ⬜ Not Started |
| 0E.14 | `Templates/Migration-Wave-Planning-Template.xlsx` | `templates/04-planning/migration-wave-planner.xlsx` | Move + lowercase | ⬜ Not Started |
| 0E.15 | `Templates/Governance-Model-Template.xlsx` | `templates/04-planning/governance-model.xlsx` | Move + lowercase | ⬜ Not Started |
| 0E.16 | `Templates/Executive-Summary-Report-Template.xlsx` | `templates/04-planning/executive-summary-data.xlsx` | Move + rename | ⬜ Not Started |
| 0E.17 | `Templates/CRA - LITE Governance Assessment Workshop Schedule Template.docx` | `templates/04-planning/governance-workshop-schedule.docx` | Move + rename | ⬜ Not Started |
| 0E.18 | `Templates/DMG - CRA - Executive Summary v2.pptx` | `templates/executive-reporting/cra-executive-summary-template.pptx` | **Debrand DMG → Rackspace**, move | ⬜ Not Started |
| 0E.19 | `Templates/DMG_CRA_Phase1_Report_v2.docx` | `templates/executive-reporting/cra-phase1-report-template.docx` | **Debrand DMG → Rackspace**, move | ⬜ Not Started |
| 0E.20 | `Templates/Cloud_Readiness_Assessment_Executive_Summary_Template_v3_Audited.pptx` | `templates/executive-reporting/cra-executive-summary-v3.pptx` | Move — already audited | ⬜ Not Started |
| 0E.21 | `Templates/Cloud_Readiness_Assessment_Report_Template_v3_Audited.docx` | `templates/executive-reporting/cra-assessment-report-template-v3.docx` | Move — already audited | ⬜ Not Started |
| 0E.22 | `Templates/ADFD-Solution-Assessment-Report.pptx` | Review: if partner-specific, move to `_internal-only/`; if generic, rebrand | Medium | ⬜ Not Started |
| 0E.23 | `Templates/MS-Solution-Assessment Report.pptx` | `templates/executive-reporting/ms-solution-assessment.pptx` | Move — Microsoft partner reference | ⬜ Not Started |
| 0E.24 | `Templates/Azure Calc.pptx` | `templates/03-evaluation/azure-calculator-walkthrough.pptx` | Move + rename | ⬜ Not Started |
| 0E.25 | `Templates/Cloud-Strategy-Generic.pptx` | `templates/executive-reporting/cloud-strategy-generic.pptx` | Move | ⬜ Not Started |
| 0E.26 | `Templates/Data Gathering Template Guide.pptx` | `docs/guides/data-gathering-guide.pptx` | Move to docs | ⬜ Not Started |

### 0F. Presentations — Review, Rebrand & Classify

> Three CRA PPTX files at root need quality review and Rackspace branding applied.

| # | File | Action | Notes | Status |
|---|---|---|---|---|
| 0F.1 | `Cloud_Readiness_Accelerator_Rackspace_V1.1.pptx` | **Keep as primary presentation** — apply Rackspace branding, move to `presentations/executive/` | Best candidate for VP/Director sharing | ⬜ Not Started |
| 0F.2 | `Cloud Readiness Accelerator Reusable Enterprise Multi-Cloud Assessment Framework V1.pptx` | Compare with V1.1; keep best version or merge, move to `presentations/executive/` | May be predecessor to V1.1 | ⬜ Not Started |
| 0F.3 | `Cloud Readiness Accelerator Reusable Enterprise Multi-Cloud Assessment Framework.pptx` | Compare with V1 and V1.1; archive if superseded | Likely earliest draft | ⬜ Not Started |
| 0F.4 | `Azure AMM - Delivery Guide.pptx` | Move to `presentations/alliance/azure-amm-delivery-guide.pptx` | Microsoft partner reference — keep | ⬜ Not Started |
| 0F.5 | `RXT Microsoft Funding Interactive Enablement (Sellers + SAs PODs)_January 2026 [SHARED].pptx` | Move to `presentations/alliance/rxt-microsoft-funding-enablement-jan2026.pptx` | Rackspace × Microsoft co-sell enablement | ⬜ Not Started |

### 0G. Examples — Anonymize & Repackage as Reference Cases

> The Examples folder has real engagement data with mixed sensitivity. Goal: keep useful financial benchmarks, remove all identifiable customer info.

| # | File | Action | Status |
|---|---|---|---|
| 0G.1 | `Examples/AWS Example/MPA Pricing Frankfurt - Full Scope.xlsx` | Anonymize customer refs → rename to `aws-mpa-pricing-example-region-1.xlsx`; move to `examples/aws/` | ⬜ Not Started |
| 0G.2 | `Examples/AWS Example/MPA Pricing Ireland - Full Scope.xlsx` | Same pattern → `aws-mpa-pricing-example-region-2.xlsx` | ⬜ Not Started |
| 0G.3 | `Examples/AWS Example/MPA Pricing London - Full Scope.xlsx` | Same pattern → `aws-mpa-pricing-example-region-3.xlsx` | ⬜ Not Started |
| 0G.4 | `Examples/AWS Example/MPA Pricing Ireland - Full Scope no DB.xlsx` | `aws-mpa-pricing-no-db-region-2.xlsx` | ⬜ Not Started |
| 0G.5 | `Examples/AWS Example/MPA Pricing London - Full Scope no DB.xlsx` | `aws-mpa-pricing-no-db-region-3.xlsx` | ⬜ Not Started |
| 0G.6 | `Examples/AWS Example/business_case_lift_and_shift.pptx` | Rename `aws-business-case-lift-shift-example.pptx`; check for customer names | ⬜ Not Started |
| 0G.7 | `Examples/AWS Example/business_case_DB_refactoring.pptx` | Rename `aws-business-case-db-refactoring-example.pptx`; check for customer names | ⬜ Not Started |
| 0G.8 | `Examples/AWS Example/Storage Assessment Business Case V2...pptx` | Rename `aws-storage-assessment-business-case-example.pptx`; check for customer names | ⬜ Not Started |
| 0G.9 | `Examples/Azure Example -1/*.xlsx` (10 files) | Rename to `azure-assessment-[scenario]-example.xlsx` format; verify no customer names in tabs | ⬜ Not Started |
| 0G.10 | `Examples/Azure Example -2/` (all 4 files) | **BLOCKED** — do not touch until 0A.1–0A.4 complete; sensitive files must be removed first | 🔴 Blocked |

### 0H. Project Plan & SOW Files at Root

| # | File | Action | Status |
|---|---|---|---|
| 0H.1 | `Cloud_Readiness_Assessment_Project_Plan.xlsx` | Move to `docs/reference/cra-project-plan-template.xlsx` — useful as project plan template | ⬜ Not Started |
| 0H.2 | `Cloud_Readiness_Assessment_SoW.docx` | Move to `templates/04-planning/sow-template.docx` — use as generic SOW template | ⬜ Not Started |

---

## EPIC 1: Repository Restructure & Cleanup

**Goal:** Reorganize GitHub repo to enterprise-grade structure  
**Target:** Release 1.0 *(example: dd/mm/yy — Week 4 from project start)*

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 1.1 | Fix git remote: point to `upendra25312/Cloud-Readiness-accelearator` | ⭐ High | Upendra | 🟢 Complete | Remote corrected and verified |
| 1.2 | Resolve git index.lock from stale background process | ⭐ High | Upendra | 🟢 Complete | Resolved by creating fresh inner `.git` |
| 1.3 | Stage and commit all local files in one clean commit | ⭐ High | Upendra | 🟢 Complete | Initial commit — all framework files staged |
| 1.4 | Force-push to `upendra25312/Cloud-Readiness-accelearator` main branch | ⭐ High | Upendra | 🟢 Complete | Force-pushed to establish clean history |
| 1.5 | Execute Epic 0 file triage: remove sensitive files, delete meta-files, rename templates | ⭐ High | Upendra | ⬜ Not Started | See Epic 0 — prerequisite for all further sharing |
| 1.6 | Create target folder structure: `docs/`, `templates/`, `presentations/`, `examples/`, `tools/` | ⭐ High | Upendra | ⬜ Not Started | Per PLAN.md Section 4.1 and Epic 0D |
| 1.7 | Move templates to phase-based subfolders (Epic 0E tasks) | Medium | Upendra | ⬜ Not Started | Depends on 1.6 |
| 1.8 | Move phase guides to `docs/guides/` (Epic 0D tasks) | Medium | Upendra | ⬜ Not Started | Depends on 1.6 |
| 1.9 | Move integration + customization guides to `docs/integration/` and `docs/customization/` | Medium | Upendra | ⬜ Not Started | Depends on 1.6 |
| 1.10 | Commit all restructuring changes and push to GitHub | ⭐ High | Upendra | ⬜ Not Started | Final clean commit after Epic 0 complete |

---

## EPIC 2: Executive README & Branding

**Goal:** Create VP/Director-quality README and apply Rackspace branding  
**Target:** Release 1.0 *(example: dd/mm/yy — Week 4 from project start)*

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 2.1 | Rewrite README.md to VP/Director standard (see PRD FR-50) | ⭐ High | Upendra | ⬜ Not Started | Reference: AWS professional-services, Azure CAF repos |
| 2.2 | Add Rackspace logo SVG badge to README header | ⭐ High | Upendra | ⬜ Not Started | Download from brand.rackspace.com |
| 2.3 | Fix all GitHub badge URLs to point to `upendra25312/Cloud-Readiness-accelearator` | ⭐ High | Upendra | ⬜ Not Started | Currently pointing to wrong repo |
| 2.4 | Add "Quick Decision Guide: SMART vs. CRA" section to README | High | Upendra | ⬜ Not Started | See PLAN.md Section 2.3 |
| 2.5 | Update CONTRIBUTING.md with clear contribution guidelines | Medium | Upendra | ⬜ Not Started | |
| 2.6 | Create SECURITY.md (security disclosure policy) | Medium | Upendra | ⬜ Not Started | |
| 2.7 | Update CHANGELOG.md with v1.0, v1.1, v2.0 release history | Medium | Upendra | ⬜ Not Started | |
| 2.8 | Apply Rackspace color scheme (#E31C3D) to all PPTX presentations | ⭐ High | Upendra | ⬜ Not Started | Executive Overview deck priority |
| 2.9 | Add Rackspace logo to all PPTX title slides and footers | ⭐ High | Upendra | ⬜ Not Started | |
| 2.10 | Review all docs for internal jargon — replace with external-facing language | High | Upendra | ⬜ Not Started | |

---

## EPIC 3: Core Methodology & Documentation

**Goal:** Ensure methodology docs are complete, accurate, and peer-reviewed  
**Target:** Release 1.0 *(example: dd/mm/yy — Week 4 from project start)*

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 3.1 | Peer-review `docs/METHODOLOGY.md` — validate phase durations against DMG experience | ⭐ High | Upendra | ⬜ Not Started | DMG took longer than guide estimates |
| 3.2 | Update phase duration estimates to reflect real-world ranges (not optimistic) | High | Upendra | ⬜ Not Started | METHODOLOGY.md already has v2 note |
| 3.3 | Add "When to Use This Framework" decision tree to methodology | High | Upendra | ⬜ Not Started | SMART vs CRA vs DIY |
| 3.4 | Create `docs/MICROSOFT-CAF-ALIGNMENT.md` | Medium | Upendra | ⬜ Not Started | Maps CRA phases to CAF stages |
| 3.5 | Create `docs/AWS-MAP-ALIGNMENT.md` | Medium | Upendra | ⬜ Not Started | Maps CRA to AWS MAP phases |
| 3.6 | Create `docs/GOOGLE-PSO-ALIGNMENT.md` | Medium | Upendra | ⬜ Not Started | Maps CRA to Google Cloud migration framework |
| 3.7 | Review all four phase guides (Discovery, Analysis, Evaluation, Planning) | High | Upendra | ⬜ Not Started | |
| 3.8 | Add "SOW template" section to Planning Phase guide | High | Upendra | ⬜ Not Started | Leverage DMG SOW as reference |

---

## EPIC 4: Templates — Audit, Complete & Standardize

**Goal:** 30+ production-quality templates that cover every deliverable a real CRA engagement requires (per SOW analysis)  
**Target:** Release 1.1 *(example: dd/mm/yy — Week 12 from project start)*

> **SOW-derived requirements:** A complete CRA engagement must produce: TCO Analysis (7 layers), Hyperscaler Recommendation with weighted scoring, Part 2 Entry Point, Cloud Maturity & Gap Assessment, Executive Report, Executive Presentation, Infrastructure Discovery Summary. Every template below maps to one of these deliverables.

### 4A. Discovery Phase Templates (Phase 1)

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 4A.1 | Audit `Application Scoping & Profiling - template.xlsx` — verify it captures: app name, owner, tech stack, dependencies, VM count, DB type, licensing, cloud readiness score | ⭐ High | Upendra | ⬜ Not Started | SOW: estate exceeded expected scope — template must scale to 200+ apps |
| 4A.2 | Audit `Infrastructure-Profiling-Template.xlsx` — verify it captures: server count, CPU/RAM/storage, OS, hypervisor, region/DC location, network segments | ⭐ High | Upendra | ⬜ Not Started | SOW: all original VM/DB/storage caps exceeded — template must handle this gracefully |
| 4A.3 | Audit `Dependency-Mapping-Template.xlsx` — verify it can represent app-to-app and app-to-infra dependencies | High | Upendra | ⬜ Not Started | SOW: full network dependency mapping is Part 2 — but high-level dependency view is Part 1 |
| 4A.4 | Create `templates/01-discovery/saas-application-assessment.xlsx` — track SaaS applications separately (vendor, contract, renewal, migration path) | Medium | Upendra | ⬜ Not Started | SOW: SaaS workshop was a separate workstream; SaaS apps have different migration patterns |
| 4A.5 | Add instructions tab to all Discovery templates explaining: who fills it in, when, what "good data" looks like | ⭐ High | Upendra | ⬜ Not Started | See Epic 10.4 — data quality directly impacts TCO accuracy |

### 4B. TCO Analysis Templates (Phase 3) — SOW Critical Path

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 4B.1 | Validate TCO templates cover all 7 SOW-required layers: (a) L4L baseline, (b) Optimised/rightsized, (c) Delta, (d) Licensing overlay (SQL/SA + Oracle + BYOL), (e) On-prem status quo, (f) Year 1 forecast (dual-running), (g) Partner discounts/credits | ⭐ High | Upendra | ⬜ Not Started | **Most critical gap** — current templates may not cover all 7 layers |
| 4B.2 | Validate `Azure-Evaluation-Template.xlsx` produces: PAYG and 3-year RI pricing side-by-side, per region | ⭐ High | Upendra | ⬜ Not Started | SOW: Azure L4L largely done — validate template matches this approach |
| 4B.3 | Validate `AWS-Evaluation-Template.xlsx` produces: On-Demand + 3-year RI + Savings Plans, per region | ⭐ High | Upendra | ⬜ Not Started | SOW: AWS was last to complete — template must handle multi-region |
| 4B.4 | Validate `GCP-Evaluation-Template.xlsx` produces: On-Demand + 3-year CUD, per region | ⭐ High | Upendra | ⬜ Not Started | SOW: GCP largely done |
| 4B.5 | Add on-premises status quo tab to `Business-Case-Template.xlsx` — captures current hardware, maintenance, licensing, facilities costs | ⭐ High | Upendra | ⬜ Not Started | SOW: on-prem baseline was a major risk item; template must make it easy to populate |
| 4B.6 | Add Year 1 dual-running forecast tab to `Business-Case-Template.xlsx` — models overlap period costs | High | Upendra | ⬜ Not Started | SOW: Year 1 forecast is a named SOW deliverable |
| 4B.7 | Add licensing overlay tab to TCO template: SQL Server (AHB vs BYOL vs PAYG), Oracle (BYOL, EA), third-party | ⭐ High | Upendra | ⬜ Not Started | SOW: Oracle licensing flagged as "significant cost, core to the estate" |
| 4B.8 | Add partner commercial overlay tab: AWS MAP credits, Azure AMM credits, GCP migration credits | High | Upendra | ⬜ Not Started | SOW: partner discounts/credits are a named deliverable layer |
| 4B.9 | Validate TCO models against current Azure/AWS/GCP pricing (rates current at time of validation) | ⭐ High | Upendra | ⬜ Not Started | Reference Examples/AWS Example/ MPA files and Examples/Azure Example -1/ files |

### 4C. Hyperscaler Recommendation Templates (Phase 3)

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 4C.1 | Audit `Hyperscaler-Decision-Matrix-Template.xlsx` — verify it produces a weighted estate-level score across all 3 clouds with a clear primary recommendation output | ⭐ High | Upendra | ⬜ Not Started | SOW: scoring consolidation was Lead Architect's primary deliverable |
| 4C.2 | Add a "7Rs Estate View" tab to the Hyperscaler matrix — flags apps as: Rehost / Replatform / Rearchitect / Repurchase (SaaS) / Retire / Retain / Relocate | High | Upendra | ⬜ Not Started | SOW: 7Rs view is a named deliverable — "not detailed, but flags areas of value and complexity" |
| 4C.3 | Add worked example to `Hyperscaler-Decision-Matrix-Template.xlsx` using anonymized DMG scoring | ⭐ High | Upendra | ⬜ Not Started | Architects need to see what a completed matrix looks like |
| 4C.4 | Add a "multi-cloud exceptions" worksheet: apps that cannot move to primary cloud and why | Medium | Upendra | ⬜ Not Started | SOW: small number of exceptions = primary platform + multi-cloud element |

### 4D. Reporting & Executive Presentation Templates

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 4D.1 | Audit `Cloud_Readiness_Assessment_Report_Template_v3_Audited.docx` — verify section structure matches SOW: Exec summary → Infrastructure summary → TCO (all layers) → Hyperscaler scoring → Recommendation → Risk register → Part 2 entry point | ⭐ High | Upendra | ⬜ Not Started | SOW: "Evidence before recommendation" principle must be reflected in structure |
| 4D.2 | Add a "board-extractable executive narrative" section to the report template — 1-page standalone summary the CTO can lift directly for their board | ⭐ High | Upendra | ⬜ Not Started | SOW explicitly calls out: "executive narrative extractable for the DMG CTO to extract for his board" |
| 4D.3 | Create `templates/executive-reporting/part2-entry-point-template.docx` — scope, phases, indicative cost ranges, hyperscaler funding (MAP/AMM/PSO), Oracle modernisation section, next steps | ⭐ High | Upendra | ⬜ Not Started | SOW: Part 2 entry point is a named critical-path deliverable; no template exists for this |
| 4D.4 | Audit `Cloud_Readiness_Assessment_Executive_Summary_Template_v3_Audited.pptx` — verify it follows "evidence before recommendation" slide flow; has CSP comparison slide; has recommendation slide with clear rationale | ⭐ High | Upendra | ⬜ Not Started | SOW: presentation is for CTO/board playback |
| 4D.5 | Create `templates/04-planning/sow-template.docx` — generic, reusable SOW for CRA Part 1 engagements; based on DMG SOW fully anonymized | ⭐ High | Upendra | ⬜ Not Started | SOW: use DMG document as the reference; strip all customer names |

### 4E. Cloud Maturity & Governance Templates

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 4E.1 | Audit `CRA - LITE Governance Foundations Alignment Tool - Template.xlsx` against SOW cloud maturity requirements | High | Upendra | ⬜ Not Started | SOW: cloud maturity workshop was a named supporting deliverable |
| 4E.2 | Audit `Risk-Assessment-Template.xlsx` — ensure it includes: technical risks, dependency risks, licensing risks (Oracle), data risks, timeline risks | High | Upendra | ⬜ Not Started | SOW: risk assessment is a supporting deliverable |
| 4E.3 | Create Governance Model template with RACI matrix (delivery roles: Lead Architect, Platform Architects, PM, Pre-Sales, Delivery Director, Practice Lead) | Medium | Upendra | ⬜ Not Started | SOW governance model is a clear reference for what roles CRA engagements need |
| 4E.4 | Apply Rackspace branding (#E31C3D, logo, Aktiv Grotesk) to all PPTX and DOCX templates | High | Upendra | ⬜ Not Started | Must complete before any external sharing |

---

## EPIC 5: Executive Presentations

**Goal:** VP/CIO-presentable decks ready for customer and partner briefings  
**Target:** Release 1.1 *(example: dd/mm/yy — Week 12 from project start)*

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 5.1 | Create `presentations/executive/CRA-Leadership-Overview.pptx` using Rackspace PowerPoint template | ⭐ High | Upendra | ⬜ Not Started | **Primary artifact for leadership meeting** — use official Rackspace PPTX template from brand.rackspace.com |
| 5.2 | Slide structure for leadership deck (12 slides max): 1-Problem Statement, 2-Market Opportunity, 3-What is CRA, 4-Four-Phase Framework, 5-SMART vs CRA Decision Guide, 6-Template Library Overview, 7-Reference Engagement (anonymized), 8-Business Value (30% faster delivery), 9-Alliance Partner Alignment, 10-Roadmap, 11-Investment Ask, 12-CTA / Next Steps | ⭐ High | Upendra | ⬜ Not Started | Designed for 20-min leadership briefing slot |
| 5.3 | Add business value stats to deck: delivery time reduction %, average deal size, pipeline influenced | ⭐ High | Upendra | ⬜ Not Started | Quantify the ask — VPs need numbers |
| 5.4 | Create `presentations/executive/CRA-Executive-Overview.pptx` (15 slides, customer-facing) | Medium | Upendra | ⬜ Not Started | For VP/CIO audience at customer organizations |
| 5.5 | Create `presentations/technical/CRA-Technical-Overview.pptx` (25–30 slides, architect-level) | Medium | Upendra | ⬜ Not Started | For solution architects and delivery leads |
| 5.6 | Create `presentations/alliance/CRA-Microsoft-Partner-Deck.pptx` | Medium | Upendra | ⬜ Not Started | SMART + CAF alignment; co-brandable |
| 5.7 | Create `presentations/alliance/CRA-AWS-Partner-Deck.pptx` | Medium | Upendra | ⬜ Not Started | MAP alignment; deal registration guide |
| 5.8 | Create `presentations/alliance/CRA-GCP-Partner-Deck.pptx` | Medium | Upendra | ⬜ Not Started | PSO alignment; Migration Center integration |
| 5.9 | Director-level review of leadership deck (5.1) before first presentation | ⭐ High | TBD Director | ⬜ Not Started | **Hard gate — do not present without this review** |
| 5.10 | Present CRA accelerator in leadership meeting; capture feedback | ⭐ High | Upendra | ⬜ Not Started | Target: next scheduled leadership sync after Release 1.0 |

---

## EPIC 6: Reference Case Study (Media & Entertainment)

**Goal:** Anonymized end-to-end example from DMG engagement  
**Target:** Release 1.1 *(example: dd/mm/yy — Week 12 from project start)*

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 6.1 | Review DMG engagement data for anonymization requirements | ⭐ High | Upendra | ⬜ Not Started | Legal review may be needed |
| 6.2 | Create anonymized customer profile (size, industry, scope) | ⭐ High | Upendra | ⬜ Not Started | Call them "Global Media Co." or similar |
| 6.3 | Anonymize all financial data (keep ratios/percentages, remove absolutes) | ⭐ High | Upendra | ⬜ Not Started | |
| 6.4 | Document assessment approach used for the engagement | High | Upendra | ⬜ Not Started | Map to CRA phases |
| 6.5 | Document key findings and recommendations | High | Upendra | ⬜ Not Started | |
| 6.6 | Document outcomes (scope reduction, TCO savings, selected hyperscaler, etc.) | High | Upendra | ⬜ Not Started | |
| 6.7 | Create 5-page case study document (docx + pptx version) | High | Upendra | ⬜ Not Started | |
| 6.8 | Legal/compliance review of case study before publication | ⭐ High | Legal/TBD | ⬜ Not Started | **Hard gate before publishing** |

---

## EPIC 7: GitHub Publication & Hygiene

**Goal:** Professional public GitHub repo ready for partner and customer sharing  
**Target:** Release 1.0 *(example: dd/mm/yy — Week 4 from project start)*

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 7.1 | Set repo description: "Enterprise cloud readiness accelerator by Rackspace Technology" | High | Upendra | ⬜ Not Started | |
| 7.2 | Set repo topics/tags: `cloud-readiness`, `azure`, `aws`, `gcp`, `rackspace`, `migration` | High | Upendra | ⬜ Not Started | |
| 7.3 | Enable GitHub Discussions | Low | Upendra | ⬜ Not Started | Community engagement |
| 7.4 | Add GitHub Issue templates (bug report, feature request, content update) | Low | Upendra | ⬜ Not Started | |
| 7.5 | Set up GitHub Actions: markdown lint workflow | Low | Upendra | ⬜ Not Started | |
| 7.6 | Scan all files for sensitive data before final push | ⭐ High | Upendra | ⬜ Not Started | PII, pricing, internal names |
| 7.7 | Create GitHub Release v1.0 with release notes | Medium | Upendra | ⬜ Not Started | |
| 7.8 | Share repo link with Microsoft Partner team | High | Upendra | ⬜ Not Started | After Legal review |
| 7.9 | Share repo link with AWS Partner team | High | Upendra | ⬜ Not Started | After Legal review |
| 7.10 | Share repo link with GCP Partner team | High | Upendra | ⬜ Not Started | After Legal review |

---

## EPIC 8: Alliance Partner Alignment

**Goal:** Position CRA as a tool that supports co-sell with Microsoft, AWS, and Google  
**Target:** Release 2.0 *(example: dd/mm/yy — Week 24 from project start)*

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 8.1 | Map CRA phases to Microsoft CAF stages (Strategy, Plan, Ready, Migrate, Govern, Manage) | High | Upendra | ⬜ Not Started | |
| 8.2 | Map CRA to AWS MAP phases (Assess, Mobilize, Migrate & Modernize) | High | Upendra | ⬜ Not Started | |
| 8.3 | Map CRA to Google Cloud Adoption Framework | High | Upendra | ⬜ Not Started | |
| 8.4 | Document how CRA outputs support Microsoft AMM funding request | High | Upendra | ⬜ Not Started | |
| 8.5 | Document how CRA outputs support AWS MAP deal registration | High | Upendra | ⬜ Not Started | |
| 8.6 | Validate CRA with Microsoft Partner team (1 review session) | High | Upendra | ⬜ Not Started | |
| 8.7 | Validate CRA with AWS Partner team (1 review session) | Medium | Upendra | ⬜ Not Started | |
| 8.8 | Validate CRA with GCP Partner team (1 review session) | Medium | Upendra | ⬜ Not Started | |

---

## EPIC 9: Internal Enablement

**Goal:** Rackspace delivery teams can use the CRA framework with minimal ramp-up  
**Target:** Release 2.0 *(example: dd/mm/yy — Week 24 from project start)*

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 9.1 | Create 30-min onboarding guide for new architects | High | Upendra | ⬜ Not Started | Must be self-contained; no prior CRA context needed |
| 9.2 | Create SharePoint site with full template library | High | Upendra | ⬜ Not Started | Internal use — includes confidential versions with customer examples |
| 9.3 | Run 1 internal workshop with SA team (3 hours) | High | Upendra | ⬜ Not Started | Hands-on template walkthrough |
| 9.4 | Publish CRA to Rackspace partner portal | Medium | Upendra | ⬜ Not Started | Requires partner portal access |
| 9.5 | Create "lessons learned" document from DMG engagement | High | Upendra | ⬜ Not Started | Feed back into framework methodology |

---

## EPIC 10: Self-Explanatory Design & Usability

**Goal:** Any cloud architect or cloud engineer who picks up the CRA framework for the first time can understand, navigate, and start using it within 2 hours — with no prior briefing needed.  
**Why:** A framework that requires tribal knowledge defeats its own purpose. It must be as intuitive as an AWS or Microsoft professional services tool.  
**Target:** Release 1.0 *(example: dd/mm/yy — Week 4 from project start)* — usability is a gate for any sharing

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 10.1 | Write a `START-HERE.md` file at repo root: 5-minute guide explaining what CRA is, who uses it, and the 4 key files to open first | ⭐ High | Upendra | ⬜ Not Started | Replace all current "start here" meta-files with one definitive guide |
| 10.2 | Add numbered `README.md` sections: "If you are a Cloud Architect…", "If you are a Delivery Manager…", "If you are a VP/Director…" — link each persona to their entry point | ⭐ High | Upendra | ⬜ Not Started | Removes cognitive load: each reader immediately knows where to go |
| 10.3 | Add a visual framework map (ASCII or embedded diagram) to README showing the 4 phases, their templates, and their outputs | ⭐ High | Upendra | ⬜ Not Started | One-glance orientation for a new reader |
| 10.4 | Add an "Instructions" tab to every Excel template with: purpose, who fills it in, when in the engagement, step-by-step instructions | ⭐ High | Upendra | ⬜ Not Started | Makes templates self-contained; no guide needed |
| 10.5 | Add a cover slide to every PPTX template with: purpose, audience, when to use, what to customize | High | Upendra | ⬜ Not Started | Architects should not need to guess what a deck is for |
| 10.6 | Add a header block to every DOCX template with: document purpose, target audience, phase it belongs to, estimated time to complete | High | Upendra | ⬜ Not Started | Standard header prevents misuse of templates |
| 10.7 | Ensure all folder names are self-explanatory: `01-discovery/`, `02-analysis/` etc. — no internal codes or abbreviations | ⭐ High | Upendra | ⬜ Not Started | Naming convention must be intuitive without a legend |
| 10.8 | Add a one-paragraph description at the top of every markdown guide file explaining its scope, target reader, and how it connects to the next step | High | Upendra | ⬜ Not Started | First paragraph answers "should I be reading this?" |
| 10.9 | Add an "Example output" section to each phase guide showing what the deliverables look like at the end of that phase | High | Upendra | ⬜ Not Started | Engineers are visual learners — show, don't tell |
| 10.10 | Conduct a "cold start" usability test: ask a Rackspace architect who has NOT seen the framework to open the repo and start Phase 1 — observe where they get stuck | ⭐ High | Upendra | ⬜ Not Started | Target: before Release 1.0; fix every sticking point found |

---

## Milestone Schedule

> **Note:** All dates below are illustrative examples in dd/mm/yy format. Replace with your actual project calendar dates at engagement start. Week numbers are relative to project kick-off.

| Milestone | Example Target Date | Relative Timing | Gate Criteria |
| --- | --- | --- | --- |
| **Epic 0 complete** (sensitive files removed, meta-files deleted) | **dd/mm/yy** | Week 2 from kick-off | No sensitive files on GitHub; root is clean |
| **Release 1.0** (repo restructured, README rewritten, branding applied) | **dd/mm/yy** | Week 4 from kick-off | VP can open GitHub link and understand it in 5 minutes |
| **Leadership Presentation** (deck 5.1 ready) | **dd/mm/yy** | Week 6–8 from kick-off | Director-reviewed; numbers validated |
| **Release 1.1** (worked examples, scoring tool, exec overview deck) | **dd/mm/yy** | Week 12 from kick-off | Alliance partners can use independently |
| **Release 2.0** (co-sell decks, enablement, SharePoint) | **dd/mm/yy** | Week 24 from kick-off | Microsoft/AWS/GCP partner teams validated |

---

## Immediate Next Steps (First 2 Weeks)

> Replace "Day N" with actual calendar dates in dd/mm/yy format at engagement start.

| Priority | Action | Owner | Due |
|---|---|---|---|
| 1 | Complete Epic 0A tasks: remove sensitive customer files from GitHub repo | Lead Architect | Day 5 *(dd/mm/yy)* |
| 2 | Complete Epic 0B: delete all GITHUB-*.md, SHAREPOINT-*.md, EXECUTE-*.sh meta-files from root | Lead Architect | Day 5 *(dd/mm/yy)* |
| 3 | Rename GITHUB-CHANGELOG.md → CHANGELOG.md, GITHUB-CONTRIBUTING.md → CONTRIBUTING.md (Epic 0C) | Lead Architect | Day 10 *(dd/mm/yy)* |
| 4 | Start Epic 10.1: write new self-explanatory `START-HERE.md` | Lead Architect | Day 10 *(dd/mm/yy)* |
| 5 | Send CLOUD-READINESS-ACCELERATOR-PLAN.md and PRD.md to Practice Director for review | PM | Day 5 *(dd/mm/yy)* |
| 6 | Download official Rackspace PowerPoint template; begin leadership deck (Epic 5.1) | Lead Architect | Day 14 *(dd/mm/yy)* |

---

## Progress Summary

> Last updated: 2026-06-02

| Epic | Total Tasks | Complete | In Progress | Not Started | % Done |
|---|---|---|---|---|---|
| 0A. Sensitive & Customer-Data Files | 11 | 9 | 0 | 2 | 82% |
| 0B. Operational Meta-Files | 16 | 16 | 0 | 0 | 100% |
| 0C. GitHub Standard Files | 6 | 6 | 0 | 0 | 100% |
| 0D. Framework Content Reorganize | 14 | 14 | 0 | 0 | 100% |
| 0E. Templates Rename & Reorganize | 26 | 24 | 0 | 2 | 92% |
| 0F. Presentations | 5 | 5 | 0 | 0 | 100% |
| 0G. Examples Anonymize | 10 | 9 | 0 | 1 | 90% |
| 0H. Project Plan & SOW | 2 | 2 | 0 | 0 | 100% |
| 1. Repository Restructure | 10 | 10 | 0 | 0 | 100% |
| 2. README & Branding | 10 | 4 | 0 | 6 | 40% |
| 3. Methodology Docs | 8 | 0 | 0 | 8 | 0% |
| 4A. Discovery Phase Templates | 5 | 0 | 0 | 5 | 0% |
| 4B. TCO Analysis Templates (SOW critical) | 9 | 0 | 0 | 9 | 0% |
| 4C. Hyperscaler Recommendation Templates | 4 | 0 | 0 | 4 | 0% |
| 4D. Reporting & Executive Presentation | 5 | 0 | 0 | 5 | 0% |
| 4E. Cloud Maturity & Governance Templates | 4 | 0 | 0 | 4 | 0% |
| 5. Executive Presentations | 10 | 0 | 0 | 10 | 0% |
| 6. Case Study | 8 | 0 | 0 | 8 | 0% |
| 7. GitHub Publication | 10 | 3 | 0 | 7 | 30% |
| 8. Alliance Alignment | 8 | 0 | 0 | 8 | 0% |
| 9. Internal Enablement | 5 | 0 | 0 | 5 | 0% |
| 10. Self-Explanatory Design | 10 | 5 | 0 | 5 | 50% |
| **TOTAL** | **186** | **107** | **0** | **79** | **58%** |

### Remaining Release 1.0 Gates

| # | Task | Blocker |
| --- | --- | --- |
| 0E.18 | Debrand `Templates/executive-reporting/cra-executive-summary-template.pptx` content | Manual — open in PowerPoint |
| 0E.19 | Debrand `Templates/executive-reporting/cra-phase1-report-template.docx` content | Manual — open in Word |
| 0G.10 | Review `Examples/Azure Example -2/Hyperscaler_Decision_Matrix_Microsoft_Completed.xlsx` for anonymization | Manual review |
| 2.2 | Add Rackspace logo SVG badge to README | Requires logo URL from brand.rackspace.com |
| 2.8/2.9 | Apply Rackspace branding to PPTX presentations | Manual — open in PowerPoint |
| 7.6 | Sensitive-data scan before public sharing | Run before any external link-sharing |

---

*Document Owner: Rackspace Cloud Solutions Architecture Team*  
*Last Updated: dd/mm/yy — v1.1 (audited by expert team: Azure Architect, Sr. PM, Alliance SA, Senior Director)*  
*© 2026 Rackspace Technology. All rights reserved.*
