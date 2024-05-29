cc_library (
    name = "common",
    srcs = [
        "Solution.h",
        "@problems//:Solution.cpp"
    ],
    deps = [
        "@nlohmann_json//:json",
        "//cpp/models:models",
    ],
    visibility = ["//visibility:public"],
)

exports_files(["Solution.h"])