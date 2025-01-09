import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Crear una figura y un eje con proyección ortográfica centrada en Colombia
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.Orthographic(central_longitude=-78, central_latitude=5)})

# Añadir características del mapa
ax.coastlines(resolution='110m', linewidth=0.5)
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.LAND, facecolor='orange')
ax.add_feature(cfeature.LAKES, facecolor='aqua')
ax.add_feature(cfeature.STATES, linewidth=0.5)

# Límites de la proyección
ax.set_global()

# Dibujar los meridianos y paralelos
ax.gridlines(draw_labels=True, linewidth=0.5)

# Función para la visualización
n = 100
d = 2 * np.pi / (n - 1)
lats, lons = np.indices((n, n)) * d

wave = np.exp(-lats / 10) * np.cos(lons)
mean = np.cos(2. * lats) * np.sin(2. * lats)

# Convertir las coordenadas a longitud y latitud en grados
lons_deg = lons * 180. / np.pi
lats_deg = lats * 180. / np.pi

# Mostrar la función sobre el mapa
contour = ax.contour(lons_deg, lats_deg, mean + wave, 15, transform=ccrs.PlateCarree(), linewidths=1.5)

# Título
plt.title("Gráfica sobre un mapa global")

# Mostrar la gráfica
plt.show()
