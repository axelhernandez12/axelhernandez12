#lista conformada por tuplas de 3 elementos y queremos ordenarla por el resultado
#  de multiplicar el primer elemento por el segundo elmeneto y queremos que se ordene de mayor a menor

lista_tuplas = [
    (0,1,2),
    (-1,3,5),
    (-1,-2,5),
    (4,2,-5)
]

#Sorted te vuelve la lista ordenada
print(f" lista ordenada {sorted(lista_tuplas, key=lambda elemetos: elemetos[0] * elemetos[1],
reverse=True)}")
print(f"lista original{lista_tuplas}")



#filter
#Esto trozo de codigo hace lo mismo que el print filter
lista2 =[]
for tuplas in lista_tuplas:
    if tuplas[0] >= 0:
        lista2.append(tuplas)

print(lista2)
print(filter(lambda tupla:tupla[0] >= 0,lista_tuplas))
#lista(filter())


def factorial(n):
    if n == 1:
        return 1
    else :
        return n * factorial(n - 1)
print(factorial(5))

def factorial2(n):
    return factorial_aux(1,n)

def factorial_aux(valor_actual,valor_finla):
    if valor_actual == valor_finla:
        return valor_finla
    else:
        return valor_actual * factorial_aux(valor_actual + 1, valor_finla)

print(factorial2(5))
#Esto seria al contrario estamos llendo hacia abajo y estamos llendo hacia arriba


#Ejercicio 5 recursividad (no esta terminado )

def imprimir_num(n):
    if n ==1:
        print(1)
        return 1

    else:
        result = imprimir_num(result-1)
        print((result))
        print(result)
        return result
    
print(imprimir_num)