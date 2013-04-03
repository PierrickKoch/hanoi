#!/usr/bin/env python

from pymorse import Morse

def is_mouse_visible(semantic_camera_stream):
    data = semantic_camera_stream.get()
    return [visible_object for visible_object in data['visible_objects'] \
            if visible_object['name'] == 'MOUSE']

with Morse() as sim:
    camera = sim.cat.camera
    motion = sim.cat.motion
    while sim:
        if is_mouse_visible(camera):
            v_w = {"v": 2, "w": 0}
        else:
            v_w = {"v": 0, "w": 1}
        motion.publish(v_w)

