'''Enunciado/s:
Tabla de Posiciones de Torneo de Ping-Pong
Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
Los datos que se cargarán son:
Nombre del jugador
Edad (validar)
Cantidad de puntos (validar-número entero positivo, hasta 60).
Tipo de saque ("plano", "liftado", "cortado")
Categoría ("elite", "experto", "avanzado")
Se necesita saber
Tema A:
1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
inclusive.
2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
3-Porcentaje de jugadores de categoría "experto".
4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”.'''

seguir = "si"
contador_elite_plano = 0
bandera_jugador_menor = True
menor_edad = 0
nombre_mas_joven = ""
categoria_mas_joven = ""
jugadores_totales = 0
jugadores_expertos = 0
jugadores_avanzados = 0
suma_edad_avanzados = 0
plano = 0
liftado = 0
cortado = 0

while seguir == "si": 

    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    cantidad_puntos = int(input("Cantidad de puntos(hasta 60): "))
    while cantidad_puntos < 0 or cantidad_puntos > 60:
        cantidad_puntos = int(input("ERROR, Cantidad de puntos(hasta 60): "))
    numero_partidos_ganados = int(input("Cantidad de partidos ganados(hasta 35): "))
    while numero_partidos_ganados <= 0 or numero_partidos_ganados > 35:
        numero_partidos_ganados = int(input("ERROR, Cantidad de partidos ganados(hasta 35): "))
    tipo_saque = input("Tipo de saque (plano, liftado, cortado): ")
    while tipo_saque != "plano" and tipo_saque != "liftado" and tipo_saque != "cortado":
        tipo_saque = input("ERROR, Tipo de saque (plano, liftado, cortado): ")
    categoria = input("Categoria (elite, experto, avanzado): ")
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        categoria = input("ERROR, Categoria (elite, experto, avanzado): ")

    if categoria == "elite" and tipo_saque == "plano" and edad >= 19 and edad <= 25:
        contador_elite_plano += 1
    
    if cantidad_puntos > 50:
        if bandera_jugador_menor == True or edad < menor_edad:
            menor_edad = edad
            nombre_mas_joven = nombre
            categoria_mas_joven = categoria
            bandera_jugador_menor = False
    
    if categoria == "experto":
        jugadores_expertos += 1
        
    if categoria == "avanzado":
        jugadores_avanzados += 1
        suma_edad_avanzados += edad
            
    
    if categoria == "elite":
        jugadores_elite += 1
        if tipo_saque == "plano":
            plano += 1
        elif tipo_saque == "liftado":
            liftado += 1
        else:
            cortado += 1

    
    jugadores_totales += 1

    seguir = input("Quieres seguir cargando (si/no): ")
    while seguir != "si" and seguir != "no":
        seguir = input("ERROR, Quieres seguir cargando (si/no): ")

porcentaje_experto = (jugadores_expertos / jugadores_totales) * 100
promedio_avanzado = suma_edad_avanzados / jugadores_avanzados

if plano >= liftado and plano >= cortado:
    tipo_saque_mas_usado = "plano"
elif liftado >= plano and liftado >= cortado:
    tipo_saque_mas_usado = "liftado"
else:
    tipo_saque_mas_usado = "cortado"


print(f"Jugadores elite con saque plano entre 19 y 25 años son {contador_elite_plano}")
print(f"{nombre_mas_joven} fue el jugador de la categoria {categoria_mas_joven} de menor edad ({menor_edad}) con más de 50 puntos.")
print(f"Porcentaje de jugadores de categoría experto: {porcentaje_experto}")
print(f"El promedio de edad de los jugadores de categoria avanzado es {promedio_avanzado}")
print(f"El tipo de saque más usado por los jugadores de categoria elite es {tipo_saque_mas_usado}")
    


 



