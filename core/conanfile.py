from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.build import check_max_cppstd, check_min_cppstd


class coreRecipe(ConanFile):
    name = "core"
    version = "1.0"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of hello package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True,
        "poco*:shared": True,
        "poco*:enable_activerecord":False,
        "poco*:enable_activerecord_compiler":False,
        "poco*:enable_apacheconnector":False,
        "poco*:enable_cppparser":False,
        "poco*:enable_crypto":False,
        "poco*:enable_data":False,
        "poco*:enable_data_mysql":False,
        "poco*:enable_data_odbc":False,
        "poco*:enable_data_postgresql":False,
        "poco*:enable_data_sqlite":False,
        "poco*:enable_encodings":False,
        "poco*:enable_json":False,
        "poco*:enable_jwt":False,
        "poco*:enable_mongodb":False,
        "poco*:enable_net":False,
        "poco*:enable_netssl":False,
        "poco*:enable_netssl_win":False,
        "poco*:enable_pagecompiler":False,
        "poco*:enable_pagecompiler_file2page":False,
        "poco*:enable_pdf":False,
        "poco*:enable_pocodoc":False,
        "poco*:enable_prometheus":False,
        "poco*:enable_redis":False,
        "poco*:enable_sevenzip":False,
        "poco*:enable_util":False,
        "poco*:enable_xml":False,
        "poco*:enable_zip":False
    }

    generators = "CMakeDeps"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def validate(self):
        check_min_cppstd(self, "11")
        check_max_cppstd(self, "17")

    def requirements(self):
        self.requires("poco/1.12.4", transitive_headers=True)
    
    def config_options(self):
        pass

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["core"]
