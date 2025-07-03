# el ordenador"elige" un número secreto entre 1 y 100, y el jugador tiene un número limitado de intentos para adivinarlo. el ordenador dará pistas (mayor o menor) después de cada intento.

import random

def juego_adivina_numero():
    """
    Juego de adivinanza de números simple.
    El jugador tiene que adivinar un número secreto entre 1 y 100.
    """
    print("--- ¡Bienvenido al Juego de Adivinanza! ---")
    print("Estoy pensando en un número entre 1 y 100.")
    print("Tienes 7 intentos para adivinarlo.")

    # Generar un número secreto aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos_realizados = 0
    max_intentos = 7

    while intentos_realizados < max_intentos:
        try:
            intento = int(input(f"Intento #{intentos_realizados + 1}: Adivina el número: "))

            if intento < 1 or intento > 100:
                print("Por favor, ingresa un número entre 1 y 100.")
                continue # Volver al inicio del bucle sin contar este intento como válido

            intentos_realizados += 1

            if intento < numero_secreto:
                print("¡Demasiado bajo! Intenta un número mayor.")
            elif intento > numero_secreto:
                print("¡Demasiado alto! Intenta un número menor.")
            else:
                # El jugador adivinó el número
                print(f"¡Felicidades! ¡Adivinaste el número en {intentos_realizados} intentos!")
                return # Salir de la función (y del juego)

        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")
            # No incrementamos intentos_realizados para no penalizar entradas incorrectas

    # Si el bucle termina, significa que se agotaron los intentos
    print("\n--- ¡Lo siento! ---")
    print(f"Has agotado tus {max_intentos} intentos.")
    print(f"El número secreto era: {numero_secreto}")

# --- Ejecutar el juego ---
if __name__ == "__main__":
    juego_adivina_numero()