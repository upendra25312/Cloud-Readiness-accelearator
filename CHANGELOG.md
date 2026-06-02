# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2026-06-02

### Changed

- Reorganized all templates into phase-based subfolders: `01-discovery/`, `02-analysis/`, `03-evaluation/`, `04-planning/`, `executive-reporting/`
- Reorganized all phase guides and reference docs into structured `docs/` subdirectories (`guides/`, `integration/`, `customization/`, `governance/`, `reference/`)
- Moved executive and alliance presentations into `presentations/executive/` and `presentations/alliance/`
- Renamed all example files to anonymized, consistent naming conventions (`aws-mpa-pricing-example-region-{n}.xlsx`, `azure-assessment-{pricing-model}-{region}.xlsx`)
- Moved examples into clean subfolders: `Examples/aws/` and `Examples/azure/`
- Moved project plan template to `docs/reference/cra-project-plan-template.xlsx`
- Moved SOW template to `Templates/04-planning/sow-template.docx`
- Complete rewrite of `README.md` — professional director-grade overview with accurate file paths, working links, and phase-based template table
- Updated `START-HERE.md` — all links corrected to new file locations
- Root directory reduced to 14 items — framework content only, no working-notes clutter

### Removed

- All operational meta-files from root (`GITHUB-*.md`, `SHAREPOINT-*.md`, `EXECUTE-*.sh`, session artifacts)
- Empty folders: `Integration-Guides/`, `Customization-Guides/`, `Quality-Assurance/`
- `QUICK-START-GUIDE.md`, `START-GITHUB-PUBLICATION.md` — superseded by `START-HERE.md` and `README.md`

### Security

- `.gitignore` updated to exclude all sensitive customer files and local tool configurations
- All customer-identifying filenames removed from public-facing file paths
- `_internal-only/` folder established for session artifacts and partner-specific files

---

## [1.0.0] - 2026-05-08

### Added

- Initial release of the Cloud Readiness Accelerator framework
- Four-phase assessment methodology: Discovery → Analysis → Evaluation → Planning
- 24+ reusable assessment templates covering every major CRA deliverable
- 5-dimensional readiness scoring model: Technical, Operational, Security, Financial, Business
- Multi-cloud evaluation framework supporting AWS, Azure, and Google Cloud
- Financial analysis templates: TCO, ROI, NPV, payback period, on-premises vs cloud
- Risk and compliance assessment framework
- Dependency mapping and migration wave planning templates
- Enterprise governance and stakeholder management templates
- Phase guides for all four phases
- Integration guides: CMDB, monitoring tools, cloud assessment tools
- Customization guides: industry verticals, organisation size adaptation
- Executive reporting templates: full assessment report and executive summary deck
- Alliance partner alignment: Microsoft CAF/AMM, AWS MAP, Google PSO
- Reference examples: AWS MPA pricing (3 regions), Azure Migrate assessments (PAYG and RI)
- `START-HERE.md` — 5-minute framework orientation
- `docs/METHODOLOGY.md` — complete four-phase methodology with entry/exit criteria
- Community contribution guidelines (`CONTRIBUTING.md`)
- MIT License

---

## Future Releases

See [ROADMAP.md](ROADMAP.md) for planned features and improvements.
