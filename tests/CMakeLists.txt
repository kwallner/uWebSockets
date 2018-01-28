if (WIN32)
    # Tests do not build for Windows
    return()
endif()

add_definitions(-DBUILDING_UWEBSOCKETS)

set(TARGET_NAME_POSTFIX _test)
foreach(BASENAME main)
	add_executable(${BASENAME}${TARGET_NAME_POSTFIX}
		${BASENAME}.cpp
		)

	target_link_libraries(${BASENAME}${TARGET_NAME_POSTFIX}
		PRIVATE
			${PROJECT_NAME}::uWS
		)
endforeach()