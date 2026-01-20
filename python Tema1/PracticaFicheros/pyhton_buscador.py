import argparse
import os
from pathlib import pathlib 
import datetime


parser = argparse.ArgumentParser()
parser.add_argument("directorio",default=0) 


def validacion(directorio):
     if not (os.path.exists(directorio)): 
         raise argparse.ArgumentTypeError("El directorio no existe")
     return directorio
parser = argparse.ArgumentParser(description="Buscador de ficheros")
parser.add_argument(
     "directorio",
     nargs="?",
     default=".",
     type=validacion,
     help="Directorio donde realizar la búsqueda (por defecto el directorio actual)"
)

group_busqueda = parser.add_mutually_exclusive_group(required=True)

group_busqueda.add_argument("--tipo")
group_busqueda.add_argument("--nombre")
group_busqueda.add_argument("--contiene")
#Linea Verbose
parser.add_argument("--verbose","-v" ,action="store_true")



argr = parser.parse_args()


def escribir_log(ruta,mensaje):
     fecha = datetime.now().isoformat()
     with open("buscador.logs","a") as f:
          f.write(f"{fecha} - {ruta} - {mensaje}\n")


if argr.tipo:
     escribir_log(argr.directorio, f"comienza la busqueda de los ficheros {argr.tipo}")
elif argr.nombre:
     escribir_log(argr.directorio, f"comienza la busqueda del fichero {argr.nombre}")    
elif argr.contiene:
     escribir_log(argr.directorio, f"comienza la busqueda del texto {argr.contiene}")


def recorrer_directorio(ruta):
    for elemento in ruta.iterdir():

        # LOG SOLO SI -v
        if argr.verbose and elemento.is_dir():
            escribir_log(str(elemento), "se accede al directorio")

        if elemento.is_dir():
            recorrer_directorio(elemento)

        elif elemento.is_file():
            # búsqueda por extensión
            if argr.tipo and elemento.name.endswith(argr.tipo):
                resultados.append(str(elemento.resolve()))
                escribir_log(str(elemento), f"se ha encontrado {argr.tipo}")