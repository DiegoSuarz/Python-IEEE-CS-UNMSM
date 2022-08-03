"""2. Elimina un elemento por un índice existente y ya no por el valor."""

"""1. Crear una lista vacía y luego agregar elemento con diferentes cursos que llevas en tu pregrado
(utilizando append)"""

listaVacia = []

print("Mi lista contiene: {}".format(listaVacia))

listaVacia.append("Calculo 1")
listaVacia.append("Microcontroladores")
listaVacia.append("Ciencia de datos")
listaVacia.append("Fisica III")

print("Mi lista actualizada contiene: {}".format(listaVacia))

listaVacia.pop(2) #eliminar el elemento de indice 2 ("ciencia de datos")

print("Mi lista actuazlida contiene: {}".format(listaVacia))