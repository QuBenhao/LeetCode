def add_files(name, path):
    native.filegroup(
        name = name,
        srcs = native.glob([
            "{}/*.cpp".format(path),
        ]),
    )
    native.filegroup(
        name = name + "_testcase",
        srcs = native.glob([
            "{}/testcase".format(path),
        ]),
    )

def create_cc_test(name, file_group):
    native.cc_library(
        name = "common_" + name,
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
        name = name,
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
            "//:common_" + name,
            "@bazel_tools//tools/cpp/runfiles",
            "@com_google_googletest//:gtest_main",
            "@nlohmann_json//:json",
        ],
    )

def generate_cc_tests():
    for subdir in native.glob(["problems/**/Solution.cpp"]):
        sub_dir_name = subdir.split("/")[1]
        dir_name = subdir.split("/Solution.cpp")[0]
        test_name = "test_" + sub_dir_name.replace("/", "_")
        add_files(name = sub_dir_name, path = dir_name)
        create_cc_test(name = test_name, file_group = sub_dir_name)
