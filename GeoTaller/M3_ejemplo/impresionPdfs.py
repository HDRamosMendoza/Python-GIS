import arcpy
import time
import pythonaddins

arcpy.env.overwriteOutput = True

class Impresion:
	def __init__(self):
		self.mxd = arcpy.mapping.MapDocument("CURRENT")
		self.df = arcpy.mapping.ListDataFrames(self.mxd, "Layers_01")[0]
		self.influencia = arcpy.mapping.ListLayers(self.mxd, "Influencia")[0]
		self.viviendas = arcpy.mapping.ListLayers(self.mxd, "Viviendas")[0]
		self.shapeInfluencia = [x[0] for x in arcpy.da.SearchCursor(self.influencia, ["SHAPE@"])][0]
		self.barraEscala = arcpy.mapping.ListLayoutElements(self.mxd, "MAPSURROUND_ELEMENT", "SCBAR")[0]
		self.agrupacion = arcpy.mapping.ListLayoutElements(self.mxd, "GRAPHIC_ELEMENT", "AGRUPACION")[0]
		self.norte = arcpy.mapping.ListLayoutElements(self.mxd, "MAPSURROUND_ELEMENT", "North Arrow")[0]
		self.lyraleatorios = r'D:\geoTaller\M3_ejemplo\lyr\aleatorios.lyr' #---------------------> REFERENCIAR


	def par(self):
		self.agrupacion.elementPositionY = 0.5
		self.df.elementPositionY = 3.8
		self.barraEscala.elementPositionY = 4
		self.norte.elementPositionY = 26
		arcpy.RefreshActiveView()
	

	def impar(self):
		self.agrupacion.elementPositionY = 24.5
		self.df.elementPositionY = 0.5
		self.barraEscala.elementPositionY = 1
		self.norte.elementPositionY = 22.5
		arcpy.RefreshActiveView()

		
	def main(self):
		count = 0
		for x in arcpy.da.SearchCursor(self.viviendas, ["SHAPE@"]):
			if x[0].overlaps(self.shapeInfluencia):
				count = count + 1
				if count%2 == 0:
					self.par()
					if count == 12:
						self.df.extent = aleatorios.getExtent()
						arcpy.RefreshActiveView()
						time.sleep(5)
						arcpy.mapping.RemoveLayer(self.df, aleatorios)
						time.sleep(2)
					elif count == 14:
						controlador = 24000
						self.df.scale = controlador
						self.viviendas.showLabels = False
						while self.df.scale >= 500:
							self.df.scale = controlador
							controlador = controlador - 400
							arcpy.RefreshActiveView()
						self.viviendas.showLabels = True
						break

				else:
					self.impar()
					if count == 5:
						arcpy.CreateRandomPoints_management('in_memory', 'aleatorios', self.influencia, "#", 60)
						aleatorios = arcpy.mapping.ListLayers(self.mxd, "aleatorios")[0]
						self.df.extent = aleatorios.getExtent()
						arcpy.RefreshActiveView()
						arcpy.RefreshTOC()
						time.sleep(10)
					elif count == 9:
						arcpy.ApplySymbologyFromLayer_management(aleatorios, self.lyraleatorios)
						self.df.extent = aleatorios.getExtent()
						arcpy.RefreshActiveView()
						arcpy.RefreshTOC()
						time.sleep(10)
				self.df.extent = x[0].extent
				time.sleep(2)
				arcpy.RefreshActiveView()
		pythonaddins.MessageBox("El proceso se ejecuto satisfactoriamente", "MSG")


if __name__ == "__main__":
	obj = Impresion()
	obj.main()

				



