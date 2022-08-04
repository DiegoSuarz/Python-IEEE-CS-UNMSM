
tam = int(input("Ingrese el tamaño de la lista: "))
lista = []
listaCubos = []
listaCuadrados = []
sumaLista = []
for i in range(tam):
    num=int(input("Ingrese un número: "))
    lista.append(num)
    listaCubos.append(num*num*num)
    listaCuadrados.append(num*num)
    sumaLista.append(num*num*num+num*num)

print("Mi lista contiene: {}".format(lista))

print("Mi lista al cubo contiene: {}".format(listaCubos))

print("Mi lista al cuadrado contiene: {}".format(listaCuadrados))

print("suma de listas inversa: {}".format(sumaLista))
sumaLista.reverse()
print("suma de listas inversa: {}".format(sumaLista))