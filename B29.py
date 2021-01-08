#import matplotlib.pyplot as plt
#from scipy import stats
import numpy as np

x = np.array([2, 3, 5, 7, 9])
y = np.array([4, 5, 7, 10, 15])
n = len(x)
x2 = np.array([])
x2 = [0 for i in range(n)]
xy = np.array([])
xy = [0 for i in range(n)]

def power(x):
    j = 0

    for i in range(n):
        x2[j] = x[i]**2
        j += 1
    print("x^2 este egal cu:")
    print(x2)

power(x)

def prod(x, y):
    j = 0

    for i in range(n):
        xy[j] = x[i] * y[i]
        j += 1
    print("x*y este egal cu:")
    print(xy)

prod(x, y)

def suma(x, y, x2, xy):
    sumax = 0
    sumay = 0
    sumax2 = 0
    sumaxy = 0
    for i in x:
        sumax += i
    for i in y:
        sumay += i
    for i in x2:
        sumax2 += i
    for i in xy:
        sumaxy += i
    print(sumax)
    print(sumay)
    print(sumax2)
    print(sumaxy)

suma(x, y, x2, xy)

#plt.scatter(x, y)
#plt.show()

