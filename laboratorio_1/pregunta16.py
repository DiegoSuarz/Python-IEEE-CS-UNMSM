"""16. Crear una función valide un número de DNI, retorne True si el número es válido y False si no
lo es. Para que un número de DNI sea válido debe tener entre 8 dígitos."""



num = int(input("Ingrese el numero de DNI "))

def DNI(dni):
    cont = 0
    while(dni>0):
        dni//=10
        cont+=1
    print(cont)
    if cont == 8:
        return True
    else:
        return False

print("El numero de DNI es: {}".format(DNI(num)))
