#Escribir un programa que lea por teclado una serie de valores hasta que se introduzca la palabra fin. Cada valor deberá ser introducido en una lista
lista=[]

valores = input("Introduzca una palabra")

while valores.lower() != "fin":
    lista.append(valores)
    valores = input("introduzca una palabra")

print(lista)