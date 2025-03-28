cc_test(
    name = "test_problem_LCR_034",
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
        "@googletest//:gtest_main",
        "@nlohmann_json//:json",
    ],
)
