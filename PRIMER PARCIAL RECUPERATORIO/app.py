from pokemones import *
from mensajes import *
from abm import *
from validaciones import *

def app(lista_pokemon:list)->None:
    '''
    brief: Controla el flujo principal de la aplicación mediante un 
    menú interactivo que permite administrar los pokemones
    
    lista_pokemon: lista de listas que contiene la base de 
    datos inicial de los pokemones a gestionar
    '''
    flag = True
    listas_cargadas = False

    while flag == True:
        mostrar_menu()

        opcion = solicitar_opcion_valida()

        listas_on = validar_opcion(opcion, listas_cargadas)

        if listas_on == True:
            if opcion == "1":
                lista_pokemon = cargar_lista(lista_pokemon)
                listas_cargadas = True
            elif opcion == "2":
                listar_pokemones(lista_pokemon)
            elif opcion == "3":
                agregar_pokemon(lista_pokemon)
            elif opcion == "4":
                eliminar_pokemon_nombre(lista_pokemon)
            elif opcion == "5":
                ordenar_por_nombre(lista_pokemon, 0)
            elif opcion == "6":
                resultado = buscar_maximo(lista_pokemon, 3, "Agua")
                mostrar_pokemon(resultado)
            elif opcion == "7":
                resultado = buscar_maximo(lista_pokemon, 5)
                mostrar_pokemon(resultado)
            elif opcion == "8":
                listar_por_region(lista_pokemon)
            elif opcion == "9":
                flag = False
    
        
app(lista_pokemon)



    
