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

class CarroSedan:
    #altura = 1.5

    def __init__(self):
        super(CarroSedan,self).__init__()
        self.altura = 1.5

class CarroVolador(Carro, CarroSedan): #hereda los atributos de la clase Carro y la clase CarroSedan
    ruedas = 6

    def __init__(self, color, aceleracion, estado_volando = False):
        super().__init__(color,aceleracion)         #clase padre
        Carro.__init__(self, color, aceleracion)    #clase padre
        CarroSedan.__init__(self)

        self.estado_vol = estado_volando

    def vuela(self):
        self.estado_vol = True

    def aterriza(self):
        self.estado_vol = False

carroVol = CarroVolador("Blanco",60)

print("El colo de mi carro es: {}".format(carroVol.color))
print("La velocidad de mi carro es: {}".format(carroVol.color))
print("La altura de mi carro es: {}".format(carroVol.altura))

