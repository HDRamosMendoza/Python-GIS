#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Cómo obtener las propiedades de datos y verificar una extension.
import arcpy
import os

PATH_WORK = r'c:/data/Portland.gdb/streets'
print arcpy.Exists(PATH_WORK)
boolPath = arcpy.Exists(PATH_WORK)

try:
    #if boolPath:
        sr = arcpy.Describe("c:/data/Portland.gdb/streets").spatialReference

        print sr.name

        #Print available
        print arcpy.CheckExtension("spatial")

        arcpy.CheckOutExtension("spatial")
    #else:
    #    print "No Exite el objeto geográfico"
except IOError as err:
    #Para controlar el error de no existencia IOError
    print "Error OS {0}".format(err)
    print("Oops! No era valido. Intente de nuevo")
    with open(os.path.join(os.path.dirname(__file__), 'log.txt'), 'w') as f:
        f.write(err.message)
        f.close()