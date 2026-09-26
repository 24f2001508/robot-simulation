#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan


class SafetyOverride(Node):

    def __init__(self):
        super().__init__('safety_override')

        self.current_speed = 0.0
        self.min_distance = float('inf')

        self.k = 0.5
        self.dmin = 0.30

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.timer = self.create_timer(
            0.05,
            self.safety_check
        )

        self.get_logger().info(
            'Safety Override Node started'
        )

    def odom_callback(self, msg):
        vx = msg.twist.twist.linear.x
        vy = msg.twist.twist.linear.y

        self.current_speed = math.sqrt(
            vx * vx + vy * vy
        )

    def scan_callback(self, msg):
        valid_ranges = [
            r for r in msg.ranges
            if math.isfinite(r)
            and r >= msg.range_min
            and r <= msg.range_max
        ]

        if valid_ranges:
            self.min_distance = min(valid_ranges)
        else:
            self.min_distance = float('inf')

    def safety_check(self):

        d_safe = (
            self.k * self.current_speed * self.current_speed
            + self.dmin
        )

        if self.min_distance <= d_safe:

            stop = Twist()

            self.cmd_pub.publish(stop)

            self.get_logger().warn(
                f'EMERGENCY STOP: obstacle={self.min_distance:.2f} m '
                f'safe_distance={d_safe:.2f} m'
            )


def main(args=None):

    rclpy.init(args=args)

    node = SafetyOverride()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
