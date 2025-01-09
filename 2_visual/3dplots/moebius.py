import numpy as np
import matplotlib.pyplot as plt
from matplotlib import tri

n = 50 ; l=5

u = np.arange(n)*2*np.pi/(n-1)
u = u*np.ones((l,1))
u = u.reshape(n*l)

v = np.arange(l)/(l-1)-0.5
v = v*np.ones((n,1))
v = v.transpose().reshape(n*l)

#Cinta de mobius 
x = (1+0.5*v*np.cos(u/2.0))*np.cos(u)
y = (1+0.5*v*np.cos(u/2.0))*np.sin(u)
z = 0.5*v*np.sin(u/2.0)

#Superficie triangular
surface = tri.Triangulation(u,v)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_trisurf(x,y,z,triangles=surface.triangles)
ax.set_xlim(-1,1);ax.set_ylim(-1,1);ax.set_zlim(-1,1)
plt.show()