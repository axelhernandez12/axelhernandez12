#Importar la biblioteca datetime 
import datetime

ahora =datetime.datetime.now()
#Forma estandar de almacenar fechas
print(ahora.isoformat())
fecha_cadena_texto =ahora.strftime("%d/%m/%Y")
print(fecha_cadena_texto)
print(datetime.datetime.strptime(fecha_cadena_texto, "%d/%m/%Y"))


cosas = 2.5
nombre ="persona"
print(f"{cosas:^20.2f} | {nombre:>10}")
#^20 significa 20 espacios que dejamos en el medio 
#> 10 espacios hacia a la derecha 
#< 10 espacios a la izquierda  


#Ficheros



with open("ficherito","r") as fichero:
    linea = fichero.readline()
    while linea:
        print(linea)
        linea = fichero.readline()

        #Esto funciona para leer un csv entero con un bucle 



