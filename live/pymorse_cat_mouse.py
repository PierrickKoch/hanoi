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
        if seen_right:
            cmd = {'v': 1, 'w': 0}
        # TODO smart stuff here ! :-)
        else:
            cmd = {'v': 0, 'w': 1}
        sim.cat.motion.publish(cmd)

