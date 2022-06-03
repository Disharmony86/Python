nombres = ["juan", "Ñaña", "Trutru", "Pipo"]
#Imprimir Lista de nombres
print(nombres)
#Acceder a los elementos de una lista:
print(nombres[3])
print(nombres[0])
print(nombres[2])
print(nombres[-1])
print(nombres[1:3])
print(nombres[:3])
print(nombres[1:])
 #Iterar una lista
for nombre in nombres:
     print(nombre)
else:
    print("no existen mas nombres en la lista")

print(len(nombres))
nombres.append("Loca")
print(nombres)
nombres.insert(1, "chiquilin")
print(nombres)
nombres.remove("juan")
print(nombres)
nombres.pop()
print(nombres)
del nombres[0]
print(nombres)
nombres.clear()
print(nombres)
#Borrar lista
del nombres
print("Borrado exitosamente")