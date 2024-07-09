load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

http_archive(
  name = "com_google_googletest",
  urls = ["https://github.com/google/googletest/archive/5ab508a01f9eb089207ee87fd547d290da39d015.zip"],
  strip_prefix = "googletest-5ab508a01f9eb089207ee87fd547d290da39d015",
)

git_repository(
    name = "nlohmann_json",
    remote = "https://github.com/nlohmann/json.git",
    branch = "master",
)

new_local_repository(
    name = "problems",
    path = "problems/problems_3102/",
    build_file = "//cpp:solution.BUILD",
)

new_local_repository(
    name = "problem0",
    path = "problems/problems_160/",
    build_file = "//cpp:solution.BUILD",
)
