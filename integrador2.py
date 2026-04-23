'''
UTN Technologies, una reconocida software factory se encuentra en la búsqueda
de ideas para su próximo desarrollo en Python, que promete revolucionar el
mercado.
Las posibles aplicaciones son las siguientes:
● Inteligencia artificial (IA),
● Realidad virtual/aumentada (RV/RA),
● Internet de las cosas (IOT)
Para ello, la empresa realiza entre sus empleados una encuesta, con el
propósito de conocer ciertas métricas.
A) Los datos a ingresar por cada empleado encuestado son:
● nombre del empleado
● edad (no menor a 18)
● género (Masculino - Femenino - Otro)
● tecnologia (IA, RV/RA, IOT)
B) Cargar por terminal 10 encuestas.
C) Determinar:
1. Cantidad de empleados de género masculino que votaron por IOT o IA,
cuya edad esté entre 25 y 50 años inclusive.
2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
género no sea Femenino o su edad se encuentre entre los 33 y 40.
3. Nombre y tecnología que votó, de los empleados de género masculino con
mayor edad de ese género.
'''

encuestas = 0
contador_masculino = 0
empleados_no_ia = 0
mayor_edad = 0
nombre_mayor = ""
tecnologia_mayor = ""



while encuestas < 10:

    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad (no menor a 18): "))
    while edad < 18:
        edad = int(input("ERROR, Ingresa tu edad (no menor a 18): "))
    genero = input("Ingresa tu genero(Masculino - Femenino - Otro): ")
    while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
        genero = input("ERROR, Ingresa tu genero(Masculino - Femenino - Otro): ")  
    tecnologia = input("Ingresa la tecnologia (IA, RV/RA, IOT): ")
    while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
        tecnologia = input("ERROR, Ingresa la tecnologia (IA, RV/RA, IOT): ")

    if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50:
        contador_masculino += 1
    
    if tecnologia != "IA" and (genero != "Femenino" or 33 <= edad <= 40):
        empleados_no_ia += 1
    
    if genero == "Masculino":
        if edad > mayor_edad:
            mayor_edad = edad
            nombre_mayor = nombre
            tecnologia_mayor = tecnologia
            

    encuestas += 1

porcentaje_empleados_no_ia = (empleados_no_ia / encuestas) * 100

print(f"La cantidad de empleados de género masculino que votaron por IOT o IA,edad entre 25 y 50 fueron {contador_masculino}")
print(f"Porcentaje de empleados que no votaron por IA {porcentaje_empleados_no_ia}")
print(f"Nombre y tecnología que votó el empleado masculino con mayor edad es {nombre_mayor}, tiene {mayor_edad} y voto {tecnologia_mayor}")

