def invertir_cadena(cadena):
    if cadena == "" or len(cadena)==1:
        return cadena
    else:
        return invertir_cadena(cadena[1:])+ cadena[0]
print(invertir_cadena("hola"))
