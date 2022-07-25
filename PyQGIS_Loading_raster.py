# Loading raster into QGIS 
## Paste this code into QGIS Python console
DEM_Raster_1 = QgsRasterLayer("/Users/samuelrussell/Documents/GitHub/PyQGIS_Scripting/Tanzania_COP30.tif")

# Check if the raster was loaded correctly
DEM_Raster_1.isValid()

# Visualise Raster
QgsProject.instance().addMapLayer(DEM_Raster_1)

# Inspecting raster values
## Raster width:

print(DEM_Raster_1.height(), ':', DEM_Raster_1.width())

## Raster extent

print(DEM_Raster_1.extent())

## Bounding box coordinates

ext = DEM_Raster_1.extent()
print(ext.xMinimum(), ext.yMinimum(), ':', ext.xMaximum(), ext.yMaximum())
