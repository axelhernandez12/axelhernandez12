def es_palandrima(cadena):
    if len(cadena) < 2:
        return True
    if cadena[0] != cadena[-1]:
        return False
    return es_palandrima(cadena[1:-1]) 
print(es_palandrima("Axel"))