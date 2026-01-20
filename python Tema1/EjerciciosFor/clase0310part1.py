# #Lea un numero y que dibuje un cudrado con *


# n= int(input("Introduzca un numero para crear el cuadrado"))

# for i in range(n):
#     for j in range(n):
#         print("*" ,end=" ") #Hace un salto de linea 
#     print() # Imprime las filas 



#Triangulo 
x =0
contador =0
k = int(input("Introduzca los valores que quieres de la piramide"))

for i in range(k):
    contador +=1
    for j in range(k):
        if x < contador: 
            print("*", end=" ")
        print(" ")

