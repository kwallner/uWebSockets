#
# Policies
#
if(POLICY CMP0020)
    cmake_policy(SET CMP0020 NEW)
endif()
if(POLICY CMP0048)
    cmake_policy(SET CMP0048 NEW)
endif()

#
# Project
#
project(uWebSockets
    LANGUAGES CXX
    VERSION 0.13.0
    )

#
# Settings
#
set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(CMAKE_CXX_STANDARD 11)

#
# Settings
#
cmake_minimum_required(VERSION 3.5)
include (CTest)

#
# Use Conan.io
#
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
conan_define_targets()

#
# Packages from Conan.io
#
find_package(Boost REQUIRED)
add_library(libuv::uv UNKNOWN IMPORTED)
set_target_properties(libuv::uv PROPERTIES
    INTERFACE_INCLUDE_DIRECTORIES "${CONAN_INCLUDE_DIRS_LIBUV}")
if(WIN32)
    set_target_properties(libuv::uv PROPERTIES
        IMPORTED_LOCATION "${CONAN_LIB_DIRS_LIBUV}/libuv.lib")
else()
    set_target_properties(libuv::uv PROPERTIES
        IMPORTED_LOCATION "${CONAN_LIB_DIRS_LIBUV}/libuv.a")
endif()

find_package(ZLIB REQUIRED)
find_package(OpenSSL REQUIRED)

#
# Subdirectories
#
add_subdirectory(src)
add_subdirectory(examples)
add_subdirectory(benchmarks)
add_subdirectory(tests)

#
# Export
#
add_subdirectory(exports)

#
# Install
#
install(
    FILES
        "LICENSE"
        "README.md"
    DESTINATION
        . # Root Directory
    )
