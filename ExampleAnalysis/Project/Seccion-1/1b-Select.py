#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Source: https://pro.arcgis.com/es/pro-app/tool-reference/analysis/select.htm

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

# Set local variables
listValues = {}
listValues['select'] = []

pathUrl_Result = "D:/RepositorioGitHub/ArcPy-GIS/Project/Seccion-1/Result/"

# Execute Select
listValues['select'].append({
		'Geometry': 'GPT',
		'inFeatures': 'Pasivos_Ambientales_Mineros.shp',
		'outFeatures': os.path.join(pathUrl_Result, 'Pasivos_Ambientales_Mineros_Avandonados.shp'),
		'whereClause': 'CLASE = \'ABANDONADO\''
	})

listValues['select'].append({
		'Geometry': 'GPL',
		'inFeatures': 'Red_Vial_Nacional.shp',
		'outFeatures': os.path.join(pathUrl_Result, 'Red_Vial_Nacional_Sin_Informacion.shp'),
		'whereClause': 'ESTADO = \'Sin Data\' OR ESTADO = \'Sin Informacion\' OR ESTADO = \'SIN INFORMACION\''
	})

listValues['select'].append({
		'Geometry': 'GPO',
		'inFeatures': 'Forestal.shp',
		'outFeatures': os.path.join(pathUrl_Result, 'BosquesProtegidos.shp'),
		'whereClause': 'CATEGOR = \'Bosque de proteccion\''
	})

print listValues['select'][1]['inFeatures']
print "Count: " + str(len(listValues['select']))
for item in listValues['select']:
	arcpy.Select_analysis(item['inFeatures'], item['outFeatures'], item['whereClause'])
	print ("Creado: ", item['inFeatures'], item['outFeatures'])

# Field Calculator
outFeatures = listValues['select'][1]['outFeatures']
fieldName = 'ESTADO'
newExpression = 'newString(!ESTADO!)'
codeblock = """
def newString(paramEstado):
	varReturn = ''
	if (paramEstado == "Sin Data") or (paramEstado == "Sin Informacion") or (paramEstado == "SIN INFORMACION"):
		varReturn = 'Sin Datos'
	return varReturn
"""

arcpy.CalculateField_management(outFeatures, fieldName, newExpression, "PYTHON", codeblock)

# Como hemos extraido informacion de Forestal. Tenemos que actualizar el área.
# Al inicio no nos deja porque está en grados decimales. Y para calcular el área lo teneamos que hacer
# a través de coordenadas planas. Cambiar el data Frame nuestro sistema de referencia a WGS 1984 UTM Zone 18S
# Calcule Geometry :> Units - Hectares [ha]
# Statistics :> Area total

# FALATA TERMINAR ESTOS PUNTOS