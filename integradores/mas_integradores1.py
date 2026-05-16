'''
Ejercicio 1: Registro de internaciones en un hospital
Un hospital registra una cantidad indeterminada de internaciones en un día.
Por cada paciente se ingresan los siguientes datos:
● Nombre del paciente
● Edad (entre 0 y 100)
● Tipo de atención (urgencia, control, cirugía)
● Cantidad de días internado (entre 1 y 60)
● Costo por día (mayor a 0)
● Sexo (F, M, NB)
● Tiene obra social (sí/no)
● Forma de pago (efectivo, tarjeta, transferencia)
Todos los datos deben ser validados.
Consideraciones:
● Si el paciente tiene obra social, se aplica un descuento del 20% sobre el costo de su
internación.
● Si la cantidad total de días acumulados supera los 500, se aplica un descuento
general del 10% sobre el total bruto.
Se pide:
a. Total bruto recaudado por internaciones. Luego, total final con descuentos aplicados.
b. Cantidad de pacientes por tipo de atención.
c. El tipo de atención con mayor cantidad de días acumulados.
d. El nombre del paciente con mayor costo total de internación.
e. El promedio de costo por día de todos los pacientes.
f. Qué forma de pago fue la más utilizada.
g. Cuántos pacientes tienen más de 10 días de internación.
'''

internaciones = "si"
total_dias = 0
total_bruto_internaciones = 0
urgencia = 0
control = 0
cirugia = 0
dias_urgencia = 0
dias_control = 0
dias_cirugia = 0
max_costo = 0
max_paciente = ""
costos_dias = 0
cantidad_pacientes = 0
efectivo = 0
transferencia = 0
tarjeta = 0
#dias_internados = 0
mas_de_10_dias = 0

while internaciones == "si":
    nombre = input("Ingresa el nombre del paciente: ")

    edad = int(input("Ingresa la edad del paciente (0-100): "))
    while edad <= 0 or edad > 100:
        edad = int(input("ERROR, Ingresa la edad del paciente (0-100): "))

    tipo_atencion = input("Ingresa el tipo de antecion (urgencia, control, cirugía): ")
    while tipo_atencion != "urgencia" and tipo_atencion != "control" and tipo_atencion != "cirugía":
        tipo_atencion = input("ERROR, Ingresa el tipo de antecion (urgencia, control, cirugía): ")

    cant_dias = int(input("Ingresa la cantidad de dias internado(1-60): "))
    while cant_dias < 1 or cant_dias > 60:
        cant_dias = int(input("ERROR, Ingresa la cantidad de dias internado(1-60): "))

    costo_por_dia = int(input("Ingresa el costo por dia(mayor a 0): "))
    while costo_por_dia < 0:
        costo_por_dia = int(input("ERROR, Ingresa el costo por dia(mayor a 0): "))

    sexo = (input("Ingresa el sexo(F/M O NB): "))
    while sexo != "F" and sexo != "M" and sexo != "NB":
        sexo = (input("ERROR, Ingresa el sexo(F/M O NB): "))

    obra_social = (input("Tiene obra social (SI/NO): "))
    while obra_social != "SI" and obra_social != "NO":
        obra_social = (input("ERROR, Tiene obra social (SI/NO): "))

    forma_pago = (input("Forma de pago (efectivo, tarjeta, transferencia) "))
    while forma_pago != "efectivo" and forma_pago != "tarjeta" and forma_pago != "transferencia":
        forma_pago = (input("ERROR, Forma de pago (efectivo, tarjeta, transferencia) "))
    


    costo_internacion = cant_dias * costo_por_dia

    if obra_social == "SI":
        costo_internacion *= 0.8

    total_dias += cant_dias
    total_bruto_internaciones += costo_internacion
    
    if tipo_atencion == "urgencia":
        urgencia += 1
        dias_urgencia += cant_dias
    elif tipo_atencion == "control":
        control += 1
        dias_control += cant_dias
    elif tipo_atencion == "cirugía":
        cirugia +=1
        dias_cirugia += cant_dias
    
    if costo_internacion > max_costo:
        max_costo = costo_internacion
        max_paciente = nombre
    
    costos_dias += costo_por_dia
    cantidad_pacientes += 1

    if forma_pago == "efectivo":
        efectivo += 1
    elif forma_pago == "tarjeta":
        tarjeta += 1
    elif forma_pago == "transferencia":
        transferencia += 1
    
    if cant_dias > 10:
        mas_de_10_dias += 1
    



    internaciones = input("Quieres seguir agregando internaciones (si/no): ")
    while internaciones != "si" and internaciones != "no":
            internaciones = input("Quieres seguir agregando internaciones (si/no): ")

if total_dias > 500:
    total_dinero = total_bruto_internaciones * 0.9
else:
    total_dinero = total_bruto_internaciones

promedio_costo = costos_dias / cantidad_pacientes

if dias_cirugia > dias_control and dias_cirugia > dias_urgencia:
    tipo_mayor = "cirugia"
elif dias_control > dias_cirugia and dias_control > dias_urgencia:
    tipo_mayor = "control"
else:
    tipo_mayor = "urgencia"

if efectivo > transferencia and efectivo > tarjeta:
    forma_pago_mayor = "efectivo"
elif transferencia > efectivo and transferencia > tarjeta:
    forma_pago_mayor = "transferencia"
else:
    forma_pago_mayor = "tarjeta"


print(f"El total bruto recaudado por internaciones es {total_bruto_internaciones}, y el final con los descuentos es {total_dinero}")
print(f"La cantidad de pacientes por tipo es: URGENCIA: {urgencia}, CONTROL: {control} y CIRUGÍA: {cirugia}")
print(f"El tipo de atención con mayor cantidad de días acumulados es {tipo_mayor} ")
print(f"El nombre del paciente es con mayor costo total de internación es {max_paciente}, costo: {max_costo}")
print(f"El promedio de costo por día de todos los pacientes es {promedio_costo}")
print(f"La forma de pago fue la más utilizada fue: {forma_pago_mayor}")
print(f"Pacientes que tienen más de 10 días de internación: {mas_de_10_dias}")