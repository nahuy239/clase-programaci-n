'''
1. Escribir una función que calcule el área de un rectángulo. La función recibe la base y
la altura y retorna el área.
2. Escribe una función que calcule el área de un círculo. La función debe recibir el radio
como parámetro y devolver el área.
3. Crea una función que verifique si un número dado es par o impar. La función debe
imprimir un mensaje indicando si el número es par o impar.
4. Crea una función que verifique si un número dado es par o impar. La función retorna
True si el número es par, False en caso contrario.
5. Define una función que encuentre el máximo de tres números. La función debe
aceptar tres argumentos y devolver el número más grande.
6. Diseña una función que calcule la potencia de un número. La función debe recibir la
base y el exponente como argumentos y devolver el resultado.
7. Crear una función que reciba un número y retorne True si el número es primo, False
en caso contrario.
8. Crear una función que (utilizando la función del punto 11 de la guía de For),
muestre todos los números primos comprendidos entre entre la unidad y un número
ingresado como parámetro. La función retorna la cantidad de números primos
encontrados.
9. Crear una función que imprima la tabla de multiplicar de un número recibido como
parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir
el rango de multiplicación. Por defecto es del 1 al 10.
10. Crear una función que le solicite al usuario el ingreso de un número entero y lo
retorne.
11. Crear una función que le solicite al usuario el ingreso de un número flotante y lo
retorne.
12. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.
13. Especializar las funciones del punto 10, 11, 12 para hacerlas reutilizables. Agregar
validaciones.'''

#1----------------------------------------------------------------------------------------------------

'''def retorno_area_rectangulo():
    base = int(input("Ingresa la base: "))
    altura = int(input("Ingresa la altura: "))
    return base * altura

area = retorno_area_rectangulo()

print(f"El area del rectangulo es {area}")'''

#2----------------------------------------------------------------------------------------------------

'''def retorno_potencia(radio:float):
    return 3.1416 * (radio ** 2)

area = retorno_potencia(15)

print(f"El area del circulo es {area}")'''

#3----------------------------------------------------------------------------------------------------

'''def determinar_primo(numero):
    return numero % 2 == 0

num = int(input("Ingresa un numero: "))

resultado = determinar_primo(num)

if resultado == True:
    print("El numero es par")
else:
    print("El numero es impar")
'''
#4----------------------------------------------------------------------------------------------------

'''def determinar_primo(numero):
    return numero % 2 == 0

num = int(input("Ingresa un numero: "))

resultado = determinar_primo(num)
print(resultado)'''
#5----------------------------------------------------------------------------------------------------

'''def encontrar_maximo(num1:int, num2:int, num3:int):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

resultado = encontrar_maximo(10, 25, 18)

print(f"El número mayor es: {resultado}")'''
#6----------------------------------------------------------------------------------------------------

'''def retorno_potencia(base:int, exponente:int):
    return base ** exponente

resultado = retorno_potencia(3, 3)

print(f"La potencia es {resultado}")'''
#7----------------------------------------------------------------------------------------------------
'''def determinar_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero): 
        if numero % i == 0:
            return False

    return True

num = int(input("Ingresa un numero: "))

resultado = determinar_primo(num)
print(resultado)'''
#8----------------------------------------------------------------------------------------------------

'''def mostrar_primos(numero):
    contador = 0

    print("Números primos encontrados:")

    for i in range(2, numero + 1):
        es_primo = True

        for j in range(2, i):
            if i % j == 0:
                es_primo = False
                break

        if es_primo:
            print(i)
            contador += 1

    return contador


num = int(input("Ingrese un número: "))

cantidad = mostrar_primos(num)

print(f"Cantidad de números primos: {cantidad}")'''
#9----------------------------------------------------------------------------------------------------

'''def imprimir_tabla(numero:int, inicio:int, fin:int):
    
    for i in range(inicio, fin + 1):
        print(f"{numero} x {i} = {numero * i}")

imprimir_tabla(5, 1, 10)
'''
#10----------------------------------------------------------------------------------------------------

'''def pedir_entero():
    numero = int(input("Ingrese un número entero: "))
    return numero

num = pedir_entero()
print(f"El número ingresado es: {num}")'''

#11----------------------------------------------------------------------------------------------------
'''def pedir_flotante():
    numero = float(input("Ingrese un número entero: "))
    return numero

num = pedir_flotante()
print(f"El número ingresado es: {num}")'''

#12----------------------------------------------------------------------------------------------------
'''def pedir_cadena():
    cadena = (input("Ingrese una cadena de texto: "))
    return cadena

cadena = pedir_cadena()
print(f"La cadena es: {cadena}")'''

#13----------------------------------------------------------------------------------------------------

def pedir_entero(mensaje, desde, hasta):
    numero = int(input(mensaje))

    while numero < desde or numero > hasta:
        numero = int(input(f"Error. Ingrese un número ({desde}-{hasta}): "))
    return numero

def pedir_flotante(mensaje, desde, hasta):
    numero = float(input(mensaje))

    while numero < desde or numero > hasta:
        numero = float(input(f"Error. Ingrese un número ({desde}-{hasta}): "))
    return numero

def pedir_cadena(mensaje):
    texto = input(mensaje)

    while texto == "":
        texto = input("Error. No puede estar vacío: ")
    return texto

edad = pedir_entero("Ingrese su edad: ", 1, 100)
precio = pedir_flotante("Ingrese el precio: ", 1, 1000)
nombre = pedir_cadena("Ingrese su nombre: ")

print(edad)
print(precio)
print(nombre)