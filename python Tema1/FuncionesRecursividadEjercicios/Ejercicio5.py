#Crea una funcion imprimir numeros(n) que imprima los numeros entre 1 y  n. Por ejemplo: imprimir numeros(3) → 1 2 3 2 1.
def imprimir_numero(n):
    for i in range(1 ,n+1):
      print(i,end=" ")
        
    for i in range(n-1,0,-1):
        print(i,end=" ")
imprimir_numero(3)
        
        