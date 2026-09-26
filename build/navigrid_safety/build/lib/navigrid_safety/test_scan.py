import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class TestScan(Node):

    def __init__(self):
        super().__init__('test_scan')

        self.pub = self.create_publisher(
            LaserScan,
            '/scan',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.publish_scan
        )

    def publish_scan(self):

        msg = LaserScan()

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'lidar_link'

        msg.angle_min = -3.14
        msg.angle_max = 3.14
        msg.angle_increment = 0.01745

        msg.range_min = 0.05
        msg.range_max = 10.0

        # Simulated obstacle at 0.20 m
        msg.ranges = [0.20] * 360

        self.pub.publish(msg)


def main():
    rclpy.init()
    node = TestScan()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

