#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: http://pro.arcgis.com/es/pro-app/tool-reference/analysis/buffer.htm

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
listValues['buffer'] = []

# Generaremos radio de influencia.
listValues['buffer'].append({
		'inFeatures'	: "Pasivos_Puno.shp",
		'outFeatures'	: os.path.join(pathUrl_Result,"Buffer/Buffer_01.shp"),
		'bufferDistanceField' : "10 Kilometers",
		'lineSide' : "FULL",
		'lineEndType' : "ROUND",
		'dissolveOption': "NONE"
	})

# Se cambia el parametro para que el BUFFER sea compacto.
listValues['buffer'].append({
		'inFeatures'	: "Pasivos_Puno.shp",
		'outFeatures'	: os.path.join(pathUrl_Result,"Buffer/Buffer_02.shp"),
		'bufferDistanceField' : "10 Kilometers",
		'lineSide' : "FULL",
		'lineEndType' : "ROUND",
		'dissolveOption': "ALL"
	})

# Realizamos un radio de influencia por el campo "Influencia" de pasivos puno.
listValues['buffer'].append({
		'inFeatures'	: "Pasivos_Puno.shp",
		'outFeatures'	: os.path.join(pathUrl_Result,"Buffer/Buffer_03.shp"),
		'bufferDistanceField' : "Influencia",
		'lineSide' : "FULL",
		'lineEndType' : "ROUND",
		'dissolveOption': "ALL"
	})

for item in listValues['buffer']:
	arcpy.Buffer_analysis(
		in_features = item['inFeatures'],
		out_feature_class = item['outFeatures'],
		buffer_distance_or_field = item['bufferDistanceField'],
		line_side = item['lineSide'],
		line_end_type = item['lineEndType'],
		dissolve_option = item['dissolveOption']
   	)