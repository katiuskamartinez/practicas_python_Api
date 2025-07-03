#programa que pida al usuario su peso (en kg) y su estatura en (en metros), calcule el indice de masa corporal y lo almacene en una variable y muestre por pantalla la frase Tu indice de masa corporal es <imc> donde <imc> es el indice de masa corporal calculado redondeado con dos decimales.

peso= float(input("escriba su peso en kg ")) 

altura= float(input("escriba su estatura en metros ")) 

imc=peso/(altura**2)

print(f"Tu indice de masa corporal es {round(imc,2)}")