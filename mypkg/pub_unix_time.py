# SPDX-FileCopyrightText: 2023 Yujiro Shito
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64  # Int64型を使用
import time

class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(Int64, "unix_time", 10)
        node.create_timer(1.0, self.cb)  # タイマーを1秒に変更

    def cb(self):
        msg = Int64()
        msg.data = int(time.time())  # 現在のUnix時間を取得
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Node("pub_unix_time")
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
