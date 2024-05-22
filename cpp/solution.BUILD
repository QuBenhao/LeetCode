cc_library(
    name = "solution",
    srcs = ["Solution.cpp", "Solution.h"],
    hdrs = ["@utils//:StringUtil.h"],
    deps = [
        "@nlohmann_json//:json",
        "@utils",
    ],
    visibility = ["//visibility:public"],

)

exports_files(["Solution.h", "Solution.cpp"])