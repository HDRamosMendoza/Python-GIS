#!/usr/bin/env python
# -*- coding: utf-8 -*-
# source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/summary-statistics.htm
# Me da la sumatoria de área, perimetro, longitud, media, media aritmetica, valor mas algo y bajo entre otros.

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
listValues['summaryStatistics'] = []

listValues['summaryStatistics'].append({
	'inFeatures': os.path.join(inWorkspace, "Tema_01/Capas/Forestal.shp"),
	'outFeatures': os.path.join(pathUrl_Result, "SummaryStatistics/Summary_01.dbf"),
	'statisticsFields':[
		["AREA","SUM"],
		["AREA","MEAN"],
		["AREA","MAX"],
		["AREA","MIN"],
		["AREA","COUNT"]
	],
	'caseField':["DESCRIP","SYMBOL"]
})

listValues['summaryStatistics'].append({
	'inFeatures': os.path.join(inWorkspace, "Tema_01/Capas/Forestal.shp"),
	'outFeatures': os.path.join(pathUrl_Result, "SummaryStatistics/Summary_02.dbf"),
	'statisticsFields':[
		["AREA","SUM"],
		["AREA","MEAN"],
		["PERIMETER","SUM"],
		["PERIMETER","MEAN"],
	],
	'caseField':["CATEGOR"]
})

listValues['summaryStatistics'].append({
	'inFeatures': os.path.join(inWorkspace, "Tema_02/Capas/Rios_Quebradas.shp"),
	'outFeatures': os.path.join(pathUrl_Result, "SummaryStatistics/Summary_03.dbf"),
	'statisticsFields':[
		["Longitud","SUM"],
		["Longitud","MEAN"],
		["Longitud","MIN"],
		["Longitud","MAX"],
	],
	'caseField':["Rasgo_Prin"]
})

for item in listValues['summaryStatistics']:
	arcpy.Statistics_analysis(
		in_table 			= item['inFeatures'],
		out_table 			= item['outFeatures'],
		statistics_fields 	= item['statisticsFields'],
		case_field 			= item['caseField']
	)