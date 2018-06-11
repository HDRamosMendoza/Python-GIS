#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Cómo obtener las propiedades de datos y verificar una extension.
import arcpy
import os
import time

PATH_WORK = r'c:/data/Portland.gdb/streets'
print arcpy.Exists(PATH_WORK)
boolPath = arcpy.Exists(PATH_WORK)

try:
    sr = arcpy.Describe("c:/data/Portland.gdb/streets").spatialReference
    print sr.name
    print arcpy.CheckExtension("spatial")
    arcpy.CheckOutExtension("spatial")
except IOError as err:
    errorTime = time.strftime("%H:%M:%S")
    print "Error OS {0}".format(err)
    with open(os.path.join(os.path.dirname(__file__), 'log.txt'), 'a') as f:
        f.write(str(errorTime)+ '\n')
        f.write(err.message + '\n')
        f.close()