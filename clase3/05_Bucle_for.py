"""Uso del for"""

ingenierias = ["Software", "Sistemas", "Industrial", "Mecánica"]  #lista
i = 0

nombre = input("Ingrese su primer nombre: ")

print("El tamaño de nuestra lista es: {}, programa creado por: {}".format(len(ingenierias), nombre))

for ingenieria in ingenierias:

    print("Ingeniería: {}".format(ingenieria))
    i = i + 1
    print("Esta es la vuelta número: {}".format(i))

print("Llegó al final de nuestro for")
