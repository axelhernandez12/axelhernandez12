import argparse

contador =0
with open("fichero.txt","r") as f:
    for linea in f:
        contador+=1
print(contador)
