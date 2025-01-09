import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


# Definición de la proyección Mercator
wms_server = "https://ows.terrestris.de/osm/service?"
proj = ccrs.Mercator()

# Creación de la figura
fig = plt.figure(figsize=(12, 10), dpi=800)

# Primer subplot (izquierda)
ax = fig.add_subplot(121, projection=proj)
ax.set_extent([-85, -65, -5, 15])  # Establecer el límite geográfico del área de visualización

# Añadir capa de topografía
ax.add_wms(wms_server, layers=["SRTM30-Colored-Hillshade"])



# Añadir leyenda
ax.legend()

# Segundo subplot (derecha)
ax2 = fig.add_subplot(122, projection=proj)
ax2.set_extent([-76, -70, 9, 12])  # Establecer el límite geográfico del área de visualización

# Añadir capa de topografía en la segunda área
ax2.add_wms(wms_server, layers=["SRTM30-Colored-Hillshade"])



# Mostrar el gráfico
plt.show()
