"""Tests for generated problem repository health checks."""

import json
from pathlib import Path

import pytest

from python.scripts.repository_health import apply_fix, build_fix_suggestions, scan_repository


def _write_problem(problem_path: Path, *, with_rust: bool = False) -> None:
    problem_path.mkdir(parents=True)
    (problem_path / "problem.md").write_text("# 1. Two Sum\n", encoding="utf-8")
    (problem_path / "testcase.py").write_text("testcases = []\n", encoding="utf-8")
    (problem_path / "solution.py").write_text("class Solution:\n    pass\n", encoding="utf-8")
    if with_rust:
        (problem_path / "solution.rs").write_text("pub struct Solution;\n", encoding="utf-8")
        (problem_path / "Cargo.toml").write_text(
            '[package]\nname = "solution_1"\nversion = "0.1.0"\nedition = "2021"\n',
            encoding="utf-8",
        )


@pytest.mark.unit
def test_health_accepts_complete_problem(tmp_path: Path):
    root = tmp_path
    _write_problem(root / "problems" / "problems_1")

    report = scan_repository(root, ["problems"])

    assert report.ok
    assert report.scanned == 1
    assert report.issues == ()


@pytest.mark.unit
def test_health_reports_missing_testcase(tmp_path: Path):
    problem = tmp_path / "problems" / "problems_1"
    problem.mkdir(parents=True)
    (problem / "problem.md").write_text("# 1. Two Sum\n", encoding="utf-8")
    (problem / "solution.py").write_text("class Solution:\n    pass\n", encoding="utf-8")

    report = scan_repository(tmp_path, ["problems"])

    assert not report.ok
    assert any("missing testcase" in issue.message for issue in report.errors)


@pytest.mark.unit
def test_health_validates_link_target(tmp_path: Path):
    target = tmp_path / "problems" / "problems_1"
    _write_problem(target)
    linked = tmp_path / "problems" / "problems_2"
    linked.mkdir()
    (linked / "problem.md").write_text("# 2. Same Problem\n", encoding="utf-8")
    (linked / "link.json").write_text(
        json.dumps({"link_to": "1", "link_folder": "problems"}),
        encoding="utf-8",
    )

    report = scan_repository(tmp_path, ["problems"])

    assert report.ok
    assert report.scanned == 2


@pytest.mark.unit
def test_health_reports_missing_link_target(tmp_path: Path):
    linked = tmp_path / "problems" / "problems_2"
    linked.mkdir(parents=True)
    (linked / "problem.md").write_text("# 2. Same Problem\n", encoding="utf-8")
    (linked / "link.json").write_text(
        json.dumps({"link_to": "999", "link_folder": "problems"}),
        encoding="utf-8",
    )

    report = scan_repository(tmp_path, ["problems"])

    assert not report.ok
    assert any("linked target does not exist" in issue.message for issue in report.errors)


@pytest.mark.unit
def test_health_warns_for_rust_workspace_mismatch(tmp_path: Path):
    _write_problem(tmp_path / "problems" / "problems_1", with_rust=True)
    (tmp_path / "Cargo.toml").write_text(
        '[workspace]\nmembers = ["rust/library"]\n',
        encoding="utf-8",
    )

    report = scan_repository(tmp_path, ["problems"])

    assert report.ok
    assert any("not listed in root Cargo.toml" in issue.message for issue in report.warnings)


@pytest.mark.unit
def test_health_ignores_legacy_problem_containers(tmp_path: Path):
    problems = tmp_path / "problems"
    (problems / "剑指Offer").mkdir(parents=True)
    (problems / "Interview").mkdir()
    (problems / "LCP").mkdir()

    report = scan_repository(tmp_path, ["problems"])

    assert report.ok
    assert report.scanned == 0
    assert report.issues == ()


@pytest.mark.unit
def test_health_suggests_removing_cache_only_problem_dir(tmp_path: Path):
    problem = tmp_path / "problems" / "problems_3878"
    cache = problem / "__pycache__"
    cache.mkdir(parents=True)
    (cache / "solution.cpython-314.pyc").write_bytes(b"cache")

    report = scan_repository(tmp_path, ["problems"])
    fixes = build_fix_suggestions(report, tmp_path)

    assert not report.ok
    assert len(fixes) == 1
    assert fixes[0].action == "remove_empty_dir"
    assert fixes[0].path == problem.resolve()


@pytest.mark.unit
def test_health_empty_dir_fix_removes_only_after_revalidation(tmp_path: Path):
    problem = tmp_path / "problems" / "problems_3878"
    cache = problem / "__pycache__"
    cache.mkdir(parents=True)
    (cache / "testcase.cpython-314.pyc").write_bytes(b"cache")

    fix = build_fix_suggestions(scan_repository(tmp_path, ["problems"]), tmp_path)[0]
    result = apply_fix(fix)

    assert "Removed:" in result
    assert not problem.exists()


@pytest.mark.unit
def test_health_does_not_suggest_removing_non_empty_problem_dir(tmp_path: Path):
    problem = tmp_path / "problems" / "problems_3878"
    problem.mkdir(parents=True)
    (problem / "notes.txt").write_text("keep me\n", encoding="utf-8")

    report = scan_repository(tmp_path, ["problems"])
    fixes = build_fix_suggestions(report, tmp_path)

    assert not report.ok
    assert fixes == ()


@pytest.mark.unit
def test_health_suggests_rust_cargo_sync(tmp_path: Path):
    _write_problem(tmp_path / "problems" / "problems_1", with_rust=True)
    (tmp_path / "Cargo.toml").write_text(
        '[workspace]\nmembers = ["rust/library", "problems/problems_999"]\n\n[dependencies]\n'
        'solution_999 = { path = "problems/problems_999", features = ["solution_999"] }\n',
        encoding="utf-8",
    )

    report = scan_repository(tmp_path, ["problems"])
    fixes = build_fix_suggestions(report, tmp_path)

    assert report.ok
    assert any("not listed in root Cargo.toml" in issue.message for issue in report.warnings)
    assert any("workspace member path does not exist" in issue.message for issue in report.warnings)
    assert any(fix.action == "sync_rust_cargo" for fix in fixes)


@pytest.mark.unit
def test_health_rust_cargo_sync_adds_missing_and_removes_stale(tmp_path: Path):
    _write_problem(tmp_path / "problems" / "problems_1", with_rust=True)
    (tmp_path / "Cargo.toml").write_text(
        '[workspace]\nmembers = [\n    "rust/library",\n    "problems/problems_999",\n]\n\n[dependencies]\n'
        'solution_999 = { path = "problems/problems_999", features = ["solution_999"] }\n',
        encoding="utf-8",
    )

    fix = next(fix for fix in build_fix_suggestions(scan_repository(tmp_path, ["problems"]), tmp_path)
               if fix.action == "sync_rust_cargo")
    result = apply_fix(fix)
    cargo = (tmp_path / "Cargo.toml").read_text(encoding="utf-8")

    assert "Synced Rust Cargo entries" in result
    assert '"problems/problems_1"' in cargo
    assert 'solution_1 = { path = "problems/problems_1", features = ["solution_1"] }' in cargo
    assert "problems/problems_999" not in cargo
