from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np

# ELDHOSE VATTAPPARAMBIL GEEVARGHESE (N0954952)
# NOTTINGHAM TRENT UNIVERSITY.
# "Simulating and Controlling a Robotic Manipulator for Mobile IoT Sensing for Sustainable Precision Farming Using Robots".

# Using Python-Ros interface implemented a system that controls arm from pre-specified actions and parameters.
# This script makes First and foremost, the Target postures and assigns commands based on that.
# The robotic arm moves forward, stoop down, touch the ground, probe, and then return to it its sleep pose.

# To get started, open a terminal and type 'roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=vx250'
# Then change to this directory and type 'python bartender.py'

def main():
    bot = InterbotixManipulatorXS("vx250", "arm", "gripper")
    # The ViperX 250 robotic arm from is used in this project.
    bot.arm.go_to_home_pose()
    # Arm wiil return to its predefined Home pose.
    bot.arm.go_to_sleep_pose()
    # Arm will return to its Sleep pose, which is the resrting position.

if __name__=='__main__':
    main()
