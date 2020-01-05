from tkinter import *
import time, math as m
import random
from enum import Enum
from threading import Thread, RLock
import cv2
import numpy as np


# framerate = 60
# self.t += 1 / framerate
# time.sleep(1 / framerate)

class Move(Enum):
    UP = 1
    LEFT = 2
    DOWN = 3
    RIGHT = 4

verrou = RLock()

class Fourmis(Thread):

    def __init__(self, r, g, b, img):
        Thread.__init__(self)
        self.x = random.randint(0, 399)
        self.y = random.randint(0, 399)
        self.heading = Move.LEFT
        self.r = r
        self.g = g
        self.b = b
        self.img = img

    def deplacer(self):
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

        self.img[self.x%400, self.y%400] = [self.r, self.g, self.b]

    def run(self):
        for i in range(10000000):
            self.deplacer()

if __name__ == '__main__':
    img = np.zeros((400, 400, 3), np.uint8)
    img.fill(255)

    Fourmis(255,0,0, img).start()
    Fourmis(0,255,0, img).start()
    Fourmis(0,0,255, img).start()
    for _ in range(10000000):
        cv2.imshow("board", img)
        cv2.waitKey(1)

    """cv2.imshow("board", img)
    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()"""


