"""11. Elimina el key edad de tu diccionario, incluyendo su valor.
del var[‘key’]"""

datos = {"nombre" : "Diego", "edad" : 30, "DNI": 47408434 }

del datos["edad"]

print("Mi lista actualizada contiene: {}".format(datos))