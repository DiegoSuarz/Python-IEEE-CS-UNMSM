"""9. Convierte tu diccionario creado a una lista, mostrar el tipo de dato."""

datos = {"nombre" : "Diego", "edad" : 30, "DNI": 47408434 }

print("Mi diccionario contiene: {}".format(datos))

dictToList = list(datos)
print("Mi lista contiene: {}".format(dictToList))

for item in dictToList:
    print("{} es del tipo: {}".format(item,type(item)))