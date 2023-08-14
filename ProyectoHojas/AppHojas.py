import tkinter as tk
from sqlite3 import connect

# Creacion de la base de datos / Hojas - Heidy
#Conexion :)
conexion = connect("ventas.db")
cursor = conexion.cursor()

#Tabla de ventas
cursor.execute('''
CREATE TABLE ventas (
  nombre text,
  tipo int,
  cantidad int,
  precio_por_hoja float,
  total float
)
''')

#Creacion de la funcion que se encargara de calcular el precio total y el recibo de una venta
def calcular_total(nombre, tipo_cliente, cantidad, precio_por_hoja):
    descuentos = {1: 0.05, 2: 0.08, 3: 0.12, 4: 0.15}
    
    if tipo_cliente in descuentos:
        descuento = descuentos[tipo_cliente]
    else:
        descuento = 0.0
    
    subtotal = cantidad * precio_por_hoja
    neto_por_pagar = subtotal * (1 - descuento)
    
    imprimir_recibo(nombre, subtotal, neto_por_pagar)

def print_receipt(name, subtotal, net_total):
  print("Name of the client:", name)
  print("Subtotal to pay:", subtotal)
  print("Net to pay:", net_total)

#App

