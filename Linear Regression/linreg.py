import csv

xset = yset = []

fh = open("dataset.csv", newline="")
reader = csv.reader(fh)
for i in reader:
    xset.append(i[0])
    yset.append(i[1])
fh.close()

def error(m, c):
    pass