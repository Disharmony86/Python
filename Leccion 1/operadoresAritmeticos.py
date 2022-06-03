operando1 = 10
operando2 = 5

suma = operando1 + operando2
print("suma: ", suma)
multiplicacion = operando1 * operando2
print("multiplicacion: ", multiplicacion)
division = operando1 / operando2
divisionInt = operando1 // operando2
print("Division (Float): ", division)
print("Division (Int): ", divisionInt)
resta = operando1 - operando2
print("Resta: ", resta)
modulo = operando1 % operando2
print("Modulo: ", modulo)
exponente = operando1 ** operando2
print("Exponente: ", exponente)

# Hallar el area y el perimetro de un rectangulo
print("-------------------------------------------------------------------------")

# Primero solicitamos al usuario el ancho y el alto:

alto = int(input("Ingresa el alto del rectangulo: "))
ancho = int(input("Ingresa el ancho del rectangulo: "))

# ahora multiplicamos el alto por el ancho y enviamos a consola.

area = alto * ancho
print("El area del rectangulo es: ", area)

# ahora para mostrar el perimetro, dividimos al alto pot el ancho y luego multiplicamos por 2.

perimetro = (alto + ancho) * 2
print("EL perimetro del rectangulo es: ", perimetro)
