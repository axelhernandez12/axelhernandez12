import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--base",required=True)
parser.add_argument("--altura",required=True)

arg = parser.parse_args()

base = float(arg.base)
altura = float(arg.altura)

area = (base * altura)/2

print(f"Area {area}")