from morse.builder import *

class Mana(SegwayRMP400):
    def __init__(self):
        # call parent constructor
        SegwayRMP400.__init__(self)
        # init Mana's sensors and actuator
        self.init_components()
    def init_components(self):
        self.velodyne = Velodyne()
        self.append(self.velodyne)
        self.velodyne.translate(z=0.80)

        self.cameraL = VideoCamera()
        self.append(self.cameraL)
        self.cameraL.translate(x=-0.15, y=0.35, z=0.45)

        self.cameraR = VideoCamera()
        self.append(self.cameraR)
        self.cameraR.translate(x=+0.15, y=0.35, z=0.45)

        self.odometry = Odometry()
        self.append(self.odometry)
        self.odometry.translate(z=0.25)

        self.gps = GPS()
        self.append(self.gps)
        self.gps.translate(y=-0.30, z=0.60)

    def add_motion(self):
        self.motion = MotionVWDiff()
        self.append(self.motion)
        self.motion.translate(z=0.10)

    def add_keyboard(self):
        self.kb = Keyboard()
        self.kb.properties(Type="Differential")
        self.append(self.kb)


# test with: morse run mana.py
if __name__ == "__main__":
    mana = Mana()
    mana.add_keyboard()
    env = Environment("outdoors")
    del env # finalize scene initialization

