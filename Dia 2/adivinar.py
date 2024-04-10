import random

# Explicación del juego
print("Bienvenido a 'Adivina el número'!")
print("El objetivo del juego es adivinar un número secreto.")
print("Después de cada intento, recibirás una retroalimentación para ayudarte.")
print("¡Vamos a empezar!")

continuar = "si"
while continuar.lower() == "si":
 # Generar un número secreto aleatorio entre 1 y 100
 numero_secreto = random.randint(1, 100)

 # Solicitar la entrada del jugador
 Numintentos = 0
 adivinadaa = False

 # Bucle principal del juego
 while not adivinadaa and Numintentos < 10:
    suposicion = input("Ingresa tu número (entre 1 y 100): ")
    
    # Validación de entrada
    if not suposicion.isdigit():
        print("Por favor, ingresa un número válido.")
        continue
    
    suposicion = int(suposicion)
    
    # Validación de rango
    if suposicion < 1 or suposicion > 100:
        print("El número debe estar entre 1 y 100.")
        continue
    Numintentos += 1

    # Comparación y retroalimentación
    if suposicion < numero_secreto:
        print("Muy bajito. ¡Intenta otra vez!")
    elif suposicion > numero_secreto:
        print("Muy altote. ¡Intenta otra vez!")
    else:
        print(f"¡Felicidades! ¡Adivinaste el número en {Numintentos} intentos!")
        adivinadaa = True

    # Contador de intentos
    print(f"Intentos realizados: {Numintentos}")

 # Finalización del juego

 if adivinadaa:
    print(f"¡Felicidades! ¡Adivinaste el número en {Numintentos} intentos!")
 else:
    print("No has adivinado el número en diez intentos. El número secreto era: ", numero_secreto)

 continuar = input("¿Desea continuar? (si/no): ")
 if continuar.lower() == "no":
    print("Hasta luego")

#Realizado por Jesús Bustamante PPT: 1258502