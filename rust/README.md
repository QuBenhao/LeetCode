# Rust

## Start

Install rust environment by following the instructions in [Rust](https://www.rust-lang.org/tools/install).

Then, you can run the tests by running:
Simply, 
**add [dependencies] path question id in [Cargo.toml](../Cargo.toml)**,
and **change PROBLEM_ID in [test.rs](test_executor/tests/test.rs)**, and try:

```shell
cargo test --test solution_test
```

If you write to run more than one solution, 
you can 
**add [dependencies] path question id in [Cargo.toml](../Cargo.toml)**,
and **add more tests in [solution_test.rs](test_executor/tests/solutions_test.rs)**, and try:

```shell
cargo test --test solutions_test
```
