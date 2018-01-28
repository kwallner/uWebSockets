#
# Create Config Files
#
install(EXPORT Targets
    FILE Targets.cmake
    NAMESPACE ${PROJECT_NAME}::
    DESTINATION share/cmake/${PROJECT_NAME}
    )

#
# Export Interface
#
include(CMakePackageConfigHelpers)

write_basic_package_version_file("${PROJECT_NAME}ConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
    )

configure_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/LibraryConfig.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    @ONLY
    )

install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
    DESTINATION
        . # Root Directory
    )

