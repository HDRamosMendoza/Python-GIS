#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
import os

class Analysis(object):
	def __init__(self, **kwargs):
        self.codigoEspectro = kwargs['codigoEspectro']
        self.spatialReference = kwargs.get('spatialReference', 84)
        #self.descripcion = kwargs['descripcion']

    @property
    def buffer(self):
        arcpy.Buffer_analysis(
			in_features = item['inFeatures'],
			out_feature_class = item['outFeatures'],
			buffer_distance_or_field = item['bufferDistanceField'],
			line_side = item['lineSide'],
			line_end_type = item['lineEndType'],
			dissolve_option = item['dissolveOption']
   		)
