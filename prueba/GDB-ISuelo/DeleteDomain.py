#Modulo WorkGDB.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
import os
import json
import WorkGDB

# Instanciando classe principal
mainWork = WorkGDB.GeoDatabase(os.getcwd())
try:
    # Espacio de trabajo
    arcpy.env.workspace = mainWork.pathWork()

    # Nombre de la GDB
    out_GDB = mainWork.geoDatabase()
    
    # Cargando Json de DOMINIOS
    output_ColorJson = open('Json\\dominio.json').read()
    dominio = json.loads(output_ColorJson)

    # Creando Dominios
    for x in dominio:
        arcpy.DeleteDomain_management( out_GDB, 
            dominio[x][0]["FieldName"])
    	print dominio[x][0]["FieldName"] + " eliminado"

    print "Dominios eliminados"

except Exception as err:
    print(err.args[0])