#Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = int(input("Introduce un número entero: "))
print(f"El factorial de {numero} es {factorial(numero)}")
