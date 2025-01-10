cmake_minimum_required(VERSION 3.8)
project(auv_description)

# Compiler flags for warnings
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)

# Uncomment the following section to fill in further dependencies manually.
# find_package(<dependency> REQUIRED)

# Install URDF/Xacro files
install(
  DIRECTORY urdf/
  DESTINATION share/${PROJECT_NAME}/urdf
)

# Install launch files
install(
  DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

# Install other resources if needed (like meshes)
# install(
#   DIRECTORY meshes/
#   DESTINATION share/${PROJECT_NAME}/meshes
# )

# Testing (optional)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # Skip the linter which checks for copyrights
  set(ament_cmake_copyright_FOUND TRUE)
  # Skip cpplint (only works in a git repo)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# Finalize the package
ament_package()

