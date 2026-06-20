cmake_minimum_required(VERSION 3.24)

project(quant_all_in_one VERSION 0.1.0 LANGUAGES CXX)

option(QUANTLAB_BUILD_TESTS "Build C++ tests" ON)
option(QUANTLAB_BUILD_BENCHMARKS "Build C++ benchmarks" OFF)
option(QUANTLAB_ENABLE_SANITIZERS "Enable sanitizers" OFF)
option(QUANTLAB_BUILD_PYBIND "Build Python extension module" OFF)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(quantlab_core
  cpp/src/bsm.cpp
  cpp/src/event_engine.cpp
  cpp/src/factor_engine.cpp
  cpp/src/optimizer.cpp
  cpp/src/risk_engine.cpp
)

target_include_directories(quantlab_core PUBLIC cpp/include)
target_compile_features(quantlab_core PUBLIC cxx_std_20)

if(MSVC)
  target_compile_options(quantlab_core PRIVATE /W4)
else()
  target_compile_options(quantlab_core PRIVATE -Wall -Wextra -Wpedantic)
endif()

if(QUANTLAB_ENABLE_SANITIZERS AND NOT MSVC)
  target_compile_options(quantlab_core PRIVATE -fsanitize=address,undefined -fno-omit-frame-pointer)
  target_link_options(quantlab_core PRIVATE -fsanitize=address,undefined)
endif()

if(QUANTLAB_BUILD_PYBIND)
  find_package(pybind11 CONFIG REQUIRED)
  pybind11_add_module(_quantlab_core cpp/bindings/pybind_module.cpp)
  target_link_libraries(_quantlab_core PRIVATE quantlab_core)
endif()

if(QUANTLAB_BUILD_TESTS)
  enable_testing()
  find_package(GTest CONFIG QUIET)
  if(GTest_FOUND)
    add_executable(quantlab_cpp_tests
      cpp/tests/test_bsm.cpp
      cpp/tests/test_factor_engine.cpp
      cpp/tests/test_optimizer.cpp
    )
    target_link_libraries(quantlab_cpp_tests PRIVATE quantlab_core GTest::gtest_main)
    include(GoogleTest)
    gtest_discover_tests(quantlab_cpp_tests)
  else()
    message(STATUS "GTest not found; skipping C++ tests")
  endif()
endif()

if(QUANTLAB_BUILD_BENCHMARKS)
  find_package(benchmark CONFIG QUIET)
  if(benchmark_FOUND)
    add_executable(bench_factor_engine cpp/benchmarks/bench_factor_engine.cpp)
    target_link_libraries(bench_factor_engine PRIVATE quantlab_core benchmark::benchmark_main)

    add_executable(bench_event_engine cpp/benchmarks/bench_event_engine.cpp)
    target_link_libraries(bench_event_engine PRIVATE quantlab_core benchmark::benchmark_main)
  else()
    message(STATUS "Google Benchmark not found; skipping C++ benchmarks")
  endif()
endif()
