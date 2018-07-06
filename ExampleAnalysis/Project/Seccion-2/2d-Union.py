#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/union.htm
# Es de uso exclusivo de tipo poligono. Se podrá realizar en punto o línea.

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
listValues['union'] = []

# Vamos a unir la Cuenta Urubamba con los Departamentos de Perú.
listValues['union'].append({
		'inFeatures'  	: ["Cuenca_Urubamba.shp", os.path.join(inWorkspace,"Departamentos.shp")],
		'outFeatures' 	: os.path.join(pathUrl_Result, "Union/Urubamba_Departamentos.shp"),
		'joinAttributes': "ALL"
	})

for item in listValues['union']:
	arcpy.Union_analysis(
		in_features = item['inFeatures'],
		out_feature_class = item['outFeatures'],
		join_attributes = item['joinAttributes']
	)