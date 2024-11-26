cmake_minimum_required(VERSION 3.10)
project(CppProject)

set(CMAKE_CXX_STANDARD 17)

include_directories(include)

# Подключение Kafka
find_package(PkgConfig REQUIRED)
pkg_check_modules(RDKAFKA REQUIRED rdkafka)

add_executable(cpp_app main.cpp helpers.cpp)
target_link_libraries(cpp_app ${RDKAFKA_LIBRARIES})
