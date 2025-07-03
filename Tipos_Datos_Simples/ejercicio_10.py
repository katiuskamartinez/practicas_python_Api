#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

peso_payaso=112
peso_muneca=75

payasos_vendidos= int(input("Cuantos payasos fueron vendidos?: "))

Munecas_vendidas= int(input("cuantas munecas fueron vendidas?:"))

total_payasos= payasos_vendidos * peso_payaso
total_munecas= Munecas_vendidas * peso_muneca

Total_peso= (total_payasos + total_munecas) 
print((f" Total enviado: {Total_peso/1000} Kg"))