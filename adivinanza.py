import random

def juego_adivinanza():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de la adivinanza!")
    print("He elegido un número entre 1 y 100. Tienes que adivinarlo.")

    # Bucle principal del juego
    while not adivinado:
        # Solicitar al jugador que ingrese un número
        try:
            # Leer la entrada del jugador
            jugador = int(input("Introduce tu adivinanza: "))
            intentos += 1
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        # Comprobar si el número es mayor, menor o igual al número secreto
        if jugador < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        elif jugador > numero_secreto:
            print("El número es menor. Intenta de nuevo.")
        else:
            adivinado = True
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")

# Llamar a la función para iniciar el juego
juego_adivinanza()
