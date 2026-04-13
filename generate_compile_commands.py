#!/usr/bin/env python3
"""Generate compile_commands.json for clangd."""

import json
import os
import subprocess
from pathlib import Path


def get_bazel_external_path():
    """Get the path to Bazel's external directory."""
    result = subprocess.run(
        ["bazel", "info", "output_base"],
        capture_output=True,
        text=True,
        check=True,
    )
    return Path(result.stdout.strip()) / "external"


def main():
    workspace_root = Path(__file__).parent
    bazel_external = get_bazel_external_path()

    # Find nlohmann_json include path
    nlohmann_path = None
    for p in bazel_external.iterdir():
        if p.name.startswith("nlohmann_json"):
            include_path = p / "include"
            if include_path.exists():
                nlohmann_path = include_path
                break

    if nlohmann_path is None:
        print("Warning: nlohmann_json not found in Bazel external")
        nlohmann_path = workspace_root  # fallback

    # Build include flags
    include_flags = [
        f"-I{workspace_root / 'cpp'}",
        f"-I{workspace_root / 'cpp' / 'common'}",
        f"-I{workspace_root / 'cpp' / 'models'}",
        f"-I{workspace_root}",
        f"-I{nlohmann_path}",
    ]

    compile_flags = [
        "-std=c++23",
        "-Wall",
        "-Wno-unused-variable",
        "-Wno-unused-parameter",
        "-D_GLIBCXX_USE_CXX11_ABI=1",
        *include_flags,
    ]

    compile_commands = []

    # Add entries for all Solution.cpp files
    for cpp_file in workspace_root.rglob("Solution.cpp"):
        # Skip premiums folder if needed
        if "premiums" in str(cpp_file):
            continue

        entry = {
            "directory": str(workspace_root),
            "command": f"clang++ {' '.join(compile_flags)} -c {cpp_file.relative_to(workspace_root)}",
            "file": str(cpp_file.relative_to(workspace_root)),
        }
        compile_commands.append(entry)

    # Add entries for cpp/*.cpp files
    for cpp_file in (workspace_root / "cpp").rglob("*.cpp"):
        entry = {
            "directory": str(workspace_root),
            "command": f"clang++ {' '.join(compile_flags)} -c {cpp_file.relative_to(workspace_root)}",
            "file": str(cpp_file.relative_to(workspace_root)),
        }
        compile_commands.append(entry)

    # Add a catch-all entry for header files
    header_entry = {
        "directory": str(workspace_root),
        "command": f"clang++ {' '.join(compile_flags)} -c dummy.cpp",
        "file": "cpp/common/Solution.h",
    }
    compile_commands.append(header_entry)

    output_path = workspace_root / "compile_commands.json"
    with open(output_path, "w") as f:
        json.dump(compile_commands, f, indent=2)

    print(f"Generated {output_path} with {len(compile_commands)} entries")
    print(f"nlohmann_json path: {nlohmann_path}")


if __name__ == "__main__":
    main()
