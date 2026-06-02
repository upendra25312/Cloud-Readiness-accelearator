# CRA Internal Enablement Workshop — Agenda & Facilitator Guide

**Who should read this:** The practice lead or senior architect running the CRA enablement workshop.  
**What this covers:** Full workshop agenda, facilitator notes, exercises, and Q&A guide for a 3-hour internal session with the Rackspace Solutions Architecture team.  
**Audience:** Rackspace Cloud Architects and Solutions Engineers who will deliver CRA engagements.  
**Format:** 3 hours, in-person or Teams; works for groups of 4–12 architects.

> **Epic 9.3 — Internal SA Enablement Workshop**  
> Run this workshop before the first new architect-led CRA engagement. Target: all architects who have not yet delivered a CRA independently. Minimum group size: 4 (learning is peer-driven in the exercises).

---

## Workshop Objectives

By the end of this workshop, each participant can:

1. **Explain** the CRA four-phase methodology to a customer in 5 minutes
2. **Navigate** the template library and find the right template for any phase
3. **Recognise** the nine common failure modes (from DMG lessons learned)
4. **Complete** a Phase 1 kickoff checklist for a mock customer
5. **Identify** when to escalate to Oracle practice, Alliance Manager, or Pre-Sales

---

## Pre-Workshop Preparation (Facilitator)

Complete these actions before the workshop:

- [ ] Share `docs/guides/00-architect-onboarding-guide.md` with all participants 48 hours before — ask them to read Part 1 (Framework Overview) only
- [ ] Confirm SharePoint site is set up and participants have access (or use GitHub repo as backup)
- [ ] Print or share the SMART vs CRA Decision Guide (from README)
- [ ] Open `Templates/01-discovery/application-scoping-profiling.xlsx` on a projector/screen for the template demo
- [ ] Prepare mock customer scenario (see Exercise 2 below)
- [ ] Book 3-hour slot; break at 90 minutes; end with 30-min Q&A

---

## Workshop Agenda (3 Hours)

| Time | Section | Format | Duration |
| --- | --- | --- | --- |
| 0:00 | Welcome & Objectives | Facilitator presentation | 5 min |
| 0:05 | Part 1: What is CRA and Why Does It Exist | Presentation | 20 min |
| 0:25 | Part 2: The Four Phases — Deep Dive | Presentation + discussion | 30 min |
| 0:55 | Exercise 1: Phase Navigation Challenge | Group exercise | 15 min |
| 1:10 | Part 3: Template Library Walkthrough | Live demo | 20 min |
| 1:30 | **BREAK** | | 10 min |
| 1:40 | Part 4: DMG Media UK Lessons Learned | Facilitator storytelling | 25 min |
| 2:05 | Exercise 2: Mock Phase 1 Kickoff | Pairs exercise | 30 min |
| 2:35 | Part 5: Alliance Partners and Funding | Presentation | 15 min |
| 2:50 | Q&A and Next Steps | Open discussion | 30 min |
| 3:20 | Close | | 5 min |

---

## Part 1: What is CRA and Why Does It Exist (20 min)

### Facilitator Notes

Open with the business context — not the methodology. Start with the problem:

> "A mid-market enterprise with 200–500 VMs wants to move to cloud. They have a Microsoft SE, an AWS SA, and a GCP CE all telling them different things. They don't have time to run three separate evaluations. They don't have the internal skills to know which cloud is right for their specific estate. That's the gap CRA fills."

**Key points to make:**

1. **CRA is a commercial accelerator**, not just a methodology. It enables Rackspace to win Part 2 migration engagements by being the most credible technical advisor in Phase 1.

2. **The average CRA deal size:** ~£80K–£120K for Part 1. The Part 2 migration (what Part 1 leads to) is the real commercial outcome: $650K+ average deal size.

3. **CRA is infrastructure-agnostic.** It doesn't pre-select a cloud. It produces evidence that leads to a defensible recommendation. If the data says AWS, we recommend AWS.

4. **Three things make CRA different from a generic cloud assessment:**
   - The 7-layer TCO model (most assessments only do Layer a and b — we do all 7)
   - Alliance partner funding identification (AMM/MAP/PSO — this is the Rackspace commercial differentiator)
   - The DMG Media UK reference engagement — we have a live, complete example

**Show this slide/diagram:** Four-phase ASCII diagram from `docs/guides/00-architect-onboarding-guide.md`

**Pause for questions:** 3 minutes

---

## Part 2: The Four Phases — Deep Dive (30 min)

### Phase 1: Discovery (7 weeks)

**Key message:** Phase 1 is a data quality project. Everything in Phase 3 is only as accurate as the data collected in Phase 1.

**Critical facts to communicate:**
- Discovery tooling (Azure Migrate / GCP Migration Center / AWS ADS) requires firewall changes — submit the CAB request on **Day 1**, not when the appliance is deployed (DMG Lesson 2)
- Target: ≥14 days of clean CPU/RAM/storage/network utilisation data from ≥90% of VMs
- The utilisation data gate is non-negotiable — Phase 3 cannot start without it (DMG Lesson 6)
- Oracle RAC in Phase 1 inventory → escalate to Oracle practice immediately (DMG Lesson 3)
- Phase 2 can start at Phase 1 Week 6 — do not wait for Phase 1 to finish (DMG Lesson 7)

**Show:** `Templates/01-discovery/application-scoping-profiling.xlsx` — walk through the key columns

**Discussion question (2 min):** "When in Phase 1 would you flag Oracle workloads to the practice team? Why not wait until Phase 3 when you're doing TCO?"

### Phase 2: Analysis (4 weeks)

**Key message:** Phase 2 is about interpreting the Phase 1 data — not collecting more data.

**Critical facts:**
- Starts at Phase 1 Week 6 (parallelised)
- Output is a readiness score per application: Cloud Ready / Cloud Friendly / Cloud Challenged / Blocked
- Governance workshop happens here — 2–3 hours with the customer's IT Director
- Redis OSS, Elasticsearch, HashiCorp Vault: flag these for commercial licence review (DMG Lesson 4)

**Show:** `Templates/02-analysis/cloud-readiness-scoring-v2.xlsx`

### Phase 3: Evaluation (3 weeks)

**Key message:** Phase 3 produces the evidence. The recommendation is the conclusion of that evidence — not the starting point.

**Critical facts:**
- "Evidence before recommendation" — always. Recommendation comes after the TCO and scoring matrix, never before (DMG Lesson 9)
- TCO has 7 layers — most engagement only do 2. Layers (d)(e)(f)(g) are where the compelling numbers are: licensing overlay, on-prem status quo, Year 1 dual-running, partner credits
- The hyperscaler weighting must be agreed with the customer before scoring begins — this prevents "you rigged it for Azure" challenges
- AMM/MAP/PSO deal registration: start this in Phase 1 kickoff (DMG Lesson 5)

**Show:** `Templates/03-evaluation/TCO-TEMPLATES-AUDIT-SPEC.md` — the 7 layers diagram

### Phase 4: Planning (6 weeks)

**Key message:** Phase 4 turns evidence into a signed Part 2 SOW. Everything we do in Phase 4 is commercial — it is a sales document as much as a technical document.

**Critical facts:**
- The Part 2 Entry Point document is the single most important output
- Alliance partner deal registration must be complete before Rackspace countersigns Part 2 SOW
- Wave plan: Wave 0 is a PoC (non-production, 5–10% of estate, low complexity). Do not put Tier-1 apps in Wave 0.

**Show:** `Templates/executive-reporting/part2-entry-point-template-CONTENT.md`

---

## Exercise 1: Phase Navigation Challenge (15 min)

### Setup

Divide participants into pairs. Each pair receives a scenario card (below). They must answer:
1. "Which phase are you in?"
2. "Which template do you open?"
3. "What is the first action?"

Allow 8 minutes to discuss, then 7 minutes of group readback.

### Scenario Cards

**Card A:**
> You've just completed the infrastructure profiling scan. You have 3,847 VMs in the inventory. You have 6 days of CPU/RAM data. The customer's commercial director is asking you to "move to Phase 3 and start the numbers" because the board presentation is in 3 weeks.
>
> **What do you say and do?**
>
> *(Answer: You are in Phase 1. You need ≥14 days of data before Phase 3 starts. Show the customer the financial risk in writing: "TCO built on 6 days of data has ±30–50% accuracy — the business case could be off by £Xm." Open infrastructure-profiling.xlsx, Data Quality Summary tab, show the Phase 3 Ready? column.)*

**Card B:**
> In the application scoping spreadsheet, you find 23 rows flagged as "Oracle Database." Four of them are listed as Oracle RAC clusters. You're in Phase 1, Week 2. Your next customer meeting is the Phase 1 status call, tomorrow morning.
>
> **What do you do before the status call and what do you say on it?**
>
> *(Answer: Escalate to Oracle Practice Lead immediately — today, not after Phase 2. Email the Oracle Practice Lead with the count and version numbers. On the status call: "We've identified Oracle RAC in your estate. We're engaging our Oracle practice specialist to ensure the licensing analysis is accurate — this typically takes 4 weeks so we're starting now.")*

**Card C:**
> You're preparing the Phase 3 executive playback deck. A colleague has built the slide deck and the recommendation slide ("Microsoft Azure — Primary Cloud") is on slide 4 of 18. The evidence slides (TCO, scoring matrix) are on slides 12–15.
>
> **What do you do and why?**
>
> *(Answer: Restructure the deck. The recommendation must come after the evidence. Move the recommendation to slide 13 or later. Reason: if the recommendation appears before the evidence, the customer will conclude the recommendation was pre-determined and the evidence was constructed to justify it. This destroys credibility. Reference: DMG Lesson 9.)*

**Card D:**
> The customer has asked you to include their AWS account manager in the Phase 3 hyperscaler evaluation review. You're recommending Azure. The customer is asking "should AWS be at the meeting?"
>
> **What is your answer and your approach?**
>
> *(Answer: Yes — invite all three hyperscaler SEs to the Phase 3 review. This demonstrates the evaluation was objective. All three clouds should be represented equally in the comparison slides. Never invite only the recommended hyperscaler to the playback — it signals pre-determination.)*

---

## Part 3: Template Library Walkthrough (20 min, live demo)

### Facilitator Setup

Screen share or project `Templates/` directory. Walk through in phase order.

### Walkthrough Script

**"There are 30+ templates across 5 folders. You don't need to know all of them. You need to know the 8 critical ones."**

| Priority | Template | Why It's Critical |
| --- | --- | --- |
| 1 | `01-discovery/application-scoping-profiling.xlsx` | Master inventory; everything downstream depends on it |
| 2 | `01-discovery/infrastructure-profiling.xlsx` | VM data; feeds every TCO model |
| 3 | `02-analysis/cloud-readiness-scoring-v2.xlsx` | Readiness profile; the Phase 2 headline output |
| 4 | `03-evaluation/business-case-tco-roi.xlsx` | 7-layer TCO; the Phase 3 commercial output |
| 5 | `03-evaluation/hyperscaler-decision-matrix.xlsx` | The recommendation engine |
| 6 | `04-planning/migration-wave-planner.xlsx` | The Part 2 scope document |
| 7 | `04-planning/risk-assessment.xlsx` | Delivery governance + customer assurance |
| 8 | `executive-reporting/part2-entry-point-template` (DOCX) | The commercial handoff to Part 2 |

**Live demo sequence:**
1. Open `application-scoping-profiling.xlsx` — point out the Instructions tab; show the Oracle Practice Flag column; show the Scope Confidence dropdown
2. Open `infrastructure-profiling.xlsx` — show the Phase 3 Ready? calculated column; show the Data Quality Summary tab
3. Open `hyperscaler-decision-matrix.xlsx` — show the Criteria & Weights tab; point out the Worked Example tab
4. Show `Templates/03-evaluation/TCO-TEMPLATES-AUDIT-SPEC.md` — the 7-layer checklist

**Key message:** Every template has an Instructions tab. If you're not sure what a template is for or how to fill it in — read the Instructions tab first.

---

## Part 4: DMG Media UK Lessons Learned (25 min)

### Facilitator Approach

Tell this as a story, not a presentation. Use first-person plural ("we").

> "Let me walk you through what actually happened in our most recent CRA engagement. This is DMG Media UK — the Daily Mail Group Trust. A 4,000-VM, two-data-centre, 280-application estate. 18 Oracle RAC clusters. 140+ Redis instances. And a 57% scope variance."

Walk through the 9 lessons from `docs/DMG-MEDIA-UK-LESSONS-LEARNED.md`. Spend the most time on:
- Lesson 1 (scope variance) — "We scoped at 2,700 VMs. We assessed 4,212. That's why the SOW now has a scope variance clause."
- Lesson 6 (utilisation gate) — "There was genuine internal pressure to skip the data collection window. We didn't. Here's how we held the line."
- Lesson 9 (evidence before recommendation) — "We had to restructure the deck after customer feedback. Here's what we learned."

**Key question for group discussion (5 min):**
> "Which of these 9 lessons would have been hardest to push back on with your customer? What would you have said?"

---

## Exercise 2: Mock Phase 1 Kickoff (30 min)

### Setup

Pairs exercise. One person plays the Rackspace Lead Architect. The other plays the Customer IT Director.

### Mock Customer Scenario

> **Customer:** RetailCo PLC — UK mid-market retailer  
> **Estate (claimed):** 800 VMs, 1 data centre, 80 applications  
> **Key facts you know:**
> - Customer has an Oracle EBS ERP system (mission critical)
> - Their CMDB was last updated 14 months ago
> - They have a Microsoft EA including Windows Server + SQL Server
> - The CTO wants to see the Phase 3 playback in 10 weeks  
> - Their IT Manager says "we should be able to get the firewall changes done in a few days"

**Task for the Lead Architect role:**
Conduct a 10-minute Phase 1 kickoff with the Customer IT Director. Cover:
1. Scope estimate validation — "We want to cross-reference your 800-VM estimate..."
2. Discovery tooling and firewall timing — "We'll need outbound port 443..."
3. Oracle escalation — "We noticed Oracle EBS in your application list..."
4. Utilisation data gate — "Phase 3 will require at least 14 days of data..."
5. Alliance partner pre-registration — "We'll reach out to our Microsoft Alliance Manager today..."

**Task for the Customer IT Director role:**
Play realistic pushback on:
- "10 weeks is fine, let's not overthink the data collection"
- "Our IT team will handle the firewall — it shouldn't take long"
- "The Oracle ERP is stable, I don't think we need specialist review yet"

**Debrief (10 min):**
- What did the Lead Architect handle well?
- Where did they hesitate or back down when they shouldn't?
- What language worked well for pushing back on the timeline pressure?

---

## Part 5: Alliance Partners and Funding (15 min)

### Key Points

1. **Why this matters commercially:** The Alliance Manager pre-registering an AMM/MAP/PSO opportunity in Phase 1 is worth £800K–£1.2M in funded services (DMG example). This is a Rackspace differentiator — Microsoft and AWS SEs cannot do this for the customer.

2. **Quick decision table:**

| If primary cloud is | Programme | Register by | Portal |
| --- | --- | --- | --- |
| Azure | AMM (Azure Migration and Modernisation) | Phase 1 kickoff | MSPP Partner Center |
| AWS | MAP (Migration Acceleration Programme) | Phase 1 kickoff | AWS Partner Central |
| GCP | PSO Credits + RAMP | Phase 2 | Google Partner Advantage |
| Any | Multiple eligibility possible | Discuss with Alliance Manager | — |

3. **The one rule:** Alliance Manager must be on the Phase 1 kickoff call. Not "briefed after." On the call.

4. **What to say to the customer:** "As part of this engagement, we'll be identifying partner funding programmes you may be eligible for. This typically covers 10–30% of the Part 2 migration services cost. We'll pre-register the opportunity this week and confirm eligibility before Phase 3."

### Q&A prompts for this section

- "What happens if the customer already has a direct relationship with Microsoft and is registered in MPN?"
- "Can we register for AMM and MAP at the same time if the customer might go with either cloud?"
- "What if the Alliance Manager says the customer doesn't qualify?"

---

## Q&A and Next Steps (30 min)

### Facilitator Questions to Open Discussion

Use these if the group is quiet:

1. "What was the most surprising thing you learned today that you didn't know before?"
2. "Which template do you think will take the most time to fill in on a real engagement? What would help?"
3. "Where do you think the most common failure point is in a CRA engagement — Phase 1, 2, 3, or 4?"
4. "If you started a CRA engagement next Monday, what would be the first three things you'd do on Day 1?"

### Next Steps to Communicate

| Action | Owner | Timing |
| --- | --- | --- |
| Read the full onboarding guide (`00-architect-onboarding-guide.md`) | All participants | This week |
| Open one template from each phase and read the Instructions tab | All participants | This week |
| Identify the next CRA opportunity in your pipeline | All participants | 2 weeks |
| Shadow the next CRA Phase 1 kickoff | New architects (first CRA) | When scheduled |
| Run this workshop again after next engagement — add 1 new lesson | Facilitator | After next engagement |

---

## Facilitator Debrief Checklist

After the workshop, confirm:

- [ ] All participants can name the two hard gates (utilisation data gate + AMM registration gate)
- [ ] All participants know the Oracle practice escalation trigger (any Oracle RAC/EE in Phase 1 inventory)
- [ ] All participants have navigated to the Template Library (SharePoint or GitHub) during the session
- [ ] At least one participant has volunteered to be the "buddy" for the next new architect doing their first CRA
- [ ] Post a summary of key lessons in the CRA Teams channel

---

*CRA Framework v2.0 — Internal Enablement Resources — Rackspace Cloud Solutions Architecture*
