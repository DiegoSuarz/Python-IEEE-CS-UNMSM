"""Estructura de datos"""

"""List.insert(i,x) -> Permite insertar en elemento "x" en la posicion "i
  i: posición
  x: valor
"""

lista = [50, 90, 500, 390, 3000]
print("Mi lista contiene: {}".format(lista))

lista.insert(0, "Hola pythonistas!!!") #insertar string en la posición 0
lista.insert(3, 180.90) #insertar flotante en la posición 3

print("Mi lista actualizada contiene: {}".format(lista))

#no es posible imprimir una lista fuera del rango
#print(lista[10] #error