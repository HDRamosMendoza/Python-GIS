#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: 
# - http://desktop.arcgis.com/es/arcmap/10.5/tools/analysis-toolbox/polygon-neighbors.htm
# - https://pro.arcgis.com/es/pro-app/tool-reference/analysis/polygon-neighbors.htm

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
listValues['polygonNeighbors'] = []
# Por lo general cuando estamos en proyectos tomamos en cuenta siempre los limites.
# Clic derecho en Departamentos > Joins and relates > Relate > 1 NOMBDPTO - 2 .dbf - 3 src_NOMBDP - 4 Limita:
# Abriamos la tabla de tributos de departamentos y buscamos la relación.
# Desde manera se podra realizar analisis de limites politicos.
listValues['polygonNeighbors'].append({
	'inFeatures'  : "Departamentos.shp",
	'outFeatures' : os.path.join(pathUrl_Result, "PolygonNeighbors/Neighbors.dbf"),
	'inFields'	  : ["NOMBDPTO"],
	'areaOverlap' : False,
	'bothSides'	  : True,
	'outLinearUnits': "KILOMETERS",
	'outAreaUnits'	: "SQUARE_MILES"
})

for item in listValues['polygonNeighbors']:
	arcpy.PolygonNeighbors_analysis(
		in_features  = item['inFeatures'],
		out_table 	 = item['outFeatures'],
		in_fields 	 = item['inFields'],
		area_overlap = item['areaOverlap'],
		both_sides 	 = item['bothSides'],
		out_linear_units= item['outLinearUnits'],
		out_area_units 	= item['outAreaUnits']
	)