#!/usr/bin/env python3
import time
import pymorse

def follow(pose):
    wp = {'x':0,'y':0,'z':0,'yaw':0,'tolerance':0}
    wp['x'] = pose['x']
    wp['y'] = pose['y']
    wp['z'] = pose['z'] + 1.5 # height in meters
    # command to be published
    return wp

with pymorse.Morse() as sim:
    while sim:
        pose = sim.mouse.pose.get()
        wp = follow(pose)
        sim.hawk.waypoint.publish(wp)
        time.sleep(.1)
