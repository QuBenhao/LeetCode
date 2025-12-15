cmake_minimum_required(VERSION 3.22)
project(OpenJudge CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 获取项目根目录
get_filename_component(PROJECT_ROOT ${CMAKE_CURRENT_SOURCE_DIR} ABSOLUTE)

# 递归查找所有 solution.cpp
file(GLOB_RECURSE SOLUTION_FILES "*/solution.cpp")

foreach(SOLUTION_FILE ${SOLUTION_FILES})
    # 获取相对于项目根目录的路径
    file(RELATIVE_PATH REL_PATH ${PROJECT_ROOT} ${SOLUTION_FILE})

    # 提取目录名
    get_filename_component(DIR_NAME ${REL_PATH} DIRECTORY)

    # 如果是在子目录中
    if(DIR_NAME)
        # 移除路径前缀，只保留最后一级目录
        get_filename_component(SHORT_DIR_NAME ${DIR_NAME} NAME)

        # 生成目标名（如果担心重名，可以加上父目录前缀）
        string(MAKE_C_IDENTIFIER ${DIR_NAME} TARGET_NAME)

        # 简化目标名：用下划线替换斜杠
        string(REPLACE "/" "_" TARGET_NAME ${DIR_NAME})

        # 添加可执行文件
        add_executable(${TARGET_NAME} ${SOLUTION_FILE})

        # 设置输出名为更友好的名称
        set_target_properties(${TARGET_NAME} PROPERTIES
                OUTPUT_NAME ${SHORT_DIR_NAME}
                RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
        )

        message(STATUS "Found: ${DIR_NAME}/solution.cpp -> ${TARGET_NAME} (输出: ${SHORT_DIR_NAME})")
    else()
        # 如果在根目录
        add_executable(root_solution ${SOLUTION_FILE})
        set_target_properties(root_solution PROPERTIES
                RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
        )
    endif()
endforeach()