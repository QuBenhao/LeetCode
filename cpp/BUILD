cc_test(
    name = "solution_test",
    size = "small",
    srcs = [
        "TestMain.cpp",
        "TestMain.h",
    ],
    args = [
        "$(rlocationpath @problems//:testcase)",
    ],
    data = ["@problems//:testcase"],
    deps = [
        "//cpp/common",
        "@bazel_tools//tools/cpp/runfiles",
        "@com_google_googletest//:gtest_main",
        "@nlohmann_json//:json",
    ],
)

cc_test(
    name = "premium_solution_test",
    size = "small",
    srcs = [
        "TestMain.cpp",
        "TestMain.h",
    ],
    args = [
        "$(rlocationpath @premium//:testcase)",
    ],
    data = ["@premium//:testcase"],
    deps = [
        "//cpp/common",
        "@bazel_tools//tools/cpp/runfiles",
        "@com_google_googletest//:gtest_main",
        "@nlohmann_json//:json",
    ],
)
