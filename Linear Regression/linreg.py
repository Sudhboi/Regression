import csv
import matplotlib.pyplot as plt
import numpy as np

xset = []
yset = []

fh = open("Linear Regression\dataset.csv", newline="")
reader = csv.reader(fh)
for i in reader:
    xset.append(float(i[0]))
    yset.append(float(i[1]))
fh.close()

n = len(xset)
p = 0.000000001
tries = 10000

def meanError(m, c):
    error = 0
    for i in range(0, n):
        error += (m*xset[i] + c - yset[i]) ** 2
    merror = error/n
    return merror

def pderm(m, c):
    temp = 0
    for i in range(n):
        temp += (m*xset[i] + c - yset[i]) * xset[i]
    return (2/n) * temp

def pderc(m, c):
    temp = 0
    for i in range(n):
        temp += (m*xset[i] + c - yset[i])
    return (2/n) * temp

m = c = 1

for i in range(tries):
    print("Mean Error:", meanError(m, c))
    m -= p * pderm(m, c)
    c -= p * pderc(m, c)
    print(m, c)

x = np.linspace(min(xset), max(xset) + 10, 101)
y = m*x + c
plt.plot(xset, yset, 'o')
plt.plot(x, y)
plt.show()