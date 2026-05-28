from mensajes import *
from validaciones import *

def listar_pokemones(lista:list)->None:
    '''
    brief: Recorre la lista de pokemones completa y los muestra 
    uno por uno en pantalla

    lista: lista de listas que contiene la base de datos de los pokemones.
    '''
    for i in range(len(lista)):
        mostrar_pokemon(lista[i])

def agregar_pokemon(lista:list)->None:
    '''
    brief: Pide los datos de un nuevo pokemon por consola, 
    los valida, arma una sublista y la agrega a la lista principal

    lista: lista de listas donde se guardará el nuevo 
    pokemon mediante un append
    '''

    nombre = input("Ingresa el nombre: ")
    while validaciones_string(nombre) == False:
        nombre = input("Error. Ingresa un nombre válido: ")

    tipo = input("Ingresa el tipo: ")
    while validaciones_string(tipo) == False:
        tipo = input("Error. Ingresa un tipo válido: ")

    altura = input("Ingresa la altura: ")
    while validaciones_num(altura) == False:
        altura = input("Error. Ingresa una altura válida: ")
    altura = float(altura)
    
    peso = input("Ingresa el peso: ")
    while validaciones_num(peso) == False:
        peso = input("Error. Ingresa un peso válido: ")
    peso = float(peso)

    nivel = input("Ingresa el nivel: ")
    while validaciones_num(nivel) == False:
        nivel = input("Error. Ingresa un nivel válido: ")
    nivel = int(nivel)

    fuerza_ataque = input("Ingresa la fuerza de ataque: ")
    while validaciones_num(fuerza_ataque) == False:
        fuerza_ataque = input("Error. Ingresa fuerza válida: ")
    fuerza_ataque = int(fuerza_ataque)

    mostrar_region()
    region = input("Ingresa la región: ")
    while validaciones_region(region) == False:
        mostrar_region()
        region = input("Error. Región inválida: ")

    pokemon_nuevo = [nombre, tipo, altura, peso,
                     nivel, fuerza_ataque, region]

    lista.append(pokemon_nuevo)

def eliminar_pokemon_nombre(lista:list)->None:
    '''
    brief: Busca un pokemon por su nombre para mostrarlo en 
    pantalla y eliminarlo de la lista principal

    lista: lista de listas de la cual se removerá el 
    pokemon que coincida con el nombre ingresado
    '''
    nombre = input("Ingresa el nombre del pokemon a eliminar: ")
    for i in range(len(lista)):
        if nombre == lista[i][0]:
            mostrar_pokemon(lista[i])
            lista.pop(i)           
            break

def ordenar_por_nombre(lista:list, indice:int)->None:
    '''
    brief: Ordena la lista de pokemones de manera alfabética de la Z a la A
    basándose en el índice recibido
    
    lista: lista de listas que se modificará e intercambiará de posición internamente
    indice: entero que representa la posición del dato por el cual se quiere ordenar
    '''
    for i in range(len(lista)-1):
        for j in range(i + 1, len(lista)):
            if lista[i][indice] < lista[j][indice]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def buscar_maximo(lista:list, indice:int, tipo:str ="")->list:
    '''
    brief: Busca y encuentra al pokemon con el valor más alto en un índice 
    determinado, permitiendo filtrar opcionalmente por tipo
    
    lista: lista de listas sobre la que se realizará la búsqueda del valor máximo
    indice: entero que indica qué característica numérica se va a evaluar
    tipo: string opcional que sirve para filtrar la búsqueda únicamente 
    a un tipo de pokemon específico
    '''
    mayor = lista[0]
    flag_primero = True
    for i in range(len(lista)):
        if tipo == "" or lista[i][1] == tipo:
            if flag_primero == True or lista[i][indice] > mayor[indice]:
                mayor = lista[i]
                flag_primero = False          
    return mayor

def listar_por_region(lista:list)->None:
    '''
    brief: Solicita una región al usuario por consola y 
    muestra en pantalla únicamente a los pokemones pertenecientes a ella
    
    lista: lista de listas que se recorrerá para filtrar los 
    pokemones según la región indicada
    '''
    mostrar_region()
    region = input("Ingresa la región: ")
    while validaciones_region(region) == False:
        mostrar_region()
        region = input("""Región inválida. Intenta de nuevo: """)
    print("-------POKEMONES DE LA REGIÓN---------")
    for i in range(len(lista)):
        if lista[i][6] == region:
            mostrar_pokemon(lista[i])