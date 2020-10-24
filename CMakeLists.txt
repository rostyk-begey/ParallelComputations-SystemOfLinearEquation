cmake_minimum_required(VERSION 3.17)
project(Task3)

set(CMAKE_CXX_STANDARD 20)
SET(CMAKE_CXX_FLAGS -pthread)

add_executable(Task3 main.cpp Matrix.h Matrix.cpp ConsoleApp.cpp ConsoleApp.h)