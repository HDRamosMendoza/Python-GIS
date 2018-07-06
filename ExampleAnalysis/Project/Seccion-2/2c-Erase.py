#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/erase.htm
# Nos permitira eliminar informacion que se intersecta.

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
pathUrl_Result = "D:/RepositorioGitHub/ArcPy-GIS/Project/Seccion-2/Result"

listValues = {}
listValues['erase'] = []

# Vamos a determinar los rios que se encuentran totalmente 
# contenidos dentro el limite del departamento. Haremos uso de analisis anterior (Rios_Cruce_Departamento)
listValues['erase'].append({
		'inFeatures'  	: "Rios_Quebradas.shp",
		'eraseFeatures'	: os.path.join(pathUrl_Result, "SpatialJoin/Rios_Cruce_Departamento.shp"),
		'outFeatures' 	: os.path.join(pathUrl_Result, "Erase/Rios_Completo.shp")
	})

# Se realizara un inventario forestal.
listValues['erase'].append({
		'inFeatures'  	: "Forestal.shp",
		'eraseFeatures'	: "Departamnentos_No.shp",
		'outFeatures' 	: os.path.join(pathUrl_Result, "Erase/Forestal_Proyecto.shp")
	})

# Se necesita los restos arqueologicos que no se 
# encuentren cerca a un rio en un radio de 100 metros.
listValues['erase'].append({
		'inFeatures'  	: "Restos_Arqueologicos.shp",
		'eraseFeatures'	: os.path.join(pathUrl_Result, "SpatialJoin/Arqueologia_100m.shp"),
		'outFeatures' 	: os.path.join(pathUrl_Result, "Erase/Restos_Mayores_100.shp")
	})

for item in listValues['erase']:
	arcpy.Erase_analysis(
		in_features 		= item['inFeatures'],
		erase_features 		= item['eraseFeatures'],
		out_feature_class 	= item['outFeatures']
	)