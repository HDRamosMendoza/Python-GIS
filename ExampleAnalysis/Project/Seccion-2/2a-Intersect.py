#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/intersect.htm
# Nos permite conbinar informacion cartográfica y 
# alfa númerica a la vez. De una o varias capas de 
# polígono, línea o punto.

# Autor 	: Ing. Daniel Ramos Mendoza
# Web		: HDRamosMendoza.github.io/Perfil-Profesional
# Email		: heber.daniel.ramos.mendoza@gmail.com
# Móvil		: 051 999130638
# Originario: Perú - Lima
# NOTA: No es el mejor código que eh realizado. Es una simple demo de mis inicios de un par de años atras.
import arcpy
import os

arcpy.env.overwriteOutput = True
arcpy.env.workspace = "D:\\RepositorioGitHub\\ArcPy-GIS\\Mixed\\Tema_02\\Capas"
inWorkspace = "D:\\RepositorioGitHub\\ArcPy-GIS\\Mixed\\Tema_01\\Capas"

xy_tolerance = ""
pathUrl_Result = "D:\\RepositorioGitHub\\ArcPy-GIS\\Project\\Seccion-2\\Result"

# Obtener información de las cuencas hidrográficas del Perú
# y que me indique a categoria borestal pertenece.

# Execute Table Select
listValues = {}
listValues['intersect'] = []

'''
# ERROR AL EJECUTAR EL CODIGO. NO REALIZA INTERSECT CORRECTAMENTE.
listValues['intersect'].append({
		'inFeatures'  	: [
							os.path.join(inWorkspace,'Cuencas_Hidrograficas.shp'),
							os.path.join(inWorkspace,'Forestal.shp')
						],
		'joinAttributes': "ALL",
		'outFeatures' 	: os.path.join(pathUrl_Result, 'Intersect/Cuenca_Daniel.shp'),
		'outputType' 	: "INPUT"
	})
'''

listValues['intersect'].append({
		'inFeatures'  	: [
							"Restos_Arqueologicos.shp",
							os.path.join(inWorkspace,"Departamentos.shp")
						],
		'joinAttributes': "ALL",
		'outFeatures' 	: os.path.join(pathUrl_Result, 'Intersect/Restos_Arqueologicos_Departamentos.shp'),
		'outputType' 	: "INPUT"
	})

listValues['intersect'].append({
		'inFeatures'  	: [
							"Rios_Quebradas.shp",
							"Vias.shp"
						],
		'joinAttributes': "ALL",
		'outFeatures' 	: os.path.join(pathUrl_Result, 'Intersect/Puentes.shp'),
		'outputType' 	: "POINT"
	})

listValues['intersect'].append({
		'inFeatures'  	: [
							os.path.join(pathUrl_Result, 'Intersect/Puentes.shp'),
							os.path.join(inWorkspace,"Departamentos.shp")
						],
		'joinAttributes': "ALL",
		'outFeatures' 	: os.path.join(pathUrl_Result, 'Intersect/Puentes_Departamentos.shp'),
		'outputType' 	: "POINT"
	})

'''
print listValues['intersect'][0]['inFeatures']
print listValues['intersect'][0]['outFeatures']
print listValues['intersect'][0]['joinAttributes']
print listValues['intersect'][0]['outputType']
'''

for item in listValues['intersect']:
	arcpy.Intersect_analysis(
		in_features 	  	= item['inFeatures'],
		out_feature_class	= item['outFeatures'],
		join_attributes   	= item['joinAttributes'],
		output_type 		= item['outputType']
	)

# Eliminar campos en "Puentes_Departamentos.shp"
arcpy.DeleteField_management(
	listValues['intersect'][2]['outFeatures'], 
 	["FID_Depart", "COUNT", "FID_Vias", "FID_Puente"]
)