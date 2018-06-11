#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import base

variableDefecto = base.Muestra(codigoEspectro='HolaMundo', sr=14)
print(variableDefecto.getSpatialReference)

print("Getter de codigoEspectro")

# Muestra el atributo de codigoEspectro.
print(variableDefecto.getCodigoEspectro)

fision1, fision2 = variableDefecto.fision()
print(fision1.getCodigoEspectro)
print(fision2.getCodigoEspectro)

#type()
print("type")
obj1, obj2 = variableDefecto.objetoDeLaMismaClase()
print(obj1.getCodigoEspectro)
print(obj2.getCodigoEspectro)

estatico = base.MuestraFirmaEspectral.suma(5,6)
print("Imprimiendo la función estática: {0}".format(estatico))

# Hard-coding
tipo1, tipo2 = variableDefecto.spatialReferenceType()
print("- - - - - - - - - - - - - - -")
print(tipo1)
print(tipo2)

# Hard-coding + Herencia
#base.MuestraFirmaEspectral()

"""
-  De clase biene y de que tipo.
mascota.__class__
type(mascota)
"""

''' Usando Getter y Setter '''
print "**************"
print "Obtener y Cambiar. Atributos"

objPer = base.Persona(documentoIdentidad=76598543, nombres='Willy', apellidos='Urbina Salinas')

print "Nombre: ", objPer.personaNombres

objPer.personApellidos = "Ramos Mendoza"

print "Apellidos actualizados: ", objPer.personApellidos

print "Etiqueta: ", base.Persona.personaDNI.__doc__

print "-------------"
lblDni = base.Persona.personaDNI.__doc__
print "{0}: {1}".format(lblDni, objPer.personaDNI)

print "%s : %d" %(lblDni, objPer.personaDNI)
