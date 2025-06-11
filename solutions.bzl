# solutions.bzl

def add_files(fname, path):
    native.filegroup(
        name = fname,
        srcs = native.glob([
            "{}/*.cpp".format(path),
        ]),
    )
    native.filegroup(
        name = fname + "_testcase",
        srcs = native.glob([
            "{}/testcase".format(path),
        ]),
    )

def create_cc_tests(fname, file_group):
    native.cc_library(
        name = "common_" + fname,
        srcs = [
            "//cpp/common:Solution.h",
            "//:{}".format(file_group)
        ],
        hdrs = ["//cpp/common:Solution.h"],
        deps = [
            "@nlohmann_json//:json",
            "//cpp/models:models",
        ],
        visibility = ["//visibility:public"],
    )
    native.cc_test(
        name = fname + "_test",
        size = "small",
        srcs = [
            "//cpp:TestMain.cpp",
            "//cpp:TestMain.h",
        ],
        args = [
            "$(rlocationpath //:{})".format(file_group + "_testcase"),
        ],
        data = ["//:{}".format(file_group + "_testcase")],
        deps = [
            "//:common_" + fname,
            "@bazel_tools//tools/cpp/runfiles",
            "@googletest//:gtest_main",
            "@nlohmann_json//:json",
        ],
    )

def generate_cc_tests(enabled = False):
    if not enabled:
        return
    for subdir in native.glob(["*/**/Solution.cpp"]):
        sub_dir_name = subdir.split("/")[1]
        dir_name = subdir.split("/Solution.cpp")[0]
        test_name = "test_" + sub_dir_name.replace("/", "_")
        add_files(fname = sub_dir_name, path = dir_name)
        create_cc_tests(fname = test_name, file_group = sub_dir_name)

def gen_plans(plans):
    # split plans by comma
    for i, plan in enumerate(plans):
        fname = "problem%s" % i
        path = "%s/%s_%s" % ("problems", "problems", plan)
        test_name = "test_%s_%s" % ("problems", plan)
        add_files(fname = fname, path = path)
        create_cc_tests(fname = fname, file_group = fname)

