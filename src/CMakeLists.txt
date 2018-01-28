configure_file(uWS.h ${CMAKE_CURRENT_BINARY_DIR}/uWS/uWS.h @COPY_ONLY@)

add_library(uWS
    Asio.h
    Backend.h
    Epoll.cpp
    Epoll.h
    Extensions.cpp
    Extensions.h
    Group.cpp
    Group.h
    HTTPSocket.cpp
    HTTPSocket.h
    Hub.cpp
    Hub.h
    Libuv.h
    Networking.cpp
    Networking.h
    Node.cpp
    Node.h
    Socket.cpp
    Socket.h
    WebSocket.cpp
    WebSocket.h
    WebSocketProtocol.h
    uWS.h
    )
add_library(${PROJECT_NAME}::uWS ALIAS uWS)

target_include_directories(uWS
    PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
        $<INSTALL_INTERFACE:include>
        $<INSTALL_INTERFACE:include/uWS>
    )

target_link_libraries(uWS
	PRIVATE
        libuv::uv
		Boost::boost
        OpenSSL::SSL
        ZLIB::ZLIB
        $<$<PLATFORM_ID:Linux>:dl>
        $<$<PLATFORM_ID:Linux>:pthread>
        $<$<PLATFORM_ID:Windows>:Psapi>
        $<$<PLATFORM_ID:Windows>:Ws2_32>
        $<$<PLATFORM_ID:Windows>:Iphlpapi>
        $<$<PLATFORM_ID:Windows>:Userenv>
    )

set_target_properties(uWS
    PROPERTIES
        COMPILE_DEFINITIONS USE_LIBUV
        INTERFACE_COMPILE_DEFINITIONS USE_LIBUV
    )
	
set_target_properties(uWS
    PROPERTIES
        FOLDER libraries
        VERSION "${PROJECT_VERSION}"
        SOVERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}"
    )

install(TARGETS uWS
    EXPORT Targets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    )

if(MSVC AND BUILD_SHARED_LIBS)
    install(
        FILES $<TARGET_PDB_FILE:uWS>
        DESTINATION bin
        OPTIONAL
        )
endif()

INSTALL (
    FILES
        Asio.h
        Backend.h
        Epoll.h
        Extensions.h
        Group.h
        HTTPSocket.h
        Hub.h
        Libuv.h
        Networking.h
        Node.h
        Socket.h
        WebSocket.h
        WebSocketProtocol.h
        uWS.h
    DESTINATION 
        include/uWS
    )
