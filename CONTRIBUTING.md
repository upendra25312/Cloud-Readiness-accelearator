# Contributing to Cloud Readiness Accelerator

The CRA framework improves through contributions from practitioners who have used it in the field. This document explains what kinds of contributions are needed and how to submit them.

---

## What We Welcome

| Contribution Type | Examples |
| --- | --- |
| **New or improved templates** | Better application scoping worksheets, updated TCO models, improved scoring criteria |
| **Anonymized examples** | Real-engagement outputs with all customer identifiers removed |
| **Phase guide improvements** | Lessons learned, corrected estimates, additional context for complex scenarios |
| **Methodology refinements** | Updated phase durations, new readiness dimensions, edge-case handling |
| **Alliance alignment docs** | Mappings to CAF, MAP, PSO, or new co-sell programme requirements |
| **Bug reports** | Broken links, formula errors in Excel templates, incorrect instructions |

---

## Quality Standards

Every contribution must meet the following before it will be merged:

- **Executive-readable**: No internal jargon. A VP reading a template for the first time must understand its purpose.
- **Cloud-neutral**: If the contribution covers a single hyperscaler, label it clearly. Templates covering all scenarios must have AWS, Azure, and GCP sections.
- **Peer-reviewed**: Add a `v[N]-audited` suffix to the filename when a peer has reviewed it (e.g. `readiness-scoring-v2-audited.xlsx`).
- **Versioned**: Include a semantic version in the document header (e.g. `Version: 2.1`).
- **No customer data**: All examples must be fully anonymized. Replace customer names with `[Client]`, financial figures with representative ranges, and remove any identifying infrastructure details.

---

## How to Contribute

### For template updates and doc improvements

1. Fork the repository
2. Create a branch: `git checkout -b contribution/your-description`
3. Make your changes following the naming conventions below
4. Submit a Pull Request with:
   - What changed and why (link to issue if applicable)
   - Which engagement or scenario surfaced the need
   - Confirmation that no customer data is included

### For anonymized examples

1. Place the file in the appropriate `Examples/` subfolder (`aws/`, `azure/`, or `media-entertainment/`)
2. Add a row to the case study markdown (or create a new one) explaining what the file demonstrates
3. Confirm you have removed or replaced all customer-identifying information
4. Submit a Pull Request with a short description of the engagement context (industry, scale, hyperscaler selected)

### For bug reports

Open an issue using the [Content Update template](.github/ISSUE_TEMPLATE/) with:

- Which file has the error
- What the error is
- What the correct content should be

---

## Naming Conventions

| Artifact type | Convention | Example |
| --- | --- | --- |
| Excel templates | `kebab-case-description-v[N].xlsx` | `readiness-scoring-v2.xlsx` |
| Word/DOCX templates | `kebab-case-description-v[N].docx` | `sow-template-v3.docx` |
| PPTX presentations | `CRA-[Audience]-[Topic]-v[N].pptx` | `CRA-Executive-Overview-v1.pptx` |
| Markdown guides | `NN-kebab-case-description.md` | `01-discovery-phase-guide.md` |
| Example files | Prefix with source context where useful | `azure-payg-lkl-uk-south.xlsx` |

---

## Folder Structure

Place contributions in the correct folder:

```text
Templates/01-discovery/        ← Application inventory, infra profiling
Templates/02-analysis/         ← Readiness scoring, governance
Templates/03-evaluation/       ← TCO models, hyperscaler decision matrix
Templates/04-planning/         ← Migration waves, risk register, SOW
Templates/executive-reporting/ ← Assessment report and exec summary templates
Examples/aws/                  ← AWS pricing and business case examples
Examples/azure/                ← Azure assessment examples
Examples/media-entertainment/  ← DMG Media UK case study and supporting files
docs/guides/                   ← Phase delivery guides
docs/integration/              ← CMDB and tooling integration guides
presentations/executive/       ← CIO/VP-ready decks
presentations/alliance/        ← Partner-aligned decks
```

---

## Review Process

1. A maintainer will review your PR within 5 business days
2. Feedback will be provided inline on the PR
3. Once all comments are addressed, the contribution will be merged
4. Significant additions will be noted in [CHANGELOG.md](CHANGELOG.md)

---

## Security

Never include customer names, financial figures, infrastructure IP addresses, or credentials in contributions. If you are unsure whether something is sensitive, remove it. See [SECURITY.md](SECURITY.md) for the security disclosure policy.

---

## Questions

Open a [GitHub Discussion](https://github.com/upendra25312/Cloud-Readiness-accelearator/discussions) or raise an issue using the Question template.

---

Cloud Readiness Accelerator — Rackspace Technology
