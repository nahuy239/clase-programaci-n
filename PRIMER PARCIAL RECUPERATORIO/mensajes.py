def mostrar_menu()->None:
    '''
    brief: Muestra en pantalla las opciones disponibles del 
    menú principal de la aplicación.
    '''
    print("""
    1) Importar la lista de pokemones
    2) Listar todos los pokemones
    3) Agregar pokemon a la lista
    4) Eliminar pokémon por nombre
    5) Ordenar la lista de pokémons por nombre (alfabéticamente de la Z a la A)
    6) Ver pokemon más pesado de los de tipo agua
    7) Ver pokemon con más fuerza de ataque
    8) Listar sólo los pokemones de una región en particular
    9) Salir
    """)

def cargar_lista(lista:list)->list:
    '''
    brief: Muestra un mensaje de confirmación de carga y retorna la 
    lista de pokemones recibida.
    
    lista: lista de listas que representa la base de datos de los pokemones.
    '''
    print("Lista cargada correctamente")
    return lista

def mostrar_region()->None:
      '''
      brief: Imprime en pantalla los nombres de las regiones válidas disponibles en el programa.
      '''
      print("Kanto, Johto, Hoenn, Sinnoh, Kalos, Unova")

def mostrar_pokemon(pokemon:list)->None:
    '''
    brief: Imprime en pantalla de forma ordenada y estética todos los datos de un único pokemon.
    
    pokemon: lista que contiene las características individuales de un pokemon.
    '''

    print(f"""\n
        Nombre: {pokemon[0]}
        Tipo: {pokemon[1]}
        Altura: {pokemon[2]}
        Peso: {pokemon[3]}
        Nivel: {pokemon[4]}
        Fuerza Ataque: {pokemon[5]}
        Región: {pokemon[6]}
    --------------------------------------------------""")