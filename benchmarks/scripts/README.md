# `benchmarks/scripts` — measurement orchestration

Scripts that run the experiment repetitions and write the *tidy* CSV files
described in [`docs/methodology.md`](../../docs/methodology.md) §6.

| Planned script | Purpose | Week |
|---|---|---|
| `run_bench.py` (or `pqc-gateway-harness bench`) | N repetitions per combination, with *warm-up* and error handling | 3 |
| `compare_groups.py` | Classical vs hybrid vs PQC-only baselines | 6 |
| `collect_env.py` | Records hardware, versions and run conditions | 3 |

Rules:

- Scripts **only measure**: they implement no cryptography.
- Execution conditions (versions, repetitions, discard criterion) are declared
  **before** looking at the results.
- Resulting CSVs are published as a CI artifact or release asset; they are not
  committed in bulk (see `benchmarks/results/README.md`).
