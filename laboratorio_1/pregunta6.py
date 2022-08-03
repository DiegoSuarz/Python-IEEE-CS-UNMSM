"""6. Almacenar en una lista los números del 1 al 10 (de forma desordenada) y los muestre por
pantalla en orden inverso separados por comas."""

list = [4,6,3,1,7,8,2,9,5]

list.sort()
print("Mi lista contiene: {}".format(list))

list.reverse()
print("Mi lista actualizada contiene: {}".format(list))

for item in list:
    print("{} ,".format(item))
