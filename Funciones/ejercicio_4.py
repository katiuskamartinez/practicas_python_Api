#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def calcular_total_factura(cantidad_sin_iva, iva=21):
    """ Calcula el total de la factura incluyendo el IVA """
    total = cantidad_sin_iva * (1 + iva / 100)
    return round(total, 2)

# Ejemplo de uso
cantidad = float(input("Introduce la cantidad sin IVA: "))
porcentaje_iva = input("Introduce el porcentaje de IVA (opcional, presiona Enter para usar 21%): ")

# Verifica si se ingresó un valor para el IVA
porcentaje_iva = float(porcentaje_iva) if porcentaje_iva else 21

total_factura = calcular_total_factura(cantidad, porcentaje_iva)
print(f"El total de la factura con {porcentaje_iva}% de IVA es {total_factura}€")
