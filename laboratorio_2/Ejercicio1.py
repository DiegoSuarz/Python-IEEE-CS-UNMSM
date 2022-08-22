"""
Clases:
1. Crear una clase Persona, con los atributos nombre, edad y DNI. Construyendo los
siguientes métodos para la clase:
• Constructor donde los datos pueden estar vacíos.
• mostrar() : Muestra los datos de la persona.
• validarDni(): Validad que tenga 9 dígitos y que no contenga caracteres.
• esMayorDeEdad() : Devuelve una respuesta indicando si la persona es mayor de
edad
"""
class Persona:

    nombre = ""
    edad = 0
    DNI = 0

    def __init__(self,nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def MostrarDatos(self):
        print("El nombre del usuario es: {}".format(self.nombre))
        print("La edad del usuario es: {}".format(self.edad))
        print("El dni del usuario es: {}".format(self.dni))

    def ValidarDni(self):
        cont = 0
        while (self.dni > 0):
            self.dni //= 10
            cont += 1
        if cont == 8:
            print("El dni es valido")
        else:
            print("El dni es inválido")

    def esMayorDeEdad(self):
        if self.edad > 18:
            print("El usuario es mayor de edad")
        else:
            print("El usuario es menor de edad")

persona1 = Persona("Diego",17,47708445)

persona1.MostrarDatos()

persona1.ValidarDni()

persona1.esMayorDeEdad()