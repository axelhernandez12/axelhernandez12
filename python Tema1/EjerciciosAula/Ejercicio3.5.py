salario_mensual = float (input("Salario del mes"))
Clientes_captados_este_mes = int (input("Introduzca la cantidad de clientes captados"))
rendimiento_mensaual=0
contador=0

if Clientes_captados_este_mes >= 20:
    contador = 0.25
elif Clientes_captados_este_mes >=10 :
    contador = 0.1
else:
    contador =0.0
rendimiento_mensaual = salario_mensual * (1 + contador)
print(f"Tu nuevo salario sera :{rendimiento_mensaual:.2f}")



