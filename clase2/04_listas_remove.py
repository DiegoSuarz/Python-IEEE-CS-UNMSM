"""Estructura de datos"""

"""list.remove(x) -> Permite quitar un valor de la lista con el nombre del elemento
    x -> nombre del elemento a eliminar
"""

lista = ["Python", "Javascript", "Postgresql", "SCRUM"]
print("Mi lista contiene: {}".format(lista))

lista.remove("Postgresql") #eliminando el valor de nombre Postgresql

print("Mi lista actualizada contiene: {}".format(lista))