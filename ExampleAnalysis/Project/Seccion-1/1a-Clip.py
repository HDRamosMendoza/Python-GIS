#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/clip.htm

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

# Capa de cortante - Constantes
clip_Features_PO = "Ancash.shp"
xy_tolerance = ""
pathUrl_Result = "D:/RepositorioGitHub/ArcPy-GIS/Project/Seccion-1/Result/"

'''
# Version - 1
# Pasivos_Ambientales_Mineros_Ancash
in_features_1 = "Pasivos_Ambientales_Mineros.shp"
outFC_1 = "D:/RepositorioGitHub/ArcPy-GIS/Project/1-Seccion/Pasivos_Ambientales_Mineros_Ancash.shp"
# Execute Clip
arcpy.Clip_analysis(in_features_1, clip_features, outFC_1, xy_tolerance)

# Red_Hidrica_Ancash
in_features_2 = "Red_Hidrica.shp"
outFC_2 = "D:/RepositorioGitHub/ArcPy-GIS/Project/1-Seccion/Red_Hidrica_Ancash.shp"
# Execute Clip
arcpy.Clip_analysis(in_features_2, clip_features, outFC_2, xy_tolerance)

# Red_Hidrica_Ancash
in_features_3 = "Forestal.shp"
outFC_3 = "D:/RepositorioGitHub/ArcPy-GIS/Project/1-Seccion/Forestal_Peru_Ancash.shp"
# Execute Clip
arcpy.Clip_analysis(in_features_3, clip_features, outFC_3, xy_tolerance)
'''

# Version - 2

listValues = {}
listValues['clip'] = []

listValues['clip'].append({
		'geometry': 'GPT',
		'inFeatures': 'Pasivos_Ambientales_Mineros.shp',
		'outFeatures': os.path.join(pathUrl_Result, 'Pasivos_Ambientales_Mineros_Ancash')
	})

listValues['clip'].append({
		'geometry': 'PL', 
		'inFeatures': 'Red_Hidrica.shp',
		'outFeatures': os.path.join(pathUrl_Result, 'Red_Hidrica_Ancash')
	})

listValues['clip'].append({
		'geometry': 'PO',
		'inFeatures': 'Forestal.shp',
		'outFeatures': os.path.join(pathUrl_Result, 'Forestal_Peru_Ancash')
	})

print "Count: " + str(len(listValues['clip']))
for item in listValues['clip']:
	arcpy.Clip_analysis(item['inFeatures'], clip_Features_PO, item['outFeatures'], xy_tolerance)
	print ("Creado: ", item['inFeatures'], item['outFeatures'])