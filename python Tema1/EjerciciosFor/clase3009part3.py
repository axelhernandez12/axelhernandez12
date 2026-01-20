numero = 1 
x =0

x = input("Introduzca un numero para saber su factorial")
for i in range(2, x+1):
    numero *=1
print(f"Factorial de {x} es {numero}")
