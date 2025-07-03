#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

coste_barra_pan= 3.49

descuento=0.6

barras_vendidas= int(input("numero de barras vendidas que no son frescas?: "))

coste = barras_vendidas * coste_barra_pan * (1 - descuento)
print("El coste de una barra fresca es " + str(coste_barra_pan) + "$")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "$")
