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
    bot.arm.set_ee_pose_components(x=0.5, z=-0.16)
    # Setting coordinates for movements. Arm moving forward to coordinate (x=0.5, z=-0.16). 
    # define T_sd in terms of the components it represents - specifically the x, y, z, roll, pitch, and yaw of the ‘Body’ frame with respect to the ‘Space’ frame.
    # (where x, y, and z are in meters, and roll, pitch and yaw are in radians).
    #bot.arm.set_single_joint_position("waist", np.pi/2.0)
    bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    # When specifying a desired pose using the command above, arm will its end-effector to the desired pose in a curved path.
    # This makes it difficult to perform movements that are ‘orientation-sensitive’ (like carrying a small cup of water without spilling).
    # To get around this, the set_ee_cartesian_trajectory method is provided.
    # This method defines a trajectory using a series of waypoints that the end-effector should follow as it travels from its current pose to the desired pose. 
    bot.arm.set_ee_cartesian_trajectory(x=-0.2, z=-0.05)
    bot.arm.set_ee_cartesian_trajectory(x=0, z=-0.15)
    bot.gripper.open()
    bot.gripper.close()
    bot.gripper.open()
    bot.gripper.close()
    # The gripper open and close represent to the probing action. since couldn't incorprate soil sensor in the simulation.
    bot.arm.go_to_home_pose()
    # Arm wiil return to its predefined Home pose.
    bot.arm.go_to_sleep_pose()
    # Arm will return to its Sleep pose, which is the resrting position.

if __name__=='__main__':
    main()
