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
total_dinero_hospital = 0

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
    

    #costo por paciente
    costo_internacion = cant_dias * costo_por_dia

    #descuento por obra social
    if obra_social == "SI":
        costo_internacion *= 0.8
    
    #acumuladores
    total_dias += cant_dias
    total_dinero_hospital += costo_internacion


    internaciones = input("Quieres seguir agregando internaciones (si/no): ")
    while internaciones != "si" and internaciones != "no":
            internaciones = input("Quieres seguir agregando internaciones (si/no): ")
    