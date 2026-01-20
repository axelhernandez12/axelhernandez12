#Dado dict1 = {"a": 1, "b": 2} y dict2 = {"b": 3, "c": 4}, únelos (las claves repetidas deben sumar sus valores).

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

for clave in dict1:
    if clave in dict2:
        dict2[clave] += dict1[clave]
    else:
        dict2[clave] = dict1[clave]
print(dict2)
