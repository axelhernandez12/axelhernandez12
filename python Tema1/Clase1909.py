texto = "Hola mundo"
print (f"La variable testo contiene el contenido {texto} y es del tipo {type(texto)}") 
texto = 42

print({type(texto)})
print (f"La variable testo contiene el contenido {texto} y es del tipo {type(texto)}") 


texto : str = 42.0

print (f"La variable testo contiene el contenido {texto} y es del tipo {type(texto)}") 

#Lee lo que introduzcamos por el teclado input solo lee cadenas de texto
entrada : str = input("Introduce tu nombre")
print(entrada)

#La sentencia print(f "Texto") se usa para concatenar las variables  

calificacion : float = input(f"Introduce la nota de {entrada}: ")
print(f"la calificaion de {entrada} es {float (calificacion)*10}")

#En python no existe los parentesis ni las llaves lo hacemos de esta manera, con tabulaciones

if not (calificacion <0 or calificacion > 100):
    if calificacion >=50 and calificacion < 60 :
        print (f"{entrada}Esta aprobada")
    elif calificacion >=60 and calificacion < 70:
        print(f"{entrada}esta bien")
    elif calificacion >=70 and calificacion < 90:
        print (f"{entrada}esta notable")
    elif calificacion >=90 and calificacion <= 100:
        print(f"{entrada}esta sobresaliente") 
    else:
        print(f"{entrada} esta suspenso") 
else:
    print("no permitada la calificacion")

