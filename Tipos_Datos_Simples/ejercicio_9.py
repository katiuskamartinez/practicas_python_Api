#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.


n=float(input("ingresa un numerador "))
m=float(input("ingresa el denominador "))

c=n/m
r=n%m
resultado=input(f"resultado de la division da cociente {c} y residuo {r}")