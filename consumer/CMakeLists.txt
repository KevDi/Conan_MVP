cmake_minimum_required(VERSION 3.15)
project(Consumer CXX)

find_package(Core REQUIRED)

add_library(Consumer src/Consumer.cpp)
target_include_directories(Consumer PUBLIC include)

set_target_properties(Consumer PROPERTIES PUBLIC_HEADER "include/Consumer/Consumer.h;include/Consumer/export.h")

target_compile_definitions(${PROJECT_NAME} PRIVATE -D_EXPORT)

target_link_libraries(Consumer PRIVATE core::core)

install(TARGETS Consumer
PUBLIC_HEADER DESTINATION include/Consumer)
