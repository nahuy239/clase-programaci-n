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