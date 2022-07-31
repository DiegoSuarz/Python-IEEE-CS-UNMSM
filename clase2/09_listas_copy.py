"""Estructura de datos"""

"""list.copy() ->Realiza una copia de la lista"""

var1 = ["sqlServer", "rDS", "nysql", "postgresql"]

var2 = var1.copy() #realiza una copia de la lista var1 y almacenarla en var2

var2.append("sqlite2") #agregar el elmento al final de la lista
var2.remove("rDS") #quitar el elemento "rDS"

print("Mi lista 1 contiene: {}".format(var1))
print("Mi lista 2 contiene: {}".format(var2))