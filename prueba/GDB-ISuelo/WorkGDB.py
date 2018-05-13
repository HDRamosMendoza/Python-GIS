import arcpy
# Clase de Sistema referencial
class SpatialRefence(object):

    #Constructor
    def __init__(self,wkId = 4326, spatialReference = arcpy.SpatialReference()):
        self.wkId = wkId
        self.spatialReference = spatialReference
        self.spatialReference.factoryCode = self.wkId

    #Soló lectura(getter)
    @property
    def SpatialRefence(self):
        return self.spatialReference

    #Crear el Sistema Referencial
    def createSpatialReference(self):
        self.spatialReference.create()



class GeoDatabase(SpatialRefence):
    def __init__(self,geoPath):
        self.geoPath    = geoPath.replace("\\","\\\\")
        self.geoGDB     = "MD-DRME-IS-0402-2017.v.1.0.gdb"
        self.geoFC      = "GPT_IS_InfoSuelo"
        self.geoFDS     = "DS_0402_DRME_Relaciones"
 
    def pathWork(self):
        return self.geoPath
 
    def geoDatabase(self):
        return self.geoGDB

    def geoDataset(self):
        return self.geoFDS 

    def geoFeatureClass(self):
        return self.geoFC   