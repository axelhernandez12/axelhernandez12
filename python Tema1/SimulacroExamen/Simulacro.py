# numero = int(input("> " ))
#Triangulo hacia a la derecha
# for i in range(numero):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(numero -i,0,-1):
#         print(j,end="")
#     print()
        

# numero =0
# try:
#     while numero < 1:
#         numero = int(input("Introduzca un numero"))
   
#         for i in range(numero):
#             for j  in range(numero -i):
#                 print(numero -i -j,end="")
 # except ValueError as e:
#    print("Valor no valido")

# numero =0
# try:
#     int(input("Introduzca un numero"))
    
#     for i in range(numero):
#       print(i+1)
# except ValueError as e :
#    print(f"no se pudo castear a entero el valor{numero}")

               
# numero =0
# contador =0

# while numero <= 42:
#     entrada = input("> ")
#     try:
#         valor = int(entrada)
#     except ValueError:
#         valor=0
#         numero+= valor
#         contador+=1
# print(f"Necesitaste {contador} numeros para alcanzar el numero {numero}")

# lista = [1,2,3,4,5]

# for i in range(len(lista)):
#     if i % 2 ==0:
#         print(lista[i])

# num = int(input("> "))
# #Bucle exterior controla las filas
# for i in range(1,num +1):
#     #Espacios a la izquierda(Paara empujar el triangulo a la derecha)
#     for j in range(num-i):
#         print(" ",end="")
#         #Numeros ascendentes 
#     for j in range(1,i+1):
#         print(j,end="")
#         #salto de linea
#     print()
  

# base_dict = {"m":1, "u":1, "r":1, "c":1, "i":1, "e":1, "l":1, "a":1, "g":1, "o":1}

# palabra = input("Introduzca la palabra")
# contador_usuario =0
# for palabra in contador_usuario:
#     if palabra in contador_usuario:
#         contador_usuario[palabra]+=1
#     else:
#         contador_usuario[palabra] =1
    
# for palabra in contador_usuario:




# num = int(input("> "))

# for i in range(num):
#     for j in range(i):
#         print("",end="")
#     for j in range(num -i ,0 ,-1):
#         print(j ,end="")
#     print()

 
num =0
contador=0
while num < 42:
    num = int(input("> ")) 
    try:
        valor = input(num)
    except ValueError:
        valor = 0
        num += 1
        contador +=1
print(f"Necesitaste {contador} numero para alcanzar el numero{num}")