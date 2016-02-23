#Kyle Kortright
#GIS-Based Modeling
#Lab 5
#3/1/16

#This code is used to created a modified flow accumultaion 
#tool for use in ESRI ArcGIS.

# Import library packages
import arcpy, os, sys, numpy

# Read in flow direction raster
Flow_Dir = arcpy.Raster('Lab5.gdb/Flow_Dir')
lowerLeft = arcpy.Point(Flow_Dir.extent.XMin,aerial.extent.YMin)
cellSize = Flow_Dir.meanCellWidth

# Read in raster BMP points
BMP = arcpy.Raster('Lab5.gdb/BMP_Points')

# Convert rasters to numpy arrays
DEM_nump = arcpy.RasterToNumPyArray(Flow_Dir,nodata_to_value=0)
BMP_nump = arcpy.RasterToNumPyArray(BMP,nodata_to_value=0)

# Set environment 
arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = Flow_Dir
arcpy.env.cellSize = cellSize

# Create variables to hold datasets

# Process (loop through) datasets


# Save outputs
