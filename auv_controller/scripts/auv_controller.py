#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class AUVController(Node):
    def __init__(self):
        super().__init__('auv_controller')
        self.cmd_vel_subscriber = self.create_subscription(
            Twist,
            '/auv/cmd_vel',
            self.cmd_vel_callback,
            10
        )

    def cmd_vel_callback(self, msg):
        # Get linear and angular velocities from the message
        linear_x = msg.linear.x
        linear_y = msg.linear.y
        linear_z = msg.linear.z
        angular_x = msg.angular.x
        angular_y = msg.angular.y
        angular_z = msg.angular.z

        # Now apply these velocities to your thrusters or internal control systems
        # You need to interface with your thrusters' control logic here
        self.get_logger().info(f'Linear Velocity: {linear_x}, {linear_y}, {linear_z}')
        self.get_logger().info(f'Angular Velocity: {angular_x}, {angular_y}, {angular_z}')

def main(args=None):
    rclpy.init(args=args)
    auv_controller = AUVController()
    rclpy.spin(auv_controller)

    auv_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

