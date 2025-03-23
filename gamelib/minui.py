#!/usr/bin/env python
# coding: utf-8

'''
usage:

form = minui.add_form()
form.topleft.add_button('New Game', on_click=lambda x:x)
form.topleft.br()
form.topleft.add_button('Exit')

...

form.draw()

'''

import pyxel
from . import common

class Minui:
    pass

class Button:
    def __init__(self, text='', on_click=None):
        self.x = 0
        self.y = 0
        self.w = 30
        self.h = 9
        self.bg = 4
        self.fg = 7
        self.hl = 9
        self.topmargin = 2
        self.leftmargin = 2
        self.text = text
        self.on_click = on_click if on_click is not None else lambda x,y: None
        self.enabled = True
        self.hidden = False
        self.hovered = False
        self.pressed = False

    def draw(self):
        hovered = common.pt_in_rect(common.Point(pyxel.mouse_x, pyxel.mouse_y), self)
        self.w = max(self.w, len(self.text)*4 + 4)
        pyxel.rect(self.x,
                   self.y,
                   self.w,
                   self.h,
                   self.hl if hovered else self.bg)
        pyxel.text(self.x+self.leftmargin,
                   self.y+self.topmargin,
                   self.text,
                   self.fg)
    def click(self, x, y):
        self.on_click(x, y)

class FormCursor:
    def __init__(self, parent, pos, dir_):
        self.parent = parent
        self.pos = pos
        self.dir_ = dir_


    def add_space(self, *args, **kwargs):
        self.pos.x += self.dir_.x
        self.pos.y += self.dir_.y

    def add_button(self, *args, **kwargs):
        b = Button(*args, **kwargs)
        b.x = self.pos.x
        b.y = self.pos.y
        self.pos.x += self.dir_.x
        self.pos.y += self.dir_.y
        self.parent.widgets.append(b)
        return b

class Form:
    def __init__(self):
        self.widgets = []
        self.topleft = FormCursor(self, common.Point(0,0), common.Point(0,10))
    def draw(self):
        for w in self.widgets:
            w.draw()
    def click(self, x, y):
        for w in self.widgets:
            if common.pt_in_rect(common.Point(x,y), w):
                w.click(x, y)

