# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a LeetCode solutions repository with multi-language support. Each problem has a dedicated folder with solutions in Python, Go, Java, C++, TypeScript, and Rust.

## Project Structure

- `problems/problems_N/` - Solution folder for LeetCode problem N
  - `solution.py` - Python solution
  - `testcase.py` - Test cases
  - `solution.go`, `Solution.java`, `Solution.cpp`, `solution.rs`, `solution.ts` - Other language implementations
- `python/` - Base classes (`Solution`, `Testcase`) and CLI tools
- `algorithm_templates/` - Algorithm templates and patterns

## Development Commands

### Run Tests
```bash
# Single problem test (reads "daily" field from daily-{folder}.json)
python python/test.py

# Multiple problems test (reads "plans" field from daily-{folder}.json)
python python/tests.py
```

The JSON config file is `daily-{folder}.json` at repository root, where `{folder}` matches `PROBLEM_FOLDER` in `.env` (defaults to `problems` → `daily-problems.json`).

Example config:
```json
{
    "daily": "2751",
    "plans": ["3833", "problems", "3834", "problems"]
}
```
The `plans` array alternates between problem IDs and folder names.

### Main CLI Tool (fetch problems, submit solutions)
```bash
python python/scripts/leetcode.py
```

### Install Dependencies
```bash
pip install -r python/requirements.txt
```

### Environment Setup

Create a `.env` file at repository root with:
```env
PYTHONPATH=.
PROBLEM_FOLDER="problems"
```

Without `PYTHONPATH=.`, Python imports will fail with `ModuleNotFoundError: No module named 'python'`.

## Solution Template

```python
import solution
from typing import *

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.methodName(*test_input)

    def methodName(self, ...) -> ReturnType:
        # Implementation
        pass
```

## Testcase Template

```python
from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])

class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(Input=[...], Output=[...]))

    def get_testcases(self):
        return self.testcases
```

## Multi-Language Test Commands

All languages read from `daily-{folder}.json` config file **except Go and Rust** (see notes below).

| Language | Single Problem | Multiple Problems |
|----------|---------------|-------------------|
| Python | `python python/test.py` | `python python/tests.py` |
| Go | `go test -tags=goexperiment.jsonv2 golang/solution_test.go golang/test_basic.go -test.timeout 3s` | `go test -tags=goexperiment.jsonv2 golang/problems_test.go golang/test_basic.go -test.timeout 10s` |
| Java | `mvn test -Dtest="qubhjava.test.TestMain"` | `mvn test -Dtest="qubhjava.test.ProblemsTest"` |
| TypeScript | `npm test --alwaysStrict --strictBindCallApply --strictFunctionTypes --target ES2022 typescript/test.ts` | `npm test --alwaysStrict --strictBindCallApply --strictFunctionTypes --target ES2022 typescript/problems.test.ts` |
| C++ | `bazel test //:daily_test --cxxopt=-std=c++23 --cxxopt=-O2 --test_output=all` | `bazel test $(bazel query 'filter("plan_*", kind(cc_test, //...))') --cxxopt=-std=c++23 --test_output=all` |
| Rust | `cargo test --test solution_test` | `cargo test --test solutions_test` |

### Language-Specific Notes

**Go:**
- Requires `-tags=goexperiment.jsonv2` for `encoding/json/v2` (Go 1.25+)
- `solution_test.go` is **hardcoded** — must manually edit import path and problem ID:
  ```go
  import problem "leetCode/problems/problems_1"
  func TestSolution(t *testing.T) {
      TestEach(t, "1", "problems", problem.Solve)
  }
  ```

**Rust:**
- Test configuration requires dynamic setup (like Java):
  1. Run `python rust/cargo_setup.py` to generate minimal `Cargo.toml`
  2. Run `cargo test --test solution_test`
  3. Restore with `cp Cargo.toml.full Cargo.toml` when done
- The script reads `daily-{folder}.json` and only compiles configured problems

**TypeScript:**
- Requires `npm install` first to get `jest`

**Environment Dependencies:**
- Java: Maven (`mvn`)
- TypeScript: Node.js + npm
- C++: Bazel
- Rust: Cargo

## Architecture Notes

- Base classes `Solution` and `Testcase` in `python/solution.py` and `python/testcase.py` define abstract `solve()` and `get_testcases()` methods
- Test runner dynamically imports `solution.py` and `testcase.py` from problem folders using `importlib`
- Language writers in `python/lc_libs/` handle multi-language solution generation and submission
