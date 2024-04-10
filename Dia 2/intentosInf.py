import random

# Explicación del juego
print("Bienvenido a '¿Cúal será el número?'!")
print("El objetivo del juego es adivinar un número secreto.")
print("Después de cada intento, recibirás una retroalimentación para ayudarte.")
print("¡Vamos a empezar!")

# Generar un número secreto aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Solicitar la entrada del jugador
intentos = 0
adivinado = False

# Bucle principal del juego
while not adivinado:
    suposicion = input("Ingresa tu suposición (entre 1 y 100): ")
    
    # Validación de entrada
    if not suposicion.isdigit():
        print("Por favor, ingresa un número válido.")
        continue
    
    suposicion = int(suposicion)
    
    # Validación de rango
    if suposicion < 1 or suposicion > 100:
        print("El número debe estar en el rango de 1 a 100.")
        continue
    intentos += 1

    # Comparación y retroalimentación
    if suposicion < numero_secreto:
        print("Demasiado bajo. ¡Intenta nuevamente!")
    elif suposicion > numero_secreto:
        print("Demasiado alto. ¡Intenta nuevamente!")
    else:
        print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
        adivinado = True

    # Contador de intentos
    print(f"Intentos realizados: {intentos}")

# Finalización del juego

print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
adivinado = True


