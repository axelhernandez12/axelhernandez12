# importaciones
import secrets

#variables y lista
listaPalabras = ["panes", "peces", "peras", "oreja", "peine", "happy", "amumu", "faker"]
intentos = 0
max_intentos = 5
letras = "abcdefghijklmnñopqrstuvwxyz"

secreta = secrets.choice(listaPalabras)
historialResultado = []

print("Adivina la palabra correcta")
print(f"La palabra tiene {len(secreta)} letras\n")

#bucle principal
while intentos < max_intentos:
    palabra = input(f"Llevas {intentos + 1}/{max_intentos} intentos: ").lower()

    #validar longitud
    if len(palabra) != 5:
        print("La palabra debe tener 5 letras\n")
        continue #hace que se ignore este intento y se empiece el bucle while de nuevo

    #validamos que solo tenga letras
    if not palabra.isalpha(): #isalpha devuelve true si es un string alfabetico (es decir que tiene letras), entonces aqui revisa si se trata de una palabra con letras y en caso de no ser asi, devuelve que no es palabra valida
        print("No es una palabra valida\n")
        continue #hace que se ignore este intento y se empiece el bucle while de nuevo

    #limpiamos/vaciamos el resultado de este intento
    resultado = ""

    #compaaramos letras
    for i in range(len(secreta)):
        if palabra[i] == secreta[i]:
            resultado += "🟩"
        elif palabra[i] in secreta:
            resultado += "🟨"
        else:
            resultado += "⬛"

    #gurardamos y mostramos el resultado
    historialResultado.append(resultado)
    print("Resultado:", resultado, "\n")

    #comprobacion de si se ha ganado
    if palabra == secreta:
        print("Has adivinado la palabra")
        break

    intentos += 1  #aumenta después del intento

#el resultado
if palabra != secreta:
    print(f"\nFin de los intentos. La palabra secreta era: {secreta}\n")

#resultado de los cuadraditos
print("Resultado de la partida:")
for r in historialResultado:
    print(r)
