# Contributing to the Cloud Readiness Accelerator

Thank you for contributing to this project! This accelerator is a living, practitioner-maintained toolkit. Contributions from cloud architects, engineers, and practitioners at Microsoft, AWS, Google Cloud, and partner organizations are welcome.

---

## How to Contribute

### 1. Reporting Issues

Found outdated content, a broken link, or incorrect guidance? Please open a GitHub Issue with:
- File path and line number (if applicable)
- Description of the issue
- Suggested correction or improvement

### 2. Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-improvement`
3. Make your changes following the [Style Guide](#style-guide) below
4. Commit with a clear message: `git commit -m "Update Azure WAF pillars to 2024 guidance"`
5. Push and open a Pull Request against `main`
6. Request review from at least one other cloud architect

### 3. Content Additions

New content areas welcome:
- Industry-specific cloud readiness guides (Financial Services, Healthcare, Government, Retail)
- Additional cloud provider frameworks (Oracle Cloud, IBM Cloud)
- Terraform / Bicep / CDK reference implementations
- Architecture decision records (ADRs)
- Customer case studies (anonymized)

---

## Style Guide

### Document Structure
- Use Markdown (`.md`) for all documents
- Begin each document with a metadata header (Version, Authors, Aligned To)
- Use H2 (`##`) for major sections, H3 (`###`) for subsections
- Use tables for comparative content (cloud provider comparisons, control matrices)
- Use code blocks (` ``` `) for architecture diagrams, commands, and configurations

### Accuracy Standards
- All cloud service names must be current and correctly capitalized (e.g., "Microsoft Entra ID", not "Azure Active Directory")
- Pricing guidance must reference official calculators — do not include hard-coded prices
- Compliance standards must reference the current version of each standard
- Links should point to official documentation where possible

### Review Criteria
Pull requests will be reviewed for:
- Technical accuracy (reviewed by a cloud architect in the relevant domain)
- Completeness (does the change fully address the stated improvement?)
- Consistency with existing framework structure and style
- Absence of vendor bias — this accelerator supports Azure, AWS, and GCP equally

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). By participating, you agree to uphold this standard.

---

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
