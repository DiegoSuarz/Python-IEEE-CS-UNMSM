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
carro1 = Carro("Rojo",60)
print("El color de mi carro1 es: {}".format(carro1.color))


carro2 = Carro("Blanco",65)

#nuevo atributo, solo funciona para carro2, atributo son todas la variables definidas en la clase
carro2.marchas = 1000
print("Las manchas de mi carro2 son: {}".format(carro2.marchas))



