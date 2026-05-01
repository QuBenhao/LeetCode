#!/usr/bin/env python3
"""Repository health checks for generated LeetCode problem folders."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11 fallback is not used in CI.
    tomllib = None


SOLUTION_FILES = (
    "solution.py",
    "solution.go",
    "solution.ts",
    "solution.rs",
    "solution.sql",
    "solution.c",
    "solution.md",
    "Solution.cpp",
    "Solution.java",
)

TESTCASE_FILES = ("testcase.py", "testcase", "input.json")
PROBLEM_DOCS = ("problem.md", "problem_zh.md")
LEGACY_CONTAINER_DIRS = {
    "problems": {"Interview", "LCP", "剑指Offer"},
}
EMPTY_ARTIFACT_DIRS = {"__pycache__", ".pytest_cache"}
EMPTY_ARTIFACT_SUFFIXES = {".pyc", ".pyo"}
EMPTY_ARTIFACT_NAMES = {".DS_Store"}


@dataclass(frozen=True)
class HealthIssue:
    """A repository health issue found during scanning."""

    level: str
    path: Path
    message: str

    def display(self, root_path: Path) -> str:
        try:
            rel_path = self.path.relative_to(root_path)
        except ValueError:
            rel_path = self.path
        return f"[{self.level.upper()}] {rel_path}: {self.message}"


@dataclass(frozen=True)
class HealthReport:
    """Aggregated repository health scan result."""

    scanned: int
    issues: tuple[HealthIssue, ...]

    @property
    def errors(self) -> tuple[HealthIssue, ...]:
        return tuple(issue for issue in self.issues if issue.level == "error")

    @property
    def warnings(self) -> tuple[HealthIssue, ...]:
        return tuple(issue for issue in self.issues if issue.level == "warning")

    @property
    def ok(self) -> bool:
        return not self.errors


@dataclass(frozen=True)
class HealthFix:
    """A conservative fix that can be applied after user confirmation."""

    action: str
    path: Path
    message: str
    folder: str | None = None

    def display(self, root_path: Path) -> str:
        try:
            rel_path = self.path.relative_to(root_path)
        except ValueError:
            rel_path = self.path
        return f"{self.message}: {rel_path}"


def scan_repository(root_path: Path, folders: Iterable[str] = ("problems",)) -> HealthReport:
    """Scan generated problem folders and return a health report."""
    root_path = root_path.resolve()
    folder_names = tuple(dict.fromkeys(folders))
    issues: list[HealthIssue] = []
    scanned = 0

    workspace_members = _load_rust_workspace_members(root_path)

    for folder_name in folder_names:
        folder_path = root_path / folder_name
        if not folder_path.exists():
            issues.append(HealthIssue("error", folder_path, "folder does not exist"))
            continue
        if not folder_path.is_dir():
            issues.append(HealthIssue("error", folder_path, "path is not a directory"))
            continue

        for problem_path in sorted(p for p in folder_path.iterdir() if p.is_dir()):
            if problem_path.name.startswith("."):
                continue
            if problem_path.name in LEGACY_CONTAINER_DIRS.get(folder_name, set()):
                continue
            if not _is_generated_problem_dir(problem_path.name, folder_name):
                issues.append(HealthIssue(
                    "warning",
                    problem_path,
                    f"directory does not match generated naming pattern {folder_name}_<id>",
                ))
                continue
            scanned += 1
            issues.extend(_scan_problem_dir(root_path, folder_name, problem_path, workspace_members))

    issues.extend(_scan_missing_rust_workspace_members(root_path, folder_names, workspace_members))
    return HealthReport(scanned=scanned, issues=tuple(issues))


def format_report(report: HealthReport, root_path: Path, limit: int = 50) -> str:
    """Format a health report for CLI output."""
    lines = [
        f"Scanned {report.scanned} generated problem directories.",
        f"Errors: {len(report.errors)}; warnings: {len(report.warnings)}.",
    ]
    if not report.issues:
        lines.append("No repository health issues found.")
        return "\n".join(lines)

    lines.append("")
    for issue in report.issues[:limit]:
        lines.append(issue.display(root_path))
    remaining = len(report.issues) - limit
    if remaining > 0:
        lines.append(f"... {remaining} more issue(s) omitted.")
    return "\n".join(lines)


def build_fix_suggestions(report: HealthReport, root_path: Path) -> tuple[HealthFix, ...]:
    """Build conservative fix suggestions from a health report."""
    suggestions: list[HealthFix] = []
    seen_keys: set[tuple[str, str]] = set()
    for issue in report.errors:
        problem_path = issue.path if issue.path.is_dir() else issue.path.parent
        key = ("remove_empty_dir", problem_path.as_posix())
        if key in seen_keys:
            continue
        if _is_effectively_empty_dir(problem_path):
            suggestions.append(HealthFix(
                action="remove_empty_dir",
                path=problem_path,
                message="Remove empty generated problem directory",
            ))
            seen_keys.add(key)
    for issue in report.warnings:
        if (
            "Rust solution is not listed in root Cargo.toml" not in issue.message
            and "root Cargo.toml workspace member path does not exist" not in issue.message
        ):
            continue
        try:
            folder = issue.path.relative_to(root_path).parts[0]
        except (IndexError, ValueError):
            continue
        key = ("sync_rust_cargo", folder)
        if key in seen_keys:
            continue
        suggestions.append(HealthFix(
            action="sync_rust_cargo",
            path=root_path / "Cargo.toml",
            message=f"Sync Rust Cargo workspace entries for {folder}",
            folder=folder,
        ))
        seen_keys.add(key)
    return tuple(suggestions)


def apply_fix(fix: HealthFix) -> str:
    """Apply a confirmed health fix and return a short result message."""
    match fix.action:
        case "remove_empty_dir":
            if not fix.path.exists():
                return f"Skipped missing path: {fix.path}"
            if not fix.path.is_dir():
                return f"Skipped non-directory path: {fix.path}"
            if not _is_effectively_empty_dir(fix.path):
                return f"Skipped non-empty directory: {fix.path}"
            shutil.rmtree(fix.path)
            return f"Removed: {fix.path}"
        case "sync_rust_cargo":
            if not fix.folder:
                return "Skipped Rust Cargo sync: missing problem folder"
            from python.scripts.tools import sync_rust_cargo_main
            result = sync_rust_cargo_main(fix.path.parent, fix.folder)
            added = ", ".join(result["added"]) if result["added"] else "none"
            removed = ", ".join(result["removed"]) if result["removed"] else "none"
            return f"Synced Rust Cargo entries. Added: {added}. Removed stale paths: {removed}."
        case _:
            return f"Unknown fix action: {fix.action}"


def _scan_problem_dir(
    root_path: Path,
    folder_name: str,
    problem_path: Path,
    workspace_members: set[str],
) -> list[HealthIssue]:
    issues: list[HealthIssue] = []

    has_link = (problem_path / "link.json").exists()
    has_sql_solution = (problem_path / "solution.sql").exists()

    if not any((problem_path / doc).exists() for doc in PROBLEM_DOCS):
        issues.append(HealthIssue("error", problem_path, "missing problem.md or problem_zh.md"))

    if not has_link and not has_sql_solution and not any((problem_path / f).exists() for f in TESTCASE_FILES):
        issues.append(HealthIssue("error", problem_path, "missing testcase.py, testcase, or input.json"))

    if not has_link and not any((problem_path / f).exists() for f in SOLUTION_FILES):
        issues.append(HealthIssue("error", problem_path, "missing solution file"))

    for file_name in SOLUTION_FILES:
        file_path = problem_path / file_name
        if file_path.exists() and file_path.stat().st_size == 0:
            issues.append(HealthIssue("error", file_path, "solution file is empty"))

    if has_link:
        issues.extend(_scan_link(root_path, problem_path))

    has_rust_solution = (problem_path / "solution.rs").exists()
    has_cargo = (problem_path / "Cargo.toml").exists()
    if has_rust_solution and not has_cargo:
        issues.append(HealthIssue("error", problem_path, "solution.rs exists but Cargo.toml is missing"))
    if has_cargo and not has_rust_solution:
        issues.append(HealthIssue("error", problem_path, "Cargo.toml exists but solution.rs is missing"))
    if has_rust_solution and has_cargo:
        workspace_member = f"{folder_name}/{problem_path.name}"
        if workspace_member not in workspace_members:
            issues.append(HealthIssue("warning", problem_path, "Rust solution is not listed in root Cargo.toml workspace members"))
        issues.extend(_scan_problem_cargo(problem_path))

    return issues


def _scan_link(root_path: Path, problem_path: Path) -> list[HealthIssue]:
    link_path = problem_path / "link.json"
    try:
        link_data = json.loads(link_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [HealthIssue("error", link_path, f"invalid JSON: {exc}")]

    issues: list[HealthIssue] = []
    link_to = link_data.get("link_to")
    link_folder = link_data.get("link_folder")
    if not link_to:
        issues.append(HealthIssue("error", link_path, "missing link_to"))
    if not link_folder:
        issues.append(HealthIssue("error", link_path, "missing link_folder"))
    if link_to and link_folder:
        target = root_path / str(link_folder) / f"{link_folder}_{link_to}"
        if not target.exists():
            issues.append(HealthIssue("error", link_path, f"linked target does not exist: {target.relative_to(root_path)}"))
    return issues


def _scan_problem_cargo(problem_path: Path) -> list[HealthIssue]:
    cargo_path = problem_path / "Cargo.toml"
    if tomllib is None:
        return []
    try:
        data = tomllib.loads(cargo_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [HealthIssue("error", cargo_path, f"invalid Cargo.toml: {exc}")]

    expected_name = f"solution_{problem_path.name.split('_', 1)[1]}"
    actual_name = data.get("package", {}).get("name")
    if actual_name != expected_name:
        return [HealthIssue("warning", cargo_path, f"package name is {actual_name!r}, expected {expected_name!r}")]
    return []


def _load_rust_workspace_members(root_path: Path) -> set[str]:
    cargo_path = root_path / "Cargo.toml"
    if not cargo_path.exists() or tomllib is None:
        return set()
    try:
        data = tomllib.loads(cargo_path.read_text(encoding="utf-8"))
    except Exception:
        return set()
    return set(data.get("workspace", {}).get("members", []))


def _scan_missing_rust_workspace_members(
    root_path: Path,
    folder_names: tuple[str, ...],
    workspace_members: set[str],
) -> list[HealthIssue]:
    issues: list[HealthIssue] = []
    folder_prefixes = tuple(f"{folder}/" for folder in folder_names)
    for member in sorted(workspace_members):
        if not member.startswith(folder_prefixes):
            continue
        member_path = root_path / member
        if not member_path.exists():
            issues.append(HealthIssue("warning", member_path, "root Cargo.toml workspace member path does not exist"))
    return issues


def _is_generated_problem_dir(name: str, folder_name: str) -> bool:
    return bool(re.match(rf"^{re.escape(folder_name)}_.+", name))


def _is_effectively_empty_dir(path: Path) -> bool:
    """Return True if a directory contains only generated cache artifacts."""
    if not path.is_dir():
        return False
    for child in path.iterdir():
        if child.name in EMPTY_ARTIFACT_NAMES:
            continue
        if child.is_dir() and child.name in EMPTY_ARTIFACT_DIRS and _is_effectively_empty_dir(child):
            continue
        if child.is_file() and child.suffix in EMPTY_ARTIFACT_SUFFIXES:
            continue
        return False
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check generated LeetCode problem folder health.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--folder", action="append", default=None, help="Problem folder to scan. Repeat to scan several.")
    parser.add_argument("--limit", type=int, default=50, help="Maximum number of issues to print.")
    args = parser.parse_args(argv)

    folders = args.folder or ["problems"]
    report = scan_repository(args.root, folders)
    print(format_report(report, args.root, args.limit))
    return 0 if report.ok else 1


if __name__ == "__main__":
    sys.exit(main())
