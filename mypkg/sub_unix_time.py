# SPDX-FileCopyrightText: 2023 Yujiro Shito
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from datetime import datetime, timezone

class Listener():
    def __init__(self, node):
        self.node = node
        self.sub = node.create_subscription(Int64, "unix_time", self.cb, 10)

    def cb(self, msg):
        unix_time = msg.data
        converted_time = self.convert_unix_to_datetime(unix_time)
        self.node.get_logger().info("Unix time: %d, Date time: %s" % (unix_time, converted_time))

    def convert_unix_to_datetime(self, unix_time):
        
        dt_object = datetime.fromtimestamp(unix_time, timezone.utc).astimezone()

        return dt_object

def main():
    rclpy.init()
    node = Node("sub_unix_time")
    listener = Listener(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
