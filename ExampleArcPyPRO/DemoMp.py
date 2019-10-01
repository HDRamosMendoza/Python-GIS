import arcpy

#project_aprx = arcpy.mp.ArcGISProject('CURRENT')
project_aprx = arcpy.mp.ArcGISProject(r'D:\MasterGis_Online\12 Script Python\8 AutomatizacionProduccionMapas\Map_production\CorvallisMeters.aprx')
map = project_aprx.listMaps()[0]
#print(project_aprx.listMaps()[0])
#lf = arcpy.mp.LayerFile(r'D:\MasterGis_Online\12 Script Python\8 AutomatizacionProduccionMapas\Map_production\Schools.lyrx')
#map.addLayer(lf)
print('---')

for lm in project_aprx.listMaps():
    '''Te Muestra las capas activas'''
    print("Mapa: " + lm.name)

for lyr in lm.listLayers():
    print("  " + lyr.name)

    # Se cambia el nombre
    if lyr.name == "ParkingMeters":
        lyr.name = "parkingLayer"

    # Se cambia el nombre
    if lyr.name == "Schools":
        lyr.name = "schoolsLayer"

'''Caracteristicas del layout'''
print("Layout")
for lyt in project_aprx.listLayouts():

    #print(f"  {lyt.name} ({lyt.pageHeight} x {lyt.pageWidth} {lyt.pageUnits})")
    print(f"  {lyt.name}")

    # Se cambia el nombre
    if lyt.name == "CorvallisMeters":
        lyt.name = "Corvallis Meters Map"

    # Se lista TEXT_ELEMENT
    elemList  = lyt.listElements("TEXT_ELEMENT")
    print("List - > TEXT_ELEMENT")
    for itemText in elemList:
        print(itemText.name)
        if itemText.name == "Corvallis Meters":
            itemText.name = "Corvallis Parking Meters Inventory Report"

    print("List - > TEXT_ELEMENT")

# Cambio de posición
parkingLayer_in = project_aprx.listMaps()[0].listLayers()[1]
schoolsLayer_in = project_aprx.listMaps()[0].listLayers()[0]

map.moveLayer(parkingLayer_in,schoolsLayer_in,"BEFORE")

#print("Se modifica la posición")
#print(project_aprx.listMaps()[0].listLayers()[0])

# Se guarda el proyecto
project_aprx.save()

# Se guarda una copia del proyecto "CorvallisMeters" en "CorvallisMeters_HDRM.aprx"
project_aprx.saveACopy(r'D:\MasterGis_Online\12 Script Python\8 AutomatizacionProduccionMapas\Map_production\CorvallisMeters_HDRM.aprx')

# Se elimina el "Objeto del Proyecto"
del project_aprx

# Se elimina el "Objeto del Archivo"
#del lf