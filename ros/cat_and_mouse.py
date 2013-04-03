#!/usr/bin/env python
# TODO import json
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

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
        motion.linear.x = 1
    else:
        motion.angular.z = 1
    # send the command to the 'cat' robot
    cmd.publish(motion)

