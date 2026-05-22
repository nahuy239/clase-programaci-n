def listar_mexico(nombres:list,paises:list,edades:list)->None:
    for i in range(len(nombres)):
        if paises[i] == "Mexico":
            print(nombres[i], edades[i])


def listar_brasil(nombres:list,paises:list,mails:list,telefonos:list)->None:
    for i in range(len(nombres)):
        if paises[i] == "Brasil":
            print(nombres[i], mails[i], telefonos[i])


def usuarios_mas_jovenes(nombres:list,edades:list)->None:
    menor = edades[0]

    for i in range(len(edades)):
        if edades[i] < menor:
            menor = edades[i]

    for i in range(len(edades)):
        if edades[i] == menor:
            print(nombres[i], edades[i])


def promedio_edades(edades:list)->float:
    suma = 0

    for i in range(len(edades)):
        suma += edades[i]

    promedio = suma / len(edades)
    return promedio

def brasil_mayor_edad(nombres:list,paises:list,edades:list)->None:
    mayor = -1
    pos = 0
    for i in range(len(nombres)):
        if paises[i] == "Brasil":
            if edades[i] > mayor:
                mayor = edades[i]
                pos = i
    print(nombres[pos], edades[pos])

def mexico_brasil_cp(nombres:list,paises:list,codigos_postales:list)->None:
    for i in range(len(nombres)):
        if (paises[i] == "Mexico" or paises[i] == "Brasil") and codigos_postales[i] > 8000:
            print(nombres[i], paises[i], codigos_postales[i])

def italianos_mayores(nombres:list,paises:list,edades:list,mails:list,telefonos:list)->None:
    for i in range(len(nombres)):
        if paises[i] == "Italia" and edades[i] > 40:
            print(nombres[i], mails[i], telefonos[i])

def mexico_ordenado_nombre(nombres:list,paises:list,edades:list,mails:list,telefonos:list,codigos_postales:list)->None:
    cantidad = len(nombres)

    for i in range(cantidad - 1):
        for j in range(i + 1, cantidad):
            if paises[i] == "Mexico" and paises[j] == "Mexico":
                if nombres[i] > nombres[j]:
                    aux = nombres[i]
                    nombres[i] = nombres[j]
                    nombres[j] = aux

                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux

                    aux = edades[i]
                    edades[i] = edades[j]
                    edades[j] = aux

                    aux = mails[i]
                    mails[i] = mails[j]
                    mails[j] = aux

                    aux = telefonos[i]
                    telefonos[i] = telefonos[j]
                    telefonos[j] = aux

                    aux = codigos_postales[i]
                    codigos_postales[i] = codigos_postales[j]
                    codigos_postales[j] = aux

    for i in range(cantidad):
        if paises[i] == "Mexico":
            print(nombres[i], edades[i], mails[i], telefonos[i], codigos_postales[i])


def jovenes_ordenados(nombres:list,edades:list)->None:
    
    cantidad = len(nombres)
    for i in range(cantidad - 1):
        for j in range(i + 1, cantidad):
            if edades[i] > edades[j] or (edades[i] == edades[j] and nombres[i] > nombres[j]):
                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux

                aux = edades[i]
                edades[i] = edades[j]
                edades[j] = aux

    menor_edad = edades[0]

    for i in range(len(edades)):
        if edades[i] < menor_edad:
            menor_edad = edades[i]

    for i in range(len(edades)):
        if edades[i] == menor_edad:
            print(nombres[i], edades[i])

def mexico_brasil_ordenado(nombres:list,paises:list,edades:list,codigos_postales:list)->None:

    cantidad = len(nombres)
    for i in range(cantidad - 1):
        for j in range(i + 1, cantidad):
            condicion_i = (paises[i] == "Mexico" or paises[i] == "Brasil") and codigos_postales[i] > 8000
            condicion_j = (paises[j] == "Mexico" or paises[j] == "Brasil") and codigos_postales[j] > 8000
            if condicion_i and condicion_j:
                if nombres[i] > nombres[j] or (nombres[i] == nombres[j] and edades[i] < edades[j]):
                    aux = nombres[i]
                    nombres[i] = nombres[j]
                    nombres[j] = aux

                    aux = paises[i]
                    paises[i] = paises[j]
                    paises[j] = aux

                    aux = edades[i]
                    edades[i] = edades[j]
                    edades[j] = aux

                    aux = codigos_postales[i]
                    codigos_postales[i] = codigos_postales[j]
                    codigos_postales[j] = aux

    for i in range(len(nombres)):
        if (paises[i] == "Mexico" or paises[i] == "Brasil") and codigos_postales[i] > 8000:
            print(nombres[i], paises[i], edades[i], codigos_postales[i])

