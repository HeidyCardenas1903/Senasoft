from Desytol import *

nombre_cliente = input("Ingrese el nombre del cliente, por favor: ")
tipo_cliente = int(input("Ingrese el tipo de cliente (1, 2, 3, 4): "))
cantidad_hojas = int(input("Ingrese la cantidad de hojas compradas:D : "))
precio_por_hoja = float(input("Ingrese el precio por el cual compro cada hoja: ")) 

calcular_total(nombre_cliente, tipo_cliente, cantidad_hojas, precio_por_hoja)

