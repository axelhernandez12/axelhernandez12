#variable para salir del programa
finPrograma = "salir"

#variables
cadena = ""
contadorInt = 0
contadorFloat = 0
contadorString = 0
contadorBoolean = 0

#funcion para el identificador entero
def identificador(cadena):
    
    #CREACION DE VARIABLES
    letras = "abcdefghijklmnñopqrstuvwxzy"
    cont = 0
    contFloat = 0
   
    #Hacer que las variables de fuera funcionen dentro de la funcion (con global)
    global contadorInt, contadorFloat, contadorString, contadorBoolean, finPrograma
    
    #condicional para evitar problemas con la salida
    if cadena != finPrograma and cadena!= "salir":
        #para salir
        if cadena.lower() == "salir":
            return None
        
        #booleano - Ir de verificar datos completos a finalmente verificar parte por parte el valor/cadena
        for i in cadena:
            if cadena.lower() == "true" or cadena.lower() == "false":
                contadorBoolean+=1
                cadena = (bool(cadena))
                return "Booleano"   

             #Caso int
            try: 
                cadena = int(cadena)
                contadorInt+=1
                cadena = int(cadena)
                return "Int"
            except:
                    pass #para pasar al siguiente si no es un int

            #float
            if i == "." or i== ",":   
                contFloat +=1
                
                          
            #string
            else:
                for i in cadena:
                    for j in letras:
                        if i == j: #evitar problema con el "salir"
                            cont +=1
           
        #VERIFICACION DEL FLOAT                 
        #si tiene más de un punto (string)
        if contFloat > 1:
            contadorString += 1
            cadena = str(cadena)
            return "String"
        #si solo tiene un punto (float)
        elif contFloat == 1:
            contadorFloat += 1
            cadena = float(cadena)
            return "Float"
        #si no es ninguna de las anteriores (string por si acaso)
        else:
            contadorString += 1
            cadena = str(cadena)
            return "String"

                  
#INICIO PROGRAMA
while cadena != finPrograma.lower():
    cadena = input("Introduce valores por teclado. Escribe 'salir para terminar'")
    print(f"Entrada: {cadena}")
    
    #funcion identificador con el parametro
    tipo = identificador(cadena)
    
    print("Tipo detectado:",tipo)
    print("Valor convertido:", cadena)
    
    #SALIDA DEL PROGRAMA
    if cadena.lower() == finPrograma:
        print(f"Has ultilizado \n\t int:{contadorInt} \n\t float:{contadorFloat}\n\t bool:{contadorBoolean}\n\t String:{contadorString}\n\t")
    