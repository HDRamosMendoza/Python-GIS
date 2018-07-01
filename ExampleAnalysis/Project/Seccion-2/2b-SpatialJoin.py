#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: http://desktop.arcgis.com/es/arcmap/10.3/tools/analysis-toolbox/spatial-join.htm
# Nos permitira obtener informacion clasificada por medio de criterio de  proximidad y solapamiento

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
pathUrl_Result = "D:/RepositorioGitHub/ArcPy-GIS/Project/Seccion-2/Result"
inWorkspace = "D:\\RepositorioGitHub\\ArcPy-GIS\\Mixed\\Tema_01\\Capas"

# Execute Table Select
# Se necesita obtener los restos arqueologicos que se encuentren a un 1km 
# de un río o Quebrada. A su vez necesito los restos arqueologicos que 
# se encuentren a 500m o a 100m de Rios y Quebradas.
listValues = {}
listValues['spatialJoin'] = []

listValues['spatialJoin'].append({
		'inFeatures'  	: "Restos_Arqueologicos.shp",
		'joinFeatures'	: "Rios_Quebradas.shp",
		'outFeatures' 	: os.path.join(pathUrl_Result, "SpatialJoin/Arqueologia_1km.shp"),
		'joinOperation' : "JOIN_ONE_TO_ONE",
		'joinType' 		: False,
		'matchOption'	: "WITHIN_A_DISTANCE",
		'searchRadius'	: "1 Kilometers"
	})

listValues['spatialJoin'].append({
		'inFeatures'  	: "Restos_Arqueologicos.shp",
		'joinFeatures'	: "Rios_Quebradas.shp",
		'outFeatures' 	: os.path.join(pathUrl_Result, "SpatialJoin/Arqueologia_500m.shp"),
		'joinOperation' : "JOIN_ONE_TO_ONE",
		'joinType' 		: False,
		'matchOption'	: "WITHIN_A_DISTANCE",
		'searchRadius'	: "500 Meters"
	})

listValues['spatialJoin'].append({
		'inFeatures'  	: "Restos_Arqueologicos.shp",
		'joinFeatures'	: "Rios_Quebradas.shp",
		'outFeatures' 	: os.path.join(pathUrl_Result, "SpatialJoin/Arqueologia_100m.shp"),
		'joinOperation' : "JOIN_ONE_TO_ONE",
		'joinType' 		: False,
		'matchOption'	: "WITHIN_A_DISTANCE",
		'searchRadius'	: "100 Meters"
	})

# Me indique cada departamento el numero de restos
# arqueologicos que se encuentre dentro de su territorio.
'''
	Comprovación:
	- Prendemos los Restos_Arqueologicos, Arqueologia_Departamentos y Departamentos. 
	- Seleccion por atributo Ancash de "Arqueologia_Departamentos.shp". 
	- Realizamos una selección por localización.
		* Seleccionamos "Restos_Arqueologicos".
		* Check: Only show selectable layers in this list.
		* Source Layer: Departamentos.
		* Check: Use selected features.
		* Spatial selection method for target layer feature(s): intersect the source layer feature.
		* Para mostrar lo seleccionado (Arqueologia_Departamentos): 
			Table > Arrange Tables > New Horizontal Tab Group.
'''
listValues['spatialJoin'].append({
		'inFeatures'  	: os.path.join(inWorkspace, "Departamentos.shp"),
		'joinFeatures'	: "Restos_Arqueologicos.shp",
		'outFeatures' 	: os.path.join(pathUrl_Result, "SpatialJoin/Arqueologia_Departamentos.shp"),
		'joinOperation' : "JOIN_ONE_TO_ONE",
		'joinType' 		: True,
		'matchOption'	: "INTERSECT",
		'searchRadius'	: ""
	})

# Realizaremos un analisis en donde me indique los rios que cruzen los departamentos.
listValues['spatialJoin'].append({
		'inFeatures'  	: "Rios_Quebradas.shp",
		'joinFeatures'	: os.path.join(inWorkspace, "Departamentos.shp"),
		'outFeatures' 	: os.path.join(pathUrl_Result, "SpatialJoin/Rios_Cruce_Departamento.shp"),
		'joinOperation' : "JOIN_ONE_TO_ONE",
		'joinType' 		: False,
		'matchOption'	: "CROSSED_BY_THE_OUTLINE_OF",
		'searchRadius'	: ""
	})

# Realizaremos un analisis en donde me indique cuales son las vías que crucen rios.
# Este analisis sirve para indicar que tipo de mantenimiento voy a darle a esas vías.
# Y es diferente a las vías que no cruzan ríos.
listValues['spatialJoin'].append({
		'inFeatures'  	: "Vias.shp",
		'joinFeatures'	: "Rios_Quebradas.shp",
		'outFeatures' 	: os.path.join(pathUrl_Result, "SpatialJoin/Vias_Rios_Cruces.shp"),
		'joinOperation' : "JOIN_ONE_TO_ONE",
		'joinType' 		: False,
		'matchOption'	: "INTERSECT",
		'searchRadius'	: ""
	})

for item in listValues['spatialJoin']:
	arcpy.SpatialJoin_analysis(
		target_features = item['inFeatures'],
		join_features = item['joinFeatures'],
		out_feature_class = item['outFeatures'],
		join_operation = item['joinOperation'],
		join_type = item['joinType'],
		match_option = item['matchOption'],
		search_radius = item['searchRadius']
	)