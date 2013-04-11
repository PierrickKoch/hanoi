#!/usr/bin/env python3
import time
import pymorse

def wander(ranges):
    assert(len(ranges) >= 30)
    mid = len(ranges) // 2
    cmd = {'v': 0, 'w': 0}
    # halt if an object is less than 2m in a 30deg angle
    halt = False
    for distance_to_object in ranges[mid-15:mid+15]:
        if distance_to_object < 2:
            halt = True
            break
    if halt:
        # we go to the highest-range side scanned
        if sum(ranges[:mid]) > sum(ranges[mid:]):
            cmd['w'] = -1
        else:
            cmd['w'] = +1
    else:
        cmd['v'] = 1
    # command to be published
    return cmd

with pymorse.Morse() as sim:
    while sim:
        data = sim.robot.sick.get()
        ranges = data['range_list']
        cmd = wander(data['range_list'])
        sim.robot.motion.publish(cmd)
        time.sleep(.1)

