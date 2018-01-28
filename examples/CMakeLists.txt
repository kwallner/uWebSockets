add_definitions(-DBUILDING_UWEBSOCKETS)

set(TARGET_NAME_POSTFIX _example)
foreach(BASENAME echo;multithreaded_echo)
	add_executable(${BASENAME}${TARGET_NAME_POSTFIX}
		${BASENAME}.cpp
		)

	target_link_libraries(${BASENAME}${TARGET_NAME_POSTFIX}
		PRIVATE
			${PROJECT_NAME}::uWS
		)
endforeach()