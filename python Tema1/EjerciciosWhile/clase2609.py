#Muestre las taplas de multiplicar hasta que alguno de los resultados sea 26 (tabla de multiplicar 10)

resultado= 0


n1 =1 
n2=1
while resultado != 26:
    while n2 < 10 and resultado !=26:
        resultado = n1 *n2 
        print(f"{n1} * {n2} = {resultado}")
        n2 += 1
    n2 =1
    n1+=1


