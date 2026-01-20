#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
# posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

abecedario=list("abcdfghijklmnñopqrstuvwxyz")
abecedarioFiltrado=[]

for i in range(len(abecedario)):
    if (i+1)%3!=0:
        abecedarioFiltrado.append(abecedario[i])
print(abecedarioFiltrado) 
    
