from morse.builder import *

# add an ATRV robot to the simulation
mouse = ATRV()
# add a Keyboard controller to the scene
actuator = Keyboard()
actuator.properties(Speed=3.0)

# link the controller to the robot
mouse.append(actuator)
mouse.properties(
        Object = True,
        Graspable = False,
        Label = "MOUSE"
    )

cat = ATRV()
# move the cat behind the mouse
cat.translate(x = -2)

# add semantic camera (left)
cameraL = SemanticCamera()
cameraL.translate(x=0.2, y=0.3, z=0.9)
cat.append(cameraL)

# add semantic camera (right)
cameraR = SemanticCamera()
cameraR.translate(x=0.2, y=-0.3, z=0.9)
cat.append(cameraR)

motion = MotionVW()
cat.append(motion)

motion.add_stream('socket')
cameraL.add_stream('socket')
cameraR.add_stream('socket')

env = Environment('outdoors')




'''

HOWTO INSTALL

check you have 'cmake' and 'gcc' installed, install them.
get http://pierriko.com/hanoi/setup.sh
make a directory ~/devel (or anywhere you have write access)
export no_proxy="localhost,127.0.0.1"
run "sh setup.sh" in a Terminal from this directory


'''
