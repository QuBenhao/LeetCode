cc_test(
    name = "test_problem_141",
    size = "small",
    srcs = [
        "//cpp:TestMain.cpp",
        "//cpp:TestMain.h",
        "//cpp/common:Solution.h",
        "@problem0//:Solution.cpp",
    ],
    args = [
        "$(rlocationpath @problem0//:testcase)",
    ],
    data = ["@problem0//:testcase"],
    deps = [
        "//cpp/models",
        "@bazel_tools//tools/cpp/runfiles",
        "@com_google_googletest//:gtest_main",
        "@nlohmann_json//:json",
    ],
)

cc_test(
    name = "test_problem_142",
    size = "small",
    srcs = [
        "//cpp:TestMain.cpp",
        "//cpp:TestMain.h",
        "//cpp/common:Solution.h",
        "@problem1//:Solution.cpp",
    ],
    args = [
        "$(rlocationpath @problem1//:testcase)",
    ],
    data = ["@problem1//:testcase"],
    deps = [
        "//cpp/models",
        "@bazel_tools//tools/cpp/runfiles",
        "@com_google_googletest//:gtest_main",
        "@nlohmann_json//:json",
    ],
)
