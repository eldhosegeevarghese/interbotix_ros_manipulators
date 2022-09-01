from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np

# TESTING FILE
# A file developed for testing purpose.
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
    bot.arm.set_ee_pose_components(x=0.5, z=-0.16)
    bot.arm.set_ee_cartesian_trajectory(pitch=1.5) 
    #bot.arm.set_single_joint_position("waist", np.pi/2.0)
    #bot.gripper.open()
    #bot.arm.set_ee_cartesian_trajectory(x=0, z=-0.005)
    #bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    #bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.2)
    #bot.gripper.close()
    #bot.arm.set_ee_cartesian_trajectory(x=-0.2, z=-0.05)
    #bot.arm.set_ee_cartesian_trajectory(x=0, z=-0.15)
    #bot.gripper.open()
    #bot.gripper.close()
    #bot.gripper.open()
    #bot.gripper.close()
    #bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    #bot.arm.set_single_joint_position("waist", -np.pi/2.0)
    #bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    #bot.arm.set_ee_cartesian_trajectory(pitch=-1.5)
    #bot.arm.set_single_joint_position("waist", np.pi/2.0)
    #bot.arm.set_ee_cartesian_trajectory(x=0.1, z=-0.16)
    #bot.gripper.open()
    #bot.arm.set_ee_cartesian_trajectory(x=-0.1, z=0.16)
    bot.arm.set_ee_cartesian_trajectory(x=-0.2, z=-0.05)
    bot.arm.set_ee_cartesian_trajectory(x=0, z=-0.15)
    bot.gripper.open()
    bot.gripper.close()
    bot.gripper.open()
    bot.gripper.close()
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()

if __name__=='__main__':
    main()


