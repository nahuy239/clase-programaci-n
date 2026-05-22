#1)
'''def ordenar_por_nombre(nombres: list, edades: list) -> None:
    n = len(nombres)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if nombres[i] > nombres[j]:
                aux_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux_nombre

                aux_edad = edades[i]
                edades[i] = edades[j]
                edades[j] = aux_edad

nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia",
           "Maria","Pedro","Antonio","Eugenia","Soledad","Mario","Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

ordenar_por_nombre(nombres, edades)

print("Nombres ordenados:")

for i in range(len(nombres)):
    print(nombres[i], edades[i])'''

#2)
'''def ordenar_materias(nombres: list, puntos: list) -> None:

    n = len(nombres)
    for i in range(n - 1):

        for j in range(i + 1, n):
            if nombres[i] > nombres[j]:

                aux_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux_nombre

                aux_puntos = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux_puntos
            elif nombres[i] == nombres[j] and puntos[i] < puntos[j]:

                aux_nombre = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux_nombre

                aux_puntos = puntos[i]
                puntos[i] = puntos[j]
                puntos[j] = aux_puntos


nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura",
           "Ciencias Sociales","Computacion","Ingles","Algebra",
           "Contabilidad","Artistica","Algoritmos","Base de Datos",
           "Ergonomia","Naturaleza"]
puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

ordenar_materias(nombres, puntos)

for i in range(len(nombres)):
    print(nombres[i], puntos[i])
'''
#3)
def ordenar_estudiantes(estudiantes: list, apellidos: list, notas: list) -> None:

    n = len(estudiantes)

    for i in range(n - 1):

        for j in range(i + 1, n):
            if apellidos[i] > apellidos[j]:

                aux = apellidos[i]
                apellidos[i] = apellidos[j]
                apellidos[j] = aux

                aux = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux

                aux = notas[i]
                notas[i] = notas[j]
                notas[j] = aux


            elif apellidos[i] == apellidos[j] and estudiantes[i] > estudiantes[j]:

                aux = apellidos[i]
                apellidos[i] = apellidos[j]
                apellidos[j] = aux

                aux = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux

                aux = notas[i]
                notas[i] = notas[j]
                notas[j] = aux

            elif apellidos[i] == apellidos[j] and estudiantes[i] == estudiantes[j] and notas[i] < notas[j]:

                aux = apellidos[i]
                apellidos[i] = apellidos[j]
                apellidos[j] = aux

                aux = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux

                aux = notas[i]
                notas[i] = notas[j]
                notas[j] = aux

estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María",
               "Sofia","Maria","Pedro","Antonio","Eugenia","Soledad",
               "Mario","María"]
apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez",
             "Perez","Lopez","Arregui","Mitre","Andrade","Loza",
             "Antares","Roca","Perez"]

nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

ordenar_estudiantes(estudiantes, apellidos, nota)

for i in range(len(estudiantes)):
    print(estudiantes[i], apellidos[i], nota[i])