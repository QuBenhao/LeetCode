#!/usr/bin/env python3
"""
Dynamic Cargo.toml generator for selective compilation.
Reads daily-{folder}.json and generates a Cargo.toml that only compiles needed problems.

This script:
1. Backs up original Cargo.toml to Cargo.toml.full
2. Generates minimal Cargo.toml with only configured problems
3. Run tests with: cargo test --test solution_test

To restore full Cargo.toml: cp Cargo.toml.full Cargo.toml
"""
import json
import shutil
from pathlib import Path

def resolve_link(problem_path: Path, visited: set = None) -> Path:
    """
    Resolve problem link if link.json exists.
    Returns the actual problem path to use for solution.
    """
    if visited is None:
        visited = set()

    link_file = problem_path / "link.json"
    if not link_file.exists():
        return problem_path

    problem_id = problem_path.name.split("_")[-1]
    if problem_id in visited:
        raise ValueError(f"Circular link detected involving problem {problem_id}")
    visited.add(problem_id)

    with link_file.open("r", encoding="utf-8") as f:
        link_info = json.load(f)

    link_to = link_info["link_to"]
    link_folder = link_info.get("link_folder", "problems")
    # problem folders are named like "problems_1848" directly under root
    base_path = problem_path.parent / f"{link_folder}_{link_to}"

    print(f"Problem {problem_id} is linked to {link_to}: {link_info.get('reason', 'No reason provided')}")
    return resolve_link(base_path, visited)

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
    
    # Collect problem IDs to compile (resolve links first)
    problem_ids = []
    seen = set()

    def add_problem(pid):
        if pid in seen:
            return
        # Resolve link first before marking as seen
        problem_path = root / "problems" / f"{problem_folder}_{pid}"
        resolved_path = resolve_link(problem_path)
        # Use the resolved problem ID for compilation
        resolved_id = resolved_path.name.split("_")[-1]
        # Extract folder prefix from the resolved path name (e.g., "problems" from "problems_1848")
        resolved_folder = resolved_path.name.rsplit("_", 1)[0]
        if resolved_id in seen:
            return
        seen.add(pid)
        seen.add(resolved_id)
        problem_ids.append((resolved_id, resolved_folder))

    if daily:
        add_problem(daily)
    if plans:
        for i in range(0, len(plans), 2):
            pid = plans[i]
            add_problem(pid)

    return problem_ids, problem_folder

def normalize_id(pid: str) -> str:
    """Convert problem ID to safe Rust identifier"""
    return pid.replace(" ", "_").replace("-", "_").replace(".", "_")

def generate_cargo_toml(problem_ids: list, problem_folder: str):
    """Generate a minimal Cargo.toml for testing only specified problems"""
    root = Path(__file__).parent.parent
    cargo_path = root / "Cargo.toml"
    backup_path = root / "Cargo.toml.full"

    # Backup original if not exists
    if not backup_path.exists():
        shutil.copy(cargo_path, backup_path)
        print(f"Backed up: {backup_path}")

    # Generate workspace members
    workspace_members = [
        '"rust/library"',
        '"rust/test_executor"',
    ]
    for resolved_id, resolved_folder in problem_ids:
        folder_name = f"{resolved_folder}_{resolved_id}"
        workspace_members.append(f'"problems/{folder_name}"')

    features_def = []
    features_default = []
    dependencies = [
        'serde_json = "1.0"',
        'rand = "0.8.4"',
        'regex = "1.10.5"',
        'assert_float_eq = "1"',
        'test_executor = { path = "rust/test_executor", features = ["run_test"] }',
    ]

    for resolved_id, resolved_folder in problem_ids:
        safe_id = normalize_id(resolved_id)
        folder_name = f"{resolved_folder}_{resolved_id}"
        dependencies.append(
            f'solution_{safe_id} = {{ path = "problems/{folder_name}", features = ["solution_{safe_id}"] }}'
        )
        features_def.append(f'{safe_id} = []')
        features_default.append(f'"{safe_id}"')
    
    cargo_content = f'''# Auto-generated Cargo.toml - Do not edit manually
# Regenerate using: python rust/cargo_setup.py
# Restore full: cp Cargo.toml.full Cargo.toml

[workspace]
members = [
{chr(10).join("    " + m + "," for m in workspace_members)}
]
resolver = "2"

[package]
name = "leetcode"
version = "0.1.0"
edition = "2021"
rust-version = "1.79.0"
authors = ["benhao"]
description = "LeetCode solutions in Rust"

[[test]]
name = "solution_test"
path = "rust/test_executor/tests/test.rs"

[[test]]
name = "solutions_test"
path = "rust/test_executor/tests/solutions_test.rs"

[features]
default = [{', '.join(features_default)}]
{chr(10).join(features_def)}

[dependencies]
{chr(10).join(dependencies)}
'''
    
    cargo_path.write_text(cargo_content)
    return cargo_path

def update_test_file(problem_ids: list, problem_folder: str):
    """Update test.rs to test only the configured problems"""
    root = Path(__file__).parent.parent

    if len(problem_ids) == 0:
        return None

    # problem_ids is now list of (resolved_id, resolved_folder) tuples
    problems_array = ", ".join(f'["{folder}", "{pid}"]' for pid, folder in problem_ids)
    imports = chr(10).join(f"\tuse solution_{normalize_id(pid)} as solution{i};"
                          for i, (pid, folder) in enumerate(problem_ids))
    match_cases = chr(10).join(f'\t\t\t\t{i} => solution{i}::solve,'
                               for i in range(len(problem_ids)))

    test_content = f'''const PROBLEMS: [[&str; 2]; {len(problem_ids)}] = [{problems_array}];

#[cfg(test)]
mod test {{
\tuse test_executor::run_test::run_test;
\tuse crate::PROBLEMS;

{imports}

\t#[test]
\tfn test_solutions() {{
\t\tfor (i, problem) in PROBLEMS.iter().enumerate() {{
\t\t\tlet (folder, id) = (problem[0], problem[1]);
\t\t\tprintln!("Testing problem {{}}", id);
\t\t\trun_test(id, folder, match i {{
{match_cases}
\t\t\t\t_ => panic!("Unknown solution"),
\t\t\t}});
\t\t}}
\t}}
}}
'''

    test_path = root / "rust/test_executor/tests/test.rs"
    test_path.write_text(test_content)
    return test_path

if __name__ == "__main__":
    problem_ids, problem_folder = get_config()
    print(f"Problems to test: {problem_ids}")
    
    cargo_path = generate_cargo_toml(problem_ids, problem_folder)
    print(f"Generated: {cargo_path}")
    
    test_path = update_test_file(problem_ids, problem_folder)
    print(f"Updated: {test_path}")
    
    print(f"\nTo run tests:")
    print(f"  cargo test --test solution_test")
    print(f"\nTo restore full Cargo.toml:")
    print(f"  cp Cargo.toml.full Cargo.toml")
