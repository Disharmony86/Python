edad = int(input("Introduce tu edad: "))

veintes = edad >= 20 and edad < 30
print(veintes)
treintas = edad >= 30 and edad < 40
print(treintas)

if veintes or treintas:
    # print("Estas en los 20's o 30's")
    if veintes:
        print("Estas en los 20's")
    elif treintas:
        print("estas en los 30's")
else:
    print("Fuera de Rango de edad")