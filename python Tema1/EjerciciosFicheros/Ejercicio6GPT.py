import argparse
contador =0
suma =0

with open("EjercicioGPT6.csv","r")as f:
    
    for linea in f:
        producto , precio = linea.split(";")        
        precio = float(precio.strip())
        suma += precio
        contador += 1
    media = suma / contador

with open("EjercicioGPT6.csv","w") as f:
    f.write(f"Precio medio {media:.2f}")
    
