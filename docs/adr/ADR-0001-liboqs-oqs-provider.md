# ADR-0001: use liboqs + oqs-provider on OpenSSL 3 as the hybrid TLS stack

- **Status:** Accepted
- **Date:** 2026-10-23
- **Context:** Week 1 of the execution plan (Project 1: PQC-Gateway)

## Context

The project needs a TLS 1.3 gateway able to negotiate a hybrid
classical/post-quantum group (`X25519 + ML-KEM-768`) reproducibly in Docker,
without implementing cryptography of our own. The ecosystem offers several
paths and one must be chosen before building starts.

Constraints:

- 0 USD/month budget and local execution;
- strict reproducibility (pinned versions, build from source);
- the stack must be scannable, SBOM-able and signable in CI;
- this repository's code must stay small: the cryptography is third-party.

## Decision

Use **OpenSSL 3** as the base TLS engine, extended with **`liboqs`** (PQC
primitives) and **`oqs-provider`** (hybrid TLS 1.3 groups over OpenSSL 3),
all **built from source in a multi-stage Docker image**
(`docker/Dockerfile.gateway`) with a deterministic `openssl.cnf` and a
build-time *smoke test*.

## Alternatives considered

| Alternative | Why it was not chosen (for now) |
|---|---|
| **wolfSSL** with native PQC support | Interesting for cross-implementation interoperability (possible extension); less flexibility to experiment with several hybrid groups and a poorer fit with the already dominant OpenSSL ecosystem |
| **BoringSSL / IETF drafts** | Fast-moving, no API stability; more fragile integration in CI |
| **`liboqs-python` only** | Does not provide a hybrid TLS *server*: it covers scripting, not the gateway |
| **Implementing TLS or a primitive ourselves** | Explicitly discarded by the project: unacceptable cryptographic risk and no portfolio value |
| **`oqs-provider` without version pinning** | Rejected: the ecosystem evolves quickly and reproducibility requires pinned references (`ARG LIBOQS_REF`, `ARG OQS_PROVIDER_REF`, `ARG OPENSSL_VERSION`) |

## Consequences

**Positive**

- A single TLS engine (OpenSSL 3) for client and gateway: the same code in the
  classical baseline and in the hybrid one, which isolates the experimental
  variable.
- Hybrid group support without touching code in this repository.
- Reproducible, scannable build from source (Trivy + Syft on the image).

**Negative / risks**

- `liboqs` and `oqs-provider` are **experimental**, as stated by the OQS
  project itself: not audited to the level of mature TLS libraries.
- Heavy compilation (OpenSSL + liboqs + provider) → slow CI builds; mitigated
  with layer caching in GitHub Actions.
- IETF hybrid group identifiers keep evolving: compatibility between versions
  must be re-verified on every upgrade.
- Variable side-channel coverage per algorithm (an `liboqs` limitation).

## Pending verifications (before depending on the stack)

- [ ] Exact version and license of `liboqs` (MIT assumed — **confirm** in the
      repository).
- [ ] Exact license of `oqs-provider` (permissive — **confirm**).
- [ ] Current NIST standardisation status of ML-KEM (FIPS 203) and ML-DSA
      (FIPS 204) when the project runs.
- [ ] Stable name of the hybrid group (`X25519MLKEM768`) in the pinned
      `oqs-provider` version.

## References

- `docker/Dockerfile.gateway` — pinned multi-stage build.
- `docs/architecture.md` §4 — stage detail and *smoke test*.
- <https://github.com/open-quantum-safe/liboqs>
- <https://github.com/open-quantum-safe/oqs-provider>
