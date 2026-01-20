pan =0.4
pan_duro = pan *0.5

numero_barras_vendidas = int(input("Introduzca el numero de barras del dia vendidas"))

numero_barras_vendidas_pan_duro= int(input("Introduzca el numero de barras de pan vendidas"))



print(f"Se ha vendido un total de barras {numero_barras_vendidas + numero_barras_vendidas_pan_duro}")
print(f"Y el total de los beficios ha sido de {numero_barras_vendidas * pan + numero_barras_vendidas_pan_duro * pan_duro}")





