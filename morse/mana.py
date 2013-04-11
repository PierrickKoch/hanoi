from morse.builder import *

class Mana(SegwayRMP400):
    def __init__(self):
        # call parent constructor
        SegwayRMP400.__init__(self)
        # init Mana's sensors and actuator
        self.init_components()
    def init_components(self):
        self.velodyne = Velodyne()
        self.velodyne.translate(z=0.80)
        self.append(self.velodyne)

        self.ptu = PTU()
        self.ptu.translate(x=0.30, z=0.40)
        self.append(self.ptu)
        # TODO PTU -> cam{r,l}

        self.cameraL = VideoCamera()
        self.cameraL.translate(x=0.35, y=-0.15, z=0.45)
        self.append(self.cameraL)

        self.cameraR = VideoCamera()
        self.cameraR.translate(x=0.35, y=+0.15, z=0.45)
        self.append(self.cameraR)

        self.odometry = Odometry()
        self.odometry.translate(z=0.25)
        self.append(self.odometry)

        self.gps = GPS()
        self.gps.translate(y=-0.30, z=0.60)
        self.append(self.gps)

        # eye sugar: the top structure
        struc = Cube("manastruct1")
        struc.scale = (.1, .1, .1)
        struc.translate(x=0.20, y=0.20, z=0.20)
        #self.append(struc)

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
    env.create() # finalize scene initialization

