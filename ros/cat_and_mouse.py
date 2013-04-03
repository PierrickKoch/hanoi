#!/usr/bin/env python
# TODO import json
import math
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped

# initialize a ROS node for this script
rospy.init_node("cat_and_mouse")
# initialize a ROS publisher to command the 'cat' robot
cmd = rospy.Publisher("/cat/motion", Twist)

while not rospy.is_shutdown():
    # block untill a new semantic camera message is published
    msg = rospy.wait_for_message("/cat/camera", String)
    # TODO json.loads(msg.data)
    motion = Twist()
    # if 'MOUSE' was in the list of seen objects
    if 'MOUSE' in msg.data:
        #pose_cat   = rospy.wait_for_message("/cat/pose", PoseStamped)
        #pose_mouse = rospy.wait_for_message("/mouse/pose", PoseStamped)
        #dx = pose_mouse.pose.position.x - pose_cat.pose.position.x
        #dy = pose_mouse.pose.position.y - pose_cat.pose.position.y
        #motion.angular.z = math.atan2(dy, dx) / 10
        motion.linear.x = 1
    else:
        motion.angular.z = 1
    # send the command to the 'cat' robot
    cmd.publish(motion)

