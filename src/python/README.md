# `src/python` — harness and orchestration

Python code for the project: benchmarking orchestration, result analysis and
support scripts.

```
src/python/
└── pqc_gateway/
    ├── __init__.py   # package version
    └── cli.py        # harness CLI (`bench` subcommand)
```

## Usage

```bash
# From the repository root
python -m pip install -e ".[dev]"
PYTHONPATH=src/python python -m pqc_gateway.cli --help
PYTHONPATH=src/python python -m pqc_gateway.cli bench --reps 30   # week 3
pytest
ruff check .
```

`pyproject.toml` (root) configures `pythonpath` so `pytest` and the scripts
find the package without installing it; if you prefer to install it,
`pip install -e .` also works.

## Design

- **`bench`** runs N repetitions per group combination, applies the warm-up
  criterion of `docs/methodology.md` and writes a *tidy* CSV (one row per
  repetition) to `benchmarks/results/`.
- The harness does **not** implement cryptography: the handshake runs in the
  container with OpenSSL 3 + `oqs-provider`; Python only measures and records.
- No PyPI dependencies at runtime for the MVP (standard library), which keeps
  the client image small and the SBOM clean.

## Status

Initial skeleton (week 1). The `bench` subcommand raises an explicit
`NotImplementedError` until week 3.
