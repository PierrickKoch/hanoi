from morse.builder import *

hawk = Quadrotor()
hawk.translate(z = 1.0)

# add a rotorcraft controller
waypoint = RotorcraftWaypoint()
hawk.append(waypoint)

mouse = ATRV()
keyboard = Keyboard()
mouse.append(keyboard)

pose = Pose()
mouse.append(pose)

pose.add_stream('socket')
waypoint.add_stream('socket')

env = Environment('outdoors', fastmode=True)
# show profile (debug properties)
env.show_framerate()

