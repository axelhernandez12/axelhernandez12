numero = int(input("Introduzca un numero"))
resultado =0

while numero > 0:
    resultado += numero % 10
    numero = numero // 10
print(resultado)