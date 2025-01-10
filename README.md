# Under_water-bot
under water auv simulation using ros2humble
## Design Spesification
###Main Body (base_link):

Represents the main structure of the AUV.
Defined as a cylindrical shape with a blue material.
Inertial properties set (mass: 30.0 kg, inertia matrix values).

###Thrusters:

Six thrusters for propulsion and maneuverability.
Defined using the xacro:macro named thruster.
Positioned strategically:
Front left and right.
Back left and right.
Top left and right.
Each thruster is represented as a rectangular box with red material.
###Sensors:

Sensors are added using a xacro:macro named sensor.
Includes three sensors:
IMU: For orientation and motion sensing, represented as a box.
Camera: Positioned at the front, also a box.
Pressure Sensor: Positioned below the base, represented as a sphere.
###Key Features
Reusability with Xacro Macros:
thruster and sensor macros make the model modular, easy to extend, and maintain.
Geometry and Visual Elements:
Different shapes (box, sphere, cylinder) provide visual clarity.
Material colors (blue, red, green) distinguish components.
###Potential Improvements
Collision Properties:
Add more realistic collision geometries for thrusters and sensors to better simulate physical interactions.
###Sensor Integration:
Link the sensors to specific ROS plugins (e.g., camera and IMU sensors) for real-world simulation.
###Thruster Dynamics:
Implement dynamic behavior for thrusters using ROS control plugins or Gazebo simulation.
