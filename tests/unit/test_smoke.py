"""Smoke tests: the harness package imports and responds."""

from pqc_gateway import __version__
from pqc_gateway.cli import build_parser, main


def test_version_is_semver() -> None:
    parts = __version__.split(".")
    assert len(parts) == 3
    assert all(p.isdigit() for p in parts)


def test_parser_exposes_the_bench_command() -> None:
    args = build_parser().parse_args(["bench", "--reps", "5", "--out", "/tmp/out"])
    assert args.command == "bench"
    assert args.reps == 5
    assert args.out == "/tmp/out"


def test_main_without_command_prints_help(capsys) -> None:
    assert main([]) == 0
    assert "bench" in capsys.readouterr().out
