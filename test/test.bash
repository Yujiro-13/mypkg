#!/bin/bash
# SPDX-FileCopyrightText: 2023 Yujiro Shito
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg datetime.launch.py > /tmp/mypkg.log &

# Sleep for a short time to allow nodes to start
sleep 2

# Get PID of the ROS2 launch process
launch_pid=$!

# Run tests
result=0

# Check if publisher is publishing
if ros2 topic list | grep -q '/unix_time'; then
    echo "Publisher is publishing"
else
    echo "Publisher is not publishing"
    result=1
fi

# Check if subscriber is receiving messages
if cat /tmp/mypkg.log | grep -q 'Date time'; then
    echo "Subscriber is receiving messages"
else
    echo "Subscriber is not receiving messages"
    result=1
fi

# Stop the ROS2 launch process
kill $launch_pid

# Return result
exit $result
