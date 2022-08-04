"""
2. En un programa solicitar a un usuario que ingrese números has que
ingrese el 0

Reglas:
    - Terminar el programa cuando se ingresa el valor 0.
    - Mostrar la suma de los digitos.
    - Crear una función que realice la suma de sus digitos y retorne la suma solicitada.
"""
def sumaDigitos(numero):
    suma = 0
    while numero != 0:  #si el numero es diferente de 0
        digito = numero % 10
        print(digito)
        suma = suma + digito
        numero = numero//10

    return suma

num = int(input("Ingrese número a procesar "))

while num != 0:
    print(sumaDigitos(num))
    num = int(input("Ingrese otro número nuevo a procesar: "))