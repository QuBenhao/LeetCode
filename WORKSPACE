load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "com_google_googletest",
    strip_prefix = "googletest-5ab508a01f9eb089207ee87fd547d290da39d015",
    urls = ["https://github.com/google/googletest/archive/5ab508a01f9eb089207ee87fd547d290da39d015.zip"],
)

git_repository(
    name = "nlohmann_json",
    branch = "master",
    remote = "https://github.com/nlohmann/json.git",
)

new_local_repository(
    name = "problems",
    build_file = "//cpp:solution.BUILD",
    path = "problems/problems_3096/",
)

new_local_repository(
    name = "problem0",
    build_file = "//cpp:solution.BUILD",
    path = "problems/problems_141/",
)

new_local_repository(
    name = "problem1",
    build_file = "//cpp:solution.BUILD",
    path = "problems/problems_142/",
)
