from enum import Enum
from threading import Thread, RLock

import random
import numpy as np
import cv2


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
        for i in range(10000):
            with verrou:
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

                cv2.rectangle(img, (self.x%400, self.y%400), (self.x%400, self.y%400), self.color, 1)
                cv2.imshow("board", img)
                cv2.waitKey(1)


global img
verrou = RLock()
img = np.zeros((400, 400, 3), np.uint8)
img.fill(255)
f = Fourmis((255, 0, 0))
f1 = Fourmis((0, 255, 0))

# Lancement des threads
f.start()
f1.start()

# Attend que les threads se terminent
f.join()
f1.join()

k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
