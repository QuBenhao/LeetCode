cmake_minimum_required(VERSION 3.14)  # FetchContent requires 3.11+
project(LeetCode)

# Set global compiler and linker options
if (APPLE)
    # Use libc++ on macOS instead of the deprecated libstdc++
    add_compile_options(-stdlib=libc++)
    add_link_options(-stdlib=libc++)
endif ()

# Enable AddressSanitizer
add_compile_options(
        -O2
        -fsanitize=address
        -fno-omit-frame-pointer
)
add_link_options(
        -fsanitize=address
)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Manage external dependencies with FetchContent
include(FetchContent)

# 1. Integrate nlohmann_json (a header-only library)
FetchContent_Declare(
        nlohmann_json
        GIT_REPOSITORY https://github.com/nlohmann/json.git
        GIT_TAG v3.12.0
)
FetchContent_MakeAvailable(nlohmann_json)

# 2. Integrate GoogleTest
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
        DOWNLOAD_EXTRACT_TIMESTAMP TRUE  # Resolve timestamp warnings
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# Enable tests
enable_testing()

configure_file(${CMAKE_SOURCE_DIR}/.env ${CMAKE_BINARY_DIR}/.env COPYONLY)
file(READ "${CMAKE_BINARY_DIR}/.env" ENV_CONTENT)
# Read the problem configuration
string(REGEX MATCH "PROBLEM_FOLDER=\"([^\"]+)\"" _ ${ENV_CONTENT})
set(PROBLEM_FOLDER "${CMAKE_MATCH_1}")

# Read the daily problem JSON
set(DAILY_JSON "${CMAKE_SOURCE_DIR}/daily-${PROBLEM_FOLDER}.json")
configure_file(${DAILY_JSON} "${CMAKE_BINARY_DIR}/daily-${PROBLEM_FOLDER}.json" COPYONLY)
file(READ "${CMAKE_BINARY_DIR}/daily-${PROBLEM_FOLDER}.json" DAILY_JSON_CONTENT)

# Parse the JSON content
# Extract the daily problem ID
string(JSON DAILY_ID GET "${DAILY_JSON_CONTENT}" daily)

# Extract the plans array
string(JSON PLANS_LENGTH LENGTH "${DAILY_JSON_CONTENT}" plans)
set(PLANS_LIST "")

# Calculate the last valid index
math(EXPR MAX_INDEX "${PLANS_LENGTH} - 1")

# Iterate over the valid index range
foreach (INDEX RANGE 0 ${MAX_INDEX})
    string(JSON ELEMENT GET "${DAILY_JSON_CONTENT}" plans ${INDEX})
    list(APPEND PLANS_LIST "${ELEMENT}")
endforeach ()

# Create the test target list
set(TEST_TARGETS)

# Add the shared solution library
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

# 1. Add the daily problem
if (DAILY_ID AND NOT "${DAILY_ID}" STREQUAL "")
    # Normalize special characters in the ID
    string(REGEX REPLACE "[^a-zA-Z0-9]" "_" CLEAN_ID ${DAILY_ID})
    set(TARGET_NAME "daily")

    set(SOLUTION_SRC "${CMAKE_SOURCE_DIR}/${PROBLEM_FOLDER}/${PROBLEM_FOLDER}_${DAILY_ID}/Solution.cpp")
    set(TESTCASE_FILE "${CMAKE_SOURCE_DIR}/${PROBLEM_FOLDER}/${PROBLEM_FOLDER}_${DAILY_ID}/testcase")

    if (EXISTS ${SOLUTION_SRC})
        # Create the executable
        add_executable(${TARGET_NAME}
                ${SOLUTION_SRC}
                "${CMAKE_SOURCE_DIR}/cpp/TestMain.cpp"
        )

        # Link dependencies, including GMock
        target_link_libraries(${TARGET_NAME}
                PRIVATE
                common_solution
                models
                GTest::gtest_main
                GTest::gmock  # Enable GMock support
        )

        # Add the test target
        add_test(NAME ${TARGET_NAME}
                COMMAND ${TARGET_NAME} ${TESTCASE_FILE} --gtest_color=yes
        )

        # Set test properties
        set_tests_properties(${TARGET_NAME} PROPERTIES
                LABELS "leetcode;daily"
                TIMEOUT 3
        )

        list(APPEND TEST_TARGETS ${TARGET_NAME})
    else ()
        message(WARNING "Daily problem source not found: ${SOLUTION_SRC}")
    endif ()
endif ()

# 2. Add planned problems
set(SEEN_IDS "")  # Track processed problem IDs to avoid duplicates
set(INDEX 0)
while (INDEX LESS PLANS_LENGTH)
    # Read the problem ID
    list(GET PLANS_LIST ${INDEX} QID)
    math(EXPR INDEX "${INDEX} + 1")

    # Read the folder
    list(GET PLANS_LIST ${INDEX} FOLDER)
    math(EXPR INDEX "${INDEX} + 1")

    # Skip problem IDs already processed
    if (QID IN_LIST SEEN_IDS)
        continue()
    endif ()
    list(APPEND SEEN_IDS ${QID})

    # Normalize special characters in the ID
    string(REGEX REPLACE "[^a-zA-Z0-9]" "_" CLEAN_ID ${QID})
    set(TARGET_NAME "plan_${FOLDER}_${CLEAN_ID}")

    set(SOLUTION_SRC "${CMAKE_SOURCE_DIR}/${FOLDER}/${FOLDER}_${QID}/Solution.cpp")
    set(TESTCASE_FILE "${CMAKE_SOURCE_DIR}/${FOLDER}/${FOLDER}_${QID}/testcase")

    if (EXISTS ${SOLUTION_SRC})
        # Create the executable
        add_executable(${TARGET_NAME}
                ${SOLUTION_SRC}
                "${CMAKE_SOURCE_DIR}/cpp/TestMain.cpp"
        )

        # Link dependencies, including GMock
        target_link_libraries(${TARGET_NAME}
                PRIVATE
                common_solution
                models
                GTest::gtest_main
                GTest::gmock  # Enable GMock support
        )

        # Add the test target
        add_test(NAME ${TARGET_NAME}
                COMMAND ${TARGET_NAME} ${TESTCASE_FILE} --gtest_color=yes
        )

        # Set test properties
        set_tests_properties(${TARGET_NAME} PROPERTIES
                LABELS "leetcode;plan"
                TIMEOUT 3
        )

        list(APPEND TEST_TARGETS ${TARGET_NAME})
    else ()
        message(WARNING "Plan problem source not found: ${SOLUTION_SRC}")
    endif ()
endwhile ()

# Add the aggregate target
add_custom_target(run_all_tests
        COMMAND ctest --output-on-failure
        DEPENDS ${TEST_TARGETS}
        COMMENT "Running all LeetCode tests"
)

# Print the configuration summary
message(STATUS "Configured LeetCode project")
message(STATUS "  Problem folder: ${PROBLEM_FOLDER}")
message(STATUS "  Daily problem: ${DAILY_ID}")
message(STATUS "  Plan problems: ${SEEN_IDS}")
message(STATUS "  Total tests: ${TEST_TARGETS}")
