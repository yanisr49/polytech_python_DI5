import matplotlib.pyplot as plt
import random

# List of 100 random numbers between 0 and 100
import numpy as np

nombres_aleatoires = [random.randint(0,100) for _ in range(100)]

# display the curve of this numbers
def f(t):
    return 100 * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 100.0, 0.5)
t2 = np.arange(0.0, 100.0, 0.1)

plt.figure()
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(222)
plt.plot(nombres_aleatoires, 'bo', nombres_aleatoires, 'k')
plt.xlabel("abscisse")
plt.ylabel("ordonné")
plt.annotate("jolie", xy=(38, 17), xytext=(100, -110), arrowprops={'facecolor':'red', 'shrink':0.05})
plt.subplot(223)
plt.hist(nombres_aleatoires, 25, density=2, facecolor='g', alpha=0.75)

plt.subplot(224)
name = ['-18', '18-25', '25-50', '50+']
data = [5000, 26000, 21400, 12000]

explode=(0.1,0.1,0.1,0.1)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=0, shadow=False)
plt.axis('equal')

plt.show()