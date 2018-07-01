#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/identity.htm
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
inWorkspace = "D:/RepositorioGitHub/ArcPy-GIS/Mixed/Tema_01/Capas"
pathUrl_Result = "D:/RepositorioGitHub/ArcPy-GIS/Project/Seccion-2/Result"

listValues = {}
listValues['identity'] = []

# Realiza un interseccion y una union con la Cuenca Urubamba.
listValues['identity'].append({
		'inFeatures': 'Cuenca_Urubamba.shp',
		'identityFeatures': os.path.join(inWorkspace, "Departamentos.shp"),
		'outFeature': os.path.join(pathUrl_Result, "Identity/Cuenca_Urubamba_Identity_01.shp"),
		'joinAttributes': "ALL"
	})

# Invertimos el orden de las capas y me a tomado como limite los departamentos.
listValues['identity'].append({
		'inFeatures': os.path.join(inWorkspace, "Departamentos.shp"),
		'identityFeatures': 'Cuenca_Urubamba.shp',
		'outFeature': os.path.join(pathUrl_Result, "Identity/Cuenca_Urubamba_Identity_02.shp"),
		'joinAttributes': "ALL"
	})

for item in listValues['identity']:
	arcpy.Identity_analysis(
		in_features = item['inFeatures'],
		identity_features = item['identityFeatures'],
		out_feature_class = item['outFeature'],
		join_attributes = item['joinAttributes']
	)