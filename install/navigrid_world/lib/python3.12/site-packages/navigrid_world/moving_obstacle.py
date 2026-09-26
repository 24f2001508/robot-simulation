import math

import rclpy
from rclpy.node import Node
from gz.msgs10 import Entity
from gz.transport13 import Node as GazeboNode


class MovingObstacle(Node):

    def __init__(self):
        super().__init__('moving_obstacle')

        self.gz_node = GazeboNode()
        self.start_time = self.get_clock().now()

        self.timer = self.create_timer(0.1, self.move_obstacle)

    def move_obstacle(self):
        elapsed = (
            self.get_clock().now() - self.start_time
        ).nanoseconds / 1e9

        x = 4.0 * math.sin(elapsed * 0.5)

        msg = Entity()
        msg.name = 'moving_obstacle'
        msg.type = Entity.MODEL
        msg.pose.position.x = x
        msg.pose.position.y = 4.0
        msg.pose.position.z = 0.5

        self.gz_node.request(
            '/world/competition_world/set_pose',
            msg,
            100
        )


def main():
    rclpy.init()
    node = MovingObstacle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

