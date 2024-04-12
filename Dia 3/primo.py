#Definimos la función para verificar si un número es primo
#Esta función verifica si un número es primo o no
#Argumentos: n = número entero a verificar
#Retorna: 'es primo' si el número es primo, 'no es primo' en caso contrario

def primo(n):
    #Si el número es menor o igual a 1, no es primo
    if n <= 1:
        return "no es primo"
    #El número 2 es primo
    elif n == 2:
        return "es primo"
    else:
        #Verificamos si el número es divisible por algún número en el rango de 2 a n
        for i in range(2, n):
            # Si el número es divisible por i, entonces no es primo
            if n % i == 0:
                return "no es primo"
        return "es primo" 


#Iniciamos el programa
print("--------------------------FUNCIONES-------------------------------------")
print("")
print("Verificador de números primos = 1")
print("Generador de contraseñas = 2\n")

opciones = input("¡Hola!. Por favor, seleccione que función desea ejecutar(1/2)\n ")

#Opción para verificar si un número es primo
if opciones == "1":

    print("Bienvenido Usuario")
    print("")
    print("El programa cumple con la función de verificar si el número dado es primo o no")
    print("")

    #Booleano para crear un ciclo
    booleanito = True
    while booleanito == True:
        
        print("--------------Menú-----------------")
        print("")
        print("1. Verificar número")
        print("2. Obtener información adicional")
        print("3. Salir")
        print("")

        opcion = input("¿Qué opción del menú desea escoger\n")
        if opcion == "1": 
            print("")
            
            n = int(input("¿Cúal es el número que desea verificar?\n"))
            print("El número ", n, primo(n))
        
        if opcion == "2":
            print("")
            print("¿Qué son los números primos?")
            print("")
            print("Los números primos son aquellos que solo son divisibles entre ellos mismos y el 1, es decir, que si intentamos dividirlos por cualquier otro número, el resultado no es entero. Dicho de otra forma, si haces la división por cualquier número que no sea 1 o él mismo, se obtiene un resto distinto de cero.")
            print("")
            print("Desarrollado por Jesús Bustamante")

        if opcion == "3":
            print("")
            print("Hasta luego")
            break

        
    booleanito = False

if opciones == "2":

    # Importamos las librerías necesarias
    import string
    import random
    
    # Definimos la función para generar una contraseña segura
    #Esta función genera una contraseña segura
    def contraseña_segura(longitud, minusculas, mayusculas, numeros, especiales):

        caracteres = "" #Inicializamos la cadena de caracteres vacía

        if minusculas: #Si el usuario quiere minúsculas, añadimos las minúsculas a la cadena de caracteres
            caracteres += string.ascii_lowercase

        if mayusculas: #Si el usuario quiere mayúsculas, añadimos las mayúsculas a la cadena de caracteres
            caracteres += string.ascii_uppercase

        if numeros: #Si el usuario quiere números, añadimos los números a la cadena de caracteres 
            caracteres += string.digits

        if especiales: #Si el usuario quiere caracteres especiales, añadimos los caracteres especiales a la cadena de caracteres
            caracteres += string.punctuation

        #Inicializamos la contraseña vacía
        contraseña = ""

        #Generamos la contraseña
        for i in range(longitud): 
            contraseña += random.choice(caracteres)
        return contraseña #Retorna: contraseña -- contraseña generada
    

    continuar = "si"
    while continuar.lower() == "si":
        print("Bienvenido usuario")
        print("")
        print("¿Qué es un generador de contraseñas segura?")
        print("")
        print("Un generador de contraseñas aleatorias es una herramienta que lo libera de tener que crear constantemente contraseñas únicas para cada uno de sus sitios. Funciona generando automáticamente contraseñas seguras y aleatorias de acuerdo a sus requerimientos, que incluyen combinaciones de números, letras mayúsculas y minúsculas y caracteres especiales.")
        print("")


        #longitud -- longitud de la contraseña
        longitud = int(input("¿Cúal es la longitud que deseas para tu contraseña segura:\n"))
        
        #minusculas -- booleano, si es True la contraseña contendrá minúsculas
        minusculas = input("¿Quieres que tu contraseña contenga minúsculas?(si/no)\n").lower() == "si"

        #mayusculas -- booleano, si es True la contraseña contendrá mayúsculas
        mayusculas = input("¿Quieres que tu contraseña contenga mayúsculas?(si/no)\n").lower() == "si"

        #numeros -- booleano, si es True la contraseña contendrá números
        numeros = input("¿Quieres que tu contraseña contenga números?(si/no)\n").lower() == "si"

        #especiales -- booleano, si es True la contraseña contendrá caracteres especiales
        especiales = input("¿Quieres que tu contraseña contenga caracteres especiales?(si/no)\n").lower() == "si"


        newContraseña = contraseña_segura(longitud, minusculas, mayusculas, numeros, especiales)
        print("Su contraseña segura es :", newContraseña)

        continuar = input("Desea crear otra contraseña(si/no)\n")

        if continuar == "no":
            print("Hasta luego")
            break

#Desarrollado por Jesús Bustamante PPT: 1258502
