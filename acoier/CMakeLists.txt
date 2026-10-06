cmake_minimum_required(VERSION 3.22)
project(ACOIER CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Get the project root directory
get_filename_component(PROJECT_ROOT ${CMAKE_CURRENT_SOURCE_DIR} ABSOLUTE)

# Recursively find all solution*.cpp files
file(GLOB_RECURSE SOLUTION_FILES "*/solution*.cpp")

foreach(SOLUTION_FILE ${SOLUTION_FILES})
    # Get the path relative to the project root
    file(RELATIVE_PATH REL_PATH ${PROJECT_ROOT} ${SOLUTION_FILE})

    # Extract the directory name and filename
    get_filename_component(DIR_NAME ${REL_PATH} DIRECTORY)
    get_filename_component(FILE_NAME ${REL_PATH} NAME)
    get_filename_component(FILE_NAME_WE ${REL_PATH} NAME_WE)  # Filename without the extension

    # Extract the last directory component
    if(DIR_NAME)
        get_filename_component(SHORT_DIR_NAME ${DIR_NAME} NAME)

        # Generate the target name
        # Option 1: Combine the directory name and filename
        string(REPLACE "/" "_" TARGET_NAME ${DIR_NAME})
        set(TARGET_NAME "${TARGET_NAME}_${FILE_NAME_WE}")

        # Option 2: Use only the filename for a shorter target name (ensure it is unique)
        # Use option 1 here

        # Ensure the name is a valid identifier
        string(MAKE_C_IDENTIFIER ${TARGET_NAME} TARGET_NAME)

        # Set the output name
        # Combine the directory name and filename to avoid duplicate names
        set(OUTPUT_NAME "${SHORT_DIR_NAME}_${FILE_NAME_WE}")

        # Add the executable
        add_executable(${TARGET_NAME} ${SOLUTION_FILE})

        # Set output properties
        set_target_properties(${TARGET_NAME} PROPERTIES
                OUTPUT_NAME ${OUTPUT_NAME}
                RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
        )

        message(STATUS "Found: ${DIR_NAME}/${FILE_NAME} -> ${TARGET_NAME} (输出: ${OUTPUT_NAME})")
    else()
        # If the file is in the root directory
        add_executable(${FILE_NAME_WE} ${SOLUTION_FILE})
        set_target_properties(${FILE_NAME_WE} PROPERTIES
                RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
        )
        message(STATUS "Found: ${FILE_NAME} -> ${FILE_NAME_WE}")
    endif()
endforeach()
