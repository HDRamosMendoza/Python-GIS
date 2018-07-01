#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/create-thiessen-polygons.htm
# Esta herramienta es muy usado en geomarketing, criminalidad, posicionamiento de ligar optimo para un tipo de centro de venta.

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
listValues['thiessenPolygons'] = []

# - Realizaremos zonas de influencia tomando como criterio los puntos
#   medios de separación que hay entre punto y punto (pasivo y pasivo).
# - Analisis con los puntos medio.
#   Distancia equidistantes.

# fieldsCopy: ALL. Que todos los elementos esten dentro.
listValues['thiessenPolygons'].append({
		'inFeatures' : "Pasivos_Puno.shp",
		'outFeatures': os.path.join(pathUrl_Result, "ThiessenPolygons/Thiessen_01.shp"),
		'fieldsCopy' : "ALL"
	})

# Avarcaremos todo el departamentos de puno.
# "Environment Settings" que tome toda la extension del departamento de PUNO
listValues['thiessenPolygons'].append({
		'inFeatures' : "Pasivos_Puno.shp",
		'outFeatures': os.path.join(pathUrl_Result, "ThiessenPolygons/Thiessen_02.shp"),
		'fieldsCopy' : "ALL"
	})

for item in listValues['thiessenPolygons']:
	arcpy.CreateThiessenPolygons_analysis(
		in_features = item['inFeatures'],
		out_feature_class = item['outFeatures'],
		fields_to_copy = item['fieldsCopy']
	)


'''
import arcpy, os

fc = r'C:\path\to\your.gdb\fc'

desc = arcpy.Describe(fc)

xmin = desc.extent.XMin
xmax = desc.extent.XMax
ymin = desc.extent.YMin
ymax = desc.extent.YMax

print "xmin: %s \nxmax: %s \nymin: %s \nymax: %s" % (xmin, xmax, ymin, ymax)


import arcpy
# Set the extent environment using a keyword.
arcpy.env.extent = "MAXOF"
# Set the extent environment using the Extent class.
arcpy.env.extent = arcpy.Extent(-107.0, 38.0, -104.0, 40.0)
# Set the extent environment using a space-delimited string.
arcpy.env.extent = "-107.0 38.0 -104.0 40.0"
'''