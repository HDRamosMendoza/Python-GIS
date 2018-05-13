#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
from arcpy import env
from FeatureGDB import ConfigGDB

# Sistema Referencial
outPut_SR = ConfigGDB.SpatialReference()
env.outputCoordinateSystem = outPut_SR.spatialRefence

# Nombre de GeoDatabase
input_GDB = "Prueba.gdb"
# Nombre de Feature Class
# Nota: Identidad geográfica: GPT(punto), GPO(polígono), GPL(línea)
# 		El nombre consta de tre partes separadas por "_". 
#		Identidad geográfica, alis del módulo y abreviatura del nombre de FC.
input_FC = "GPT_IS_InfoSuelo"
# Nombre de Feature DataSet
input_FDS = "DS_0402_DRME_Relaciones"

# Inicializar GEODATABASETB_Subtype
outPut_GDB = ConfigGDB.GeoDatabase(input_GDB,input_FC,input_FDS)

# Creamos la Geodatabase
outPut_GDB.createGeodatabase()

# Creamos el Feature DataSet
outPut_GDB.createFeatureDataSet()

# Creamos el Feature Class
outPut_GDB.createFeatureClass("FeatureJson\\GPT_IS_InfoSuelo.json")

# Creando el Table
outPut_GDB.createTable("FeatureJson\\table.json")

# Creando el SubTipo
outPut_GDB.createSubType("FeatureJson\\table.json","FeatureJson\\subtype.json")

# Asignando GlobalId
outPut_GDB.createSubType("FeatureJson\\table.json")