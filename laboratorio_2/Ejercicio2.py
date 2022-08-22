"""
Crear una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Construye los siguientes métodos para la clase.
Reglas:
• Un constructor, donde los datos pueden estar vacíos.
• mostrar(): Muestra los datos de la cuenta.
• ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
• retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
números rojos.
"""

class Cuenta:
    titular = ""
    cantidad = 0.0

    def __init__(self, titular):
        self.titular = titular
        self.cantidad = 0.0

    def mostrar(self):
        print("El titular es: {}".format(self.titular))
        print("La cantidad de dinero es: {}".format(self.cantidad))

    def ingresar(self, cantidad):

        if cantidad > 0:
            self.cantidad += cantidad

        else:
            self.cantidad = self.cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad

datos1 = Cuenta("Diego")



datos1.ingresar(300)
datos1.mostrar()

datos1.retirar(500)
datos1.mostrar()