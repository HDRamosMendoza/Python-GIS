import arcpy

while True:
    try:
        print ("Introduccion a la ruta de una GDB")
        PATH_GDB = input();
        arcpy.env.workspace = r"{}".format(PATH_GDB)
        break
    except:
        print ("Ruta no valida")

# Listamos todos los elementos de nuestra ruta
datasetList = arcpy.ListDatasets("*", "Feature")

print ("Hola Mundo")

