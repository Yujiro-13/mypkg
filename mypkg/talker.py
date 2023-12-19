# SPDX-FileCopyrightText: 2023 Yujiro Shito
# SPDX-License-Identifier: BSD-3-Clause

import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

class Talker():
    def __init__(self): # selfはオブジェクト
        self.pub = node.create_publisher(Int16, "countup", 10) # パブリッシャのオブジェクト作成
        self.n = 0

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
talker = Talker()                #talkerという「オブジェクト」を作成

def cb():          #17行目で定期実行されるコールバック関数
    global n       #関数を抜けてもnがリセットされないようにしている
    msg = Int16()  #メッセージの「オブジェクト」
    msg.data = n   #msgオブジェクトの持つdataにnを結び付け
    talker.pub.publish(msg)        #pubの持つpublishでメッセージ送信
    talker.n += 1
    
node.create_timer(0.5, cb)  #タイマー設定
rclpy.spin(node)            #実行（無限ループ）