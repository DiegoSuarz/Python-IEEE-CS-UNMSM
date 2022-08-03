"""5. Ingresar los números ganadores de la lotería (mediante consola) y almacenarlos en una lista,
finalmente mostrar estos números por consola (imprimir la lista)."""

list = []

for item in range(7):
    numeros = int(input("{} Indique el numero ganador: ".format(item+1)))
    list.append(numeros)

print("los numeros ganadores son: {}".format(list))