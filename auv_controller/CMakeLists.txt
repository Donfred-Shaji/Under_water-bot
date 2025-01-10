cmake_minimum_required(VERSION 3.5)
project(auv_controller)

# Dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Install Python scripts
install(
    PROGRAMS scripts/auv_controller.py
    DESTINATION lib/${PROJECT_NAME}
)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()

