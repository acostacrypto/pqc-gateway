# `notebooks` — result analysis

Jupyter notebooks with the benchmarking analysis: plots, median/IQR, group
combination comparison and discussion of threats to validity.

## Conventions

- **Yes to code, no to heavy outputs**: notebooks are versioned as source
  code; exported HTML and checkpoints stay out (`.gitignore`).
- Reproducibility: notebooks must run from scratch from the CSVs published as
  artifacts, with no undocumented local data.
- Every figure quoted outside the notebook links to the exact run that
  produced it (commit + `liboqs`/`oqs-provider` version).
- A null or negative result is documented like a positive one.

## Planned

| Notebook | Content | Week |
|---|---|---|
| `01_handshake_overhead.ipynb` | First run: classical vs hybrid | 3 |
| `02_multi_group_comparison.ipynb` | Group combination matrix | 6 |
