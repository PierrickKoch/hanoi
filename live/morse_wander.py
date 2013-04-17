from morse.builder import *

# add an ATRV robot to the simulation
robot = ATRV()
motion = MotionVW()
robot.append(motion)

# add LIDAR
sick = Sick()
robot.append(sick)
sick.translate(z=0.9)

sick.add_stream('socket')
motion.add_stream('socket')

env = Environment('lab2.blend', fastmode=True)

