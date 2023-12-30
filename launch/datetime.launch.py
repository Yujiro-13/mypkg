# SPDX-FileCopyrightText: 2023 Yujiro Shito
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    pub_unix_time = launch_ros.actions.Node(
        package='mypkg',
        executable='sub_unix_time',
        )
    sub_unix_time = launch_ros.actions.Node(
        package='mypkg',
        executable='pub_unix_time',
        output='screen'
        )

    return launch.LaunchDescription([pub_unix_time, sub_unix_time])
