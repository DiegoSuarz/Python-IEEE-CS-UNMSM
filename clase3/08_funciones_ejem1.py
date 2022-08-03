"""Programación funcional en Python"""

def restar(a, b, c=100):
    resultado = a - b + c
    return resultado


print("El resultado de mi función es: {}".format(restar(50, 200, 80)))
