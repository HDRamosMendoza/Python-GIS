#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/table-select.htm
# No estrae informacion tabular.

# Autor 	: Ing. Daniel Ramos Mendoza
# Web		: HDRamosMendoza.github.io/Perfil-Profesional
# Email		: heber.daniel.ramos.mendoza@gmail.com
# Móvil		: 051 999130638
# Originario: Perú - Lima
# NOTA: No es el mejor código que eh realizado. Es una simple demo de mis inicios de un par de años atras.
import arcpy
import os

arcpy.env.overwriteOutput = True
arcpy.env.workspace  = "D:/RepositorioGitHub/ArcPy-GIS/Mixed/Tema_01/Capas"

xy_tolerance = ""
pathUrl_Result = "D:/RepositorioGitHub/ArcPy-GIS/Project/Seccion-1/Result"

# Execute Table Select
listValues = {}
listValues['tableSelect'] = []

listValues['tableSelect'].append({
		'Geometry'	  : 'GPT',
		'inFeatures'  : 'Pasivos_Ambientales_Mineros.shp',
		'whereClause' :	'CLASE = \'INACTIVO\'',
		'outFeatures' : os.path.join(pathUrl_Result, 'Pasivos_Ambientales_Inactivos')
	})

listValues['tableSelect'].append({
		'Geometry'	  : 'GPL',
		'inFeatures'  : 'Red_Vial_Nacional.shp',
		'whereClause' :	'ESTADO = \'Buena\'',
		'outFeatures' : os.path.join(pathUrl_Result, 'Red_Vial_Estado_Bueno')
	})

listValues['tableSelect'].append({
		'Geometry'	  : 'GPO',
		'inFeatures'  : 'Forestal.shp',
		'whereClause' :	'CATEGOR = \'Bosque de produccion\'',
		'outFeatures' : os.path.join(pathUrl_Result, 'Bosque_Produccion')
	})

# Execute TableSelect
for item in listValues['tableSelect']:
	arcpy.TableSelect_analysis(
		in_table 	 = item['inFeatures'],
		out_table 	 = item['outFeatures'],
		where_clause = item['whereClause']
	)