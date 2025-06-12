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
    native.cc_test(
        name = fname + "_test",
        size = "small",
        srcs = [
            "//:{}".format(file_group),
            "//cpp:TestMain.cpp",
            "//cpp:TestMain.h",
            "//cpp/common:Solution.h"
        ],
        args = [
            "$(rlocationpath //:{})".format(file_group + "_testcase"),
        ],
        data = [
            "//:{}".format(file_group + "_testcase"),
        ],
        deps = [
            "//cpp/models:models",
            "@bazel_tools//tools/cpp/runfiles",
            "@googletest//:gtest_main",
            "@nlohmann_json//:json",
        ],
        stamp = 1,
    )

def generate_cc_tests():
    for subdir in native.glob(["*/**/Solution.cpp"]):
        sub_dir_name = subdir.split("/")[1]
        dir_name = subdir.split("/Solution.cpp")[0]
        test_name = sub_dir_name.replace("/", "_")
        add_files(fname = sub_dir_name, path = dir_name)
        create_cc_tests(fname = test_name, file_group = sub_dir_name)

def gen_daily(folder, problem, plans):
    # split plans by comma
    fname = "daily"
    path = "%s/%s_%s" % (folder, folder, problem)
    add_files(fname = fname, path = path)
    create_cc_tests(fname = fname, file_group = fname)
    for i in range(0, len(plans), 2):
        fname = "problem%s" % (i//2)
        plan = plans[i]
        f = plans[i+1]
        path = "%s/%s_%s" % (f, f, plan)
        test_name = "plan_%s_%s" % (f, plan)
        add_files(fname = fname, path = path)
        create_cc_tests(fname = test_name, file_group = fname)
