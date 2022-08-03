"""14. Crear un diccionario con 6 nombres de cursos que llevas o llevaste en el pregrado.
- Borrar cualquier curso (uno) usando la palabra reservada del.
- Comprobar que un curso esté dentro del diccionario.
- Ingresar el nombre de tu carrera dentro de los valores que tienes en tu diccionario y tu apellido.
- Mostrar en consola los valores de su variable final (ya sea diccionario o lista)."""

cursos = {"cuso1":"Fisica","curso2":"Quimica I","curso3":"Quimica II","curso4":"Algebra","curso5":"Cálculo I","curso6":"Cálculo II"}

print("Mi diccionario contiene: {}".format(cursos))

del cursos["curso3"]

print("Mi diccionario actualizado contiene: {}".format(cursos))

print ( "Fisica1" in cursos.values())
cursos["Carrera"]="Electrónica"
cursos["Apellido"]="Suárez"

print("Mi diccionario actualizado contiene: {}".format(cursos))