#Modulo WorkGDB.py
#!/usr/bin/env python
import arcpy
import os
import sys
import WorkGDB
mainWork = WorkGDB.GeoDatabase(os.getcwd())

# Set the workspace
workspace = "D:\PruebaGDB\MD-DRME-IS-0402-2017.v.1.0.gdb"

# Set the workspace environment
arcpy.env.workspace = "D:\PruebaGDB\MD-DRME-IS-0402-2017.v.1.0.gdb"

# Get all the stand alone tables and feature classes
dataList = arcpy.ListTables() + arcpy.ListFeatureClasses()
print dataList
print "------------------------------"

# For feature datasets get all of the featureclasses
# from the list and add them to the master list
for dataset in arcpy.ListDatasets("", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    aa = arcpy.env.workspace
    print aa

    dataList += arcpy.ListFeatureClasses()
    print dataList

print "*******************************"
print dataList

sys.exit()

# Execute enable editor tracking
for dataset in dataList:
    print('Enabling tracking on ' + dataset)
    arcpy.EnableEditorTracking_management(dataset, 
    	"REGISTRADO",
        "F_REGISTRO", 
        "CAMBIADO", 
        "F_CAMBIO",
        "ADD_FIELDS", 
        "UTC")

print('Enabling complete')