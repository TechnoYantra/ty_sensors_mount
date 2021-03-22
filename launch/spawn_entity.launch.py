#!/usr/bin/env python

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    urdf_file_name = 'ty_sensor_mount.urdf'

    urdf = os.path.join(
            get_package_share_directory('ty_sensor_mount'),
            'urdf',
            urdf_file_name)

    # add gazebo_model_path
    os.system("export GAZEBO_MODEL_PATH="+get_package_share_directory('ty_sensor_mount')+"/..")

    print("export GAZEBO_MODEL_PATH="+get_package_share_directory('ty_sensor_mount')+"/..")

    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2','run','gazebo_ros','spawn_entity.py','-entity','ty_sensor_mount','-x','0','-y','0','-z','0','-file',urdf],
            output='screen'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf]),

        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf],
            ),
        ])
