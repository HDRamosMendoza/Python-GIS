#Modulo WorkGDB.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import arcpy
from arcpy import env
import json
import WorkGDB

# Instanciando classe principal.
mainWork = WorkGDB.GeoDatabase(os.getcwd())

print mainWork

arcpy.env.workspace = r'D:\PruebaGDB\GDB-ISuelo'

# output_FCJson = open("Json\\GPT_IS_InfoSuelo.json").read()

# arcpy.JSONToFeatures_conversion("D:\PruebaGDB\GDB-ISuelo\Json\GPT_IS_InfoSuelo.json", os.path.join("MD-DRME-IS-0402-2017.v.1.0.gdb","GPT_IS_InfoSuelo"))
arcpy.TableToExcel_conversion("MD-DRME-IS-0402-2017.v.1.0.gdb/GPT_IS_InfoSuelo", "GPT_IS_InfoSuelo.xls")

#arcpy.TableToExcel_conversion("MD-DRME-IS-0402-2017.v.1.0.gdb/GPT_IS_InfoSuelo", "GPT_IS_InfoSuelo.xls")

#arcpy.TableToExcel_conversion("MD-DRME-IS-0402-2017.v.1.0.gdb/TB_IS_01_VGCampo", "TB_IS_01_VGCampo.xls")

#arcpy.TableToExcel_conversion("MD-DRME-IS-0402-2017.v.1.0.gdb/TB_IS_02_VGGeologoFicha", "TB_IS_02_VGGeologoFicha.xls")

#arcpy.TableToExcel_conversion("MD-DRME-IS-0402-2017.v.1.0.gdb/TB_IS_03_VPMuestras", "TB_IS_03_VPMuestras.xls")

print 'Finalizo'




#import arcpy
#import os
#arcpy.env.workspace = "c:/data"
#arcpy.JSONToFeatures_conversion("myjsonfeatures.json", os.path.join("outgdb.gdb","myfeatures"))