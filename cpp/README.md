# Cpp

## Start

First install bazel environment,

For daily:
**change daily in [daily.json](../daily-problems.json)** `Note: the json file is under root with your problem folder, named 'daily-${folder}.json'` and try:
```shell
bazel test --cxxopt=-std=c++23 --cxxopt=-O2 --cxxopt=-fsanitize=address --cxxopt=-D_GLIBCXX_USE_CXX11_ABI=1 --linkopt=-fsanitize=address --test_timeout=3 --test_output=all //cpp:solution_test
```

or for multiple problems from plans,
**change plans in [daily.json](../daily-problems.json)** `Note: the json file is under root with your problem folder, named 'daily-${folder}.json'` and try:
```shell
bazel test --cxxopt=-std=c++23 --cxxopt=-O2 --cxxopt=-fsanitize=address --cxxopt=-D_GLIBCXX_USE_CXX11_ABI=1 --linkopt=-fsanitize=address --test_timeout=10 --test_output=all //:all
```

## Environment setup for idea:

change line `generate_cc_tests(enabled = False)` to `generate_cc_tests(enabled = True)` in [BUILD](../BUILD)

[bazel-compile-commands-extractor](https://github.com/hedronvision/bazel-compile-commands-extractor)
```shell
bazel run @hedron_compile_commands//:refresh_all --cxxopt=-std=c++23 --cxxopt=-O2 --cxxopt=-fsanitize=address --cxxopt=-D_GLIBCXX_USE_CXX11_ABI=1 --linkopt=-fsanitize=address
```

Run all tests:
```shell
bazel test //... --cxxopt=-std=c++23 --cxxopt=-O2 --cxxopt=-fsanitize=address --cxxopt=-D_GLIBCXX_USE_CXX11_ABI=1 --linkopt=-fsanitize=address --test_timeout=3 --test_output=all
```
