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

http_archive(
    name = "rules_rust",
    integrity = "sha256-Weev1uz2QztBlDA88JX6A1N72SucD1V8lBsaliM0TTg=",
    urls = ["https://github.com/bazelbuild/rules_rust/releases/download/0.48.0/rules_rust-v0.48.0.tar.gz"],
)

load("@rules_rust//rust:repositories.bzl", "rules_rust_dependencies", "rust_register_toolchains")

rules_rust_dependencies()

rust_register_toolchains(
    edition = "2021",
    versions = [
        "1.79.0"
    ],
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

new_local_repository(
    name = "rust_problems",
    build_file = "//rust:solution.BUILD",
    path = "problems/problems_1/",
)