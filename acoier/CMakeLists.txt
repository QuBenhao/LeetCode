cmake_minimum_required(VERSION 3.22)
project(ACOIER CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 获取项目根目录
get_filename_component(PROJECT_ROOT ${CMAKE_CURRENT_SOURCE_DIR} ABSOLUTE)

# 递归查找所有 solution*.cpp 文件
file(GLOB_RECURSE SOLUTION_FILES "*/solution*.cpp")

foreach(SOLUTION_FILE ${SOLUTION_FILES})
    # 获取相对于项目根目录的路径
    file(RELATIVE_PATH REL_PATH ${PROJECT_ROOT} ${SOLUTION_FILE})

    # 提取目录名和文件名
    get_filename_component(DIR_NAME ${REL_PATH} DIRECTORY)
    get_filename_component(FILE_NAME ${REL_PATH} NAME)
    get_filename_component(FILE_NAME_WE ${REL_PATH} NAME_WE)  # 不带扩展名的文件名

    # 提取目录的最后一级
    if(DIR_NAME)
        get_filename_component(SHORT_DIR_NAME ${DIR_NAME} NAME)

        # 生成目标名
        # 方案1: 用目录名+文件名组合
        string(REPLACE "/" "_" TARGET_NAME ${DIR_NAME})
        set(TARGET_NAME "${TARGET_NAME}_${FILE_NAME_WE}")

        # 方案2: 如果希望目标名更简洁，可以只用文件名(但要确保唯一性)
        # 这里用方案1

        # 确保是有效的标识符
        string(MAKE_C_IDENTIFIER ${TARGET_NAME} TARGET_NAME)

        # 设置输出名
        # 可以使用目录名+文件名组合，避免重名
        set(OUTPUT_NAME "${SHORT_DIR_NAME}_${FILE_NAME_WE}")

        # 添加可执行文件
        add_executable(${TARGET_NAME} ${SOLUTION_FILE})

        # 设置输出属性
        set_target_properties(${TARGET_NAME} PROPERTIES
                OUTPUT_NAME ${OUTPUT_NAME}
                RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
        )

        message(STATUS "Found: ${DIR_NAME}/${FILE_NAME} -> ${TARGET_NAME} (输出: ${OUTPUT_NAME})")
    else()
        # 如果在根目录
        add_executable(${FILE_NAME_WE} ${SOLUTION_FILE})
        set_target_properties(${FILE_NAME_WE} PROPERTIES
                RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
        )
        message(STATUS "Found: ${FILE_NAME} -> ${FILE_NAME_WE}")
    endif()
endforeach()