from os import system

Usuario=[]
Contraseña=[]
Cuenta=[]
membresia=10
usuariosRegistrados=["Valeri", "Nilson", "Maria"]

opc=0 
while opc!=4:  
    system("cls")

    print("""
    --------------BIENVENIDO A PERIODICO EL SABER----------------
    Por favor, elije una opción
    1. Iniciar sesión
    2. Comprar una membresía o añadir dinero a la cuenta.
    3. ¿Qué tal si regalas una membresía?
    4. Salir del programa.
    ------------------------------------------------------------
    """)
    opc=int(input("Ingresa que opción deseas ejecutar:\n")) 

    if opc == 1:
        Us=input("Por favor, ingrese el usuario\n")
        if Us in Usuario:
            print("Usuario correcto.")

            Con=input("Por favor, ingrese su contraseña\n")
            if Con in Contraseña:
                print("Contraseña válida.")
            else:
                print("Contraseña inválida.")
        else:
            print("El usuario es incorrecto o no te has registrado.")
        input("Para continuar presione enter.")
    
    if opc == 2:
        seleccion=0
        while seleccion!=3:  
            system("cls") 
            print("""
            ---------------------------------------------------------------
            Compra de membresía anual - Añadir dinero a la cuenta.
            1. Comprar membresía.
            2. Añadir dinero a la cuenta.
            3. Volver al  menú principal.
            ---------------------------------------------------------------
            """)

            seleccion=int(input("Por favor, elije una opción\n"))

            if seleccion == 1:

                print("Ingresa tus datos para iniciar con el registro.")
                Usu = input("Agrega un nombre de usuario\n")
                Usuario.append(Usu)

                Contra=input("Crea tu contraseña\n")
                Contraseña.append(Contra)

                cm=int(input("Cuantos años de membresía deseas comprar.\n"))
                total=cm*membresia

                print("El total a pagar de su membresía es:", total)
                print ("")

                total = float(input("Ingresa el total de la membresía\n"))  
                if total>sum(Cuenta):
                    print("Lo sentimos, no cuentas con fondos en la cuenta")
                else:
                    Cuenta.append(-total)
                    print("Pago realizado con éxito.")
                    print("")
                    
                    print("El dienro restante en tu cuenta es: ", sum(Cuenta))
                    print("")

                    print("Compra exitosa.")
                    print("")
                input("Para continuar presione enter.")

            if seleccion == 2:
                money = float(input("Ingresa la cantidad de dinero a añadir a tu cuenta\n")) 
                Cuenta.append(money)
                print("")

                print("La plata añadida a tu cuenta es: ", sum(Cuenta))  
                print("")
            input("Para continuar presione enter.")

        else:
            input("Para continuar al menú principal presione enter.")   

    if opc == 3:
        regalo=input("Ingresa el nombre de usuario al que quieres regalar una membresía\n")
        print("")

        if regalo in usuariosRegistrados:
            cm=int(input("¿Cuantos años de membresía deseas regalar\n"))
            total=cm*membresia
            print("")
            print("El total a pagar de la membresía de regalo es:", total)
            total = float(input("Digita el total a pagar por la membresía de regalo\n"))  

            if total>sum(Cuenta):
                print("Lo sentimos, no cuentas con fondos en la cuenta")
            else:
                Cuenta.append(-total)
                print("Pago realizado.")
                print("")

                print("La plata restante es: ", sum(Cuenta))
                print("")

                print("Has comprado la membresía de regalar con exito.")
        else:
            print("Lo sentimos, el usuario al que le vas a regalar la membresía no existe.")
        input("Para continuar presione enter.")

else:
    print("Programa finalizado.")
    input("Para continuar presione enter.")

#Realizado por Jesus Bustamante - PPT 1258502