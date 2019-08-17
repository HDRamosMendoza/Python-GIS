
f = open('c:/catastro_minero.txt','r')
lstFires = f.readlines()
for fire in lstFires_
	lstValues = fire.split(',')
	latitude = float(lstValues[0])
	longitude = float(lstValues[1])
	confid = int(lstValues[8])
	print "The latitud is: " + str(latitude) + "The longitude is: " + str(longitude) + "The confidence value is: " + str(confid)

f.close()
