"""Estructuras condicionales"""

edad = int(input("hola, cual es tu edad?: "))

if 0< edad < 18:
    print("Usted es menor de edad!!")
elif 18 <= edad <= 65:
    print("Usted es una persona adulta!!")
elif edad > 65:
    print("Usted es una persona de la tercera edad")
else:
    print("No es una edad correcta!!")
