#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import arcpy

class Shapefile:
	# Constructor
  def __init__(self,work,geodatabase):
    self.work    	 	= work
    self.geodatabase 	= geodatabase

  # Obtener el work
  def get_work(self):
    try:
      return os.path.join(self.work)
    except:
      print("get_work: Ocurrio una exception")

  # Establecer nuevo WORK
  def set_work(self,work):
    try:
      self.work = work
    except:
      print("set_work: Ocurrio una exception")

  # Obtener la GEODATABASE
  def get_geodatabase(self):
    try:
      return os.path.join(self.geodatabase)
    except:
      print("get_geodatabase: Ocurrio una exception")

  # Establecer nueva GEODATABASE
  def set_geodatabase(self,geodatabase):
    try:
      self.geodatabase = geodatabase
    except:
      print("set_geodatabase: Ocurrio una exception")

  # Lista los archivos de la carpeta
  def dataSource(self, ruta = '.'):
    try:
      return os.listdir(ruta)
    except:
      print("dataSource: Ocurrio una exception")

  # Se asigna REFERENCIA ESPECIAL
  def spatialReference(self,wkid):
    try:
      return arcpy.SpatialReference(wkid)
    except:
      print("dataSource: Ocurrio una exception")