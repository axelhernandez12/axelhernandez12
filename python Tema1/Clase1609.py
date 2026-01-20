#crear variables
texto ="Hola"
#Cambia el final del texto
print(texto,end="")

print("Nuevo texto")


#Ejemplo sin salto de linea 
print("hola",end="")
print("desde la misma linea")

print(1+1) #Suma
print(1-1) #Resta
print(1*1) #Mulplicacion
print(1/2) #Diviion
print(1//2) #Division con float
print(1%2) #Te devuele el resto( tambien llamado un modulo)
print(2**10) #Elevado a algo
edad = 25
nombre="Persona de la familia melano"
print("Hola",nombre)
print("Hola" +nombre)
print("Hola persona con" ,edad, "años")
#str se pone por el tipo de variable si pones mas + te da error hay que poner str con , si va 
print("Hola persona con"+ str(edad)+ "años")

#Lo que este entreCorchetes lo interpreta como codigo por ejemplo si pones una operacion te la va a calcular
print(f"hola persona con {edad} años")
#Esto son curiosidades
print(f"hola persona con {1/3:.2f} años")
print(f"hola persona con {round(1/3,2)} ")