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
        arcpy.CreateDomain_management( out_GDB, 
            dominio[x][0]["FieldName"],
            dominio[x][0]["FieldDescription"],
            dominio[x][0]["FieldType"],
            dominio[x][0]["FieldDomainType"]) 
               
        # Asignando valores al DOMINIO
        for codedValues in dominio[x][0]["FieldCodedValues"]:   
            arcpy.AddCodedValueToDomain_management(out_GDB,
                dominio[x][0]["FieldName"],
                codedValues["Code"],
                codedValues["Description"])
            
        print dominio[x][0]["FieldName"] + " creado"

    print 'Se creo los DOMINIOS'

except Exception as err:
    print(err.args[0])