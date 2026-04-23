venta_diaria = 0
descuento = 0
total_unidades = 0
total_bruto = 0
venta_mas_cara_tarjeta = 0
precio_unitario_total = 0
forma_mas_usada = ""
efectivo = 0
transferencia = 0
tarjeta = 0

while venta_diaria < 25:
    tipo_producto = input("Ingresa el tipo de producto(alimento, limpieza, perfumeria): ")
    while tipo_producto != "alimento" and tipo_producto != "limpieza" and tipo_producto != "perfumeria":
        tipo_producto = input("ERROR, Ingresa el tipo de producto(alimento, limpieza, perfumeria): ")
    unid_vendidas = int(input("Ingresa la cantidad de unidades vendidas (entre 1 y 20): "))
    while unid_vendidas < 1 or unid_vendidas > 20:
        unid_vendidas = int(input("ERROR,  Ingresa la cantidad de unidades vendidas (entre 1 y 20): "))
    precio_unitario = float(input("Ingresa el precio unitario(mayor a 0): "))
    while precio_unitario <= 0:
        precio_unitario = float(input("ERROR, Ingresa el precio unitario(mayor a 0): "))
    forma_pago = input("Ingresa la forma de pago(efectivo, tarjeta, transferencia): ")
    while forma_pago != "efectivo" and forma_pago != "tarjeta" and forma_pago != "transferencia":
        forma_pago = input("ERROR, Ingresa la forma de pago(efectivo, tarjeta, transferencia): ")
    
    subtotal = unid_vendidas * precio_unitario

    if forma_pago == "efectivo":
        subtotal = subtotal - (subtotal * 0.05)
    
    if forma_pago == "tarjeta":
        if subtotal > venta_mas_cara_tarjeta:
            venta_mas_cara_tarjeta = subtotal

    if forma_pago == "efectivo":
        efectivo += 1
    elif forma_pago == "tarjeta":
        tarjeta += 1
    else:
        transferencia += 1

    
    total_unidades += unid_vendidas
    total_bruto += subtotal
    precio_unitario_total += precio_unitario
    venta_diaria += 1

if total_unidades > 400 :
    descuento = 20
elif total_unidades > 200:
    descuento = 10

if efectivo >= tarjeta and efectivo >= transferencia:
    forma_mas_usada = "efectivo"
elif tarjeta >= efectivo and tarjeta >= transferencia:
    forma_mas_usada = "tarjeta"
else:
    forma_mas_usada = "transferencia" 

total_final = total_bruto - (total_bruto * descuento / 100)
promedio_unitario = precio_unitario_total / venta_diaria


print(f"El importe total bruto sin descuento es: {total_bruto}")
print(f"El importe total bruto final con todos los descuentos es: {total_final}")
print(f"La venta más cara echa con tarjeta es {venta_mas_cara_tarjeta}")
print(f"El promedio del precio unitario de todas las ventas es {promedio_unitario} ")
print(f"La forma más usada es: {forma_mas_usada}")