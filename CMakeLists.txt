cmake_minimum_required(VERSION 3.14)  # FetchContent需要3.11+
project(LeetCode)

# 设置全局编译和链接选项
if (APPLE)
    # macOS 上使用 libc++ 而不是已弃用的 libstdc++
    add_compile_options(-stdlib=libc++)
    add_link_options(-stdlib=libc++)
endif ()

# 启用地址消毒器
add_compile_options(
        -O2
        -fsanitize=address
        -fno-omit-frame-pointer
)
add_link_options(
        -fsanitize=address
)

# 设置C++标准
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 使用FetchContent管理外部依赖
include(FetchContent)

# 1. 集成nlohmann_json (仅头文件库)
FetchContent_Declare(
        nlohmann_json
        GIT_REPOSITORY https://github.com/nlohmann/json.git
        GIT_TAG v3.12.0
)
FetchContent_MakeAvailable(nlohmann_json)

# 2. 集成GoogleTest
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
        DOWNLOAD_EXTRACT_TIMESTAMP TRUE  # 解决时间戳警告
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# 启用测试
enable_testing()

configure_file(${CMAKE_SOURCE_DIR}/.env ${CMAKE_BINARY_DIR}/.env COPYONLY)
file(READ "${CMAKE_BINARY_DIR}/.env" ENV_CONTENT)
# 读取问题配置
string(REGEX MATCH "PROBLEM_FOLDER=\"([^\"]+)\"" _ ${ENV_CONTENT})
set(PROBLEM_FOLDER "${CMAKE_MATCH_1}")

# 读取每日问题JSON
set(DAILY_JSON "${CMAKE_SOURCE_DIR}/daily-${PROBLEM_FOLDER}.json")
configure_file(${DAILY_JSON} "${CMAKE_BINARY_DIR}/daily-${PROBLEM_FOLDER}.json" COPYONLY)
file(READ "${CMAKE_BINARY_DIR}/daily-${PROBLEM_FOLDER}.json" DAILY_JSON_CONTENT)

# 解析JSON内容
# 提取daily问题ID
string(JSON DAILY_ID GET "${DAILY_JSON_CONTENT}" daily)

# 提取plans数组
string(JSON PLANS_LENGTH LENGTH "${DAILY_JSON_CONTENT}" plans)
set(PLANS_LIST "")

# 正确计算最大索引
math(EXPR MAX_INDEX "${PLANS_LENGTH} - 1")

# 使用正确的范围循环
foreach (INDEX RANGE 0 ${MAX_INDEX})
    string(JSON ELEMENT GET "${DAILY_JSON_CONTENT}" plans ${INDEX})
    list(APPEND PLANS_LIST "${ELEMENT}")
endforeach ()

# 创建测试目标列表
set(TEST_TARGETS)

# 添加公共解决方案库
add_library(common_solution INTERFACE)
target_include_directories(common_solution INTERFACE
        "${CMAKE_SOURCE_DIR}"
)
target_link_libraries(common_solution INTERFACE
        nlohmann_json::nlohmann_json
)

file(GLOB MODELS_SRC
        "${CMAKE_SOURCE_DIR}/cpp/models/*.cpp"
        "${CMAKE_SOURCE_DIR}/cpp/models/*.h"
)
add_library(models STATIC
        ${MODELS_SRC}
)
target_include_directories(models PUBLIC
        ${CMAKE_SOURCE_DIR}/cpp/models
)
target_link_libraries(models PUBLIC
        nlohmann_json::nlohmann_json
)

target_compile_definitions(common_solution INTERFACE
        -DBUILD_CMAKE=1
)
target_compile_definitions(models PUBLIC
        -DBUILD_CMAKE=1
)

# 1. 添加每日问题
if (DAILY_ID AND NOT "${DAILY_ID}" STREQUAL "")
    # 清理ID中的特殊字符
    string(REGEX REPLACE "[^a-zA-Z0-9]" "_" CLEAN_ID ${DAILY_ID})
    set(TARGET_NAME "daily")

    set(SOLUTION_SRC "${CMAKE_SOURCE_DIR}/${PROBLEM_FOLDER}/${PROBLEM_FOLDER}_${DAILY_ID}/Solution.cpp")
    set(TESTCASE_FILE "${CMAKE_SOURCE_DIR}/${PROBLEM_FOLDER}/${PROBLEM_FOLDER}_${DAILY_ID}/testcase")

    if (EXISTS ${SOLUTION_SRC})
        # 创建可执行文件
        add_executable(${TARGET_NAME}
                ${SOLUTION_SRC}
                "${CMAKE_SOURCE_DIR}/cpp/TestMain.cpp"
        )

        # 链接依赖项 - 添加GMock支持
        target_link_libraries(${TARGET_NAME}
                PRIVATE
                common_solution
                models
                GTest::gtest_main
                GTest::gmock  # 添加GMock支持
        )

        # 添加测试目标
        add_test(NAME ${TARGET_NAME}
                COMMAND ${TARGET_NAME} ${TESTCASE_FILE} --gtest_color=yes
        )

        # 设置测试属性
        set_tests_properties(${TARGET_NAME} PROPERTIES
                LABELS "leetcode;daily"
                TIMEOUT 3
        )

        list(APPEND TEST_TARGETS ${TARGET_NAME})
    else ()
        message(WARNING "Daily problem source not found: ${SOLUTION_SRC}")
    endif ()
endif ()

# 2. 添加计划问题
set(SEEN_IDS "")  # 跟踪已处理的问题ID避免重复
set(INDEX 0)
while (INDEX LESS PLANS_LENGTH)
    # 获取问题ID
    list(GET PLANS_LIST ${INDEX} QID)
    math(EXPR INDEX "${INDEX} + 1")

    # 获取文件夹
    list(GET PLANS_LIST ${INDEX} FOLDER)
    math(EXPR INDEX "${INDEX} + 1")

    # 跳过已处理的问题ID
    if (QID IN_LIST SEEN_IDS)
        continue()
    endif ()
    list(APPEND SEEN_IDS ${QID})

    # 清理ID中的特殊字符
    string(REGEX REPLACE "[^a-zA-Z0-9]" "_" CLEAN_ID ${QID})
    set(TARGET_NAME "plan_${FOLDER}_${CLEAN_ID}")

    set(SOLUTION_SRC "${CMAKE_SOURCE_DIR}/${FOLDER}/${FOLDER}_${QID}/Solution.cpp")
    set(TESTCASE_FILE "${CMAKE_SOURCE_DIR}/${FOLDER}/${FOLDER}_${QID}/testcase")

    if (EXISTS ${SOLUTION_SRC})
        # 创建可执行文件
        add_executable(${TARGET_NAME}
                ${SOLUTION_SRC}
                "${CMAKE_SOURCE_DIR}/cpp/TestMain.cpp"
        )

        # 链接依赖项 - 添加GMock支持
        target_link_libraries(${TARGET_NAME}
                PRIVATE
                common_solution
                models
                GTest::gtest_main
                GTest::gmock  # 添加GMock支持
        )

        # 添加测试目标
        add_test(NAME ${TARGET_NAME}
                COMMAND ${TARGET_NAME} ${TESTCASE_FILE} --gtest_color=yes
        )

        # 设置测试属性
        set_tests_properties(${TARGET_NAME} PROPERTIES
                LABELS "leetcode;plan"
                TIMEOUT 3
        )

        list(APPEND TEST_TARGETS ${TARGET_NAME})
    else ()
        message(WARNING "Plan problem source not found: ${SOLUTION_SRC}")
    endif ()
endwhile ()

# 添加汇总目标
add_custom_target(run_all_tests
        COMMAND ctest --output-on-failure
        DEPENDS ${TEST_TARGETS}
        COMMENT "Running all LeetCode tests"
)

# 打印配置摘要
message(STATUS "Configured LeetCode project")
message(STATUS "  Problem folder: ${PROBLEM_FOLDER}")
message(STATUS "  Daily problem: ${DAILY_ID}")
message(STATUS "  Plan problems: ${SEEN_IDS}")
message(STATUS "  Total tests: ${TEST_TARGETS}")