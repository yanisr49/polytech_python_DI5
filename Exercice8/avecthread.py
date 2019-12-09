import random
import sys
from threading import Thread, RLock
from multiprocessing import Process
import time

verrou = RLock()

n = 1E7

#test avec les threads
class calcul_long_class(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global n
        while n > 0:
            with verrou:
                n -= 1


start = time.time()


# Création des threads
thread_1 = calcul_long_class()
thread_2 = calcul_long_class()

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()

end = time.time()
print(end-start)
