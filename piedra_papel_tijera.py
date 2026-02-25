import random

# lista de opciones disponibles en el juego
opciones = ("piedra", "papel", "tijera")
# variable
jugar = True
puntos_usuario = 0
puntos_computadora = 0
ronda = 0
historial = []

print("Bienvenido al juego Piedra, Papel o Tijera")

# Estructura repetitiva del juego
while jugar:

    ronda += 1
    print(f"\n--- Ronda {ronda} ---")

    print("Selccione una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

# entrada del usuario
    opcion_usuario = input("Ingrese el número de su opción: ")

# validación de la opción
    if opcion_usuario not in ["1", "2", "3"]: 
        print("Opción inválida. Intente nuevamente.")
        continue   # regresa al inicio del ciclo

    # conversión a texto
    usuario =opciones[int(opcion_usuario) - 1]

    # la computadora elige aleatoriamente
    computadora = random.choice(opciones)
    
    print(f"Usted eligió: {usuario}")
    print(f"La computadora eligió: {computadora}")

    # comparación de opciones
    if usuario == computadora:
        print("Resultado: Empate")
    elif (
        (usuario == "piedra" and computadora == "tijera") or
        (usuario == "papel" and computadora == "piedra") or
        (usuario == "tijera" and computadora == "papel")
    ):
        print("Resultado: Ganaste")
        puntos_usuario += 1
    else:
        print("Resultado: Perdiste")
        puntos_computadora += 1

    # guardar historial (lista de tuplas)
    historial.append((usuario, computadora))

    print(f"Marcador -> tú: {puntos_usuario} | Computadora: {puntos_computadora}")

    continuar = input("¿Desea jugar de nuevo? (si/no): ").lower()
    if continuar != "si":
        jugar = False

print("\nHistorial de partidas:")
for partida in historial:
    print(partida)

print("Gracias por jugar. !Hasta pronto¡")