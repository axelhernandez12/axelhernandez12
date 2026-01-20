password = "contraseña"

Usuario = input("Introducza la contraseña")

if Usuario.lower() == password.lower():
    print("Coincide")
else:
    print("no coincide")