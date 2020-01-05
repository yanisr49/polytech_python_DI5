from tkinter import *
import time, threading, math as m
import random
from enum import Enum


# framerate = 60
# self.t += 1 / framerate
# time.sleep(1 / framerate)

class Move(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4

class Fourmis(object):

    def __init__(self, color):
        self.x = random.randint(0, 399)
        self.y = random.randint(0, 399)
        self.heading = Move.LEFT
        self.color = color

    def deplacer(self, canvas):
        new_pos = random.randint(0, 2)
        if self.heading == Move.UP:
            if new_pos == 0:
                self.x += 1
                self.heading = Move.RIGHT
            elif new_pos == 1:
                self.y -= 1
                self.heading = Move.UP
            elif new_pos == 2:
                self.x -= 1
                self.heading = Move.LEFT
        elif self.heading == Move.LEFT:
            if new_pos == 0:
                self.y -= 1
                self.heading = Move.UP
            elif new_pos == 1:
                self.x -= 1
                self.heading = Move.LEFT
            elif new_pos == 2:
                self.y += 1
                self.heading = Move.DOWN
        elif self.heading == Move.DOWN:
            if new_pos == 0:
                self.x -= 1
                self.heading = Move.LEFT
            elif new_pos == 1:
                self.y += 1
                self.heading = Move.DOWN
            elif new_pos == 2:
                self.x += 1
                self.heading = Move.RIGHT
        elif self.heading == Move.RIGHT:
            if new_pos == 0:
                self.y += 1
                self.heading = Move.DOWN
            elif new_pos == 1:
                self.x += 1
                self.heading = Move.RIGHT
            elif new_pos == 2:
                self.y -= 1
                self.heading = Move.UP

        canvas.create_rectangle(self.x%400, self.y%400, self.x%400, self.y%400, width=0, fill=self.color)

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()
f = Fourmis("#ff0000")
for i in range(1000000):
    f.deplacer(canvas)
    canvas.update()



