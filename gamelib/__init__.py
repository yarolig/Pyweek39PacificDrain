#!/usr/bin/env python
# coding: utf-8

import pyxel
import pprint
from . import minui

DISPLAY_SCALE=3
FPS=72
KEY_NAMES = {getattr(pyxel, s):s
             for s
             in dir(pyxel)
             if s.startswith('KEY_')
             or s.startswith('GAMEPAD')
             or s.startswith('MOUSE_')}


class App:
    def __init__(self):
        self.form = minui.Form()
        self.about_form = minui.Form()
        self.pallete_form = minui.Form()

        self.form.topleft.pos.x += 30
        self.form.topleft.pos.y += 30
        self.form.topleft.add_button(text="New game")
        self.form.topleft.add_button(text="Options")
        self.form.topleft.add_button(text="Color Pallete", on_click=lambda x,y: self.activate_form(self.pallete_form))
        self.form.topleft.add_button(text="About", on_click=lambda x,y: self.activate_form(self.about_form))
        self.form.topleft.add_button(text="Exit", on_click=self.exit_clicked)

        self.about_form.topleft.pos.x += 30
        self.about_form.topleft.pos.y += 30
        self.about_form.topleft.add_button(text="Pyweek39 entry by yarolig")
        self.about_form.topleft.pos.y += 10
        self.about_form.topleft.add_button(text="Back", on_click=lambda x,y: self.activate_form(self.form))

        self.pallete_form.topleft.pos.x += 30
        self.pallete_form.topleft.pos.y += 10
        for i in range(16):
            b = self.pallete_form.topleft.add_button("color %d" % i)
            b.fg = 7 if i < 6 else 1
            b.bg = i
        self.pallete_form.topleft.add_space()
        self.pallete_form.topleft.add_button(text="Back", on_click=lambda x, y: self.activate_form(self.form))

        self.active_form = self.form
    def activate_form(self, form):
        self.active_form = form
    def update(self):
        if pyxel.frame_count % 100 == 0:
            print(pyxel.frame_count, pyxel.mouse_x, pyxel.mouse_y)
        if pyxel.input_keys:
            print('key down: ' + ','.join([str(KEY_NAMES.get(k, k)) for k in pyxel.input_keys]))
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.active_form.click(pyxel.mouse_x, pyxel.mouse_y)

    def draw(self):
        pyxel.cls(0)
        self.active_form.draw()
    def exit_clicked(self, x, y):
        pyxel.quit()

app=App()

def run():
    pyxel.init(800 // DISPLAY_SCALE,
               600 // DISPLAY_SCALE,
               title="Pyweek39 by yarolig",
               display_scale=DISPLAY_SCALE,
               fps=FPS,
               quit_key=pyxel.KEY_Q)

    pyxel.mouse(True)
    pyxel.perf_monitor(True)

    pyxel.run(app.update, app.draw)