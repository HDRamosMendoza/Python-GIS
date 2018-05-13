#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import arcpy
import json
from arcpy import env

# Clase de Sistema referencial
class SpatialReference(object):

    # Constructor
    def __init__(self, wkId = 4326):
        self.wkId = wkId
        self.spatialReference = arcpy.SpatialReference()
        self.spatialReference.factoryCode = wkId
        self.spatialReference.create()

    #@property
    #def spatialRefence(self):
        #return self.spatialReference

class GeoDatabase(SpatialReference):

    # Constructor
    def __init__(self, geoDataBase, featureClass, featureDataSet,pathWorkGeoDataBase = os.getcwd()):
        self.pathWorkGeoDataBase = os.path.join(pathWorkGeoDataBase)
        self.geoDataBase = geoDataBase
        self.featureClass  = featureClass
        self.featureDataSet = featureDataSet
        super(GeoDatabase, self)
 
    # Getter workspaceGeoDataBase.
    @property
    def pathWork(self):
        return self.pathWorkGeoDataBase
        
    # Getter self.geoDataBase.
    @property
    def geoGDB(self):
        return self.geoDataBase

    # Getter self.featureClass.
    @property
    def featureC(self):
        return self.featureClass

    # Getter self.featureDataSet.
    @property
    def featureDS(self):
        return self.featureDataSet

    def pathWorkGDB(self):
        return os.path.join(self.pathWork,self.geoGDB)

    # Asigando nuestro nuevo espacio de trabajo
    def workSpace(self):
        arcpy.env.workspace = os.path.join(self.pathWork)

    # Asigando nuestro nuevo espacio de trabajo a la GDB.      
    def workSpaceGDB(self):
        arcpy.env.workspace = self.pathWorkGDB()

    # Create Geodatabase.
    def createGeodatabase(self):
        self.workSpace()
        arcpy.CreateFileGDB_management(
            self.pathWorkGeoDataBase,
            self.geoGDB)
        print "Se creo la GEODATABASE"
    
    # Create Feature DataSet.
    def createFeatureDataSet(self):
        self.workSpace()
        arcpy.CreateFeatureDataset_management(
            self.pathWorkGDB(),
            self.featureDataSet)
            # No funciona el llamado el SR es opcional en la
            # creacion del DATASET
            #self.spatialRefence
        print "Se creo el FEATURE DATASET"

    # Create Feature Class.
    def createFeatureClass(self, pathJson):
        self.workSpaceGDB()
        output_FCJson = open(pathJson).read()
        convert_FCJson = arcpy.AsShape(output_FCJson, True)
        arcpy.CopyFeatures_management(
            convert_FCJson, 
            os.path.join(
                self.pathWorkGDB(),
                self.featureC))

        output_FCJson.close()
        print "Se creo el FEATURE CLASS"

    # Alias del nombre del modulo
    def aliasModule(self,nameGDB):
        positionFirst = nameGDB.find("_")
        positionSecond = nameGDB[positionFirst+1:].find("_")
        return nameGDB[(positionFirst+1):(positionSecond+positionFirst+1)]
    
    # Abreviatura del nombre del modulo
    def abbreviationModule(self,nameGDB):
        positionFirst = nameGDB.find("_")
        positionSecond = nameGDB[positionFirst+1:].find("_")
        nameGDB = nameGDB[positionFirst+1:]
        return nameGDB[(positionSecond+1):]

    # Creando Table
    def createTable(self, pathJson):
        self.workSpaceGDB() 
        output_TablaJson = open(pathJson).read()
        table = json.loads(output_TablaJson)
        alias = self.aliasModule(self.featureC)
        abbreviation = self.abbreviationModule(self.featureC)
        # Creando TABLE.
        for tableItem in table:
            arcpy.CreateTable_management(self.pathWorkGDB(), tableItem)
            # Agregando campos a la TABLE.
            for ItemValue in table[tableItem][0]["TB_ItemCodedValues"]:
                arcpy.AddField_management( tableItem, 
                    ItemValue['ItemName'], 
                    ItemValue['ItemType'], 
                    field_alias  = ItemValue['ItemAlias'],
                    field_length = ItemValue['ItemSize'])
            # Se crea el nombre de la relacion de TABLE a FEATURE CLASS 
            relClass = "RL_" + alias + tableItem[5:9] + abbreviation + tableItem[8:]        
            print "Table " + tableItem + " creado"
            # Asignando relacion de TABLE a FEATURE CLASS 
            arcpy.CreateRelationshipClass_management(
                self.featureC, tableItem, relClass,
                table[tableItem][0]["TB_Type"],
                table[tableItem][0]["TB_ForLabel"],
                table[tableItem][0]["TB_BackLabel"],
                table[tableItem][0]["TB_Notification"],
                table[tableItem][0]["TB_Cardinality"],
                table[tableItem][0]["TB_Attributed"],
                table[tableItem][0]["TB_PrimaryKey"],
                table[tableItem][0]["TB_ForeignKey"])           
            print "\tRelationship "+ self.geoGDB +" - " + tableItem

        output_TablaJson.close()

    # Creando Subtype
    def createSubType(self, pathTableJson, pathSubtypeJson):
        self.workSpaceGDB()
        output_TablaJson = open(pathTableJson).read()
        table = json.loads(output_TablaJson)
        for tableItem in table:
            if table[tableItem][0]["TB_Subtype"] == "Y":
                arcpy.SetSubtypeField_management(tableItem, "ST_MULTIMEDIA")
                output_TablaJson = open(pathSubtypeJson).read()
                stypeDict = json.loads(output_TablaJson)
                for code in stypeDict:
                    arcpy.AddSubtype_management(tableItem, code, stypeDict[code]) 

                output_TablaJson.close()

        output_TablaJson.close() 

    def globalIdTable(self, pathTableJson):
        self.workSpaceGDB()
        output_TablaJson = open(pathTableJson).read()
        table = json.loads(output_TablaJson)
        for tableItem in table:
            arcpy.AddGlobalIDs_management(tableItem)

        output_TablaJson.close()