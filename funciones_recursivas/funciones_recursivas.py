#1-----------------------------------------------------------------------------------------

'''def suma_naturales(numero:int)-> int:
    if numero == 1:
        return 1
    else:
        return numero + suma_naturales(numero - 1)

numero = int(input("Ingrese un número: "))

resultado = suma_naturales(numero)

print(f"La suma de los primeros números naturales es: {resultado}")'''

#2-----------------------------------------------------------------------------------------
'''
def calcular_potencia(base: int, exponente: int)-> int:
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = calcular_potencia(base, exponente)

print(f"El resultado es: {resultado}")'''

#3-----------------------------------------------------------------------------------------

'''def sumar_digitos(numero: int)->int:
    if numero < 10:
        return numero
    else:
        return (numero % 10) + sumar_digitos(numero // 10)

num = int(input("Ingrese un número: "))

resultado = sumar_digitos(num)

print(f"La suma de los dígitos es: {resultado}")'''
#4-----------------------------------------------------------------------------------------
def get_int(mensaje, mensaje_error, minimo, maximo, reintentos):
    numero = int(input(mensaje))

    while (numero < minimo or numero > maximo) and reintentos > 0:
        reintentos -= 1
        numero = int(input(mensaje_error))

    return numero

def calcular_fibonacci(numero:int)->int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
