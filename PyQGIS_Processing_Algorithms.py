# PyQGIS Processing Algorithms

import processing

# Listing all available algorithms

for algo in QgsApplication.processingRegistry().algorithms():
	print(algo.id(), "------", algo.displayName())

# Get help/info regarding a gicen algorithm

processing.algorithmHelp("gdal:cliprasterbymasklayer")