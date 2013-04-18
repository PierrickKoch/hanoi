from morse.builder import *

robots = {}

for idx in range(11):
    idx_robot = 'node%i' % idx
    robots[idx_robot] = ATRV('dala%i' % idx)
    kb = Keyboard('keyb')
    robots[idx_robot].append(kb)
    robots[idx_robot].translate(idx, -idx, 0)

env = Environment('outdoors', fastmode=True)
env.show_framerate(True)

env.configure_multinode(
        protocol = "socket",
        server_address = "192.168.102.96",
        server_port = "65000",
        distribution = {idx: robots[idx].name for idx in robots.keys()}
    )

env.create()
