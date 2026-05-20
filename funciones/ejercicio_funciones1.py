'''
Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe
como parámetro.
Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.
Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La
función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
programa principal realizando la invocación o llamada.
Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en
un rango determinado pasado por parámetro “desde”-“hasta”.
Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la
función Restar en sus 4 combinaciones.
Restar1(int, int)->int:
Restar2()->int:
Restar3(int, int):
Restar4():
Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor
solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
por pantalla. Atención: pueden reutilizarse funciones ya creadas.
Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2
los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice
la operación de dichos valores a través de una función. Mostrar el resultado por
pantalla.
'''

# ------------EJERCICIO 3-1-------------

# def mostrar_numero(numero):
#     print(numero)

# mostrar_numero(5)

# ------------EJERCICIO 3-2-------------

# def pedir_numero():
#     numero = int(input("Ingresa el numero: "))
#     return numero

# num = pedir_numero()
# print(f"El numero es {num} ")

# ------------EJERCICIO 3-3-------------

# def determinar_par(numero):
#     return numero % 2 == 0

# num = int(input("Ingresa un numero: "))

# resultado = determinar_par(num)
# print(resultado)

# ------------EJERCICIO 3-4-------------

def validar_numero(desde, hasta):
    numero = int(input("ingresa el numero: "))

    while numero < desde or numero > hasta:
        numero = int(input(f"error, ingresa el numero({desde}- {hasta}): "))

    return numero

# num = validar_numero(1,10)

# print(num)

# ------------EJERCICIO 3-5-------------

# def Restar1(num1, num2)->int:
#     return num1 - num2


# def Restar2()->int:
#     num = int(input("Ingresa el primer numero: "))
#     num2 = int(input("Ingresa el segundo numero: "))
#     return num - num2


# def Restar3(num, num2):
#     print(f"resultado: {num - num2}")
    
    
# def Restar4()->int:
#     num = int(input("Ingresa el primer numero: "))
#     num2 = int(input("Ingresa el segundo numero: "))
#     print(f"resultado: {num - num2}")

# resta1 = Restar1(5,2)
# print(resta1)
# resta2= Restar2()
# print(resta2)
# Restar3(30, 15)
# Restar4()

# ------------EJERCICIO 3-6-------------

# def realizarDescuento(numero):
#     descuento = numero * 0.05
#     return numero - descuento

# numero1 = validar_numero(10,100)
# resultado = realizarDescuento(numero1)
# print(resultado)

# ------------EJERCICIO 3-7-------------

def validar_operacion():
    operacion = input("Ingrese operación ('s' sumar / 'r' restar): ")

    while operacion != "s" and operacion != "r":
        operacion = input("Error. Ingrese 's' o 'r': ")
    return operacion

def realizar_operacion(num1, num2, operacion):
    if operacion == "s":
        return num1 + num2
    else:
        return num1 - num2

numero1 = validar_numero(10, 100)
numero2 = validar_numero(10, 100)
operacion = validar_operacion()
resultado = realizar_operacion(numero1, numero2, operacion)

print(f"El resultado es:{resultado}")