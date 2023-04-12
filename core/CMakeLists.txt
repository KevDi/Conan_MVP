cmake_minimum_required(VERSION 3.15)
project(Core CXX)

find_package(Poco REQUIRED)

add_library(Core src/Core.cpp)
target_include_directories(Core PUBLIC include)

set_target_properties(Core PROPERTIES PUBLIC_HEADER "include/Core/Core.h;include/Core/export.h")

target_compile_definitions(Core PRIVATE -D_EXPORT)

target_link_libraries(Core PRIVATE Poco::Foundation)

install(TARGETS Core
PUBLIC_HEADER DESTINATION include/Core)
