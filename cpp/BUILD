cc_test(
    name = "hello_test",
    size = "small",
    srcs = [
        "TestMain.cpp",
        "TestMain.h",
        "@problems//:Solution.h",
    ],
    deps = [
        "@nlohmann_json//:json",
        "@com_google_googletest//:gtest_main",
        "@utils//:utils",
        "@problems//:solution",  
    ],
)
