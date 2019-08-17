#!/usr/bin/env python
# -*- coding: utf-8 -*-
# source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/frequency.htm

# Autor 	: Ing. Daniel Ramos Mendoza
# Web		: HDRamosMendoza.github.io/Perfil-Profesional
# Email		: heber.daniel.ramos.mendoza@gmail.com
# Móvil		: 051 999130638
# Originario: Perú - Lima
# NOTA: No es el mejor código que eh realizado. Es una simple demo de mis inicios de un par de años atras.
import arcpy
import os

arcpy.env.overwriteOutput = True
arcpy.env.workspace = "D:/RepositorioGitHub/ArcPy-GIS/Mixed/Tema_04/Capas"
inWorkspace = "D:/RepositorioGitHub/ArcPy-GIS/Mixed"
pathUrl_Result = "D:/RepositorioGitHub/ArcPy-GIS/Project/Seccion-4/Result"

listValues = {}
listValues['frequency'] = []

listValues['frequency'].append({
	'inFeatures'	 : os.path.join(inWorkspace, "Tema_01/Capas/Forestal.shp"),
	'outFeatures'	 : os.path.join(pathUrl_Result, "Frequency/frecuency_01.dbf"),
	'frequencyFields': ["DESCRIP"],
	'summaryFields'  : ["AREA", "PERIMETER"]
})

listValues['frequency'].append({
	'inFeatures'	 : os.path.join(inWorkspace, "Tema_01/Capas/Forestal.shp"),
	'outFeatures'	 : os.path.join(pathUrl_Result, "Frequency/frecuency_02.dbf"),
	'frequencyFields': ["CATEGOR"],
	'summaryFields'  : ["AREA", "PERIMETER"]
})

# El total de quebradas mas su altitud.
listValues['frequency'].append({
	'inFeatures'	 : os.path.join(inWorkspace, "Tema_02/Capas/Rios_Quebradas.shp"),
	'outFeatures'	 : os.path.join(pathUrl_Result, "Frequency/frecuency_03.dbf"),
	'frequencyFields': ["Rasgo_Prin"],
	'summaryFields'  : ["Longitud"]
})

listValues['frequency'].append({
	'inFeatures'	 : os.path.join(inWorkspace, "Tema_02/Capas/Rios_Quebradas.shp"),
	'outFeatures'	 : os.path.join(pathUrl_Result, "Frequency/frecuency_04.dbf"),
	'frequencyFields': ["Rasgo_Secu"],
	'summaryFields'  : ["Longitud"]
})

for item in listValues['frequency']:
	arcpy.Frequency_analysis(
		in_table 		= item['inFeatures'],
		out_table 		= item['outFeatures'],
		frequency_fields= item['frequencyFields'],
		summary_fields 	= item['summaryFields']
	)