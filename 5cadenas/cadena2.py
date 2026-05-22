#1) --------------------------------------------------------------------------------------
'''def contar_vocales(cadena: str)-> str:
    cadena = cadena

    vocales = [["a", 0],
               ["e", 0],
               ["i", 0],
               ["o", 0],
               ["u", 0]]
    
    for i in range(len(cadena)):
        for j in range(len(vocales)):
            if cadena[i] == vocales[j][0]:
                vocales[j][1] += 1
    return vocales

texto = input("Ingrese una cadena: ")

resultado = contar_vocales(texto)

for i in range(len(resultado)):
    print(resultado[i][0], resultado[i][1])'''

#2) --------------------------------------------------------------------------------------
'''def buscar_caracter(cadena: str, caracter: str) -> int:

    for i in range(len(cadena)):

        if cadena[i] == caracter:
            return i

    return -1


texto = input("Ingrese una cadena: ")
caracter = input("Ingrese un caracter: ")

resultado = buscar_caracter(texto, caracter)

print(resultado)'''

#3) --------------------------------------------------------------------------------------
'''def es_palindromo(cadena: str) -> bool:
    cadena_invertida = ""
    for i in range(len(cadena) - 1, -1, -1):
        cadena_invertida += cadena[i]
    return cadena == cadena_invertida

texto = input("Ingrese una cadena: ")

resultado = es_palindromo(texto)

print(resultado)'''
#4) --------------------------------------------------------------------------------------

'''def suprimir_repetidos(cadena: str) -> str:
    resultado = ""

    for i in range(len(cadena)):
        repetido = False
        for j in range(len(resultado)):
            if cadena[i] == resultado[j]:
                repetido = True
        if repetido == False:
            resultado += cadena[i]
    return resultado

texto = input("Ingrese una cadena: ")
resultado = suprimir_repetidos(texto)

print(resultado)'''
#5) --------------------------------------------------------------------------------------
'''def suprimir_vocales(cadena: str) -> str:

    resultado = ""
    vocales = "aeiouAEIOU"

    for i in range(len(cadena)):
        es_vocal = False
        for j in range(len(vocales)):
            if cadena[i] == vocales[j]:
                es_vocal = True
        if es_vocal == False:
            resultado += cadena[i]
    return resultado


texto = input("Ingrese una cadena: ")
resultado = suprimir_vocales(texto)

print(resultado)'''
#6) --------------------------------------------------------------------------------------
def contar_subcadena(cadena: str, subcadena: str) -> int:
    contador = 0
    longitud_subcadena = len(subcadena)

    for i in range(len(cadena) - longitud_subcadena + 1):
        coincide = True
        for j in range(longitud_subcadena):
            if cadena[i + j] != subcadena[j]:
                coincide = False
        if coincide == True:
            contador += 1
    return contador

texto = input("Ingrese una cadena: ")
sub = input("Ingrese subcadena: ")

resultado = contar_subcadena(texto, sub)

print(resultado)