# Cloud Readiness Accelerator — Product Requirements Document (PRD)

**Version:** 1.0  
**Date:** June 2026  
**Product Owner:** Rackspace Technology — Cloud Solutions Architecture  
**Audience:** VP / Director Level | Product | Delivery | Alliance Partners  
**Status:** DRAFT FOR REVIEW

---

## 1. Problem Statement

### 1.1 The Core Problem

Rackspace professional services teams currently build cloud readiness assessments **from scratch for every engagement**. This results in:

- **Inconsistent quality** — deliverable quality depends on the individual architect, not a standard
- **Long scoping cycles** — 4–6 weeks to scope an engagement that should take 1 week
- **Missed opportunities** — partners cannot pre-qualify or fund engagements without structured assessment artifacts
- **No institutional memory** — insights from completed assessments don't feed back into future ones
- **Competitive disadvantage** — AWS, Microsoft, and Google all have structured assessment programs; Rackspace relies on individual talent

### 1.2 The Opportunity

A **reusable, professional-grade Cloud Readiness Accelerator** will:

1. Reduce assessment delivery time by **30–40%**
2. Increase consistency and quality to **VP/CIO-presentable standard**
3. Unlock **Microsoft AMM, AWS MAP, and Google PSO** funding for qualifying engagements
4. Create a **differentiating market asset** that can be shared, referenced, and co-branded with alliance partners
5. Enable **junior architects to deliver senior-quality assessments** using the framework

---

## 2. Goals & Non-Goals

### 2.1 Goals (In Scope)

| # | Goal | Success Criterion |
|---|---|---|
| G1 | Deliver a complete, reusable assessment framework | 30+ templates, 4 phase guides, 3 hyperscaler evaluation models |
| G2 | Executive-quality presentation layer | Rackspace-branded decks presentable to VP/CIO with no modification |
| G3 | Multi-cloud vendor neutrality | Equal depth for AWS, Azure, and GCP; no hyperscaler bias |
| G4 | Alliance partner compatibility | Framework maps to Microsoft CAF, AWS MAP, and Google Cloud Adoption Framework |
| G5 | Open-source GitHub presence | Public repo, enterprise-grade structure, 500+ stars target |
| G6 | Delivery team enablement | Delivery team can execute an engagement using the framework with <2 days of training |
| G7 | Reference case study | One anonymized end-to-end example (media industry) demonstrating framework output |

### 2.2 Non-Goals (Out of Scope)

- Building a SaaS product or web application
- Replacing Microsoft SMART, AWS MAP, or Google Migration Center
- Automated cloud migration execution (framework covers assessment and planning only)
- Proprietary customer data storage
- Replacing Rackspace's existing SOW or commercial processes

---

## 3. User Personas

### Persona 1: Rackspace Cloud Solutions Architect (Primary User)
> *"I need a structured toolkit to consistently deliver high-quality assessments regardless of my personal experience level with a specific industry or cloud provider."*

- **Profile:** 3–10 years cloud architecture experience; AWS/Azure/GCP certified; works on 3–5 active engagements
- **Pain points:** Rebuilding similar documents for each engagement; inconsistent quality vs. peers; limited financial modeling skills
- **Needs:** Phase guides, templates, worked examples, financial calculators

### Persona 2: Rackspace Practice/Delivery Manager (Buyer & Approver)
> *"I need confidence that our assessment deliverables are executive-quality before they go to the customer's CIO."*

- **Profile:** 10+ years; manages a portfolio of CRA engagements; accountable for delivery quality and margins
- **Pain points:** Quality variance across team; scope creep; re-work cycles
- **Needs:** Quality checklist, milestone sign-off templates, executive reporting

### Persona 3: VP / Director, Customer Organization (End Recipient)
> *"I need a credible, clear recommendation I can take to my board to justify a $5M cloud migration investment."*

- **Profile:** C-1 or C-2 level; financial and risk-focused; not technical; 30-minute attention window
- **Pain points:** Inconsistent quality from vendors; lack of financial justification; unclear risk picture
- **Needs:** Executive summary, financial business case, risk register, recommended hyperscaler

### Persona 4: Microsoft / AWS / GCP Alliance Partner (Co-Sell Partner)
> *"I need to know this assessment is aligned with our frameworks so I can register a co-sell deal and potentially unlock customer funding."*

- **Profile:** Partner Sales/SA at Microsoft, AWS, or Google; manages Rackspace as a strategic partner
- **Pain points:** Rackspace not using structured programs; difficulty registering deals; no shared artifacts
- **Needs:** CAF/MAP/PSO alignment mapping, co-branded deck option, deal registration data

---

## 4. Functional Requirements

### 4.1 Methodology & Phase Guides

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | Framework shall include a four-phase methodology document: Discovery, Analysis, Evaluation, Planning | Must Have |
| FR-02 | Each phase shall have an entry criteria, exit criteria, activities list, and deliverables table | Must Have |
| FR-03 | Phase durations shall include minimum, typical, and maximum estimates | Must Have |
| FR-04 | Phase guides shall include resource requirements by team role | Must Have |
| FR-05 | Methodology shall map to Microsoft CAF stages, AWS MAP phases, and Google Cloud Migration Framework | Should Have |

### 4.2 Templates

| ID | Requirement | Priority |
|---|---|---|
| FR-10 | Discovery templates: application inventory (xlsx), infrastructure profiling (xlsx), dependency mapping (xlsx) | Must Have |
| FR-11 | Analysis templates: readiness scoring matrix (5 dimensions × 5 levels) (xlsx) | Must Have |
| FR-12 | Evaluation templates: hyperscaler decision matrix AWS/Azure/GCP (xlsx), TCO comparison model (xlsx) | Must Have |
| FR-13 | Planning templates: migration wave planner (xlsx), risk register (xlsx), governance model (xlsx) | Must Have |
| FR-14 | Reporting templates: executive summary (pptx), technical assessment report (docx) | Must Have |
| FR-15 | All templates shall include worked examples pre-populated with anonymized reference data | Should Have |
| FR-16 | Templates shall include user guidance / instructions tab or section | Should Have |

### 4.3 Presentations & Executive Artifacts

| ID | Requirement | Priority |
|---|---|---|
| FR-20 | Executive Overview deck (pptx): 15 slides max; designed for VP/CIO; Rackspace branded | Must Have |
| FR-21 | Technical Methodology deck (pptx): 25–30 slides; designed for solution architects | Should Have |
| FR-22 | Alliance Partner Co-sell deck (pptx): co-brandable; maps CRA to partner programs | Should Have |
| FR-23 | Customer Assessment Report template (docx): 30–50 pages; section for each phase | Must Have |
| FR-24 | Business Case Template (pptx + docx): TCO, ROI, NPV; board-presentable | Must Have |

### 4.4 Examples & Case Studies

| ID | Requirement | Priority |
|---|---|---|
| FR-30 | One end-to-end reference case study (media/entertainment industry, anonymized) | Must Have |
| FR-31 | Case study shall include: scope, approach, findings, recommendations, outcomes | Must Have |
| FR-32 | Financial outputs from case study shall use real-world benchmarks (anonymized) | Should Have |
| FR-33 | Generic enterprise reference case (50–200 application scope) | Should Have |

### 4.5 Tools & Calculators

| ID | Requirement | Priority |
|---|---|---|
| FR-40 | Readiness Scoring Tool: auto-calculates 5-dimension score; outputs radar chart | Must Have |
| FR-41 | TCO Calculator: side-by-side AWS / Azure / GCP; includes RI/CUD/SP discounts | Must Have |
| FR-42 | Migration Wave Planner: priority scoring matrix; outputs sequenced wave plan | Should Have |
| FR-43 | All tools shall work in Microsoft Excel (no special software required) | Must Have |

### 4.6 GitHub Repository

| ID | Requirement | Priority |
|---|---|---|
| FR-50 | Repository shall have a professional README with: overview, quick start, structure, contributing | Must Have |
| FR-51 | Repository structure shall follow the target folder hierarchy defined in Section 4.4 of the Plan | Must Have |
| FR-52 | All markdown files shall use consistent heading hierarchy, tables, and formatting | Must Have |
| FR-53 | CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, CHANGELOG.md shall be present | Should Have |
| FR-54 | GitHub Actions workflows: lint markdown, validate links | Nice to Have |
| FR-55 | Repository shall contain no customer PII, internal Rackspace pricing, or confidential data | Must Have |

---

## 5. Non-Functional Requirements

### 5.1 Quality

| NFR | Requirement |
|---|---|
| NFR-01 | All deliverables must be peer-reviewed by at least one Sr. Cloud Architect before publishing |
| NFR-02 | All financial models must be validated against at least one real engagement |
| NFR-03 | Executive presentations must be reviewed by a Practice Director before release |
| NFR-04 | Language must be free of internal Rackspace jargon; accessible to external VP/Director audience |

### 5.2 Branding

| NFR | Requirement |
|---|---|
| NFR-10 | All PPTX files must use Rackspace Red (#E31C3D) as primary accent color |
| NFR-11 | Rackspace logo must appear on title slide and footer of all presentation artifacts |
| NFR-12 | GitHub README must include Rackspace logo/badge and reference to Rackspace Technology |
| NFR-13 | Font: Aktiv Grotesk (or Inter as fallback) for all presentations |

### 5.3 Usability

| NFR | Requirement |
|---|---|
| NFR-20 | A new Rackspace architect should be able to start a CRA engagement using the framework with <2 days of onboarding |
| NFR-21 | Each template must be self-contained — usable without reading the full methodology |
| NFR-22 | Executive summary template should require <4 hours to populate per engagement |

### 5.4 Maintainability

| NFR | Requirement |
|---|---|
| NFR-30 | All documents must include a version number and last-reviewed date in the header |
| NFR-31 | Framework must be reviewed and updated quarterly (driven by cloud service changes) |
| NFR-32 | GitHub repo must use semantic versioning for framework releases (v1.0, v1.1, etc.) |

---

## 6. Content Requirements

### 6.1 Assessment Coverage Matrix

| Assessment Area | Discovery | Analysis | Evaluation | Planning |
|---|:---:|:---:|:---:|:---:|
| Application inventory & profiling | ✅ | | | |
| Infrastructure inventory | ✅ | | | |
| Dependency mapping | ✅ | | | |
| Technical readiness scoring | | ✅ | | |
| Operational readiness scoring | | ✅ | | |
| Security & compliance scoring | | ✅ | | |
| Business readiness scoring | | ✅ | | |
| Financial readiness scoring | | ✅ | | |
| AWS service mapping & TCO | | | ✅ | |
| Azure service mapping & TCO | | | ✅ | |
| GCP service mapping & TCO | | | ✅ | |
| Hyperscaler decision matrix | | | ✅ | |
| Business case (ROI/NPV) | | | ✅ | |
| Risk register | | | ✅ | |
| Migration wave plan | | | | ✅ |
| Resource & skills plan | | | | ✅ |
| Governance model | | | | ✅ |
| Executive roadmap | | | | ✅ |

### 6.2 Cloud Provider Coverage Balance

Each hyperscaler section must include:
- Service mapping (IaaS, PaaS, data, AI/ML, networking, security)
- Pricing model explanation (on-demand, reserved, savings plans/committed use)
- TCO estimation methodology
- Migration pathway (lift-and-shift → optimize → modernize)
- Key differentiators vs. other providers
- Rackspace managed services offerings on that platform

---

## 7. Release Strategy

### Release 1.0 — Foundation (Target: 4 weeks)
Deliverables: Reorganized GitHub repo + Rackspace-branded README + Core methodology docs + All templates (existing, cleaned and branded)

### Release 1.1 — Enrichment (Target: 12 weeks)
Deliverables: Worked examples + Interactive scoring tool + Business case template + Executive Overview deck v2

### Release 2.0 — Scale (Target: 24 weeks)
Deliverables: Alliance partner co-sell decks + SMART integration guide + Video walkthroughs + SharePoint publication + Training materials

---

## 8. Dependencies & Constraints

| # | Dependency / Constraint |
|---|---|
| D1 | Rackspace brand guidelines approval required before distributing externally |
| D2 | Legal review required for any customer data included in examples (even anonymized) |
| D3 | Alliance partner co-sell decks require NDA / joint-marketing agreement review |
| D4 | Microsoft SMART integration requires Microsoft Partner Network (MPN) account access |
| D5 | AWS MAP alignment requires AWS Partner Central account and validated practice area |

---

## 9. Approval & Sign-Off

| Role | Name | Date | Status |
|---|---|---|---|
| Product Owner | Upendra Kumar | June 2026 | In Review |
| Director, Cloud Solutions Architecture | TBD | | Pending |
| VP, Professional Services | TBD | | Pending |
| Alliance Partner Lead (Microsoft) | TBD | | Pending |
| Alliance Partner Lead (AWS) | TBD | | Pending |

---

*Document Owner: Rackspace Cloud Solutions Architecture Team*  
*Next Review: September 2026*  
*© 2026 Rackspace Technology. All rights reserved.*
