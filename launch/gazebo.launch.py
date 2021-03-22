#!/usr/bin/env python3


import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='True')

    ty_sensors_mount = get_package_share_directory('ty_sensors_mount')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(ty_sensors_mount, 'launch', 'empty_world.launch.py')
            ),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(ty_sensors_mount, 'launch', 'spawn_entity.launch.py')
            ),
        ),

        

    ])
