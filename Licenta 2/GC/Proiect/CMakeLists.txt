cmake_minimum_required(VERSION 3.15)
project(Proiect)

set(CMAKE_CXX_STANDARD 14)

include_directories("C:/freeglut/include")
link_directories("C:/freeglut/lib")

add_executable(demo main.cpp Graphics.cpp)
target_link_libraries(demo freeglut glu32 opengl32)
