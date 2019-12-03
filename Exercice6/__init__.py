import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import ndimage
from scipy import misc
from PIL import Image
from scipy import ndimage

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
        a1 = np.array([[3, 1], [1, 2]])  # résout ce systeme 3 * x0 + x1 = 9 et x0 + 2 * x1 = 8:
        a2 = np.array([9, 8])
        res_sys = np.linalg.solve(a1, a2)
        print(res_sys)
        print(np.linalg.eig(np.linspace(0, 8, 9).reshape(3, 3)))  # le premier array renvoie représente les valeurs propres et le deuxième représente les vecteurs propres associés a ces valeurs propres

    def question4(self):
        x = np.random.uniform(0., 100., 100)
        y = 3. * x + 2. + np.random.normal(0., 10., 100)
        e = np.repeat(10., 100)
        popt, pcov = curve_fit(self.line, x, y, sigma=e)

        plt.plot(x, y, '.')
        plt.errorbar(x, y, yerr=e, fmt="none")
        xfine = np.linspace(0., 100., 100)  # define values to plot the function for
        plt.plot(xfine, self.line(xfine, popt[0], popt[1]), 'r-')
        plt.show()

    def line(self, x, a, b):
        return a * x + b

    def question5(self):
        imgpil = Image.open("999decide.jpg")
        # anciennement np.asarray

        imgpil = imgpil.resize((int(imgpil.size[0]/2), int(imgpil.size[1] / 2)), Image.ANTIALIAS)

        img = np.array(imgpil)  # Transformation de l'image en tableau numpy
        plt.imshow(img)
        plt.show()

NumpyE().question2()