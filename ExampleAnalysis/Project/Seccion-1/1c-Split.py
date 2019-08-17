#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/split.htm

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
pathUrl_Result = "D:/RepositorioGitHub/ArcPy-GIS/Project/Seccion-1/Result/Split"

# Execute Split
listValues = {}
listValues['split'] = []

listValues['split'].append({
		'Geometry'		 : 'GPT',
		'inFeatures'	 : 'Pasivos_Ambientales_Mineros.shp',
		'inSplitFeatures': 'Departamentos.shp',
		'splitField'	 : 'NOMBDEP',
		'outFeatures'	 : os.path.join(pathUrl_Result, 'Pasivos')
	})

listValues['split'].append({
		'Geometry'		 : 'GPL',
		'inFeatures'	 : 'Red_Vial_Nacional.shp',
		'inSplitFeatures': 'Departamentos.shp',
		'splitField'	 : 'NOMBDEP',
		'outFeatures'	 : os.path.join(pathUrl_Result, 'Vias')
	})

listValues['split'].append({
		'Geometry'		 : 'GPO',
		'inFeatures'	 : 'Departamentos.shp',
		'inSplitFeatures': 'Departamentos.shp',
		'splitField'	 : 'NOMBDEP',
		'outFeatures'	 : os.path.join(pathUrl_Result, 'Departamentos')
	})

# PASIVOS - Dividira en departamentos aquellos que sólo contenga PASIVOS AMBIENTALES MINEROS.
# VIAS.
# Departamentos.
for item in listValues['split']:
	arcpy.Split_analysis(
		in_features    = item['inFeatures'],
		split_features = item['inSplitFeatures'],
		split_field    = item['splitField'],
		out_workspace  = item['outFeatures']
	)