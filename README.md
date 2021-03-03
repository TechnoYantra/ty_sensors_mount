# TechnoYantra Sensor Mount

This package contains the files for ROS integration of Technoyantra Sensors Mount ([ty_sensors_mount](https://github.com/TechnoYantra/ty_sensors_mount)) which is a custom designed & 3D Printed mount which holds various sensors together like

 * RPLiDAR A1 360° Laser Range Scanner - https://www.slamtec.com/en/Lidar/A1
 * Intel® RealSense™ Depth Camera D435 and - https://www.intelrealsense.com/depth-camera-d435/
 * Intel® RealSense™ Tracking Camera T265 - https://www.intelrealsense.com/tracking-camera-t265/

This sensor mount can be placed on your robot to get simultaneous data from all of your sensors.

This package currently supports and is been tested on [ROS Kinetic Kame](http://wiki.ros.org/kinetic/Installation/Ubuntu) & [ROS Melodic Morenia](http://wiki.ros.org/melodic/Installation/Ubuntu) running on Ubuntu 16.04 & Ubuntu 18.04 respectively.

## Dependencies:

### ROS on appropriate Ubuntu Version -

Install [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu), on Ubuntu 16.04 or [ROS Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu) on Ubuntu 18.04 before proceeding. 

### Catkin Workspace -

Create a catkin workspace if not made already, where you can store all your packages. Follow [this tutorial](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) to create your own catkin workspace.

**NOTE:** Please don't make another workspace just for ty_sensors_mount. Keep the package in the same workspace as your robot on which you are going to implement it.

### Git -

Make sure you have Git installed on your PC. If not, then you can install git using

```
sudo apt-get install git
```

### Realsense_ros_gazebo -

The ty_sensor_mount package uses the Realsense Camera descriptions from the [realsense_ros_gazebo](https://github.com/nilseuropa/realsense_ros_gazebo) package made by [Marton Juhasz](https://github.com/nilseuropa). We have forked Marton's repo on to avoid any type of conflict in dependencies. To install the forked package,

Simply change your terminal directory to your src folder of your workspace

```
cd catkin_ws/src
```

where *catkin_ws* should be replaced by the name of your workspace and then clone the forked package by

```
git clone https://github.com/TechnoYantra/realsense_ros_gazebo
```

You can also clone the package by the original creator, but for best support with the ty_sensors_mount package, we recommend cloning the forked repo.

## Installation:

To install the ty_sensors_mount package, stay in the src folder of your Catkin Workspace like before and then run the following command

```
git clone https://github.com/TechnoYantra/ty_sensors_mount
```

Please run catkin_make or catkin_build from your workspace directory before proceeding.

And you are done! You can now use the ty_sensors_mount package!!!

## How to use:

### As a standalone package -

Run the following command to start a simulation with the ty_sensors_mount in the centre of the world and initializing all the Sensors. It will take a little time to load depending upon your PC specification if you are loading it for the first time

```
roslaunch ty_sensors_mount gazebo.launch
```

You can also add few objects in the Simulation from Gazebo Models to test the sensors.

To visualize the data from the sensors, run the following command in another terminal making sure that the simulation is runnning in background.

```
roslaunch ty_sensors_mount display.launch
```

This will start the RViz and load a config file that will help you visualize readings and data from all the sensors.

### On your own Robot -

You can attach this mount to your robot and link the base_link of this mount to the base_link of your robot by publishing the appropriate Static TF.

### ROS 2
Coming Soon...
