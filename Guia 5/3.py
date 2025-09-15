lista=[11,5,8,22]
minimo=lista[0]
for i in range (0,len(lista)):
    if minimo>lista[i]:
        Ubicacion= i
        minimo=lista[i]
print ("El numero es",minimo)
print ("El numero es", Ubicacion)
