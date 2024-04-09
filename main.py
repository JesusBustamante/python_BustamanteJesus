#-----------------------------------
#------Día 1 cheat sheet python-----
#-----------------------------------

#Imprimir Hola Mundo
print("Hola Mundo")
print("")

#Datos primitivos

#Número
numerito = 1 #nombreVariable = valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir(tipo(variable))
print("")

#Decimal
numeritoDecimal = 1.1
print(numeritoDecimal)
print(type(numeritoDecimal))
print("")

#Booleano
miBooleanito = True
print(miBooleanito)
print(type(miBooleanito))
print("")

#Cadena de texto
texto = "MI TIBU"
print(texto)
print(type(texto))
print("")

jesus = ("love")
print(jesus)

print("")
#Ingresa por teclado la información (input)
nombre = input("Por favor, ingrese su nombre: ")


#Conversión de tipos de variables(convertir string a un número, número a booleano)
print("")
#String a int
edad = "18"
print(edad)
print(type(edad))

int_edad = int(edad)
print(int_edad + 2) 
print(type(int_edad))

#int a bool
print("")
valor_int = 10
print(valor_int)
print(type(valor_int))

valor_bool = bool(valor_int)
print(valor_bool)  # Salida: True
print(type(valor_bool))

valor_int = 0
print(valor_int)
print(type(valor_int))

valor_bool = bool(valor_int)
print(valor_bool)  # Salida: False 
print(type(valor_bool))

#Bucles For y While
print("")
#While
i = 0
while i < 10 :
  print(i**2)  
  i = i + 1
  print ("El yisus")

#For
print("")
for i in range(10) :
  print(i**2)

#Funciones de cuatro tipos
print("")
# función sin parámetros o retorno de valores
def Saluda() :
    print("jaguariyu") # llamada a la función, 'Hello!' se muestra en la consola
Saluda()

# función con un parámetro
print("")
def saludaAlpana(name) :
    print("Hola mi amigazo " + name + ", eres inteligente")
    
saludaAlpana("Jesús")

# función con múltiples parámetros con una sentencia de retorno
print("")
def resta(rest1 , rest2) :
    resta = rest1 - rest2
    return resta

resultResta = resta(10 , 5)

print("El resultado de la resta es: ", resultResta, )

#Funcion sin parametro con retorno
print("")
def suma() :
 return "2"

print("Resultado Suma: ", suma(),)

#Desarrollado por Jesús Bustamante - PPT 1.258.502