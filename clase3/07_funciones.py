
"""Programación funcional en Python"""

var1 = int(input("Ingrese un valor"))
var2 = int(input("Ingrese un segundo valor"))

"""Input: dos variables como parámetro"""

def multiplicar(a, b):
    resultado = a*b
    return resultado

"""Output: Lo que retorna la función"""

print("El valor de mi función es: {}".format(multiplicar(var1, var2)))
