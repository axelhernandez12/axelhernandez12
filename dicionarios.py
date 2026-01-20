# # p1 = {"nombre" : "Gustavo ", "Edad" : 32 }
# # print(p1)

# # print(p1["nombre"])


# #cuenta el numero de veces que aparece cada letra en la palabra patata

# diccionario={}

# cadena ="patata"
# for i in cadena:
#     if i in diccionario:
#         diccionario[i] = diccionario[i]+1
#     else:
#         diccionario[i] = 1
# print(diccionario)

# #crear diccinario sin valoores 
# diccionario={}

# #diccinario con valores
# diccionario={"x":1,"z":2}
# diccionario={"x"}=1
# diccionario ["z"]=2

#lea por teclado y que lo añada como  clave a un diccinario y despues pregunta otro valor y lo añadira como valor oara dicha clave 


# clave = input("Clave:")
# valor = input("Valor:")

# cosa = {clave : valor}

# print(cosa)


#Lea una frase por teclado y te cuente cuantas veces aparece cada vocal


# vocales={"a":0, "e":0,"i":0,"o":0,"u":0}

# palabra = input("Elige unna palabra")

# for i in palabra:
#     if i in vocales:
#         vocales[i] += 1
# print(vocales)



# Lea un numero por teclado y te (diga que numeros le componen :
#ejemplo leo el numero 12341


resultado={ 1:2,2:1,3:1,4:1}
numero = str(input("Introduzca un numero"))

for i in numero:
    if i in resultado:
        resultado[i] += 1
    else :
     resultado[i]=1
print(resultado)








