#!/usr/bin/env python
# coding: utf-8

import pyxel
import pprint

DISPLAY_SCALE=3
FPS=72
KEY_NAMES = {getattr(pyxel, s):s for s in dir(pyxel) if s.startswith('KEY_') or s.startswith('GAMEPAD')}

def update():
    if pyxel.frame_count % 100 == 0:
        print(pyxel.frame_count, pyxel.mouse_x, pyxel.mouse_y)
    if pyxel.input_keys:
        print('key down: ' + ','.join([str(KEY_NAMES.get(k, k)) for k in pyxel.input_keys]))

def draw():
    pyxel.cls(0)
    for i in range(16):
        pyxel.rect(55, i*10,
                   75, 9, i)
        pyxel.text(30, i * 10 + 2, "col:" + str(i), 3)
def run():
    pyxel.init(800 // DISPLAY_SCALE,
               600 // DISPLAY_SCALE,
               title="Pyweek39 by yarolig",
               display_scale=DISPLAY_SCALE,
               fps=FPS,
               quit_key=pyxel.KEY_Q)

    pyxel.mouse(True)
    pyxel.perf_monitor(True)
    pyxel.run(update, draw)