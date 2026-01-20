#lea un numero y te diga la longitud 

contador = 0
lectura= int(input("Introduzca un numero:"))
while lectura > 0:
    lectura = lectura // 10
    contador += 1
    
print(contador)