from funciones import *
from listas_personas import *

listas_cargadas=False

while True:

    print("""
            1-Importar listas
            2-Listar los datos de los usuarios de México
            3-Listar los nombre, mail y teléfono de los usuarios de Brasil
            4-Listar los datos del/los usuario/s más joven/es
            5-Obtener un promedio de edad de los usuarios
            6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
            7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
            8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.
            9-México ordenado por nombre
            10-Más jóvenes ordenados
            11-México y Brasil CP > 8000 ordenado
            12-Salir
""")

    opcion=int(input("\nOpcion: "))

    if opcion == 1:
        listas_cargadas=True
        print("Listas cargadas")
    elif opcion == 2:
        if listas_cargadas:
            listar_mexico(nombres,paises,edades)
        else:
            print("Primero importar")
    elif opcion == 3:
        if listas_cargadas:
            listar_brasil(nombres,paises,mails,telefonos)
        else:
            print("Primero importar")
    elif opcion == 4:
        if listas_cargadas:
            usuarios_mas_jovenes(nombres,edades)
        else:
            print("Primero importar")
    elif opcion == 5:
        if listas_cargadas:
            print(promedio_edades(edades))
        else:
            print("Primero importar")
    elif opcion == 6:
        if listas_cargadas:
            brasil_mayor_edad(nombres, paises, edades)
        else:
            print("Primero importar")
    elif opcion == 7:
        if listas_cargadas:
            mexico_brasil_cp(nombres, paises, codigos_postales)
        else:
            print("Primero importar")
    elif opcion == 8:
        if listas_cargadas:
            italianos_mayores(nombres, paises, edades, mails, telefonos)
        else:
            print("Primero importar")
    elif opcion == 9:
        if listas_cargadas:
            mexico_ordenado_nombre(nombres,paises,edades,mails,telefonos,codigos_postales)
        else:
            print("Primero importar")
    elif opcion == 10:
        if listas_cargadas:
            jovenes_ordenados(nombres,edades)
        else:
            print("Primero importar")
    elif opcion == 11:
        if listas_cargadas:
            mexico_brasil_ordenado(nombres,paises,edades,codigos_postales)
        else:
            print("Primero importar")
    elif opcion == 12:
        break
    else:
        print("Opcion invalida")