#Muestra por pantalla la entrada por teclado hasta que se introduzca la palabra fin indiferentemente de mayusculas o miniculas (en las cadenas texto existen lower() y upper()"Ejemplo".upper() delvovera "EJEMPLO")

#palabra =""

#while palabra.upper() != "FIN":
 #   palabra = input()
  #  print(palabra)

#Crea un programa hasta que lea numeros hasta qye la suma de los numeros sea divisible enntre 5 o se introduzca el numero 42 en cada interaccion muestra la suma 

numero= 0
suma =0

while not(numero == 42 or suma % 5 != 0):
    
    numero = int(input("num"))
    print(f"{suma} + {numero} = {suma + numero}" )
    suma = suma + numero


#while True:
 #   numero = int(input("num"))
  #  suma = suma + numero
   # if numero == 42 or suma%5==0:
    #    break









