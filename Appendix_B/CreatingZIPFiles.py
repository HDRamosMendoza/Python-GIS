import os
import zipfile

# Crea el archivo comprimido
zfile = zipfile.ZipFile("shapefile.zip", "w", zipfile.ZIP_STORED)
files = os.listdir("c:/ArcpyBook/data")
# Recorre los archivos con extensiones especificas
for f in files:
	if f.endswith("shp") or f.endswith("dbf") or f.endswith("shx"):
	zfile.write("C:ArcpyBook/data/" + f)

# La siguente linea es para que no se guarde la ruta en el .zip solo se guarde el expediente(file).
# zipFile.write (os.path.join(arcpy.env.scratchFolder,f),f,compress_type = zipfile.ZIP_DEFLATED)

# Lista los archivos comprimidos 
for f in zfile.namelist():
	print "Added %s" %f

#Se cierra. Lo adecuado seria trabajarlo en un WHILE
zfile.close()