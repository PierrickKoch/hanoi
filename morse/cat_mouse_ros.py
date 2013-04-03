from morse.builder import *

#
# "cat" robot
#
cat = ATRV()
cat.translate(x=-6.0, z=0.2)

motion = MotionVW()
cat.append(motion)

camera = SemanticCamera()
camera.translate(x=0.3, z=0.76)
cat.append(camera)

motion.add_stream('ros')
camera.add_stream('ros')

#
# "mouse" robot
#
mouse = ATRV()
mouse.properties(Object = True, Graspable = False, Label = "MOUSE")
mouse.translate(x=1.0, z=0.2)

keyboard = Keyboard()
keyboard.properties(Speed=3.0)
mouse.append(keyboard)

#
# Environment
#
env = Environment('outdoors')
env.place_camera([10.0, -10.0, 10.0])
env.aim_camera([1.0470, 0, 0.7854])
env.select_display_camera(camera)
