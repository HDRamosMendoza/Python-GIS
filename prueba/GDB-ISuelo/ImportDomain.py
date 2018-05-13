import arcpy
import os
import sys
import WorkGDB

mainWork = WorkGDB.GeoDatabase(os.getcwd())
try:	
	arcpy.env.workspace = mainWork.pathWork() + "\\" + mainWork.geoDatabase()

	#La ruta no debe de tener espacios en blancos	
	domWorkspace = "C:/OSI_DanielRamos/Sufrimiento/2016/DRME-Sedimento-de-Quebrada-Geoquimica/MD-DRME-SQG-001-2016.v.1.0.gdb"
	
	#Export DOMAIN to TABLE - TABLE to DOMAIN
	lista = ['04_DC_LimDistrito', '04_DC_LimProvincia', '04_DC_LimRegion', '04_DC_Direccion', '04_DC_Proyecto']
	for dominio in lista:
		tabla = dominio[6:]
		arcpy.DomainToTable_management(
			in_workspace = domWorkspace, 
			domain_name = dominio,
			out_table = mainWork.pathWork() + "\\" + mainWork.geoDatabase()+"\\"+tabla.strip(),
			code_field = "codigo", 
			description_field = "descripcion")	
		print "Migracion del DOMINIO - " + dominio + " a TABLE"

	for dominio in lista:
		tabla 	= dominio[6:]
		domName = dominio
		domDesc = "Ubigeo de " + dominio[9:]
		domOption = "REPLACE"
		arcpy.TableToDomain_management(
			tabla,
			"codigo",
			"descripcion",
			mainWork.geoDatabase(),
			domName,
			domDesc,
			domOption)
		print "TABLE " + tabla + " migrado al DOMINIO " +  dominio
		
		# Eliminando las TABLAS migradas.
		arcpy.Delete_management(tabla)
except Exception as err:
    print(err.args[0])