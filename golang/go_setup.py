#!/usr/bin/env python3
"""
Dynamic solution_test.go generator for Go testing.
Reads daily-{folder}.json and generates solution_test.go with correct imports.
Resolves link.json to import the correct solution package.

Usage:
    PYTHONPATH=. python3 golang/go_setup.py
    go test -tags=goexperiment.jsonv2 golang/solution_test.go golang/test_basic.go -test.timeout 3s -v
"""
import json
from pathlib import Path

def resolve_link(problem_path: Path, visited: set = None, original_link_info: dict = None) -> tuple:
    """
    Resolve problem link if link.json exists.
    Returns (resolved_path, link_info) tuple.
    """
    if visited is None:
        visited = set()

    link_file = problem_path / "link.json"
    if not link_file.exists():
        return problem_path, original_link_info

    problem_id = problem_path.name.split("_")[-1]
    if problem_id in visited:
        raise ValueError(f"Circular link detected involving problem {problem_id}")
    visited.add(problem_id)

    with link_file.open("r", encoding="utf-8") as f:
        link_info = json.load(f)

    if original_link_info is None:
        original_link_info = link_info

    link_to = link_info["link_to"]
    link_folder = link_info.get("link_folder", "problems")
    base_path = problem_path.parent / f"{link_folder}_{link_to}"

    return resolve_link(base_path, visited, original_link_info)

def get_config():
    """Read problem configuration from .env and daily-{folder}.json"""
    root = Path(__file__).parent.parent

    # Read .env for PROBLEM_FOLDER
    env_file = root / ".env"
    problem_folder = "problems"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("PROBLEM_FOLDER="):
                problem_folder = line.split("=")[1].strip().strip('"')
                break

    # Read config JSON
    config_file = root / f"daily-{problem_folder}.json"
    config = json.loads(config_file.read_text())
    daily = config.get("daily", "")
    plans = config.get("plans", [])

    # Collect problem IDs to test (original IDs for testcase, resolved for solution)
    problem_ids = [(daily, problem_folder)]
    if plans:
        for i in range(0, len(plans), 2):
            pid = plans[i]
            folder = plans[i + 1]
            problem_ids.append((pid, folder))

    return problem_ids, problem_folder

def generate_solution_test(problem_ids: list, default_folder: str):
    """Generate solution_test.go for the first problem (daily)"""
    if not problem_ids:
        return

    root = Path(__file__).parent.parent
    golang_path = root / "golang"

    # Use first problem (daily) for single test
    daily_id, daily_folder = problem_ids[0]

    # Resolve link to get the solution path
    # All problems are stored under "problems/" directory with prefix in the folder name
    problem_path = root / "problems" / f"{daily_folder}_{daily_id}"
    resolved_path, link_info = resolve_link(problem_path)

    # Get resolved problem ID and folder for the solution import
    resolved_id = resolved_path.name.split("_")[-1]
    # Extract folder prefix from the resolved path name (e.g., "problems" from "problems_1848")
    resolved_folder = resolved_path.name.rsplit("_", 1)[0]

    # Log link info if applicable
    if link_info:
        print(f"Problem {daily_id} uses solution from {resolved_id}: {link_info.get('reason', 'No reason provided')}")

    # Generate solution_test.go
    # The import uses the resolved (linked) solution
    # The TestEach uses the original problem ID for testcase lookup
    test_content = '''package golang

import (
\tproblem "leetCode/{resolved_folder}/{resolved_folder}_{resolved_id}"
\t"testing"
)

func TestSolution(t *testing.T) {{
\tTestEach(t, "{daily_id}", "{daily_folder}", problem.Solve)
}}
'''.format(resolved_folder=resolved_folder, resolved_id=resolved_id, daily_id=daily_id, daily_folder=daily_folder)

    test_path = golang_path / "solution_test.go"
    test_path.write_text(test_content)
    print(f"Generated: {test_path}")
    print(f"  Daily problem: {daily_id} (testcase)")
    print(f"  Solution from: {resolved_id}")

    # Generate problems_test.go for all problems if plans exist
    if len(problem_ids) > 1:
        generate_problems_test(problem_ids, root, golang_path)

def generate_problems_test(problem_ids: list, root: Path, golang_path: Path):
    """Generate problems_test.go for multiple problems"""
    imports = []
    test_cases = []

    for idx, (pid, folder) in enumerate(problem_ids):
        # All problems are stored under "problems/" directory with prefix in the folder name
        problem_path = root / "problems" / f"{folder}_{pid}"
        resolved_path, link_info = resolve_link(problem_path)

        resolved_id = resolved_path.name.split("_")[-1]
        # Extract folder prefix from the resolved path name (e.g., "problems" from "problems_1848")
        resolved_folder = resolved_path.name.rsplit("_", 1)[0]

        if link_info:
            print(f"Problem {pid} uses solution from {resolved_id}: {link_info.get('reason', 'No reason provided')}")

        imports.append('\tproblem{idx} "leetCode/{resolved_folder}/{resolved_folder}_{resolved_id}"'.format(
            idx=idx, resolved_folder=resolved_folder, resolved_id=resolved_id))
        test_cases.append('''\tt.Run("{folder}_{pid}", func(t *testing.T) {{
\t\tTestEach(t, "{pid}", "{folder}", problem{idx}.Solve)
\t}})'''.format(folder=folder, pid=pid, idx=idx))

    test_content = '''package golang

import (
\t"testing)

{imports}

func TestProblems(t *testing.T) {{
{test_cases}
}}
'''.format(imports="\n".join(imports), test_cases="\n".join(test_cases))

    test_path = golang_path / "problems_test.go"
    test_path.write_text(test_content)
    print(f"Generated: {test_path}")

if __name__ == "__main__":
    problem_ids, default_folder = get_config()
    print(f"Problems to test: {problem_ids}")

    generate_solution_test(problem_ids, default_folder)

    print(f"\nTo run single test:")
    print(f"  go test -tags=goexperiment.jsonv2 golang/solution_test.go golang/test_basic.go -test.timeout 3s -v")
    print(f"\nTo run all tests:")
    print(f"  go test -tags=goexperiment.jsonv2 golang/problems_test.go golang/test_basic.go -test.timeout 10s -v")
