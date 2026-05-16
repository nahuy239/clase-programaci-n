'''
Una empresa registra alquileres de autos durante un período. No se sabe cuántos registros
habrá.
Por cada alquiler se ingresan:
● Nombre del cliente
● Tipo de vehículo (auto, camioneta, moto)
● Cantidad de días de alquiler (entre 1 y 30)
● Precio por día (mayor a 0)
● Kilómetros recorridos (entre 0 y 5000)
● Forma de pago (efectivo, tarjeta, transferencia)
● Cliente frecuente (sí/no)
Validar todos los datos.
Consideraciones:
● Si el cliente es frecuente, tiene un descuento del 15% sobre el total del alquiler.
● Si el total de kilómetros acumulados supera los 20000 km, se aplica un recargo del
10% sobre el total bruto general.
● Las camionetas tienen un recargo del 20% sobre su costo individual.
Se pide:
a. Calcular el importe total bruto y el total final.
b. El tipo de vehículo con mayor cantidad de alquileres.
c. El nombre del cliente que más días alquiló en total.
d. El promedio de kilómetros recorridos.
e. Qué tipo de vehículo acumuló más kilómetros.
f. Cuántos alquileres fueron pagados con tarjeta.
g. El alquiler de mayor importe (indicar cliente y monto)
'''

alquileres = "si"
total_bruto_general = 0
total_kilometros = 0
auto = 0
camioneta = 0
moto = 0
nombre_cliente_max = ""
max_dias_alquier = 0
contador_alquileres = 0
km_auto = 0
km_camioneta = 0
km_moto = 0
tarjeta = 0
max_importe = 0
cliente_max_importe = ""

while alquileres == "si":
    nombre = input("Ingresa el nombre del cliente: ")

    tipo_vehiculo = input("Tipo de vehículo(auto, camioneta, moto): ")
    while tipo_vehiculo != "auto" and tipo_vehiculo != "camioneta" and tipo_vehiculo != "moto":
        tipo_vehiculo = input("ERROR, Tipo de vehículo(auto, camioneta, moto): ")

    cant_dias = int(input("Cantidad de días de alquiler (entre 1 y 30): "))
    while cant_dias < 1 or cant_dias > 30:
        cant_dias = int(input("ERROR, Cantidad de días de alquiler (entre 1 y 30): "))

    precio_por_dia = int(input("Ingresa el precio por dia(mayor a 0): "))
    while precio_por_dia < 0:
        precio_por_dia = int(input("ERROR, Ingresa el precio por dia(mayor a 0): "))

    recorridos_dia = int(input("Kilómetros recorridos (entre 0 y 5000): "))
    while   recorridos_dia < 0 or recorridos_dia > 5000:
        recorridos_dia = int(input("ERROR, Kilómetros recorridos (entre 0 y 5000): "))

    forma_pago = (input("Forma de pago (efectivo, tarjeta, transferencia) "))
    while forma_pago != "efectivo" and forma_pago != "tarjeta" and forma_pago != "transferencia":
        forma_pago = (input("ERROR, Forma de pago (efectivo, tarjeta, transferencia) "))

    cliente_frecuente = (input("Cliente frecuente (sí/no): "))
    while cliente_frecuente != "sí" and cliente_frecuente != "no":
        cliente_frecuente = (input("ERROR, Cliente frecuente (sí/no): "))
    

    total_alquiler = cant_dias * precio_por_dia
    total_kilometros += recorridos_dia


    if cliente_frecuente == "sí":
        total_alquiler *= 0.85

    if forma_pago == "tarjeta":
        tarjeta += 1

    if tipo_vehiculo == "camioneta":
        total_alquiler *= 1.20
        km_camioneta += recorridos_dia
        camioneta += 1
    elif tipo_vehiculo == "auto":
        km_auto += recorridos_dia
        auto += 1
    else:
        km_moto += recorridos_dia
        moto += 1
    
    if  cant_dias > max_dias_alquier:
        nombre_cliente_max = nombre
        max_dias_alquier = cant_dias

    if total_alquiler > max_importe:
        max_importe = total_alquiler
        cliente_max_importe = nombre



    total_bruto_general += total_alquiler
    contador_alquileres += 1



    alquileres = input("Quieres seguir registrando alquieres (si/no)?: ")
    while alquileres != "si" and alquileres != "no":
        alquileres = input("ERROR, Quieres seguir registrando alquieres (si/no)?: ")

if total_kilometros > 20000:
    total_bruto_general *= 1.10
    
total_final = total_bruto_general

if auto > camioneta and auto > moto:
    veh_mayor = "auto"
elif camioneta > auto and camioneta > moto:
    veh_mayor = "camioneta"
else:
    veh_mayor = "moto"

if km_auto > km_camioneta and km_auto > km_moto:
    vehiculo_mas_km = "auto"
elif km_camioneta > km_auto and km_camioneta > km_moto:
    vehiculo_mas_km = "camioneta"
else:
    vehiculo_mas_km = "moto"

promedio_alquiler = total_kilometros / contador_alquileres

print(f"El importe total es {total_bruto_general} y el importe final es {total_final}")
print(f"El tipo de vehículo con mayor cantidad de alquileres es: {veh_mayor}")
print(f"El nombre del cliente que más días alquiló en total es: {nombre_cliente_max}")
print(f"El promedio de kilómetros recorridos es {promedio_alquiler}")
print(f"El tipo de vehículo acumuló más kilómetros fue {vehiculo_mas_km} ")
print(f"Los alquileres que fueron pagados con tarjeta: {tarjeta}")
print(f"El alquiler de mayor importe cliente: {cliente_max_importe}, monto: {max_importe}")