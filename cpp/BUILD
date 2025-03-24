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
        "@googletest//:gtest_main",
        "@nlohmann_json//:json",
    ],
)

exports_files(["TestMain.cpp","TestMain.h"])