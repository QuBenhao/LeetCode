# Cpp

## Start

First install bazel environment,

**change path of problem `    path = "problems/problems_2028/",` in [BAZEL WORKSPACE](../WORKSPACE)**, and try:
```shell
bazel test --cxxopt=-std=c++20 --test_timeout=3 --test_output=all //cpp:solution_test
```

or if you want to run more than one questions,
**change problem and path in `new_local_repository(name = "problem0", path = "problems/problems_1/"` in [WORKSPACE](../WORKSPACE)** and maybe add the name ref `@problem0` in [BUILD](tests/BUILD), and try:
```shell
bazel test --cxxopt=-std=c++20 --test_timeout=10 --test_output=all //cpp/tests:all
```

## Environment setup for idea:
[bazel-compile-commands-extractor](https://github.com/hedronvision/bazel-compile-commands-extractor)
