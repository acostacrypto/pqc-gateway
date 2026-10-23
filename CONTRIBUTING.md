# Contributing to PQC-Gateway

Thanks for your interest. This repository is a technical portfolio with
educational and small-scale research purposes; the goal is to keep it
**reproducible, auditable and honest about its limitations**.

## Workflow

1. **Fork** the repository and create a descriptive branch
   (`feat/…`, `fix/…`, `docs/…`).
2. Small, focused changes; one concept per PR.
3. Make sure the local checks pass:
   ```bash
   ruff check .
   pytest
   ```
4. Open a **Pull Request** against `main` describing:
   - what changes and why;
   - how it was verified (commands run, captures, results);
   - security / supply-chain impact, if any.
5. **`main` is protected**: a PR and at least **1 approval** are required
   before merge (no *force-push*, no branch deletion).

## Project rules

- **Never** add custom cryptography: primitives come from OpenSSL 3,
  `liboqs` and `oqs-provider`.
- **Never** commit keys, certificates or tokens (blocked by `.gitignore`; if a
  test fixture is needed, use a name other than `*.pem`/`*.key` and mark the
  file as toy/insecure material).
- **Never** test downgrade scenarios or attacks against anything other than
  your own, isolated infrastructure (Docker).
- Benchmarking results are published as **CI artifacts or release assets**, not
  as massive commits of regenerable CSVs (see
  `benchmarks/results/README.md`).
- Any claim about security or performance must be backed by data or cited;
  pending figures are marked as `[pending measurement]`.
- Every non-trivial architecture decision is documented as an **ADR** in
  `docs/adr/`.

## Conventions

| Area | Tooling |
|------|---------|
| Python | `ruff` (lint), `pytest` (tests), `bandit` (static security) |
| C/C++ | `cppcheck` / `clang-tidy` (once there is source code) |
| Dependencies | `pip-audit`, Dependabot |
| Containers | `trivy` (vulnerabilities), `syft` (SBOM) |
| Secrets | `gitleaks` (pre-commit and CI) |
| Versioning | `vX.Y.Z` semantic tags with release notes |

## Code of conduct

Respectful treatment, no personal attacks, and the same standard of rigor
applied to the technical documentation. Technical disagreements are settled
with evidence.
