from os import system


carros = {
    "C01":{
        "Id":"C01",
        "marca":"Porsche",
        "modelo":"911GT",
        "cilindraje":2500,
        "estado":"Usado",
        "año":2017,
        "precio":42000,
        "cantidad": 3
    },
    "C02":{
        "Id":"C02",
        "marca":"BMW",
        "modelo":"X1",
        "cilindraje":1400,
        "estado":"Usado",
        "año":2021,
        "precio":28000,
        "cantidad": 3
    },
    "C03":{
        "Id":"C03",
        "marca":"FERRARI",
        "modelo":"365P",
        "cilindraje":4390,
        "estado":"Usado",
        "año":1965,
        "precio":20000000,
        "cantidad": 3
    }
}

articulo = []
carrito = {}
cont = 0
total = 0
total1=0



sel=0 # le damos valor a nuestra variable sel-eccion para asi poder ejecutarla en nuestro while
while sel!=4:  # hacemos un while para hacer un bucle a nuestras tres opciones
    system("cls") # colocamos un limpiaar pantalla
    print("""
    -----BIENVENIDO AL CONCESIONARIO TIBUYANO----------
    ¿Que deseas hacer?
    1. Revisa los autos disponibles y añade los que quieras al carrito.
    2. Revisa el contenido que tienes en carrito y tu total de compra.
    3. Resumen de tu compra.
    4. ¿Desea terminar el programa?.
    ---------------------------------------------------
    """)
    
    sel=int(input("Digita el numero de lo primero que deseas hacer:\n")) # Le pedimos al usuario que por favor ingrese el numero de alguna de nuestras opc.
        
    if sel == 1:

        for m in carros:
            car=carros[m]
            print(f"Id: {car["Id"]}, marca: {car["marca"]}, modelo: {car["modelo"]}, año: {car["año"]}, estado: {car["estado"]}, precio: {car["precio"]}, cantidad: {car["cantidad"]},")

        cantidad = int(input("Cuantos productos va a comprar\n"))

        for i in range(0,cantidad):

            articulo = (input("Elija un artículo digitando su código\n"))

            if carros[articulo]["cantidad"] >= 1:  
                carros[articulo]["cantidad"] -= 1  
                carrito[articulo] = carros[articulo]
                total += carros[articulo]["precio"]
                
            else:
                print("Lo siento, este artículo está agotado.")

        input("Para continuar presione enter.")
    
    if sel == 2:
        for m in carrito:
            car=carrito[m]
            print(f"Id: {car['Id']}, marca: {car['marca']}, modelo: {car['modelo']}, año: {car['año']}, estado: {car['estado']}, precio: {car['precio']}, cantidad: {car['cantidad']}")
        print("El total de compra es: ", total)

        input("Para continuar presione enter.")
    
    if sel == 3:
        print("\n GRACIAS POR ELEGIR A NUESTRO CONCESIONARIO PARA HACER TU COMPRA")
        print("\n Resumen de tu compra\n")

        for m in carrito:
            car=carrito[m]
            print(f"marca: {car['marca']}, modelo: {car['modelo']}, año: {car['año']}, estado: {car['estado']}, precio: {car['precio']}, cantidad: {car['cantidad']}")
        print("El total de compra es: ", total)

        input("Para continuar presione enter.")

else:
    print("El programa se ha cerrado.")
    input("Para continuar presione enter.")