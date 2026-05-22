#1-----------------------------------------------------------------------------------------
'''def guardado_nombres():
    nombres = []

    for i in range(0,10):
        nombre = input(f"Ingresa un nombre ({i}): ")
        nombres.append(nombre)
    return nombres

lista_nombres = guardado_nombres()
print(lista_nombres)'''
#2-----------------------------------------------------------------------------------------
'''def guardar_numero():
    lista = [0] * 10

    posicion = int(input("Ingrese una posición (1 al 10): "))
    numero = int(input("Ingrese un número para guardar: "))

    lista[posicion - 1] = numero

    return lista


resultado = guardar_numero()

print(f"Lista resultante:\n{resultado} ")'''
#3----------------------------------------------------------------------------------------
'''def cargar_numeros():
    lista = []

    minimo = int(input("Ingrese el valor mínimo del rango: "))
    maximo = int(input("Ingrese el valor máximo del rango: "))

    for i in range(0, 10):

        numero = int(input(f"Ingrese el número {i + 1}: "))

        while numero < minimo or numero > maximo:
            numero = int(input(f"ERROR, Ingrese el número {i + 1}: "))
        lista.append(numero)

    return lista

resultado = cargar_numeros()

print(f"Lista de números:\n{resultado}")'''
#4-----------------------------------------------------------------------------------------
'''def buscar_numero(lista:list, numero:int):
    for i in range(len(lista)):
        if lista[i] == numero:
            return True
    return False


numeros = [10, 20, 30, 40, 50]

buscar = int(input("Ingrese un número a buscar: "))
resultado = buscar_numero(numeros, buscar)

print(resultado)'''
#5-----------------------------------------------------------------------------------------
nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises",
            "Sofia","Maria","Pedro","Antonio","Eugenia",
            "Soledad","Mario","Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def buscar_menores(lista_edades:list)->int:
    menor = lista_edades[0]

    for i in range(len(lista_edades)):
        if lista_edades[i] < menor:
            menor = lista_edades[i]

    return menor


menor_edad = buscar_menores(edades)

print("Personas con menor edad:")
for i in range(len(edades)):
    if edades[i] == menor_edad:
        print(nombres[i], "-", edades[i])

#7-----------------------------------------------------------------------------------------


