from listas_personas import nombres

def mostrar_nombres(lista_personas:list)->None:
    for i in range(len(lista_personas)):
        print(lista_personas[i])

mostrar_nombres(nombres)
