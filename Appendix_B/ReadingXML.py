from xml .dom import minidom

'''
Estrcutura de ejemplo para recorrer un xml.
Se debe de tratar como si se estuviera llamando al DOM de una web.
<fires>
	<fire address="2356" />
	<fire address="2356" />
	<fire address="2356" />
	<fire address="2356" />
	<fire address="2356" />
</fires>
'''

# Se parsea el XML
xmldoc = minidom.parse("puntos_criticos.xml")

# Genera la lista de nodos de el XML
childNodes = xmldoc.childNodes

# Genera la lista de todos los nodos de <fires>
eList = childNodes[0].getElementsByTagName("fire")

# Lista todos los elementos. Si existe la propiedad de "address"
for e in eList
	if e.hasAttribute("address"):
		print e.getAttribute("address")
