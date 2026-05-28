def validar_opcion(opcion, listas_cargadas)->bool:
    '''
    brief: Verifica si la opción elegida por el usuario requiere
    que la lista esté cargada previamente y si cumple con esa condición.
    
    opcion: string que representa la opción del menú seleccionada 
    por el usuario.
    listas_cargadas: booleano que indica si la base de datos de
    pokemones ya fue importada.
    '''
    if (opcion == "2" or opcion == "3" or opcion == "4" or 
        opcion == "5" or opcion == "6" or opcion == "7" or 
        opcion == "8") and listas_cargadas == False:
        print("Primero tienes que importar la lista")

        return False
    return True

def validaciones_string(valor:str)->bool:
    '''
    brief: Valida que el texto ingresado no esté vacío y que 
    contenga al menos un carácter diferente de un espacio en blanco.
    
    valor: string que se desea analizar y validar.
    '''
    if len(valor) == 0:
        return False
    for i in range(len(valor)):
        if valor[i] != " ":
            return True          
    return False

def validaciones_num(valor: str) -> bool:
    '''
    brief: Verifica que la cadena ingresada represente un
    número válido (entero o flotante positivo), controlando que no 
    tenga caracteres extraños ni más de un punto decimal.
    
    valor: string numérico que ingresa el usuario y que se desea
    validar antes de transformarlo a float o int.
    '''
    if len(valor) == 0:
        return False    
    puntos = 0
    for i in range(len(valor)):
        caracter = valor[i]       
        if (caracter != "0" and
            caracter != "1" and
            caracter != "2" and
            caracter != "3" and
            caracter != "4" and
            caracter != "5" and
            caracter != "6" and
            caracter != "7" and
            caracter != "8" and
            caracter != "9" and 
            caracter != "."):
            return False
        if caracter == ".":
            puntos += 1
            if puntos > 1:
                return False     
    return True

def validaciones_region(valor:str)->bool:
    '''
    brief: Compara el texto ingresado con las regiones oficiales permitidas 
    en el programa para determinar si es válido.
    
    valor: string con el nombre de la región que se desea verificar.
    '''
    if (valor == "Johto" or 
        valor == "Kanto" or 
        valor == "Sinnoh"or 
        valor == "Hoenn" or 
        valor == "Kalos" or 
        valor == "Unova"):
        return True 
    return False

def solicitar_opcion_valida()->str:
    '''
    brief: Solicita al usuario una opción por consola de forma reiterada
    hasta que ingrese un número del menú válido.
    '''
    opcion = input("Ingresa una opcion: ")
    while  (opcion != "1" and opcion != "2" and opcion != "3" and 
            opcion != "4" and opcion != "5" and opcion != "6" and 
            opcion != "7" and opcion != "8" and opcion != "9"):

            opcion = input("Intenta de nuevo. Ingresa una opcion: ")
    return opcion