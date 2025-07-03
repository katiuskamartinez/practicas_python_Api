#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

interes= 0.04

inversion= float(input("Escribe el monto de inversion inicial: "))

balance_1= inversion * (1+interes)
print(f"despues de un año tienes $ {round(balance_1,2)}")

balance_2= balance_1 * (1+interes)
print(f"despues de dos años tienes $ {round(balance_2,2)}")

balance_3= balance_2 * (1+interes)
print(f"despues de tres años tienes $ {round(balance_3,2)}")