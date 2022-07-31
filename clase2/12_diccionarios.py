""""Diccionarios son poderasas estructuras de datos
en python, que almacenan pares de claves, siendo esta
representada en la siguiente forma Clave-valor, key-valor

La comprensión de los diccionarios (o dict) puede ser muy útil
en crear nuevos diccionarios basados en diccionarios
existentes e iterables.
"""
""""los nombres de los key se tienen que escribir en minúscula
por convención"""

diccionario = {"nombre": "Phyton", "antiguedad":15}

print("Nuestro diccionario tiene los siguintes datos: {}".format(diccionario))

#Agregando un nuevo key al diccionario
diccionario["tipo"]="Backend"
diccionario["SistemaOperativo"]="WINDOWS, Linux, macOS"
print("Mi diccionario actualizado tiene los siguientes datos: {}".format(diccionario))

#Eliminando un key del diccionario se usa del
del diccionario["antiguedad"]
print("Mi diccionario actualizado contiene: {}".format(diccionario))