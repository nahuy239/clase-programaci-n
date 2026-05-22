'''
Ejercicio 1: Desarrollar una función que reciba una letra y una cadena.
Debe retornar las veces que la letra está incluida en el texto.
Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.
Se debe retornar la cadena que va entre las posiciones indicadas por los índices.
Si las posiciones no son válidas se debe informar.
Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.
Se debe retornar el caracter en la posición indicada por el número si ésta es válida.
**IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el
<número de caracteres> - 1.
'''

'''
#       EJERCICIO 1

def recibir_letra(letra:str, cadena:str)->None:
    contador_letra = 0
    for i in range(len(cadena)):
        if cadena[i] == letra:
            contador_letra += 1
    return contador_letra

texto = input("Ingresa una cadena: ")
letra = input("Ingresa una letra: ")

resultado = recibir_letra(letra, texto)

print(f"La cantidad de veces que la letra esta incluida en el texto:{resultado}")'''

'''
#       EJERCICIO 2

def cadena_entre_indices(cadena: str, indice1: int, indice2: int) -> str:
    if indice1 < 0 or indice2 < 0 or indice1 >= len(cadena) or indice2 >= len(cadena) or indice1 > indice2:
        return "Posiciones no válidas"
    return cadena[indice1:indice2+1]


texto = input("Ingrese una cadena: ")
indice1 = int(input("Ingrese primer índice: "))
indice2 = int(input("Ingrese segundo índice: "))

resultado = cadena_entre_indices(texto, indice1, indice2)

print(resultado)'''

#       EJERCICIO 3

def char_at(cadena: str, posicion: int):
    if posicion < 0 or posicion >= len(cadena):
        return "Posición inválida"
    return cadena[posicion]

texto = input("Ingrese una cadena: ")
pos = int(input("Ingrese una posición: "))

resultado = char_at(texto, pos)

print(resultado)