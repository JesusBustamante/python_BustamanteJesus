from os import system

Productos = {
    "Manzana":{
        "Nombre":"Manzana",
        "Precio":10,
        "Cantidad":12,
        
    },
    "Pera":{
        "Nombre":"Pera",
        "Precio":15,
        "Cantidad":8,
        
    },
    "Mango":{
        "Nombre":"Mango",
        "Precio":8,
        "Cantidad":7,

    }   
}

carrito = {}
total = 0

booleanito = True
while booleanito == True:
    system("cls")

    print("-----------------CARRITO DE COMPRAS--------------------")
    print("")
    print("""             Estos son nuestros productos
          
            |PRODUCTO|    PRECIO   |CANT|
            |Manzana |  10 COP C/U | 12 |
            |Pera    |  15 COP C/U | 8  |
            |Fresa   |  13 COP KG  | 5  |
            |Mango   |  8  COP C/U | 7  |""")
    print("")
    print("1. Agregar al carrito")
    print("2. Ver estado del carrito")
    print("3. Salir")
    print("")
    Opcion = int(input("Elige una opción(1-2)\n"))

    if Opcion == 1:

        cantidad = int(input("Cuantos productos va a comprar\n"))

        for i in range(0,cantidad):

            carro = (input("Elija un artículo\n"))
            print("")

            if carro in Productos and Productos[carro]["Cantidad"] >= cantidad:
                Productos[carro]["Cantidad"] -= cantidad
                if carro in carrito:
                    carrito[carro]["Cantidad"] += cantidad
                else:
                    carrito[carro] = Productos[carro].copy()
                    carrito[carro]["Cantidad"] = cantidad
                    total += Productos[carro]["Precio"] * cantidad
                
                print ("Producto agregado al carrito")
                
            else:
                print("Lo siento, este artículo está agotado.")
                print("")

            input("Para continuar presione enter.")
    
    if Opcion == 2:
        for i in carrito:
            pro = carrito[i]
            print(f"Nombre: {pro["Nombre"]}, Precio: {pro["Precio"]}, Cantidad: {pro["Cantidad"]}")
        print("El total de compra es: ", total)
    input("Para continuar presione enter.")

    if Opcion == 3:
        break
booleanito = False
