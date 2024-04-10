# Este programa genera la secuencia de Fibonacci hasta un término especificado por el usuario.
# La secuencia de Fibonacci es una serie de números donde cada número es la suma de los dos anteriores.
# Comienza con 0 y 1 y cada término subsiguiente se calcula como la suma de los dos términos anteriores.

# Imprime una intrduccón a la secuencia de Fibonacci y su presencia en la naturaleza.

print("Naturaleza hipnótica: la sucesión matemática de Fibonacci")
print("")
print("Resulta sorprendente que en la naturaleza aparezca recurrentemente una construcción matemática. En el siglo XIII, el matemático italiano Leonardo de Pisa, conocido como Fibonacci, describió una serie o sucesión que aparece en configuraciones biológicas: en flores de alcachofas y girasoles, en algunas inflorescencias, en las piñas o incluso en la estructura en espiral de algunos moluscos como el nautilus.")
print("La “sucesión de Fibonacci” explica que, empezando por la unidad, cada uno de los siguientes términos de la serie es la suma de los dos anteriores (1,1,2,3,5,8,13…). Y si dividimos cualquier número de la secuencia por el anterior, el resultado siempre se aproxima a 1.61803, conocido como el “número áureo” representado por letra griega phi (por eso también se denomina a esta serie “secuencia dorada”).")
print("")

# Inicia un bucle que permite al usuario generar secuencias de Fibonacci múltiples veces.
continuar = "si"
while continuar.lower() == "si":

 # Solicita al usuario que ingrese un número entero que representa el término final de la secuencia a generar.
 intNum = input("Por favor, ingrese un valor entero (representando hasta qué término de la secuencia se generará: ")
 intNum = int(intNum)

 # Inicializa los dos primeros términos de la secuencia de Fibonacci.
 a = 0
 b = 1

 print("")

 # Imprime la secuencia de Fibonacci hasta el término especificado por el usuario.
 for i in range (1, intNum): 
    while a < 89:
        print(a)
        break
    c = a + b
    a = b
    b = c

 print("")

  # Pregunta al usuario si desea continuar o terminar el programa.
 continuar = input("¿Desea continuar? (si/no): ")
 if continuar.lower() == "no":
    print("Hasta luego")

    



#Desarrollado por Jesús Bustamante PPT: 1258502