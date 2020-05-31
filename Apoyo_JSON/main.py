import arcpy
import os

'''
arcpy.env.workspace = "D:/MasterGis_Online/Proyecto_MasterGIS/Automation/Apoyo_JSON"
arcpy.JSONToFeatures_conversion("ALA.json", os.path.join("AdministracionLocalDelAgua")) 
'''

'''
arcpy.env.workspace = "D:/MasterGis_Online/Proyecto_MasterGIS/Automation/Apoyo_JSON/LimitesDistrittal"
arcpy.JSONToFeatures_conversion("PIURA.json", os.path.join("distrito","PIURA"))
arcpy.JSONToFeatures_conversion("AMAZONAS.json", os.path.join("distrito","AMAZONAS"))
arcpy.JSONToFeatures_conversion("LIMA.json", os.path.join("distrito","LIMA"))
arcpy.JSONToFeatures_conversion("AYACUCHO.json", os.path.join("distrito","AYACUCHO"))
arcpy.JSONToFeatures_conversion("CALLAO.json", os.path.join("distrito","CALLAO"))
arcpy.JSONToFeatures_conversion("AREQUIPA.json", os.path.join("distrito","AREQUIPA"))
arcpy.JSONToFeatures_conversion("LA LIBERTAD.json", os.path.join("distrito","LA LIBERTAD"))
arcpy.JSONToFeatures_conversion("MADRE DE DIOS.json", os.path.join("distrito","MADRE DE DIOS"))
arcpy.JSONToFeatures_conversion("TACNA.json", os.path.join("distrito","TACNA"))
arcpy.JSONToFeatures_conversion("APURIMAC.json", os.path.join("distrito","APURIMAC"))
arcpy.JSONToFeatures_conversion("PASCO.json", os.path.join("distrito","PASCO"))
arcpy.JSONToFeatures_conversion("HUANCAVELICA.json", os.path.join("distrito","HUANCAVELICA"))
arcpy.JSONToFeatures_conversion("SAN MARTIN.json", os.path.join("distrito","SAN MARTIN"))
arcpy.JSONToFeatures_conversion("LORETO.json", os.path.join("distrito","LORETO"))
arcpy.JSONToFeatures_conversion("LAMBAYEQUE.json", os.path.join("distrito","LAMBAYEQUE"))
arcpy.JSONToFeatures_conversion("TUMBES.json", os.path.join("distrito","TUMBES"))
arcpy.JSONToFeatures_conversion("ANCASH.json", os.path.join("distrito","ANCASH"))
arcpy.JSONToFeatures_conversion("CUSCO.json", os.path.join("distrito","CUSCO"))
arcpy.JSONToFeatures_conversion("UCAYALI.json", os.path.join("distrito","UCAYALI"))
arcpy.JSONToFeatures_conversion("CAJAMARCA.json", os.path.join("distrito","CAJAMARCA"))
arcpy.JSONToFeatures_conversion("MOQUEGUA.json", os.path.join("distrito","MOQUEGUA"))
arcpy.JSONToFeatures_conversion("HUANUCO.json", os.path.join("distrito","HUANUCO"))
arcpy.JSONToFeatures_conversion("ICA.json", os.path.join("distrito","ICA"))
arcpy.JSONToFeatures_conversion("JUNIN.json", os.path.join("distrito","JUNIN"))
arcpy.JSONToFeatures_conversion("PUNO.json", os.path.join("distrito","PUNO"))
'''

'''
arcpy.env.workspace = "D:/MasterGis_Online/Proyecto_MasterGIS/Automation/Apoyo_JSON"
arcpy.JSONToFeatures_conversion("CuerpoDeAguasCodificadas.json", os.path.join("CuerpoDeAguasCodificadas","CuerpoDeAguasCodificadas")) 
'''

'''
arcpy.env.workspace = "D:/MasterGis_Online/Proyecto_MasterGIS/Automation/Apoyo_JSON"
arcpy.JSONToFeatures_conversion("ALA.json", os.path.join("AdministracionLocalDelAgua","AdministracionLocalDelAgua")) 
'''

arcpy.env.workspace = "D:/MasterGis_Online/Proyecto_MasterGIS/Automation/Apoyo_JSON"
arcpy.JSONToFeatures_conversion("AAA.json", os.path.join("AutoridadAdministrativaDelAgua","AutoridadAdministrativaDelAgua"))