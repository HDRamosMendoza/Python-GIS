#Modulo WorkGDB.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import arcpy
from arcpy import env
import json
import WorkGDB

# Instanciando classe principal.
mainWork = WorkGDB.GeoDatabase(os.getcwd())

# Sistema Referencial.
WKID = 4326 # WGS-1984.
out_SR = arcpy.SpatialReference()
out_SR.factoryCode = WKID
out_SR.create()
env.outputCoordinateSystem = out_SR

# Carpeta de trabajo.
out_Folder_Path = mainWork.pathWork()

# Asignacion de carpeta de trabajo.
arcpy.env.workspace = out_Folder_Path

# Nombre de Geodatabase.
out_GDB = mainWork.geoDatabase()

# Creando la GDB.
arcpy.CreateFileGDB_management(out_Folder_Path, out_GDB)
print 'Geodatabase creado'

# Nombre de Feature DataSet
out_FD = mainWork.geoDataset()

# Nombre de Feature Class
out_FC = mainWork.geoFeatureClass()

# Creando el Feature DataSet. 
arcpy.CreateFeatureDataset_management(out_Folder_Path + "\\" + out_GDB, out_FD, out_SR)
print 'Feature Dataset creado'

output_TablaJson = open('Json\\table.json').read()
table = json.loads(output_TablaJson)

# Asigando nuestro espacio de trabajo.
arcpy.env.workspace = out_Folder_Path+"\\"+out_GDB

# Creando el FEATURE CLASS.
output_FCJson = open("Json\\GPT_IS_InfoSuelo.json").read()
convert_FCJson = arcpy.AsShape(output_FCJson, True)
arcpy.CopyFeatures_management(convert_FCJson, os.path.join(out_GDB,out_FC))
#arcpy.JSONToFeatures_conversion("Json\\GPT_IS_InfoSuelo.json", os.path.join(out_GDB,"GPT_IS_InfoSuelo"))
print 'Feature Class creado'

# Creando TABLE.
for tableItem in table:
	arcpy.CreateTable_management(out_Folder_Path + "\\" + out_GDB, tableItem)
	# Agregando campos a TABLE.
	for ItemValue in table[tableItem][0]["TB_ItemCodedValues"]:
		arcpy.AddField_management( tableItem, 
			ItemValue['ItemName'], 
			ItemValue['ItemType'], 
			field_alias  = ItemValue['ItemAlias'],
			field_length = ItemValue['ItemSize'])
	
	# Se crea el nombre de las relaciones
	relClass = "RL_IS" + tableItem[5:9] + "InfSuelo" + tableItem[8:]		
	print "Table " + tableItem + " creado"

	# Agregando las relaciones		
	arcpy.CreateRelationshipClass_management(
		out_FC, tableItem, relClass,
	    table[tableItem][0]["TB_Type"],
	    table[tableItem][0]["TB_ForLabel"],
	    table[tableItem][0]["TB_BackLabel"],
	    table[tableItem][0]["TB_Notification"],
	    table[tableItem][0]["TB_Cardinality"],
	    table[tableItem][0]["TB_Attributed"],
	    table[tableItem][0]["TB_PrimaryKey"],
	    table[tableItem][0]["TB_ForeignKey"])			
	print "Relationship GPT_IS_InfoSuelo - " + tableItem + " creado"

# Activar EDITOR TRACKING.
dataList = arcpy.ListTables() + arcpy.ListFeatureClasses()
for dataset in dataList:
    arcpy.EnableEditorTracking_management(dataset, 
    	"REGISTRADO","F_REGISTRO", 
        "CAMBIADO", "F_CAMBIO",
        "ADD_FIELDS", "UTC")
    print "Habilitado rastreo de EDITOR " + dataset

# Creacion del SUBTYPE en un parametro
inFeatures = "TB_IS_04_Multimedia"
arcpy.SetSubtypeField_management(inFeatures, "ST_MULTIMEDIA")

# Agregando ITEM al SUBTYPE
stypeDict = {"1": "The Sketch of Deep Sample", "2": "Photo Code", "3": "Industrial and Agricultural", "4": "GPS Coordinate Data File"} 
for code in stypeDict:
	arcpy.AddSubtype_management(inFeatures, code, stypeDict[code])   


# Agregando GLOBALID a TABLE.
for tableItem in table:
	arcpy.AddGlobalIDs_management(tableItem)
	print "GlobalID adicionados " + tableItem

# Habilitando el ATTACHMENTS de la GDB
arcpy.EnableAttachments_management(out_FC)

print 'Finalizado'