import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

#x =  np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
#y =  np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

#x = np.array([2, 3, 5, 7, 9])
#y = np.array([4, 5, 7, 10, 15])

x = np.array([1.21, 3.00, 5.16, 8.31, 10.21])
y = np.array([1.69, 5.89, 4.11, 5.49, 8.65])

n = len(x)
x2 = np.array([])
x2 = [0 for i in range(n)]
xy = np.array([])
xy = [0 for i in range(n)]
m=0    #slope
b=0    #intercept
sumax = 0
sumay = 0
sumax2 = 0
sumaxy = 0

def f(a):
    for i in range(n):
        format(a[i], '.3f')

def power(x):
    j = 0
    for i in range(n):
        x2[j] = x[i]**2
        j += 1
    f(x2)
    print("x^2 este egal cu:", x2)
    #print(x2)

power(x)

def prod(x, y):
    j = 0

    for i in range(n):
        xy[j] = x[i] * y[i]
        j += 1
    print("x*y este egal cu:", xy)
    #print(xy)

prod(x, y)

def suma(x, y, x2, xy):
    global sumax
    global sumay
    global sumax2
    global sumaxy
    for i in x:
        sumax += i
    for i in y:
        sumay += i
    for i in x2:
        sumax2 += i
    for i in xy:
        sumaxy += i
    print("Σx =", sumax)
    print("Σy =", sumay)
    print("Σx^2 =", sumax2)
    print("Σxy =", sumaxy)
    print("\n")

#suma(x, y, x2, xy)

def slope(a, b, c, d):
    suma(x, y, x2, xy)
    global sumax
    global sumay
    global sumax2
    global sumaxy
    global m
    m = n * sumaxy - sumax * sumay
    m = m / (n * sumax2 - sumax**2)
    print("m = ", m)

#slope(sumax, sumay, sumax2, sumaxy)

def Intercept(a, be, c, d):
    global sumax
    global sumay
    global n
    global b
    slope(sumax, sumay, sumax2, sumaxy)

    b = (sumay - m * sumax) / n
    print("b = ", b)

Intercept(sumax, sumay, m, n)

def myfunc(x):
    global b
    global m
    return m * x + b

mymodel = list(map(myfunc, x))

print(mymodel)

plt.scatter(x, y)  #punctele in sistem
plt.plot(x, mymodel)
plt.show()

