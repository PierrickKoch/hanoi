import pymorse

def seen(msg):
    for obj in msg['visible_objects']:
        if obj['name'] == "MOUSE":
            return True
    return False

with pymorse.Morse() as sim:
    while sim:
        seen_right = seen(sim.cat.cameraR.get())
        seen_left  = seen(sim.cat.cameraL.get())
        # if we see the mouse on both camera go straight
        if seen_right and seen_left:
            cmd = {'v': 2, 'w': 0}
        elif seen_right:
            # turn right
            cmd = {'v': 0, 'w': -1}
        elif seen_left:
            # turn left
            cmd = {'v': 0, 'w': +1}
        else:
            # turn faster
            cmd = {'v': 0, 'w': 3}
        # send the command to the motion controller (publish)
        sim.cat.motion.publish(cmd)

