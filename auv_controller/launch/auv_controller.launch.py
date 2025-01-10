import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='auv_controller',
            executable='auv_controller.py',
            name='auv_controller',
            output='screen',
        )
    ])

