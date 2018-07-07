#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
'''
	collections.namedtuple()
	Lo que namedtuple(), una Factory Function, nos devuelve,
	es una nueva clase que hereda de tuple pero que tambien
	permite acceso a los atributos por nombre.

	Nada más y nada menos -- pero al ser una subclase significa que
	todos  los métodos mágicos  que necesitábamos ya están implementados.
'''
# Para ver todos sus funciones help(collections)

Punto = collections.namedtuple("Punto","x y z")
p = Punto(3,1,5)
print 'x',p.x
print 'y',p.y
print 'z',p.z
print "Tamano",len(p)
p2 = Punto(3,1,5)
print p == p2 

