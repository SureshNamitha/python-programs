import matplotlib.pyplot as plt
from numpy import genfromtxt
import csv
x=[]
y=[]
with open('/home/bl109/Desktop/NamithaBL1/l.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
plt.plot(x,y)
#plt.xlable('x axis')
#plt.ylable('y axis')

plt.show()



