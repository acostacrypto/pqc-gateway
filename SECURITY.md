# Security policy

## Scope of this project

**PQC-Gateway is an experimental, educational prototype.** It is not meant for
production and must never expose real third-party traffic. Before any real use
would be required, at minimum: an external audit, side-channel hardening,
production-grade key custody and interoperability validation.

Explicit warnings:

- `liboqs` and `oqs-provider` are experimental, as stated by the Open Quantum
  Safe project itself: many of their implementations have not been scrutinised
  to the level of mature TLS libraries.
- This project **does not implement its own cryptography**: every KEM and every
  signature comes from recognised libraries (OpenSSL 3 + oqs-provider).
- No component should ever be described as "quantum-proof". These are
  mechanisms designed under current post-quantum hardness assumptions, with no
  guarantee that they will hold in the future.

## What counts as a security issue here

- Leakage of real secrets (keys, tokens, credentials) in the repository or in
  published artifacts.
- Configuration that silently allows **downgrade** to unintended classical
  groups (see `docs/architecture.md` and the crypto-agility module).
- Vulnerabilities in this repository's own code (harness, scripts, TLS
  configuration, Dockerfiles, CI pipelines).
- *Packaging* problems (dependencies, base image, supply chain).

## How to report one

1. **Do not open a public issue** for vulnerabilities.
2. Use GitHub's private reporting: **Security → Report a vulnerability**
   (kept *private* until disclosure is coordinated).
3. Include: affected version/commit, reproduction steps, estimated impact and
  any known exploitation.

Target initial response time: 7 business days.

## Reports that belong upstream

- Cryptographic or implementation flaws in `liboqs` →
  <https://github.com/open-quantum-safe/liboqs>
- Flaws in `oqs-provider` → <https://github.com/open-quantum-safe/oqs-provider>
- Flaws in OpenSSL 3 → <https://www.openssl.org/news/vulnerabilities.html>

This repository is only responsible for its own code and configuration.

## Known limitations of the detection tooling

- **Gitleaks** only detects known patterns: it cannot guarantee the total
  absence of secrets.
- **Trivy/Syft** do not replace a professional audit; their results depend on
  the age of their vulnerability databases.
- **cosign keyless** depends on the availability of the Sigstore services
  (Fulcio/Rekor). Local-key signing is available as an alternative.
