#!/bin/bash
# SPDX-FileCopyrightText: 2023 Yujiro Shito
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg datetime.launch.py > /tmp/mypkg.log &

# 少し待機
sleep 2

ret=0

# publisherがトピックを発行しているか確認
if ros2 topic list | grep -q '/unix_time'; then
    echo "OK"
else
    echo "NG"
    ret=1
fi

# subscriberがトピックを受信しているか確認
if cat /tmp/mypkg.log | grep -q 'Date time'; then
    echo "OK"
else
    echo "OK"
    ret=1
fi

[ "$ret" = 0 ] && echo OK
exit $ret
