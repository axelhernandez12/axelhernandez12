# numero =int(input("Introduzca un numero"))
# resultado =0
# while numero > 0:
#     resultado += (numero %10) * 10 **(len(str(numero))-1)
#     numero = numero //10
# print(resultado)





n = int(input("> "))
if n >= 1:
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range(n-i,0,-1):
            print(j , end="")
        print()
else:
    print("NOPE")


C =0
T =0

while T <= 42:
    try :
        num = int(input("> "))
    except ValueError:
        num =0
    finally : 
        t+= num
        C+= 1
print(f"{C}para {t}")


