#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor 	: Ing. Daniel Ramos Mendoza
# Web		: HDRamosMendoza.github.io/Perfil-Profesional
# Email		: heber.daniel.ramos.mendoza@gmail.com
# Móvil		: 051 999130638
# Originario: Perú - Lima
# NOTA: No es el mejor código que eh realizado. Es una simple demo de mis inicios de un par de años atras.
import arcpy
import os

arcpy.env.overwriteOutput = True
arcpy.env.workspace = "D:\\RepositorioGitHub\\ArcPy-GIS\\Mixed\\Tema_05\\Capas"
inWorkspace = "D:\\RepositorioGitHub\\ArcPy-GIS\\Mixed\\Tema_05\\Capas"
pathUrl_Result = "D:\\RepositorioGitHub\\ArcPy-GIS\\Project\\Seccion-5\\Result"
#WGS 1984 UTM Zone 18S
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(32718)

# Caso Practico 1:
# - El presidente del Gobierno Regional de Lima, autoriza que se haga un EIA,
#   para determinar los Centros Poblados que se encuentran afectados por 4 Industrias
#	> Radio de Influencia:
#		- Industria 01 (4,000 km).
#		- Industria 02 (2,500 km).
#		- Industria 03 (3,500 km).
#		- Industria 04 (4,500 km).
#	> Jurisdiccion:
#		- Distrito.
#		- Provincia.
#		- Departamento.
#	> Distancia:
#		- Centros Poblados a las Industrias.
#	
#	4236
#	
#   ¿Qué es un EIA?.
#	https://www.senace.gob.pe/wp-content/uploads/2016/10/info_que_es_eia.pdf

listValues = {}
listValues['bufferIndustrias'] = []
listValues['intersect'] = []
listValues['near'] = []

listValues['bufferIndustrias'].append({
	'inFeatures': 'Industrias.shp',
	'outFeatures': os.path.join(pathUrl_Result, 'Influencia.shp'),
	'bufferDistanceField': 'Contaminac',
	'lineSide': 'FULL',
	'lineEndType': 'ROUND',
	'dissolveOption': 'ALL'
})

for item in listValues['bufferIndustrias']:
	arcpy.Buffer_analysis(
		in_features = item['inFeatures'],
		out_feature_class = item['outFeatures'],
		buffer_distance_or_field = item['bufferDistanceField'],
		line_side = item['lineSide'],
		line_end_type = item['lineEndType'],
		dissolve_option = item['dissolveOption']
   	)
# Tambien se puede realizar por un Union Espacial.
# Vamos a extraer los centros poblados de la Influencia.
listValues['intersect'].append({
	'inFeatures'  	: ['Influencia.shp', 'Centros_Poblados.shp'],
	'joinAttributes': 'ALL',
	'outFeatures' 	: os.path.join(pathUrl_Result, 'ccppAfectados.shp'),
	'outputType' 	: 'INPUT'
})

arcpy.Intersect_analysis(
	in_features 		= listValues['intersect'][0]['inFeatures'],
	out_feature_class 	= listValues['intersect'][0]['outFeatures'],
	join_attributes 	= listValues['intersect'][0]['joinAttributes'],
	output_type 		= listValues['intersect'][0]['outputType']
)

# Ahora tenemos que ver cual es su jurisdicción. A que Provincia, Distrito y Departamento.
# Eliminar campos que no vamos a utilizar
arcpy.DeleteField_management(
	listValues['intersect'][0]['outFeatures'], 
 	["FID_Influe", "Id", "FID_Centro"]
)

# Para tener la jurisdicción vamos a realizar un INTERSECT entre CentrosPobladosAfectados.shp y Distritos.shp
listValues['intersect'].append({
	'inFeatures'  	: [os.path.join(pathUrl_Result, 'ccppAfectados.shp'), 'Distritos.shp'],
	'joinAttributes': 'ALL',
	'outFeatures' 	: os.path.join(pathUrl_Result, 'ccppAfectados_Jurisdiccion.shp'),
	'outputType' 	: 'INPUT'
})

arcpy.Intersect_analysis(
	in_features 		= listValues['intersect'][1]['inFeatures'],
	out_feature_class 	= listValues['intersect'][1]['outFeatures'],
	join_attributes 	= listValues['intersect'][1]['joinAttributes'],
	output_type 		= listValues['intersect'][1]['outputType']
)

# Eliminar campos que no vamos a utilizar
arcpy.DeleteField_management(
	listValues['intersect'][1]['outFeatures'], 
 	["FID_Distri", "FID_CP_Afe"]
)

#Ahora vamos a determinar la distancia que tiene los centros poblados a las INDUSTRIAS.
listValues['near'].append({
	'inFeatures'	: os.path.join(pathUrl_Result, 'ccppAfectados_Jurisdiccion.shp'),
	'nearFeatures' 	: ['Industrias.shp'],
	'searchRadius' 	: 'Unknom',
	'location'		: False,
	'angle'			: False,
	'method'		: 'PLANAR'
})

arcpy.Near_analysis(
	in_features = listValues['near'][0]['inFeatures'],
	near_features = listValues['near'][0]['nearFeatures'],
	location	= listValues['near'][0]['location'],
	angle 	= listValues['near'][0]['angle'],
	method	= listValues['near'][0]['method']
)
