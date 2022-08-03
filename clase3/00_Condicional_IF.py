"""Estructuras condicionales"""

#capturar valores por consola:

var = input("Ingrese un valor entero: ") #el input siempre es un tipo string

"""
Para convertir string a entero
    A entero: int(var1)
    A flotante: float(var1)
"""
var1 = int(input("Indique el primer valor: "))
var2 = int(input("Indique el seguendo valor: "))

print(var1)
print(type(var1))  #verificamos el tipo de variable entero, string, flotante, etc

print(var2)
print(type(var2))

if var1 > var2: #El if se activa cuando la sentencia es verdadero
    print("El valor 1 es mayor que el valor 2")
    suma = var1 + var2
    print(suma)
else:

    resta = var1 - var2
    print(resta)
    print("El valor 2 es mayor que el valor 1")