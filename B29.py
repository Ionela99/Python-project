import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import array

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

x = np.array([])
y = np.array([])

f = open("file.txt", 'r')

content = f.readline()
content = content.replace("\n", "")
content = content.split(' ')
print(content)
for nr in content:
    x = np.append(x, int(nr))

content = f.readline()
content = content.replace("\n", "")
content = content.split(' ')
print(content)
for nr in content:
    y = np.append(y, int(nr))

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
ymax=0
xmijloc=0

def maximY(a):
    #global ymax
    ym = 0
    for i in range(n):
        if y[i] > ym:
            ym = y[i]
    return ym

ymax = maximY(y)
#print(ymax)

x.sort()
print("x sortat: ", x)


def power(x):
    global xmijloc
    j = 0
    for i in range(n):
        x2[j] = x[i]**2
        j += 1
    l =int (n / 2)
    xmijloc = x[l]
    print("x^2 este egal cu:", x2)
    print(l)
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

def slope(a, be, c, d):
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

def ecuatia(x):
    global b
    global m
    return m * x + b

reprezentare = list(map(ecuatia, x))

print("punctele de pe dreapta sunt: ", reprezentare)

plt.scatter(x, y)  #punctele in sistem
plt.plot(x, reprezentare)
plt.title('Metoda celor mai mici patrate', fontdict=font)
str = f'y={round(m, 2)}*x+{round(b, 2)}'
plt.text(xmijloc, ymax-1, f'{str}', fontdict=font)
plt.xlabel('Axa x', fontdict=font)
plt.ylabel('Axa y', fontdict=font)
plt.subplots_adjust(left=0.15)
plt.show()


