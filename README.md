# InterbotiX X-Series Arm ROS Packages

[![View Documentation](https://trossenrobotics.com/docs/docs_button.svg)](https://www.trossenrobotics.com/docs/interbotix_xsarms/index.html)

![xsarm_banner](images/xsarm_banner.png)

## Overview

Welcome to the *interbotix_ros_xsarms* sub-repo! This sub-repository contains ROS packages meant to be used with the many [X-Series robotic arms](https://www.trossenrobotics.com/robotic-arms/ros-research-arms.aspx)  sold by Trossen Robotics. Packages were tested on Ubuntu Linux 18.04 and 20.04 using ROS Melodic and Noetic respectively. Additionally, all ROS nodes were written using Python or C++. However, any programming language capable of sending ROS messages can be used to control the robots. To that effect, the core packages inside this repo are as follows:
- **interbotix_xsarm_moveit** - contains the config files necessary to launch an arm using MoveIt either in Gazebo, on the physical robot, or just in RViz
- **interbotix_xsarm_gazebo** - contains the config files necessary to launch an arm in Gazebo, including tuned PID gains for ros_control
- **interbotix_xsarm_control** - contains the motor configuration files and the 'root' launch file that is responsible for launching the robot arm
- **interbotix_xsarm_ros_control** - contains the config files necessary to setup ROS controllers between MoveIt and the physical robot arm
- **interbotix_xsarm_descriptions** - contains the meshes and URDFs (including accurate inertial models for the links) for all arm platforms

Finally, there is also an **examples** directory containing various demos of how the above mentioned core packages can be used. So what are you waiting for? Let's get started!

## IRROS Structure
Refer [here](https://github.com/Interbotix/interbotix_ros_core#code-structure) to get a general understanding of IRROS.
![xsarm_irros_structure](images/xsarm_irros_structure.png)

##### Hardware Layer
All X-Series arms are made up of [X-Series Dynamixel servos](https://www.trossenrobotics.com/dynamixel-x-series-robot-servos). Each servo has two 3-pin JST ports that allows it to be daisy chained with other servos using 3-pin cables. The 'root' Dynamixel (i.e. the 'waist' motor) then connects to the [XM/XL motor power hub](https://www.trossenrobotics.com/3-pin-x-series-power-hub.aspx). Besides for providing 12V to the motors from the barrel jack, the hub also connects to the 3-pin JST port on the [U2D2](https://www.trossenrobotics.com/dynamixel-u2d2.aspx). This device acts as a communication interface between a computer (connected via microUSB cable) and the motors - converting USB/TTL signals back and forth.

On the right side of this layer, there are two sensors. While the base robot kit from Interbotix does not come with either a RealSense camera or joystick controller, there are some demos (ROS packages in the Application layer) that may use them.

##### Driver Layer
The ROS packages in this sub-repo build up from the *interbotix_xs_sdk* ROS wrapper found in the *interbotix_ros_core* repository. Reference the package there for implementation details. The *realsense_ros* and *joy* packages are ROS wrappers around the RealSense camera and PS3/PS4 controller devices respectively.

##### Control Layer
The *interbotix_xsarm_control* ROS package found in this layer holds the config files for every one of our X-Series arms. These config files define the names of the joints that make up each arm as well as initial values for the motor registers. The launch file inside the package then passes the appropriate parameters to the *interbotix_xs_sdk* driver node depending on the type of arm being used.

##### Application Support Layer
The three main items shown in this layer can be found in the *interbotix_ros_toolboxes* repository [here](https://github.com/Interbotix/interbotix_ros_toolboxes/tree/main/interbotix_xs_toolbox). Specifically, the Arm IK Solver module can be found within the *interbotix_xs_modules* ROS package in a file called 'arm.py' and 'InterbotixArmXSInterface.'. These modules essentially provides a small API to allow users to control an arm's end-effector in Python or MATLAB - no ROS experience necessary. Additionally, the *interbotix_xs_ros_control* and *interbotix_moveit_interface* packages make it possible for the *interbotix_xsarm_ros_control* and *interbotix_xsarm_moveit_interface* packages respectively to function properly.

##### Research Layer
All the ROS packages, Python scripts, and MATLAB scripts found within the [examples](examples/) directory fall in this category.

## Documentation

Find all documentation related to the X-Series arms including specifications, hardware setup, ROS packages, troubleshooting, and more at the [Trossen Robotics X-Series Arms Documentation site](https://www.trossenrobotics.com/docs/interbotix_xsarms/index.html).

Look for the [![View Documentation](https://trossenrobotics.com/docs/docs_button.svg)](https://www.trossenrobotics.com/docs/interbotix_xsarms/index.html) button on package and example READMEs for their structure and usage information.

## Contributing
To contribute your own custom X-Series arm in this repo, you will need to do the following steps:
- Create a motor config file similar to the YAML files found [here](interbotix_xsarm_control/config/) (excluding the 'modes.yaml' file). To get familiar with the parameter names, checkout the [Motor Config Template](https://github.com/Interbotix/interbotix_ros_core/blob/main/interbotix_ros_xseries/interbotix_xs_sdk/config/motor_configs_template.yaml). Note that the name of this file is what defines your *robot_model* name, and should be used when naming other files like the URDF.
- Create a URDF similar in structure to the ones found [here](interbotix_xsarm_descriptions/urdf/). Don't forget to put all necessary meshes in the [meshes](interbotix_xsarm_descriptions/meshes/) directory! As an FYI, you should follow the naming convention for the links, joints, and frame poses as found in the other arm files for consistency.
- Create a set of Gazebo/ROS position controllers similar to the ones found [here](interbotix_xsarm_gazebo/config/position_controllers/).
- Create a set of Gazebo/ROS trajectory controllers similar to the ones found [here](interbotix_xsarm_gazebo/config/trajectory_controllers/).
- Create an SRDF file for Moveit similar to the ones found [here](interbotix_xsarm_moveit/config/srdf/). You should first use the MoveIt Setup Assistant Wizard for this step and then edit the generated SRDF file based on the structure of those files.
- Add the appropriate Screw axes and M matrices to the [mr_descriptions.py](https://github.com/Interbotix/interbotix_ros_toolboxes/blob/main/interbotix_xs_toolbox/interbotix_xs_modules/src/interbotix_xs_modules/mr_descriptions.py) and [mr_descriptions.m](https://github.com/Interbotix/interbotix_ros_toolboxes/blob/main/interbotix_xs_toolbox/interbotix_xs_modules/src/interbotix_xs_modules/mr_descriptions.m) modules. For help doing this, refer to Chapter 4 in [Modern Robotics](http://hades.mech.northwestern.edu/images/7/7f/MR.pdf) and [this video](https://www.youtube.com/watch?v=cKHsil0V6Qk&ab_channel=NorthwesternRobotics), or check out our [kinematics_from_description](https://github.com/Interbotix/kinematics_from_description) tool.
- Make sure to follow the same naming convention, structure, and documentation procedures as found in the repo before making a PR.

## Contributors
- [Solomon Wiznitzer](https://github.com/swiz23) - **ROS Engineer**
- [Luke Schmitt](https://github.com/lsinterbotix) - **Robotics Software Engineer**
- [Levi Todes](https://github.com/LeTo37) - **CAD Engineer**


## UPDATE BY ELDHOSE VATTAPPARAMBIL GEEVARGHESE (eldhose.geevarghese2021@my.ntu.ac.uk, eldhosevg07@gmail.com)
# Simulating and Controlling a Robotic Manipulator for Mobile IoT Sensing for Sustainable Precision Farming Using Robots
The idea is to develop a simulated environment to test the control of a robotic manipulator with the purpose of operating the soil nutrient measuring probe. To get the arm working in this project, ROS packages for Noetic on Ubuntu Linux 20.04 is used.  Gazebo enables realistic and efficient simulation of robot populations in complex indoor and outdoor contexts. The ViperX 250 robotic arm from Interbotix is utilised in this project. The arm uses the same core open-source code repository, making it simple to move concepts from one platform to another. Docker, an open platform for developing, shipping, and executing applications. In the ROS framework, created a workspace to control the Robotic Arm and its End-effector. The Gazebo Simulation Configuration was used to control the robotic arm directly, as well as in conjunction with MoveIt via the Follow Joint Trajectory interface and alone via the Joint Position Controller interface.
# Arm Descriptions
The URDFs and meshes for the Arm is included in this description package. The URDF is a file format used in ROS to define the geometry and structure of robots. The STL files for robot are kept in the folder under the meshes directory. The Interbotix black.png image is in the meshes directory and this image influences the appearance and texture of the robot. The robot's URDFs are then located in the urdf directory. They are written in xacro format so that users may configure which elements of the URDF are loaded to the parameter server.

![summit_xl_gazebo](https://user-images.githubusercontent.com/109370103/189695616-6cfae43f-7bff-413c-99b4-55e6868270cb.png)

Placed the arm over the robot but having trouble finding the correct mesh files for the SUMMIT-XL robot. So, there were concerns with arm balancing and inertial factors.

![Arm_over_Summit_xl](https://user-images.githubusercontent.com/109370103/187939480-9299b440-173f-410f-aba3-164e415fbefa.png)

Therefore, a box with the same dimensions (Width, Height and Depth) is employed as the base of the arm in replacement of the robot. The use_world_frame argument is set to false to attach the arm's base link frame to a different frame, which is true by default. Then a box, same dimension as robot is attached to the base_link_frame which is the root link of the arm.

![Picture1](https://user-images.githubusercontent.com/109370103/189698433-384d99ae-4c68-44c2-9fee-02a729021d7a.jpg)

To make the model simulate properly, different physical properties of the robot must be defined, i.e., the properties that a physics engine like Gazebo would require. 
Every simulated link element requires an inertial tag. The inertia element specifies the 3x3 rotating inertia matrix. Since it is symmetrical, it can be represented by only six components. The inertia tensor is determined by the object's mass and mass distribution. Assuming equal distribution of mass in the volume of the item and computing the inertia tensor based on the object's form is a fair initial estimate.

![Picture2](https://user-images.githubusercontent.com/109370103/189699435-e9466854-db9a-43a3-9a6b-48f279b2578f.jpg)

![image](https://user-images.githubusercontent.com/109370103/189699645-0fc1ef97-09fd-4d17-823a-d7c1451fa28c.png)


When employing Realtime controllers, inertia components of zero (or nearly zero) might cause the robot model to collapse unexpectedly, and all links will appear with their origins coinciding with the world origin. Therefore, the box's and arm's physical properties are updated. 

# ARM CONTROL:
A well-defined controlling approach is required for a system to perform properly. The system has accurate robotic arm motions and allows the user to instruct the robotic arm in specified end-effector orientations. The installation package includes the setup and launch files required to start the arm platform. This includes launching the xs_sdk node, which is in charge of operating the DYNAMIXEL motors on the robot, as well as loading the URDF into the robot description parameter. Essentially, this package is what all 'downstream' ROS packages should refer to get the robot up and running. 
xsarm_control package builds on top of the xsarm_descriptions and xs_sdk packages. The parameters in there define the desired operating modes for either a group of joints or single joints, and whether they should be torqued on/off at node startup.

![ViperX-250 RViz](https://user-images.githubusercontent.com/109370103/189700267-615fefe8-2982-47cc-90c9-3b5eac9f503f.png)

It includes YAML files that have PID gains optimised for the arm and gripper joints so that ros_control can successfully control the arms. There are two uses for this. It may be used either alone or in combination with MoveIt using the JointPositionController interface or the FollowJointTrajectory interface.

The MoveIt Setup Assistant wizard was used to create a MoveIt package for each robot. ROS controllers effectively receive Joint Trajectory orders from MoveIt (through the FollowJointTrajectoryAction interface) and then publish joint commands to the xs_sdk node at the appropriate time. Currently, just the 'position' data in the Joint Trajectory messages are used since they give the smoothest motion. While this package is only designed to be used with MoveIt, it may potentially be used with any other node that can interact properly with the joint trajectory controller package.

![2](https://user-images.githubusercontent.com/109370103/189700442-3487a505-3c47-4e28-8273-857e801a73c2.png)

# PYTHON-ROS INTERFACE:
To direct an arm to perform desired end-effector poses or to follow Cartesian trajectories. Using Python-Ros interface implemented a system that controls arm from pre-specified actions and parameters.

- **robot_manipulation** - a ROS node that runs in the background and receives Python API commands and publishes data to various ROS topics as needed. It is not a classic ROS node in the sense that it can’t be launched from a ROS launch file or run from the terminal using a rosrun command. Instead, the Python API module includes a Class that, when created, brings the node to life. At the completion of a program, the object gets destroyed, killing the node.

![Picture3](https://user-images.githubusercontent.com/109370103/189701707-ed1386ee-c1d8-4824-b0bc-cf992ee125dd.jpg)

![Picture4](https://user-images.githubusercontent.com/109370103/189701738-02013092-4607-4cc5-be1e-58c750b7cda2.jpg)

![Picture5](https://user-images.githubusercontent.com/109370103/189701800-2c328153-42bc-4be8-adb6-241d8d9fc9b5.jpg)
