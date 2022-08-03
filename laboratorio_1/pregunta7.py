"""7. Escribir un programa que pregunte por 5 números, los almacene en una lista (append) y
muestre por pantalla su media."""

list = []
suma = 0

for item in range(5):
    num = int(input("{} ingrese el numero: ".format(item+1)))
    list.append(num)
    suma += num

media = suma/(item + 1)
print("Mi lista contiene: {}".format(list))
print("la media es: {}".format(media))