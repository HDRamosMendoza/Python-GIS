import arcpy

'''
pathGDB = r"C:\prueba\CreateGDB\Prueba.gdb"
arcpy.env.workspace = pathGDB

describeGDB = arcpy.Describe(pathGDB)
if hasattr(describeGDB, "name"):
	print "Name: " + describeGDB.name 

if hasattr(describeGDB, "dataType"):
	print "datatype: " + describeGDB.dataType

if hasattr(describeGDB, "file"):
	print "file: " + describeGDB.file

if hasattr(describeGDB, "catalogPath"):
	print "catalog path: " + describeGDB.catalogPath

print "Children"
#Busca todos los objetos hijos.
for childGDB in describeGDB.children:
	describeFeature = arcpy.Describe(childGDB.name);
	if describeFeature.dataType == 'FeatureDataset':
		print "\-t" + describeFeature.name
		print "\-t" + desc.spatialReference.name
	print '* * * * * *'

	if describeFeature.dataType == 'FeatureClass':
		print "\-t" + describeFeature.name
		print "\-t" + describeFeature.shapeType
	print '* * * * * *'

	if describeFeature.dataType == 'Table':
		print "\-t" + describeFeature.name
	print '* * * * * *'
'''

'''
import os
#rootPath = os.getcwd()
rootPath = r"C:\prueba\CreateGDB"

arcpy.env.workspace	= os.path.join(rootPath, "Prueba.gdb")

featureList = arcpy.ListFeatureClasses()
print "Feature clases in "+ os.path.basename(arcpy.env.workspace)

for name in featureList:
	print name

datasetList = arcpy.ListDatasets(feature_type = 'Feature')

for dataset in datasetList:
	print "Feature Dataset" + dataset
	dataset = arcpy.ListFeatureClasses("", "", dataset)
	for fc in dataset:
		print "\-t" + fc
'''

'''
fieldList = arcpy.ListFields("Schools")
for field in fliedList:
	fieldName = field.name
	fieldType = field.type
	fieldLength = field.length
	print "Name: {}, type "
'''

'''
arcpy.env.workspace = r"C:\Student\PYTH\Running_scripts\Wilson.gdb"
#Variables
restFC = "Wilson_Restaurants"
restLyr = "RestLyr"
crimeFC = "Wilson_Crimes96"
crimeLyr = "AlcoholRelatedCrimes"
histDistFC = "Wilson_HistDist"
histLyr = "HistoricLyr"

#Create feature layer for restaurants
arcpy.MakeFeatureLayer_management(restFC, restLyr)

#Create feature layer for Historical District
arcpy.MakeFeatureLayer_management(histDistFC, histLyr)

#Create feature layer for crimen96
arcpy.MakeFeatureLayer_management(crimeFC, crimeLyr)

# Perform Select By Location to select all restaurants
# within 1000 feet of district
arcpy.SelectLayerByLocation_management(restLyr, "WITHIN_A_DISTANCE",
										histLyr, "1000 feet",
										"NEW_SELECTION")

# Perform Select by Location on crimes that are within 500 feet of the restaurant
arcpy.SelectLayerByLocation_management(crimeLyr, "WITHIN_A_DISTANCE",
										restLyr, "500 feet",
										"NEW_SELECTION")

# Perform final selection on crimes that are alcohol related
arcpy.SelectLayerByAttribute_management(crimeLyr, "SUBSET_SELECTION",
										' "ALCOHOL" > 0')

crimeCount = arcpy.GetCount_management(crimeLyr)
print "Number of school related crime: {}".format(crimeCount)

print "Script completed"
'''

'''
arcpy.env.workspace = r"C:\Student\PYTH\Selections\SanDiego.gdb"
featClass = "MajorAttractions"
featLayer = "OldAttractions"
fldName = "ESTAB"

# Add delimiters to the field name based on the workspace
newFldName = arcpy.AddFieldDelimiters( datasource = arcpy.env.workspace, field = fldName)

# Assemble the SQL expression, where ESTAB > 0 nad ESTAB < 1956
SQLExp = newFldName + "> 0 and " + newFldName + " < 1956"

# Create a feture layer in memory, applying the SQL expression
arcpy.MakeFeatureLayer_management(in_features = featClass,
									out_layer = featLayer,
									where_clause = SQLExp)

# Obtain a count of the numer of features from the feature Layer.
featCount = arcpy.GetCount_management( in_rows = featLayer)

# Report reuslts
print "Feature couint: {0}".format(featCount)
print "Script completed"
'''

fc = r"C:\Student\PYTH\Selections\SanDiego.gdb\MajorAttractions"
fld1, fld2, fld3 = 'NAME', 'ESTAB', 'EMP'

cur = arcpy.da.SearchCursor(fc, [fld1, fld2, fld3], """ "ESTAB" > 1956""")

#for row in cur:
#	print "{0} was established in {1} and employs {2} people".format(row[0], row[1], row[2])

#del cur

with arcpy.da.SearchCursor(fc,[fld1, fld2, fld3],""" "ESTAB" > 1956 """) as cursor:
	for row in cursor:
		print "{0} was established in {1} and employs {2} people".format(row[0], row[1], row[2])


''''
fc = "Bexar.dsb/Roads"
fld1, fld2 = "ROAD_TYPE", "CASINGS"
cursor = arcpy.da.UpdateCursor(fc, (fld1, fld2))
for row in cursor:
	row[1] = row[0] * 5
	cursor.updateRow(row)

del cursor	
'''

'''
fc = "Bexar.dsb/Roads"
fld1, fld2 = "ROAD_TYPE", "CASINGS"

with arcpy.da.UpdateCursor(fc, (fld1, fld2)) as cursor:
	for row in cursor:
		if row[0] == 40:
			cursor.deleteRow() #deletes the current row
		else:
			row[1] = row[0] * 5
			cursor.updateRow(row) 
'''

'''
fc = "Bexar.dsb/Roads"
fld1, fld2 = 'ROAD_TYPE', 'CASINGS' 
cursor = acrpy.da.InsertCursor(fc, (fld1, fld2))
for x in xrange(0,30):
	cursor.insertRow(x,10,50)
del cursor
'''

'''
fc = "Bexar.dsb/Roads"
cursor = arcpy.da.InsertCursor(fc, ('NAME', 'SHAPE@XY'))
cursor.insertRow(('WILSON', (2311534.55, 722088.963)))
del cursor
'''