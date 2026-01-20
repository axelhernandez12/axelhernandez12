#Escribir un programa que pida por terminal una palabra y muestre por pantalla el número de veces que 
# contiene cada vocal

vocales=list("aeiou")
contador_valores=[0,0,0,0,0]
palabra  = input("introduzca la palabra")

for i in range(len(vocales)):
   contador_valores[i] = palabra.count(vocales[i])

for i in range(len(vocales)):
   print(f"hay {contador_valores[i]} vocales {vocales[i]}")
