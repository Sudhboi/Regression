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

xset = np.array(xset)
yset = np.array(yset)
n = len(xset)
p = 0.000000001
tries = 10000

def meanError(m, c):
    pred = m*xset + c
    error = (pred - yset) ** 2
    return np.mean(error)

def pderm(m, c):
    return  2 * np.mean((m * xset + c - yset) * xset)

def pderc(m, c):
    return  2 * np.mean(m * xset + c - yset)

m = c = 1

for i in range(tries):
    m -= p * pderm(m, c)
    c -= p * pderc(m, c)

x = np.linspace(min(xset), max(xset), 101)
y = m*x + c
plt.plot(xset, yset, 'o')
plt.plot(x, y)
plt.show()