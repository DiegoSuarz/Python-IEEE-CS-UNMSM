"""3. Crear una lista con los 10 primeros números al cuadrado y mostrar el resultado."""

lista = []

for item in range(10):  #repite 15 veces
    item *= item
    lista.append(item)

print("La lista actualizada es: {}".format(lista))