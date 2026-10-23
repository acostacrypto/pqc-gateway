# Experimental methodology

> Goal: answer the project's research question with reproducible, honest data.
> This document is written **before** running the experiment (to avoid
> *p-hacking* and post-hoc conclusions).

## 1. Research question

> What is the **latency and handshake-size overhead** of adopting hybrid TLS
> 1.3 `X25519 + ML-KEM-768` over classical ECDHE, under controlled local
> network conditions?

## 2. Hypotheses

- **H1:** the hybrid handshake measurably increases the bytes exchanged over
  the classical one.
- **H2:** the hybrid handshake measurably increases handshake CPU time over the
  classical one.
- **H3:** the order of magnitude of both increases is **to be determined
  empirically** — no figure is assumed a priori.

They are formulated as measurable increments, not concrete percentages: any
unmeasured figure is written as `[pending measurement]`.

## 3. Variables

| Type | Variable | Unit |
|---|---|---|
| Dependent | Handshake time | ms |
| Dependent | Total bytes exchanged | bytes |
| Dependent | CPU usage during handshake | % / CPU·s |
| Dependent | Connection success rate | % |
| Independent | Negotiated group (plain ECDHE, `X25519MLKEM768`, PQC-only if available) | categorical |
| Control | Hardware, OpenSSL/liboqs/oqs-provider versions, system load, network | documented |
| Noise | Jitter between repetitions | median and IQR |

## 4. Experimental design

1. **Pinned environment:** the whole stack runs in Docker with pinned
   versions (see `docker/Dockerfile.gateway`). Hardware and system load are
   documented for every run.
2. **Same machine and network** for all conditions; no third-party traffic;
   isolated internal Docker network.
3. **Repetitions:** ≥30 per combination (more if the initial variance is high).
4. **Warm-up:** the first N runs are discarded (cold caches) and N is
   documented.
5. **Baselines:**
   - pure classical ECDHE (X25519 without a PQC component);
   - PQC-only, if the tooling allows it (no classical component).
6. **Randomisation:** the order of conditions is alternated so that order
   effects are not confused with group effects.
7. **Fixed seeds** where applicable (synthetic backend data generation).

## 5. Variability handling

- **Median and IQR** are reported, not the mean alone (heavy-tailed
  distributions).
- Raw data (CSV) of every run is kept, not just aggregates.
- Standard deviation and the number of discarded runs are recorded, with the
  reason.

## 6. Data schema

Tidy CSV, one row per repetition:

| column | description |
|---|---|
| `timestamp` | ISO-8601 UTC |
| `group` | negotiated group identifier |
| `variant` | `classic` / `hybrid` / `pqc-only` |
| `rep` | repetition number (0-based) |
| `warmup` | `true` if the run is discarded |
| `handshake_ms` | handshake time |
| `bytes_total` | bytes exchanged (client + server) |
| `cpu_pct` | CPU usage during handshake |
| `success` | connection success/failure |
| `openssl_version`, `liboqs_ref`, `oqs_provider_ref` | exact environment |

Results are published as a **CI artifact or release asset**, never as mass
commits (see `benchmarks/results/README.md`).

## 7. Threats to validity

| Threat | Impact | Mitigation |
|---|---|---|
| Hardware not representative of production | External | Hardware declared; results are local in scope |
| No real network latency/loss | External | Controlled, documented network; the gap is acknowledged |
| Concrete `liboqs`/`oqs-provider` versions | External | Pinned versions published with every result |
| Measurement noise | Internal | Warm-up, ≥30 repetitions, median/IQR |
| Correlation with system load | Internal | Conditions documented; run order alternated |

## 8. How to avoid exaggerated conclusions

- Results are presented as a **local exploratory study**, not as the
  authoritative measurement of the "real cost of PQC".
- Organisations such as Cloudflare, Google or AWS have already published
  larger-scale measurements; this work is positioned as a **methodologically
  rigorous small-scale replication**, not a scoop.
- "Post-quantum resistance" always means *designed under current computational
  hardness assumptions, with no cryptographically relevant quantum computer
  known to break it, and no guarantee that this will remain true*.
- Every negative or null result is reported like a positive one.

## 9. Reproducibility

From a clean `git clone`, on a new machine:

```bash
docker build -f docker/Dockerfile.gateway -t pqc-gateway:base .
docker compose -f docker/docker-compose.yml up --build
# Once implemented (week 3):
PYTHONPATH=src/python python -m pqc_gateway.cli bench --reps 30 \
  --out benchmarks/results
pytest
```

Reproducibility checklist:

- [ ] Exact versions of OpenSSL, `liboqs` and `oqs-provider` documented.
- [ ] Exact execution commands documented.
- [ ] Raw data published next to the analysis notebook.
- [ ] Hardware conditions described.
- [ ] Number of repetitions and the discard criterion declared *before* seeing
      the results.

## 10. Publication

- Public repository with scripts, raw data (CSV) and the analysis notebook.
- Possible additional deposit on Zenodo with a DOI via `CITATION.cff`.
- Realistic contribution level: a **reproducible experimental study** with
  didactic and methodological-rigor value. Publication in high-impact journals
  is not promised: the field (hybrid TLS overhead) has already been partly
  explored by industry and by the OQS project itself.
