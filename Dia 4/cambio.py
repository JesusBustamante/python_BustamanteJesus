#Se pide una cantidad
#Se da el cambio con la cantidad minima de modedas posibles
#Denominaciones: 1, 5, 10

print("Bienvenido usuario")
print("")
print("Cajero de cambio de dinero")
print("")

continuar = "si"
while continuar.lower() == "si":
    cantidad = input("¿Cuanto es la cantidad de dinero que quieres cambiar?\n")

    #En Python podemos hacer uso del método split(). Si se utiliza la función de esta manera se separan los caracteres teniendo en cuenta el espacio vacío que haya entre cada uno de ellos. Si, por el contrario, deseas especificar el carácter de separación, puedes hacerlo poniéndolo entre los paréntesis del método
    dolares = int(cantidad.split(".")[0])

    #La variable monedas contiene los valores de monedas disponibles
    monedas = [10, 5, 1]

    #Cambio se inicializa con el valor de la variable dolares que es la cantidad de dinero a cambiar
    cambio = dolares

    #si dolares tiene un valor negativo se enviará un mensaje de error
    if dolares <= -1:
        print("Error. Escriba un número positivo")

        print("")

    #Si dolares tiene un valor de cero se enviará un mensaje avisando que no hay cambio para un valor de cero
    if dolares == 0:
        print("No hay cambio para esta cantidad")

        print("")


    #Este bucle revisa la variable monedas en cada iteracion
    for i in range(len(monedas)):
        
        #La variable b es igual al resultado de la division entera entre cambio y los valores de la variable moneda
        #Es decir, esta division me dice cuantas monedas caben dentro del valor de cambio
        b = cambio//monedas[i]


        if b>0:
            print(b, " monedas de ", monedas[i], " dolares")
            cambio%= monedas[i]

    continuar = input("¿Quieres volver a ingresar una cantidad de dinero?(si/no)\n")
    if continuar.lower() == "no":
        break
