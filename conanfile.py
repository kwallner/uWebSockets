import os
import subprocess

from conans import ConanFile, tools, CMake
from conans.util import files

class uWebSocketsConan(ConanFile):
    name = "uWebSockets"
    version = "0.15.0"
    license = "BSD 3-clause \"New\" or \"Revised\" License"
    license_url = "https://raw.githubusercontent.com/uNetworking/uWebSockets/master/LICENSE"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    description = "lightweight, efficient & scalable WebSocket & HTTP server implementations"
    author = "Karl Wallner <kwallner@mail.de>"
    url = 'karl@xeon:/Repositories/repository.wak/conan-uWebSockets.git'
    exports_sources = "*"
    no_copy_source = True

    def requirements(self):
        self.requires("Boost/1.65.1@%s/%s" % ("kwallner", "testing"))
        self.requires("libuv/1.15.0@%s/%s" % ("kwallner", "testing"))
        self.requires("zlib/1.2.11@%s/%s" % ("kwallner", "testing"))
        self.requires("OpenSSL/1.0.2m@%s/%s" % ("kwallner", "testing"))

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_DEBUG_POSTFIX"]= "" # No postfix as distinct directories are used
        cmake.configure()
        #cmake.build()
        #cmake.install()
        #cmake.test()
