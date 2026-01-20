import random
#Crea una lista con 10 números aleatorios entre 1 y 50 y cuenta el número de veces que aparecen números pares y el número de veces que aparecen números impares.

numeros_aleatorios=[]
contador_pares =0
contador_impres=0

for i in range(10):
    numeros_aleatorios.append(random.randint(1,50))

for numero in numeros_aleatorios:
    if numero % 2==0:
        contador_impres+=1
    else:
        contador_pares+=1
print(numeros_aleatorios)
print(f"Numeros pares {contador_pares} y numeros {contador_impres}")