#if (WIN32)
#	add_definitions(-D_WIN32_WINNT=0x0501)
#endif()

add_library(uWS SHARED
    Asio.h
    Backend.h
    CMakeLists.txt
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
add_library(uWebSockets::uWS ALIAS uWS)

target_include_directories(uWS
    PRIVATE
        source
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
    )

target_link_libraries(uWS
	PRIVATE
        libuv::uv
		Boost::boost
        OpenSSL::SSL
        ZLIB::ZLIB
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

if(MSVC)
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
