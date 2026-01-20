import argparse

def positivo(num):
    if int(num)> 0:
        return int(num)
    else:
        raise Exception("error")


parser = argparse.ArgumentParser()
parser.add_argument("Numero1",type=int)
parser.add_argument("--numero2",type=int,default=0)
parser.add_argument("-p ",action="store_true")
args = parser.parse_args()


print("el agurmento de numero1 es :" ,args.Numero1)
print("el agurmento de numero1 es :" ,args.numero2)
print(args.Numero1 + args.numero2)

