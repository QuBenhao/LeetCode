# Cpp

## Start

First install bazel environment,

**change path of problem `    path = "problems/problems_2028/",` in [BAZEL WORKSPACE](../WORKSPACE)**, and try:
```shell
bazel test --cxxopt=-std=c++20 --test_timeout=3 --test_output=all //cpp:solution_test
```