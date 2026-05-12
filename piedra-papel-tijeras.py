print("PIEDRA, PAPEL O TIJERAS ✊ ✋ ✌\n")

# ======= JUGADORES =======

nombre1 = input("Hola Jugador 1, ¿cuál es tu nombre?: ")
nombre2 = input("Hola Jugador 2, ¿cuál es tu nombre?: ")


while True:

# ======= JUGADOR 1 =======

    while True:
        jugador1 = input(f"Hola {nombre1}, elige piedra, papel o tijeras: ").strip().lower()

        if jugador1 in ["piedra", "papel", "tijeras"]:
            break   
        else: 
            print("❌ Elegí una opción válida: piedra, papel o tijeras.")

# ======= JUGADOR 2 =======

    while True:
        jugador2 = input(f"Hola {nombre2}, elige piedra, papel o tijeras: ").strip().lower()

        if jugador2 in ["piedra", "papel", "tijeras"]:
            break   
        else: 
            print("❌ Elegí una opción válida: piedra, papel o tijeras.")

# ======= CONDICIONES =======

    condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

# ======= RESULTADOS =======

    if jugador1 == jugador2:
        print("¡Empate!")
    elif condicion1 or condicion2 or condicion3:
        print(f"{nombre1} gana! 🎉")
    else: 
        print(f"{nombre2} gana! 🎉")

# ======= ¿JUGAMOS DE NUEVO? =======
    while True:
        respuesta = input("\n¿Jugamos una más? (s/n): ").strip().lower()
        
        if respuesta in ["s", "si", "sí", "y"]:
            print("¡Genial! Nueva ronda...\n")
            break                     # Sale del bucle de pregunta y vuelve al juego
        elif respuesta in ["n", "no"]:
            print("\n¡Gracias por jugar! 👋")
            exit()                    # Termina el programa
        else:
            print("❌ Por favor responde solo 's' o 'n'.")