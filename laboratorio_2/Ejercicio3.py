"""
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
 CuantaJoven que deriva de la anterior.
 Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar
 una bonificación que estará expresada en tanto por ciento.Construye
 los siguientes métodos para la clase:
Reglas:
• Un constructor.
• En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de
  edad., por lo tanto hay que crear un método esTitularValido() que devuelve
  verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso
  contrario.
• Además la retirada de dinero sólo se podrá hacer si el titular es válido.
• El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación
  de la cuenta.
• Piensa los métodos heredados de la clase madre que hay que reescribir.
"""
valido = False
boni = 0.0

class Cuenta:
    titular = ""
    cantidad = 0.0

    def __init__(self, titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print("Cuenta Joven")
        print("El titular es: {}".format(self.titular))
        print("La cantidad de dinero es: {}".format(self.cantidad))
        print("La bonificacion es: {}".format(self.cantidad * boni))

    def ingresar(self, cantidad):

        if cantidad > 0:
            self.cantidad += cantidad

        else:
            self.cantidad = self.cantidad

    def retirar(self, cantidad):
        if valido == True:
            self.cantidad -= cantidad

class CuentaJoven(Cuenta):
     def __init__(self, titular, cantidad, bonificacion, edad):
        global boni
        super().__init__(titular,cantidad)
        Cuenta.__init__(self,titular,cantidad)
        self.bonificacion = bonificacion
        self.edad = edad
        boni = self.bonificacion
     def TitularValido(self):
         global valido
         if self.edad >= 25:
             valido = True
         else:
             valido = False


persoan1 = CuentaJoven("Diego",400,0.1,25)
persoan1.TitularValido()
persoan1.retirar(100)
persoan1.mostrar()