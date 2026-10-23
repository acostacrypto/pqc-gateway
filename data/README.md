# `data` — small datasets

**Small** datasets versioned directly (e.g. reference results, anonymised
fixtures, parameter tables cited from the literature).

## Rules

- No keys, certificates or real third-party data (blocked by `.gitignore` and
  by `CONTRIBUTING.md`).
- Wireshark captures: **anonymised** before being added (MAC/IP/hosts).
- Large datasets → **Zenodo with a DOI** (cited in `CITATION.cff`) or
  **Git LFS**, not this repository's history.
- Every dataset includes its provenance: how it was generated, with which stack
  version and with which command (traceability with `docs/methodology.md` §9).
