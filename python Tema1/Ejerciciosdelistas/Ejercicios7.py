import random
numeros_aleatorios =[]

for i in range(10):
    numeros_aleatorios.append(random.randint(1,100))
    numeros_aleatorios.sort(reverse=True)
print(numeros_aleatorios)
