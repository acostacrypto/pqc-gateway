"""Benchmarking harness CLI (initial skeleton).

The real handshake against the gateway is implemented in week 3 of the
execution plan (see ``docs/methodology.md``). This module fixes, from the very
first commit, the interface and entry point that the smoke tests and the
client container depend on.
"""

from __future__ import annotations

import argparse

from pqc_gateway import __version__


def build_parser() -> argparse.ArgumentParser:
    """Return the harness CLI parser."""
    parser = argparse.ArgumentParser(
        prog="pqc-gateway-harness",
        description="Orchestrates measurements of classical and hybrid TLS 1.3 handshakes.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s " + __version__,
    )
    subparsers = parser.add_subparsers(dest="command")

    bench = subparsers.add_parser(
        "bench",
        help="Runs N repetitions and writes the results to CSV.",
    )
    bench.add_argument(
        "--reps",
        type=int,
        default=30,
        help="Repetitions per combination (>=30 recommended).",
    )
    bench.add_argument(
        "--out",
        default="benchmarks/results",
        help="Output directory for the CSV files.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entry point. Returns the exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "bench":
        raise NotImplementedError(
            "The 'bench' command is implemented in week 3 (harness v1). "
            "See docs/methodology.md."
        )
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
