# Repository Guidelines

## Project Structure
Problem folders: `problems/problems_<id>/` with `problem.md`, `problem_zh.md`, `solution.*`, `Solution.*`, `solution.md`, testcases. Shared helpers: `python/`, `golang/`, `typescript/`, `cpp/`, `rust/`. Algorithm notes: `algorithm_templates/`. Metadata: `data/`. Tests: `tests/`. Multithreading: `multi_threading/<id>/`.

## Build & Test
- `make verify`: stable local checks (Python codegen/unit, TypeScript smoke, Go helpers)
- `make health`: scan for missing docs/testcases/links/solutions, Rust workspace drift
- `make test` / `make test-unit` / `make test-integration` / `make test-codegen` / `make test-coverage`
- `npm test`: TypeScript/Jest suite
- `make test-go-libs`: Go helper package tests
- `python python/scripts/leetcode.py`: interactive LeetCode helper (fetch/submit)
- `make help`: full command list

## Solution Style
- Python: concise, trick-oriented, avoid boilerplate
- Prefer math/insight over brute force
- One clean approach per solution file, not multiple explorations

## Commit
Use short prefixes: `test:`, `fix:`, `feat:`. Keep scoped to one change.

## Done Means
- Solution passes test cases (local runner or LeetCode submit)
- No leftover debug prints or commented-out code
- If tooling changed: `make verify` passes
- Changed files summarized

## Security
Do not commit `.env`, LeetCode cookies, PushDeer keys. Required env vars: `COOKIE`, `PROBLEM_FOLDER`, `LANGUAGES`, `LEETCODE_USER`, `PYTHONPATH=.`.

Use `agent-preferences.json` for non-secret language and folder preferences.
Never read `.env`, its copies, browser cookies, or credential stores for those
values. Keep credentials out of agent instructions, terminal output, and test
fixtures. Authenticated fetch/submission and cookie refresh belong in the
owner's separate terminal, without sending credential output to an agent.

Start Claude Code at the repository root so `.claude/settings.json` loads.
It denies `.env` reads and edits, including nested copies, and requires shell
sandboxing without unsandboxed retries. The settings are intended for current
Claude Code on macOS or Linux/WSL2; unsupported sandbox environments fail closed.
`claude doctor` checks configuration errors, and `/status` and `/sandbox` show
the loaded configuration. Do not override these protections for a failing tool.
Git ignores are not access controls, and these Claude settings do not configure
other agents. Review their filesystem permissions separately.
