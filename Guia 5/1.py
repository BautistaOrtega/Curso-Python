lista=[11,5,8,22]
maximo=lista[0]
for i in range (0,len(lista)):
    if maximo<lista[i]:
        maximo=lista[i]
print (f"el numero es {maximo}")
print ("el numero es",maximo)
