"""Estructura de datos"""

"""list.count(x) -> Devuelve la cantidad de veces que se repite
el valor "x" en un lista.
"""

lista = ["Python","php", "MongoDB", "Kamban"]
print("Mi lista contiene: {}".format(lista))

lista.append("Python")
lista.append("Python")
lista.append("Python")
lista.append("php")

print("Mi lista actualizada contiene: ".format(lista))

#lista.count("Python") #cuenta la cantidad de veces que se repite el valor "Python"
#lista.count("php")

print("La cantidad de vaces que se repite {} es: {}".format(lista[0],lista.count("Python")))
print("La cantidad de vaces que se repite {} es: {}".format(lista[1],lista.count("php")))
