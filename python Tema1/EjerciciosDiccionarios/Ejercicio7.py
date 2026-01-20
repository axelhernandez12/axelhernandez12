#Dado un diccionario, intercambia sus claves y valores (asumiendo que los valores son únicos).

persona ={"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
intercambio={}

for clave in persona:
    intercambio[persona[clave]] = clave 

print(intercambio)
