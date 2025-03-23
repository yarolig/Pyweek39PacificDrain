#!/usr/bin/env python
# coding: utf-8

class Point:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

def pt_in_rect(pt, rt):
    return (rt.x <= pt.x < rt.x + rt.w and
            rt.y <= pt.y < rt.y + rt.h)
