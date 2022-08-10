"""Programación orientada a Objetos"""
"""Herencia"""

class Carro:
    """Atributos"""
    ruedas = 4

    """Constructor: Valores que va a tener por defecto mi clase cuando se le instancie en un variable"""
    def __init__(self, color, aceleracion):
        self.color =color
        self.aceleracion = aceleracion
        self.velociadad = 0

    """Métodos: son las funciones de la clase"""

    def acelera(self):
        self.velociadad = self.velociadad + self.aceleracion

    def frena(self):
        velocidad = self.velociadad - self.aceleracion
        if velocidad < 0:
            velocidad = 0

        self.velociadad = velocidad

class CarroVolador(Carro):
    ruedas = 6

    def __init__(self, color, aceleracion, estado_volando = False):
        super().__init__(color,aceleracion)
        self.estado_vol = estado_volando

    def vuela(self):
        self.estado_vol = True

    def aterriza(self):
        self.estado_vol = False

carro1 = Carro("Rojo",35)
carroVolador = CarroVolador("Blanco", 45)

print("Color de mi carro volador es:{}".format(carroVolador.color))
print("Estado de carro volador es: {}".format(carroVolador.estado_vol))

carroVolador.acelera()
carroVolador.acelera()
carroVolador.acelera()

print("La velocidad actual de mi carro volador es: {}".format(carroVolador.velociadad))

#print("El carro1 tiene un estod volando es: {}".format(carro1.estado_vol))
#Esto no es posible que ocurra ya que es un atributo de la clase hija y la herencia no es viceversa, es en un solo sentido

