#Crea una lista con 10 números aleatorios entre 1 y 100. Debes de mostrar por pantalla el mayor y el menor de dicha lista.
import random
numeros_aleatorios =[]

for i in range(10):
    if numeros_aleatorios.append(random.randint(1,100)):
        numeros_aleatorios.sort()

print(f"El mayor es {numeros_aleatorios[-1]}")
print(f"El menor es {numeros_aleatorios[0]}")
