from re import I
from tkinter import *
from unittest import result

ventana = Tk()
ventana.title("Calculaldora By Alfredo Revollo")

# Input
entradaTexto = Entry(ventana, font=("Calibri 20"))
entradaTexto.grid(row=0, column=0, columnspan=4, padx=50, pady=5)

#Funciones
i = 0

#Insertar valor en Textbox

def clickButton(valor):
    global i
    entradaTexto.insert(i, valor)
    i += 1

#Borrar o Reset de Textbox
def borrar():
    entradaTexto.delete(0, END)
    i=0

#Resultado al oprimir =
def operacion():
    ecuacion = entradaTexto.get()
    resultado =eval(ecuacion)
    entradaTexto.delete(0, END)
    entradaTexto.insert(0, resultado)
    i=0


# Buttons

boton1 = Button(ventana, text="1", width=5, height=2, command= lambda: clickButton(1))
boton2 = Button(ventana, text="2", width=5, height=2, command= lambda: clickButton(2))
boton3 = Button(ventana, text="3", width=5, height=2, command= lambda: clickButton(3))
boton4 = Button(ventana, text="4", width=5, height=2, command= lambda: clickButton(4))
boton5 = Button(ventana, text="5", width=5, height=2, command= lambda: clickButton(5))
boton6 = Button(ventana, text="6", width=5, height=2, command= lambda: clickButton(6))
boton7 = Button(ventana, text="7", width=5, height=2, command= lambda: clickButton(7))
boton8 = Button(ventana, text="8", width=5, height=2, command= lambda: clickButton(8))
boton9 = Button(ventana, text="9", width=5, height=2, command= lambda: clickButton(9))
boton0 = Button(ventana, text="0", width=19, height=2, command= lambda: clickButton(0))

botonBorrar = Button(ventana, text="AC", width=5, height=2, command= lambda: borrar())
botonParentesis1 = Button(ventana, text="(", width=5, height=2, command= lambda: clickButton("("))
botonParentesis2 = Button(ventana, text=")", width=5, height=2, command= lambda: clickButton(")"))
botonPunto = Button(ventana, text=".", width=5, height=2, command= lambda: clickButton("."))

botonDivision = Button(ventana, text="/", width=5, height=2, command= lambda: clickButton("/"))
botonMultiplicacion = Button(ventana, text="*", width=5, height=2, command= lambda: clickButton("*"))
botonSuma = Button(ventana, text="+", width=5, height=2, command= lambda: clickButton("+"))
botonIgual = Button(ventana, text="=", width=5, height=2, command= lambda: operacion())
botonResta = Button(ventana, text="-", width=5, height=2, command= lambda: clickButton("-"))

#Show buttons on main

#Primera Fila (De Izquierda a Derecha):

botonBorrar.grid(row= 1, column= 0, padx=5 , pady=5 )
botonParentesis1.grid(row= 1, column= 1, padx=5 , pady=5 )
botonParentesis2.grid(row= 1, column= 2, padx=5 , pady=5 )
botonDivision.grid(row= 1, column= 3, padx=5 , pady=5 )

#Segunda Fila:

boton7.grid(row= 2, column= 0, padx=5 , pady=5 )
boton8.grid(row= 2, column= 1, padx=5 , pady=5 )
boton9.grid(row= 2, column= 2, padx=5 , pady=5 )
botonMultiplicacion.grid(row= 2, column= 3, padx=5 , pady=5 )

#Tercera fila:

boton4.grid(row= 3, column= 0, padx=5 , pady=5 )
boton5.grid(row= 3, column= 1, padx=5 , pady=5 )
boton6.grid(row= 3, column= 2, padx=5 , pady=5 )
botonSuma.grid(row= 3, column= 3, padx=5 , pady=5 )

#Cuarta fila

boton1.grid(row= 4, column= 0, padx=5 , pady=5 )
boton2.grid(row= 4, column= 1, padx=5 , pady=5 )
boton3.grid(row= 4, column= 2, padx=5 , pady=5 )
botonResta.grid(row= 4, column= 3, padx=5 , pady=5 )

#Quinta fila

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady= 5 )
botonPunto.grid(row=5, column=2, padx=5, pady= 5 )
botonIgual.grid(row=5, column=3, padx=5, pady= 5 )



ventana = mainloop()
