import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(r'/home/lapdog/GIS/NaturalEarth/ne_10m_land/ne_10m_land.shp')
cities = pd.read_csv(r'/home/lapdog/Documents/Python/SIMR/ref_files/OpenBible.Info/places_edited.csv')
countries = gpd.read_file(r'/home/lapdog/GIS/NaturalEarth/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp')
#wgs84 = gpd.read_file(r'P:\GIS\NaturalEarthData\10m_physical\ne_10m_wgs84_bounding_box.shp')
oceans = gpd.read_file(r'/home/lapdog/GIS/NaturalEarth/ne_10m_ocean/ne_10m_ocean.shp')

#plot world to map
base = world.plot(color='tan', edgecolor='black')

#convert csv city points to geometry
geometry = [Point(xy) for xy in zip(cities['Lon'], cities['Lat'])]
crs = {'init': 'epsg:4326'}#set crs to wgs84
gdf = gpd.GeoDataFrame(cities, crs=crs, geometry=geometry)

#plot cities to map
pl = gdf.plot(ax=base, marker='o', color='r', markersize=5)

#label cities (very slow)
#for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf.ESV):
#    pl.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")

#add wgs84 bounding box
#wgs84.plot(ax=base, facecolor='none', edgecolor = 'cyan')

#add countries' borders
countries.plot(ax=base, facecolor='none', edgecolor = 'black')

#plot oceans
oceans.plot(ax=base, color='lightblue')

#set layers to same crs as cities (coordinate reference system as cities)
world = world.to_crs(gdf.crs)
#wgs84 = wgs84.to_crs(gdf.crs)
countries = countries.to_crs(gdf.crs)
oceans = oceans.to_crs(gdf.crs)

plt.show()