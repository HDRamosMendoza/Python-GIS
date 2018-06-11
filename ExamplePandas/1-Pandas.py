#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Fuente
# http://www.pybonacci.org/2015/01/14/introduccion-a-machine-learning-con-python-parte-1/
from pandas import read_csv
# leemos el dataset
iris = read_csv('iris.csv')
# descartamos la familia setosa que ya tenemos clasificada
iris = iris[iris.Name != 'Iris-setosa']
virginica = iris.Name=='Iris-virginica'
# obtenemos un array con los nombres de las características que medimos
features = iris.columns[:4]
# inicializamos en valor de precisión
best_acc = 0.0
for fi in features:                    # Por cada parámetro o característica de la que tenemos valores
    thresh = iris[fi].copy()           # obtenemos una lista de valores para el umbral
    thresh.sort(inplace=True)          # que ordenamos de menor a mayor.
    for t in thresh:                   # Por cada posible valor de umbral
        pred = (iris[fi] > t)       # determinamos los elementos de la tabla que están por encima
        acc = (pred==virginica).mean() # y calculamos que porcentaje de la familia virginica está recogida.
        if acc > best_acc:          # Si mejoramos la detección, actualizamos los parámetro de la colección.
            best_acc = acc             # Mejor precisión obtenida.
            best_fi = fi               # Mejor característica para clasificar las familias.
            best_t = t                 # Valor óptimo de umbral.