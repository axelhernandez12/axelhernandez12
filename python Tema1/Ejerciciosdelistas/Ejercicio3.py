#Escribir un programa que pregunte una serie de 5 números, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor
num_lista=[]

for i in range(5):
    num = (input("introduzca un numero"))
    num_lista.append(num)
print(f"lista original{num_lista}")
num_lista.sort()
print(f"lista ordenada con sort{num_lista}")


