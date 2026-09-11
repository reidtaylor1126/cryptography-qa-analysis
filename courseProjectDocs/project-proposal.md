# Project Proposal

## Overview

`cryptography` is the de facto Python library for all common cryptography applications. It provides encryption through both primitives and recipes (most notably Fernet, a symmetric-key encryption specification, and Cobblestone, a version adapted for streaming), allowing encryption to be integrated in python programs easily and simply with secure default configurations, but also exposing lower-level features for developers with more specific needs. It is developed under the supervision of the Python Cryptographic Authority, which also manages projects like `bcrypt` and `pyopenssl`.

Emphasizing safety, the project is structured so as to encourage the use of Fernet and Cobblestone (as well as X.509) as easy and safe options. Primitives, old/deprecated algorithms, and other low-level utilities are referred to as "hazardous materials" in both the documentation and directory structure.
Software quality has been a focus of the project since its v0.1 release in 2014, which included a robust unit test suite using pytest with parameterization.

We evaluated the project's codebase using SonarQube to extract comprehensive quality and maintainability metrics, alongside the original repository's rigorous Continuous Integration (CI) pipeline for test coverage.

---

## Quality Metrics

We collected the following standard maintainability and quality metrics to establish a baseline for the `cryptography` project:

### Size and Complexity (SonarQube)

- **Lines of Code (LOC):** 42,780 Total across 211 files (including 107 Rust files, highlighting the hybrid Python/Rust architecture).
- **Comment Density:** 7.8% in the source directory. This reflects the proportion of documentation and inline explanations relative to the code.
- **Cyclomatic Complexity:** 9,270 across the source directory. This indicates the number of decision points and linear paths through the code, serving as a baseline to identify areas that may be difficult to test or maintain.

### Code Quality and Security (SonarQube)

- **Code Smells & Maintainability:** SonarQube scans provide insights into potential code smells, allowing us to identify areas for refactoring and calculate the estimated **Technical Debt**.
- **Security Hotspots & Vulnerabilities:** Given the project's domain, we leverage SonarQube's static analysis to flag standard coding vulnerabilities, though core cryptographic robustness is enforced by community audits and mathematical proofs.
- **Code Duplication:** SonarQube checks for duplicated code blocks to ensure DRY (Don't Repeat Yourself) principles are upheld across the Python and Rust codebases.

### Testing and Reliability (Repository CI)

- **Unit Test Coverage:** 100%. This metric is enforced and retrieved directly from the repository's existing GitHub Actions CI pipeline. The `cryptography` project maintains extremely strict standards, causing the CI build to explicitly fail if statement or branch coverage drops even a fraction below 100%.

Within the context of a cryptographic library, there are a plethora of other relevant quality metrics that are difficult to measure via standard static analysis tools. These include the algorithmic robustness against side-channel attacks, memory safety in native bindings (enforced via Rust), and the overall ease of use of the high-level API.
