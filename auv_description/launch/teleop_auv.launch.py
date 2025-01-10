# File: teleop_auv.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launching teleop_twist_keyboard (keyboard control)
        Node(
            package='teleop_twist_keyboard',
            executable='teleop_twist_keyboard',
            name='teleop_twist_keyboard',
            output='screen',
            remappings=[('/cmd_vel', '/auv/cmd_vel')]  # Ensure this is the same topic as your AUV's velocity command
        ),
        
        # Alternatively, launch teleop_twist_joy for joystick control (uncomment below if using joystick)
        # Node(
        #     package='teleop_twist_joy',
        #     executable='teleop_twist_joy',
        #     name='teleop_twist_joy',
        #     output='screen',
        #     remappings=[('/cmd_vel', '/auv/cmd_vel')]  # Ensure this is the same topic as your AUV's velocity command
        # ),
    ])

