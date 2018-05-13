#Modulo WorkGDB.py
#!/usr/bin/env python
import arcpy
import os
import sys
import WorkGDB
"""	Nota:	Cuando se asigna los DOMINIOS a los campos deL FC o TB se 
			debe de cerrar el ArcMap y ArcCatalog para que no se
			bloque la ejecucion del codigo."""	
# Instanciando classe principal
mainWork = WorkGDB.GeoDatabase(os.getcwd())
try:
	# Carpeta de trabajo
	arcpy.env.workspace = mainWork.pathWork() + "\\\\" + mainWork.geoDatabase()

	# Asignando DOMINIO a los CAMPOS
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "DIR", "04_DC_Direccion")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "CD_PROY", "04_DC_Proyecto")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "IDENTIFIER", "04_DC_Identifier")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "ZONA", "04_DC_Zona")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "DATUM", "04_DC_Datum")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "REGION", "04_DC_LimRegion")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "PROVINCIA", "04_DC_LimProvincia")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "DISTRITO", "04_DC_LimDistrito")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "COLOR", "04_DC_Color")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "POLLUTION", "04_DC_Pollution")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "EROSION", "04_DC_Erosion")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "SALT_MARSH", "04_DC_SaltMarsh")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "CAUSES", "04_DC_Causes")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "LAND_APPLICATION", "04_DC_LandApplication")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "PHYSIOGNOMY", "04_DC_Physiognomy")
	# arcpy.AssignDomainToField_management("GPT_IS_InfoSuelo", "HISTORIAL", "04_DC_Historial")
	# print "GPT_IS_InfoSuelo - Dominios asignados"
	
	arcpy.AssignDomainToField_management("TB_IS_01_VGCampo", "RRS_POINT", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_01_VGCampo", "CBGTS_POINT", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_01_VGCampo", "SAM_METHOD", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_01_VGCampo", "SAM_DEPTH", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_01_VGCampo", "CHK_M_RECORD", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_01_VGCampo", "CHK_W_Record", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_01_VGCampo", "CHK_U_RECORD", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_01_VGCampo", "HISTORIAL", "04_DC_Historial")
	print "TB_IS_01_VGCampo - Dominios asignados"
	
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "CF_R_CARD", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "PL_CT_CHART", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "PL_RD_DISTRIBUTION", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "PL_SAM_GRID", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "RC_M_RECORD", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "RC_W_RECORD", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "RC_CLARITY", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "S_WS_CODE", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "S_S_COMPONENT", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "S_OS_WEIGHT", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "S_OS_QUALITY", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "S_POLLUTION", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_02_VGGeologoFicha", "HISTORIAL", "04_DC_Historial")
	print "TB_IS_02_VGGeologoFicha - Dominios asignados"
	
	arcpy.AssignDomainToField_management("TB_IS_03_VPMuestras", "QPS_CODE", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_03_VPMuestras", "WPS_CODE", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_03_VPMuestras", "US_CODE", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_03_VPMuestras", "PSCD_DRYING", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_03_VPMuestras", "BBSCD_PROCESSING", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_03_VPMuestras", "SC_PROTOCOL", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_03_VPMuestras", "CS_LBB", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_03_VPMuestras", "USC_WEIGHT", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_03_VPMuestras", "TRE_SUGGESTION", "04_DC_SiNo")
	arcpy.AssignDomainToField_management("TB_IS_03_VPMuestras", "HISTORIAL", "04_DC_Historial")
	print "TB_IS_03_VPMuestras - Dominios asignados"
	
	arcpy.AssignDomainToField_management("TB_IS_04_Multimedia", "HISTORIAL", "04_DC_Historial")
	print "TB_IS_04_Multimedia - Dominios asignados"
	
	print 'Dominio asignados'

	arcpy.AssignDefaultToField_management("GPT_IS_InfoSuelo", "DIR", "DRME")
	arcpy.AssignDefaultToField_management("GPT_IS_InfoSuelo", "ZONA", "18")
	arcpy.AssignDefaultToField_management("GPT_IS_InfoSuelo", "DATUM", "84")
	arcpy.AssignDefaultToField_management("GPT_IS_InfoSuelo", "SAM_UNIT", "INGEMMET")
	arcpy.AssignDefaultToField_management("GPT_IS_InfoSuelo", "HISTORIAL", "A")
	print "GPT_IS_InfoSuelo | Campos por defecto"

	arcpy.AssignDefaultToField_management("GPT_IS_InfoSuelo", "HISTORIAL", "A")
	arcpy.AssignDefaultToField_management("TB_IS_01_VGCampo", "HISTORIAL", "A")
	arcpy.AssignDefaultToField_management("TB_IS_02_VGGeologoFicha", "HISTORIAL", "A")
	arcpy.AssignDefaultToField_management("TB_IS_03_VPMuestras", "HISTORIAL", "A")
	arcpy.AssignDefaultToField_management("TB_IS_04_Multimedia", "HISTORIAL", "A")
	print "Campos por defectos asignados"

	arcpy.SetDefaultSubtype_management("TB_IS_04_Multimedia", "1")
	print "TB_IS_04_Multimedia - 1 | Subtipo por defecto"

	

except Exception as err:
    print(err.args[0])