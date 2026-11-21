#!/usr/bin/env python3
"""Minimal C++ compile-and-test runner for local competitive programming practice."""

import argparse
import difflib
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BUILD_DIR = REPO_ROOT / "build"


def natural_key(path: Path) -> list:
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", path.name)]


def normalize_output(text: str) -> str:
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def resolve_test_dir(source: Path, explicit_dir: str | None) -> Path | None:
    if explicit_dir:
        return Path(explicit_dir).resolve()
    try:
        rel = source.resolve().relative_to(REPO_ROOT)
    except ValueError:
        return None
    candidate = REPO_ROOT / "tests" / rel.with_suffix("")
    return candidate if candidate.is_dir() else None


def compile_source(source: Path, std: str, use_san: bool) -> Path:
    compiler = shutil.which("clang++") or shutil.which("g++")
    if not compiler:
        sys.exit("Error: neither clang++ nor g++ was found on PATH.")

    BUILD_DIR.mkdir(exist_ok=True)
    binary = BUILD_DIR / f"{source.stem}{'_san' if use_san else ''}"

    cmd = [compiler, f"-std=c++{std}", "-Wall", "-Wextra", "-Wshadow"]
    if use_san:
        cmd += ["-O1", "-g", "-fsanitize=address,undefined", "-fno-omit-frame-pointer"]
    else:
        cmd += ["-O2"]
    cmd += [str(source), "-o", str(binary)]

    print(f"Compiling ({Path(compiler).name}, C++{std}{', ASan+UBSan' if use_san else ''}): {source}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(result.returncode)
    return binary


def run_tests(binary: Path, test_dir: Path, timeout: float) -> int:
    in_files = sorted(test_dir.glob("*.in"), key=natural_key)
    if not in_files:
        print(f"No .in test files found in {test_dir}")
        return 1

    passed = 0
    failed = 0

    for in_file in in_files:
        expected_file = in_file.with_suffix(".out")
        raw_input = in_file.read_text(encoding="utf-8")

        start = time.perf_counter()
        try:
            proc = subprocess.run(
                [str(binary)],
                input=raw_input,
                text=True,
                capture_output=True,
                timeout=timeout,
            )
            elapsed_ms = (time.perf_counter() - start) * 1000.0
        except subprocess.TimeoutExpired:
            print(f"[TLE]  {in_file.name} (> {timeout:.1f}s)")
            failed += 1
            continue

        if proc.returncode != 0:
            print(f"[RE]   {in_file.name} (exit {proc.returncode}, {elapsed_ms:.1f} ms)")
            if proc.stderr.strip():
                print(proc.stderr.rstrip())
            failed += 1
            continue

        if expected_file.exists():
            actual = normalize_output(proc.stdout)
            expected = normalize_output(expected_file.read_text(encoding="utf-8"))
            if actual == expected:
                print(f"[PASS] {in_file.name} ({elapsed_ms:.1f} ms)")
                passed += 1
            else:
                print(f"[FAIL] {in_file.name} ({elapsed_ms:.1f} ms)")
                diff = difflib.unified_diff(
                    expected.splitlines(),
                    actual.splitlines(),
                    fromfile=expected_file.name,
                    tofile="actual",
                    lineterm="",
                )
                for line in diff:
                    print("  " + line)
                failed += 1
        else:
            print(f"[RAN]  {in_file.name} ({elapsed_ms:.1f} ms) — no {expected_file.name}")
            if proc.stdout.strip():
                print(proc.stdout.rstrip())

        if proc.stderr.strip():
            print(f"  stderr: {proc.stderr.rstrip()}")

    if passed or failed:
        print(f"\nLocal tests: {passed}/{passed + failed} passed (local check only, not an official judge verdict).")
    else:
        print("\nFinished running input files without expected .out files (local check only).")

    return 0 if failed == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile and test a C++ solution locally.")
    parser.add_argument("source", help="Path to the .cpp source file")
    parser.add_argument("--std", choices=["17", "20"], default="17", help="C++ standard (default: 17)")
    parser.add_argument("--san", action="store_true", help="Enable AddressSanitizer and UndefinedBehaviorSanitizer")
    parser.add_argument("--tests", help="Optional directory containing .in/.out test files")
    parser.add_argument("--run", action="store_true", help="Run interactively with stdin/stdout")
    parser.add_argument("--timeout", type=float, default=2.0, help="Per-test timeout in seconds (default: 2.0)")
    args = parser.parse_args()

    source = Path(args.source)
    if not source.is_file():
        sys.exit(f"Error: file not found: {source}")

    binary = compile_source(source, args.std, args.san)

    if args.run:
        return subprocess.run([str(binary)]).returncode

    test_dir = resolve_test_dir(source, args.tests)
    if test_dir is None:
        print("No matching tests/ directory found; running interactively (pass stdin, Ctrl-D to end).")
        return subprocess.run([str(binary)]).returncode

    return run_tests(binary, test_dir, args.timeout)


if __name__ == "__main__":
    sys.exit(main())
