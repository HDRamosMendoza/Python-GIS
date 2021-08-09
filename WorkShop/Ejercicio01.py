import arcpy
import os
arcpy.env.addOutputsToMap = False
arcpy.env.overwriteOutput = True
'''Recomiendad tan solo tener 24 variables de ingreso'''
Arcex = arcpy.GetParameterAsText(0)
Zona = arcpy.GetParameterAsText(1) 

Directorio = os.path.dirname(Arcex)
arcpy.env.workspace = Directorio
arcpy.env.scratchWorkspace = Directorio

arcpy.ExcelToTable_conversion(Arcex, "Lista", "Predio") #dbf
a = arcpy.GetCount_management("Lista") #32u
b = str(a) # "32"
cantidad = int(b) # 32

Cuadro = "Lista"
Datos = [] # ["Juan", "Lucas", "Maria", "Fernanda"]
BASE = arcpy.SearchCursor(Cuadro)
CAMPO = "Nombres" 
for extraer in BASE:
	valor = extraer.getValue(CAMPO)
	Datos.append(valor)
	Predios = Datos 

Zona19 = r"Coordinate Systems\Projected Coordinate Systems\Utm\WGS 1984\Southern Hemisphere\WGS 1984 UTM Zone 19s.prj"
Zona20 = r"Coordinate Systems\Projected Coordinate Systems\Utm\WGS 1984\Southern Hemisphere\WGS 1984 UTM Zone 20s.prj"
Zona21 = r"Coordinate Systems\Projected Coordinate Systems\Utm\WGS 1984\Southern Hemisphere\WGS 1984 UTM Zone 21s.prj"

d = 1
while(d <= Cantidad):
	arcpy.ExcelToTable_conversion(Arcex, "COOR" + str(d), "Hoja" + str(d))
	if Zona == "19":
		info1 = "Procesando el Predio: " + Predios[d-1]
		arcpy.AddMessage(info1)
		arcpy.MakeXYEventLayer_management("COOR" + str(d), "xcoord", "ycoord", "sal" + str(d), Zona19, "")
		arcpy.CopyFeatures_management("sal" + str(d), "Ver_" + Predios[d-1] + ".shp")
		arcpy.Delete_management("COOR" + str(d))
		arcpy.PointsToLine_management("Ver_" + Predios[d-1] + ".shp", "Des_" + Predios[d-1] + ".shp")
		arcpy.FeatureToPolygon_management("Des_" + Predios[d-1] + ".shp", "Pol_" + Predios[d-1] + ".shp")
		arcpy.Delete_management("Des_" + Predios[d-1] + ".shp")
		arcpy.AddField_management("Pol_" + Predios[d-1] + ".shp", "SUPERFICIE", "FLOAT", "8", "2")
		expr = "!shape.area!/10000"
		arcpy.CalculateField_management("Pol_" + Predios[d-1] + ".shp", "SUPERFICIE", expr, "PYTHON")
	elif Zona == "20":
		info1 = "Procesando el Predio: " + Predios[d-1]
		arcpy.AddMessage(info1)
		arcpy.MakeXYEventLayer_management("COOR" + str(d), "xcoord", "ycoord", "sal" + str(d), Zona20, "")
		arcpy.CopyFeatures_management("sal" + str(d), "Ver_" + Predios[d-1] + ".shp")
		arcpy.Delete_management("COOR" + str(d))
		arcpy.PointsToLine_management("Ver_" + Predios[d-1] + ".shp", "Des_" + Predios[d-1] + ".shp")
		arcpy.FeatureToPolygon_management("Des_" + Predios[d-1] + ".shp", "Pol_" + Predios[d-1] + ".shp")
		arcpy.Delete_management("Des_" + Predios[d-1] + ".shp")
		arcpy.AddField_management("Pol_" + Predios[d-1] + ".shp", "SUPERFICIE", "FLOAT", "8", "2")
		expr = "!shape.area!/10000"
		arcpy.CalculateField_management("Pol_" + Predios[d-1] + ".shp", "SUPERFICIE", expr, "PYTHON")
	else:
		info1 = "Procesando el Predio: " + Predios[d-1]
		arcpy.AddMessage(info1)
		arcpy.MakeXYEventLayer_management("COOR" + str(d), "xcoord", "ycoord", "sal" + str(d), Zona21, "")
		arcpy.CopyFeatures_management("sal" + str(d), "Ver_" + Predios[d-1] + ".shp")
		arcpy.Delete_management("COOR" + str(d))
		arcpy.PointsToLine_management("Ver_" + Predios[d-1] + ".shp", "Des_" + Predios[d-1] + ".shp")
		arcpy.FeatureToPolygon_management("Des_" + Predios[d-1] + ".shp", "Pol_" + Predios[d-1] + ".shp")
		arcpy.Delete_management("Des_" + Predios[d-1] + ".shp")
		arcpy.AddField_management("Pol_" + Predios[d-1] + ".shp", "SUPERFICIE", "FLOAT", "8", "2")
		expr = "!shape.area!/10000"
		arcpy.CalculateField_management("Pol_" + Predios[d-1] + ".shp", "SUPERFICIE", expr, "PYTHON")

	d = d + 1

arcpy.Delete_management("Lista")
info = "Proceso terminado con exito !!!"
arcpy.AddMessage(info)
