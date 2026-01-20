# #Ejericiocio 1
# import argparse
# import datetime
# import os

# parser = argparse.ArgumentParser()

# parser.add_argument("--Inicio",required=True)
# parser.add_argument("--fin",required=True)

# args = parser.parse_args()


# inicio = args.inicio.split(":")
# fin = args.fin.split(":")

# inicio_min = int(inicio[0])*60 + int(inicio[1])
# fin_min = int(fin[0])*60 + int(fin[1])

# print(inicio_min - fin_min)



#Ejercicio 3 

# nombre = input("introduzca un nombre")

# n1 = float(input("nota 1"))
# n2 = float(input("nota 2"))
# n3 = float(input("nota 3"))

# media = n1 + n2+ n3 / 3

# estado ="APROBADO" if media >= 5  else "SUSPENSO"

# print(f'{"Alumno"} : {nombre}')
# print(f'{"media:"} : {media:.2f}')
# print(f'{"estado"} : {estado}')

# def mcd(a,b):
#     if b==0:
#         return a
#     else:
#         mcd(b,a%b)

# #Delvolvera 10 porque multiplica el numero que le sigues que es 5 , una lambda es una funcion de un solo y que no tiene nombre 

# #Ejercicio 6 

# def sumar(f,n):
#     total =0
#     for i in range(1,n+1):
#         total +=f(i)
#     return total


# #Ejercicio 2 
# import json
# salarios ={}
# contadores={}

# with open("fichero.csv","r") as f:
#     for linea in f:
#         nombre, dpto , salario = linea.split(";")
#         salario = float(salarios)

#         salarios[dpto] = salarios.get(dpto,0) + salario
#         contadores[dpto] = contadores.get(dpto,0) + 1
# medias = {}
# for dpto in salarios:
#     medias[dpto] = salarios[dpto]/contadores[dpto]

# with open("result.json", "w") as f:
#     json.dump(medias, f, indent=4)

#Ejercicios de chatgpt 







        



