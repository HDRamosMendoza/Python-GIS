#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/symmetrical-difference.htm
# Nos permite unir informacion dependiendo de la forma y la extensión de la capa de entrada.

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
listValues['symmetricalDifference'] = []

# - Realizaara una union con el departamento Ucayali con 
#   la Cuenca Urubamba pero que no considere su intersección.
# - Este tipo es de suma importancia cuando
#   vayamos a realizar analisis de zonas de influencia 
listValues['symmetricalDifference'].append({
		'inFeatures'	: 'Ucayali.shp',
		'updateFeatures': 'Cuenca_Urubamba.shp',
		'outFeatures'	: os.path.join(pathUrl_Result, "SymmetricalDifference/Ucayali_Urubamba.shp"),
		'joinAttributes': "ALL"
	})

for item in listValues['symmetricalDifference']:
	arcpy.SymDiff_analysis(
		in_features 		= item['inFeatures'],
		update_features 	= item['updateFeatures'],
		out_feature_class 	= item['outFeatures'],
		join_attributes 	= item['joinAttributes']
	)