lista = []
dicc = {}
def diccionario():

    nombre = input("Ingrese su nombre: ")
    dicc["Nombre"] = nombre
    apellidos = input("Ingrese su apellido: ")
    dicc["apellidos"] = apellidos

    edad = int(input("Ingrese su edad: "))
    dicc["edad"] = edad

    dni = int(input("Ingrese su dni: "))
    dicc["dni"] = dni

    lista = list(dicc)

    dicc["Profesion"] = "Electronica"

    return dicc

print("Los datos del usuario son los siguientes:",diccionario())

print("{}".format(lista))

dicc["Profesion"] = "Electronica"
print("{}".format(dicc))

del dicc["dni"]
print("{}".format(dicc))