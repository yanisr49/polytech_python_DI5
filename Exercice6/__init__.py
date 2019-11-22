import numpy as np

class NumpyE(object):

    def __init__(self):
        print("Exercice sur numpy :)")

    def question1(self):
        a = np.random.rand(4,3,2)
        print(a.ndim)
        print(a.shape)
        print(a.size)
        print(a.dtype)
        print(a.itemsize)
        print(a.data)

    def question2(self):
        m1 = np.linspace(0, 8, 9).reshape(3, 3)
        m2 = np.linspace(2, 10, 9).reshape(3, 3)
        print(m1*m2) # Terme à terme
        print(m1.dot(m2)) # multiplication de matrice
        print(m1.dot(m2).T) # multiplication de matrice

    def question3(self):
        m1 = np.random.rand(3,3)
        print(np.linalg.det(m1)) # calcul le déterminant
        print(np.linalg.inv(m1)) # calcul la matrice inverse

NumpyE().question3()