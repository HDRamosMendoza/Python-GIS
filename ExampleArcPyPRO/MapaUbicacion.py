#!/usr/bin/env python
# -*- coding: utf-8 -*-

import arcpy
import os
import sys

## Autpomatización de mapas de ubicación.

# Autor: "Heber "Daniel" Ramos Mendoza - HDRamosMendoza."
# Redes sociales: HDRamosMendoza
# Correo: heber.daniel.ramos.mendoza@gmail.com
# Web: https://hdramosmendoza.github.io/Perfil-Profesional/

arcpy.env.overwriteOutput = True

class EmptyRows(Exception):
    pass

class MapaUbicacion:
    def __init__(self):
        self.out_pathProject = r'D:\MasterGis_Online\12 Script Python\ProyectoModelo\MapaUbicacion\MapaUbicacion.aprx'

    def main(self):
        # while os.path.isfile(path_project):
        try:
            # Proyecto actual
            project_aprx = arcpy.mp.ArcGISProject(self.out_pathProject)
            # Mapa de Departamentos
            mapDepartamentos = project_aprx.listMaps("Departamentos")[0]
            # Mapa de Provincias
            mapProvincias = project_aprx.listMaps("Provincias")[0]
            # Mapa de Distritos
            mapDistritos = project_aprx.listMaps("Distritos")[0]

            # Asignando carpeta de trabajo
            arcpy.env.workspace = os.path.join(project_aprx.homeFolder,'Shapefile')

            # Lista los "shapefile"
            fc_list = arcpy.ListFeatureClasses()

            # Este seria otra forma pero es un limitado
            # fc_list_new = ["GPO_{}".format(item) for item in fc_list if item != '']
            # arcpy.FeatureClassToGeodatabase_conversion(fc_list_new, os.path.abspath(project_aprx.defaultGeodatabase))

            # Se carga los datos a la GDB
            for itemShapefile in fc_list:
                # Determine la nueva ruta y el nombre de la clase de entidad de salida
                # [0]. Obtiene el nombre -> os.path.splitext(itemShapefile)[0]
                # [1]. Obtiene la extensión -> os.path.splitext(itemShapefile)[1]
                # desc.datatype ==> shapefile
                desc = arcpy.Describe(itemShapefile)

                # Nombre del feature
                nameFeature = os.path.splitext(itemShapefile)[0]
                if desc.shapeType == 'Polyline':
                    nameFeature = "GPL_{}".format(nameFeature)
                elif desc.shapeType == 'Point':
                    nameFeature = "GPT_{}".format(nameFeature)
                elif desc.shapeType == 'Polygon':
                    nameFeature = "GPO_{}".format(nameFeature)
                else:
                    itemShapefile = None

                out_featureClass = os.path.join(project_aprx.defaultGeodatabase, nameFeature)
                pathSave_Layer = os.path.join(project_aprx.homeFolder, "Layer", nameFeature)
                # Se crea si no existe el GDB
                if not arcpy.Exists(out_featureClass):
                    # Se copia a la GDB
                    arcpy.CopyFeatures_management(itemShapefile, out_featureClass)

                    # Nombre temporal
                    tempLayer = nameFeature

                    # Se guarda en memoria
                    arcpy.MakeFeatureLayer_management(out_featureClass, nameFeature)

                    # Se guarda un .lyrx en la carpeta LAYER
                    arcpy.SaveToLayerFile_management(
                        nameFeature, os.path.join(project_aprx.homeFolder, "Layer", nameFeature), "ABSOLUTE"
                    )

                    if os.path.splitext(itemShapefile)[0] == 'DEPARTAMENTOS':
                        lf_departamentos = arcpy.mp.LayerFile(pathSave_Layer + ".lyrx")
                        mapDepartamentos.addLayer(lf_departamentos)
                    elif os.path.splitext(itemShapefile)[0] == 'PROVINCIAS':
                        lf_provincias = arcpy.mp.LayerFile(pathSave_Layer + ".lyrx")
                        mapProvincias.addLayer(lf_provincias)
                    elif os.path.splitext(itemShapefile)[0] == 'DISTRITOS':
                        lf_distritos = arcpy.mp.LayerFile(pathSave_Layer + ".lyrx")
                        mapDistritos.addLayer(lf_distritos)
                    else:
                        pass

                # else:
                #
                #     if os.path.splitext(itemShapefile)[0] == 'DEPARTAMENTOS':
                #         lf_departamentos = arcpy.mp.LayerFile(pathSave_Layer + '.lyrx')
                #         mapDepartamentos.addLayer(lf_departamentos)
                #     elif os.path.splitext(itemShapefile)[0] == 'PROVINCIAS':
                #         lf_provincias = arcpy.mp.LayerFile(pathSave_Layer + '.lyrx')
                #         mapProvincias.addLayer(lf_provincias)
                #     elif os.path.splitext(itemShapefile)[0] == 'DISTRITOS':
                #         lf_distritos = arcpy.mp.LayerFile(pathSave_Layer + '.lyrx')
                #         mapDistritos.addLayer(lf_distritos)
                #     else:
                #         pass



            # Asignando carpeta de trabajo
            arcpy.env.workspace = os.path.abspath(project_aprx.defaultGeodatabase)


            # fc_list_lyr = arcpy.ListFeatureClasses()
            # print("Ramos")
            # for itemLyr in fc_list_lyr:
            #     print(itemLyr)
            #     # Convertir de GDB a LAYER.a/mexico.gdb/cities"
            #     tempLayer = "Temp_lyr_{}".format(itemLyr)
            #     arcpy.MakeFeatureLayer_management(itemLyr, tempLayer)
            #     arcpy.SaveToLayerFile_management(tempLayer, os.path.join(project_aprx.homeFolder, "Layer", itemLyr),"ABSOLUTE")
            # print("Ramos")

            #map.name = "Departamentos"
            print(project_aprx.defaultGeodatabase)

            #abc = arcpy.MakeFeatureLayer_management(os.path.join(project_aprx.defaultGeodatabase,"GPO_DEPARTAMENTOS"), "cities_lyr")
            #ttt = os.path.join(project_aprx.defaultGeodatabase,'GPO_DEPARTAMENTOS')

            print(" - - - - - - - ")
            featureclasses = arcpy.ListFeatureClasses()
            # Copy shapefiles to a file geodatabase
            for fc in featureclasses:
                print(fc)
            print(" - - - - - - - ")

            #qwe = arcpy.mp.LayerFile(abc)
            #map.addLayer(qwe)

            for m in project_aprx.listMaps():
                print("Map: {0} Layers".format(m.name))
                for lyr in m.listLayers():
                    if lyr.isBroken:
                        print("(BROKEN) " + lyr.name)
                    else:
                        print("  " + lyr.name)




            # Guarda los cambios en el proyecto
            project_aprx.save()

            # Elimina el "Objeto del Proyecto"
            del project_aprx

            # map.addLayer(lf)

            #lyt = project_aprx.listLayouts("Main Attractions*")[0]
            #lyt.exportToPDF(r"C:\Project\YosemiteNP\Output\Yosemite.pdf", resolution=300)

            #except EmptyRows: print("Oops!  No existe proyecto.")

        # Imprime solo el error de ArcGIS
        except arcpy.ExecuteError:
            print(arcpy.AddError(arcpy.GetMessages(2)))
        # Captura de cualquier error de python
        except Exception:
            e = sys.exec_info()[1]
            print(e.args[0])

if __name__ == "__main__":
    mapUbicacion = MapaUbicacion()
    mapUbicacion.main()



# #print(project_aprx.listMaps()[0])
# #lf = arcpy.mp.LayerFile(r'D:\MasterGis_Online\12 Script Python\8 AutomatizacionProduccionMapas\Map_production\Schools.lyrx')
# #map.addLayer(lf)
# print('---')
#
# for lm in project_aprx.listMaps():
#     '''Te Muestra las capas activas'''
#     print("Mapa: " + lm.name)
#
# for lyr in lm.listLayers():
#     print("  " + lyr.name)
#
#     # Se cambia el nombre
#     if lyr.name == "ParkingMeters":
#         lyr.name = "parkingLayer"
#
#     # Se cambia el nombre
#     if lyr.name == "Schools":
#         lyr.name = "schoolsLayer"
#
# '''Caracteristicas del layout'''
# print("Layout")
# for lyt in project_aprx.listLayouts():
#
#     #print(f"  {lyt.name} ({lyt.pageHeight} x {lyt.pageWidth} {lyt.pageUnits})")
#     print(f"  {lyt.name}")
#
#     # Se cambia el nombre
#     if lyt.name == "CorvallisMeters":
#         lyt.name = "Corvallis Meters Map"
#
#     # Se lista TEXT_ELEMENT
#     elemList  = lyt.listElements("TEXT_ELEMENT")
#     print("List - > TEXT_ELEMENT")
#     for itemText in elemList:
#         print(itemText.name)
#         if itemText.name == "Corvallis Meters":
#             itemText.name = "Corvallis Parking Meters Inventory Report"
#
#     print("List - > TEXT_ELEMENT")
#
# # Cambio de posición
# parkingLayer_in = project_aprx.listMaps()[0].listLayers()[1]
# schoolsLayer_in = project_aprx.listMaps()[0].listLayers()[0]
#
# map.moveLayer(parkingLayer_in,schoolsLayer_in,"BEFORE")
#
# #print("Se modifica la posición")
# #print(project_aprx.listMaps()[0].listLayers()[0])
#
# # Se guarda el proyecto
# project_aprx.save()
#
# # Se guarda una copia del proyecto "CorvallisMeters" en "CorvallisMeters_HDRM.aprx"
# project_aprx.saveACopy(r'D:\MasterGis_Online\12 Script Python\8 AutomatizacionProduccionMapas\Map_production\CorvallisMeters_HDRM.aprx')
#
# # Se elimina el "Objeto del Proyecto"
# del project_aprx
#
# # Se elimina el "Objeto del Archivo"
# #del lf