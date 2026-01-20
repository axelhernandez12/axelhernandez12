import random

numero= random.randint(1,100)
numeroIntroducido=-1

while numero  !=numeroIntroducido :
    numeroIntroducido= int(input("Introducza otro numero"))
    if numeroIntroducido > numero:
        print(f"El {numeroIntroducido} que estas buscando es mayor al buscado")
    else:
        if numeroIntroducido< numero:
            print(f"El {numeroIntroducido} que estas buscando es menor")
        else:
            print( f"Has acertado , {numeroIntroducido}") 
    


