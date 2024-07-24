cc_test(
    name = "test_problem_49",
    size = "small",
    srcs = [
        "//cpp:TestMain.cpp",
        "//cpp:TestMain.h",
        "//cpp/common:Solution.h",
        "@problem0//:Solution.cpp"
    ],
    args = [
        "$(rlocationpath @problem0//:testcase)",
    ],
    data = ["@problem0//:testcase"],
    deps = [
        "//cpp/models:models",
        "@bazel_tools//tools/cpp/runfiles",
        "@com_google_googletest//:gtest_main",
        "@nlohmann_json//:json",
    ],
)

