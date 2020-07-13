import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(111)
#creates evenly spaced array for given initial and final points
u=np.linspace(-1,1,100)
x,y=np.meshgrid(u,u)
z=x**2+y**2
ax.contourf(x,y,z)
plt.show()

