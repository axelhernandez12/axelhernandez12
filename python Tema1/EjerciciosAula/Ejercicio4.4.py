numero =int(input("Introduzca un numero de la tabla de mulyplicar"))

for i in range(numero):
    for j in range(numero):
        print(f"{i} x {j}  = {i*j}")