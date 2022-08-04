"""
1. Pedir al usuario un correo electrónico por consola.

Reglas:
- Crear una función que valide si es un corro electrónico, si
contiene un "@".
- Retornar un mensaje si es un correo valido en caso contrario mostrar otro
mensaje índicado, que el correo electrónico ingresado no es válido
"""

def validarCorreo(email):

    caracterValido = '@'
    mensaje = ""
    for caracter in email:
        if caracter == caracterValido:
            #print("Es un emal válido")
            mensaje = "Es un email válido"
            break #rompe el bucle for cuando se encuentra el "@"
        else:
            mensaje = "No es un email válido"
            #print("No es un email válido")

    return mensaje

correo = input("Ingrese sus correo electrónico: ")

#print("{}".format(validarCorreo(correo)))
print(validarCorreo(correo))