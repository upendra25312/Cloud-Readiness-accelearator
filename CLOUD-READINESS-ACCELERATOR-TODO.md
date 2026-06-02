# Cloud Readiness Accelerator — To-Do Tracker

**Version:** 1.0  
**Date:** June 2026  
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

## EPIC 1: Repository Restructure & Cleanup

**Goal:** Reorganize GitHub repo to enterprise-grade structure  
**Target:** Release 1.0 (Week 4)

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 1.1 | Fix git remote: point to `upendra25312/Cloud-Readiness-accelearator` | ⭐ High | Upendra | 🟡 In Progress | Lock file issue — background task running |
| 1.2 | Resolve git index.lock from stale background process | ⭐ High | Upendra | 🟡 In Progress | Waiting for lock to clear |
| 1.3 | Stage and commit all local files in one clean commit | ⭐ High | Upendra | ⬜ Not Started | Depends on 1.2 |
| 1.4 | Force-push to `upendra25312/Cloud-Readiness-accelearator` main branch | ⭐ High | Upendra | ⬜ Not Started | Depends on 1.3 |
| 1.5 | Create new folder structure: `docs/`, `templates/`, `presentations/`, `examples/`, `tools/`, `guides/` | Medium | Upendra | ⬜ Not Started | Per PLAN.md Section 4.1 |
| 1.6 | Move 60+ operational/meta markdown files to `_archive/` or delete | Medium | Upendra | ⬜ Not Started | Files like EXECUTE-GITHUB-PUBLICATION.sh, FINAL-SUMMARY.md etc. |
| 1.7 | Move existing templates to `templates/01-discovery/`, `templates/02-analysis/`, etc. | Medium | Upendra | ⬜ Not Started | |
| 1.8 | Move phase guides to `docs/guides/` | Medium | Upendra | ⬜ Not Started | |
| 1.9 | Move integration guides to `docs/integration/` | Low | Upendra | ⬜ Not Started | |
| 1.10 | Move examples to `examples/media-entertainment/` | Medium | Upendra | ⬜ Not Started | Anonymize before moving |

---

## EPIC 2: Executive README & Branding

**Goal:** Create VP/Director-quality README and apply Rackspace branding  
**Target:** Release 1.0 (Week 4)

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
**Target:** Release 1.0 (Week 4)

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

**Goal:** 30+ production-quality templates ready for use on real engagements  
**Target:** Release 1.1 (Week 12)

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 4.1 | Audit all existing templates in `Templates/` folder | ⭐ High | Upendra | ⬜ Not Started | Check completeness, branding, worked examples |
| 4.2 | Add instructions tab/page to all Excel templates | High | Upendra | ⬜ Not Started | |
| 4.3 | Add worked example data to Readiness Scoring template (anonymized) | ⭐ High | Upendra | ⬜ Not Started | Use DMG data anonymized |
| 4.4 | Add worked example data to Hyperscaler Decision Matrix (anonymized) | ⭐ High | Upendra | ⬜ Not Started | Use DMG data anonymized |
| 4.5 | Validate TCO models against real Azure/AWS/GCP pricing (June 2026 rates) | ⭐ High | Upendra | ⬜ Not Started | Check MPA pricing files in Examples/ |
| 4.6 | Add 3-Year RI / Savings Plans / CUD scenarios to TCO models | High | Upendra | ⬜ Not Started | |
| 4.7 | Create `templates/04-planning/SOW-Template.docx` (generic, reusable) | ⭐ High | Upendra | ⬜ Not Started | Based on DMG SOW — fully anonymized |
| 4.8 | Create Governance Model template with RACI matrix | Medium | Upendra | ⬜ Not Started | |
| 4.9 | Create Migration Wave Planning template with dependency visualization | Medium | Upendra | ⬜ Not Started | |
| 4.10 | Apply Rackspace branding to all PPTX and DOCX templates | High | Upendra | ⬜ Not Started | |

---

## EPIC 5: Executive Presentations

**Goal:** VP/CIO-presentable decks ready for customer and partner briefings  
**Target:** Release 1.1 (Week 12)

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 5.1 | Create `presentations/executive/CRA-Executive-Overview.pptx` (15 slides) | ⭐ High | Upendra | ⬜ Not Started | Primary artifact for VP/Director audience |
| 5.2 | Slide structure: Problem → Solution → Framework → ROI → Case Study → CTA | High | Upendra | ⬜ Not Started | |
| 5.3 | Add business value stats: delivery time reduction, cost savings, deal size | High | Upendra | ⬜ Not Started | |
| 5.4 | Create `presentations/technical/CRA-Technical-Overview.pptx` (25–30 slides) | Medium | Upendra | ⬜ Not Started | For architect-level audience |
| 5.5 | Create `presentations/alliance/CRA-Microsoft-Partner-Deck.pptx` | Medium | Upendra | ⬜ Not Started | SMART + CAF alignment mapping |
| 5.6 | Create `presentations/alliance/CRA-AWS-Partner-Deck.pptx` | Medium | Upendra | ⬜ Not Started | MAP alignment |
| 5.7 | Create `presentations/alliance/CRA-GCP-Partner-Deck.pptx` | Medium | Upendra | ⬜ Not Started | PSO alignment |
| 5.8 | Director-level review of Executive Overview deck before publication | ⭐ High | TBD Director | ⬜ Not Started | **Gate for external sharing** |

---

## EPIC 6: Reference Case Study (Media & Entertainment)

**Goal:** Anonymized end-to-end example from DMG engagement  
**Target:** Release 1.1 (Week 12)

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
**Target:** Release 1.0 (Week 4)

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
**Target:** Release 2.0 (Week 24)

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
**Target:** Release 2.0 (Week 24)

| # | Task | Priority | Owner | Status | Notes |
|---|---|---|---|---|---|
| 9.1 | Create 30-min onboarding guide for new architects | High | Upendra | ⬜ Not Started | |
| 9.2 | Create SharePoint site with full template library | High | Upendra | ⬜ Not Started | Internal use (includes confidential versions) |
| 9.3 | Run 1 internal workshop with SA team (3 hours) | High | Upendra | ⬜ Not Started | Hands-on template walkthrough |
| 9.4 | Publish CRA to Rackspace partner portal | Medium | Upendra | ⬜ Not Started | |
| 9.5 | Create "lessons learned" document from DMG engagement | High | Upendra | ⬜ Not Started | Feed back into framework |

---

## Immediate Next Steps (This Week)

| Priority | Action | Owner |
|---|---|---|
| 1 | Resolve git lock issue and push all local files to GitHub | Upendra |
| 2 | Review and clean up repo structure (archive meta files) | Upendra |
| 3 | Update README.md badges to point to correct repo | Upendra |
| 4 | Send PLAN.md and PRD.md to Practice Director for review | Upendra |
| 5 | Schedule review call with Microsoft Partner team | Upendra |

---

## Progress Summary

| Epic | Total Tasks | Complete | In Progress | Not Started | % Done |
|---|---|---|---|---|---|
| 1. Repository Restructure | 10 | 0 | 2 | 8 | 0% |
| 2. README & Branding | 10 | 0 | 0 | 10 | 0% |
| 3. Methodology Docs | 8 | 0 | 0 | 8 | 0% |
| 4. Templates | 10 | 0 | 0 | 10 | 0% |
| 5. Executive Presentations | 8 | 0 | 0 | 8 | 0% |
| 6. Case Study | 8 | 0 | 0 | 8 | 0% |
| 7. GitHub Publication | 10 | 0 | 0 | 10 | 0% |
| 8. Alliance Alignment | 8 | 0 | 0 | 8 | 0% |
| 9. Internal Enablement | 5 | 0 | 0 | 5 | 0% |
| **TOTAL** | **77** | **0** | **2** | **75** | **3%** |

---

*Document Owner: Rackspace Cloud Solutions Architecture Team*  
*Last Updated: June 2026*  
*© 2026 Rackspace Technology. All rights reserved.*
