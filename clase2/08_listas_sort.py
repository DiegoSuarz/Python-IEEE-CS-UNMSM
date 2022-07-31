"""Estructura de datos"""

"""list.sort() -> Permite ordenar los elementos de una lista 
    para numeros de menor a mayor tambien ordena los flotantes
    para string primero mayusculas y odena alfabeticamente

"""

lista1 = ["sqlServer", "RDS", "mysql", "postgresql","rDS"]

print("Mi lista es: {}".format(lista1))
lista1.sort()
print("Mi lista actualizada es: {}".format(lista1))

lista2 = [60,2,1000, 50.6, 150, 10.2]
print("Mi lista2 contiene: {}".format(lista2))
lista2.sort()
print("Mi lista2 actualizada contiene: {}".format(lista2))