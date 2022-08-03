"""Uso del búcle while"""

year = 2011

while year < 2022:   #se seguira repitiendo mientras la sentencia sea verdadera
    print("Informes del año {}".format(year))
    year = year + 1

    if year == 2018:
        print("Llegó al año {}".format(year))
        break # Break fuerza el fin del bucle while o fuerza el término de una condición
