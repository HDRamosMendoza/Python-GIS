#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/multiple-ring-buffer.htm

# Autor 	: Ing. Daniel Ramos Mendoza
# Web		: HDRamosMendoza.github.io/Perfil-Profesional
# Email		: heber.daniel.ramos.mendoza@gmail.com
# Móvil		: 051 999130638
# Originario: Perú - Lima
# NOTA: No es el mejor código que eh realizado. Es una simple demo de mis inicios de un par de años atras.
import arcpy
import os

arcpy.env.overwriteOutput = True
arcpy.env.workspace = "D:/RepositorioGitHub/ArcPy-GIS/Mixed/Tema_03/Capas"
pathUrl_Result = "D:/RepositorioGitHub/ArcPy-GIS/Project/Seccion-3/Result"

listValues = {}
listValues['multipleRingBuffer'] = []

# Podemos realizar multiples radios de proximidad.
listValues['multipleRingBuffer'].append({
		'inFeatures' 	: "Pasivos_Puno.shp",
		'outFeatures'	: os.path.join(pathUrl_Result, "Buffer/Buffer_04.shp"),
		'distances'	 	: [5, 10, 20, 30],
		'bufferUnit' 	: "Kilometers",
		'fieldName'	 	: "Influencia",
		'dissolveOption': "ALL",
		'outsidePolygonsOnly': "FULL"
	})

for item in listValues['multipleRingBuffer']:
	arcpy.MultipleRingBuffer_analysis(
		Input_Features 		  = item['inFeatures'],
		Output_Feature_class  = item['outFeatures'],
		Distances 			  = item['distances'],
		Buffer_Unit 		  = item['bufferUnit'],
		Field_Name 			  = item['fieldName'],
		Dissolve_Option 	  = item['dissolveOption'],
		Outside_Polygons_Only = item['outsidePolygonsOnly']
	)
