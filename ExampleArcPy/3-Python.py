#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
from arcpy.sa import *

arcpy.CheckOutExtension("spatial")
arcpy.env.workspace = "C:/MyData/MyProject.gdb"
ras1 = "Slope"("elevation", "DEGREE", 0.3043)
ras2 = "SolarRad"
outRAS = (Raster(ras1) + (Raster(ras2)))


