"""
Definir una función que compara números complejos y una clase NumeroComplejo.
Reglas:
- Si dos objetos (números complejos) distintos, tienen sus atributos iguales,
  no se consideran iguales
- Crear método son Iguales
- Crear método imprimir.
- Comprobar los métodos de sus clases con dos números complejos pasando sus valores
 (los valores de un número complejo) por parámetro.
"""
comp = 0
def comparaNumComplejo(num1, num2):

    return NumeroComplejo(num1,num2)

class NumeroComplejo():
    numComp1 = 0 + 0j
    numComp2 = 0 + 0j
    igual = 0

    def __init__(self,num1,num2):
        self.numComp1 = num1
        self.numComp2 = num2
    def Iguales(self):

        if self.numComp1 == self.numComp2:
            self.igual = 1
        else:
            self.igual = 0

    def Imprimir(self):
        if self.igual == 1:
            print("Los numeros complejos son iguales")
        else:
            print("Los numeros complejos son diferentes")

num1 = complex(input("Ingrese el primer número a procesar "))
num2 = complex(input("Ingrese el segundo número a procesar "))

compara = comparaNumComplejo(num1,num2)
compara.Iguales()
compara.Imprimir()






