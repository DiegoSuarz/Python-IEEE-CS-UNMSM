"""Programación orientada a Objetos"""

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
        velocidad = self.velociadad + self.aceleracion
        if velocidad < 0:
            velocidad = 0

        self.velociadad = velocidad

"instancias:"
"""Instancia de nuestra clase Carro"""
carro1 = Carro("Negro",60)
print("El color de mi carro 1 es: {}".format(carro1.color))
print("La aceleración de carro 1 es: {}".format(carro1.aceleracion))
print("La velocidad inicial de mi carro 1 es: {}".format(carro1.velociadad))
print("La cantidad de ruedas de mi carro 1 es: {}".format(carro1.ruedas))

carro2 = Carro("Blanco",30)
print("El color de mi carro 2 es: {}".format(carro2.color))
print("La aceleración de carro 2 es: {}".format(carro2.aceleracion))

carro3 = Carro("Azul",78)
print("El color de mi carro 3 es: {}".format(carro3.color))
print("La aceleración de carro 3 es: {}".format(carro3.aceleracion))