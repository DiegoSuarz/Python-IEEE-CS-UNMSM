"""12. Verifica el valor de valor en tu diccionario convertido en lista.
valor in var"""

datos = {"nombre" : "Diego", "edad" : 30, "DNI": 47408434 }

dictToList = list(datos)

"""Extraer las llaves para poder verificarlas"""
print(dictToList)
print(sorted(dictToList))