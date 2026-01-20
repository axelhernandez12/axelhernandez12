#Usa sorted con una lambda para ordenar la lista por la edad de menor a mayor.4

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Marta", "edad": 20}
]

orden_edad = sorted(personas ,key=lambda x :x[1]["edad"])
print(orden_edad)