import random

# lista de opciones disponibles en el juego
opciones = ("piedra", "papel", "tijera")
# variable
jugar = True

print("Bienvenido al juego Piedra, Papel o Tijera")

# Estructura repetitiva del juego
while jugar:

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
    else:
        print("Resultado: Perdiste")

    continuar = input("¿Desea jugar de nuevo? (si/no)").lower()
    if continuar != "si":
        jugar = False

print("Gracias por jugar. !Hasta pronto¡")