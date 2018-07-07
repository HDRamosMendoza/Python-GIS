#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
import os
import time
# Search People

# Variable assigments
fc = "D:/PYTH/Debugging_scripts/SanDiego.gdb/MajorAttractions"
fields = ["NAME", "EMP"]
whereClause = 'EMP > 500'

majorAttractionsLookup = {}
try:
    with arcpy.da.SearchCursor(fc, fields, whereClause) as cursor:
        for place in cursor:
            print ("{0} employs {1} people".format(place[0], place[1]))
            majorAttractionsLookup[place[0]] = place[1]

except IOError as err:
    errorTime = time.strftime("%H:%M:%S")
    print "Error OS {0}".format(err)
    with open(os.path.join(os.path.dirname(__file__), 'log.txt'), 'a') as f:
        f.write(str(errorTime)+ '\n')
        f.write(err.message + '\n')
        f.close()