import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal


x = y = np.arange(-5.0,5.0,0.1)

X , Y = np.meshgrid(x,y)

#Z1 = plt.mlab.bivariate_normal(X,Y,1.0,2.0,-2.0,-2.0)
#Z2 = plt.mlab.bivariate_normal(X,Y,2.0,1.0,1.0,1.0)
#Z=(Z1-Z2)

rv1 = multivariate_normal([-2.0,-2.0],[[1.0,0.0],[1.0,2.0]])
Z1 = rv1.pdf(np.dstack((X,Y)))

rv2 = multivariate_normal([1.0,1.0],[[2.0,0.0],[0.0,1.0]])
Z2= rv2.pdf(np.dstack((X,Y)))

Z=(Z1-Z2)

CS =plt.contourf(X,Y,Z,cmap="coolwarm"); plt.colorbar(CS,label="Densidad")


levels=np.arange(-0.095,0.095,0.02)
CS = plt.contourf(X,Y,Z,levels,cmap="coolwarm")
CS4 = plt.contour(X,Y,Z,levels,colors='k')
plt.clabel(CS4,colors='k',fontsize=16)
plt.savefig('bivariate2.png')
plt.show()