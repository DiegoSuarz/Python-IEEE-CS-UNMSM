"""Uso del búcle while"""

numero = int(input("Ingrese un número menor a 10: "))

while numero < 10:
    print(numero)
    numero = numero + 1  #Se aumenta en uno el valor de la variable en cada vuelta

print("Llegó al final del búcle while")
