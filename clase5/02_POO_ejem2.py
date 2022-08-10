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

carro1 = Carro("Azul",20)
print("La velocidad inicial de carro1 es: {}".format(carro1.color))

carro1.acelera()
print("La velocidad actual de mi carro1 es: {}".format(carro1.velociadad))

#Herencia puedeo llamar a intanciar y el valor anterior se mantiene
carro1.acelera()
carro1.acelera()
print("La velocidad actualizada de carro1 es: {}".format(carro1.velociadad))

carro1.frena()
print("La velocidad actual de carro1 es: {}".format(carro1.velociadad))

carro1.frena()
carro1.frena()
print("La velocidad actual de carro1 es: {}".format(carro1.velociadad))