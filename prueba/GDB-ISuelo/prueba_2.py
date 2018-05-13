# -*- coding: utf-8 -*-
import os
import arcpy


# Asignacion de carpeta de trabajo.
#arcpy.env.workspace = out_Folder_Path

out_FC ="C:\OSI_DanielRamos\Sufrimiento\Connection to BDGEOCAT.sde\T_LITOTECA"

field = ["CODIGO_INTERNO_MUESTRA","COD_CAMPO", "NORTE", "ESTE", "ZONA", "LONGITUD", "LATITUD", "CODIGO_HOJA", "CUADRANTE"]

cursor = arcpy.da.SearchCursor( out_FC, field)
for row in cursor:
	print row[0] , row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]