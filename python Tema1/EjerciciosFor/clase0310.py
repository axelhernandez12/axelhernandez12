#lea 2 numeros por teclado y van a representar el inicio y el final 
# del bucle. Muestra todos los numeros que hay entre ellos , pero no estos.
#leo 1 
#leo 5
#leo 2 3 4


numero1 = int (input("Introduzca un numero"))
numero2 =  int (input("Introduzca otro numero"))

for i in range(numero1 +1,numero2):
 print(i)


