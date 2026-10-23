# Integration tests

End-to-end tests that bring up the **gateway + client** with Docker and verify
that the handshake completes with the `X25519MLKEM768` hybrid group.

Planned for weeks 2 and 5 of the execution plan:

| Week | Expected test |
|---|---|
| 2 | Client↔gateway connection with the negotiated hybrid group (smoke test) |
| 5 | End-to-end test via `docker compose up` in CI: bring up the stack, run N handshakes, verify the success rate and write the CSV |
| 6 | Interoperability matrix: every supported group combination has its own case |

Until then this directory is deliberately empty: `pytest` is configured to
walk `tests/unit` and `tests/integration` (see `pyproject.toml`), and the
smoke tests in `tests/unit` keep the pipeline green.

Convention: integration tests **fail** if the handshake does not negotiate the
expected group; a silent fallback to classical is never accepted as success.
