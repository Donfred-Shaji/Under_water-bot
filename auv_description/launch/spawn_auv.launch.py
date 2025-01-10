from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    # Path to the generated URDF file
    urdf_file = '/tmp/auv_model.urdf'

    # Path to the Gazebo world file (optional, replace with your custom world if necessary)
    gazebo_world_file = 'world/empty.world'

    return LaunchDescription([
        # Launch robot_state_publisher with the URDF file
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),

        # Launch RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
        ),

        # Launch Gazebo with ROS integration
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '--ros-args', '--plugin', 'gazebo_ros', '--world', gazebo_world_file],
            output='screen'
        ),

        # Spawn the robot in Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'auv', '-file', urdf_file],
            output='screen',
        ),
    ])

