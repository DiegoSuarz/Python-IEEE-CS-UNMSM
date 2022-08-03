"""Diccionario en Python"""

"""Convertir un diccionario en una lista"""

persona = {"nombre": "Fernanda", "apellido": "Guitierrez","edad":27, "dni":47708434}

"""Convertiendo el diccionario a una lista"""

dictToList = list(persona)

print("El diccionario convertido a una lista es el siguiente: {}".format(dictToList))

"""Obteniendo los valore del diccionario a una lista"""

valuesDict = list(persona.values())
print("Los valores del diccionario convertido a una lista es el siguiente: {}".format(valuesDict))
