num1 =  int(input("Introduzca un numero"))
num2 = int(input("Introduzca otro numero"))

simbolo = input("Introduzca la operacion")

if simbolo =="+":
    print(f"La suma de {num1} {simbolo} {num2} = {num1+num2}")
else:
    if simbolo =="-":
        print(f"La resta de numero {num1} {simbolo} {num2} = {num1-num2}")
    else:
        if simbolo =="*":
         print(f"La resta de numero {num1} {simbolo} {num2} = {num1*num2}")
        else:
           if simbolo =="/":
            print(f"La resta de numero {num1} {simbolo} {num2} = {num1/num2}")
           else:
              print("El simbolo no es valido")


    
        




