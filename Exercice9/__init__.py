from tkinter import *
import time, math as m
import random
from enum import Enum
from threading import Thread, RLock
import cv2



# framerate = 60
# self.t += 1 / framerate
# time.sleep(1 / framerate)

class Move(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4


class Fourmis(Thread):

    def __init__(self, color):
        Thread.__init__(self)
        self.x = random.randint(0, 399)
        self.y = random.randint(0, 399)
        self.heading = Move.LEFT
        self.color = color

    def run(self):
        for i in range(1000000):
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

            canvas.update()

verrou = RLock()
root = Tk()
global canvas
canvas = Canvas(root, width=400, height=400)
canvas.pack()
f = Fourmis("#ff0000")
#f2 = Fourmis("#000500")


# Lancement des threads
f.start()
#f2.start()

# Attend que les threads se terminent
f.join()
#f2.join()

