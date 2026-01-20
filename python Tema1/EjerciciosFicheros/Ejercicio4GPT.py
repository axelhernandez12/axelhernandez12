import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--texto")
parser.add_argument("--veces")

arg = parser.parse_args()

veces_contador = int(arg.veces)
texto_imprimir = (arg.texto)

for i in range(veces_contador):
    print(f"{texto_imprimir}")


