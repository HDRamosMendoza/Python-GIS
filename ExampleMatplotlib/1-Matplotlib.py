#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt

fig = plt.figure(u'Gráfica de barras') # Figure
ax = fig.add_subplot(111) # Axes

nombres = ['Juan','Ana','Pablo','Ximena','Jorge']
datos = [90,88,78,94,93]
xx = range(len(datos))

ax.bar(xx, datos, width=0.8, align='center')
ax.set_xticks(xx)
ax.set_xticklabels(nombres)

plt.show()