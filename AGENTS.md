# Repository Guidelines

## Project Structure & Module Organization

This repository stores LeetCode solutions, local runners, and code-generation tooling across several languages. Problem folders live under `problems/problems_<id>/` and usually contain `problem.md`, `problem_zh.md`, `solution.*`, `Solution.*`, `solution.md`, and testcase files. Shared language helpers are in `python/`, `golang/`, `typescript/`, `cpp/`, and `rust/`; reusable algorithm notes are in `algorithm_templates/`; metadata is in `data/`; automated tests are in `tests/`. Multithreading problems have their own layout under `multi_threading/<id>/`.

## Build, Test, and Development Commands

- `make verify`: run stable local checks across Python codegen/unit tests, TypeScript smoke tests, and Go helper packages.
- `make test`: run the full Python pytest suite with `PYTHONPATH=.`.
- `make test-unit`: run fast unit tests marked `unit`.
- `make test-integration`: run integration tests that may require language runtimes.
- `make test-codegen`: validate code generation behavior.
- `make test-coverage`: run pytest with terminal and HTML coverage reports.
- `npm test`: run the full TypeScript/Jest suite through `ts-jest`.
- `make test-go-libs`: run stable Go helper package tests.
- `python python/scripts/leetcode.py`: launch the interactive LeetCode helper for fetching/submitting problems.

Use `make help` for the maintained command list.

## Coding Style & Naming Conventions

Follow the style of the target language and existing generated files. Python uses pytest-compatible modules and 4-space indentation. Go code should be `gofmt` formatted. TypeScript uses lowercase filenames in `typescript/` and Jest test files such as `debug.test.ts`. Problem directories use `problems_<id>` naming, with language-specific solution names like `solution.py`, `solution.go`, `solution.ts`, `solution.rs`, `Solution.cpp`, and `Solution.java`.

## Testing Guidelines

Pytest discovers `test_*.py` and `*_test.py` under `tests/`; test classes start with `Test`, and test functions start with `test_`. Use markers from `pytest.ini`: `unit`, `integration`, `codegen`, and `slow`. For problem-level validation, run `make test-daily`, `make test-problems`, or the relevant language command. Add focused tests when changing code generation, language writers, shared models, or testcase parsing.

## Commit & Pull Request Guidelines

Recent commits use short prefixes such as `test:` and `fix:`; examples include `test: 3742 solution`, `test: [20260430] Add (3742)`, and `fix: 题解链接bug`. Keep messages imperative or descriptive, scoped to one change. Pull requests should summarize changed problems or tooling, list test commands run, mention required environment variables, and link related issues when applicable. Include screenshots only for documentation or UI-facing changes.

## Security & Configuration Tips

Do not commit `.env`, LeetCode cookies, PushDeer keys, or other secrets. Required local values include `COOKIE`, `PROBLEM_FOLDER`, `LANGUAGES`, `LEETCODE_USER`, and `PYTHONPATH=.`; see `README.md` for an example configuration.
