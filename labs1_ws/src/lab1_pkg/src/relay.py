import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Relay(Node):
    def __init__(self):
        super().__init__('relay')
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive_relay', 10)
        self.subscription = self.create_subscription(
            AckermannDriveStamped,
            'drive',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        new_msg = AckermannDriveStamped()
        new_msg.drive.speed = msg.drive.speed * 3
        new_msg.drive.steering_angle = msg.drive.steering_angle * 3

        self.publisher_.publish(new_msg)
        self.get_logger().info(f'Publishing to drive_relay: speed: "{new_msg.drive.speed}" steering angle: "{new_msg.drive.steering_angle}"')

def main(args=None):
    rclpy.init(args=args)
    relay = Relay()
    rclpy.spin(relay)
    relay.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
