import random
import sys
from threading import Thread, RLock
import time
import timeit
from multiprocessing import Pool, Process, set_start_method, Queue


def f(x):
    while x > 0:
        x = x-1
    return x

if __name__ == '__main__':
    print("Execution sans multiprocessing : ")
    start = timeit.default_timer()
    print(f(1E7))
    stop = timeit.default_timer()
    print('Time : ', stop - start)


    nb_worker = 5
    with Pool(nb_worker) as p:
        print("Execution avec multiprocessing : ")
        start = timeit.default_timer()
        n = 1E7 / nb_worker
        print(p.map(f, [n,n,n,n,n]))
        stop = timeit.default_timer()
        print('Time : ', stop - start)
