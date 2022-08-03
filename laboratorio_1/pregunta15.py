"""15. Pedir al usuario en un programa que ingrese un número entero e informar si este primo o
no (es primo cuando se puede de manera exacta entre el mismo y 1), crear una función que
decida si este número es primo o no (imprimir por consola un mensaje al usuario indicándoselo)."""


numero = int(input("Ingrese un numero: "))

def num_esPrimo(a):
    if(a>1):
        cont = 0
        for item in range(2,a):
            resto = a % item
            if resto == 0:
                cont+=1

        if cont == 0:
            return " es primmo"
        else:
            return "no es primo"

    else:
        return "no es primmo"


print("El numero {}".format(num_esPrimo(numero)))
