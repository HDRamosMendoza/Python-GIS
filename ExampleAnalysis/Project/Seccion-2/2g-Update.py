#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/update.htm

# Autor 	: Ing. Daniel Ramos Mendoza
# Web		: HDRamosMendoza.github.io/Perfil-Profesional
# Email		: heber.daniel.ramos.mendoza@gmail.com
# Móvil		: 051 999130638
# Originario: Perú - Lima
# NOTA: No es el mejor código que eh realizado. Es una simple demo de mis inicios de un par de años atras.
import arcpy
import os

arcpy.env.overwriteOutput = True
arcpy.env.workspace = "D:/RepositorioGitHub/ArcPy-GIS/Mixed/Tema_02/Capas"
inWorkspace = "D:/RepositorioGitHub/ArcPy-GIS/Mixed/Tema_01/Capas"
pathUrl_Result = "D:/RepositorioGitHub/ArcPy-GIS/Project/Seccion-2/Result"

listValues = {}
listValues['update'] = []

# Vamos a actualizar los limites de los departamentos 
# tomando en consideración el limite de la Cuenca Urubmaba.
# Se actualiza el poligono y se tendra que actualizar manualmente el nombre con el nuevo limite.
listValues['update'].append({
		'inFeatures'	: os.path.join(inWorkspace,"Departamentos.shp"),
		'updateFeatures': "Cuenca_Urubamba.shp",
		'outFeatures'	: os.path.join(pathUrl_Result, "Update/Departamentos_Update.shp"),
		'keepBorders'	: True
	})

for item in listValues['update']:
	arcpy.Update_analysis(
		in_features 		= item['inFeatures'],
		update_features 	= item['updateFeatures'],
		out_feature_class 	= item['outFeatures'],
		keep_borders 		= item['keepBorders']
	)