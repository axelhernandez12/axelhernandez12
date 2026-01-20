#Imprima los 50 primeros numeros divisibles entre 3

#con for e if 
#con while e if
contandor =0


for i in range(0,300):
    if (i %3)==0:
        contandor += 1
        print(i)
    
    if contandor ==50:
        break

#con for y range sin if imprimir los numeros divisibles entre 3 del 0 a 50    
for i in range(0 , 50 ,3):
    print(i)