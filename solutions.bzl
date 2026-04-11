# solutions.bzl

load("@rules_cc//cc:cc_test.bzl", "cc_test")

def _get_resolved_path(path, link_mappings):
    """Get the resolved path for a problem, following links if necessary."""
    folder_name = path.rsplit("/", 1)[-1] if "/" in path else path
    if folder_name in link_mappings:
        linked_folder = link_mappings[folder_name]
        parent = path.rsplit("/", 1)[0] if "/" in path else ""
        return parent + "/" + linked_folder if parent else linked_folder
    return path

def add_files(fname, path, link_mappings = {}):
    # Resolve link if necessary
    resolved_path = _get_resolved_path(path, link_mappings)

    native.filegroup(
        name = fname,
        srcs = native.glob([
            "{}/*.cpp".format(resolved_path),
        ]),
    )
    native.filegroup(
        name = fname + "_testcase",
        srcs = native.glob([
            "{}/testcase".format(path),
        ]),
    )

def create_cc_tests(fname, file_group):
    cc_test(
        name = fname + "_test",
        size = "small",
        srcs = [
            "//:{}".format(file_group),
            "//cpp:TestMain.cpp",
            "//cpp:TestMain.h",
            "//cpp/common:Solution.h",
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

def generate_cc_tests(link_mappings = {}):
    for subdir in native.glob(["*/**/Solution.cpp"]):
        if subdir.startswith("acoier/"):
            continue
        sub_dir_name = subdir.split("/")[1]
        dir_name = subdir.split("/Solution.cpp")[0]
        test_name = sub_dir_name.replace("/", "_")
        add_files(fname = sub_dir_name, path = dir_name, link_mappings = link_mappings)
        create_cc_tests(fname = test_name, file_group = sub_dir_name)

def gen_daily(folder, problem, plans, link_mappings = {}):
    # split plans by comma
    fname = "daily"
    path = "%s/%s_%s" % (folder, folder, problem)
    add_files(fname = fname, path = path, link_mappings = link_mappings)
    create_cc_tests(fname = fname, file_group = fname)
    for i in range(0, len(plans), 2):
        fname = "problem%s" % (i // 2)
        plan = plans[i]
        f = plans[i + 1]
        path = "%s/%s_%s" % (f, f, plan)
        test_name = "plan_%s_%s" % (f, plan)
        add_files(fname = fname, path = path, link_mappings = link_mappings)
        create_cc_tests(fname = test_name, file_group = fname)
