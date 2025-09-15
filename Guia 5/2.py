from xml.dom import minicompat


lista=[11,5,8,22]
minimo=lista[0]
for i in range (0,len(lista)):
    if minimo>lista[i]:
        minimo=lista[i]
print ("el numero es",minimo)
