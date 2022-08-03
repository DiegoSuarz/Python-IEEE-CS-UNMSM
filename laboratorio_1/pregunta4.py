"""
4. Crear una lista con los 15 primeros números impares (usando for), luego agregar 3 números
repetidos (los cuales son impares dentro del rango indicado y que no sea el último impar).
- Empezando desde 1 y no 0, para la generación de estos números.
- Agregar una cadena de caracteres en la posición 3 de la lista.
- Eliminar este valor string de la cadena usando del.
- Resultado final: la impresión de la cadena en consola.
"""

lista = []

for impares in range(1,16):  #repite 15 veces
    impares = 2*impares - 1
    lista.append(impares)
print("La lista actualizada es: {}".format(lista))

lista.insert(2, "Cadena de caracteres") #insertar string en la posición 0
print("La lista actualizada es: {}".format(lista))

del lista[2]
print("La lista actualizada es: {}".format(lista))
