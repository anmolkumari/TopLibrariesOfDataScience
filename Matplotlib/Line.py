
#matplotlib is a visualization library in python , with a lot of pre def functions
#matplotlib->pyplot

import matplotlib.pyplot as plt


# basic functions:
X=[10,12,30,17,6]
plt.plot(X)
plt.xlabel("Birthdays")
plt.legend("IBD")
plt.axis([0,20,0,31])
plt.show()


#modifyng plots
XX=[1,2,3,4,5]
Y=[7,8,9,10,11]
x=10;

plt.plot(XX,'ro')

plt.show()

#modifyng plots
XX=[1,2,3,4,5]
plt.plot(XX,'gv')
plt.show()

#to draw a line/arrow

x=10
y=15
plt.arrow(x,y,10,10)
plt.plot(x,y,'ro')

import numpy as np

# evenly sampled time at 200ms intervals
ts = np.arange(0., 5., 0.2)

 # red dashes, blue squares and green triangles
plt.plot(ts, ts, 'r--', ts, ts**2, 'bs', ts, ts**3, 'g^')
plt.show()