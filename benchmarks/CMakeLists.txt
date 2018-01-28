if (WIN32)
    # Tests do not build for Windows
    return()
endif()

add_definitions(-DBUILDING_UWEBSOCKETS)

set(TARGET_NAME_POSTFIX _bench)
# Missing: beast Reason: Not compiling
# Missing: crow Reason: Not compiling
# Missing: lws Reason: Not tested
# Missing: uWS Reason: Not tested
# Missing: wsPP Reason: Not tested
# Missing: scalability Reason: Not compiling (Unix only)
# Missing: scalability_socketio Reason: Not compiling (Unix only)
# Missing: throughput Reason: Not compiling
# Missing: throughput_socketio Reason: Not compiling
foreach(BASENAME scalability)
	add_executable(${BASENAME}${TARGET_NAME_POSTFIX}
		${BASENAME}.cpp
		)

	target_link_libraries(${BASENAME}${TARGET_NAME_POSTFIX}
		PRIVATE
			${PROJECT_NAME}::uWS
		)
endforeach()