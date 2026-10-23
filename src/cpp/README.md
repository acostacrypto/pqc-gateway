# `src/cpp` — C/C++ utilities

Directory reserved for C/C++ utilities and *bindings*, when applicable.

## Planned content

- **Pure C++ measurement client** (optional extension): measures handshake
  overhead without the Python interpreter, removing any bias the GIL might
  introduce into CPU measurements.
- Small **wrappers over OpenSSL 3 + `oqs-provider`** to inspect the groups and
  cipher suites available in the base image.
- Entry points for handshake *fuzzing* with existing tools (AFL++, libFuzzer)
  — never with our own implementations.

## Status

No source code yet. The CI pipeline already detects this directory
automatically: if `.c/.cc/.cpp/.h/.hpp` files appear, `cppcheck` runs in
`ci.yml`; if it is empty, the step is skipped without failing.

## Rules

- Always link against the base image's OpenSSL 3 + `oqs-provider`
  (`/opt/ossl`), never against the host/system OpenSSL.
- No custom cryptographic primitives: everything goes through recognised
  libraries.
- Build with CMake pinned in the Docker image; no host dependencies.
