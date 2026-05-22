'''
Un gimnasio registra ventas de planes a sus clientes. La cantidad de registros es
indeterminada.
Por cada venta se ingresan:
● Nombre del cliente
● Tipo de plan (mensual, trimestral, anual)
● Edad (entre 12 y 80)
● Precio del plan (mayor a 0)
● Forma de pago (efectivo, tarjeta, transferencia)
● Turno elegido (mañana, tarde, noche)
● Es alumno nuevo (sí/no)
Validar todos los datos.
Consideraciones:
● Si es alumno nuevo, tiene un descuento del 10%.
● Si se venden más de 50 planes en total, se aplica un descuento general del 5%.
● Los planes anuales tienen un recargo del 15%.
Se pide:
a. Total bruto y total final con descuentos/recargos.
b. Cantidad de ventas por tipo de plan.
c. El turno con más clientes.
d. El nombre del cliente que pagó el plan más caro.
e. El promedio de precios de planes vendidos.
f. Qué forma de pago fue la más utilizada.
g. Cuántos clientes son menores de 18 años.
'''

ventas = "si"
total_bruto = 0
total_final_general = 0 
cantidad_ventas = 0
mensual = 0
trimestral = 0
anual = 0
manana = 0
tarde = 0
noche = 0
max_precio = 0
cliente_max_precio = ""
suma_precios = 0
efectivo = 0
tarjeta = 0
transferencia = 0
menores = 0

while ventas == "si":
    nombre = input("Ingrese el nombre del cliente: ")

    tipo_plan = input("Tipo de plan (mensual, trimestral, anual): ")
    while tipo_plan != "mensual" and tipo_plan != "trimestral" and tipo_plan != "anual":
        tipo_plan = input("ERROR, Tipo de plan (mensual, trimestral, anual) ")

    edad = int(input("Edad (entre 12 y 80): "))
    while edad < 12 or edad > 80:
        edad = int(input("ERROR, Edad (entre 12 y 80): "))

    precio = float(input("Precio del plan (mayor a 0): "))
    while precio <= 0:
        precio = float(input("ERROR, Precio del plan (mayor a 0) "))

    forma_pago = input("Forma de pago (efectivo, tarjeta, transferencia): ")
    while forma_pago != "efectivo" and forma_pago != "tarjeta" and forma_pago != "transferencia":
        forma_pago = input("ERROR, Forma de pago (efectivo, tarjeta, transferencia): ")

    turno = input("Turno elegido (mañana, tarde, noche): ")
    while turno != "mañana" and turno != "tarde" and turno != "noche":
        turno = input("ERROR, Turno elegido (mañana, tarde, noche) ")

    nuevo = input("Es alumno nuevo (sí/no): ")
    while nuevo != "si" and nuevo != "no":
        nuevo = input("ERROR, Es alumno nuevo (sí/no): ")

    total_bruto += precio  
    suma_precios += precio
    cantidad_ventas += 1

    total = precio
    if tipo_plan == "anual":
        total *= 1.15

    if nuevo == "si":
        total *= 0.90

    total_final_general += total  

    if tipo_plan == "mensual":
        mensual += 1
    elif tipo_plan == "trimestral":
        trimestral += 1
    else:
        anual += 1

    if turno == "mañana":
        manana += 1
    elif turno == "tarde":
        tarde += 1
    else:
        noche += 1

    if forma_pago == "efectivo":
        efectivo += 1
    elif forma_pago == "tarjeta":
        tarjeta += 1
    else:
        transferencia += 1

    if edad < 18:
        menores += 1

    if precio > max_precio:
        max_precio = precio
        cliente_max_precio = nombre

    ventas = input("Quieres seguir añadiendo? (si/no): ")
    while ventas != "si" and ventas != "no":
        ventas = input("ERROR, Quieres seguir añadiendo? (si/no): ")

if cantidad_ventas > 50:
    total_final_general *= 0.95

if mensual > trimestral and mensual > anual:
    plan_max = "mensual"
elif trimestral > mensual and trimestral > anual:
    plan_max = "trimestral"
else:
    plan_max = "anual"

if manana > tarde and manana > noche:
    turno_max = "mañana"
elif tarde > manana and tarde > noche:
    turno_max = "tarde"
else:
    turno_max = "noche"

if efectivo > tarjeta and efectivo > transferencia:
    pago_max = "efectivo"
elif tarjeta > efectivo and tarjeta > transferencia:
    pago_max = "tarjeta"
else:
    pago_max = "transferencia"

promedio = suma_precios / cantidad_ventas


print(f"El total bruto es {total_bruto} y el total final es {total_final_general}")
print(f"El plan más vendido es {plan_max}")
print(f"El turno con más clientes es {turno_max}")
print(f"El cliente que pagó el plan más caro es {cliente_max_precio} con {max_precio}")
print(f"El promedio de precios de los planes es {promedio}")
print(f"La forma de pago más utilizada es {pago_max}")
print(f"La cantidad de clientes menores de 18 años es {menores}")