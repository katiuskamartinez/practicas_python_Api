#programa que muestre el numero de veces que se repite una letra en un texto

def contar_letra_en_mayusculas():
    texto = input("Introduce tu nombre: ").upper()  # Convierte el texto a mayúsculas
    letra_a_buscar = "O"
    cantidad = texto.count(letra_a_buscar)

    print(f"\nNombre en mayúsculas: {texto}")
    print(f"La letra '{letra_a_buscar}' aparece {cantidad} veces.")

# Ejecutar la función
contar_letra_en_mayusculas()
