"""Estructura de datos"""

"""del list -> permiete eliminar un elmento o la lista completamente una lista"""

lista = []

lista.append(2023)
lista.append("Julio")
lista.append("Pytho para ciencia de datos")

print("Mi lista contiene: {}".format(lista))

del lista[1] #eliminar elemento de la posicion 2
print("Mi lista actualizada contiene: {}".format(lista))

"""Nota: no es posible eliminar un elemento fuera del rango"""
#del lista[15]

