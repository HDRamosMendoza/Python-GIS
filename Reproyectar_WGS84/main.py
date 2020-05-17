#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import arcpy
import zipfile
from util import shapefile

# Inicializa SHAPEFILE
shp = shapefile.Shapefile(
	work = 'D:\\MasterGis_Online\\Proyecto_MasterGIS\\Shapefile',
	geodatabase = 'D:\\MasterGis_Online\\Proyecto_MasterGIS\\Geodatabase\\GDB_Hidrico.gdb'
)

def main(shp):

	# Ruta de SHAPEFILE
	pathWork = shp.get_work()
	# Ruta de la GEODATABASE
	pathGDB = shp.get_geodatabase()

	# Antes de entrar a la ruta se tiene que verificar si existe el directorio
	if (os.path.exists(pathWork)):
		# Lista los archivos de la carpeta
		outDir = shp.dataSource(pathWork)
		# Lista todos los archivos de la carpeta shapefile.
		for infile in outDir:
			merge = []
			# Ruta de origen
			infile_zip = os.path.join(pathWork,infile)
			#arcpy.env.workspace = os.path.join(pathWord, infile)
			zipfilename = shp.dataSource(infile_zip)
			#print(len(zipfilename))
			# Lista todos los .zip de la carpeta
			for filename in zipfilename:
				# Ruta del .zip
				fileZip = os.path.join(pathWork,infile,filename)
				# Valida solo si es .zip
				if(zipfile.is_zipfile(fileZip)):
					nameFile = filename.split('.')[0]
					'''
						Paso 1 - Lo descomprime.
					'''
					archivo_zip = zipfile.ZipFile(os.path.join(fileZip), "r")
					# Ruta en donde se va a extraer el archivo
					geoJSON = os.path.join(infile_zip,filename.split('.')[0])
					# Donde se va guardar
					archivo_zip.extractall(pwd='',path=geoJSON)
					# Se accede al shapefile
					shapefile = os.path.join(geoJSON,'OGRGeoJSON.shp')
					'''
						PASO 2 - Se define la projección y asigna la referencia espacial
					'''
					arcpy.DefineProjection_management(
						shapefile,
						shp.spatialReference(wkid=102100)
					)
					'''
						PASO 3 - Se reproyecta y guarda con el mismo nombre del comprimido .zip
					'''
					arcpy.Project_management(
						shapefile, 
						os.path.join(geoJSON,filename.split('.')[0]),
						shp.spatialReference(wkid=4326)
					)
					'''
						Paso 4 - Se agrega para el MERGE
					'''
					merge.append(
						os.path.join(
							geoJSON,
							'{0}.{1}'.format(filename.split('.')[0],'shp')
						)
					)
			
			# Ruta de la carpeta
			fileFC = os.path.join(pathGDB,infile)
			# Valida. Si existe lo elimina.
			if arcpy.Exists(fileFC):
				# Se elimina para no tener problema en su creación
				arcpy.Delete_management(fileFC)
			'''
				Paso 5 - Geoprocesamiento de MERGE
			'''
			arcpy.Merge_management(
				merge,fileFC,arcpy.FieldMappings()
			)
			'''
				Paso 6 
				- Lista y elimina todos los archivos que no son .zip
				- Se elimina par poder ejecutar cuantas veces se requiera
			'''
			# Lista todos los archivos .zip
			for filename in zipfilename:
				# Ruta del .zip
				fileZip = os.path.join(pathWork,infile,filename.split('.')[0])
				# Valida solo si es .zip o carpeta
				if(zipfile.is_zipfile(fileZip)):
					pass
				else:
					shutil.rmtree(os.path.join(fileZip))
	else:
		print("No existe RUTA")

'''
	Heber Daniel Ramos Mendoza
	---------------------------------
	PRESENTATION: 
		I'm a GIS/WEB developer. 
	WEB: 
		https://HDRamosMendoza.github.io/Perfil-Profesional
	Móvil: 
		051 999130638
	--------------------------------
	Lima - Perú
'''

if __name__ == "__main__":
    main(shp)