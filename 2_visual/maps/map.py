#decays exponentially toward the poles, oscillated like a wave with the longitude


import mpl_toolkits.basemap as bm
import matplotlib.pyplot as plt
import numpy as np

#Encima de Colombia

myMap=bm.Basemap(projection='ortho',lat_0=5,lon_0=-78,resolution='l')

#Costas, paises y continentes

myMap.drawcoastlines(linewidth=0.25)
myMap.drawcountries(linewidth=0.25)
myMap.fillcontinents(color='orange',lake_color='aqua')
myMap.drawstates(linewidth=0.2)
#Limites, meridianos y paralelos
myMap.drawmapboundary(fill_color='aqua')
myMap.drawmeridians(np.arange(0,360,30))
myMap.drawparallels(np.arange(-90,90,30))

#Funcion

n = 100 ; d = 2*np.pi/(n-1)
[lats,lons]=d*np.indices((n,n))
wave = np.exp(-lats/10)*np.cos(lons)
mean= np.cos(2.*lats)*np.sin(2.*lats)
x ,y = myMap(lons*180./np.pi , lats*180/np.pi)
cs =myMap.contour(x,y,mean+wave,15,linewidths=1.5)

plt.title("Grafica sobre un mapa global")
plt.show()


'''
La biblioteca de  basemap esta descontinuada y se recomienda usar GeoPandas o CartoPy

'''