#!/usr/bin/env python
# -*- coding: utf-8 -*-
import arcpy
arcpy.env.overwriteOutput = True
# arcpy.env.workspace = r"D:/PYTH/Debugging_scripts/SanDiego.gdb"
# GEOQUIMICA
# Mi unidad > INGEMMET > Modulos > Geoquimica

arcpy.env.workspace = r"D:\RepositorioGitHub\Python-Coffee\Python-Coffee\DRME - Sedimentos de Quebrada Geoquimica\MD-DRME-SQG-001-2017.v.2.0.mdb"
'''
workspace = "c:/data/gdb.gdb"  
rc_list = [c.name for c in arcpy.Describe(workspace).children if c.datatype == "RelationshipClass"]  

import arcpy, osfrom arcpy import env # Set workspaceenv.workspace = "C:/Users/XXX/Desktop/test.gdb" #get list of relationship classesrc_list = [c.name for c in arcpy.Describe(env.workspace).children if c.datatype == "RelationshipClass"]   #remove all underscoresfor rc in rc_list:    out_data = rc.replace("_","")    
arcpy.Rename_management(os.path.join(env.workspace,rc), out_data)#get the list of relationship classes againrc_list = [c.name for c in arcpy.Describe(env.workspace).children if c.datatype == "RelationshipClass"] for rc in rc_list:       
#    if "reading" in rc OR "action" in rc:        
#add underscores between name and ATTACHREL        
    if "ATTACH" in rc:            
        out_data = rc.replace("ATTACHREL","TblGPS__ATTACHREL")            
        arcpy.Rename_management(os.path.join(env.workspace,rc), out_data)            
        print (rc)         
        #add underscores between name and rel        
        if "rel" in rc:            
            out_data = rc.replace("rel","TblGPS__rel")            
            arcpy.Rename_management(os.path.join(env.workspace,rc), out_data)           
            print (rc)    
        else:        
            #add underscores between name and ATTACHREL        
            if "ATTACH" in rc:            
                out_data = rc.replace("ATTACHREL","PtGPS__ATTACHREL")            
                arcpy.Rename_management(os.path.join(env.workspace,rc), out_data)            
                print (rc)         
                #add underscores between name and rel        
                if "rel" in rc:            
                    out_data = rc.replace("rel","PtGPS__rel")            
                    arcpy.Rename_management(os.path.join(env.workspace,rc), out_data)            
print (rc)
'''

# PATH_FC = "D:/PYTH/Debugging_scripts/SanDiego.gdb"
# desc = arcpy.Describe(PATH_FC)
# desc.name desc.path desc.dataType


# List DataSets

listDS = arcpy.ListDatasets()
for itemDS in listDS:
    abc = arcpy.Describe(itemDS)
    for childRS in abc.children:
        print "\t %s -> %s" % (childRS.dataType, childRS.name)
        print "\t \t %s" % (childRS.backwardPathLabel)
        print "\t \t %s" % (childRS.cardinality)
        print "\t \t %s" % (childRS.classKey)
        print "\t \t %s" % (childRS.destinationClassNames)
        print "\t \t %s" % (childRS.forwardPathLabel)
        print "\t \t %s" % (childRS.isAttributed)
        print "\t \t %s" % (childRS.isComposite)
        print "\t \t %s" % (childRS.isReflexive)
        print "\t \t %s" % (childRS.keyType)
        print "\t \t %s" % (childRS.notification)
        print "\t \t %s" % (childRS.originClassNames)
# List Feature Class

listFC = arcpy.ListFeatureClasses()
for itemFC in listFC:
    print " * Feature Class : " + itemFC
    itemFCDesc = arcpy.Describe(itemFC)
    print "Shape Field Name " + itemFCDesc.shapeFieldName
    print "Feature Type " + itemFCDesc.featureType
    print "Shape type " + itemFCDesc.shapeType
    print "Spatial Index " + str(itemFCDesc.hasSpatialIndex)

    listFieldFC = arcpy.ListFields(itemFC)
    for listField in listFieldFC:
        print "ItemName " + listField.name
        print "ItemType " + listField.type
        print "ItemAlias " + listField.aliasName
        print "ItemDefault %r" %(listField.defaultValue)
        print "ItemDomain " + listField.domain
        print "ItemIsNullable %r" %(listField.isNullable)
        print "ItemLength %i" %(listField.length)

listTB = arcpy.ListTables()
for itemTB in listTB:
    #print(itemTB)
    itemTBDesc = arcpy.Describe(itemTB)
    listFieldTB = arcpy.ListFields(itemTB)
    for fieldTB in listFieldTB:
        print fieldTB.name
